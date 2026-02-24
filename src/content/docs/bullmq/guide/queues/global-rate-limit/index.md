---
title: '전역 속도 제한'
description: '원본 URL: https://docs.bullmq.io/guide/queues/global-rate-limit'
---

원본 URL: https://docs.bullmq.io/guide/queues/global-rate-limit

# 전역 속도 제한

전역 속도 제한 구성은 특정 시간 동안 처리되도록 허용되는 작업 수를 결정하는 큐 옵션입니다.

```typescript
import { Queue } from 'bullmq';

// 1 job per second
await queue.setGlobalRateLimit(1, 1000);
```

이 값을 가져오려면:

```typescript
const { max, duration } = await queue.getGlobalRateLimit();
```

현재 TTL을 가져오려면:

```typescript
const ttl = await queue.getRateLimitTtl();
```

{% hint style="info" %}
워커에서 속도 제한 수준을 선택하더라도 전역 설정은 덮어쓰지 않습니다.
{% endhint %}

### 전역 속도 제한 제거

다음 메서드를 사용해 수행할 수 있습니다:

```typescript
await queue.removeGlobalRateLimit();
```

## 더 읽어보기:

* 💡 [Set Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#setglobalratelimit)
* 💡 [Get Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getglobalratelimit)
* 💡 [Get Rate Limit Ttl API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getratelimitttl)
* 💡 [Remove Global Rate Limit API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removeglobalratelimit)

