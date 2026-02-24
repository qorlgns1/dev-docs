---
title: '자식 의존성 제거'
description: '일부 상황에서는 부모 작업이 있고, 그 자식 중 하나의 의존성을 제거해야 할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/flows/remove-child-dependency

# 자식 의존성 제거

일부 상황에서는 부모 작업이 있고, 그 자식 중 하나의 의존성을 제거해야 할 수 있습니다.

이 요구사항을 해결하는 패턴은 **removeChildDependency** 메서드를 사용하는 것입니다. 이 메서드는 해당 작업이 마지막 대기 중인 자식일 경우 부모를 *waiting* 으로 이동시키고, 부모의 미처리 목록에 표시되지 않도록 보장합니다.

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
      opts: {},
    },
  ],
});

await originalTree.children[0].job.removeChildDependency();
```

{% hint style="info" %}
**자식**이 이 메서드를 호출하는 즉시, 기존 부모가 있는지 확인하며 부모가 없으면 오류를 발생시킵니다.
{% endhint %}

이 옵션을 사용하는 실패 또는 완료된 자식은 미처리 목록에 포함되지 않으므로 제거 작업이 발생하지 않습니다.

