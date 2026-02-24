---
title: '작업 자동 제거'
description: '기본적으로 큐 작업이 완료(또는 실패)되면 와 라는 두 개의 특별한 세트에 저장됩니다. 이는 특히 개발 초기 단계에서 작업 결과를 확인하는 데 유용합니다. 하지만 솔루션이 프로덕션 수준에 도달하면, Redis를 크게 유용하지 않은 데이터로 채우지 않도록 보관할 완료된 ...'
---

Source URL: https://docs.bullmq.io/guide/queues/auto-removal-of-jobs

# 작업 자동 제거

기본적으로 큐 작업이 완료(또는 실패)되면 `"completed"`와 `"failed"`라는 두 개의 특별한 세트에 저장됩니다. 이는 특히 개발 초기 단계에서 작업 결과를 확인하는 데 유용합니다. 하지만 솔루션이 프로덕션 수준에 도달하면, Redis를 크게 유용하지 않은 데이터로 채우지 않도록 보관할 완료된 작업 수를 제한해야 하는 경우가 많습니다.

BullMQ는 최종 상태가 된 작업을 자동 제거하기 위한 다양한 전략을 지원합니다. 이러한 전략은 Job 옵션인 [`removeOnComplete`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#removeoncomplete)와 [`removeOnFail`](https://api.docs.bullmq.io/interfaces/v5.BaseJobOptions.html#removeonfail)에서 설정합니다.

### 모든 최종 상태 작업 제거

가장 간단한 방법은 `removeOnComplete`/`removeOnFail`를 `true`로 설정하는 것입니다. 이 경우 모든 작업은 최종 상태가 되는 즉시 자동으로 제거됩니다.

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  { removeOnComplete: true, removeOnFail: true },
);
```

{% hint style="warning" %}
작업은 이름과 관계없이 삭제됩니다.
{% endhint %}

### 특정 개수의 작업 유지

유지할 작업의 최대 개수를 지정할 수도 있습니다. 일반적으로 완료된 작업은 소수만 유지하고, 실패한 작업은 훨씬 더 큰 값을 유지하는 것이 좋은 방법입니다.

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  { removeOnComplete: 1000, removeOnFail: 5000 },
);
```

### 작업 생성 시점(나이) 기준으로 유지

또 다른 방법은 특정 기간까지만 작업을 유지하는 것입니다. `removeOn` 옵션은 [`KeepJobs`](https://api.docs.bullmq.io/interfaces/v5.KeepJobs.html) 객체를 받으며, 여기에는 `age`와 `count` 필드가 포함됩니다. `age`는 얼마나 오래된 작업까지 유지할지(초 단위)를 지정하고, `count`는 전체 유지 개수를 제한할 때 사용할 수 있습니다. `count` 옵션은 매우 짧은 시간에 예상치 못한 양의 작업이 들어오는 경우에 유용하며, 이때 메모리 부족을 방지하기 위해 일정 개수로 제한할 수 있습니다.

```typescript
await myQueue.add(
  'test',
  { foo: 'bar' },
  {
    removeOnComplete: {
      age: 3600, // keep up to 1 hour
      count: 1000, // keep up to 1000 jobs
    },
    removeOnFail: {
      age: 24 * 3600, // keep up to 24 hours
    },
  },
);
```

{% hint style="info" %}
작업 자동 제거는 지연(lazy) 방식으로 동작합니다. 즉, 새 작업이 완료되거나 실패할 때에만 자동 제거가 수행되므로, 그 시점이 아니면 작업은 제거되지 않습니다.
{% endhint %}

### 멱등성은 어떻게 되나요?

BullMQ에서 멱등성을 구현하는 전략 중 하나는 고유한 작업 id를 사용하는 것입니다. 큐에 이미 존재하는 id로 작업을 추가하면 새 작업은 무시되고 **duplicated** 이벤트가 트리거됩니다. 작업 자동 제거를 활성화할 때는 이 점을 반드시 염두에 두어야 합니다. 제거된 작업은 더 이상 큐의 일부로 간주되지 않으므로, 같은 Id를 가질 수 있는 이후 작업에 영향을 주지 않습니다.

## 더 읽어보기:

* 💡 [중복 이벤트 참조](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html#duplicated)

