---
title: '이벤트 수동 trim'
description: 'BullMQ의 모든 클래스는 큐에서 실행 중인 작업의 수명 주기를 알려주는 유용한 이벤트를 발생시킵니다. 모든 클래스는 이며 서로 다른 이벤트를 발생시킵니다.'
---

Source URL: https://docs.bullmq.io/guide/events

# 이벤트

BullMQ의 모든 클래스는 큐에서 실행 중인 작업의 수명 주기를 알려주는 유용한 이벤트를 발생시킵니다. 모든 클래스는 `EventEmitter`이며 서로 다른 이벤트를 발생시킵니다.

몇 가지 예시:

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

myQueue.on('waiting', (job: Job) => {
  // Job is waiting to be processed.
});
```

```typescript
import { Worker } from 'bullmq';

const myWorker = new Worker('Paint');

myWorker.on('drained', () => {
  // Queue is drained, no more jobs left
});

myWorker.on('completed', (job: Job) => {
  // job has completed
});

myWorker.on('failed', (job: Job) => {
  // job has failed
});
```

위 이벤트들은 실제로 작업을 완료한 워커에 대한 로컬 이벤트입니다. 하지만 많은 경우, 모든 워커가 발생시키는 모든 이벤트를 한 곳에서 수신하고 싶을 수 있습니다. 이럴 때 [`QueueEvents`](https://api.docs.bullmq.io/classes/v5.QueueEvents.html) 클래스를 사용할 수 있습니다.

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('Paint');

queueEvents.on('completed', ({ jobId }) => {
  // Called every time a job is completed in any worker.
});

queueEvents.on(
  'progress',
  ({ jobId, data }: { jobId: string; data: number | object }) => {
    // jobId received a progress event
  },
);
```

`QueueEvents` 클래스는 [Redis streams](https://redis.io/topics/streams-intro)를 사용해 구현되어 있습니다. 이는 몇 가지 장점이 있는데, 예를 들어 일반적인 pub-sub과 달리 연결이 끊어지는 상황에서도 이벤트가 전달되고 유실되지 않음을 보장합니다.

{% hint style="danger" %}
이벤트 스트림은 크기가 너무 커지지 않도록 자동으로 trim됩니다. 기본값은 \~10.000 이벤트이며, `streams.events.maxLen` 옵션으로 설정할 수 있습니다.
{% endhint %}

### 이벤트 수동 trim

이벤트를 수동으로 trim해야 하는 경우 **`trimEvents`** 메서드를 사용할 수 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.trimEvents(10); // leaves 10 events
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

await queue.trimEvents(10) # leaves 10 events
```

{% endtab %}
{% endtabs %}

## 더 읽어보기:

* 💡 [Queue Events API 레퍼런스](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)
* 💡 [Queue Events Listener API 레퍼런스](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)
* 💡 [Queue Listener API 레퍼런스](https://api.docs.bullmq.io/interfaces/v5.QueueListener.html)
* 💡 [Worker Listener API 레퍼런스](https://api.docs.bullmq.io/interfaces/v5.WorkerListener.html)

