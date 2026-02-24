---
title: '의존성 무시'
description: '일부 상황에서는 부모 작업이 있을 때, 자식 작업 중 하나가 실패하더라도 이를 무시해야 할 수 있습니다.'
---

소스 URL: https://docs.bullmq.io/guide/flows/ignore-dependency

# 의존성 무시

일부 상황에서는 부모 작업이 있을 때, 자식 작업 중 하나가 실패하더라도 이를 무시해야 할 수 있습니다.

이 요구사항을 해결하는 패턴은 **ignoreDependencyOnFailure** 옵션을 사용하는 것입니다. 이 옵션을 사용하면 작업이 실패했을 때 부모 작업에서 해당 의존성을 무시하므로, 부모 작업은 실패한 자식 작업을 기다리지 않고 완료됩니다.

```typescript
const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: { ignoreDependencyOnFailure: true },
      children: [
        {
          name,
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
        },
        {
          name,
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
        },
      ],
    },
    {
      name,
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

{% hint style="info" %}
이 옵션이 설정된 **child**가 실패하면, 더 이상 대기 중인 자식 작업이 없을 때에만 부모 작업이 waiting 상태로 이동합니다.
{% endhint %}

이 옵션을 사용해 실패한 자식 작업은 **getIgnoredChildrenFailures** 메서드로 조회할 수 있습니다.

```typescript
const ignoredChildrenFailures =
  await originalTree.job.getIgnoredChildrenFailures();
```

## 더 읽어보기:

* 💡 [Add Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)

