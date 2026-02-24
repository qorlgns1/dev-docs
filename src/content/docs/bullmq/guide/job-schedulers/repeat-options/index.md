---
title: '반복 옵션'
description: '원본 URL: https://docs.bullmq.io/guide/job-schedulers/repeat-options'
---

원본 URL: https://docs.bullmq.io/guide/job-schedulers/repeat-options

# 반복 옵션

반복의 일부 동작을 제어하기 위해 모든 Job Scheduler에서 사용할 수 있는 몇 가지 옵션이 있습니다. 하나씩 살펴보겠습니다.

#### 시작 날짜

이 옵션은 작업 스케줄링이 시작될 미래 날짜를 설정합니다. 특정 날짜부터 반복을 시작해야 하는 작업을 설정할 때 유용합니다.

```typescript
const { Queue } = require('bullmq');
const connection = { host: 'localhost', port: 6379 };
const myQueue = new Queue('my-dated-jobs', { connection });

await myQueue.upsertJobScheduler(
  'start-later-job',
  {
    every: 60000, // every minute
    startDate: new Date('2024-10-15T00:00:00Z'), // start on October 15, 2024
  },
  {
    name: 'timed-start-job',
    data: { message: 'Starting later' },
  },
);
```

#### 종료 날짜

이 옵션을 사용해 작업 스케줄링이 중단될 시점을 지정할 수 있으며, 결과적으로 작업 반복에 대한 만료일을 설정하게 됩니다.

```typescript
await myQueue.upsertJobScheduler(
  'end-soon-job',
  {
    every: 60000, // every minute
    endDate: new Date('2024-11-01T00:00:00Z'), // end on November 1, 2024
  },
  {
    name: 'timed-end-job',
    data: { message: 'Ending soon' },
  },
);
```

#### 제한

이 설정은 작업이 반복되는 횟수를 제한하는 데 사용됩니다. 횟수가 이 제한에 도달하면 해당 Job Scheduler에 대해 더 이상 작업이 생성되지 않습니다.

```typescript
await myQueue.upsertJobScheduler(
  'limited-job',
  {
    every: 10000, // every 10 seconds
    limit: 10, // limit to 10 executions
  },
  {
    name: 'limited-execution-job',
    data: { message: 'Limited runs' },
  },
);
```

#### immediately

이 설정은 스케줄과 관계없이 작업이 추가되자마자 즉시 실행되도록 강제합니다. 정규 주기에 들어가기 전에 즉각적인 동작이 필요한 상황에서 도움이 됩니다.

BullMQ에서 every 옵션을 사용하면 작업은 고정된 시간 간격을 기준으로 스케줄링되며, 처음에는 다소 직관에 어긋나 보일 수 있습니다. 예를 들어 간격을 2000ms로 설정하면 작업은 0, 2, 4, 6, 8초처럼 짝수 초마다 트리거됩니다. 즉, 실제로 작업을 언제 추가했는지와 관계없이 스케줄링은 시계 기준에 맞춰 정렬됩니다.

간격의 시계 정렬 여부와 상관없이 Job Scheduler를 추가한 직후 작업 처리를 시작해야 한다면 immediately 설정을 사용할 수 있습니다. 이는 특히 간격이 긴 경우에 중요합니다. 예를 들어 작업을 매월 반복하도록 설정하면, 일반적으로는 다음 달의 첫 번째 초가 될 때까지 시작을 기다립니다. 월중에 작업을 추가하면 다음 달 시작 시점까지 실행되지 않습니다. immediately를 사용하면 예약 간격이 시작될 때까지 기다리지 않고, 작업이 추가되는 즉시 첫 실행이 이루어집니다.

```typescript
await myQueue.upsertJobScheduler(
  'immediate-job',
  {
    every: 86400000, // once a day
    immediately: true, // execute the first one immediately
  },
  {
    name: 'instant-job',
    data: { message: 'Immediate start' },
  },
);
```

{% hint style="danger" %}
버전 5.19.0부터 "immediately" 옵션은 deprecated 되었습니다. 현재 동작은 "immediately"가 항상 true인 것과 같으며, 즉 새로 삽입된 Job Scheduler의 첫 반복은 항상 즉시 실행되고 이후에는 "every" 설정에 따라 반복됩니다. **기존** Scheduler에 대해 upsertJobScheduler를 다시 호출하는 경우에는 즉시 반복이 발생하지 않고, 대신 "every" 간격을 따릅니다.
{% endhint %}

