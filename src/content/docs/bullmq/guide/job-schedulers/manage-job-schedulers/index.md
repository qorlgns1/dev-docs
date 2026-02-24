---
title: 'Job Scheduler 관리'
description: 'BullMQ에서는 효율적이고 체계적인 백그라운드 작업을 유지하기 위해 Job Scheduler의 수명 주기와 목록을 관리하는 것이 중요합니다. Job Scheduler를 추가하거나 업데이트할 수 있는 upsertJobScheduler 메서드 외에도, removeJobS...'
---

Source URL: https://docs.bullmq.io/guide/job-schedulers/manage-job-schedulers

# Job Scheduler 관리

BullMQ에서는 효율적이고 체계적인 백그라운드 작업을 유지하기 위해 Job Scheduler의 수명 주기와 목록을 관리하는 것이 중요합니다. Job Scheduler를 추가하거나 업데이트할 수 있는 upsertJobScheduler 메서드 외에도, removeJobScheduler와 getJobSchedulers라는 두 가지 메서드가 핵심적인 역할을 합니다. 이 함수들은 각각 스케줄러 삭제와 기존 스케줄러 전체 조회를 가능하게 하여, 작업 스케줄링 환경을 포괄적으로 제어할 수 있게 해줍니다.

#### Job Scheduler 삭제

**removeJobScheduler** 메서드는 큐에서 특정 Job Scheduler를 삭제하도록 설계되었습니다. 예약된 작업이 더 이상 필요하지 않거나, 비활성/구식 스케줄러를 정리해 리소스 사용을 최적화하려는 경우에 특히 유용합니다.

```typescript
// Remove a job scheduler with ID 'scheduler-123'
const result = await queue.removeJobScheduler('scheduler-123');
console.log(
  result ? 'Scheduler removed successfully' : 'Missing Job Scheduler',
);
```

이 메서드는 주어진 ID에 해당하는 Job Scheduler가 존재해 삭제되면 true를, 존재하지 않으면 false를 반환합니다.

#### Job Schedulers 조회

**getJobSchedulers** 메서드는 지정한 범위 내에서 설정된 모든 Job Scheduler 목록을 조회합니다. 이는 여러 Job Scheduler를 모니터링하고 관리할 때 매우 유용하며, 특히 작업이 동적으로 예약되고 빈번한 검토나 조정이 필요한 시스템에서 가치가 큽니다.

```typescript
// Retrieve the first 10 job schedulers in ascending order of their next execution time
const schedulers = await queue.getJobSchedulers(0, 9, true);
console.log('Current job schedulers:', schedulers);
```

이 메서드는 작업이 언제 실행되도록 예약되어 있는지에 대한 인사이트를 제공하는 리포트나 대시보드를 생성할 때 특히 유용하며, 시스템 모니터링과 트러블슈팅에 도움이 됩니다.

#### Job Scheduler 조회

**getJobScheduler** 메서드는 id로 Job Scheduler를 조회합니다. 이는 특정 설정을 점검할 때 매우 유용합니다.

```typescript
const scheduler = await queue.getJobScheduler('test');
console.log('Current job scheduler:', scheduler);
```

## 더 읽어보기:

* 💡 [Remove Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removejobscheduler)
* 💡 [Get Job Schedulers API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobschedulers)
* 💡 [Get Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobscheduler)

