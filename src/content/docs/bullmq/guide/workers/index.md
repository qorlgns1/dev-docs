---
title: 'Workers'
description: '원본 URL: https://docs.bullmq.io/guide/workers'
---

원본 URL: https://docs.bullmq.io/guide/workers

# Workers

워커는 큐에 추가된 작업을 기반으로 실제 작업을 수행하는 인스턴스입니다. 워커는 전통적인 메시지 큐에서 "message" 수신자와 동일합니다. 워커의 역할은 작업을 완료하는 것입니다. 성공하면 작업은 `"completed"` 상태로 이동합니다. 워커가 처리 중 예외를 발생시키면 작업은 자동으로 `"failed"` 상태로 이동합니다.

{% hint style="info" %}
실패한 작업은 자동으로 재시도할 수 있습니다. [Retrying failing jobs](https://docs.bullmq.io/guide/retrying-failing-jobs)를 참고하세요.
{% endhint %}

워커는 `Worker` 클래스로 인스턴스화되며, 실제 작업은 *process function* 에서 수행됩니다. 프로세스 함수는 `async` 키워드를 사용하거나 promise를 반환하는 비동기 함수여야 합니다.

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(queueName, async (job: Job) => {
  // Optionally report some progress
  await job.updateProgress(42);

  // Optionally sending an object as progress
  await job.updateProgress({ foo: 'bar' });

  // Do something with job
  return 'some value';
});
```

프로세서 함수는 작업 취소를 지원하기 위해 선택적인 세 번째 파라미터를 받을 수도 있습니다:

```typescript
const worker = new Worker(
  queueName,
  async (job: Job, token?: string, signal?: AbortSignal) => {
    // signal can be used to detect when a job has been cancelled
    return 'some value';
  },
);
```

{% hint style="info" %}
자세한 내용은 전용 가이드 [cancelling jobs](https://docs.bullmq.io/guide/workers/cancelling-jobs)를 참고하세요.
{% endhint %}

{% hint style="info" %}
워커 인스턴스가 생성되면 프로세서는 즉시 시작됩니다.
{% endhint %}

프로세서 실행 시작 시점을 직접 결정하려면 워커 옵션의 일부로 `autorun: false`를 전달하세요:

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(
  queueName,
  async (job: Job) => {
    // Optionally report some progress
    await job.updateProgress(42);

    // Optionally sending an object as progress
    await job.updateProgress({ foo: 'bar' });

    // Do something with job
    return 'some value';
  },
  { autorun: false },
);

worker.run();
```

프로세서는 선택적으로 값을 반환할 수 있습니다. 이 값은 작업을 가져와 `returnvalue` 속성에 접근하거나 `completed` 이벤트를 수신하여 가져올 수 있습니다:

```typescript
worker.on('completed', (job: Job, returnvalue: any) => {
  // Do something with the return value.
});
```

#### Progress

워커 프로세스 함수 내부에서는 진행률 이벤트를 발생시킬 수도 있습니다. `job.progress`를 호출하면 숫자를 지정할 수 있고, 더 복잡한 요구사항이 있다면 객체를 지정할 수도 있습니다. `progress` 이벤트는 `completed` 이벤트와 같은 방식으로 수신할 수 있습니다:

```typescript
worker.on('progress', (job: Job, progress: number | object) => {
  // Do something with the return value.
});
```

마지막으로, 프로세스가 예외로 실패할 때 `failed` 이벤트도 수신할 수 있습니다:

```typescript
worker.on('failed', (job: Job | undefined, error: Error, prev: string) => {
  // Do something with the return value.
});
```

작업 완료, 진행률, 실패 알림을 받기 위해 전역 이벤트를 수신하는 것도 가능합니다:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('Paint');

queueEvents.on('completed', ({ jobId, returnvalue }) => {
  // Called every time a job is completed by any worker.
});

queueEvents.on('failed', ({ jobId, failedReason }) => {
  // Called whenever a job is moved to failed by any worker.
});

queueEvents.on('progress', ({ jobId, data }) => {
  // jobId received a progress event
});
```

마지막으로, 에러 발생 시 NodeJS가 처리되지 않은 예외를 발생시키지 않도록 워커에 에러 리스너를 연결해야 합니다. 예를 들어:

```typescript
worker.on('error', err => {
  // log the error
  console.error(err);
});
```

{% hint style="danger" %}
에러 핸들러가 없으면 에러가 발생했을 때 워커가 작업 처리를 중단할 수 있습니다! 자세한 정보는 [here](https://nodejs.org/api/events.html#events_error_events)를 참고하세요.
{% endhint %}

## Typescript typings

제네릭을 사용하여 Job 데이터와 반환값의 데이터 타입을 지정할 수도 있습니다:

```typescript
const worker = new Worker<MyData, MyReturn>(queueName, async (job: Job) => {});
```

## 더 읽어보기:

* 💡 [Worker API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Worker.html)
* 💡 [Queue Events API 레퍼런스](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)

