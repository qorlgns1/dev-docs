---
title: '우선순위 지정'
description: '작업에는  옵션도 포함할 수 있습니다. 우선순위를 사용하면 작업 처리 순서는 FIFO 또는 LIFO 패턴을 따르지 않고, 지정된 의 영향을 받습니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/prioritized

# 우선순위 지정

작업에는 `priority` 옵션도 포함할 수 있습니다. 우선순위를 사용하면 작업 처리 순서는 FIFO 또는 LIFO 패턴을 따르지 않고, 지정된 `priority`의 영향을 받습니다.

{% hint style="warning" %}
우선순위 작업을 추가하는 작업은 다른 유형의 작업보다 느리며, 큐의 우선순위 집합에 있는 작업 수를 기준으로 복잡도는 `O(log(n))`입니다.
{% endhint %}

우선순위는 `1`부터 `2 097 152`까지이며, 숫자가 낮을수록 항상 더 **높은** 우선순위라는 점에 유의하세요.

{% hint style="danger" %}
`priority`가 지정되지 않은 작업은 가장 높은 우선순위를 가지며, 우선순위가 지정된 작업보다 먼저 처리됩니다.
{% endhint %}

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

await myQueue.add('wall', { color: 'pink' }, { priority: 10 });
await myQueue.add('wall', { color: 'brown' }, { priority: 5 });
await myQueue.add('wall', { color: 'blue' }, { priority: 7 });

// The wall will be painted first brown, then blue and
// finally pink.
```

여러 작업이 동일한 우선순위 값으로 추가되면, 해당 우선순위 내 작업들은 [FIFO (*First in, first out*)](https://docs.bullmq.io/guide/jobs/fifo) 방식으로 처리됩니다.

## 우선순위 변경

작업을 삽입한 뒤 `priority`를 변경하려면 **`changePriority`** 메서드를 사용하세요. 예를 들어, `priority`를 `16`에서 `1`로 변경하려는 경우:

```typescript
const job = await Job.create(queue, 'test2', { foo: 'bar' }, { priority: 16 });

await job.changePriority({
  priority: 1,
});
```

또는 [LIFO (*Last In, First Out*)](https://docs.bullmq.io/guide/jobs/lifo) 옵션을 사용하려는 경우:

```typescript
const job = await Job.create(queue, 'test2', { foo: 'bar' }, { priority: 16 });

await job.changePriority({
  lifo: true,
});
```

## 우선순위 작업 가져오기

prioritized는 새로운 상태이므로, 다음과 같이 **`getJobs`** 또는 **`getPrioritized`** 메서드를 사용해야 합니다:

```typescript
const jobs = await queue.getJobs(['prioritized']);

const jobs2 = await queue.getPrioritized();
```

## 우선순위별 개수 가져오기

`prioritized` 상태(우선순위 0보다 큼) 또는 `waiting` 상태(우선순위 0)에 있는 작업의 `count`를 가져오려면 **`getCountsPerPriority`** 메서드를 사용하세요. 예를 들어, `priority` `1`과 `0`의 개수를 가져오려는 경우:

```typescript
const counts = await queue.getCountsPerPriority([1, 0]);
/*
{
  '1': 11,
  '0': 10
}
*/
```

## 더 읽어보기:

* 📋 [Faster Priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)
* 💡 [Change Priority API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#changepriority)
* 💡 [Get Prioritized API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getprioritized)
* 💡 [Get Counts per Priority API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#getcountsperpriority)

