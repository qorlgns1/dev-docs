---
title: '의존성 제거'
description: '일부 상황에서는 부모 작업이 있고, 자식 작업 중 하나가 실패할 때 그 관계를 제거해야 할 수 있습니다.'
---

원문 URL: https://docs.bullmq.io/guide/flows/remove-dependency

# 의존성 제거

일부 상황에서는 부모 작업이 있고, 자식 작업 중 하나가 실패할 때 그 관계를 제거해야 할 수 있습니다.

이 요구 사항을 해결하는 패턴은 **removeDependencyOnFailure** 옵션을 사용하는 것입니다. 이 옵션은 작업이 실패할 때 부모에서 해당 의존성이 제거되도록 보장하므로, 부모 작업은 실패한 자식 작업을 기다리지 않고 완료됩니다.

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
      opts: { removeDependencyOnFailure: true },
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
이 옵션이 설정된 **자식** 작업이 실패하는 즉시, 더 이상 대기 중인 자식이 없는 경우에만 부모 작업이 대기 상태로 이동합니다.
{% endhint %}

## 더 읽어보기:

* 💡 [Add Flow API 레퍼런스](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)

