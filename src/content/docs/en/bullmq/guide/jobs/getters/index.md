---
title: 'Getters'
description: 'When jobs are added to a queue, they will be in different statuses during their lifetime. BullMQ provides methods to retrieve information and jobs fro...'
---

Source URL: https://docs.bullmq.io/guide/jobs/getters

# Getters

When jobs are added to a queue, they will be in different statuses during their lifetime. BullMQ provides methods to retrieve information and jobs from the different statuses.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-8ccf86e0633ddb1016f5f56af5dbe0decc412aa3%2Fsimple-architecture.png?alt=media" alt="Diagram of the lifecycle of a BullMQ job in the queue"><figcaption><p>Lifecycle of a job</p></figcaption></figure>

#### Job Counts

It is often necessary to know how many jobs are in a given status:

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

The available status are:

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

It is also possible to retrieve the jobs with pagination style semantics. For example:

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

## Read more:

* 💡 [Get Job Counts API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobcounts)
* 💡 [Get Jobs API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getjobs)

