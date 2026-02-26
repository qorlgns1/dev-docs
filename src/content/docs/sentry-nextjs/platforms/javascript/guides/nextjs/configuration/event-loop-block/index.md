---
title: 'Event Loop Block 감지 | Next.js용 Sentry'
description: 'Event Loop Block 감지는 Node.js 메인 스레드의 event loop가 지정된 임계값보다 오래 블로킹될 때를 모니터링합니다. Node SDK는 이러한 이벤트를 자동으로 수집된 스택 트레이스와 함께 Sentry에 보고하여 블로킹 코드를 식별할 수 있도록 ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block

# Event Loop Block 감지 | Next.js용 Sentry

Event Loop Block 감지는 Node.js 메인 스레드의 event loop가 지정된 임계값보다 오래 블로킹될 때를 모니터링합니다. Node SDK는 이러한 이벤트를 자동으로 수집된 스택 트레이스와 함께 Sentry에 보고하여 블로킹 코드를 식별할 수 있도록 돕습니다.

이 기능은 현재 Beta입니다. Beta 기능은 아직 개발 중이므로 버그가 있을 수 있습니다. 아이러니하다는 점은 저희도 알고 있습니다.

Event loop block 감지는 [Node.js clusters](https://nodejs.org/api/cluster.html)에서는 지원되지 않습니다.

## [Event Loop Block 통합 (권장)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#event-loop-block-integration-recommended)

최상의 성능과 포괄적인 모니터링을 위해 `@sentry/node-native` 패키지의 [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md) 사용을 권장합니다. 블로킹이 감지되면 스택 트레이스가 자동으로 수집됩니다. 이 통합은 Node.js 애플리케이션의 모든 스레드를 모니터링할 수 있으며, 더 이상 사용이 권장되지 않는 ANR 통합보다 더 나은 성능을 제공합니다.

```javascript
import * as Sentry from "@sentry/node";
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [eventLoopBlockIntegration({ threshold: 1000 })],
});
```

자세한 사용 방법과 구성 옵션은 [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md) 문서를 참고하세요.

## [더 이상 사용 권장되지 않는 Application Not Responding (ANR) 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#deprecated-application-not-responding-anr-integration)

**Deprecated**: `anrIntegration`은 더 이상 사용이 권장되지 않습니다. 더 나은 성능과 더 포괄적인 모니터링을 위해 대신 [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)을 사용하세요.

*(버전 7.91.0 이상에서 사용 가능)*

레거시 ANR 통합은 여전히 사용할 수 있지만 더 이상 권장되지 않습니다. 현재 사용 중이라면 새로운 `eventLoopBlockIntegration`으로 마이그레이션하는 것을 권장합니다.

ANR 감지에는 Node 16 이상이 필요하며 Node.js 런타임에서만 사용할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.anrIntegration({ captureStackTrace: true })],
});
```

- [레거시 ANR 구성 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#legacy-anr-configuration-options)

더 이상 권장되지 않는 ANR 통합은 다음 구성 옵션을 지원합니다:

```ts
interface Options {
  /**
   * Interval to send heartbeat messages to the ANR thread.
   *
   * Defaults to 50ms.
   */
  pollInterval: number;
  /**
   * Threshold in milliseconds to trigger an ANR event.
   *
   * Defaults to 5000ms.
   */
  anrThreshold: number;
  /**
   * Whether to capture a stack trace when the ANR event is triggered.
   *
   * Defaults to `false`.
   *
   * This uses the node debugger which enables the inspector API.
   */
  captureStackTrace: boolean;
}
```

- [레거시 ANR 구현 및 오버헤드](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#legacy-anr-implementation-and-overhead)

레거시 Node SDK의 ANR 감지는 워커 스레드를 사용해 메인 앱 스레드의 event loop를 모니터링합니다. 메인 앱 스레드는 50ms마다 ANR 워커 스레드에 heartbeat 메시지를 보냅니다. ANR 워커가 5초 동안 heartbeat 메시지를 받지 못하면 ANR 이벤트를 트리거합니다. `captureStackTrace` 옵션이 활성화되어 있으면 ANR 워커는 `inspector` 모듈을 사용해 [v8 inspector API](https://nodejs.org/api/inspector.html)를 통해 스택 트레이스를 수집합니다.

ANR 이벤트가 한 번 보고되면, 이후 중복 이벤트를 방지하기 위해 ANR 워커 스레드는 종료되며 메인 앱 스레드는 평소처럼 계속 실행됩니다.

Node.js ANR 추적으로 인한 오버헤드는 최소 수준이어야 합니다. ANR이 감지되지 않은 경우, 메인 앱 스레드에서의 유일한 오버헤드는 기본적으로 50ms마다 IPC를 통해 ANR 워커를 폴링하는 것입니다. ANR 워커 스레드는 이 폴링을 추적하기 위해 약 10~20MB의 RAM을 사용합니다. ANR이 감지되면 스택 트레이스 프레임을 수집하기 위해 메인 스레드가 디버거에서 잠시 일시 중지됩니다. 이 시점에는 event loop가 이미 수 초 동안 블로킹된 상태이므로 디버깅 오버헤드는 무시할 수 있습니다.

