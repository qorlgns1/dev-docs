---
title: '프로듀서'
description: '작업 프로듀서는 큐에 작업을 추가합니다. 프로듀서는 일반적으로 애플리케이션 서비스(Nest provider)입니다. 큐에 작업을 추가하려면 먼저 다음과 같이 서비스에 큐를 주입합니다:'
---

Source URL: https://docs.bullmq.io/guide/nestjs/producers

# 프로듀서

작업 프로듀서는 큐에 작업을 추가합니다. 프로듀서는 일반적으로 애플리케이션 서비스(Nest provider)입니다. 큐에 작업을 추가하려면 먼저 다음과 같이 서비스에 큐를 주입합니다:

```typescript
import { Injectable } from '@nestjs/common';
import { InjectQueue } from '@nestjs/bullmq';
import { Queue } from 'bullmq';

@Injectable()
export class AudioService {
  constructor(@InjectQueue('audio') private audioQueue: Queue) {}
}
```

{% hint style="info" %}
**`@InjectQueue()`** 데코레이터는 **`registerQueue()`** 에서 제공한 이름으로 큐를 식별합니다.
{% endhint %}

이제 큐의 add() 메서드를 호출해 작업을 추가합니다.

```typescript
const job = await this.audioQueue.add('sample', {
  foo: 'bar',
});
```

## 플로우 프로듀서

플로우를 추가하려면 먼저 다음과 같이 서비스에 플로우 프로듀서를 주입합니다:

```typescript
import { Injectable } from '@nestjs/common';
import { InjectFlowProducer } from '@nestjs/bullmq';
import { FlowProducer } from 'bullmq';

@Injectable()
export class FlowService {
  constructor(
    @InjectFlowProducer('flow') private fooFlowProducer: FlowProducer,
  ) {}
}
```

{% hint style="info" %}
**`@InjectFlowProducer()`** 데코레이터는 **`registerFlowProducer()`** 에서 제공한 `name`으로 플로우 프로듀서를 식별합니다.
{% endhint %}

이제 플로우 프로듀서의 \`add()\`\` 메서드를 호출해 플로우를 추가합니다.

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

