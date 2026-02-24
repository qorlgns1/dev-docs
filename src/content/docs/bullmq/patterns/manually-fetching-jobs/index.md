---
title: '수동으로 job 처리하기'
description: 'Worker를 생성할 때 가장 일반적인 사용 방식은 process 함수를 지정하여, 큐에 들어오는 job을 워커가 자동으로 처리하게 하는 것입니다.'
---

원문 URL: https://docs.bullmq.io/patterns/manually-fetching-jobs

# 수동으로 job 처리하기

Worker를 생성할 때 가장 일반적인 사용 방식은 process 함수를 지정하여, 큐에 들어오는 job을 워커가 자동으로 처리하게 하는 것입니다.

하지만 경우에 따라 job을 수동으로 가져올 수 있어야 할 때도 있습니다. processor 없이 worker를 생성하고 `getNextJob`을 호출해 다음 job을 가져오면 됩니다:

```typescript
const worker = new Worker('my-queue');

// Specify a unique token
const token = 'my-token';

const job = (await worker.getNextJob(token)) as Job;

// Access job.data and do something with the job
// processJob(job.data)
if (succeeded) {
  await job.moveToCompleted('some return value', token, false);
} else {
  await job.moveToFailed(new Error('my error message'), token, false);
}

await worker.close();
```

수동 처리 시 job "lock"과 관련해 중요한 고려사항이 있습니다. lock은 다른 worker가 이미 처리 중인 job을 가져오지 못하게 합니다. lock의 소유권은 job을 가져올 때 전달한 "token"으로 결정됩니다.

{% hint style="info" %}
다른 큐 시스템에서는 lock duration 설정을 "visibility window"라고 부릅니다.
{% endhint %}

일반적으로 job은 큐에서 가져오는 즉시 lock되며, 최대 유지 시간은 worker 옵션 `lockDuration`에 지정된 값입니다. 기본값은 30초지만 쉽게 다른 값으로 변경할 수 있습니다. 예를 들어 60초로 변경하려면:

```typescript
const worker = new Worker('my-queue', null, { lockDuration: 60000 });
```

표준 worker processor를 사용할 때는 lock duration의 절반 시간이 지나면 lock이 자동으로 갱신됩니다. 하지만 수동으로 job을 처리할 때는 이 메커니즘이 없으므로, job이 큐의 대기 목록으로 다시 이동하지 않게 하려면 `lockDuration`보다 빠르게 job을 처리하거나 lock을 수동으로 연장해야 합니다:

```typescript
const job = (await worker.getNextJob(token)) as Job;

// Extend the lock 30 more seconds
await job.extendLock(token, 30000);
```

### token 선택하기

token은 특정 worker가 현재 특정 job을 처리하고 있다는 소유권을 나타냅니다. worker가 예기치 않게 종료되면 lock이 만료될 때 다른 worker가 해당 job을 가져갈 수 있습니다. job용 token을 생성하는 좋은 방법은 새 job마다 UUID를 생성하는 것이지만, 이는 사용 사례에 따라 달라집니다.

## stalled job 확인하기

job을 수동으로 처리할 때는 stalled job checker도 시작하는 것이 좋습니다. 이 checker는 stalled 상태(lock이 만료된 상태)의 job을 다시 *wait* 상태로 옮기거나(또는 기본값이 1인 [stalled attempts](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#maxstalledcount) 최대 횟수를 모두 소진했다면 *failed*로) 이동시키는 데 필요합니다.

```typescript
await worker.startStalledCheckTimer()
```

checker는 worker가 종료될 때까지 [`stalledInterval`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#stalledinterval) 옵션에 따라 주기적으로 실행됩니다.

## job 순회 처리하기

많은 경우 아래 예시처럼 job을 하나씩 처리하는 "무한" 루프를 사용하게 됩니다. `job.moveToCompleted`/`job.moveToFailed`의 세 번째 파라미터는 사용되지 않으며, 이는 다음 job을 자동으로 반환하라는 의미입니다.

```typescript
const worker = new Worker('my-queue');

const token = 'my-token';
let job;

while (1) {
  let jobData = null,
    jobId,
    success;

  if (job) {
    // Use job.data to process this particular job.
    // and set success variable if succeeded

    if (success) {
      [jobData, jobId] = await job.moveToCompleted('some return value', token);
    } else {
      await job.moveToFailed(new Error('some error message'), token);
    }

    if (jobData) {
      job = Job.fromJSON(worker, jobData, jobId);
    } else {
      job = null;
    }
  } else {
    if (!job) {
      job = await worker.getNextJob(token);
    }
  }
}
```

## Rate Limiting

큐에 rate limit이 걸려 있어서 job을 다시 wait으로 이동하려는 경우입니다.

```typescript
const worker = new Worker('my-queue', null, { connection, prefix });
const token = 'my-token';
await Job.create(queue, 'test', { foo: 'bar' });
const job = (await worker.getNextJob(token)) as Job;

await queue.rateLimit(60000);
await job.moveToWait(token);
```

## 더 읽어보기:

* 💡 [Get Next Job API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Worker.html#getnextjob)
* 💡 [Move To Completed API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#movetocompleted)
* 💡 [Move To Failed API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#movetofailed)
* 💡 [Move To Wait API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#movetowait)

