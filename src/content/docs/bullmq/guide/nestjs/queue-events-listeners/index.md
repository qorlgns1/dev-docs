---
title: 'Queue 이벤트 리스너'
description: 'QueueEvents 인스턴스를 등록하려면  데코레이터를 사용해야 합니다:'
---

Source URL: https://docs.bullmq.io/guide/nestjs/queue-events-listeners

# Queue 이벤트 리스너

QueueEvents 인스턴스를 등록하려면 **`QueueEventsListener`** 데코레이터를 사용해야 합니다:

```typescript
import {
  QueueEventsListener,
  QueueEventsHost,
  OnQueueEvent,
} from '@nestjs/bullmq';

@QueueEventsListener('queueName')
export class TestQueueEvents extends QueueEventsHost {
  @OnQueueEvent('completed')
  onCompleted({
    jobId,
  }: {
    jobId: string;
    returnvalue: string;
    prev?: string;
  }) {
    // do some stuff
  }
}
```

그런 다음 이를 provider로 등록합니다:

```typescript
@Module({
  imports: [
    BullModule.registerQueue({
      name: 'queueName',
      connection: {
        host: '0.0.0.0',
        port: 6380,
      },
    }),
  ],
  providers: [TestQueueEvents],
})
export class AppModule {}
```

## 더 읽어보기:

* 💡 [Queues Technique](https://docs.nestjs.com/techniques/queues)
* 💡 [Register Queue API Reference](https://nestjs.bullmq.pro/classes/BullModule.html#registerQueue)
* 💡 [Queue Events Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)

