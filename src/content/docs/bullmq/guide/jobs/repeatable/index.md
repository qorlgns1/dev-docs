---
title: 'Repeatable'
description: '원본 URL: https://docs.bullmq.io/guide/jobs/repeatable'
---

원본 URL: https://docs.bullmq.io/guide/jobs/repeatable

# Repeatable

{% hint style="danger" %}
참고: BullMQ 버전 5.16.0부터는 이 API들이 deprecated 되었으며, 반복 작업 처리를 더 일관되고 견고하게 제공하는 ["Job Schedulers"](https://docs.bullmq.io/guide/job-schedulers) 사용을 권장합니다.
{% endhint %}

**repeatable** 이라는 특별한 유형의 *meta* 작업이 있습니다. 이 작업은 큐에 한 번만 추가하더라도, 미리 정의된 스케줄에 따라 계속 반복된다는 점에서 특별합니다.

`repeat` 옵션을 설정해 작업을 추가하면 즉시 두 가지가 수행됩니다. Repeatable Job 설정을 생성하고, 해당 작업의 첫 실행을 위한 일반 지연 작업을 스케줄링합니다. 첫 실행은 "정각 기준(on the hour)"으로 스케줄됩니다. 즉, 15분마다 반복되는 작업을 4:07에 생성하면 첫 실행은 4:15, 그다음은 4:30처럼 진행됩니다.

Repeatable Job 설정은 작업 자체가 아니므로 `getJobs()` 같은 메서드에는 표시되지 않습니다. Repeatable Job 설정을 관리하려면 [`getRepeatableJobs()`](https://api.docs.bullmq.io/classes/v5.Queue.html#getrepeatablejobs) 등을 사용하세요. 이는 반복 작업이 `jobId` 고유성 평가에 참여하지 않는다는 뜻이기도 합니다. 즉, 비반복 작업이 Repeatable Job 설정과 동일한 `jobId`를 가질 수 있고, 두 Repeatable Job 설정도 반복 옵션이 다르면 같은 `jobId`를 가질 수 있습니다.

반복 작업이 처리 대상으로 선택될 때마다, 적절한 지연 시간과 함께 다음 반복 작업이 큐에 추가됩니다. 따라서 반복 작업은 특정 설정에 따라 큐에 추가되는 지연 작업일 뿐입니다.

{% hint style="info" %}
Repeatable 작업은 지연 작업일 뿐이므로, BullMQ 2.0 이전에는 작업을 올바르게 스케줄링하기 위해 `QueueScheduler` 인스턴스가 추가로 필요합니다.

하지만 BullMQ 2.0부터는 `QueueScheduler`가 더 이상 필요하지 않습니다.
{% endhint %}

반복 패턴을 지정하는 방법은 두 가지입니다. cron 표현식([cron-parser](https://www.npmjs.com/package/cron-parser)의 "unix cron w/ optional seconds" 형식 사용)을 쓰거나, 반복 간격을 밀리초 고정값으로 지정할 수 있습니다.

```typescript
import { Queue, QueueScheduler } from 'bullmq';

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint');

// Repeat job once every day at 3:15 (am)
await myQueue.add(
  'submarine',
  { color: 'yellow' },
  {
    repeat: {
      pattern: '0 15 3 * * *',
    },
  },
);

// Repeat job every 10 seconds but no more than 100 times
await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
  },
);
```

반복 작업과 관련해 중요한 고려사항이 있습니다.

* 반복 옵션이 동일하면 Bull은 같은 반복 작업을 중복 추가하지 않을 만큼 똑똑하게 동작합니다.
* 실행 중인 워커가 없을 때는, 다음에 워커가 온라인이 되더라도 반복 작업이 누적되지 않습니다.
* 반복 작업은 [`removeRepeatable`](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatable) 또는 [`removeRepeatableByKey`](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatablebykey) 메서드로 제거할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const repeat = { pattern: '*/1 * * * * *' };

const myQueue = new Queue('Paint');

const job1 = await myQueue.add('red', { foo: 'bar' }, { repeat });
const job2 = await myQueue.add('blue', { foo: 'baz' }, { repeat });

const isRemoved1 = await myQueue.removeRepeatableByKey(job1.repeatJobKey);
const isRemoved2 = await queue.removeRepeatable('blue', repeat);
```

모든 반복 작업은 작업 자체의 메타데이터를 담는 repeatable job key를 가집니다. 현재 큐의 모든 반복 작업은 [`getRepeatableJobs`](https://api.docs.bullmq.io/classes/v5.Queue.html#getrepeatablejobs) 호출로 조회할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

const repeatableJobs = await myQueue.getRepeatableJobs();
```

표준 `jobId` 옵션은 일반 작업과 동일하게 동작하지 않습니다. 반복 작업은 *delayed* 작업이며, 현재 작업이 처리 시작되기 직전에 새 지연 작업을 생성해 반복을 구현합니다. 따라서 중복으로 간주되지 않도록 작업마다 고유 ID가 필요합니다. 이 때문에 반복 작업에서는 `jobId`가 고유 ID 그 자체가 아니라, 고유 ID를 *생성*하는 데 사용됩니다. 예를 들어 이름과 옵션이 같은 두 반복 작업을 구분하려면 서로 다른 `jobId`를 사용할 수 있습니다.

```typescript
import { Queue, QueueScheduler } from 'bullmq';

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint');

// Repeat job every 10 seconds but no more than 100 times
await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
    jobId: 'colibri',
  },
);

await myQueue.add(
  'bird',
  { color: 'bird' },
  {
    repeat: {
      every: 10000,
      limit: 100,
    },
    jobId: 'pigeon',
  },
);
```

### 느린 반복 작업

반복 주기가 작업 처리 시간보다 더 짧은 경우를 짚고 넘어갈 필요가 있습니다.

예를 들어 작업이 1초마다 반복되지만 실제 처리에는 5초가 걸린다고 가정해 봅시다. 앞서 설명했듯 반복 작업은 지연 작업이므로, 다음 반복 작업은 다음 작업의 처리가 시작되자마자 추가됩니다.

이 예시에서는 워커가 다음 작업을 가져오면서 반복 간격이 1초이므로 1초 지연된 다음 반복 작업도 추가합니다. 워커는 현재 작업 처리에 5초가 필요하고, 워커가 1개뿐이라면 다음 작업은 처리되기까지 5초 전체를 기다려야 합니다.

반대로 워커가 5개라면, 대부분의 경우 초당 1개라는 원하는 빈도로 반복 작업을 처리할 수 있습니다.

### Repeat Strategy

기본적으로 cron 표현식의 기본 반복 전략에는 [cron-parser](https://www.npmjs.com/package/cron-parser)를 사용합니다.

반복 작업 스케줄링에 다른 전략을 정의할 수도 있습니다. 예를 들어 RRULE용 커스텀 전략을 만들 수 있습니다.

```typescript
import { Queue, QueueScheduler, Worker } from 'bullmq';
import { rrulestr } from 'rrule';

const settings = {
  repeatStrategy: (millis, opts) => {
    const currentDate =
      opts.startDate && new Date(opts.startDate) > new Date(millis)
        ? new Date(opts.startDate)
        : new Date(millis);
    const rrule = rrulestr(opts.pattern);
    if (rrule.origOptions.count && !rrule.origOptions.dtstart) {
      throw new Error('DTSTART must be defined to use COUNT with rrule');
    }

    const next_occurrence = rrule.after(currentDate, false);
    return next_occurrence?.getTime();
  },
};

const myQueueScheduler = new QueueScheduler('Paint');
const myQueue = new Queue('Paint', { settings });

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'green' },
  {
    repeat: {
      pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=;WKST=MO',
    },
    jobId: 'colibri',
  },
);

await myQueue.add(
  'bird',
  { color: 'gray' },
  {
    repeat: {
      pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=;WKST=MO',
    },
    jobId: 'pigeon',
  },
);

const worker = new Worker(
  'Paint',
  async () => {
    doSomething();
  },
  { settings },
);
```

{% hint style="warning" %}
보시다시피 반복 전략 설정은 `Queue`와 `Worker` 클래스 모두에 제공해야 합니다. **둘 다** 필요한 이유는, 작업을 처음 `Queue`에 추가할 때 다음 반복 시점을 계산해야 하고, 그 이후에는 `Worker`가 이를 이어받아 워커 설정을 사용하기 때문입니다.
{% endhint %}

{% hint style="info" %}
반복 전략 함수는 선택적인 세 번째 파라미터 `jobName`을 전달받습니다.
{% endhint %}

### Custom Repeatable Key

기본적으로 repeatable key는 반복 옵션과 작업 이름을 기반으로 생성됩니다.

경우에 따라 반복 옵션이 같더라도 반복 작업을 구분할 수 있도록 커스텀 key를 전달하는 것이 바람직할 수 있습니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint', { connection });

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'gray' },
  {
    repeat: {
      every: 10_000,
      key: 'colibri',
    },
  },
);

// Repeat job every 10 seconds
await myQueue.add(
  'bird',
  { color: 'brown' },
  {
    repeat: {
      every: 10_000,
      key: 'eagle',
    },
  },
);
```

#### 반복 작업 옵션 업데이트

커스텀 key를 사용하면 같은 key로 새 반복 작업을 추가하는 것만으로 기존 반복 작업을 업데이트할 수 있습니다. 예를 들어 key가 "eagle"인 이전 작업의 반복 간격을 변경하려면 다음처럼 새 작업을 추가하면 됩니다.

```typescript
// Repeat job every 25 seconds instead of 10 seconds
await myQueue.add(
  'bird',
  { color: 'turquoise' },
  {
    repeat: {
      every: 25_000,
      key: 'eagle',
    },
  },
);
```

위 코드는 새로운 반복 meta 작업을 생성하지 않고, 기존 meta 작업의 간격을 10초에서 25초로 업데이트합니다. 10초 설정으로 이미 지연된 작업이 있다면, 새로운 반복 작업 설정을 사용하는 작업으로 대체됩니다.

### 더 읽어보기:

* 💡 [Repeat Strategy API Reference](https://api.docs.bullmq.io/types/v5.RepeatStrategy.html)
* 💡 [Remove Repeatable Job API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatable)
* 💡 [Remove Repeatable Job by Key API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#removerepeatablebykey)

