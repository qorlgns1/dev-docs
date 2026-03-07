---
title: "Next.js | Next.js용 Sentry"
description: "Sentry 마법사를 실행해 Next.js 애플리케이션에 Sentry를 자동으로 구성할 수 있습니다."
---

출처 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs

# Next.js | Next.js용 Sentry

## 사전 요구 사항

필요한 항목:

- Next.js 애플리케이션
- Sentry [계정](https://sentry.io/signup/) 및 [프로젝트](https://docs.sentry.io/product/projects.md)

## 설치

Sentry 마법사를 실행하면 Next.js 애플리케이션에 Sentry가 자동으로 구성됩니다:

```bash
npx @sentry/wizard@latest -i nextjs
```

마법사가 기능 선택을 요청합니다. 활성화할 기능을 선택하세요:

- 오류 모니터링 `[x]`
- 로그 `[ ]`
- 세션 리플레이 `[x]`
- 트레이싱

직접 설정하고 싶으신가요? [수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md) 가이드를 확인하세요.

## 마법사가 생성한 항목

마법사는 모든 Next.js 런타임 환경에 대해 Sentry를 구성하고, 설정을 테스트할 파일도 생성했습니다.

- [SDK 초기화](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#sdk-initialization)

Next.js는 서로 다른 환경에서 코드를 실행합니다. 마법사는 각 환경별로 별도의 초기화 파일을 생성합니다:

- **클라이언트** (`instrumentation-client.ts`) — 브라우저에서 실행
- **서버** (`sentry.server.config.ts`) — Node.js에서 실행
- **엣지** (`sentry.edge.config.ts`) — 엣지 런타임에서 실행

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // 사용자에 대한 요청 헤더와 IP를 추가합니다
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ session-replay
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  integrations: [
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
  ],
});
```

##### 프로덕션용 샘플링 비율 조정

위 예시는 개발 환경에서 트레이스의 100%, 프로덕션 환경에서 10%를 샘플링합니다. [사용량 통계](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans)를 모니터링하고 트래픽 규모에 따라 `tracesSampleRate`를 조정하세요. [샘플링 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md)에 대해 더 알아보세요.

- [서버 사이드 등록](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#server-side-registration)

`instrumentation.ts` 파일은 서버 및 엣지 구성을 Next.js에 등록합니다.

`instrumentation.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./sentry.server.config");
  }
  if (process.env.NEXT_RUNTIME === "edge") {
    await import("./sentry.edge.config");
  }
}

export const onRequestError = Sentry.captureRequestError;
```

- [Next.js 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#nextjs-configuration)

`next.config.ts`는 `withSentryConfig`로 감싸져 소스 맵 업로드, 터널링(광고 차단기 회피), 기타 빌드 시점 기능을 활성화합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // 읽기 쉬운 스택 트레이스를 위해 소스 맵을 업로드합니다
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Sentry 요청을 서버를 통해 전달합니다(광고 차단기 우회)
  tunnelRoute: "/monitoring",

  silent: !process.env.CI,
});
```

