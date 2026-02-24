---
title: '중복 제거'
description: 'BullMQ의 중복 제거(Deduplication)는 특정 식별자를 기준으로 작업 실행을 지연시키고 중복을 제거하는 프로세스입니다. 지정된 기간 동안, 또는 특정 작업이 완료되거나 실패할 때까지 동일한 식별자를 가진 새 작업이 큐에 추가되지 않도록 보장합니다. 대신 이...'
---

Source URL: https://docs.bullmq.io/guide/jobs/deduplication

# 중복 제거

BullMQ의 중복 제거(Deduplication)는 특정 식별자를 기준으로 작업 실행을 지연시키고 중복을 제거하는 프로세스입니다. 지정된 기간 동안, 또는 특정 작업이 완료되거나 실패할 때까지 동일한 식별자를 가진 새 작업이 큐에 추가되지 않도록 보장합니다. 대신 이러한 시도는 deduplicated 이벤트를 트리거합니다.

## Simple 모드

Simple 모드는 작업이 완료되거나 실패할 때까지 중복 제거 기간을 연장합니다. 즉, 작업이 미완료 상태(성공도 실패도 아님)로 남아 있는 동안에는 동일한 deduplication ID를 가진 후속 작업이 모두 무시됩니다.

```typescript
// Add a job that will be deduplicated as this record is not finished (completed or failed).
await myQueue.add(
  'house',
  { color: 'white' },
  { deduplication: { id: 'customValue' } },
);
```

이 작업이 completed 또는 failed 상태로 이동하지 않은 동안에는 동일한 **deduplication id**로 추가되는 다음 작업들이 무시되며, QueueEvent 클래스에 의해 *deduplicated* 이벤트가 트리거됩니다.

이 모드는 실행 시간이 긴 작업이나, 해결되기 전까지 중복되면 안 되는 작업에 특히 유용합니다. 예를 들어 파일 업로드 처리나, 초기 시도가 아직 진행 중일 때 반복 실행되면 안 되는 중요한 업데이트 작업이 이에 해당합니다.

## Throttle 모드

Throttle 모드에서는 작업 생성 시 지연 시간(TTL, Time to Live)을 부여하는 방식으로 중복 제거가 동작합니다. 이 지연 기간 동안 동일한 작업(고유 deduplication ID로 식별됨)이 추가되면 무시됩니다. 이를 통해 동일 작업의 다중 인스턴스로 큐가 과부하되는 것을 방지하고, 처리 시간과 리소스 활용을 최적화할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be deduplicated for 5 seconds.
await myQueue.add(
  'house',
  { color: 'white' },
  { deduplication: { id: 'customValue', ttl: 5000 } },
);
```

이 예시에서는 중복 제거 파라미터(id와 ttl)를 사용해 house painting 작업을 추가한 뒤, 5초 이내에 동일한 deduplication ID `customValue`로 추가되는 후속 작업은 모두 무시됩니다. 이는 여러 사용자나 프로세스가 같은 작업을 빠르게 반복 요청하는 상황에서 유용합니다.

## Debounce 모드

Debounce 모드는 작업 생성 시 지연을 주고, 동일한 TTL을 제공하며, `extend`와 `replace` 옵션을 모두 true로 설정해 구현할 수 있습니다. Debounce가 성립되는 이유는, 이 지연(및 TTL) 기간 동안 동일한 deduplication ID를 가진 다른 작업이 추가되면 이전 작업을 새 작업으로 교체하고 TTL도 재설정하기 때문입니다. 그 결과 가장 최신 작업만 유지됩니다. 이 메커니즘은 큐가 중복 작업으로 넘치는 것을 막으면서 최신 작업 데이터는 유지합니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const worker = new Worker('Paint', async () => {});

worker.once('completed', job => {
  // only one instance is completed and
  // 9 additions were ignored
  console.log(job.data.color); // `white 10`
});

// Add 10 jobs with deduplication option in debounce mode.
for (let i = 1; i < 11; i++) {
  await myQueue.add(
    'house1',
    { color: `white ${i}` },
    {
      deduplication: {
        id: 'customValue',
        ttl: 5000,
        extend: true,
        replace: true,
      },
      delay: 5000,
    },
  );
}
```

이 예시에서는 중복 제거 파라미터(id, ttl, replace)와 5초 지연으로 house painting 작업을 추가한 뒤, 5초 이내에 동일한 deduplication 옵션으로 들어오는 후속 작업이 이전 작업 정보를 대체합니다. 이는 여러 사용자나 프로세스가 서로 다른 payload로 같은 작업을 빠르게 반복 트리거하는 상황에서 유용하며, 작업 처리 시 마지막으로 업데이트된 데이터를 사용할 수 있습니다.

deduplication id는 반드시 해당 작업을 대표할 수 있는 값으로 제공해야 합니다. 이 식별자는 작업 전체 데이터 또는 일부 속성을 해시해 만들 수 있습니다.

{% hint style="warning" %}
수동 삭제를 수행하면 deduplication이 비활성화됩니다. 예를 들어 *job.remove* 메서드를 호출하는 경우입니다.
{% endhint %}

## Deduplicated 이벤트

**deduplicated** 이벤트는 Simple 모드, Throttle 모드, Debounce 모드에서 deduplication에 의해 작업이 중복 제거(무시 또는 교체)될 때마다 발생합니다. 이 이벤트를 통해 중복 제거 동작을 모니터링하고, 필요 시 발생 로그를 남기거나 사용자에게 요청이 무시되었음을 알리는 등의 조치를 취할 수 있습니다.

### Deduplicated 이벤트 수신하기

**deduplicated** 이벤트를 수신하려면 BullMQ의 `QueueEvents` 클래스를 사용하세요:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('myQueue');

queueEvents.on(
  'deduplicated',
  ({ jobId, deduplicationId, deduplicatedJobId }, id) => {
    console.log(`Job ${deduplicatedJobId} was deduplicated due to existing job ${jobId}
  with deduplication ID ${deduplicationId}`);
  },
);
```

이 예시에서:

* `jobId`: 큐에 유지될 작업의 ID
* `deduplicationId`: deduplication을 유발한 deduplication ID
* `deduplicatedJobId`: deduplicated(무시 또는 교체)된 작업의 ID

## Deduplication Job ID 가져오기

deduplicated 상태를 시작한 작업의 id를 알아야 한다면 **getDeduplicationJobId** 메서드를 호출하면 됩니다.

```typescript
const jobId = await myQueue.getDeduplicationJobId('customValue');
```

## Deduplication Key 제거하기

ttl이 끝나기 전이나 작업 완료 전에 deduplication을 중지해야 한다면 **queue.removeDeduplicationKey** 메서드를 호출하면 됩니다.

```typescript
await myQueue.removeDeduplicationKey('customValue');
```

또는 deduplication을 유발한 특정 작업일 때만 deduplication을 중지하고 싶다면

```typescript
const isDeduplicatedKeyRemoved = await job.removeDeduplicationKey();
```

## 더 읽어보기:

* 💡 [Add Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#add)
* 💡 [Queue Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removededuplicationkey)
* 💡 [Job Remove Deduplication Key API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#removededuplicationkey)
* 💡 [Deduplication Patterns](https://docs.bullmq.io/patterns/deduplication)

