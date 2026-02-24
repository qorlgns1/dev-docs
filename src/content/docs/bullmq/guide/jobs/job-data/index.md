---
title: 'Job 데이터'
description: '원본 URL: https://docs.bullmq.io/guide/jobs/job-data'
---

원본 URL: https://docs.bullmq.io/guide/jobs/job-data

# Job 데이터

모든 job은 고유한 커스텀 데이터를 가질 수 있습니다. 데이터는 job의 **`data`** 속성에 저장됩니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('paint');

const job = await myQueue.add('wall', { color: 'red' });

job.data; // { color: 'red' }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 'red'})

job.data # { color: 'red' }
```

{% endtab %}
{% endtabs %}

## 데이터 업데이트

job을 추가한 후 데이터를 변경하려면 **`updateData`** 메서드를 사용하면 됩니다. 예를 들면 다음과 같습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const job = await Job.create(queue, 'wall', { color: 'red' });

await job.updateData({
  color: 'blue',
});

job.data; // { color: 'blue' }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 'red'})

await job.updateData({'color': 'blue'})
job.data # { color: 'blue' }
```

{% endtab %}
{% endtabs %}

## 더 읽어보기:

* 💡 [데이터 업데이트 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Job.html#updatedata)

