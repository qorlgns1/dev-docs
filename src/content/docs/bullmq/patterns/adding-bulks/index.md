---
title: '서로 다른 큐에 작업을 대량으로 추가하기'
description: '때로는 여러 큐에 작업을 원자적으로 대량 추가해야 할 필요가 있습니다. 예를 들어, 모든 작업이 생성되거나 아무것도 생성되지 않아야 한다는 요구사항이 있을 수 있습니다. 또한 작업을 대량으로 추가하면 Redis로의 왕복 횟수가 줄어들어 더 빠를 수 있습니다.'
---

Source URL: https://docs.bullmq.io/patterns/adding-bulks

# 서로 다른 큐에 작업을 대량으로 추가하기

때로는 여러 큐에 작업을 원자적으로 대량 추가해야 할 필요가 있습니다. 예를 들어, 모든 작업이 생성되거나 아무것도 생성되지 않아야 한다는 요구사항이 있을 수 있습니다. 또한 작업을 대량으로 추가하면 Redis로의 왕복 횟수가 줄어들어 더 빠를 수 있습니다.

아마 [`queue.addBulk`](https://api.docs.bullmq.io/classes/v5.Queue.html#addbulk)를 떠올릴 수 있지만, 이 메서드는 단일 큐에만 작업을 추가합니다. 또 다른 옵션은 [`flowProducer.addBulk`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk)이므로, 예제를 살펴보겠습니다:

```typescript
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer({ connection });

const trees = await flow.addBulk([
  {
    name: 'job-1',
    queueName: 'queueName-1',
    data: {}
  },
  {
    name: 'job-2',
    queueName: 'queueName-2',
    data: {}
  },
]);
```

자식 작업 없이 개별 작업을 추가하는 것도 가능합니다.

이 호출은 성공하거나 실패만 하며, 모든 작업이 추가되거나 하나도 추가되지 않습니다.

## 더 읽어보기:

* 💡 [Add Bulk API Reference](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#addbulk)

