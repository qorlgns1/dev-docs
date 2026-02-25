---
title: '이벤트 루프 차단 | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 작동합니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block

# 이벤트 루프 차단 | Next.js용 Sentry

이 통합은 Node.js 런타임에서만 작동합니다.

*가져오기 이름: `@sentry/node-native`의 `eventLoopBlockIntegration`*

`eventLoopBlockIntegration`은 Node.js 애플리케이션의 모든 스레드에서 이벤트 루프 차단을 모니터링하는 데 사용할 수 있습니다. 차단이 감지되면 스택 트레이스가 자동으로 수집됩니다.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#installation)

```bash
npm install @sentry/node-native
```

## [사용법](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#usage)

Node.js `--import` 플래그를 통해 애플리케이션을 계측하면, Sentry가 시작되고 이 계측이 모든 워커 스레드에 자동으로 적용됩니다.

`instrument.mjs`

```javascript
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "__YOUR_DSN__",
  // Monitor event loop blocking for more than 500ms (stack traces automatically captured)
  integrations: [eventLoopBlockIntegration({ threshold: 500 })],
});
```

`app.mjs`

```javascript
import { Worker } from "worker_threads";

const worker = new Worker(new URL("./worker.mjs", import.meta.url));

// This main thread will be monitored for blocked event loops
```

`worker.mjs`

```javascript
// This worker thread will also be monitored for blocked event loops too
```

애플리케이션을 시작합니다:

```bash
node --import instrument.mjs app.mjs
```

스레드가 구성된 임계값보다 오래 차단되면, 모든 스레드의 스택 트레이스가 자동으로 수집되어 Sentry로 전송됩니다.

## [구성 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#configuration-options)

동작을 사용자 지정하기 위해 `eventLoopBlockIntegration`에 구성 객체를 전달할 수 있습니다:

```typescript
interface ThreadBlockedIntegrationOptions {
  /**
   * Threshold in milliseconds to trigger an event.
   *
   * Defaults to 1000ms.
   */
  threshold: number;
  /**
   * Maximum number of blocked events to send per clock hour.
   *
   * Defaults to 1.
   */
  maxEventsPerHour: number;
  /**
   * Tags to include with blocked events.
   */
  staticTags: { [key: string]: Primitive };
}
```

## [구성 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#example-configuration)

```javascript
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "__YOUR_DSN__",
  integrations: [
    eventLoopBlockIntegration({
      threshold: 500, // Trigger after 500ms of blocking (stack traces automatically captured)
      maxEventsPerHour: 5, // Maximum 5 events per hour
      staticTags: {
        component: "main-thread",
        environment: "production",
      },
    }),
  ],
});
```

