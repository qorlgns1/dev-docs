---
title: '더 읽어보기:'
description: '원본 URL: https://docs.bullmq.io/guide/queues'
---

원본 URL: https://docs.bullmq.io/guide/queues

# 큐

큐(Queue)는 처리되기를 기다리는 작업(job) 목록에 불과합니다. 작업은 큐를 메시지 브로커로 사용할 수 있을 만큼 작은 메시지 형태일 수도 있고, 오래 실행되는 더 큰 작업일 수도 있습니다.

큐는 `Queue` 클래스로 제어합니다. BullMQ의 모든 클래스와 마찬가지로, 이 클래스는 큐를 제어할 수 있게 해 주는 몇 가지 메서드만 가진 경량 클래스입니다.

```typescript
const queue = new Queue('Cars');
```

{% hint style="info" %}
큐에서 사용할 Redis 세부 정보를 전달하는 방법은 [Connections](https://docs.bullmq.io/guide/connections)를 참고하세요.
{% endhint %}

Queue를 인스턴스화하면 BullMQ는 작은 "meta-key"를 *upsert*만 수행하므로, 큐가 이미 존재했다면 그대로 가져와서 작업을 계속 추가할 수 있습니다.

가장 중요한 메서드는 아마 [***add***](https://api.docs.bullmq.io/classes/v5.Queue.html#add) 메서드일 것입니다. 이 메서드를 사용하면 다양한 방식으로 큐에 작업을 추가할 수 있습니다.

```typescript
await queue.add('paint', { color: 'red' });
```

위 코드는 페이로드가 `{ color: 'red' }`인 *paint*라는 이름의 작업을 큐에 추가합니다. 이 작업은 이제 Redis에 저장되어, 워커가 가져가 처리하기를 기다리게 됩니다. 작업을 추가할 때 워커가 실행 중이 아닐 수도 있지만, 워커 하나라도 큐에 연결되는 즉시 해당 작업을 가져가 처리합니다.

작업을 추가할 때 옵션 객체를 지정할 수도 있습니다. 이 옵션 객체는 추가된 작업의 동작을 크게 바꿀 수 있습니다. 예를 들어 지연된 작업을 추가할 수 있습니다.

```typescript
await queue.add('paint', { color: 'blue' }, { delay: 5000 });
```

이제 이 작업은 처리되기 전에 **최소** 5초를 기다립니다.

{% hint style="danger" %}
BullMQ 2.0 이전에는 지연 작업이 동작하려면 인프라 어딘가에 최소 하나의 `QueueScheduler`가 필요합니다. 자세한 내용은 [여기](https://docs.bullmq.io/guide/queuescheduler)를 읽어보세요.

BullMQ 2.0부터는 `QueueScheduler`가 더 이상 필요하지 않습니다.
{% endhint %}

이 외에도 우선순위, backoff 설정, lifo 동작, 완료 시 제거 정책 등 다양한 옵션이 있습니다. 이러한 옵션에 대한 자세한 내용은 이 가이드의 나머지 부분을 확인하세요.

## 더 읽어보기:

* 💡 [Queue API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html)

