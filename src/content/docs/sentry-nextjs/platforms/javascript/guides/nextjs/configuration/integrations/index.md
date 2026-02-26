---
title: '통합 | Sentry for Next.js'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations

# 통합 | Sentry for Next.js

Sentry SDK는 통합(integration)을 사용해 널리 쓰이는 라이브러리의 기능에 연결(hook)하여, 애플리케이션을 자동으로 계측하고 별도 설정 없이도 최적의 데이터를 제공합니다.

통합은 애플리케이션에 오류 계측, 성능 계측, 그리고/또는 추가 컨텍스트 정보를 자동으로 추가합니다. 일부는 기본적으로 활성화되어 있지만, 비활성화하거나 설정을 수정할 수 있습니다.

Next.js는 세 가지 런타임, 즉 Node.js.js 런타임, 브라우저 런타임, Edge 런타임에서 동작할 수 있습니다. 다만, 모든 통합이 이 모든 런타임과 호환되는 것은 아니라는 점을 유의해야 합니다.

브라우저 런타임용 BrowserTracing 통합이나 Node.js.js 런타임용 RequestData 통합처럼, 특정 런타임의 기능을 확장하는 통합은 해당 런타임의 설정 파일에만 포함할 수 있습니다.

* 브라우저 런타임의 경우, `instrumentation-client.(js|ts)`에 통합을 추가합니다.
* Node.js.js의 경우, `instrumentation.(js|ts)`의 Sentry 설정에 통합을 추가합니다.
* Edge 런타임의 경우, `instrumentation.(js|ts)`의 Sentry 설정에 통합을 추가합니다.

- [공통 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#common-integrations)

|                                                                                                                                           | **자동 활성화** | **오류** | **트레이싱** | **추가 컨텍스트** |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`dedupeIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)                     | ✓                | ✓          |             |                        |
| [`functionToStringIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md) | ✓                |            |             |                        |
| [`inboundFiltersIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)     | ✓                | ✓          |             |                        |
| [`linkedErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)         | ✓                | ✓          |             |                        |
| [`captureConsoleIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)     |                  |            |             | ✓                      |
| [`extraErrorDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)     |                  |            |             | ✓                      |
| [`rewriteFramesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)       |                  | ✓          |             |                        |

- [브라우저 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#browser-integrations)

|                                                                                                                                             | **자동 활성화** | **오류** | **트레이싱** | **리플레이** | **추가 컨텍스트** |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------- | ---------------------- |
| [`breadcrumbsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)             | ✓                |            |             |            | ✓                      |
| [`browserApiErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)   | ✓                | ✓          |             |            |                        |
| [`browserSessionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)       | ✓                |            |             |            | ✓                      |
| [`browserTracingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)       | ✓                |            | ✓           |            | ✓                      |
| [`globalHandlersIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)       | ✓                | ✓          |             |            |                        |
| [`httpContextIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)             | ✓                |            |             |            | ✓                      |
| [`browserProfilingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)   |                  |            | ✓           |            |                        |
| [`contextLinesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)           |                  | ✓          |             |            |                        |
| [`featureFlagsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)           |                  |            |             |            | ✓                      |
| [`graphqlClientIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)         |                  |            |             |            | ✓                      |
| [`httpClientIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)               |                  | ✓          |             |            |                        |
| [`launchDarklyIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)           |                  |            |             |            | ✓                      |
| [`moduleMetadataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)       |                  |            |             |            | ✓                      |
| [`openFeatureIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)             |                  |            |             |            | ✓                      |
| [`replayCanvasIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)           |                  |            |             | ✓          |                        |
| [`replayIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)                       |                  |            |             | ✓          | ✓                      |
| [`reportingObserverIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md) |                  | ✓          |             |            |                        |
| [`statsigIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)                     |                  |            |             |            | ✓                      |
| [`supabaseIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)                   |                  | ✓          | ✓           |            |                        |
| [`unleashIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)                     |                  |            |             |            | ✓                      |

- [서버 (Node.js, Edge) 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#server-nodejs-edge-integrations)

|                                                                                                                                 | **자동 활성화** | **오류** | **트레이싱** | **추가 컨텍스트** |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`requestDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md) | ✓                |            | ✓           |                        |

