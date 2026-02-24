---
title: '작업 재시도 중지'
description: '프로세서가 복구 불가능한 예외를 던지는 경우에는  클래스를 사용해야 합니다. 이 경우 BullMQ는 작업을 failed set으로 바로 이동시키고 재시도를 수행하지 않으므로, 작업을 큐에 추가할 때 설정한  값도 무시됩니다.'
---

Source URL: https://docs.bullmq.io/patterns/stop-retrying-jobs

# 작업 재시도 중지

프로세서가 복구 불가능한 예외를 던지는 경우에는 `UnrecoverableError` 클래스를 사용해야 합니다. 이 경우 BullMQ는 작업을 failed set으로 바로 이동시키고 재시도를 수행하지 않으므로, 작업을 큐에 추가할 때 설정한 `attempts` 값도 무시됩니다.

```typescript
import { Worker, UnrecoverableError } from 'bullmq';

const worker = new Worker(
  'foo',
  async job => {
    doSomeProcessing();
    throw new UnrecoverableError('Unrecoverable');
  },
  { connection },
);

await queue.add(
  'test-retry',
  { foo: 'bar' },
  {
    attempts: 3,
    backoff: 1000,
  },
);
```

## 수동 rate-limit 시 작업 실패 처리

`RateLimitError`로 작업이 rate limit된 뒤 다시 시도되면, rate limiting은 실제 오류로 간주되지 않기 때문에 `attempts` 검사가 무시됩니다. 하지만 `attempts`를 수동으로 확인해 작업 재시도를 피하고 싶다면, 아래와 같이 `job.attemptsStarted`를 확인할 수 있습니다.

```typescript
import { Worker, RateLimitError, UnrecoverableError } from 'bullmq';

const worker = new Worker(
  'myQueue',
  async job => {
    const [isRateLimited, duration] = await doExternalCall();
    if (isRateLimited) {
      await queue.rateLimit(duration);
      if (job.attemptsStarted >= job.opts.attempts) {
        throw new UnrecoverableError('Unrecoverable');
      }
      // Do not forget to throw this special exception,
      // since we must differentiate this case from a failure
      // in order to move the job to wait again.
      throw new RateLimitError();
    }
  },
  {
    connection,
    limiter: {
      max: 1,
      duration: 500,
    },
  },
);
```

{% hint style="info" %}
`job.attemptsMade`는 `RateLimitError`, `DelayedError`, `WaitingChildrenError`를 제외한 오류가 발생했을 때 증가합니다. 반면 `job.attemptsStarted`는 작업이 active로 이동할 때마다 증가합니다.
{% endhint %}

## 더 읽어보기:

* 💡 [Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#ratelimit)

