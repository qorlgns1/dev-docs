---
title: '큐 계측 | Sentry for Next.js'
description: '메시징 큐에 대한 성능 데이터를 확보하려면 큐 프로듀서와 컨슈머 주변에 커스텀 span 및 transaction을 계측해야 합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/queues-module

# 큐 계측 | Sentry for Next.js

메시징 큐에 대한 성능 데이터를 확보하려면 큐 프로듀서와 컨슈머 주변에 커스텀 span 및 transaction을 계측해야 합니다.

## [프로듀서 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/queues-module.md#producer-instrumentation)

성능 메트릭 수집을 시작하려면 `Sentry.startSpan` 함수를 사용해 큐 프로듀서 이벤트를 감싸세요. span `op`는 반드시 `queue.publish`로 설정해야 합니다. 큐 메트릭으로 프로듀서 span을 보강하려면 다음 속성을 포함하세요:

| 속성                          | 유형   | 설명                           |
| ----------------------------- | ------ | ------------------------------ |
| `messaging.message.id`        | string | 메시지 식별자                  |
| `messaging.destination.name`  | string | 큐 또는 토픽 이름              |
| `messaging.message.body.size` | int    | 메시지 본문의 크기(바이트 단위) |

메시지가 수신되었을 때 컨슈머가 trace를 이어갈 수 있도록, `spanToTraceHeader`와 `spanToBaggageHeader`를 사용해 메시지에 trace header도 반드시 포함해야 합니다.

`queue.publish` span이 프로듀서 span으로 인식되려면 상위 span의 자식으로 존재해야 합니다. 아직 상위 프로듀서 span이 없다면 `Sentry.startSpan`으로 새로 시작할 수 있습니다.

`my-queue.js`

```javascript
app.post("/publish", async (req, res) => {
  // Route handler automatically instruments a parent span
  await Sentry.startSpan(
    {
      name: "queue_producer",
      op: "queue.publish",
      attributes: {
        "messaging.message.id": messageId,
        "messaging.destination.name": "messages",
        "messaging.message.body.size": messageBodySize,
      },
    },
    async () => {
      const { "sentry-trace": sentryTrace, baggage: sentryBaggage } =
        Sentry.getTraceData();
      await redisClient.lPush(
        "messages",
        JSON.stringify({
          sentryTrace,
          sentryBaggage,
          timestamp: Date.now(),
          messageId,
        }),
      );
    },
  );
});
```

## [컨슈머 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/queues-module.md#consumer-instrumentation)

성능 메트릭 수집을 시작하려면 `Sentry.startSpan` 함수를 사용해 큐 컨슈머를 감싸세요. span `op`는 반드시 `queue.process`로 설정해야 합니다. 큐 메트릭으로 컨슈머 span을 보강하려면 다음 속성을 포함하세요:

| 속성                                | 유형   | 설명                                                                 |
| ----------------------------------- | ------ | -------------------------------------------------------------------- |
| `messaging.message.id`              | string | 메시지 식별자                                                        |
| `messaging.destination.name`        | string | 큐 또는 토픽 이름                                                    |
| `messaging.message.body.size`       | number | 메시지 본문의 크기(바이트 단위)                                      |
| `messaging.message.retry.count`     | number | 메시지 처리 시도 횟수                                                |
| `messaging.message.receive.latency` | number | 메시지가 큐에서 처리를 기다린 시간(밀리초)                           |

`Sentry.continueTrace`를 사용해 컨슈머 span을 연결된 프로듀서 span과 이어주고, `setStatus`로 메시지 trace를 성공 또는 실패로 표시하세요.

`queue.process` span이 컨슈머 span으로 인식되려면 상위 span의 자식으로 존재해야 합니다. 상위 span이 없다면 `Sentry.startSpan`을 사용해 컨슈머 span을 감싸는 상위 span을 만들 수 있습니다.

`my-consumer.js`

```javascript
const message = JSON.parse(await redisClient.lPop(QUEUE_KEY));
const latency = Date.now() - message.timestamp;

Sentry.continueTrace(
    { sentryTrace: message.sentryTrace, baggage: message.sentryBaggage },
    () => {
        Sentry.startSpan({
                name: 'queue_consumer_transaction',
            },
            (parent) => {
                Sentry.startSpan({
                    name: 'queue_consumer',
                    op: 'queue.process',
                    attributes: {
                        'messaging.message.id': message.messageId,
                        'messaging.destination.name': 'messages',
                        'messaging.message.body.size': message.messageBodySize,
                        'messaging.message.receive.latency': latency,
                        'messaging.message.retry.count': 0,
                    }
                }, (span) => {
                    ... // Continue message processing
                    parent.setStatus({code: 1, message: 'ok'});
                });
            },
        ),
    },
)
```