- [Node.js 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#nodejs-integrations)

|                                                                                                                                                 | **자동 활성화** | **오류** | **트레이싱** | **추가 컨텍스트** |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`amqplibIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)                         | ✓                |            | ✓           |                        |
| [`consoleIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)                         | ✓                |            |             | ✓                      |
| [`contextLinesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)               | ✓                | ✓          |             |                        |
| [`genericPoolIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)                 | ✓                |            | ✓           |                        |
| [`graphqlIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)                         | ✓                |            | ✓           |                        |
| [`httpIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)                               | ✓                | ✓          | ✓           | ✓                      |
| [`kafkaIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)                             | ✓                |            | ✓           |                        |
| [`lruMemoizerIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)                 | ✓                |            | ✓           |                        |
| [`modulesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)                         | ✓                |            |             | ✓                      |

| [`mongoIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)                             | ✓                |            | ✓           |                        |
| [`mongooseIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)                       | ✓                |            | ✓           |                        |
| [`mysqlIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)                             | ✓                |            | ✓           |                        |
| [`mysql2Integration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)                           | ✓                |            | ✓           |                        |
| [`nodeContextIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)                 | ✓                |            |             | ✓                      |
| [`nativeNodeFetchIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)               | ✓                |            | ✓           | ✓                      |
| [`onUncaughtExceptionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md) | ✓                | ✓          |             |                        |
| [`onUnhandledRejectionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md) | ✓                | ✓          |             |                        |
| [`postgresIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)                       | ✓                |            | ✓           |                        |
| [`redisIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)                             | ✓                |            | ✓           |                        |
| [`requestDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)                 | ✓                |            | ✓           |                        |
| [`tediousIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)                         | ✓                |            | ✓           |                        |
| [`dataloaderIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)                   | ✓                |            | ✓           |                        |
| [`childProcessIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)               | ✓                |            |             | ✓                      |
| [`prismaIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)                           | ✓                |            | ✓           |                        |
| [`anrIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)                                 |                  | ✓          |             |                        |
| [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)         |                  | ✓          |             |                        |
| [`extraErrorDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)           |                  |            |             | ✓                      |
| [`fsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)                                   |                  |            | ✓           |                        |
| [`knexIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)                               |                  |            | ✓           |                        |
| [`localVariablesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)           |                  | ✓          |             |                        |
| [`nodeProfilingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)             |                  |            | ✓           |                        |
| [`trpcMiddleware`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)                                |                  | ✓          | ✓           | ✓                      |
| [`vercelAiIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)                       | ✓                |            | ✓           | ✓                      |
| [`openAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)                           | ✓                |            | ✓           |                        |
| [`anthropicAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)                   | ✓                | ✓          | ✓           |                        |
| [`googleGenAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)                | ✓                | ✓          | ✓           |                        |
| [`langChainIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)                     | ✓                | ✓          | ✓           |                        |
| [`zodErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)                     |                  |            |             | ✓                      |
| [`pinoIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)                               |                  | ✓          |             |                        |

- [Edge 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#edge-integrations)

|                                                                                                                                     | **자동 활성화** | **에러** | **트레이싱** | **추가 컨텍스트** |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`winterCGFetchIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md) | ✓                |            | ✓           | ✓                      |
| [`vercelAiIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)           |                  |            | ✓           |                        |

## [기본 통합 수정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)

시스템 통합을 비활성화하려면 `init()` 호출 시 `defaultIntegrations: false`를 설정하세요.

설정을 재정의하려면 `integrations` 옵션에 원하는 구성의 새 인스턴스를 제공하세요. 예를 들어 브라우저의 콘솔 호출 캡처를 끄려면 다음과 같이 합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.breadcrumbsIntegration({
      console: false,
    }),
  ],

});
```

## [통합 추가하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#adding-an-integration)

`init` 호출에서 추가 통합을 넣을 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.reportingObserverIntegration()],
});
```

또는 `Sentry.addIntegration()`을 통해 통합을 추가할 수도 있습니다. 특정 환경에서만 통합을 활성화하거나 나중에 통합을 로드하고 싶을 때 유용합니다. 그 외의 경우에는 `integrations` 옵션 사용을 권장합니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  integrations: [],
});

Sentry.addIntegration(Sentry.reportingObserverIntegration());
```

## [통합 지연 로딩](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#lazy-loading-integrations)

