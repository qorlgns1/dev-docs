---
title: '플로우 일괄 추가'
description: '때로는 플로우를 원자적으로 대량 추가해야 할 필요가 있습니다. 예를 들어, 모든 플로우가 생성되거나 아무것도 생성되지 않아야 하는 요구사항이 있을 수 있습니다. 또한 플로우를 대량으로 추가하면 Redis로의 왕복 횟수를 줄일 수 있어 더 빠를 수 있습니다.'
---

원문 URL: https://docs.bullmq.io/guide/flows/adding-bulks

# 플로우 일괄 추가

때로는 플로우를 원자적으로 대량 추가해야 할 필요가 있습니다. 예를 들어, 모든 플로우가 생성되거나 아무것도 생성되지 않아야 하는 요구사항이 있을 수 있습니다. 또한 플로우를 대량으로 추가하면 Redis로의 왕복 횟수를 줄일 수 있어 더 빠를 수 있습니다.

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const trees = await flow.addBulk([
  {
    name: 'root-job-1',
    queueName: 'rootQueueName-1',
    data: {},
    children: [
      {
        name,
        data: { idx: 0, foo: 'bar' },
        queueName: 'childrenQueueName-1',
      },
    ],
  },
  {
    name: 'root-job-2',
    queueName: 'rootQueueName-2',
    data: {},
    children: [
      {
        name,
        data: { idx: 1, foo: 'baz' },
        queueName: 'childrenQueueName-2',
      },
    ],
  },
]);
```

이 호출은 성공하거나 실패만 할 수 있으며, 모든 job이 추가되거나 하나도 추가되지 않습니다.

## 더 읽어보기:

* 💡 [Add Bulk API 레퍼런스](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk)

