---
title: '수동 설정 | Next.js용 Sentry'
description: '가장 빠르게 설정하려면 wizard installer 사용을 권장합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup

# 수동 설정 | Next.js용 Sentry

가장 빠르게 설정하려면 [wizard installer](https://docs.sentry.io/platforms/javascript/guides/nextjs.md) 사용을 권장합니다.

이 가이드는 **Turbopack 및 App Router를 사용하는 Next.js 15+**의 수동 설정을 다룹니다. 다른 설정은 다음을 참고하세요.

* [Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md) - Pages Router를 사용하는 애플리케이션용
* [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md) - Turbopack을 사용하지 않는 애플리케이션용

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#prerequisites)

필요한 항목:

* Next.js 애플리케이션
* Sentry [account](https://sentry.io/signup/) 및 [project](https://docs.sentry.io/product/projects.md)

구성하려는 기능을 선택하세요.

오류 모니터링\[x]로그\[ ]세션 리플레이\[x]트레이싱\[ ]사용자 피드백

**이 가이드의 진행 방식:**

1. **Install** - 프로젝트에 Sentry SDK 추가
2. **Configure** - SDK 초기화 파일 및 Next.js 설정 구성
3. **Verify** - 오류 모니터링과 활성화한 추가 기능 테스트

## [Install](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#install)

- [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#install-the-sentry-sdk)

선호하는 패키지 매니저 명령어를 실행해 애플리케이션에 Sentry SDK를 추가하세요.

```bash
npm install @sentry/nextjs --save
```

## [Configure](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#configure)

- [Apply Instrumentation to Your App](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#apply-instrumentation-to-your-app)

`next.config.ts` 파일에 `withSentryConfig`를 추가해 앱의 기본 Next.js 옵션을 확장하세요.

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
});
```

- [Initialize Sentry SDKs](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#initialize-sentry-sdks)

애플리케이션 루트 디렉터리(또는 `src` 폴더가 있다면 그 폴더)에 다음 파일을 생성하세요.

* `instrumentation-client.ts` - 클라이언트 측 SDK 초기화
* `sentry.server.config.ts` - 서버 측 SDK 초기화
* `sentry.edge.config.ts` - Edge runtime SDK 초기화

##### 팁

이 파일들에 DSN을 직접 포함하거나, `NEXT_PUBLIC_SENTRY_DSN` 같은 *public* 환경 변수를 사용하세요.

`instrumentation-client.ts`

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
    // ___PRODUCT_OPTION_START___ user-feedback
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
    // ___PRODUCT_OPTION_END___ user-feedback
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

// ___PRODUCT_OPTION_START___ performance
// This export will instrument router navigations
export const onRouterTransitionStart = Sentry.captureRouterTransitionStart;
// ___PRODUCT_OPTION_END___ performance
```

##### 프로덕션용 샘플링 비율 조정

위 예시는 개발 환경에서 trace를 100%, 프로덕션에서 10% 샘플링합니다. [usage stats](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans)를 모니터링하고 트래픽 규모에 맞게 `tracesSampleRate`를 조정하세요. 자세한 내용은 [sampling configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md)을 참고하세요.

- [Register Server-Side SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#register-server-side-sdk)

프로젝트 루트(또는 `src` 폴더)에 `instrumentation.ts`라는 [Next.js Instrumentation file](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation)을 생성하세요. 이 파일은 서버 및 엣지 설정을 가져오고 서버 측 오류를 수집하기 위해 `onRequestError`를 내보냅니다.

`onRequestError` 훅은 `@sentry/nextjs` 버전 `8.28.0` 이상과 Next.js 15가 필요합니다.

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

// Capture errors from Server Components, middleware, and proxies
export const onRequestError = Sentry.captureRequestError;
```

- [Capture React Render Errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#capture-react-render-errors)

App Router 애플리케이션 어디에서든 발생하는 오류를 수집하려면 `app/global-error.tsx`를 생성하세요.

`global-error.tsx`

```tsx
"use client";

import * as Sentry from "@sentry/nextjs";
import NextError from "next/error";
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
        {/* `NextError` is the default Next.js error page component. Its type
        definition requires a `statusCode` prop. However, since the App Router
        does not expose status codes for errors, we simply pass 0 to render a
        generic error message. */}
        <NextError statusCode={0} />
      </body>
    </html>
  );
}
```

- [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#server-actions)

`Sentry.withServerActionInstrumentation()`으로 Server Actions를 감싸세요.

`app/actions.ts`

```typescript
"use server";
import * as Sentry from "@sentry/nextjs";
import { headers } from "next/headers";

export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm", // Action name for Sentry
    {
      headers: await headers(), // Connect client and server traces
      formData, // Attach form data to events
      recordResponse: true, // Include response data
    },
    async () => {
      // Your server action logic
      const result = await processForm(formData);
      return { success: true, data: result };
    },
  );
}
```

- [Source Maps (Optional)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#source-maps-optional)

가독성 있는 스택 트레이스를 활성화하려면 `next.config.ts`에 `authToken` 옵션을 추가하세요. CI/CD에서 `SENTRY_AUTH_TOKEN` 환경 변수를 설정하세요.

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

- [Tunneling (Optional)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#tunneling-optional)

이벤트를 Next.js 서버를 통해 라우팅해 광고 차단기가 Sentry 이벤트를 차단하지 못하게 하세요.

이 방식은 서버 부하를 증가시킵니다. 애플리케이션에 맞는 트레이드오프를 검토하세요.

터널링과 함께 Next.js 미들웨어 사용

요청을 가로채는 Next.js 미들웨어(`middleware.ts`)를 사용 중이라면 터널 라우트를 제외하세요.

`middleware.ts`

```typescript
export const config = {
  matcher: ["/((?!monitoring|_next/static|_next/image|favicon.ico).*)"],
};
```

`next.config.ts`

```typescript
export default withSentryConfig(nextConfig, {
  // Use a fixed route (recommended)
  tunnelRoute: "/monitoring",
});
```

## [Error Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#error-monitoring)

오류를 발생시켜 Sentry에서 확인하면서 오류 모니터링 설정을 테스트하세요.

- [Throw a Test Error](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#throw-a-test-error)

아무 페이지에나 이 버튼을 추가하고 클릭해 테스트 오류를 트리거하세요.

##### 중요

브라우저 개발자 도구(예: 브라우저 콘솔) 내부에서 트리거한 오류는 샌드박스 처리되므로 Sentry 오류 모니터링을 트리거하지 않습니다.

```jsx
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>;
```

- [Verify](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#verify)

Sentry에서 [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/)를 열어 테스트 오류를 확인하세요. [오류 수집에 대해 더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/usage.md).

## [Verify Additional Features](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#verify-additional-features)

위에서 선택한 기능을 기준으로, 각 기능이 정상 동작하는지 확인하세요.

- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#session-replay)

Session Replay는 사용자 세션을 영상처럼 재현해 수집합니다. 클라이언트 설정에서 `replayIntegration()`으로 구성합니다.

기본적으로 Sentry는 모든 텍스트, 입력값, 미디어를 마스킹합니다. 이는 [Privacy Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)에서 사용자 지정할 수 있습니다.

**확인:** 오류를 트리거하거나 앱을 탐색한 뒤, Sentry의 [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/)를 확인하세요.

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.replayIntegration({
      maskAllText: true,
      maskAllInputs: true,
      blockAllMedia: true,
    }),
  ],

  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

- [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#tracing)

Tracing은 SDK 초기화 파일의 `tracesSampleRate`로 구성됩니다. Next.js 라우트와 API 호출은 자동으로 계측됩니다.

코드 내 특정 작업을 추적하려면 [custom spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/custom-instrumentation.md)를 추가하세요.

**확인:** 아무 페이지로 이동한 뒤 Sentry의 [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/)를 확인하세요.

```typescript
import * as Sentry from "@sentry/nextjs";