지연 로딩을 사용하면 초기 번들 크기를 늘리지 않고 플러그형 통합을 추가할 수 있습니다. 방법은 두 가지입니다.

- [1. 동적 import (권장)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#1-dynamic-import-recommended)

`import()`를 사용한 동적 import로 통합을 추가할 수 있습니다. 이 방식은 npm 패키지에서 통합을 로드합니다. `import()` 관련 문제를 피하려면 동적 import를 지원하는 번들러를 사용해야 합니다. 프로젝트에서 Vite 같은 도구를 사용하고 있다면 번들링 과정이 이미 설정되어 있을 가능성이 높습니다.

`instrumentation-client.ts`

```javascript
Sentry.init({
  // Note, Replay is NOT instantiated below:
  integrations: [],
});
```

그다음 애플리케이션의 어딘가, 예를 들어 `useEffect` 훅에서 Replay 통합을 지연 로딩할 수 있습니다.

```javascript
import("@sentry/nextjs").then((lazyLoadedSentry) => {
  Sentry.addIntegration(lazyLoadedSentry.replayIntegration());
});
```

- [2. `lazyLoadIntegration()`으로 CDN에서 로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#2-load-from-cdn-with-lazyloadintegration)

`Sentry.lazyLoadIntegration()`을 통해서도 플러그형 통합을 지연 로딩할 수 있습니다. 이 경우 Sentry CDN에서 통합 로드를 시도합니다. 사용자가 광고 차단기를 쓰거나 네트워크 문제가 있는 경우 Sentry CDN에서 통합 로드에 실패하며 이 함수는 reject됩니다. 애플리케이션에서 이 함수의 rejection이 항상 처리되도록 해야 합니다.

```javascript
async function loadHttpClient() {
  const httpClientIntegration = await Sentry.lazyLoadIntegration(
    "httpClientIntegration",
  );
  Sentry.addIntegration(httpClientIntegration());
}
```

다음 통합에서 지연 로딩을 사용할 수 있습니다.

* `replayIntegration`
* `replayCanvasIntegration`
* `feedbackIntegration`
* `feedbackModalIntegration`
* `feedbackScreenshotIntegration`
* `captureConsoleIntegration`
* `contextLinesIntegration`
* `linkedErrorsIntegration`
* `dedupeIntegration`
* `extraErrorDataIntegration`
* `httpClientIntegration`
* `reportingObserverIntegration`
* `rewriteFramesIntegration`
* `browserProfilingIntegration`

## [기본 통합 제거하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#removing-a-default-integration)

기본 통합 전체를 `defaultIntegrations: false`로 비활성화하는 대신, 기본 통합 중 하나 또는 일부만 제거하고 싶다면 아래 구문을 사용해 원하지 않는 항목을 필터링할 수 있습니다.

다음 예시는 기본 활성화된, 이벤트에 breadcrumb를 추가하는 통합을 제거합니다.

```javascript
Sentry.init({
  // ...
  integrations: function (integrations) {
    // integrations will be all default integrations
    return integrations.filter(function (integration) {
      return integration.name !== "Breadcrumbs";
    });
  },
});
```

## [사용자 정의 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#custom-integrations)

[사용자 정의 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md)도 만들 수 있습니다.

## [사용 가능한 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#available-integrations)

*
- [RequestData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)

  백엔드에서 처리되는 요청 중 발생하는 트랜잭션 및 에러 이벤트에 들어오는 요청 데이터를 추가합니다. (기본값)

*
- [Amqplib](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)

  Amqplib용 계측을 추가합니다. (기본값)

*
- [Anr](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)

  이벤트 루프가 차단되어 애플리케이션이 더 이상 응답하지 않을 때 이벤트를 캡처합니다.

*

- [Anthropic](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)

  Anthropic SDK용 계측을 추가합니다.

*
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)

  breadcrumb를 수집하기 위해 네이티브 브라우저 API를 래핑합니다. (기본값)

*
- [BrowserApiErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)

  비동기 예외를 처리하기 위해 네이티브 시간 및 이벤트 API (\`setTimeout\`, \`setInterval\`, \`requestAnimationFrame\`, \`addEventListener/removeEventListener\`)를 \`try/catch\` 블록으로 래핑합니다. (기본값)

*
- [BrowserProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)

  Browser의 프로파일링 데이터를 수집합니다.

*
- [BrowserSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)

  Browser에서 정상 Session을 추적합니다.

*
- [BrowserTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)

  Browser의 성능 데이터를 수집합니다.

*
- [CaptureConsole](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)

  \`captureException\` 또는 \`captureMessage\`를 통해 모든 Console API 호출을 수집합니다.

*
- [Child Process Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)

  child process 및 worker thread용 계측을 추가합니다. (기본값)

*
- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)

  콘솔 로그를 breadcrumb로 수집합니다. (기본값)

*
- [Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)

  클라이언트가 실행되는 환경과 디바이스에 대한 컨텍스트를 수집해 이벤트에 추가합니다. (기본값)

*
- [ContextLines](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)

  현재 페이지 HTML의 인라인 JavaScript에서 소스 코드를 추가합니다.

*
- [Dataloader](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)

  Dataloader용 계측을 추가합니다.

*
- [Dedupe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)

  중복 오류 수신을 방지하기 위해 특정 이벤트를 중복 제거합니다. (기본값)

*
- [Event Loop Block](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)

  Node.js 애플리케이션의 모든 스레드에서 이벤트 루프 차단을 모니터링합니다.

*
- [ExtraErrorData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)

  error 객체에서 네이티브가 아닌 모든 속성을 추출해 추가 데이터로 이벤트에 첨부합니다.

*
- [FileSystem](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)

  파일 시스템 작업용 계측을 추가합니다.

*
- [FunctionToString](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md)

  함수나 메서드가 오류 또는 breadcrumb 핸들러로 래핑된 경우에도 SDK가 원래 함수 및 메서드 이름을 제공할 수 있게 합니다. (기본값)

*
- [Generic Feature Flags Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)

  사용자 지정 기능 플래그 데이터를 Sentry 오류 이벤트에 첨부하는 방법을 알아보세요.

*
- [Generic Pool](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)

  Generic Pool용 계측을 추가합니다. (기본값)

*
- [GlobalHandlers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)

  포착되지 않은 예외 및 처리되지 않은 reject를 수집하기 위한 전역 핸들러를 연결합니다. (기본값)

*
- [Google Gen AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)

  Google Gen AI SDK용 계측을 추가합니다.

*
- [GraphQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)

  GraphQL용 계측을 추가합니다. (기본값)

*
- [GraphQLClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)

  GraphQL 요청의 데이터로 스팬과 breadcrumb를 강화합니다.

*
- [Http](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)

  http 요청에 대한 스팬 및 breadcrumb를 수집합니다. (기본값)

*
- [HttpClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)

  Fetch 및 XHR의 실패한 요청에서 오류를 수집하고 요청/응답 정보를 첨부합니다.

*
- [HttpContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)

  URL, user-agent, referrer 및 기타 헤더와 같은 HTTP 요청 정보를 이벤트에 첨부합니다. (기본값)

*
- [InboundFilters](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)

  주어진 예외의 타입, 메시지 또는 URL을 기준으로 특정 오류를 무시할 수 있게 합니다. (기본값)

*
- [Kafka](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)

  KafkaJS용 계측을 추가합니다. (기본값)

*
- [Knex](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)

  Knex용 계측을 추가합니다.

*
- [LangChain](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)

  LangChain용 계측을 추가합니다.

*
- [LangGraph](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md)

  LangGraph SDK용 계측을 추가합니다.

*
- [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)

  Sentry를 LaunchDarkly와 함께 사용하는 방법을 알아보세요.

*
- [LinkedErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)

  연결된 오류를 구성할 수 있게 합니다. (기본값)

*
- [LocalVariables](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)

  예외 프레임에 로컬 변수를 추가합니다. (기본값)

*
- [LRU Memoizer](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)

  LRU Memoizer용 계측을 추가합니다. (기본값)

*
- [ModuleMetadata](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)

  스택 프레임에 모듈 메타데이터를 추가합니다.

*
- [Modules](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)

  이벤트에 node modules / packages를 추가합니다. (기본값)

*
- [MongoDB](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)

  MongoDB용 계측을 추가합니다. (기본값)

*
- [Mongoose](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)

  Mongoose용 계측을 추가합니다. (기본값)

*
- [MySQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)

  MySQL용 계측을 추가합니다. (기본값)

*
- [MySQL2](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)

  MySQL2용 계측을 추가합니다. (기본값)

*
- [NodeFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)

  node fetch 요청에 대한 스팬 및 breadcrumb를 수집합니다. (기본값)

*
- [NodeProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)

  Node.js 애플리케이션의 프로파일링 데이터를 수집합니다.

*
- [OnUncaughtException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md)

  전역 포착되지 않은 예외를 수집하기 위한 핸들러를 등록합니다. (기본값)

*
- [OnUnhandledRejection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md)

  전역 처리되지 않은 promise reject를 수집하기 위한 핸들러를 등록합니다. (기본값)

*
- [OpenAI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)

  OpenAI SDK용 계측을 추가합니다.

*
- [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)

  Sentry를 OpenFeature와 함께 사용하는 방법을 알아보세요.

*
- [Pino](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)

  Pino의 로그와 오류를 수집합니다.

*
- [Postgres](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)

  Postgres용 계측을 추가합니다. (기본값)

*
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)

  Prisma용 계측을 추가합니다. (기본값)

*
- [Redis](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)

  Redis용 계측을 추가합니다. (기본값)

*
- [Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)

  사용자 브라우저에서 무슨 일이 일어났는지 비디오처럼 재현한 내용을 수집합니다.

*
- [ReplayCanvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)

  HTML canvas 요소에서 session replay를 수집합니다.

*
- [ReportingObserver](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md)

  \`ReportingObserver\` 인터페이스를 통해 수집된 보고서를 캡처해 Sentry로 전송합니다.

*
- [RewriteFrames](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)

  스택 트레이스의 각 프레임에 변환을 적용할 수 있게 합니다.

*
- [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)

  Sentry를 Statsig와 함께 사용하는 방법을 알아보세요.

*
- [Supabase](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)

  Supabase 클라이언트 작업용 계측을 추가합니다.

*
- [Tedious](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)

  Tedious용 계측을 추가합니다. (기본값)

*
- [trpcMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)

  tRPC 핸들러의 스팬과 오류를 수집합니다.

*
- [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)

  Sentry를 Unleash와 함께 사용하는 방법을 알아보세요.

*
- [Vercel AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)

  Vercel AI SDK용 계측을 추가합니다.

*
- [WebWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md)

  Web Worker를 메인 스레드에서 실행 중인 SDK와 연결합니다.

*
- [WinterCGFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md)

  edge runtime의 fetch 요청에 대해 스팬을 생성하고 tracing 헤더를 첨부합니다. (기본값)

*
- [ZodErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)

  Zod 유효성 검사 오류에 추가 데이터를 더합니다.

## 이 섹션의 페이지

- [RequestData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)
- [Amqplib](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)

- [Anr](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)
- [Anthropic](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)
- [BrowserApiErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)
- [BrowserProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)
- [BrowserSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)
- [BrowserTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)
- [CaptureConsole](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)
- [자식 프로세스 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)
- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)
- [Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)
- [ContextLines](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)
- [Dataloader](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)
- [Dedupe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)
- [이벤트 루프 블록](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)
- [ExtraErrorData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)
- [FileSystem](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)
- [FunctionToString](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md)
- [범용 기능 플래그 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)
- [범용 풀](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)
- [GlobalHandlers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)
- [Google Gen AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)
- [GraphQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)
- [GraphQLClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)
- [Http](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)
- [HttpClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)
- [HttpContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)
- [InboundFilters](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)
- [Kafka](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)
- [Knex](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)
- [LangChain](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)
- [LangGraph](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md)
- [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)
- [LinkedErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)
- [LocalVariables](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)
- [LRU 메모이저](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)
- [ModuleMetadata](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)
- [Modules](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)
- [MongoDB](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)
- [Mongoose](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)
- [MySQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)
- [MySQL2](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)
- [NodeFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)
- [NodeProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)
- [OnUncaughtException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md)
- [OnUnhandledRejection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md)
- [OpenAI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)
- [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)
- [Pino](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)
- [Postgres](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x.md)
- [Redis](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)
- [Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)
- [ReplayCanvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)
- [ReportingObserver](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md)
- [RewriteFrames](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)
- [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)
- [Supabase](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)
- [Tedious](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)
- [trpcMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)
- [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)
- [Vercel AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)
- [WebWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md)
- [WinterCGFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md)
- [ZodErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)
- [사용자 지정 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md)

