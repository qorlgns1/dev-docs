---
title: 'Delayed'
description: '지연 작업(Delayed jobs)은 가능한 한 빨리 처리되는 대신, 특별한 "delayed set"에 저장되는 특수한 유형의 작업입니다. 지연 시간이 지나면 해당 작업은 일반 작업처럼 처리됩니다.'
---

출처 URL: https://docs.bullmq.io/guide/jobs/delayed

# Delayed

지연 작업(Delayed jobs)은 가능한 한 빨리 처리되는 대신, 특별한 "delayed set"에 저장되는 특수한 유형의 작업입니다. 지연 시간이 지나면 해당 작업은 일반 작업처럼 처리됩니다.

큐에 지연 작업을 추가하려면, 작업을 지연시키고 싶은 시간(밀리초)을 `delay` 옵션으로 지정하세요.

지정한 *정확한* 지연 시각에 작업이 처리된다고 보장되지는 않습니다. 이는 지연 시간이 지난 시점의 워커 부하 상태와, 정확히 같은 시각에 예약된 다른 지연 작업 수에 따라 달라지기 때문입니다. 다만 실제로는 대부분의 경우 지연 시간은 꽤 정확합니다.

다음은 큐에 지연 작업을 추가하는 예시입니다:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be delayed by at least 5 seconds.
await myQueue.add('house', { color: 'white' }, { delay: 5000 });
```

특정 시점 이후에 작업을 처리하고 싶다면, 그 시점까지 남은 시간을 더하면 됩니다. 예를 들어 2035년 7월 3일 10:30에 작업을 처리하고 싶다면:

```typescript
const targetTime = new Date('03-07-2035 10:30');
const delay = Number(targetTime) - Number(new Date());

await myQueue.add('house', { color: 'white' }, { delay });
```

## 지연 시간 변경

삽입 *이후* 지연 작업을 다시 스케줄링하려면 **`changeDelay`** 메서드를 사용하세요. 이 메서드는 원래 지연 시간과 관계없이, 현재 시각 기준으로 지정한 밀리초 후에 작업이 실행되도록 다시 예약합니다. 예를 들어:

```typescript
const job = await Job.create(queue, 'test', { foo: 'bar' }, { delay: 2000 });

// Reschedule the job to execute 4000ms (4 seconds) from now
await job.changeDelay(4000);
```

{% hint style="warning" %}
현재 **delayed** 상태인 작업만 지연 시간을 변경할 수 있습니다.
{% endhint %}

## 더 읽어보기:

* 💡 [Change Delay API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#changedelay)

