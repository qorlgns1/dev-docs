---
title: '텔레메트리'
description: 'BullMQ 오픈 소스 에디션에서 텔레메트리를 지원하는 것과 같은 방식으로, BullMQ Pro에서도 텔레메트리를 지원합니다. 기본적으로 동일하게 동작하며, 실제로 Pro 버전에서도 BullMQ에서 사용 가능한 동일한 통합을 그대로 사용할 수 있습니다. 따라서 이를 활...'
---

Source URL: https://docs.bullmq.io/bullmq-pro/telemetry

# 텔레메트리

BullMQ 오픈 소스 에디션에서 텔레메트리를 지원하는 것과 같은 방식으로, BullMQ Pro에서도 텔레메트리를 지원합니다. 기본적으로 동일하게 동작하며, 실제로 Pro 버전에서도 BullMQ에서 사용 가능한 동일한 통합을 그대로 사용할 수 있습니다. 따라서 이를 활성화하려면 다음과 같이 하면 됩니다.

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';
import { BullMQOtel } from 'bullmq-otel';

// Initialize a Pro queue using BullMQ-Otel
const queue = new QueuePro('myProQueue', {
  connection,
  telemetry: new BullMQOtel('guide'),
});

await queue.add(
  'myJob',
  { data: 'myData' },
  {
    attempts: 2,
    backoff: 1000,
    group: {
      id: 'myGroupId',
    },
  },
);
```

Worker의 경우에도 비슷한 방식으로 설정합니다:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';
import { BullMQOtel } from 'bullmq-otel';

const worker = new WorkerPro(
  'myProQueue',
  async job => {
    console.log('processing job', job.id);
  },
  {
    name: 'myWorker',
    connection,
    telemetry: new BullMQOtel('guide'),
    concurrency: 10,
    batch: { size: 10 },
  },
);
```

BullMQ 애플리케이션에 OpenTelemetry를 통합하는 방법에 대한 입문 가이드는 다음 튜토리얼을 참고하세요: <https://blog.taskforce.sh/how-to-integrate-bullmqs-telemetry-on-a-newsletters-subscription-application-2/>

