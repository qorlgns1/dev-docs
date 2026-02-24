---
title: '단계별 작업 처리'
description: '때로는 processor 함수를, 이전에 실행된 단계에 따라 처리되는 작은 조각으로 나누는 것이 유용합니다. 이런 종류의 로직을 처리하는 한 가지 방법은 switch 문을 사용하는 것입니다.'
---

Source URL: https://docs.bullmq.io/patterns/process-step-jobs

# 단계별 작업 처리

때로는 processor 함수를, 이전에 실행된 단계에 따라 처리되는 작은 조각으로 나누는 것이 유용합니다. 이런 종류의 로직을 처리하는 한 가지 방법은 switch 문을 사용하는 것입니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
enum Step {
  Initial,
  Second,
  Finish,
}

const worker = new Worker(
  'queueName',
  async job => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Finish,
          });
          step = Step.Finish;
          return Step.Finish;
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% endtab %}

{% tab title="Python" %}

```python
class Step(int, Enum):
  Initial = 1
  Second = 2
  Finish = 3

async def process(job: Job, token: str):
  step = job.data.get("step")
  while step != Step.Finish:
    if step == Step.Initial:
      await doInitialStepStuff()
      await job.updateData({
          "step": Step.Second
      })
      step = Step.Second
    elif step == Step.Second:
      await doSecondStepStuff()
      await job.updateData({
          "step": Step.Finish
      })
      step = Step.Finish
    else:
      raise Exception("invalid step")

worker = Worker("queueName", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

이전 단계를 완료할 때마다 다음 단계 값을 저장하면(여기서는 job의 data에 저장), job에서 오류가 발생해 재시도되더라도 올바른 단계부터 시작하도록 보장할 수 있습니다.

## 지연(Delaying)

처리 중인 job을 지연시키는 것이 유용한 상황이 있습니다.

이것은 `moveToDelayed` 메서드로 처리할 수 있습니다. 다만, job이 worker에 의해 처리되는 동안 worker는 특정 token 값으로 해당 job의 lock을 유지한다는 점이 중요합니다. `moveToDelayed` 메서드가 동작하려면, 오류 없이 unlock할 수 있도록 해당 token을 전달해야 합니다. 마지막으로, processor에서 특수 에러(`DelayedError`)를 throw하여 종료해야 하며, 이를 통해 worker는 job이 지연되었음을 인지하고 job을 완료(또는 실패 처리)하려고 시도하지 않게 됩니다.

```typescript
import { DelayedError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Finish,
}

const worker = new Worker(
  'queueName',
  async (job: Job, token?: string) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await job.moveToDelayed(Date.now() + 200, token);
          await job.updateData({
            step: Step.Second,
          });
          throw new DelayedError();
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Finish,
          });
          step = Step.Finish;
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

## 자식 작업 대기(Waiting Children)

일반적인 사용 사례 중 하나는 런타임에 자식 작업을 추가한 다음, 자식 작업이 완료될 때까지 기다리는 것입니다.

이것은 `moveToWaitingChildren` 메서드로 처리할 수 있습니다. 다만, job이 worker에 의해 처리되는 동안 worker는 특정 token 값으로 해당 job의 lock을 유지한다는 점이 중요합니다. `moveToWaitingChildren` 메서드가 동작하려면, 오류 없이 unlock할 수 있도록 해당 token을 전달해야 합니다. 마지막으로, processor에서 특수 에러(`WaitingChildrenError`)를 throw하여 종료해야 하며, 이를 통해 worker는 job이 *waiting-children* 상태로 이동했음을 인지하고 job을 완료(또는 실패 처리)하려고 시도하지 않게 됩니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { WaitingChildrenError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Third,
  Finish,
}

