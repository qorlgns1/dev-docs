---
title: 'Flow 트리 가져오기'
description: '일부 상황에서는 하나의 job과 그 모든 자식, 손자식 등을 함께 가져와야 할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/flows/get-flow-tree

# Flow 트리 가져오기

일부 상황에서는 하나의 job과 그 모든 자식, 손자식 등을 함께 가져와야 할 수 있습니다.

이 요구사항을 해결하는 패턴은 [`getFlow`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#getflow) 메서드를 사용하는 것입니다.

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
      children: [
        {
          name,
          data: { idx: 4, foo: 'baz' },
          queueName: 'grandchildrenQueueName',
        },
      ],
    },
    {
      name,
      data: { idx: 2, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
    {
      name,
      data: { idx: 3, foo: 'bis' },
      queueName: 'childrenQueueName',
    },
  ],
});

const { job: topJob } = originalTree;

const tree = await flow.getFlow({
  id: topJob.id,
  queueName: 'topQueueName',
});

const { children, job } = tree;
```

{% hint style="info" %}
각 *child*는 `job` 속성을 가질 수 있으며, 해당 child에도 자식이 있는 경우 `children` 속성도 갖게 됩니다.
{% endhint %}

job 노드 중 하나에 자식이 매우 많은 경우, 그 정보를 제한할 수 있는 방법이 필요할 수도 있습니다.

```typescript
const limitedTree = await flow.getFlow({
  id: topJob.id,
  queueName: 'topQueueName',
  depth: 1, // get only the first level of children
  maxChildren: 2, // get only 2 children per node
});

const { children, job } = limitedTree;
```

## 더 읽어보기:

* 💡 [Get Flow API 참조](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#getflow)

