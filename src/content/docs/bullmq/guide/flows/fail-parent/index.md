---
title: '부모 작업 실패 처리'
description: '특정 워크플로에서는 자식 작업 중 하나라도 실패하면 부모 작업이 즉시 실패해야 할 수 있습니다.  옵션을 사용하면 이 동작을 구현할 수 있습니다. 자식 작업에서 이 값을 true로 설정하면, 해당 자식이 실패할 때 부모 작업도 실패로 표시됩니다. 이 효과는 작업 계층 ...'
---

Source URL: https://docs.bullmq.io/guide/flows/fail-parent

# 부모 작업 실패 처리

특정 워크플로에서는 자식 작업 중 하나라도 실패하면 부모 작업이 즉시 실패해야 할 수 있습니다. `failParentOnFailure` 옵션을 사용하면 이 동작을 구현할 수 있습니다. 자식 작업에서 이 값을 true로 설정하면, 해당 자식이 실패할 때 부모 작업도 실패로 표시됩니다. 이 효과는 작업 계층 구조를 따라 재귀적으로 전파될 수 있으며, 설정에 따라 조부모 작업이나 그 이상의 상위 조상 작업까지 실패할 수 있습니다.

### 핵심 포인트

* 선택적 적용: failParentOnFailure: true가 설정된 자식 작업만 실패 시 부모 작업의 실패를 유발합니다. 이 옵션이 없는 자식 작업이 실패하더라도 부모 상태에는 영향을 주지 않습니다.
* 재귀 동작: 이 옵션이 있는 자식이 실패하고, 그 부모에도 failParentOnFailure: true가 설정되어 있으면 실패가 작업 트리를 따라 위로 전파되어 조부모 이상까지 영향을 줄 수 있습니다.
* 즉시 효과: 조건을 만족하는 자식 작업이 실패하는 즉시 부모 작업은 failed 상태로 이동합니다.

### 예시

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name: 'child-job',
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      // This child will fail its parent if it fails
      opts: { failParentOnFailure: true },
      children: [
        {
          name,
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
          // This grandchild will fail its parent if it fails
          opts: { failParentOnFailure: true },
        },
        {
          name,
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
          // No failParentOnFailure; its failure won't affect the parent
        },
      ],
    },
    {
      name,
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
      // No failParentOnFailure; its failure won't affect the parent
    },
  ],
});
```

{% hint style="info" %}
이 옵션이 설정된 *자식*이 실패하면, 부모 작업은 지연 방식으로 실패로 표시됩니다. 부모 작업이 failed 상태로 전환되기 전에 워커가 부모 작업을 처리해야 합니다. 실패 시 메시지 **child {childKey} failed**를 포함한 *UnrecoverableError*가 발생합니다. 또한 이 옵션은 재귀적으로 검증되므로, 설정에 따라 조부모나 그 이상의 상위 조상 작업도 실패할 수 있습니다.
{% endhint %}

### 동작 방식

* grandchild-job-1이 실패하면 failParentOnFailure: true 때문에 그 부모(child-job-1)가 실패합니다. 그리고 child-job-1에도 failParentOnFailure: true가 설정되어 있으므로 루트 작업(root-job)도 함께 실패합니다.
* grandchild-job-2가 실패하면, 이 손자 작업에는 failParentOnFailure가 설정되어 있지 않으므로 그 부모(child-job-1)는 실패하지 않습니다.
* 마찬가지로 child-job-2가 실패하더라도, 해당 자식에 failParentOnFailure가 활성화되어 있지 않기 때문에 루트 작업은 영향을 받지 않습니다.

### 사용 사례

이 옵션은 부모 작업의 성공이 특정 자식 작업의 성공에 결정적으로 의존하는 워크플로에서 특히 유용하며, 엄격한 의존성을 강제하고 필요할 때 빠르게 실패(fail fast)하도록 할 수 있습니다.

## 더 읽어보기:

* 💡 [Add Flow API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add)

