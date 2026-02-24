---
title: '프로듀서'
description: '원본 URL: https://docs.bullmq.io/bullmq-pro/nestjs/producers'
---

원본 URL: https://docs.bullmq.io/bullmq-pro/nestjs/producers

# 프로듀서

## 프로듀서

Job 프로듀서는 큐에 job을 추가합니다. 프로듀서는 일반적으로 애플리케이션 서비스(Nest provider)입니다. 큐에 job을 추가하려면, 먼저 다음과 같이 서비스에 큐를 주입합니다:

```typescript
import { Injectable } from '@nestjs/common';
import { QueuePro } from 'taskforcesh/bullmq-pro';
import { InjectQueue } from '@taskforcesh/nestjs-bullmq-pro';

@Injectable()
export class AudioService {
  constructor(@InjectQueue('audio') private audioQueue: QueuePro) {}
}
```

{% hint style="info" %}
`@InjectQueue()` 데코레이터는 `registerQueue()`에 제공된 이름으로 큐를 식별합니다.
{% endhint %}

이제 큐의 `add()` 메서드를 호출하여 job을 추가합니다.

```typescript
const job = await this.audioQueue.add({
  foo: 'bar',
});
```

## 플로우 프로듀서

플로우를 추가하려면, 먼저 다음과 같이 서비스에 플로우 프로듀서를 주입합니다:

```typescript
import { Injectable } from '@nestjs/common';
import { FlowProducerPro } from 'taskforcesh/bullmq-pro';
import { InjectFlowProducer } from '@taskforcesh/nestjs-bullmq-pro';

@Injectable()
export class FlowService {
  constructor(
    @InjectFlowProducer('flow') private fooFlowProducer: FlowProducerPro,
  ) {}
}
```

{% hint style="info" %}
`@InjectFlowProducer()` 데코레이터는 `registerFlowProducer()`에 제공된 이름으로 플로우 프로듀서를 식별합니다.
{% endhint %}

이제 플로우 프로듀서의 `add()` 메서드를 호출하여 플로우를 추가합니다.

```typescript
const job = await this.fooFlowProducer.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name,
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

### 더 읽어보기:

* 💡 [큐 기법](https://docs.nestjs.com/techniques/queues)
* 💡 [Inject Queue API 레퍼런스](https://nestjs.bullmq.pro/functions/InjectQueue.html)
* 💡 [Inject Flow Producer API 레퍼런스](https://nestjs.bullmq.pro/functions/InjectFlowProducer.html)
* 💡 [QueuePro API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html)
* 💡 [FlowProducerPro API 레퍼런스](https://api.bullmq.pro/classes/v7.FlowProducerPro.html)

