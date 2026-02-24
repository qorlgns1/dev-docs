---
title: 'Getters'
description: '큐에 작업이 추가되면, 작업 수명 주기 동안 서로 다른 상태에 있게 됩니다. BullMQ는 이러한 다양한 상태의 정보와 작업을 조회할 수 있는 메서드를 제공합니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/getters

# Getters

큐에 작업이 추가되면, 작업 수명 주기 동안 서로 다른 상태에 있게 됩니다. BullMQ는 이러한 다양한 상태의 정보와 작업을 조회할 수 있는 메서드를 제공합니다.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-8ccf86e0633ddb1016f5f56af5dbe0decc412aa3%2Fsimple-architecture.png?alt=media" alt="큐에서 BullMQ 작업의 수명 주기를 나타낸 다이어그램"><figcaption><p>작업의 수명 주기</p></figcaption></figure>

#### Job Counts

특정 상태에 있는 작업 수를 확인해야 하는 경우가 자주 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const counts = await myQueue.getJobCounts('wait', 'completed', 'failed');

// Returns an object like this { wait: number, completed: number, failed: number }
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

myQueue = Queue('Paint')

counts = await myQueue.getJobCounts('wait', 'completed', 'failed')

# Returns an object like this { wait: number, completed: number, failed: number }
```

{% endtab %}
{% endtabs %}

사용 가능한 상태는 다음과 같습니다:

* *completed*,
* *failed*,
* *delayed*,
* *active*,
* *wait*,
* *waiting-children*,
* *prioritized*,
* *paused*, and
* *repeat*.

#### Get Jobs

페이지네이션 방식의 의미론으로 작업을 조회하는 것도 가능합니다. 예를 들면:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const completed = await myQueue.getJobs(['completed'], 0, 100, true);

// returns the oldest 100 jobs
```

{% endtab %}

{% tab title="Python" %}

```python
completed = await myQueue.getJobs(['completed'], 0, 100, True)

# returns the oldest 100 jobs
```

{% endtab %}
{% endtabs %}

## 더 읽어보기:

* 💡 [Get Job Counts API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobcounts)
* 💡 [Get Jobs API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobs)

