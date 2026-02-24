---
title: '커스텀 이벤트 생성'
description: '원본 URL: https://docs.bullmq.io/guide/events/create-custom-events'
---

원본 URL: https://docs.bullmq.io/guide/events/create-custom-events

# 커스텀 이벤트 생성

BullMQ에서는 **QueueEventsProducer** 클래스를 사용해 범용 분산 실시간 이벤트 이미터를 생성할 수 있습니다.

컨슈머는 관심 있는 이벤트를 구독하기 위해 **QueueEvents** 클래스를 사용해야 합니다.

```typescript
const queueName = 'customQueue';
const queueEventsProducer = new QueueEventsProducer(queueName, {
  connection,
});
const queueEvents = new QueueEvents(queueName, {
  connection,
});

interface CustomListener extends QueueEventsListener {
  example: (args: { custom: string }, id: string) => void;
}
queueEvents.on<CustomListener>('example', async ({ custom }) => {
  // custom logic
});

interface CustomEventPayload {
  eventName: string;
  custom: string;
}

await queueEventsProducer.publishEvent<CustomEventPayload>({
  eventName: 'example',
  custom: 'value',
});
```

`eventName` 속성만 필수입니다.

{% hint style="warning" %}
일부 이벤트 이름은 [Queue Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueListener.html)에서 예약되어 있습니다.
{% endhint %}

## 더 읽어보기:

* 💡 [Queue Events API Reference](https://api.docs.bullmq.io/classes/v5.QueueEvents.html)
* 💡 [Queue Events Listener API Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html)
* 💡 [Queue Events Producer API Reference](https://api.docs.bullmq.io/classes/v5.QueueEventsProducer.html)

