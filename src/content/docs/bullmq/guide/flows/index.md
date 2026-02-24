---
title: 'A FlowProducer constructor takes an optional "connection"'
description: 'BullMQ는 잡 간의 부모-자식 관계를 지원합니다. 기본 아이디어는 모든 자식 잡이 성공적으로 처리될 때까지 부모 잡이 wait 상태(즉, 워커가 가져갈 수 있는 상태)로 이동되지 않는다는 것입니다. 이를 제외하면 부모 잡이나 자식 잡은 일반 잡과 다르지 않습니다.'
---

Source URL: https://docs.bullmq.io/guide/flows

# 플로우

BullMQ는 잡 간의 부모-자식 관계를 지원합니다. 기본 아이디어는 모든 자식 잡이 성공적으로 처리될 때까지 부모 잡이 wait 상태(즉, 워커가 가져갈 수 있는 상태)로 이동되지 않는다는 것입니다. 이를 제외하면 부모 잡이나 자식 잡은 일반 잡과 다르지 않습니다.

이 기능을 통해 잡이 임의 깊이 트리의 노드가 되는 플로우를 만들 수 있습니다.

{% hint style="warning" %}
플로우는 `FlowProducer` 클래스를 사용해 큐에 추가됩니다.
{% endhint %}

"플로우"를 생성하려면 [`FlowProducer`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html) 클래스를 사용해야 합니다. [***`add`***](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add) 메서드는 다음 인터페이스를 따르는 객체를 받습니다.

```typescript
interface FlowJobBase<T> {
  name: string;
  queueName: string;
  data?: any;
  prefix?: string;
  opts?: Omit<T, 'debounce' | 'deduplication' | 'repeat'>;
  children?: FlowChildJob[];
}

type FlowChildJob = FlowJobBase<
  Omit<JobsOptions, 'debounce' | 'deduplication' | 'parent' | 'repeat'>
>;

type FlowJob = FlowJobBase<JobsOptions>;
```

따라서 다음과 같은 플로우를 추가할 수 있습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { FlowProducer } from 'bullmq';

// A FlowProducer constructor takes an optional "connection"
// object otherwise it connects to a local redis instance.
const flowProducer = new FlowProducer();