// Wrap operations with spans
const result = await Sentry.startSpan(
  { name: "expensive-operation", op: "function" },
  async () => {
    return await fetchDataFromAPI();
  },
);
```

- [Logs NEW](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#logs-)

로그는 SDK 설정에서 `enableLogs: true`로 활성화됩니다. Sentry 로거를 사용해 애플리케이션 어디에서든 구조화된 로그를 전송하세요.

[Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations)을 통해 널리 쓰이는 로깅 라이브러리를 연결할 수 있습니다.

**확인:** 로그 구문을 추가하고 트리거한 뒤, Sentry의 [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/)를 확인하세요.

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.logger.info("User clicked checkout button");

Sentry.logger.info("Order completed", {
  orderId: "12345",
  total: 99.99,
});

Sentry.logger.warn("Warning message");
Sentry.logger.error("Error occurred");
```

- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#user-feedback)

User Feedback는 `feedbackIntegration()`을 통해 삽입 가능한 위젯을 추가하여 사용자가 앱에서 직접 버그를 보고할 수 있게 합니다.

**확인:** 피드백 버튼(오른쪽 하단)을 찾아 테스트 피드백을 제출한 뒤, Sentry의 [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/)를 확인하세요.

[User Feedback에 대해 더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md)

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
  ],
});
```

## 하이브리드 앱 (App Router + Pages Router)

애플리케이션이 App Router와 Pages Router를 모두 사용하는 경우:

1. App Router 컴포넌트에는 이 가이드를 따르세요.
2. Pages Router 오류 처리를 위해 `pages/_error.tsx` 파일을 추가하세요([Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md) 참고).
3. 두 라우터는 동일한 Sentry 설정 파일을 공유합니다.

Sentry SDK는 사용 중인 라우터를 자동으로 감지하고 적절한 계측을 적용합니다.

## 다음 단계

Next.js 애플리케이션에 Sentry를 성공적으로 통합했습니다. 다음 항목도 살펴보세요.

* [Logs Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Pino, Winston, Bunyan 같은 널리 쓰이는 로깅 라이브러리 연결
* [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - 서비스 및 마이크로서비스 전반의 요청 추적
* [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Vercel AI SDK, LangChain 등으로 구축한 AI 에이전트 모니터링
* [Connect GitHub + Seer](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - GitHub 저장소를 연결해 AI 기반 [root cause analysis](https://docs.sentry.io/product/ai-in-sentry/seer.md) 활성화
* [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - 확장 SDK 설정 옵션 살펴보기

SDK 설정에 문제가 있나요?

* 자동 설정을 위해 [installation wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)를 사용해 보세요.
* [지원 받기](https://sentry.zendesk.com/hc/en-us/)

## 이 섹션의 페이지

- [Pages Router Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/pages-router.md)
- [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md)

