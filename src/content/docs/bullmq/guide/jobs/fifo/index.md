---
title: 'FIFO'
description: '우리가 설명할 첫 번째 작업 유형은 FIFO(*First-In, First-Out*) 유형입니다. 이는 큐에 작업을 추가할 때의 표준 유형입니다. 작업은 큐에 삽입된 순서와 동일한 순서로 처리됩니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/fifo

# FIFO

우리가 설명할 첫 번째 작업 유형은 FIFO(*First-In, First-Out*) 유형입니다. 이는 큐에 작업을 추가할 때의 표준 유형입니다. 작업은 큐에 삽입된 순서와 동일한 순서로 처리됩니다.

이 순서는 프로세서 수와 관계없이 유지됩니다. 다만 워커가 둘 이상이거나 동시성 계수가 1보다 크면, 워커가 작업을 순서대로 시작하더라도 완료 순서는 약간 달라질 수 있습니다. 일부 작업은 다른 작업보다 완료에 더 많은 시간이 걸릴 수 있기 때문입니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be processed after all others
await myQueue.add('wall', { color: 'pink' });
```

큐에 작업을 추가할 때 사용할 수 있는 옵션이 몇 가지 있습니다. 예를 들어, 작업이 완료되거나 실패했을 때 몇 개의 작업을 유지할지 지정할 수 있습니다.

```typescript
await myQueue.add(
  'wall',
  { color: 'pink' },
  { removeOnComplete: true, removeOnFail: 1000 },
);
```

위 예시에서는 완료된 모든 작업이 자동으로 제거되고, 실패한 작업은 최근 1000개가 큐에 유지됩니다.

## 기본 작업 옵션

큐에 추가하는 모든 작업에 동일한 작업 옵션을 적용하고 싶은 경우가 자주 있습니다. 이 경우 `Queue` 클래스를 인스턴스화할 때 `defaultJobOptions` 옵션을 사용할 수 있습니다.

```typescript
const queue = new Queue('Paint', { defaultJobOptions: {
  removeOnComplete: true, removeOnFail: 1000
});
```

## 더 읽어보기:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)

