---
title: 'Pages Router 설정 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router

# Pages Router 설정 | Next.js용 Sentry

가장 빠르게 설정하려면 [wizard installer](https://docs.sentry.io/platforms/javascript/guides/nextjs.md) 사용을 권장합니다.

이 가이드는 **Pages Router를 사용하는 Next.js 애플리케이션**의 수동 설정을 다룹니다. 다른 설정은 다음을 참고하세요.

* [App Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md) - App Router를 사용하는 애플리케이션용 (Next.js 15+)
* [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md) - Turbopack을 사용하지 않는 애플리케이션용

## [사전 요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#prerequisites)

필요한 항목:

* Next.js 애플리케이션
* Sentry [계정](https://sentry.io/signup/) 및 [프로젝트](https://docs.sentry.io/product/projects.md)

설정할 기능을 선택하세요.

오류 모니터링\[x]로그\[ ]세션 리플레이\[x]트레이싱

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#install)

- [Sentry SDK 설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#install-the-sentry-sdk)

사용 중인 패키지 매니저에 맞는 명령어를 실행해 애플리케이션에 Sentry SDK를 추가하세요.

```bash
npm install @sentry/nextjs --save
```

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#configure)

- [앱에 계측 적용](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#apply-instrumentation-to-your-app)

`next.config.ts`(또는 `next.config.js`) 파일에 `withSentryConfig`를 추가해 앱의 기본 Next.js 옵션을 확장하세요.

Pages Router 애플리케이션은 일반적으로 Webpack을 사용합니다. Webpack 구성에는 API 라우트와 페이지 데이터 페칭 메서드를 자동으로 래핑하는 자동 계측 옵션이 포함되어 있습니다.

`next.config.ts`

```typescript
import type { NextConfig } from "next";
import { withSentryConfig } from "@sentry/nextjs";

const nextConfig: NextConfig = {
  // Your existing Next.js configuration
};

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Only print logs for uploading source maps in CI
  silent: !process.env.CI,

  // Webpack-specific options for Pages Router
  webpack: {
    // Auto-instrument API routes and data fetching methods (default: true)
    autoInstrumentServerFunctions: true,

    // Auto-instrument middleware (default: true)
    autoInstrumentMiddleware: true,

    // Tree-shake Sentry logger statements to reduce bundle size
    treeshake: {
      removeDebugLogging: true,
    },
  },
});
```

- [Sentry SDK 초기화](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#initialize-sentry-sdks)

애플리케이션 루트 디렉터리(또는 `src` 폴더가 있다면 해당 폴더)에 다음 파일을 생성하세요.

* `sentry.client.config.ts` - 클라이언트 측 SDK 초기화
* `sentry.server.config.ts` - 서버 측 SDK 초기화
* `sentry.edge.config.ts` - Edge 런타임 SDK 초기화(Edge 라우트를 사용하는 경우)

##### 팁

이 파일들에 DSN을 직접 포함하거나 `NEXT_PUBLIC_SENTRY_DSN` 같은 *public* 환경 변수를 사용하세요.

`sentry.client.config.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Capture 100% in dev, 10% in production
  // Adjust based on your traffic volume
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  integrations: [
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
  ],
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

##### 프로덕션 환경에 맞게 샘플링 비율 조정

[사용량 통계](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans)를 모니터링하고 트래픽 규모에 따라 `tracesSampleRate`를 조정하세요. [샘플링 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md)에 대해 더 알아보세요.

- [Pages Router 오류 수집](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#capture-pages-router-errors)

서버 사이드 렌더링 중 또는 페이지 컴포넌트에서 발생하는 오류를 수집하도록 `pages/_error.tsx`를 생성하거나 업데이트하세요.

`getInitialProps` 메서드는 오류를 비동기로 수집하므로, 서버리스 함수가 종료되기 전에 Sentry가 오류를 전송할 시간을 확보할 수 있습니다.

`_error.tsx`

```tsx
import * as Sentry from "@sentry/nextjs";
import type { NextPage } from "next";
import type { ErrorProps } from "next/error";
import Error from "next/error";

const CustomErrorComponent: NextPage<ErrorProps> = (props) => {
  return <Error statusCode={props.statusCode} />;
};

CustomErrorComponent.getInitialProps = async (contextData) => {
  // In case this is running in a serverless function, await this in order to give Sentry
  // time to send the error before the lambda exits
  await Sentry.captureUnderscoreErrorException(contextData);

  // This will contain the status code of the response
  return Error.getInitialProps(contextData);
};

export default CustomErrorComponent;
```

- [소스 맵(선택 사항)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#source-maps-optional)

읽기 쉬운 스택 트레이스를 활성화하려면 `next.config.ts`에 `authToken` 옵션을 추가하세요. CI/CD에서 `SENTRY_AUTH_TOKEN` 환경 변수를 설정하세요.

##### 중요

인증 토큰은 비밀로 유지하고 버전 관리에 포함하지 마세요.

`next.config.ts`

```typescript
export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Pass the auth token
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Upload a larger set of source maps for prettier stack traces
  widenClientFileUpload: true,
});
```

## [오류 모니터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#error-monitoring)

오류를 발생시켜 Sentry에서 확인해 오류 모니터링 설정을 테스트하세요.

- [테스트 오류 발생시키기](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#throw-a-test-error)

아무 페이지에나 이 버튼을 추가하고 클릭해 테스트 오류를 트리거하세요.

`pages/index.tsx`

```tsx
export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        throw new Error("Sentry Test Error");
      }}
    >
      Throw Test Error
    </button>
  );
}
```

- [검증](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#verify)

Sentry에서 [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/)를 열어 테스트 오류를 확인하세요. [오류 수집에 대해 더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/usage.md).

## [추가 기능 검증](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#verify-additional-features)

위에서 선택한 기능을 기준으로 각각이 정상 동작하는지 검증하세요.

- [세션 리플레이](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#session-replay)

세션 리플레이는 사용자 세션을 동영상처럼 재현해 수집합니다. 클라이언트 구성의 `replayIntegration()`으로 설정합니다.

**검증:** 오류를 트리거하거나 앱을 탐색한 뒤, Sentry의 [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/)를 확인하세요.

`sentry.client.config.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [Sentry.replayIntegration()],

  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

