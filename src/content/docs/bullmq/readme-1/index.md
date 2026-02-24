---
title: '빠른 시작'
description: '{% hint style="info" %}'
---

Source URL: https://docs.bullmq.io/readme-1

# 빠른 시작

## 설치

npm을 사용해 설치:

```
$ npm install bullmq
```

yarn을 사용해 설치:

```
$ yarn add bullmq
```

{% hint style="info" %}
BullMQ는 TypeScript로 작성되었으며, 순수 JavaScript에서도 사용할 수 있지만 이 가이드의 모든 예제는 TypeScript로 작성됩니다.
{% endhint %}

프로젝트에 가져와 몇 가지 작업을 추가합니다:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('foo');

async function addJobs() {
  await myQueue.add('myJobName', { foo: 'bar' });
  await myQueue.add('myJobName', { qux: 'baz' });
}

await addJobs();
```

{% hint style="danger" %}
이 예제를 성공적으로 실행하려면 로컬 컴퓨터에서 Redis 서비스가 실행 중이어야 합니다. Redis 연결에 대한 자세한 내용은 [여기](https://docs.bullmq.io/guide/connections)에서 확인할 수 있습니다.
{% endhint %}

작업은 큐에 추가되며, 워커를 실행하는 Node.js 프로세스가 최소 하나 이상 있으면 언제든 처리할 수 있습니다:

```typescript
import { Worker } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis({ maxRetriesPerRequest: null });

const worker = new Worker(
  'foo',
  async job => {
    // Will print { foo: 'bar'} for the first job
    // and { qux: 'baz' } for the second.
    console.log(job.data);
  },
  { connection },
);
```

{% hint style="info" %}
원하는 만큼 워커 프로세스를 둘 수 있으며, BullMQ가 라운드 로빈 방식으로 작업을 워커들에 분배합니다.
{% endhint %}

워커에 리스너를 연결하면 완료된(또는 실패한) 작업을 수신할 수 있습니다:

```typescript
worker.on('completed', job => {
  console.log(`${job.id} has completed!`);
});

worker.on('failed', (job, err) => {
  console.log(`${job.id} has failed with ${err.message}`);
});
```

{% hint style="info" %}
사용 가능한 다른 이벤트도 많이 있습니다. 자세한 내용은 [Guide](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/events.md) 또는 [API reference](https://api.docs.bullmq.io/)를 확인하세요.
{% endhint %}

때로는 특정 위치에서 모든 워커 이벤트를 수신해야 할 때가 있으며, 이 경우 특수 클래스 [`QueueEvents`](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)를 사용해야 합니다:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents("my-queue-name");

queueEvents.on('waiting', ({ jobId }) => {
  console.log(`A job with ID ${jobId} is waiting`);
});

queueEvents.on('active', ({ jobId, prev }) => {
  console.log(`Job ${jobId} is now active; previous status was ${prev}`);
});

queueEvents.on('completed', ({ jobId, returnvalue }) => {
  console.log(`${jobId} has completed and returned ${returnvalue}`);
});

queueEvents.on('failed', ({ jobId, failedReason }) => {
  console.log(`${jobId} has failed with reason ${failedReason}`);
});
```

이벤트의 타임스탬프에도 접근할 수 있으며, 형태는 "1580456039332-0"와 같습니다.

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents("my-queue-name");

queueEvents.on('progress', ({ jobId, data }, timestamp) => {
  console.log(`${jobId} reported progress ${data} at ${timestamp}`);
});
```

{% hint style="danger" %}
성능상의 이유로 `QueueEvents` 인스턴스가 내보내는 이벤트에는 `Job` 인스턴스가 포함되지 않고 `jobId`만 포함됩니다. `Job` 인스턴스가 필요하면 [`Job.fromId`](https://api.docs.bullmq.io/classes/v5.Job.html#fromid) 메서드를 사용하세요.
{% endhint %}

