---
title: 'NestJs'
description: '설치 과정이 완료되면 루트 에 을 가져올 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/nestjs

# NestJs

[NestJs](https://github.com/nestjs/nest)에서 사용할 수 있는 호환 모듈이 있습니다.

```bash
npm i @nestjs/bullmq
```

설치 과정이 완료되면 루트 **`AppModule`**에 **`BullModule`**을 가져올 수 있습니다.

```typescript
import { Module } from '@nestjs/common';
import { BullModule } from '@nestjs/bullmq';

@Module({
  imports: [
    BullModule.forRoot({
      connection: {
        host: 'localhost',
        port: 6379,
      },
    }),
  ],
})
export class AppModule {}
```

큐를 등록하려면 다음과 같이 **`BullModule.registerQueue()`** 동적 모듈을 가져오세요.

```typescript
BullModule.registerQueue({
  name: 'queueName',
});
```

플로우 프로듀서를 등록하려면 다음과 같이 **`BullModule.registerFlowProducer()`** 동적 모듈을 가져오세요.

```typescript
BullModule.registerFlowProducer({
  name: 'flowProducerName',
});
```

## Processor

프로세서를 등록하려면 **`Processor`** 데코레이터를 사용해야 할 수 있습니다.

```typescript
import { Processor, WorkerHost, OnWorkerEvent } from '@nestjs/bullmq';
import { Job } from 'bullmq';

@Processor('queueName')
class TestProcessor extends WorkerHost {
  async process(job: Job<any, any, string>): Promise<any> {
    // do some stuff
  }

  @OnWorkerEvent('completed')
  onCompleted() {
    // do some stuff
  }
}
```

그런 다음 이를 provider로 등록합니다.

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
    BullModule.registerFlowProducer({
      name: 'flowProducerName',
      connection: {
        host: '0.0.0.0',
        port: 6380,
      },
    }),
  ],
  providers: [TestProcessor],
})
export class AppModule {}
```

### 더 읽어보기:

* 💡 [Queues Technique](https://docs.nestjs.com/techniques/queues)

