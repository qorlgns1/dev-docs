---
title: 'Web Workers | Next.js용 Sentry'
description: 'Sentry의 Browser SDK는 Web Workers API를 지원합니다. SDK는 여러 방식으로 사용할 수 있지만, 워커의 처리되지 않은 오류를 자동으로 수집하려면 메인 스레드에서 초기화하는 것을 권장합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers

# Web Workers | Next.js용 Sentry

Sentry의 Browser SDK는 [Web Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)를 지원합니다. SDK는 여러 방식으로 사용할 수 있지만, 워커의 처리되지 않은 오류를 자동으로 수집하려면 메인 스레드에서 초기화하는 것을 권장합니다.

## [권장 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#recommended-setup)

*지원 시작 버전* : 9.40.0

Web Workers의 처리되지 않은 오류를 수집하려면, 메인 스레드에서 실행되는 애플리케이션 코드에서 Sentry를 초기화하고 SDK에 웹 워커를 알려주세요.

`index.js`

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
});

const worker = new Worker("worker.js");

// Add the integration before listening to worker messages
Sentry.addIntegration(Sentry.webWorkerIntegration({ worker }));

worker.onmessage = (event) => {
  // ...
};
```

그다음 워커와 SDK 사이의 통신을 설정합니다.

`worker.js`

```javascript
import * as Sentry from "@sentry/browser";

// Call this before posting any message
Sentry.registerWebWorker({ self });

// Errors from `onmessage` callback of `worker.js`
// will be captured automatically.
self.postMessage("Worker ready!");
self.onmessage = (event) => {
  // ...
};
```

##### 순서가 중요합니다

메시지 수신을 시작하기 전에 메인 스레드와 워커 모두에서 Sentry를 초기화해야 합니다. Sentry SDK는 워커에서 메인 스레드로 메시지를 전송하므로, Sentry 초기화 전에 수신을 시작하면 해당 메시지가 리스너에 나타나고 수동으로 처리해야 합니다.

- [여러 워커](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#multiple-workers)

`sentryWebWorkerIntegration`을 사용하면 여러 워커를 등록할 수 있습니다. 통합을 초기화할 때 등록하거나, 나중에 추가할 수도 있습니다. 이는 애플리케이션 생명주기에서 서로 다른 시점에 초기화되는 워커가 있을 때 유용합니다.

`index.js`

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
});

const worker1 = new Worker("worker.js");
const worker2 = new Worker("worker2.js");

// Multiple workers can be added directly:
const webWorkerIntegration = Sentry.webWorkerIntegration({
  worker: [worker1, worker2],
});
Sentry.addIntegration(webWorkerIntegration);

// or later on:
const worker3 = new Worker("worker3.js");

webWorkerIntegration.addWorker(worker3);
```

##### 유의 사항

* 모든 워커는 `Sentry.registerWebWorker({ self })`를 호출해 SDK에 자신을 등록해야 합니다.
* `Sentry.webWorkerIntegration()`을 여러 번 호출하지 마세요! 예기치 않은 동작이 발생할 수 있습니다.

## [오류 수동 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#manually-capturing-errors)

Web Workers 내부에서 `Sentry.captureMessage` 또는 `Sentry.captureException`을 통해 오류나 메시지를 수동으로 수집하려면, 워커에서 SDK를 import하고 초기화할 수도 있습니다.

`worker.js`

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
});

self.onmessage = (message) => {
  // This message will be captured

  Sentry.captureMessage("Message received");

  // This error will also be captured.
  throw new Error();
};
```

워커에서 SDK를 초기화하면 메인 스레드에서 실행 중인 SDK와 **완전히 분리**된다는 점에 유의하세요. 즉, 한쪽에서 설정한 사용자, 태그, 트레이스 또는 스코프 데이터는 다른 쪽과 공유되지 않습니다.

경우에 따라 이 방식이 더 적합할 수 있습니다. 예를 들어, 임의의 애플리케이션에서 사용되는 워커를 개발하는 경우가 그렇습니다. 반대로 워커가 애플리케이션의 일부일 뿐이라면, 일반적으로 [메인 스레드의 SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#recommended-setup)를 사용하는 것이 좋습니다.

##### 유의 사항

워커에서 SDK를 초기화하는 경우, 워커 등록에 `Sentry.webWorkerIntegration`을 사용하지 마세요. 마찬가지로 워커 내부에서 `Sentry.registerWebWorker`도 사용하지 마세요. 두 메서드 모두 [메인 스레드](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#recommended-setup)의 SDK를 사용할 때만 사용해야 합니다.

- [통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#integrations)

웹 워커 내부에서 기본값이 아닌 통합을 사용하면 예상대로 동작하지 않을 수 있습니다. 하지만 메인 스레드 SDK에서 활성화한 기본값이 아닌 통합은 영향을 받지 않으며 예상대로 동작합니다. 여기에는 Session Replay도 포함됩니다.

## [소스 맵](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#source-maps)

웹 워커의 오류가 원본 소스 코드에 올바르게 매핑되도록 하려면 소스 맵을 Sentry에 제공해야 합니다. 메인 애플리케이션 코드에 대해서는 이미 소스 맵을 Sentry에 제공하고 있을 가능성이 높지만, 워커에 대해서는 일부 조정이 필요할 수 있습니다.

중요하게도, 번들러가 워커 번들에 대해서도 **소스 맵을 생성**하도록 설정되어 있는지 확인하세요.

- [Vite](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md#vite)

워커를 빌드할 때 Vite를 사용하는 경우, 워커 빌드는 메인 코드 빌드와 동일한 플러그인을 사용하지 않는다는 점에 유의하세요. 따라서 최상위 `plugins` 배열과 별도로 워커 빌드에도 Sentry의 Vite 플러그인을 추가해야 합니다.

`vite.config.mjs`

```javascript
const sentryPlugin = sentryVitePlugin({
  org: "sentry-sdks",
  project: "javascript",
});

export default defineConfig({
  build: {

    // This enables source maps for main and worker bundles
    sourcemap: "hidden",

  },

  // Vite plugin for main bundle

  plugins: [sentryPlugin],

  worker: {

    // Vite plugin for worker bundle
    plugins: () => [...sentryPlugin],

  },
});
```