- [트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#tracing)

트레이싱은 SDK 초기화 파일의 `tracesSampleRate`로 설정합니다. Next.js 라우트와 API 호출은 자동으로 계측됩니다.

**검증:** 아무 페이지로 이동한 뒤, Sentry의 [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/)를 확인하세요.

`sentry.server.config.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
});
```

- [로그 NEW](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#logs-)

로그는 SDK 구성에서 `enableLogs: true`로 활성화됩니다. Sentry 로거를 사용해 구조화된 로그를 전송하세요.

**검증:** 로그 구문을 추가해 트리거한 뒤, Sentry의 [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/)를 확인하세요.

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Warning message");
Sentry.logger.error("Error occurred");
```

## [Vercel Cron 작업(선택 사항)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#vercel-cron-jobs-optional)

[Vercel cron jobs](https://vercel.com/docs/cron-jobs)에 대해 Sentry에서 [Cron Monitors](https://docs.sentry.io/product/crons.md)를 자동 생성하세요.

- [자동 Cron 모니터링 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md#enable-automatic-cron-monitoring)

`next.config.ts`에 `automaticVercelMonitors` 옵션을 추가하세요.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  automaticVercelMonitors: true,
});
```

## 하이브리드 앱 (App Router + Pages Router)

애플리케이션이 App Router와 Pages Router를 모두 사용하는 경우:

1. App Router 컴포넌트에는 [App Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md)을 따르세요.
2. Pages Router 오류 처리를 위해 이 가이드의 `pages/_error.tsx` 파일을 추가하세요.
3. 두 라우터는 동일한 Sentry 구성 파일을 공유합니다.

Sentry SDK는 사용 중인 라우터를 자동으로 감지하고 적절한 계측을 적용합니다.

## 다음 단계

* [Logs Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Pino, Winston, Bunyan 같은 인기 로깅 라이브러리 연결
* [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - 서비스 및 마이크로서비스 전반에서 요청 추적
* [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Vercel AI SDK, LangChain 등으로 구축한 AI 에이전트 모니터링
* [Connect GitHub + Seer](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - AI 기반 [근본 원인 분석](https://docs.sentry.io/product/ai-in-sentry/seer.md) 활성화
* [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - 확장 SDK 구성 옵션 살펴보기

SDK 설정에 문제가 있나요?

* 자동 설정을 위해 [installation wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)를 시도해 보세요.
* [지원 받기](https://sentry.zendesk.com/hc/en-us/)

