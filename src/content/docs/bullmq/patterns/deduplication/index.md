---
title: '중복 제거'
description: '때로는 작업 중복 제거를 언제 중단할지 결정하고 싶을 수 있습니다.'
---

원문 URL: https://docs.bullmq.io/patterns/deduplication

# 중복 제거

때로는 작업 중복 제거를 언제 중단할지 결정하고 싶을 수 있습니다.

## 작업이 active 상태가 될 때까지

작업이 active 상태로 이동하는 즉시, **removeDeduplicationKey** 메서드를 호출해야 합니다:

```typescript
import { Job, Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async (job: Job) => {
  await job.removeDeduplicationKey();
  console.log('Do something with job');
  return 'some value';
});

myQueue.add('house', { color: 'white' }, { deduplication: { id: 'house' } });
```

{% hint style="info" %}
이전 예제는 [Simple Mode](https://docs.bullmq.io/guide/jobs/deduplication#simple-mode)를 사용하지만, [Throttle Mode](https://docs.bullmq.io/guide/jobs/deduplication#throttle-mode) 또는 [Debounce Mode](https://docs.bullmq.io/guide/jobs/deduplication#debounce-mode)와 함께 조합할 수도 있습니다.
{% endhint %}

## job scheduler 사용하기

때로는 리소스를 절약하고 불필요한 작업을 피하기 위해 job scheduler가 생성한 작업을 중복 제거하고 싶을 수 있습니다:

중복 제거 옵션은 scheduler 템플릿에서 작업 생성에 간섭할 수 있으므로 [`JobSchedulerTemplateOptions`](https://api.docs.bullmq.io/types/v5.JobSchedulerTemplateOptions.html)에서 사용할 수 없습니다. 이전 작업이 active 상태로 이동하자마자 새 작업이 추가되기 때문에, 중복 제거는 이 새 레코드 추가를 막아 이 과정을 방해할 수 있습니다. 하지만 이를 처리할 대안이 있습니다. 예제를 살펴보겠습니다:

```typescript
import { Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker(
  'Paint',
  async job => {
    if (job.name === 'paint-trigger') {
      // Add a job that will be deduplicated for 90 seconds.
      await myQueue.add(
        'house',
        { color: 'white' },
        { deduplication: { id: 'customValue', ttl: 90000 } },
      );
    }
  },
  { connection },
);

await myQueue.upsertJobScheduler('repeat', {
  pattern: '* * * * *', // every minute
  template: {
    name: 'paint-trigger',
    data: {},
  },
});
```

이 방식으로 job scheduler를 사용할 때 작업을 중복 제거할 수 있습니다.

## 더 읽어보기:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)
* 💡 [Deduplication Reference](https://docs.bullmq.io/guide/jobs/deduplication)
* 💡 [Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#removededuplicationkey)
* 💡 [Upsert Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#upsertJobScheduler)

