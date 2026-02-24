---
title: '작업 일괄 추가'
description: '원본 URL: https://docs.bullmq.io/guide/queues/adding-bulks'
---

원본 URL: https://docs.bullmq.io/guide/queues/adding-bulks

# 작업 일괄 추가

때로는 많은 작업을 원자적으로 추가해야 할 때가 있습니다. 예를 들어, 모든 작업이 큐에 들어가야 하거나 아니면 하나도 들어가면 안 되는 요구사항이 있을 수 있습니다. 또한 작업을 일괄로 추가하면 Redis와의 왕복 횟수를 줄여 더 빠를 수 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const name = 'jobName';
const jobs = await queue.addBulk([
  { name, data: { paint: 'car' } },
  { name, data: { paint: 'house' } },
  { name, data: { paint: 'boat' } },
]);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue("paint")

jobs = await queue.addBulk([
  { "name": "jobName", "data": { "paint": "car" } },
  { "name": "jobName", "data": { "paint": "house" } },
  { "name": "jobName", "data": { "paint": "boat" } }
])
```

{% endtab %}
{% endtabs %}

이 호출은 성공하거나 실패만 하며, 모든 작업이 추가되거나 하나도 추가되지 않습니다.

## 더 읽어보기:

* 💡 [Add Bulk API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#addbulk)

