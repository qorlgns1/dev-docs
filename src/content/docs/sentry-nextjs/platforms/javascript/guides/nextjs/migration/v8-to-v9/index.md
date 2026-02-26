---
title: '8.x에서 9.x로 마이그레이션 | Sentry for Next.js'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9

# 8.x에서 9.x로 마이그레이션 | Sentry for Next.js

Sentry JavaScript SDK 버전 9는 주로 API 정리와 지원 버전 변경을 도입합니다.

이번 업데이트에는 타입 체커, 린터, 테스트로는 잡히지 않는 동작 변경이 포함되어 있으므로, 자동 도구에 의존하기보다 전체 마이그레이션 가이드를 꼼꼼히 읽는 것을 권장합니다.

SDK 버전 9는 Sentry self-hosted 버전 24.4.2 이상과 호환됩니다(v8과 동일). 더 낮은 버전에서도 계속 동작할 수는 있지만, 일부 기능은 지원되지 않을 수 있습니다.

## [지원 버전 변경 사항:](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#version-support-changes)

Sentry SDK 버전 9는 런타임 및 프레임워크에 대한 새로운 호환 범위를 가집니다.

- [일반 런타임 지원 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#general-runtime-support-changes)

#
- [최소 호환 ECMAScript 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#minimum-compatible-ecmascript-version)

이제 Sentry SDK 패키지의 모든 JavaScript 코드에 ECMAScript 2020 기능이 포함될 수 있습니다. 여기에는 Nullish Coalescing (`??`), Optional Chaining (`?.`), `String.matchAll()`, Logical Assignment Operators (`&&=`, `||=`, `??=`), `Promise.allSettled()` 같은 기능이 포함됩니다.

위에 나열된 문법 또는 기능으로 인해 실패가 발생한다면, 현재 런타임이 ES2020을 지원하지 않는다는 의미일 수 있습니다. 런타임이 ES2020을 지원하지 않는 경우 Babel 또는 유사한 도구로 SDK를 트랜스파일하는 것을 권장합니다.

#
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#nodejs)

최소 지원 Node.js 버전은 **18.0.0**(출시일: 2022년 4월 19일)입니다. 단, ESM 전용 SDK(`@sentry/astro`, `@sentry/nuxt`, `@sentry/sveltekit`)는 Node.js **18.19.1**(출시일: 2024년 2월 14일) 이상이 필요합니다.

#
- [브라우저](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#browsers)

SDK 코드에 ES2020 기능이 포함되면서, 최소 지원 브라우저 목록은 다음과 같습니다:

* Chrome 80 (출시일: 2020년 2월 5일)
* Edge 80 (출시일: 2020년 2월 7일)
* Safari 14, iOS Safari 14.4 (출시일: 2020년 9월 16일)
* Firefox 74 (출시일: 2020년 3월 10일)
* Opera 67 (출시일: 2020년 3월 12일)
* Samsung Internet 13.0 (출시일: 2020년 11월 20일)

구형 브라우저를 지원해야 한다면 SWC, Babel 또는 유사한 도구로 코드를 트랜스파일하는 것을 권장합니다.

- [TypeScript 버전 정책](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#typescript-version-policy)

OpenTelemetry SDK v2를 준비하기 위해 최소 요구 TypeScript 버전이 `5.0.4`로 상향되었습니다.

또한 OpenTelemetry SDK와 마찬가지로, Sentry JavaScript SDK는 [DefinitelyType의 버전 지원 정책](https://github.com/DefinitelyTyped/DefinitelyTyped#support-window)을 따릅니다. 이 정책은 TypeScript의 각 릴리스 버전에 대해 2년의 지원 기간을 가집니다.

구형 TypeScript 버전도 계속 호환될 *수는* 있지만, 보장되지는 않습니다.

- [패키지](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#packages)

* Prisma 버전 `5.x` 이하는 더 이상 지원되지 않습니다(최소 지원 버전은 `6.x`).

## [동작 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#behavior-changes)

이 섹션의 변경 사항은 업그레이드 후 SDK 동작이 어떤 방식으로 달라질 수 있는지 설명합니다:

* `beforeSendSpan` 훅에서 span을 드롭하는 것은 더 이상 불가능합니다. 즉, `beforeSendSpan` 훅에서 더 이상 `null`을 반환할 수 없습니다. 이 훅은 span에 추가 데이터를 넣거나 불필요한 속성(예: PII 제거)을 제거하는 데 사용되도록 의도되었습니다. 어떤 span을 기록할지 제어하려면 대신 [integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md) 설정을 권장합니다.

* 이제 `beforeSendSpan` 훅은 child span뿐 아니라 root span도 전달받습니다. 이 변경 사항을 반영하도록 `beforeSendSpan`을 점검하는 것을 권장합니다.

* `tracesSampler` 및 `profilesSampler` 옵션으로 전달되는 `samplingContext` 인자의 `request` 속성이 제거되었습니다. 대신 `samplingContext.normalizedRequest`를 사용할 수 있습니다. `normalizedRequest`의 타입은 `request`와 다르다는 점에 유의하세요.

* 사용자 지정 `scope`를 전달할 때 `startSpan` 동작이 변경되었습니다. v8에서는 전달한 scope 자체에 직접 active 설정했지만, v9에서는 scope를 복제합니다. 이 동작 변경은 `@sentry/node`에는 적용되지 않습니다(`@sentry/node`는 이미 scope를 복제하고 있었기 때문). 이 변경은 span이 callback 내부에서만 active 상태를 유지하도록 보장하고, `@sentry/node`와 다른 모든 SDK 간 동작을 일치시키기 위해 도입되었습니다. 그 결과 span 계층 구조가 더 정확해져야 합니다. 다만 `startSpan` callback 내부에서 scope를 수정하는 경우(예: 태그 설정) 동작이 이제 약간 다릅니다.

  ```javascript
  startSpan({ name: "example", scope: customScope }, () => {
    // This tag will only remain within the callback.
    getCurrentScope().setTag("tag-a", "a");

    // Set the tag directly on customScope in addition,
    // if you want to to persist the tag outside of the callback.
    customScope.setTag("tag-a", "a");
  });
  ```

* `tracesSampleRate` 옵션 값으로 `undefined`를 전달하면 이제 해당 속성이 아예 정의되지 않은 것과 동일하게 처리됩니다. 이전 버전에서는 tracing을 위해 trace 데이터를 전파할지 결정할 때 SDK 옵션에 `tracesSampleRate` 속성이 존재하는지 확인했습니다. 그 결과 `tracesSampleRate: undefined`를 전달하면 SDK가 음수 샘플링 결정을 전파하는 경우가 있었습니다. 이제는 그렇지 않으며, 분산 추적을 위한 샘플링 결정은 downstream SDK로 위임됩니다. 이는 호환성 파괴 변경이라기보다 버그 수정에 가깝지만, SDK 구성에 따라 샘플링된 trace가 증가할 수 있습니다.

* 선택 사항인 `captureConsoleIntegration`을 사용하고 `Sentry.init` 호출에서 `attachStacktrace: true`를 설정한 경우, 콘솔 메시지는 더 이상 unhandled(`handled: false`)로 표시되지 않고 handled(`handled: true`)로 표시됩니다. 계속 unhandled로 전송하려면 integration 추가 시 `handled` 옵션을 설정하세요:

  ```javascript
  Sentry.init({
    integrations: [Sentry.captureConsoleIntegration({ handled: false })],
    attachStacktrace: true,
  });
  ```

- SDK는 더 이상 기본값으로 Sentry backend에 IP 주소 자동 추론을 지시하지 않습니다. Sentry backend(self-hosted) 버전에 따라 Sentry에서 IP 주소가 더 이상 표시되지 않고 이벤트가 "anonymous users"로 그룹화될 수 있습니다. 이 문서 작성 시점에는 Sentry SaaS 솔루션이 계속 IP 주소를 추론하지만, 가까운 시일 내에 변경될 예정입니다. Sentry backend가 항상 IP 주소를 추론하도록 하려면 `Sentry.init()`에서 `sendDefaultPii: true`를 설정하세요.

* 이제 `tracesSampler` 훅은 *모든* span에 대해 호출되지 않습니다. 다만 root span에는 분산 추적 사용 시처럼 다른 서비스에서 들어온 trace 데이터가 있을 수 있습니다.

* `requestDataIntegration`은 `express` 사용 시 더 이상 `request.user`에서 사용자를 자동 설정하지 않습니다. v9부터는 Sentry 이벤트에 사용자를 설정하려면 middleware 등에서 `Sentry.setUser()`를 수동 호출해야 합니다.

* `processThreadBreadcrumbIntegration`은 `childProcessIntegration`으로 이름이 변경되었습니다.

* `childProcessIntegration`(이전 `processThreadBreadcrumbIntegration`)의 `name` 값이 `"ProcessAndThreadBreadcrumbs"`에서 `"ChildProcess"`로 변경되었습니다. 등록된 integration에 대한 필터링 로직이 있다면 변경된 이름을 반영하도록 업데이트해야 합니다.

* `vercelAIIntegration`의 `name` 값이 `"vercelAI"`에서 `"VercelAI"`(대문자화)로 변경되었습니다. 등록된 integration에 대한 필터링 로직이 있다면 변경된 이름을 반영하도록 업데이트해야 합니다.

* Prisma integration은 더 이상 Prisma v5를 지원하지 않으며 기본으로 Prisma v6를 지원합니다. Prisma v6 기준으로, Prisma integration에서 tracing을 사용하기 위해 Prisma 스키마의 `previewFeatures = ["tracing"]` client generator 옵션은 더 이상 필요하지 않습니다.

  다른/구형 Prisma 버전에서 성능 계측을 사용하려면:

  1. 원하는 버전의 `@prisma/instrumentation` 패키지를 설치합니다.

  2. `@prisma/instrumentation`에서 export된 `new PrismaInstrumentation()` 인스턴스를 이 integration의 `prismaInstrumentation` 옵션으로 전달합니다:

     ```js
     import { PrismaInstrumentation } from "@prisma/instrumentation";
     Sentry.init({
       integrations: [
         prismaIntegration({
           // Override the default instrumentation that Sentry uses
           prismaInstrumentation: new PrismaInstrumentation(),
         }),
       ],
     });
     ```

     전달된 instrumentation 인스턴스는 integration이 기본으로 사용하는 instrumentation 인스턴스를 덮어쓰며, `prismaIntegration`은 다양한 Prisma 버전에 대한 데이터 호환성을 계속 보장합니다.

  3. Prisma 버전(Prisma 6 미만)에 따라 Prisma 스키마의 client generator 블록에 `previewFeatures = ["tracing"]`를 추가합니다:

     ```bash
     generator client {
       provider = "prisma-client-js"
       previewFeatures = ["tracing"]
     }
     ```

* `skipOpenTelemetrySetup: true`가 설정되면, 기본값으로 `httpIntegration({ spans: false })`가 설정됩니다. 더 이상 이를 수동으로 지정할 필요가 없습니다. 이 변경으로 `skipOpenTelemetrySetup: true`를 설정하면 추가 설정 없이 span이 생성되지 않습니다.

- SDK는 더 이상 빌드 설정(Vite config, Rollup config, `next.config.js` 등)에서 source map 생성을 위한 사용자 제공 값을 변환하지 않습니다.

  source map이 명시적으로 비활성화되어 있으면 SDK가 이를 활성화하지 않습니다. source map이 명시적으로 활성화되어 있으면 SDK가 출력 방식을 변경하지 않습니다. **하지만,** 업로드 후 source map을 삭제하지도 *않습니다*. source map 생성이 설정되어 있지 않으면 SDK가 이를 활성화하고 업로드 후 삭제합니다.

  업로드 후 삭제할 파일을 사용자 지정하려면 globs를 포함한 `filesToDeleteAfterUpload` 배열을 정의하세요.

* `ErrorBoundary` 컴포넌트의 `componentStack` 필드는 이제 `onError`와 `onReset` 라이프사이클 메서드에서 `string | null | undefined` 대신 `string`으로 타입 지정됩니다. 이는 component stack을 사용할 수 있을 때 React가 항상 `string`을 반환하는 실제 동작과 더 일치합니다.

  `onUnmount` 라이프사이클 메서드에서 `componentStack` 필드는 이제 `string | null`로 타입 지정됩니다. 언마운트 시점까지 오류가 발생하지 않았다면 `componentStack`은 `null`입니다.

- 기본적으로 클라이언트 측 source map은 빌드 중 Sentry에 업로드된 뒤 자동으로 삭제됩니다. 이 동작을 비활성화하려면 Sentry 설정에서 `sourcemaps.deleteSourcemapsAfterUpload`를 명시적으로 `false`로 설정하세요.

- Sentry Next.js SDK는 더 이상 릴리스의 대체 식별자로 Next.js Build ID를 사용하지 않습니다. SDK는 계속 CI 제공자별 환경 변수와 현재 git SHA를 읽어 릴리스 이름을 자동 결정하려고 시도합니다. Sentry에서 릴리스가 더 이상 생성되지 않는다면, `withSentryConfig`에 `release.name` 옵션으로 릴리스 이름을 수동 제공하는 것을 권장합니다.

  이 동작은 Next.js Build ID가 비결정적이어서, 릴리스 이름이 클라이언트 번들에 주입될 때 빌드 산출물이 비결정적이 되는 문제 때문에 변경되었습니다.

- source map은 `sourcemaps.disable`로 명시적으로 비활성화하지 않는 한, 이제 클라이언트와 서버 빌드 모두에서 자동으로 활성화됩니다. 클라이언트 빌드는 `hidden-source-map`, 서버 빌드는 `source-map`을 webpack `devtool` 설정으로 사용합니다. 단, 이미 `false` 또는 `undefined` 이외의 값이 할당되어 있다면 기존 값을 유지합니다.

- Next.js config 객체의 `sentry` 속성은 공식적으로 더 이상 사용되지 않습니다. 옵션은 `withSentryConfig`에 직접 전달하세요.

## [패키지 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#package-removals)

`@sentry/utils` 패키지는 더 이상 배포되지 않습니다.

`@sentry/types` 패키지는 계속 배포되지만, deprecated 상태이며 API가 확장되지 않습니다. 또한 향후 메이저 버전의 일부로는 배포되지 않습니다.

`@sentry/utils`와 `@sentry/types`의 모든 export 및 API(이 마이그레이션 가이드에서 제거 대상으로 명시된 항목 제외)는 `@sentry/core` 패키지로 이동되었습니다.

## [제거된 API](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#removed-apis)

이 섹션에서 설명하는 변경 사항은 이전에 deprecated 되었고 이제 제거된 API를 다룹니다.

* **이전 메트릭 API가 SDK에서 제거되었습니다.**

  이전 Sentry metrics 베타는 종료되었고 해당 API는 SDK에서 제거되었습니다. 최신 SDK 버전에서는 새로운 Metrics 기능을 사용할 수 있습니다. 설정 방법은 [Metrics 문서](https://docs.sentry.io/platforms/javascript/metrics.md)를 참고하세요.

* `tracesSampler` 및 `profilesSampler` 옵션에 전달되는 `samplingContext` 인수의 `transactionContext` 속성이 제거되었습니다. 모든 객체 속성은 `samplingContext`의 최상위 레벨에서 사용할 수 있습니다:

  ```javascript
  Sentry.init({
    // Custom traces sampler
    tracesSampler: samplingContext => {
  -   if (samplingContext.transactionContext.name === '/health-check') {
  +   if (samplingContext.name === '/health-check') {
        return 0;
      } else {
        return 0.5;
      }
    },

    // Custom profiles sampler
    profilesSampler: samplingContext => {
  -   if (samplingContext.transactionContext.name === '/health-check') {
  +   if (samplingContext.name === '/health-check') {
        return 0;
      } else {
        return 0.5;
      }
    },
  })
  ```

* `enableTracing` 옵션이 제거되었습니다. 대신 `tracesSampleRate: 1` 또는 `tracesSampleRate: 0`을 설정하세요.

* `autoSessionTracking` 옵션이 제거되었습니다.

  세션 추적을 활성화하려면 브라우저 환경에서는 `browserSessionIntegration`이 추가되어 있거나, 서버 환경에서는 `httpIntegration`이 추가되어 있어야 합니다. (둘 다 기본으로 추가됩니다)

  세션 추적을 비활성화하려면 브라우저 환경에서는 `browserSessionIntegration`을 제거하거나, 서버 환경에서는 `httpIntegration`의 `trackIncomingRequestsAsSessions` 옵션을 `false`로 설정하세요. 또한 Node.js 환경에서는 `autoSessionTracking`이 `true`로 설정되면 각 node 프로세스마다 세션이 자동 생성되었습니다. 이 동작은 기본 설정되는 `processSessionIntegration`으로 대체되었습니다.

* `getCurrentHub()`, `Hub`, `getCurrentHubShim()` API가 제거되었습니다. 이들은 v8 릴리스 이후 호환성 유지를 위해 최소한으로만 유지되어 왔으며, 이제 SDK에서 완전히 제거되었습니다.

* `addOpenTelemetryInstrumentation` 메서드가 제거되었습니다. 대신 `Sentry.init()` 또는 사용자 정의 Sentry Client에서 `openTelemetryInstrumentations` 옵션을 사용하세요.

  ```js
  import * as Sentry from "@sentry/node";

  // before
  Sentry.addOpenTelemetryInstrumentation(new GenericPoolInstrumentation());

  // after
  Sentry.init({
    openTelemetryInstrumentations: [new GenericPoolInstrumentation()],
  });
  ```

* `debugIntegration`이 제거되었습니다. 나가는 이벤트를 로깅하려면 [Hook Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#hooks) (`beforeSend`, `beforeSendTransaction`, ...)를 사용하세요.

* `sessionTimingIntegration`이 제거되었습니다. 이벤트와 함께 세션 지속 시간을 수집하려면 [Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/context.md) (`Sentry.setContext()`)를 사용하세요.

- `addOpenTelemetryInstrumentation` 메서드가 제거되었습니다. 대신 `Sentry.init()` 또는 사용자 정의 Sentry Client에서 `openTelemetryInstrumentations` 옵션을 사용하세요.

- `registerEsmLoaderHooks`는 이제 `true | false | undefined`만 허용합니다. SDK는 OpenTelemetry Instrumentation의 일부로 사용되는 모듈을 기본적으로 래핑합니다.

- `nestIntegration`이 제거되었습니다. 대신 NestJS SDK (`@sentry/nestjs`)를 사용하세요.

- `setupNestErrorHandler`가 제거되었습니다. 대신 NestJS SDK (`@sentry/nestjs`)를 사용하세요.

* `captureUserFeedback` 메서드가 제거되었습니다. 대신 `captureFeedback` 메서드를 사용하고 `comments` 필드를 `message`로 변경하세요.

- `hideSourceMaps` 옵션이 대체 없이 제거되었습니다. SDK는 기본적으로 hidden sourcemaps를 내보냅니다.

## [빌드 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#build-changes)

* 이제 SDK의 CJS 코드는 default export가 있는 모듈에서만 CJS/ESM 호환성 구문을 포함합니다:

  ```js
  Object.defineProperty(exports, "__esModule", { value: true });
  ```

  이 변경이 현재 설정에서 문제를 일으킨다면 GitHub 이슈를 열어 알려주세요.

* `@sentry/deno`는 더 이상 `deno.land` 레지스트리에 게시되지 않으므로, npm에서 SDK를 import해야 합니다:

  ```javascript
  import * as Sentry from "npm:@sentry/deno";

  Sentry.init({
    dsn: "__DSN__",
    // ...
  });
  ```

## [타입 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#type-changes)

* `Scope` 사용은 이제 항상 `Scope` 인스턴스를 기대합니다.

* `Client` 사용은 이제 항상 `BaseClient` 인스턴스를 기대합니다. 추상 `Client` 클래스는 제거되었습니다. 이제 Client 클래스는 `BaseClient`를 상속해야 합니다.

이 변경 사항은 내부 메서드에 유사한 형태의 객체를 전달하는 방식에 의존한 경우가 아니라면 대부분의 사용자에게 영향을 주지 않습니다.

v8에서는 인터페이스가 `@sentry/types`에서 export되었고, 구현체는 다른 패키지에서 export되었습니다.

## [기타 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#other-changes)

아래 변경 사항은 SDK 사용자에게 영향을 줄 가능성이 낮습니다. 완결성을 위해 여기에 나열했으며, 내부 동작에 의존할 수 있는 사용자에게 알리기 위한 목적입니다.

- [`@sentry/core`에서 제거된 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#removals-in-sentrycore)

* 이제 `PropagationContext`의 `sampleRand` 필드는 필수입니다. 이는 `scope.setPropagationContext(...)`를 사용했다면 관련이 있습니다.

* `DEFAULT_USER_INCLUDES` 상수가 제거되었습니다. 대체 항목은 없습니다.

* `BAGGAGE_HEADER_NAME` export가 제거되었습니다. 대신 `"baggage"` 문자열 상수를 직접 사용하세요.

* `extractRequestData` 메서드가 제거되었습니다. 대신 요청 객체에서 관련 데이터를 직접 추출하세요.

* `addRequestDataToEvent` 메서드가 제거되었습니다. 대신 `httpRequestToRequestData`를 사용하고, 결과 객체를 `event.request`에 직접 넣으세요.

* `addNormalizedRequestDataToEvent` 메서드가 제거되었습니다. 대신 `httpRequestToRequestData`를 사용하고, 결과 객체를 `event.request`에 직접 넣으세요.

* `generatePropagationContext()` 메서드가 제거되었습니다. `generateTraceId()`를 직접 사용하세요.

* `propagationContext`의 `spanId` 필드가 제거되었습니다. 동일한 의미를 갖는 **optional** 필드 `propagationSpanId`로 대체되었으며, 특정 span ID에 실행 단위를 연결해야 할 때만 정의됩니다.

* `ServerRuntimeClient`의 `initSessionFlusher` 메서드는 대체 없이 제거되었습니다. 세션을 생성하는 메커니즘은 자체적으로 flush를 수행합니다.

* `IntegrationClass` 타입이 제거되었습니다. 대신 `Integration` 또는 `IntegrationFn`을 사용하세요.

* 다음 export는 대체 없이 제거되었습니다:

  * `getNumberOfUrlSegments`
  * `validSeverityLevels`
  * `makeFifoCache`
  * `arrayify`
  * `flatten`
  * `urlEncode`
  * `getDomElement`
  * `memoBuilder`
  * `extractPathForTransaction`
  * `_browserPerformanceTimeOriginMode`
  * `addTracingHeadersToFetchRequest`
  * `SessionFlusher`

* 다음 타입은 대체 없이 제거되었습니다:

  * `Request` `RequestEventData`
  * `TransactionNamingScheme`
  * `RequestDataIntegrationOptions`
  * `SessionFlusherLike`
  * `RequestSession`
  * `RequestSessionStatus`

- [`@sentry/opentelemetry`에서 제거된 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#removals-in-sentryopentelemetry)

* `getPropagationContextFromSpan`이 대체 없이 제거되었습니다.

* `generateSpanContextForPropagationContext`가 대체 없이 제거되었습니다.

- `client._prepareEvent()`는 이제 인수로 `currentScope`와 `isolationScope`를 모두 전달해야 합니다.

- `client.recordDroppedEvent()`는 더 이상 세 번째 인수로 `event`를 받지 않습니다. `event`는 한동안 사용되지 않았으며, 대신 세 번째 인수로 드롭된 이벤트 수를 (선택적으로) 전달할 수 있습니다.

## [버전 지원 타임라인](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v8-to-v9.md#version-support-timeline)

버전 지원 타임라인은 SDK를 사용하는 모두에게 부담이 될 수 있으므로, 별도로 정의하지 않겠습니다. 대신 수요가 있는 한 이전 버전에도 버그 수정과 기능을 적용하겠습니다.

또한 보안 이슈에 대해서는 책임 있게 대응합니다. 즉, 취약점이 발견되면 거의 모든 경우에 백포트할 것입니다.

단, 백포트 결정은 사안별(case-by-case)로 이루어집니다. SDK 이전 버전에 수정이나 기능이 필요하다면 GitHub Issue를 통해 문의해 주세요.

