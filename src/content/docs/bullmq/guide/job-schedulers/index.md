---
title: 'Job Schedulers'
description: 'Job Scheduler는 지정된 "repeat" 설정에 따라 작업을 생성하는 팩토리 역할을 합니다. Job Scheduler는 매우 유연하여, 고정 간격으로 생성되는 작업, cron 표현식에 따른 작업, 또는 사용자 정의 요구사항 기반 작업 등 다양한 시나리오를 지원...'
---

Source URL: https://docs.bullmq.io/guide/job-schedulers

# Job Schedulers

Job Scheduler는 지정된 "repeat" 설정에 따라 작업을 생성하는 팩토리 역할을 합니다. Job Scheduler는 매우 유연하여, 고정 간격으로 생성되는 작업, cron 표현식에 따른 작업, 또는 사용자 정의 요구사항 기반 작업 등 다양한 시나리오를 지원합니다. 역사적인 이유로, Job Scheduler가 생성한 작업은 흔히 ‘Repeatable Jobs’라고 불립니다.

스케줄러를 생성하려면, 아래 예시처럼 "upsertJobScheduler" 메서드를 사용하면 됩니다:

```typescript
// Creates a new Job Scheduler that generates a job every 1000 milliseconds (1 second)
const firstJob = await queue.upsertJobScheduler('my-scheduler-id', {
  every: 1000,
});
```

이 예시는 매초 새 작업을 생성하는 새로운 Job Scheduler를 만듭니다. 또한 이 Job Scheduler에 대해 처음 생성된 작업도 반환하며, 이 작업은 1초 후 처리되기를 기다리는 "delayed" 상태가 됩니다.

여기서 설명해야 할 중요한 고려사항이 몇 가지 더 있습니다.:

* **Upsert vs. Add:** 반복 작업 관리를 단순화하기 위해, 특히 프로덕션 배포 환경에서는 'add' 대신 'upsert'를 사용합니다. 이를 통해 중복 없이 스케줄러를 생성하거나 업데이트할 수 있습니다.
* **Job Production Rate:** 스케줄러는 마지막 작업이 처리를 시작할 때만 새 작업을 생성합니다. 따라서 큐가 매우 바쁘거나, 워커 수 또는 concurrency가 충분하지 않으면, 지정된 반복 간격보다 작업 생성 주기가 더 길어질 수 있습니다.
* **Job Status:** Job Scheduler가 작업을 계속 생성하는 동안에는, 해당 스케줄러와 연결된 작업 하나가 항상 "Delayed" 상태로 존재합니다.

### Using Job Templates

큐에 추가되는 작업에 대해 표준 이름, 데이터, 옵션을 포함한 템플릿도 정의할 수 있습니다. 이렇게 하면 Job Scheduler가 생성하는 모든 작업이 이 설정을 상속받습니다:

```typescript
// Create jobs every day at 3:15 (am)
const firstJob = await queue.upsertJobScheduler(
  'my-scheduler-id',
  { pattern: '0 15 3 * * *' },
  {
    name: 'my-job-name',
    data: { foo: 'bar' },
    opts: {
      backoff: 3,
      attempts: 5,
      removeOnFail: 1000,
    },
  },
);
```

이 스케줄러가 생성하는 모든 작업은 주어진 설정을 사용합니다. 또한 이후에 같은 "my-scheduler-id"로 "upsertJobScheduler"를 다시 호출해, repeat 옵션이나 작업 템플릿 설정 등 이 특정 job scheduler의 설정을 업데이트할 수 있습니다.

{% hint style="info" %}
Job Scheduler가 생성하는 작업은 주어진 repeat 설정보다 더 자주 생성되지 않도록 보장하기 위해 특별한 job ID를 사용하므로, 사용자 정의 job id를 선택할 수 없습니다. 다만 이러한 작업을 다른 작업과 구분해야 한다면 job name을 사용할 수 있습니다.
{% endhint %}

## Read more:

* 💡 [Upsert Job Scheduler API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#upsertjobscheduler)

