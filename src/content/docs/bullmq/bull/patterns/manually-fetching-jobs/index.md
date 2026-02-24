---
title: '작업 수동으로 가져오기'
description: '자동 프로세서에 맡기지 않고 큐에서 작업을 수동으로 가져오고 싶다면, 이 패턴이 적합합니다.'
---

Source URL: https://docs.bullmq.io/bull/patterns/manually-fetching-jobs

# 작업 수동으로 가져오기

자동 프로세서에 맡기지 않고 큐에서 작업을 수동으로 가져오고 싶다면, 이 패턴이 적합합니다.

몇 가지 간단한 메서드로 작업 상태를 수동 전환할 수 있습니다.

1. 작업을 `'waiting'` 큐에 추가합니다. 큐를 가져와 `add`를 호출합니다.

```typescript
import Queue from 'bull';

const queue = new Queue({
  limiter: {
    max: 5,
    duration: 5000,
    bounceBack: true // important
  },
  ...queueOptions
});
queue.add({ random_attr: 'random_value' });
```

1. `'waiting'`에서 작업을 가져와 `'active'`로 이동합니다.

```typescript
const job: Job = await queue.getNextJob();
```

1. 문제가 발생하면 작업을 `'failed'` 큐로 이동합니다.

```typescript
const (nextJobData, nextJobId) = await job.moveToFailed(
  {
    message: 'Call to external service failed!',
  },
  true,
);
```

1. 작업을 `'completed'` 큐로 이동합니다.

```typescript
const (nextJobData, nextJobId) = await job.moveToCompleted('succeeded', true);
```

1. 다음 작업이 있으면 반환합니다.

```typescript
if (nextJobdata) {
  return Job.fromJSON(queue, nextJobData, nextJobId);
}
```

**참고**

기본적으로 `getNextJob` 또는 `moveToCompleted`가 반환한 작업의 lock duration은 30초입니다. 이보다 더 오래 걸리면 작업은 자동으로 stalled로 표시되며, max stalled 옵션에 따라 wait 상태로 다시 이동하거나 failed로 표시됩니다. 이를 피하려면 lock이 만료되기 전에 시간을 더 확보할 수 있도록 `job.extendLock(duration)`을 사용해야 합니다. lock 시간의 절반이 지났을 때 lock을 연장하는 것을 권장합니다.

