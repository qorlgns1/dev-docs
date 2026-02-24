---
title: '반복 전략'
description: 'BullMQ에는 반복 가능 작업을 생성하기 위한 두 가지 사전 정의 전략이 있습니다. ‘every’ 전략은 간단하며, 초 단위로 측정된 특정 간격마다 작업이 반복되도록 예약할 수 있습니다. 더 복잡한 ‘cron’ 전략은 cron-parser에서 정의한 cron 표현식을...'
---

Source URL: https://docs.bullmq.io/guide/job-schedulers/repeat-strategies

# 반복 전략

BullMQ에는 반복 가능 작업을 생성하기 위한 두 가지 사전 정의 전략이 있습니다. ‘every’ 전략은 간단하며, 초 단위로 측정된 특정 간격마다 작업이 반복되도록 예약할 수 있습니다. 더 복잡한 ‘cron’ 전략은 [cron-parser](https://www.npmjs.com/package/cron-parser)에서 정의한 cron 표현식을 사용해 정교한 패턴으로 작업을 예약합니다. 또한 BullMQ는 사용자 정의 전략도 지원하므로, 작업 간격을 설정하는 자체 로직을 유연하게 정의할 수 있습니다.

### "Every" 전략

every 전략은 특정 간격으로 반복 작업을 단순히 생성하고 싶을 때 사용합니다:

```typescript
const { Queue, Worker } = require('bullmq');

const connection = {
  host: 'localhost',
  port: 6379,
};

const myQueue = new Queue('my-repeatable-jobs', { connection });

// Upserting a repeatable job in the queue
await myQueue.upsertJobScheduler(
  'repeat-every-10s',
  {
    every: 10000, // Job will repeat every 10000 milliseconds (10 seconds)
  },
  {
    name: 'every-job',
    data: { jobData: 'data' },
    opts: {}, // Optional additional job options
  },
);

// Worker to process the jobs
const worker = new Worker(
  'my-repeatable-jobs',
  async job => {
    console.log(`Processing job ${job.id} with data: ${job.data.jobData}`);
  },
  { connection },
);
```

### "Cron" 전략

BullMQ의 “cron” 전략은 [cron-parser](https://www.npmjs.com/package/cron-parser) 라이브러리를 활용해 cron 표현식으로 작업을 더 구체적으로 예약합니다. 이 방식은 자동 보고서나 유지보수 작업처럼 정확한 시각 또는 간격에 실행되어야 하는 작업에 적합합니다.

아래는 cron-parser에서 지원하는 cron 표현식 형식입니다:

```
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    │
│    │    │    │    │    └ day of week (0 - 7, 1L - 7L, where 0 or 7 is Sunday)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31, L for the last day of the month)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, optional)
```

이 형식에는 선택적인 초(second) 필드가 포함되며, 이는 일반적인 표준 cron 스케줄에서는 보통 제공되지 않아 더 정밀한 예약이 가능합니다.

Cron 표현식은 시간대 차이와 일광 절약 시간 전환을 매끄럽게 처리할 수 있어, 로컬 시간에 의존하는 작업에 매우 유용합니다. 또한 특정 요일이나 월의 마지막 날 같은 조건을 나타내는 특수 문자를 사용할 수 있어 월간 및 주간 작업에 유연성을 제공합니다.

Cron 표현식이 처음이라면, [Wikipedia](https://en.wikipedia.org/wiki/Cron)는 사용법을 익히기 좋은 훌륭한 시작점입니다.

다음은 월요일부터 금요일까지 오전 9:00에 실행되도록 작업을 설정하는 예시입니다:

```typescript
const { Queue, Worker } = require('bullmq');

const connection = {
  host: 'localhost',
  port: 6379,
};

const myQueue = new Queue('my-cron-jobs', { connection });

// Upserting a job with a cron expression
await myQueue.upsertJobScheduler(
  'weekday-morning-job',
  {
    pattern: '0 0 9 * * 1-5', // Runs at 9:00 AM every Monday to Friday
  },
  {
    name: 'cron-job',
    data: { jobData: 'morning data' },
    opts: {}, // Optional additional job options
  },
);

// Worker to process the jobs
const worker = new Worker(
  'my-cron-jobs',
  async job => {
    console.log(
      `Processing job ${job.id} at ${new Date()} with data: ${
        job.data.jobData
      }`,
    );
  },
  { connection },
);
```

### 사용자 정의 전략

반복 가능 작업을 예약하기 위해 다른 전략을 정의할 수 있습니다. 핵심 아이디어는 반복 전략이 패턴과 최신 작업의 밀리초 값을 기반으로 다음에 원하는 타임스탬프를 반환하는 것입니다. 아래 예시에서는 사용하지 않지만, 원한다면 현재 작업 이름에 따라 반복 전략의 동작을 다르게 구성할 수도 있습니다. 다만 하나의 큐에는 **오직** **하나의** repeatStrategy만 정의할 수 있습니다.

예를 들어 [RRULE](https://jkbrzt.github.io/rrule/)용 사용자 정의 전략을 다음과 같이 만들 수 있습니다:

```typescript
import { Queue, Worker } from 'bullmq';
import { rrulestr } from 'rrule';

const settings = {
  repeatStrategy: (millis: number, opts: RepeatOptions, _jobName: string) => {
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

const myQueue = new Queue('Paint', { settings });

// Repeat job every 10 seconds
await myQueue.upsertJobScheduler(
  'collibris',
  {
    pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=10;WKST=MO',
  },
  {
    data: { color: 'green' },
  },
);

// Repeat job every 20 seconds
await myQueue.upsertJobScheduler(
  'pingeons',
  {
    pattern: 'RRULE:FREQ=SECONDLY;INTERVAL=20;WKST=MO',
  },
  {
    data: { color: 'gray' },
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

{% hint style="danger" %}
이미 눈치챘을 수 있듯이, repeat strategy 설정은 **Queue**와 **Worker** 클래스 **모두에** 제공되어야 합니다. 그 이유는 작업을 처음 Queue에 추가할 때 다음 반복 시점을 계산해야 하기 때문입니다. 이후에는 Worker가 이를 이어받아 Worker에 구성된 설정을 사용합니다.
{% endhint %}

