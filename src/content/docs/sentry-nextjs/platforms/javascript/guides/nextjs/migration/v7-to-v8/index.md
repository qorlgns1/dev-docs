---
title: '7.x에서 8.x로 마이그레이션 | Sentry for Next.js'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8

# 7.x에서 8.x로 마이그레이션 | Sentry for Next.js

버전 8의 주요 목표는 성능 모니터링 API, 통합 API, 그리고 ESM 지원을 개선하는 것입니다. 이 버전은 호환성이 깨지는 변경이 포함되어 있는데, 더 이상 사용되지 않는 API를 제거하고, npm 패키지 구성을 재구성했으며, OpenTelemetry에 대한 새로운 의존성을 도입했기 때문입니다.

## [Migration Codemod](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#migration-codemod)

SDK를 `8.x`로 업데이트하기 전에 `7.x` 최신 버전으로 먼저 업그레이드할 것을 권장합니다. `7.x`의 대부분의 deprecated 항목을 수정하려면 [`@sentry/migr8`](https://www.npmjs.com/package/@sentry/migr8) codemod를 사용해 SDK 사용 코드를 자동으로 업데이트할 수 있습니다. `@sentry/migr8`는 Node 18+가 필요합니다.

```bash
npx @sentry/migr8@latest
```

마이그레이션 도구를 사용하면 실행할 업데이트를 선택하고 코드를 자동으로 업데이트할 수 있습니다. 일부 경우에는 코드를 자동으로 변경할 수 없으며, 이때는 `TODO(sentry)` 주석으로 표시됩니다. `@sentry/migr8` 실행 후에는 모든 코드 변경 사항을 반드시 검토하세요! deprecated 항목에 대한 자세한 내용은 [Deprecations in 7.x](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md) 문서를 참고하세요. `@sentry/migr8`가 있더라도 마이그레이션 가이드를 읽는 것을 권장합니다. `@sentry/migr8`는 마이그레이션에 필요한 모든 변경 사항을 다루지는 않습니다.

## [`8.x`로 업그레이드](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#upgrading-to-8x)

`8.x`는 Sentry Next.js SDK 초기화를 단순화하고 트레이싱을 위해 Next.js OpenTelemetry 계측을 활용합니다.

[Important Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#important-changes)는 모든 SDK 사용자에게 영향을 주므로 전체를 읽어보시길 권장합니다. 아래에 연결된 [Other Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#other-changes)는 더 맞춤화된 계측을 사용하는 사용자에게만 영향을 줍니다. 일반적인 이슈를 위한 [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#troubleshooting) 섹션도 있습니다.

GitHub에도 SDK 소스 코드와 함께 모든 변경 사항을 포괄적으로 정리한 [상세 마이그레이션 가이드](https://github.com/getsentry/sentry-javascript/blob/develop/MIGRATION.md#upgrading-from-7x-to-8x)가 있습니다.

## [Important Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#important-changes)

- [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#supported-versions)

Sentry Next.js SDK `8.x`는 다음을 지원합니다:

* Next.js 버전 `13.2.0` 이상
* Webpack `5.0.0` 이상
* Node `14.18.0` 이상

더 오래된 Node.js 또는 Next.js 버전을 지원해야 한다면 Sentry Next.js SDK `7.x`를 사용하세요.

이제 SDK는 ES2018 호환성과 [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis) 지원이 필요합니다. 최소 지원 브라우저 버전은 다음과 같습니다:

* Chrome 71
* Edge 79
* Safari 12.1, iOS Safari 12.2
* Firefox 65
* Opera 58
* Samsung Internet 10

IE11을 지원하려면 babel 또는 유사한 도구를 사용해 코드를 ES5로 트랜스파일하고 필요한 polyfill을 추가하세요.

- [업데이트된 SDK 초기화](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-sdk-initialization)

`8.x`에서는 서버 사이드 SDK 초기화를 위해 `sentry.server.config.js|ts` 및 `sentry.edge.config.js|ts` 모듈을 실행할 수 있도록 추가 `instrumentation.ts` 파일이 필요합니다. `instrumentation.ts` 파일은 [instrumentation hook](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)이라 불리는 Next.js 네이티브 API입니다.

Next.js instrumentation hook 사용을 시작하려면 다음 단계를 따르세요:

1. 먼저 `next.config.js`에서 [`experimental.instrumentationHook`](https://nextjs.org/docs/app/api-reference/next-config-js/instrumentationHook)을 true로 설정해 Next.js instrumentation hook을 활성화하세요. (이 단계는 Next.js 15부터 더 이상 필요하지 않습니다)

`next.config.js`

```JavaScript
module.exports = {

  experimental: {
    instrumentationHook: true, // Not required on Next.js 15+
  },

}
```

2. 다음으로 프로젝트 루트 디렉터리(또는 `src` 폴더를 사용 중이라면 그곳)에 `instrumentation.ts|js` 파일을 만드세요.

3. 이제 `instrumentation.ts|js` 파일에서 register 함수를 export하고 `sentry.server.config.js|ts` 및 `sentry.edge.config.js|ts` 모듈을 import하세요:

`instrumentation.js`

```JavaScript
import * as Sentry from '@sentry/nextjs';

export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./sentry.server.config');
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./sentry.edge.config');
  }
}
```

[Next.js custom server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server)를 사용하는 경우 `instrumentation.ts|js` hook은 Next.js에서 호출되지 않으므로 SDK 계측이 예상대로 동작하지 않습니다. 자세한 내용은 [troubleshooting section](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#nextjs-custom-server)을 참고하세요.

8.x에서 서버의 `@sentry/nextjs`는 완전히 개편되었습니다. 이제 내부적으로 [OpenTelemetry](https://opentelemetry.io/) 기반으로 동작합니다. Sentry를 사용하기 위해 OpenTelemetry를 알거나 이해할 필요는 없습니다. OpenTelemetry 설정은 내부에서 처리됩니다. OpenTelemetry 네이티브 API를 사용해 span을 시작하면 Sentry가 모든 것을 자동으로 수집합니다.

이제 다음 통합을 설정 없이 바로 지원합니다:

* `httpIntegration`: Node http 및 https 표준 라이브러리를 자동 계측
* `nativeNodeFetchIntegration`: 최상위 fetch 및 undici를 자동 계측
* `graphqlIntegration`: GraphQL을 자동 계측
* `mongoIntegration`: MongoDB를 자동 계측
* `mongooseIntegration`: Mongoose를 자동 계측
* `mysqlIntegration`: MySQL을 자동 계측
* `mysql2Integration`: MySQL2를 자동 계측
* `postgresIntegration`: PostgreSQL을 자동 계측

- [업데이트된 `withSentryConfig` 사용법](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-withsentryconfig-usage)

Sentry Next.js SDK `8.x`에서는 `withSentryConfig`가 더 이상 3개의 인자를 받지 않습니다. 두 번째 인자(Sentry Webpack plugin 옵션)와 세 번째 인자(SDK 빌드 타임 구성 옵션)는 이제 하나로 전달해야 합니다:

`next.config.js`

```JavaScript
const nextConfig = {
  // Your Next.js options...
};

-module.exports = withSentryConfig(
-  nextConfig,
-  {
-    // Your Sentry Webpack Plugin Options...
-  },
-  {
-    // Your Sentry SDK options...
-  },
-);
+module.exports = withSentryConfig(nextConfig, {
+  // Your Sentry Webpack Plugin Options...
+  // AND your Sentry SDK options...
+});
```

이 변경의 일환으로 SDK는 더 이상 `sentry` 속성을 가진 Next.js 옵션을 `withSentryConfig`에 전달하는 방식을 지원하지 않습니다. 대신 SDK 설정에는 `withSentryConfig`의 두 번째 인자를 사용하세요.

`next.config.js`

```JavaScript
 const nextConfig = {
   // Your Next.js options...
-
-  sentry: {
-    // Your Sentry SDK options...
-  },
 };

 module.exports = withSentryConfig(nextConfig, {
   // Your Sentry Webpack Plugin Options...
+  // AND your Sentry SDK options...
 });
```

- [새로운 Tracing API](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#new-tracing-apis)

Tracing용 Custom Instrumentation API가 `8.x`에서 개편되었습니다. 새로운 메서드가 도입되었고, `startTransaction` 및 `span.startChild`는 제거되었습니다. 자세한 내용은 [new Tracing APIs docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md)를 참고하세요.

## [Other Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#other-changes)

- [개선된 Source Map 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#improved-source-map-uploading)

내부적으로 Next.js SDK는 source map 업로드와 이벤트에 릴리스 자동 연결/추가를 위해 [Sentry Webpack Plugin](https://www.npmjs.com/package/@sentry/webpack-plugin)을 사용합니다. `8.x`에서는 SDK가 Sentry Webpack Plugin `2.x`를 사용하며, 많은 개선과 버그 수정이 포함됩니다. 이제 Next.js SDK의 source map 업로드는 [Debug IDs](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/debug-ids.md)를 사용합니다.

- [deprecated API 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-deprecated-api)

다음의 기존 deprecated API가 `@sentry/nextjs` 패키지에서 제거되었습니다:

* `nextRouterInstrumentation`은 제거되었으며 `browserTracingIntegration`을 사용해야 합니다.

`sentry.client.config.js`

```JavaScript
 import * as Sentry from '@sentry/nextjs';

 Sentry.init({
   dsn: '___PUBLIC_DSN___',
   integrations: [
-    new Sentry.Integrations.BrowserTracing({
-      routingInstrumentation: Sentry.nextRouterInstrumentation
-    }),
+    Sentry.browserTracingIntegration(),
   ]
 });
```

* `withSentryApi`는 제거되었으며 `wrapApiHandlerWithSentry`를 사용해야 합니다.

`pages/api/*`

```JavaScript
-import { withSentryApi } from "@sentry/nextjs";
+import { wrapApiHandlerWithSentry } from "@sentry/nextjs";

 const handler = (req, res) => {
   res.status(200).json({ name: "John Doe" });
 };

-export default withSentryApi(handler, "/api/myRoute");
+export default wrapApiHandlerWithSentry(handler, "/api/myRoute");
```

* `withSentryGetServerSideProps`는 제거되었으며 `wrapGetServerSidePropsWithSentry`를 사용해야 합니다.

`pages/index.js`

```JavaScript
-import { withSentryGetServerSideProps } from "@sentry/nextjs";
+import { wrapGetServerSidePropsWithSentry } from "@sentry/nextjs";

 export async function _getServerSideProps() {
   // Fetch data from external API
 }

-export const getServerSideProps = withSentryGetServerSideProps(_getServerSideProps);
+export const getServerSideProps = wrapGetServerSidePropsWithSentry(_getServerSideProps);
```

* `withSentryGetStaticProps`는 제거되었으며 `wrapGetStaticPropsWithSentry`를 사용해야 합니다.

`pages/index.js`

```JavaScript
-import { withSentryGetStaticProps } from "@sentry/nextjs";
+import { wrapGetStaticPropsWithSentry } from "@sentry/nextjs";

 export async function _getStaticProps() {
   // Fetch data from external API
 }

-export const getStaticProps = withSentryGetStaticProps(_getServerSideProps);
+export const getStaticProps = wrapGetStaticPropsWithSentry(_getServerSideProps);
```

* `withSentryServerSideGetInitialProps`는 제거되었으며 `wrapGetInitialPropsWithSentry`를 사용해야 합니다.

`pages/index.js`

```JavaScript
-import { withSentryServerSideGetInitialProps } from "@sentry/nextjs";
+import { wrapGetInitialPropsWithSentry } from "@sentry/nextjs";

 async function getInitialProps() {
   // Fetch data from external API
   return { data }
 }

-Page.getInitialProps = withSentryServerSideGetInitialProps(getInitialProps);
+Page.getInitialProps = wrapGetInitialPropsWithSentry(getInitialProps);

 export default function Page({ data }) {
   return data
 }
```

위 변경과 유사하게 다음 API도 제거되었습니다:

* `withSentryServerSideAppGetInitialProps`는 제거되었으며 `wrapAppGetInitialPropsWithSentry`를 사용해야 합니다.
* `withSentryServerSideDocumentGetInitialProps`는 제거되었으며 `wrapDocumentGetInitialPropsWithSentry`를 사용해야 합니다.
* `withSentryServerSideErrorGetInitialProps`는 제거되었으며 `wrapErrorGetInitialPropsWithSentry`를 사용해야 합니다.

`IS_BUILD` 및 `isBuild` export는 제거되었습니다. 이 export들에 대한 대체 항목은 없습니다.

- [OpenTelemetry 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#opentelemetry-instrumentation)

이제 Next.js SDK는 트레이싱을 위해 Next.js OpenTelemetry 계측을 활용합니다. 즉, 추가 설정 없이 Next.js 애플리케이션의 OpenTelemetry 데이터를 SDK가 자동으로 수집합니다.

이전에 `@sentry/opentelemetry-node`를 사용했다면 더 이상 필요하지 않으며 프로젝트에서 제거할 수 있습니다. `@sentry/opentelemetry-node` 사용에서 Next.js SDK로 마이그레이션하려면 다음 단계를 따르세요:

1. 위의 [업데이트된 SDK 초기화](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-sdk-initialization) 섹션에 따라 SDK 초기화를 업데이트했는지 확인하세요.

2. 서버 사이드 SDK 초기화의 `Sentry.init` 호출에서 `instrumenter: "otel",`을 제거하세요.

`sentry.server.config.js`

```JavaScript
 import * as Sentry from '@sentry/nextjs';

 Sentry.init({
   dsn: '___PUBLIC_DSN___',
-  instrumenter: 'otel',
 });
```

3. 프로젝트에서 `@sentry/opentelemetry-node` 패키지와 `instrumentation.node.js|ts` 파일을 제거하세요. 또한 `instrumentation.js|ts`가 더 이상 `instrumentation.node.js|ts` 파일을 import하지 않는지 확인하세요.

- [개편된 Application Not Responding 감지](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#revamped-application-not-responding-detection)

`enableAnrDetection` 및 `Anr` class export가 SDK에서 제거되었습니다. 대신 이제 `Sentry.anrIntegration`을 사용해 [Application Not Responding detection](https://docs.sentry.io/platforms/javascript/guides/node/configuration/application-not-responding.md)을 활성화할 수 있습니다.

```JavaScript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [

    Sentry.anrIntegration({ captureStackTrace: true })

  ],
});
```

- [Node.js의 `onUncaughtException` 핸들러와 함께 사용할 때의 동작](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#behaviour-in-combination-with-onuncaughtexception-handlers-in-nodejs)

이전에는 추가 `onUncaughtException`이 등록되어 프로세스 종료를 막을 수 있는 경우에도 SDK가 기본적으로 프로세스를 종료했습니다. `onUncaughtExceptionIntegration` 옵션에서 `exitEvenIfOtherHandlersAreRegistered: false`를 설정하면 이 동작을 비활성화할 수 있었습니다. 지금까지 이 옵션의 기본값은 `true`였습니다.

앞으로 `exitEvenIfOtherHandlersAreRegistered`의 기본값은 `false`가 됩니다. 즉, 다른 `onUncaughtException` 핸들러가 등록되어 있을 때 SDK가 프로세스를 종료하지 않습니다.

- [`deepReadDirSync` 메서드 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-deepreaddirsync-method)

`deepReadDirSync` 메서드는 SDK export에서 제거되었습니다. 대체 API는 없습니다.

- [`Sentry.Handlers.trpcMiddleware()` 제거 및 `Sentry.trpcMiddleware()`로 대체](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryhandlerstrpcmiddleware-in-favor-of-sentrytrpcmiddleware)

Sentry tRPC 미들웨어가 `Sentry.Handlers.trpcMiddleware()`에서 `Sentry.trpcMiddleware()`로 이동되었습니다.

#
- [클라이언트 사이드 health check 트랜잭션 필터 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-client-side-health-check-transaction-filters)

SDK는 더 이상 기본적으로 health check 트랜잭션을 필터링하지 않습니다. 대신 이 트랜잭션들은 Sentry로 전송되지만, 기본 설정에서는 여전히 Sentry 백엔드에서 드롭됩니다. Sentry 프로젝트 설정에서 이 드롭 동작을 비활성화할 수 있습니다. SDK 내에서 특정 트랜잭션을 계속 드롭하고 싶다면 `ignoreTransactions` SDK 옵션을 사용할 수 있습니다.

- [`@sentry/replay` 패키지 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryreplay-package)

`@sentry/replay` 패키지는 더 이상 필요하지 않습니다. 대신 관련 메서드를 SDK에서 직접 import할 수 있습니다. 또한 integration은 이제 클래스 기반이 아니라 함수 기반입니다.

```JavaScript
-import { Replay } from '@sentry/replay';
-
 Sentry.init({
   dsn: '___PUBLIC_DSN___',
   integrations: [
-    new Replay(),
+    Sentry.replayIntegration(),
   ],
 });
```

- [Replay 기본 옵션 변경 (`unblock` 및 `unmask`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#change-of-replay-default-options-unblock-and-unmask)

Replay 옵션 `unblock`과 `unmask`의 기본값이 이제 `[]`입니다. 즉, 이 옵션들을 사용하려면 다음처럼 명시적으로 설정해야 합니다:

```JavaScript
Sentry.init({
  integrations: [
    Sentry.replayIntegration({
      unblock: [".sentry-unblock, [data-sentry-unblock]"],
      unmask: [".sentry-unmask, [data-sentry-unmask]"],
    }),
  ],
});
```

- [`makeXHRTransport` transport 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-makexhrtransport-transport)

`makeXHRTransport`를 통한 xhr transport는 제거되었습니다. 이제 `makeFetchTransport`만 사용할 수 있습니다. 즉, Sentry SDK가 동작하려면 환경에서 `fetch` API를 사용할 수 있어야 합니다.

- [`Offline` integration 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-the-offline-integration)

`Offline` integration은 [offline transport wrapper](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/transports.md#makebrowserofflinetransport)로 대체되어 제거되었습니다.

- [`wrap` export 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-wrap-export)

`Sentry.wrap` export가 제거되었습니다. 대체 API는 없습니다.

- [브라우저에서 `tracePropagationTargets` 동작 변경](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-behaviour-of-tracepropagationtargets-in-the-browser)

`tracePropagationTargets` 옵션이 정의되지 않았을 때 SDK 동작을 업데이트했습니다. 다시 말해, 어떤 outgoing request에 tracing HTTP 헤더를 붙일지 SDK에 알려주기 위해 URL과 매칭할 문자열 또는 RegEx 목록을 제공할 수 있습니다. 이 tracing 헤더는 분산 추적에 사용됩니다.

이전에는 브라우저에서 `tracePropagationTargets`를 정의하지 않으면 기본값이 `['localhost', /^\/(?!\/)/]`였습니다. 즉 URL에 "localhost"가 포함되거나 `/`로 시작하는 모든 요청 대상에 tracing 헤더가 붙었습니다. 이 기본값은 브라우저 애플리케이션의 CORS 오류를 방지하기 위해 선택되었습니다. 하지만 이 기본값에는 몇 가지 문제가 있었습니다.

앞으로는 `tracePropagationTargets` 옵션을 설정하지 않으면, 동일한 origin의 모든 outgoing request에 tracing 헤더가 붙습니다. 예를 들어 `https://example.com/`에서 `https://example.com/api`로 요청을 보내면 해당 요청은 추적됩니다(즉 trace 헤더가 첨부됨). `https://api.example.com/`에 대한 요청은 다른 origin이므로 추적되지 않습니다. `localhost`에서 실행되는 모든 애플리케이션도 동일하게 적용됩니다.

`tracePropagationTargets` 옵션을 제공하면, 이제 정의한 모든 항목이 outgoing request의 전체 URL과 매칭됩니다. 이전에는 request API를 호출할 때 사용한 값하고만 매칭되었습니다. 예를 들어 `fetch("/api/posts")` 같은 요청을 보냈다면, 제공한 `tracePropagationTargets`는 `"/api/posts"`와만 비교되었습니다.

- [`Hub` 및 `getCurrentHub()` 사용 중단(deprecation)](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#deprecation-of-hub-and-getcurrenthub)

`Hub`는 지금까지 Sentry SDK API에서 매우 중요한 부분이었습니다. Hub는 스레드 간 데이터를 추적하고 코드의 특정 부분에 데이터를 스코프하기 위한 SDK의 "동시성 단위(unit of concurrency)"였습니다. 하지만 고급 사용자에게도 과하게 복잡하고 혼란을 주기 때문에, 새로운 API 집합인 "new Scope API"로 대체될 예정입니다. 현재는 `Hub`와 `getCurrentHub`를 계속 사용할 수 있지만, 다음 메이저 버전에서 제거될 예정입니다.

기존 Hub API 사용을 어떻게 대체할지에 대한 자세한 내용은 [Deprecate Hub](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-hub)를 참고하세요.

- [클래스 기반 integration 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-class-based-integrations)

v7에서 integration은 클래스였고 예를 들어 `integrations: [new Sentry.Replay()]`처럼 추가할 수 있었습니다. v8에서는 integration이 더 이상 클래스가 아니라 함수가 됩니다. 클래스 방식 사용과 `Integrations.XXX` 해시를 통한 접근 모두, 새로운 함수형 integration 사용으로 대체되며 사용 중단(deprecated)되었습니다. 예를 들어 `new Integrations.LinkedErrors()`는 `linkedErrorsIntegration()`이 됩니다.

integration 목록과 대체 항목은 [the `7.x` deprecation documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-class-based-integrations)을 참고하세요.

- [`Sentry.configureScope` 메서드 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryconfigurescope-method)

최상위 `Sentry.configureScope` 함수가 제거되었습니다. 대신 `Sentry.getCurrentScope()`를 사용해 현재 scope에 접근하고 변경해야 합니다.

```JavaScript
- Sentry.configureScope((scope) => {
-  scope.setTag("key", "value");
- });
+ Sentry.getCurrentScope().setTag("key", "value");
```

- [`tracingOrigins`가 `tracePropagationTargets`로 대체됨](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#tracingorigins-has-been-replaced-by-tracepropagationtargets)

`tracingOrigins`는 제거되었고 `tracePropagationTargets` 옵션으로 대체되었습니다. `tracePropagationTargets` 옵션은 `Sentry.init()` 옵션에 설정하거나, 커스텀 `Client`를 생성하는 경우 해당 옵션에 설정해야 합니다.

```TypeScript
Sentry.init({
  dsn: "___DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: ["localhost", "example.com"],
});
```

- [Metrics 설정 단순화](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#simplification-of-metrics-configuration)

`7.x`에서는 `_experiments` 옵션을 `{ metricsAggregator: true }`로 설정해 metrics aggregator를 활성화해야 했습니다. 또한 브라우저 환경에서는 `metricsAggregatorIntegration`을 `integrations` 배열에 추가해야 했습니다.

```TypeScript
// v7 - Server (Node/Deno/Bun)
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  _experiments: {
    metricsAggregator: true,
  },
});

// v7 - Browser
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.metricsAggregatorIntegration()],
});

Sentry.metrics.increment("my_metric");
```

`8.x`에서는 metrics API를 사용하기 위해 추가 설정이 필요하지 않습니다.

```ts
// v8
Sentry.init({
  dsn: "___PUBLIC_DSN___",
});

Sentry.metrics.increment("my_metric");
```

- [Severity Enum 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-severity-enum)

`7.x`에서는 번들 크기 절감을 위해 `Severity` enum 대신 `SeverityLevel` 타입 사용을 권장하며 `Severity` enum을 사용 중단 처리했습니다. 이것이 `8.x`에서 제거되었습니다. 이제 `SeverityLevel` 타입을 직접 사용해야 합니다.

```JavaScript
- import { Severity } from '@sentry/types';
+ import { SeverityLevel } from '@sentry/types';

- const level = Severity.error;
+ const level: SeverityLevel = "error";
```

#
- [`spanStatusfromHttpCode` 제거 및 `getSpanStatusFromHttpCode`로 대체](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-spanstatusfromhttpcode-in-favour-of-getspanstatusfromhttpcode)

`8.x`에서는 `spanStatusfromHttpCode` 함수를 제거하고 `getSpanStatusFromHttpCode`를 사용합니다.

```JavaScript
- const spanStatus = spanStatusfromHttpCode(200);
+ const spanStatus = getSpanStatusFromHttpCode(200);
```

- [`framesToPop`이 파싱된 프레임에 적용됨](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#framestopop-applies-to-parsed-frames)

`framesToPop` 속성이 있는 에러는 스택 상단에서 지정한 수만큼 프레임이 제거됩니다. 이는 v7에서 `framesToPop` 속성이 스택 문자열의 상단 n줄을 제거하는 데 사용되던 동작과 달라진 점입니다.

- [SDK 패키지에서 `Span` 클래스 export 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-span-class-export-from-sdk-packages)

`8.x`에서는 SDK 패키지에서 `Span` 클래스를 더 이상 export하지 않습니다. 내부적으로 이 클래스는 이제 `SentrySpan`이라고 불리며, 사용자에게 직접 사용하도록 의도되지 않았습니다.

- [transport 반환 타입에서 `void` 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-void-from-transport-return-types)

`Transport` 인터페이스의 `send` 메서드는 이제 promise에서 항상 `TransportMakeRequestResponse`를 반환해야 합니다. 즉, 더 이상 `void` 반환 타입은 허용되지 않습니다.

```TypeScript
// v7
 interface Transport {
-  send(event: Event): Promise<void | TransportMakeRequestResponse>;
+  send(event: Event): Promise<TransportMakeRequestResponse>;
 }
```

- [`extraErrorDataIntegration` 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#extraerrordataintegration-changes)

`extraErrorDataIntegration` integration은 이제 기본적으로 [`error.cause`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)를 확인합니다.

- [`transactionContext`가 더 이상 `tracesSampler`에 전달되지 않음](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#transactioncontext-no-longer-passed-to-tracessampler)

앞으로 `transactionContext`를 `tracesSampler` 콜백에 전달하는 대신, 콜백이 `name`과 `attributes`를 직접 받게 됩니다. `attributes`는 span 생성 시점의 속성만 포함하며, 일부 속성은 span 라이프사이클 후반에 설정될 수 있으므로(따라서 샘플링 시점에는 사용할 수 없음) 주의해야 합니다.

- [`getClient()`는 항상 client를 반환](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#getclient-always-returns-a-client)

이제 `Sentry.init()`이 호출되었다면 `getClient()`는 항상 client를 반환합니다. 따라서 Sentry가 실제로 초기화되었는지 확인하는 용도로 `getClient()`를 사용하는 방식은 더 이상 동작하지 않습니다. 대신 새 유틸리티인 `Sentry.isInitialized()`를 사용해 확인해야 합니다.

- [`addGlobalEventProcessor` 제거 및 `addEventProcessor`로 대체](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-addglobaleventprocessor-in-favour-of-addeventprocessor)

`8.x`에서는 `addGlobalEventProcessor` 함수를 제거하고 `addEventProcessor`를 사용합니다.

```JavaScript
- Sentry.addGlobalEventProcessor((event) => {
+ Sentry.getGlobalScope().addEventProcessor((event) => {
   delete event.extra;
   return event;
 });
```

- [`@sentry/integrations` 패키지 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryintegrations-package)

`@sentry/integrations`는 제거되었으며 더 이상 배포되지 않습니다. 플러그형 integration은 별도 패키지(`@sentry/integrations`)에서 `@sentry/nextjs`로 이동했습니다. 또한 이제 클래스가 아닌 함수입니다.

클라이언트 사이드 init을 위해 이제 `@sentry/nextjs`에서 export되는 integration:

* `httpClientIntegration` (`HTTPClient`)
* `contextLinesIntegration` (`ContextLines`)
* `reportingObserverIntegration` (`ReportingObserver`)

클라이언트 사이드 및 서버 사이드 init을 위해 이제 `@sentry/nextjs`에서 export되는 integration:

* `captureConsoleIntegration` (`CaptureConsole`)
* `debugIntegration` (`Debug`)
* `extraErrorDataIntegration` (`ExtraErrorData`)
* `rewriteFramesIntegration` (`RewriteFrames`)
* `sessionTimingIntegration` (`SessionTiming`)
* `dedupeIntegration` (`Dedupe`) - 참고: 기본 활성화되어 있으며 플러그형이 아님

`Transaction` integration은 `@sentry/integrations`에서 제거되었습니다. 대체 API는 없습니다.

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#troubleshooting)

- [`sentry.server.config.js|ts` 및 `sentry.edge.config.js|ts` 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryserverconfigjsts-and-sentryedgeconfigjsts)

Next.js SDK `8.x` 업데이트에서는 SDK를 초기화하는 더 유연하고 강력한 방식인 `instrumentation.ts` 파일 사용을 강제합니다. 이를 통해 Next.js 내장 훅과 OpenTelemetry 계측을 사용할 수 있습니다. 또한 Next.js SDK `7.x`에서 지원되지 않는 [Turbopack](https://turbo.build/pack)과의 호환성도 개선됩니다. Next.js 팀은 SDK 초기화에 `instrumentation.ts` 파일 사용을 권장하며, 저희도 SDK가 Next.js와 매끄럽게 동작하도록 긴밀히 협력하고 있습니다.

- [Next.js 커스텀 서버](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#nextjs-custom-server)

[Next.js 커스텀 서버](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server)를 사용하는 경우, `instrumentation.ts|js` 훅은 Next.js에서 호출되지 않으므로 서버 코드 내부에서 직접 호출해야 합니다. 애플리케이션 라이프사이클에서 가능한 한 이른 시점에 호출하는 것을 권장합니다.

다음은 [Next.js documentation](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server)의 커스텀 서버 예제에 Sentry 초기화 코드를 추가한 예시입니다:

```JavaScript
// make sure that Sentry is imported and initialized before any other imports.

+ const Sentry = require('@sentry/nextjs');
+
+ Sentry.init({
+   dsn: '___PUBLIC_DSN___',
+   // Your Node.js Sentry configuration...
+ })

const { createServer } = require('http')
const { parse } = require('url')
const next = require('next')

const dev = process.env.NODE_ENV !== 'production'
const hostname = 'localhost'
const port = 3000

const app = next({ dev, hostname, port })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer(async (req, res) => {
    // server code
  })
    .once('error', (err) => {
      // error code
    })
    .listen(port, () => {
      console.log(`> Ready on http://${hostname}:${port}`)
    })
})
```

## 이 섹션의 페이지

- [새로운 Tracing API](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md)
- [7.x의 사용 중단 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md)

