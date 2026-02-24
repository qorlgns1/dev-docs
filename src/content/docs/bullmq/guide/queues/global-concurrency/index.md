---
title: '전역 동시성'
description: '전역 동시성 계수는 모든 worker 인스턴스 전체에서 병렬로 처리할 수 있는 job 수를 결정하는 queue 옵션입니다.'
---

Source URL: https://docs.bullmq.io/guide/queues/global-concurrency

# 전역 동시성

전역 동시성 계수는 모든 worker 인스턴스 전체에서 병렬로 처리할 수 있는 job 수를 결정하는 queue 옵션입니다.

```typescript
import { Queue } from 'bullmq';

await queue.setGlobalConcurrency(4);
```

그리고 이 값을 가져오려면:

```typescript
const globalConcurrency = await queue.getGlobalConcurrency();
```

{% hint style="info" %}
worker에서 동시성 수준을 선택하더라도 전역 동시성을 덮어쓰지는 않습니다. 이는 특정 worker가 병렬로 처리할 수 있는 최대 job 수를 의미할 뿐이며, 전역 동시성 값을 절대 초과할 수 없습니다.
{% endhint %}

### 전역 동시성 제거

다음 메서드를 사용해 수행할 수 있습니다:

```typescript
await queue.removeGlobalConcurrency();
```

## 더 읽어보기:

* 💡 [전역 동시성 설정 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#setglobalconcurrency)
* 💡 [전역 동시성 조회 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#getglobalconcurrency)
* 💡 [전역 동시성 제거 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#removeglobalconcurrency)