const flow = await flowProducer.add({
  name: 'renovate-interior',
  queueName: 'renovate',
  children: [
    { name: 'paint', data: { place: 'ceiling' }, queueName: 'steps' },
    { name: 'paint', data: { place: 'walls' }, queueName: 'steps' },
    { name: 'fix', data: { place: 'floor' }, queueName: 'steps' },
  ],
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import FlowProducer

# A FlowProducer constructor takes an optional "connection"
# object otherwise it connects to a local redis instance.
flowProducer = FlowProducer()

flow = await flowProducer.add({
  "name": "renovate-interior",
  "queueName": "renovate",
  "children": [
    { "name": "paint", "data": { "place": "ceiling" }, "queueName": "steps" },
    { "name": "paint", "data": { "place": "walls" }, "queueName": "steps" },
    { "name": "fix", "data": { "place": "floor" }, "queueName": "steps" },
  ],
})
```

{% endtab %}
{% endtabs %}

위 코드는 4개의 잡을 원자적으로 추가합니다. 하나는 "renovate" 큐에, 나머지 3개는 "steps" 큐에 추가됩니다. "steps" 큐의 3개 잡이 완료되면 "renovate" 큐의 부모 잡이 일반 잡처럼 처리됩니다.

위 호출은 큐에 추가된 모든 잡의 인스턴스를 반환합니다.

{% hint style="info" %}
부모 큐는 자식에 사용된 큐와 같을 필요가 없습니다.
{% endhint %}

{% hint style="warning" %}
`jobId` 옵션을 제공하는 경우 구분자로 간주되므로 콜론 **:** 이 포함되지 않도록 하세요.
{% endhint %}

부모 잡이 처리될 때 자식 잡이 생성한 결과에 접근할 수 있습니다. 예를 들어, 자식 잡에 대해 다음과 같은 워커가 있다고 가정해 보겠습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Worker } from 'bullmq';

const stepsWorker = new Worker('steps', async job => {
  await performStep(job.data);

  if (job.name === 'paint') {
    return 2500;
  } else if (job.name === 'fix') {
    return 1750;
  }
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

async def process(job: Job, token: str):
  await performStep(job.data)
  if job.name == 'paint':
    return 2500
  elif job.name == 'fix':
    return 1750

stepsWorker = Worker("steps", process, {"connection": connection})
```

{% endtab %}
{% endtabs %}

`getChildrenValues` 메서드를 사용하면 자식 잡들의 비용을 합산하는 부모 워커를 구현할 수 있습니다. 이 메서드는 *job key*를 키로, *해당 잡의 결과*를 값으로 갖는 객체를 반환합니다:

```typescript
import { Worker } from 'bullmq';

const renovateWorker = new Worker('renovate', async job => {
  const childrenValues = await job.getChildrenValues();

  const totalCosts = Object.values(childrenValues).reduce(
    (prev, cur) => prev + cur,
    0,
  );

  await sendInvoice(totalCosts);
});
```

필요에 따라 원하는 만큼 깊은 잡 계층을 추가할 수 있습니다. 다음 예시처럼 잡들이 서로 의존하도록 구성하면 잡을 직렬로 실행할 수 있습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { FlowProducer } from 'bullmq';
const flowProducer = new FlowProducer();

const queueName = 'assembly-line';
const chain = await flowProducer.add({
  name: 'car',
  data: { step: 'engine' },
  queueName,
  children: [
    {
      name: 'car',
      data: { step: 'wheels' },
      queueName,
      children: [{ name: 'car', data: { step: 'chassis' }, queueName }],
    },
  ],
});
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import FlowProducer

flowProducer = FlowProducer()

queueName = 'assembly-line'
chain = await flowProducer.add({
  "name": "car",
  "data": { "step": "engine" },
  "queueName": queueName,
  "children": [
    {
      "name": "car",
      "data": { "step": "wheels" },
      "queueName": queueName,
      "children": [{ "name": "car", "data": { "step": "chassis" }, "queueName": queueName }],
    },
  ],
})
```

{% endtab %}
{% endtabs %}

이 경우 이전 잡이 완료된 뒤 다음 잡이 처리됩니다.

{% hint style="info" %}
처리 순서는 `chassis`, `wheels`, 마지막으로 `engine` 입니다.
{% endhint %}

## 게터

플로우와 관련된 잡을 가져오기 위해 사용할 수 있는 몇 가지 특별한 게터가 있습니다. 먼저, `Job` 클래스에는 특정 잡의 모든 의존성을 가져오는 메서드가 있습니다:

```typescript
const dependencies = await job.getDependencies();
```

이 메서드는 모든 **직접** **의존성**(즉, 해당 잡의 자식들)을 반환합니다.

또는 특정 타입의 자식만 가져오고 싶다면:

```typescript
// cursors are used in pagination
const { processed, nextProcessedCursor } = await job.getDependencies({
  processed: {
    count: 5,
    cursor: 0,
  },
});

const { unprocessed, nextUnprocessedCursor } = await job.getDependencies({
  unprocessed: {
    count: 5,
    cursor: 0,
  },
});

const { failed, nextFailedCursor } = await job.getDependencies({
  failed: {
    count: 5,
    cursor: 0,
  },
});

const { ignored, nextIgnoredCursor } = await job.getDependencies({
  ignored: {
    count: 5,
    cursor: 0,
  },
});
```

`Job` 클래스는 위에서 소개한 다른 메서드들도 제공합니다.

## 의존성 개수 가져오기

타입별 자식의 개수를 모두 가져오려면:

```typescript
const { failed, ignored, processed, unprocessed } =
  await job.getDependenciesCount();
```

또는 특정해서 가져오고 싶다면:

```typescript
const { failed } = await job.getDependenciesCount({
  failed: true,
});

const { ignored, processed } = await job.getDependenciesCount({
  ignored: true,
  processed: true,
});

const { unprocessed } = await job.getDependenciesCount({
  unprocessed: true,
});
```

## 자식 값 가져오기

특정 잡의 자식들이 생성한 모든 값을 가져오려면:

```typescript
const values = await job.getChildrenValues();
```

또한 `Job` 클래스에 새 속성 ***`parentKey`,*** 가 추가되었으며, 이는 해당 잡 부모의 fully qualified key를 제공합니다.

마지막으로, 자식이 아직 완료되지 않은 부모 잡을 위한 새 상태 "waiting-children" 도 추가되었습니다:

```typescript
const state = await job.getState();
// state will be "waiting-children"
```

## 옵션 제공

플로우를 추가할 때 추가 객체인 **`queueOptions`** 객체를 함께 제공할 수도 있습니다. 이 객체에는 플로우에서 사용되는 각 큐에 대한 옵션을 설정할 수 있습니다. 이 옵션들은 `FlowProducer` 를 통해 플로우에 추가되는 각 잡에 영향을 줍니다.

```typescript
import { FlowProducer } from 'bullmq';
const flowProducer = new FlowProducer();

const queueName = 'assembly-line';
const chain = await flowProducer.add(
  {
    name: 'car',
    data: { step: 'engine' },
    queueName,
    children: [
      {
        name: 'car',
        data: { step: 'wheels' },
        queueName,
      },
    ],
  },
  {
    queuesOptions: {
      [queueName]: {
        defaultJobOptions: {
          removeOnComplete: true,
        },
      },
    },
  },
);
```

{% hint style="warning" %}
큐 옵션은 각 인스턴스의 컨텍스트에서 정의됩니다. 예상치 못한 동작을 피하려면 두 번째 파라미터에서 설정을 제공해야 합니다.
{% endhint %}

## 잡 제거

BullMQ는 플로우에 포함된 잡에 대해 매끄러운 제거 기능도 제공합니다.

플로우의 일부인 잡을 제거할 때는 다음의 중요한 사항들을 고려해야 합니다:

1. 부모 잡을 제거하면 모든 자식도 함께 제거됩니다.
2. 자식 잡을 제거하면 해당 자식에 대한 부모의 의존성도 제거되며, 그 자식이 의존성 목록의 마지막 자식이었다면 부모 잡은 완료됩니다.
3. 큰 플로우에서 하나의 잡이 부모이면서 자식일 수 있으므로, 이런 잡을 제거하면 1과 2가 모두 발생합니다.
4. 제거 대상 잡 중 하나라도 lock 상태라면 어떤 잡도 제거되지 않으며 예외가 발생합니다.

위 고려사항 외에는 `Job` 또는 `Queue` 클래스를 사용해 간단히 잡을 제거할 수 있습니다:

```typescript
await job.remove();
// or
await queue.remove(job.id);
```

## 더 읽어보기:

* 📋 [플로우를 사용해 큰 잡 분할하기](https://blog.taskforce.sh/splitting-heavy-jobs-using-bullmq-flows/)
* 💡 [FlowProducer API 레퍼런스](https://api.docs.bullmq.io/classes/v5.FlowProducer.html)
* 💡 [Job API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html)
* 💡 [Get Children Values API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#getchildrenvalues)
* 💡 [Get Dependencies API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#getdependencies)
* 💡 [Get Dependencies Count API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#getdependenciescount)