- [오류 처리](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#error-handling)

마법사는 App Router 애플리케이션에서 React 렌더링 오류를 캡처하기 위해 `app/global-error.tsx`를 생성합니다.

`app/global-error.tsx`

```tsx
"use client";

import * as Sentry from "@sentry/nextjs";
import { useEffect } from "react";

export default function GlobalError({
  error,
}: {
  error: Error & { digest?: string };
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html>
      <body>
        <h1>문제가 발생했습니다!</h1>
      </body>
    </html>
  );
}
```

- [소스 맵](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#source-maps)

마법사는 소스 맵 업로드용 auth token이 포함된 `.env.sentry-build-plugin`을 생성합니다. 이 파일은 자동으로 `.gitignore`에 추가됩니다.

CI/CD에서는 빌드 시스템에 `SENTRY_AUTH_TOKEN` 환경 변수를 설정하세요.

`.env.sentry-build-plugin`

```bash
SENTRY_AUTH_TOKEN=sntrys_eyJ...
```

- [예제 페이지](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#example-page)

마법사는 테스트 오류를 발생시키는 버튼이 있는 `/sentry-example-page`를 생성합니다. 이를 사용해 설정을 검증하세요.

```bash
app/
├── sentry-example-page/
│   └── page.tsx       # 오류 버튼이 있는 테스트 페이지
└── api/
    └── sentry-example-api/
        └── route.ts   # 테스트 API 라우트
```

## 설정 검증

##### 중요

브라우저 개발자 도구(예: 브라우저 콘솔) 내부에서 트리거된 오류는 샌드박싱되므로 Sentry 오류 모니터링을 트리거하지 않습니다.

예제 페이지는 한 번의 동작으로 활성화한 모든 기능을 테스트합니다:

1. 개발 서버를 시작하세요:

```bash
npm run dev
```

2. [localhost:3000/sentry-example-page](http://localhost:3000/sentry-example-page) 방문

3. **"샘플 오류 발생시키기"** 클릭

- [Sentry에서 데이터 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#check-your-data-in-sentry)

**오류** — [이슈 열기](https://sentry.io/orgredirect/organizations/:orgslug/issues/)

소스 코드를 가리키는 전체 스택 트레이스와 함께 "This is a test error"가 표시되어야 합니다.

**트레이싱** — [트레이스 열기](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/)

페이지 로드 트레이스와 버튼 클릭 span이 표시되어야 합니다. [사용자 정의 span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/custom-instrumentation.md)에 대해 더 알아보세요.

**세션 리플레이** — [리플레이 열기](https://sentry.io/orgredirect/organizations/:orgslug/replays/)

오류가 발생한 순간을 포함한 세션의 영상 같은 기록을 확인하세요. [Session Replay 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md)에 대해 더 알아보세요.

**로그** — [로그 열기](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/)

애플리케이션의 구조화된 로그 항목을 확인하세요. 어디서든 로그를 보낼 수 있습니다:

```typescript
Sentry.logger.info("사용자 동작", { userId: "123" });
Sentry.logger.warn("응답이 느립니다", { duration: 5000 });
Sentry.logger.error("작업이 실패했습니다", { reason: "timeout" });
```

[Logs 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md)에 대해 더 알아보세요.

SDK 설정 중 문제가 있나요?

- 설치 마법사에서 문제가 발생했다면 [Sentry 수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md)을 시도해 보세요
- 일반적인 문제는 [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md)을 확인하세요
- [지원 받기](https://sentry.io/support/)

## 다음 단계

Next.js 애플리케이션에 Sentry를 성공적으로 통합했습니다! 다음 항목을 살펴보세요:

- 설정 이후 무엇을 모니터링, 로깅, 추적, 조사할지에 대한 [실전 가이드](https://docs.sentry.io/guides.md) 살펴보기
- [로그 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Pino, Winston, Bunyan 같은 인기 로깅 라이브러리 연결
- [분산 트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - 서비스 및 마이크로서비스 전반에 걸친 요청 추적
- [AI 에이전트 모니터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Vercel AI SDK, LangChain 등으로 구축한 AI 에이전트 모니터링
- [GitHub + Seer 연결](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - GitHub 저장소를 연결해 AI 기반 [근본 원인 분석](https://docs.sentry.io/product/ai-in-sentry/seer.md) 활성화
- [구성 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - 확장 SDK 구성 옵션 살펴보기

## 기타 JavaScript 프레임워크

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md)
- [Connect](https://docs.sentry.io/platforms/javascript/guides/connect.md)
- [Cordova](https://docs.sentry.io/platforms/javascript/guides/cordova.md)
- [Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md)
- [Electron](https://docs.sentry.io/platforms/javascript/guides/electron.md)
- [Ember](https://docs.sentry.io/platforms/javascript/guides/ember.md)
- [Express](https://docs.sentry.io/platforms/javascript/guides/express.md)
- [Fastify](https://docs.sentry.io/platforms/javascript/guides/fastify.md)
- [Gatsby](https://docs.sentry.io/platforms/javascript/guides/gatsby.md)
- [Google Cloud Functions](https://docs.sentry.io/platforms/javascript/guides/gcp-functions.md)
- [Hapi](https://docs.sentry.io/platforms/javascript/guides/hapi.md)
- [Hono](https://docs.sentry.io/platforms/javascript/guides/hono.md)
- [Koa](https://docs.sentry.io/platforms/javascript/guides/koa.md)
- [Nest.js](https://docs.sentry.io/platforms/javascript/guides/nestjs.md)
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md)
- [Nuxt](https://docs.sentry.io/platforms/javascript/guides/nuxt.md)
- [React](https://docs.sentry.io/platforms/javascript/guides/react.md)
- [React Router Framework](https://docs.sentry.io/platforms/javascript/guides/react-router.md)
- [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## 주제

- [수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md)
- [오류 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md)
- [소스 맵](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md)
- [로그](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md)
- [세션 리플레이](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md)
- [트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)
- [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md)
- [Metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md)
- [사용자 피드백](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md)
- [샘플링](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md)
- [이벤트 보강](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md)
- [확장 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md)
- [OpenTelemetry 지원](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry.md)
- [기능 플래그](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md)
- [데이터 관리](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management.md)
- [보안 정책 보고](https://docs.sentry.io/platforms/javascript/guides/nextjs/security-policy-reporting.md)
- [특수 사용 사례](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices.md)
- [마이그레이션 가이드](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration.md)
- [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md)
