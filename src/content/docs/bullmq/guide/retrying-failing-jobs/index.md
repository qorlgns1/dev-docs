---
title: '실패한 작업 재시도'
description: '큐가 작업을 처리하는 동안, 시간이 지나면서 일부 작업이 실패하는 것은 불가피합니다. BullMQ에서 작업은 다음과 같은 경우 실패한 것으로 간주됩니다:'
---

원문 URL: https://docs.bullmq.io/guide/retrying-failing-jobs

# 실패한 작업 재시도

큐가 작업을 처리하는 동안, 시간이 지나면서 일부 작업이 실패하는 것은 불가피합니다. BullMQ에서 작업은 다음과 같은 경우 실패한 것으로 간주됩니다:

* [`Worker`](https://docs.bullmq.io/guide/workers)에 정의된 프로세서 함수가 예외를 던진 경우.
* 작업이 [*stalled*](https://docs.bullmq.io/guide/jobs/stalled) 상태가 되었고 "max stalled count" 설정을 소진한 경우.

{% hint style="danger" %}
BullMQ가 올바르게 동작하려면, 프로세서에서 던지는 예외는 반드시 [`Error`](https://nodejs.org/api/errors.html#class-error) 객체여야 합니다.

일반적으로 모범 사례는 항상 `Error` 객체를 던지는 것입니다. 이를 강제하고 싶다면 [ESLint rule](https://eslint.org/docs/latest/rules/no-throw-literal)도 사용할 수 있습니다.
{% endhint %}

## 실패한 작업 재시도

프로세서가 예외를 던지면 워커가 이를 잡아 작업을 failed 세트로 이동시킵니다. [Queue settings](https://docs.bullmq.io/guide/queues/auto-removal-of-jobs)에 따라 작업은 failed 세트에 영구히 남을 수도 있고, 자동으로 제거될 수도 있습니다.

많은 경우, 일정 횟수의 재시도마저 실패하기 전까지는 포기하지 않도록 실패한 작업을 자동으로 재시도하는 것이 바람직합니다. 자동 재시도를 활성화하려면 [`attempts`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#attempts) 설정을 1보다 큰 값으로 지정해야 합니다(아래 예시 참고).

BullMQ는 back-off 함수를 사용해 실패한 작업 재시도를 지원합니다. **내장** backoff 함수를 사용할 수도 있고, **커스텀** 함수를 제공할 수도 있습니다. back-off 함수를 지정하지 않으면 작업은 실패 즉시 지연 없이 재시도됩니다.

{% hint style="info" %}
재시도된 작업은 waiting 상태로 다시 이동될 때 우선순위를 유지합니다.
{% endhint %}

### 내장 backoff 전략

현재 내장 backoff 함수는 **fixed**와 **exponential**입니다.

#### Fixed

fixed backoff를 사용하면 `delay` 밀리초 후에 재시도합니다. 따라서 지연이 3000밀리초라면, 이전 시도 후 3000밀리초마다 *매* 시도를 재시도합니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'fixed',
      delay: 1000,
    },
  },
);
```

[jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) 옵션도 제공할 수 있으며, jitter 사용 비율에 따라 `delay`와 0밀리초 사이의 임의 지연이 생성됩니다. 예를 들어 jitter 값을 0.5로, delay를 1000밀리초로 지정하면 `1000` 밀리초 = 1초와 `1000 * 0.5` 밀리초 = 500ms 사이의 지연이 생성됩니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 8,
    backoff: {
      type: 'fixed',
      delay: 1000,
      jitter: 0.5,
    },
  },
);
```

#### Exponential

exponential backoff를 사용하면 `2 ^ (attempts - 1) * delay` 밀리초 후에 재시도합니다. 예를 들어 지연이 3000밀리초일 때 7번째 시도는 이전 시도 후 `2^6 * 3000` 밀리초 = 3.2분 뒤에 재시도됩니다.

아래 코드는 시드 값으로 1초 지연을 갖는 내장 "exponential" backoff 함수를 지정하는 방법을 보여줍니다. 이렇게 하면 최대 2번 재시도하므로(첫 시도 이후, 총 3번 시도) 각각 1초, 2초, 4초 간격으로 재시도됩니다:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 1000,
    },
  },
);
```

[jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) 옵션도 제공할 수 있으며, jitter 사용 비율에 따라 `2 ^ (attempts - 1) * delay`와 0밀리초 사이의 임의 지연이 생성됩니다. 예를 들어 jitter 값을 0.5로, delay를 3000밀리초로 지정하면 7번째 시도에서 이전 시도 후 `2^6 * 3000` 밀리초 = 192000ms와 `2^6 * 3000 * 0.5` 밀리초 = 96000ms 사이의 지연이 생성됩니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 8,
    backoff: {
      type: 'exponential',
      delay: 3000,
      jitter: 0.5,
    },
  },
);
```

큐의 `defaultJobOptions`에 back-off 전략을 정의할 수도 있으며, 작업 추가 시 재정의하지 않는 한 큐에 추가되는 모든 작업에 적용됩니다. 예를 들어:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo', {
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 1000,
    },
  },
});

await queue.add('test-retry', { foo: 'bar' });
```

{% hint style="info" %}
jitter 비율 옵션 값은 0과 1 사이여야 합니다. 0은 랜덤성이 적용되지 않음을 의미하며(기본 동작), 1은 내장 전략 중 어떤 전략이든 생성 가능한 최대 값과 0 사이에서 임의 지연이 생성됨을 의미합니다.
{% endhint %}

### 커스텀 back-off 전략

커스텀 backoff 함수를 정의하려면 워커 설정에서 정의해야 합니다:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('foo', async job => doSomeProcessing(), {
  settings: {
    backoffStrategy: (attemptsMade: number) => {
      return attemptsMade * 1000;
    },
  },
});
```

{% hint style="info" %}
`backoffStrategy`가 0을 반환하면 작업은 waiting 리스트의 끝(priority 0)으로 이동하거나 prioritized 상태(priority > 0)로 다시 이동합니다.

`backoffStrategy`가 -1을 반환하면 작업은 재시도되지 않고 failed 상태로 이동합니다.
{% endhint %}

그다음 작업을 추가할 때 커스텀 전략을 사용할 수 있습니다:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: {
      type: 'custom',
    },
  },
);
```

여러 개의 커스텀 backoff 타입을 정의하려면 다음 예시처럼 정의해야 합니다:

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('foo', async job => doSomeProcessing(), {
  settings: {
    backoffStrategy: (
      attemptsMade: number,
      type: string,
      err: Error,
      job: Job,
    ) => {
      switch (type) {
        case 'custom1': {
          return attemptsMade * 1000;
        }
        case 'custom2': {
          return attemptsMade * 2000;
        }
        default: {
          throw new Error('invalid type');
        }
      }
    },
  },
});
```

## 더 읽어보기:

* 💡 [Stop Retrying Jobs](https://docs.bullmq.io/patterns/stop-retrying-jobs)

