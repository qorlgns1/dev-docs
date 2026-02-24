---
title: 'NestJs'
description: '{% hint style="info" %}'
---

Source URL: https://docs.bullmq.io/bullmq-pro/nestjs

# NestJs

[@nestjs/bullmq](https://www.npmjs.com/package/@nestjs/bullmq)를 기반으로 [NestJs](https://github.com/nestjs/nest)에서 사용할 수 있는 호환 모듈이 있습니다.

```bash
yarn add @taskforcesh/nestjs-bullmq-pro
```

{% hint style="info" %}
BullMQ-Pro는 [install](https://docs.bullmq.io/bullmq-pro/install) 섹션에서 설명한 것처럼 토큰이 필요합니다.
{% endhint %}

설치 과정이 완료되면 루트 `AppModule`에 `BullModule`을 import할 수 있습니다.

```typescript
import { Module } from '@nestjs/common';
import { BullModule } from '@taskforcesh/nestjs-bullmq-pro';

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

큐를 등록하려면 다음과 같이 `BullModule.registerQueue()` 동적 모듈을 import하세요.

```typescript
BullModule.registerQueue({
  name: 'queueName',
});
```

플로우 프로듀서를 등록하려면 다음과 같이 `BullModule.registerFlowProducer()` 동적 모듈을 import하세요.

```typescript
BullModule.registerFlowProducer({
  name: 'flowProducerName',
});
```

## 프로세서

프로세서를 등록하려면 `Processor` 데코레이터를 사용해야 할 수 있습니다.

```typescript
import {
  Processor,
  WorkerHost,
  OnWorkerEvent,
} from '@taskforcesh/nestjs-bullmq-pro';
import { JobPro } from 'taskforcesh/bullmq-pro';

@Processor('queueName')
class TestProcessor extends WorkerHost {
  async process(job: JobPro<any, any, string>): Promise<any> {
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

## 예제

작동하는 예제는 [여기](https://github.com/taskforcesh/nestjs-bullmq-pro-example)에서 확인할 수 있습니다.

### 더 읽어보기:

* 💡 [큐 기법](https://docs.nestjs.com/techniques/queues)
* 💡 [Register Queue API 레퍼런스](https://nestjs.bullmq.pro/classes/BullModule.html#registerQueue)
* 💡 [Register Flow Producer API 레퍼런스](https://nestjs.bullmq.pro/classes/BullModule.html#registerFlowProducer)
* 💡 [Worker Listener API 레퍼런스](https://api.docs.bullmq.io/interfaces/v5.WorkerListener.html)

