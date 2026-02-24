---
title: '로컬 동시성 계수'
description: 'BullMQ에서 Worker 인스턴스를 사용해 동시성을 달성하는 방법은 기본적으로 두 가지입니다.  계수를 1보다 크게 설정해 워커를 실행할 수 있고(기본값), 서로 다른 node 프로세스에서 여러 워커를 실행할 수도 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/workers/concurrency

# 동시성

BullMQ에서 Worker 인스턴스를 사용해 동시성을 달성하는 방법은 기본적으로 두 가지입니다. `concurrency` 계수를 1보다 크게 설정해 워커를 실행할 수 있고(기본값), 서로 다른 node 프로세스에서 여러 워커를 실행할 수도 있습니다.

#### 로컬 동시성 계수

로컬 동시성 계수는 해당 인스턴스에서 동시에(샌드박스 프로세서를 사용하는 경우 병렬로) 처리할 수 있는 작업 수를 결정하는 worker 옵션입니다. 즉, 동일한 worker가 여러 작업을 동시에 처리하면서도 "at-least-once" 보장이나 처리 순서 같은 특성을 유지할 수 있습니다.

```typescript
import { Worker, Job } from 'bullmq';

const worker = new Worker(
  queueName,
  async (job: Job) => {
    // Do something with job
    return 'some value';
  },
  { concurrency: 50 },
);
```

{% hint style="info" %}
동시성은 worker가 데이터베이스 호출이나 외부 HTTP 서비스 호출처럼 비동기 작업을 수행할 때만 가능합니다. node가 기본적으로 동시성을 지원하는 방식이 그렇기 때문입니다. worker가 CPU 집약적인 경우에는 [Sandboxed processors](https://docs.bullmq.io/guide/workers/sandboxed-processors)를 사용하는 것이 더 좋습니다.
{% endhint %}

또한 worker가 실행 중일 때 필요에 따라 동시성 값을 업데이트할 수 있습니다.

```typescript
worker.concurrency = 5;
```

#### 여러 worker

동시성을 달성하는 또 다른 방법은 여러 worker를 제공하는 것입니다. 이는 동시성뿐 아니라 worker의 고가용성도 제공하므로 BullMQ를 설정할 때 권장되는 방식입니다. 여러 머신에서 실행되는 worker 집합을 쉽게 구성해, 예측 가능하고 견고한 방식으로 작업을 병렬 실행할 수 있습니다.

{% hint style="info" %}
전역 동시성을 한 번에 최대 1개 작업으로 제한해야 한다면 [Global concurrency](https://docs.bullmq.io/guide/queues/global-concurrency)를 참고하세요.
{% endhint %}

각 worker마다 높은 동시성 계수를 선택하는 것도 여전히 가능하며(그리고 매우 좋은 실무 방식입니다), 이렇게 하면 worker가 실행되는 각 머신의 리소스를 더 효율적으로 사용할 수 있습니다.

