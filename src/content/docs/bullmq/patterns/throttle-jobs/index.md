---
title: '작업 스로틀링'
description: '때로는 자주 발생하는 이벤트에 반응해 작업을 큐에 넣되, *모든* 이벤트마다 해당 작업을 실행하고 싶지는 않을 수 있습니다. 예를 들어 사용자가 프로필을 업데이트할 때 이메일을 보내고 싶지만, 짧은 시간에 여러 변경을 연속으로 수행하는 경우 매번 이메일을 보내고 싶지는...'
---

Source URL: https://docs.bullmq.io/patterns/throttle-jobs

# 작업 스로틀링

때로는 자주 발생하는 이벤트에 반응해 작업을 큐에 넣되, *모든* 이벤트마다 해당 작업을 실행하고 싶지는 않을 수 있습니다. 예를 들어 사용자가 프로필을 업데이트할 때 이메일을 보내고 싶지만, 짧은 시간에 여러 변경을 연속으로 수행하는 경우 매번 이메일을 보내고 싶지는 않을 수 있습니다.

이를 위해 동일한 `jobId`를 설정할 수 있습니다(기본 고유 정수를 재정의하려면 `JobsOptions.jobId?: string` 사용). 그러면 **동일한 작업은 중복으로 간주되어 큐에 추가되지 않습니다**. 이 옵션을 사용할 경우 `jobId`의 고유성은 직접 보장해야 합니다.

{% hint style="warning" %}
힌트: `removeOnComplete`/`removeOnFailed` 옵션을 사용할 때 주의하세요. 작업이 제거되면 기존 작업으로 간주되지 않으므로, 같은 작업 ID를 가진 새 작업이 중복으로 감지되지 않은 채 큐에 추가될 수 있습니다.
{% endhint %}

예시:

```typescript
import { Job, Queue, Worker } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async (job: Job) => {
  console.log('Do something with job');
  return 'some value';
});

worker.on('completed', (job: Job, returnvalue: any) => {
  console.log('worker done painting', new Date());
});

worker.on('failed', (job: Job, error: Error) => {
  console.error('worker fail painting', job, error, new Date());
});

// Add only one job that will be delayed at least 1 second.
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
myQueue.add('house', { color: 'white' }, { delay: 1000, jobId: 'house' });
```