const worker = new Worker(
  'parentQueueName',
  async (job: Job, token?: string) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await childrenQueue.add(
            'child-1',
            { foo: 'bar' },
            {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          );
          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await childrenQueue.add(
            'child-2',
            { foo: 'bar' },
            {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          );
          await job.updateData({
            step: Step.Third,
          });
          step = Step.Third;
          break;
        }
        case Step.Third: {
          const shouldWait = await job.moveToWaitingChildren(token);
          if (!shouldWait) {
            await job.updateData({
              step: Step.Finish,
            });
            step = Step.Finish;
            return Step.Finish;
          } else {
            throw new WaitingChildrenError();
          }
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker, WaitingChildrenError
from enum import Enum

class Step(int, Enum):
  Initial = 1
  Second = 2
  Third = 3
  Finish = 4

async def process(job: Job, token: str):
  step = job.data.get("step")
  while step != Step.Finish:
    if step == Step.Initial:
      await doInitialStepStuff()
      await children_queue.add('child-1', {"foo": "bar" },{
        "parent": {
            "id": job.id,
            "queue": job.queueQualifiedName
        }
      })
      await job.updateData({
          "step": Step.Second
      })
      step = Step.Second
    elif step == Step.Second:
      await doSecondStepStuff()
      await children_queue.add('child-2', {"foo": "bar" },{
        "parent": {
          "id": job.id,
          "queue": job.queueQualifiedName
        }
      })
      await job.updateData({
          "step": Step.Third
      })
      step = Step.Third
    elif step == Step.Third:
      should_wait = await job.moveToWaitingChildren(token, {})
      if not should_wait:
        await job.updateData({
            "step": Step.Finish
        })
        step = Step.Finish
        return Step.Finish
      else:
        raise WaitingChildrenError
    else:
      raise Exception("invalid step")

worker = Worker("parentQueueName", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
Bullmq-Pro: 이 패턴은 observables를 사용해 처리할 수 있으며, 이 경우 다음 단계를 저장할 필요가 없습니다.
{% endhint %}

## 플로우 체이닝(Chaining Flows)

또 다른 사용 사례는 런타임에 플로우를 추가한 다음, 자식 작업이 완료될 때까지 기다리는 것입니다.

예를 들어, worker의 processor 함수에서 자식 작업을 동적으로 추가할 수 있습니다.

```typescript
import { FlowProducer, WaitingChildrenError, Worker } from 'bullmq';

enum Step {
  Initial,
  Second,
  Third,
  Finish,
}

const flow = new FlowProducer({ connection });
const worker = new Worker(
  'parentQueueName',
  async (job, token) => {
    let step = job.data.step;
    while (step !== Step.Finish) {
      switch (step) {
        case Step.Initial: {
          await doInitialStepStuff();
          await flow.add({
            name: 'child-job',
            queueName: 'childrenQueueName',
            data: {},
            children: [
              {
                name,
                data: { idx: 0, foo: 'bar' },
                queueName: 'grandchildrenQueueName',
              },
              {
                name,
                data: { idx: 1, foo: 'baz' },
                queueName: 'grandchildrenQueueName',
              },
            ],
            opts: {
              parent: {
                id: job.id,
                queue: job.queueQualifiedName,
              },
            },
          });

          await job.updateData({
            step: Step.Second,
          });
          step = Step.Second;
          break;
        }
        case Step.Second: {
          await doSecondStepStuff();
          await job.updateData({
            step: Step.Third,
          });
          step = Step.Third;
          break;
        }
        case Step.Third: {
          const shouldWait = await job.moveToWaitingChildren(token);
          if (!shouldWait) {
            await job.updateData({
              step: Step.Finish,
            });
            step = Step.Finish;
            return Step.Finish;
          } else {
            throw new WaitingChildrenError();
          }
        }
        default: {
          throw new Error('invalid step');
        }
      }
    }
  },
  { connection },
);
```

{% hint style="info" %}
특수 에러를 사용해 job을 수동으로 이동하면 **attemptsMade** 속성은 증가하지 않습니다. 이 속성은 일반적인 job 완료 또는 실패 시 증가합니다(여기에는 backoff 전략을 사용한 재시도도 포함됩니다). **DelayedError**, **RateLimitError**, **WaitingChildrenError**, **WaitingError** 같은 특수 에러를 사용할 때, 시도 횟수 증가 없이 job이 건너뛸 수 있는 횟수를 제어할 수 있습니다. job이 처리 시작을 허용받는 횟수를 제어하려면 **maxStartedAttempts** 옵션을 사용하세요.
{% endhint %}

## 더 읽어보기:

* 💡 [Move To Delayed API 참조](https://api.docs.bullmq.io/classes/v5.Job.html#movetodelayed)
* 💡 [Move To Waiting Children API 참조](https://api.docs.bullmq.io/classes/v5.Job.html#movetowaitingchildren)

