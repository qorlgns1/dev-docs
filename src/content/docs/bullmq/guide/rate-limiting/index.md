---
title: '속도 제한'
description: 'BullMQ는 큐 속도 제한을 제공합니다. 주어진 속도 제한 옵션을 따르도록 워커를 구성할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/rate-limiting

# 속도 제한

BullMQ는 큐 속도 제한을 제공합니다. 주어진 속도 제한 옵션을 따르도록 워커를 구성할 수 있습니다.

```typescript
import { Worker, QueueScheduler } from 'bullmq';

const worker = new Worker('painter', async job => paintCar(job), {
  limiter: {
    max: 10,
    duration: 1000,
  },
});

const scheduler = new QueueScheduler('painter');
```

{% hint style="warning" %}
속도 제한에 걸린 작업은 실제로 `waiting` 상태에 머무르게 됩니다.
{% endhint %}

{% hint style="danger" %}
BullMQ 2.0부터는 `QueueScheduler`가 더 이상 필요하지 않습니다.
{% endhint %}

{% hint style="info" %}
속도 제한기는 전역으로 적용됩니다. 예를 들어 위 설정으로 하나의 큐에 워커가 10개 있어도, 초당 처리되는 작업은 여전히 10개뿐입니다.
{% endhint %}

### 그룹 키

{% hint style="danger" %}
BullMQ 3.0부터는 전역 속도 제한 개선을 위해 그룹 키 지원이 제거되었습니다. 따라서 아래 내용은 이전 버전에만 유효합니다.
{% endhint %}

그룹 키를 기반으로 속도 제한기를 정의할 수도 있습니다. 예를 들어 모든 고객에 대한 전역 속도 제한기 대신, 고객별 속도 제한기를 적용하고 싶을 수 있습니다.

```typescript
import { Queue, Worker, QueueScheduler } from 'bullmq';

const queue = new Queue('painter', {
  limiter: {
    groupKey: 'customerId',
  },
});

const worker = new Worker('painter', async job => paintCar(job), {
  limiter: {
    max: 10,
    duration: 1000,
    groupKey: 'customerId',
  },
});

const scheduler = new QueueScheduler('painter');

// jobs will be rate limited by the value of customerId key:
await queue.add('rate limited paint', { customerId: 'my-customer-id' });
```

### 수동 속도 제한

정적 옵션 기반이 아니라 큐를 수동으로 속도 제한해야 할 때가 있습니다. 예를 들어 API가 `429 Too Many Requests`를 반환하고, 그 응답을 기준으로 큐에 속도 제한을 적용하고 싶을 수 있습니다.

이를 위해 워커 메서드 **`rateLimit`**를 다음과 같이 사용할 수 있습니다.

```typescript
import { Worker } from 'bullmq';

const worker = new Worker(
  'myQueue',
  async () => {
    const [isRateLimited, duration] = await doExternalCall();
    if (isRateLimited) {
      await worker.rateLimit(duration);
      // Do not forget to throw this special exception,
      // since we must differentiate this case from a failure
      // in order to move the job to wait again.
      throw Worker.RateLimitError();
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

{% hint style="warning" %}
속도 제한 검증 실행 여부를 판단할 때 *limiter.max*를 사용하므로, 워커 옵션에 limiter 옵션을 전달하는 것을 잊지 마세요.
{% endhint %}

### 큐 속도 제한 TTL 조회

큐에 속도 제한이 걸려 있는지 확인해야 할 때가 있습니다.

이를 위해 **`getRateLimitTtl`** 메서드를 다음과 같이 사용할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('myQueue', { connection });
const maxJobs = 100;

const ttl = await queue.getRateLimitTtl(maxJobs);

if (ttl > 0) {
  console.log('Queue is rate limited');
}
```

### 속도 제한 키 제거

속도 제한 지연을 중단해야 할 때가 있습니다.

이를 위해 **`removeRateLimitKey`** 메서드를 다음과 같이 사용할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('myQueue', { connection });

await queue.removeRateLimitKey();
```

속도 제한 키를 제거하면 워커가 다시 작업을 가져갈 수 있고, 속도 제한 카운터는 0으로 재설정됩니다.

## 더 읽어보기:

* 💡 [Rate Limit API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Worker.html#ratelimit)
* 💡 [Get Rate Limit Ttl API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#getratelimitttl)
* 💡 [Remove Rate Limit Key API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#removeratelimitkey)

