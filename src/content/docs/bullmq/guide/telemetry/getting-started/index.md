---
title: '시작하기'
description: '이 가이드에서는 BullMQ를 위한 로컬 텔레메트리 환경을 설정하는 방법을 보여줍니다. 이는 더 큰 애플리케이션에 통합할 때 좋은 기반이 됩니다. OpenTelemetry는 널리 지원되는 표준이므로, 애플리케이션 실행 시 생성되는 트레이스와 스팬을 시각화할 수 있는 다...'
---

Source URL: https://docs.bullmq.io/guide/telemetry/getting-started

# 시작하기

이 가이드에서는 BullMQ를 위한 로컬 텔레메트리 환경을 설정하는 방법을 보여줍니다. 이는 더 큰 애플리케이션에 통합할 때 좋은 기반이 됩니다. OpenTelemetry는 널리 지원되는 표준이므로, 애플리케이션 실행 시 생성되는 트레이스와 스팬을 시각화할 수 있는 다양한 서드파티 UI가 있습니다. 이 가이드에서는 [Jaeger](https://www.jaegertracing.io)를 사용하겠습니다.

텔레메트리를 추가하려는 동작 중인 BullMQ 프로젝트가 이미 있다고 가정하고, 먼저 프로젝트에 `bullmq-otel` 패키지를 추가해 보겠습니다:

```
npm add --save bullmq-otel
```

이 모듈은 OpenTelemetry 표준을 위한 BullMQ 텔레메트리 인터페이스의 동작 가능한 구현을 제공합니다. 기존 Queue 인스턴스와 Worker에 추가하는 작업도 매우 간단합니다:

```typescript
import { Queue } from 'bullmq'
import { BullMQOtel } from "bullmq-otel";

const queue = new Queue("myQueue", {
  connection: {
    host: "127.0.0.1",
    port: 6379,
  },
  telemetry: new BullMQOtel("simple-guide"),
});
```

```typescript
import { Worker } from "bullmq";
import { BullMQOtel } from "bullmq-otel";

const worker = new Worker(
  "myQueue",
  async (job) => {
    return 'some value'
  },
  {
    name: "myWorker",
    connection: {
      host: "127.0.0.1",
      port: 6379,
    },
    telemetry: new BullMQOtel("simple-guide"),
  }
);
```

이것만으로도 코드를 관찰하기 위한 트레이스와 스팬 생성을 시작할 수 있습니다.

