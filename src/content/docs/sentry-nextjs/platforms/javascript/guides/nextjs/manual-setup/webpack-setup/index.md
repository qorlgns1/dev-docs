---
title: 'Webpack 설정 | Next.js용 Sentry'
description: '이 가이드는 Webpack을 사용하는 Next.js 애플리케이션(Next.js 15 이전의 기본 번들러)에 대한 설정 차이점을 다룹니다. 먼저 메인 수동 설정을 완료한 뒤, 이 Webpack 전용 설정을 적용하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup

# Webpack 설정 | Next.js용 Sentry

이 가이드는 **Webpack을 사용하는 Next.js 애플리케이션**(Next.js 15 이전의 기본 번들러)에 대한 설정 차이점을 다룹니다. 먼저 [메인 수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md)을 완료한 뒤, 이 Webpack 전용 설정을 적용하세요.

모든 빌드 설정 옵션의 전체 참고 자료는 [Build Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md) 문서를 확인하세요.

Next.js 15+에서 Turbopack(기본값)을 사용 중이라면 이 가이드는 필요하지 않습니다. 대신 [메인 수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md)을 참고하세요.

## [핵심 차이점: Webpack vs Turbopack](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#key-differences-webpack-vs-turbopack)

| 기능                            | Turbopack                         | Webpack                                              |
| ----------------------------- | --------------------------------- | ---------------------------------------------------- |
| 서버 함수 계측                    | Next.js telemetry를 통한 자동               | 빌드 시 코드 주입                                          |
| 미들웨어 계측                      | Next.js telemetry를 통한 자동               | 빌드 시 코드 주입                                          |
| 소스 맵 업로드                      | 빌드 중 컴파일 후 업로드                     | 플러그인을 통한 빌드 중 업로드(기본값)                              |
| 라우트 제외                        | 지원되지 않음                           | `webpack.excludeServerRoutes`를 통해 지원                |
| React 컴포넌트 주석                 | 지원되지 않음                           | `webpack.reactComponentAnnotation`을 통해 지원           |
| Logger 트리 셰이킹                 | 지원되지 않음                           | `webpack.treeshake.removeDebugLogging`을 통해 지원       |

## [자동 계측 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#auto-instrumentation-options)

Webpack에서는 Sentry가 빌드 시점에 서버 함수, 미들웨어, 그리고 app 디렉터리 컴포넌트를 자동으로 계측합니다. 이 동작은 다음과 같이 제어할 수 있습니다.

- [자동 계측 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-auto-instrumentation)

이 옵션들은 Webpack에서 기본으로 활성화됩니다. 수동 계측을 선호하거나 빌드 이슈가 있다면 비활성화하세요.

**참고**: 이 옵션들은 Pages Router 페이지, API 라우트, App Router 컴포넌트를 계측하지만, Server Actions는 자동으로 계측하지 않습니다. Server Actions는 `withServerActionInstrumentation()`을 사용해 수동으로 래핑해야 합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    // Instrument Pages Router API routes and data fetching methods (default: true)
    autoInstrumentServerFunctions: true,

    // Instrument Next.js middleware (default: true)
    autoInstrumentMiddleware: true,

    // Instrument App Router components (default: true)
    autoInstrumentAppDirectory: true,

    // Tree-shake Sentry logger statements to reduce bundle size
    treeshake: {
      removeDebugLogging: true,
    },
  },
});
```

## [계측에서 라우트 제외](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#exclude-routes-from-instrumentation)

Webpack에서는 특정 라우트를 자동 계측 대상에서 제외할 수 있습니다. 이는 헬스 체크 엔드포인트나 모니터링하면 안 되는 라우트에 유용합니다.

Turbopack을 사용할 때는 이 옵션이 효과가 없습니다. Turbopack은 빌드 시점 계측 대신 Next.js telemetry 기능에 의존하기 때문입니다.

- [라우트 제외 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-route-exclusions)

라우트는 파일 시스템 경로가 아니라 URL 경로로 지정하세요. 라우트는 앞에 슬래시가 있어야 하며, 뒤에 슬래시는 없어야 합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    excludeServerRoutes: [
      "/api/health",
      "/api/excluded/[parameter]",
      /^\/internal\//, // Regex for all /internal/* routes
    ],
  },
});
```

## [소스 맵 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#source-map-upload)

기본적으로 Webpack은 Sentry Webpack Plugin을 사용해 **빌드 과정 중에** 소스 맵을 업로드합니다. 이 작업은 각 빌드(client, server, edge)마다 별도로 수행되므로 빌드 시간이 늘어날 수 있습니다.

더 빠른 빌드를 위해 post-build 업로드 모드(Next.js 15.4.1+에서 사용 가능)를 사용할 수 있습니다. 이 모드는 모든 빌드가 완료된 후 모든 소스 맵을 한 번에 업로드합니다.

- [기본값: 빌드 중 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#default-upload-during-build)

Sentry Webpack Plugin은 각 webpack 컴파일 중에 실행되며, 생성되는 소스 맵을 즉시 업로드합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,
});
```

- [옵션: 빌드 후 업로드 (Next.js 15.4.1+)](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#option-upload-after-build-nextjs-1541)

더 빠른 빌드를 위해 post-build 업로드를 활성화하세요. 모든 webpack 빌드가 완료된 후 모든 소스 맵을 한 번만 업로드합니다.

이 옵션은 Next.js 15.4.1 이상이 필요합니다. Turbopack은 항상 이 모드를 사용합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Upload after all builds complete (faster)
  useRunAfterProductionCompileHook: true,
});
```

- [고급 Webpack Plugin 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#advanced-webpack-plugin-options)

고급 설정이 필요하면 기본 Sentry Webpack Plugin에 옵션을 직접 전달할 수 있습니다.

`unstable_sentryWebpackPluginOptions` API는 향후 릴리스에서 변경될 수 있습니다.

이 옵션들은 `useRunAfterProductionCompileHook`가 `false`(기본값)일 때만 적용됩니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,

  webpack: {
    // Advanced Webpack plugin options
    unstable_sentryWebpackPluginOptions: {
      sourcemaps: {
        assets: ["./build/**/*.js", "./build/**/*.map"],
        ignore: ["node_modules/**"],
      },
    },
  },
});
```

## [Webpack에서 Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#server-actions-with-webpack)

Server Actions(`"use server"`로 표시된 함수)는 Webpack의 빌드 시점 계측으로 **자동 계측되지 않습니다**. 오류 및 성능 모니터링을 위해 직접 래핑해야 합니다.

- [수동 Server Action 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#manual-server-action-instrumentation)

오류와 성능 데이터를 수집하려면 Server Actions를 `withServerActionInstrumentation()`으로 래핑하세요.

`app/actions.ts`

```typescript
"use server";
import * as Sentry from "@sentry/nextjs";

export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm", // Action name for Sentry
    {
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

## [React 컴포넌트 주석](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#react-component-annotation)

Webpack에서는 React 컴포넌트 이름 추적을 활성화할 수 있습니다. 이 기능은 React 컴포넌트에 `data-sentry-*` 속성을 주석으로 추가하여, 사용자가 [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md) 및 [breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)에서 어떤 컴포넌트와 상호작용했는지 Sentry가 식별할 수 있게 합니다.

이 기능은 Webpack에서만 사용할 수 있습니다. Turbopack은 React 컴포넌트 주석을 지원하지 않습니다.

- [컴포넌트 주석 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#enable-component-annotation)

애플리케이션에서 컴포넌트 이름 추적을 위해 `reactComponentAnnotation`을 활성화하세요. 특히 Session Replay에서 사용자 상호작용을 디버깅할 때 유용합니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    reactComponentAnnotation: {
      enabled: true,
    },
  },
});
```

- [특정 컴포넌트 제외](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#exclude-specific-components)

주석을 달고 싶지 않은 컴포넌트가 있다면(개인정보 또는 성능상의 이유), 이름으로 제외할 수 있습니다.

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  webpack: {
    reactComponentAnnotation: {
      enabled: true,
      ignoredComponents: ["SensitiveForm", "InternalDebugPanel"],
    },
  },
});
```

## [Webpack에서 터널링](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#tunneling-with-webpack)

터널링은 Webpack과 Turbopack 모두에서 동일하게 동작합니다. Sentry는 모니터링 데이터의 노이즈를 방지하기 위해 미들웨어 스팬에서 터널 요청을 자동으로 필터링합니다.

- [터널 라우트 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#configure-tunnel-route)

광고 차단기를 우회하려면 터널링을 활성화하세요. 필요 시 미들웨어에서 제외할 수 있도록 고정 라우트를 사용하세요.

랜덤 터널 라우트 사용

`tunnelRoute: true`를 사용하면 랜덤 라우트를 자동 생성할 수 있습니다. 하지만 라우트가 빌드마다 바뀌므로 랜덤 라우트는 미들웨어 matcher에서 제외할 수 없습니다. 모든 요청을 가로채는 미들웨어가 있다면 문제가 생길 수 있습니다.

```typescript
tunnelRoute: true, // Auto-generated random route
```

`next.config.ts`

```typescript
import { withSentryConfig } from "@sentry/nextjs";

export default withSentryConfig(nextConfig, {
  // Use a fixed route (recommended)
  tunnelRoute: "/monitoring",
});
```

## [Webpack에서 Turbopack으로 마이그레이션](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#migrating-from-webpack-to-turbopack)

Turbopack으로 업그레이드하는 경우:

1. **webpack 전용 옵션 제거** - `excludeServerRoutes`와 `unstable_sentryWebpackPluginOptions`는 Turbopack에서 효과가 없습니다.
2. **소스 맵 변경사항 이해** - Turbopack은 항상 빌드 후 업로드를 사용합니다(플러그인 기반 업로드 옵션 없음).
3. **자동 계측 테스트** - Turbopack은 빌드 시점 주입 대신 Next.js telemetry를 사용하므로, 모니터링이 계속 동작하는지 확인하세요.

`next.config.ts`

```typescript
// Before (Webpack)
export default withSentryConfig(nextConfig, {
  excludeServerRoutes: ["/api/health"],
  tunnelRoute: "/monitoring",
});

// After (Turbopack)
export default withSentryConfig(nextConfig, {
  // excludeServerRoutes is not supported with Turbopack
  tunnelRoute: "/monitoring",
});
```

## [다음 단계](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#next-steps)

* [Logs Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) - Pino, Winston, Bunyan 같은 인기 로깅 라이브러리 연결
* [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md) - 서비스 및 마이크로서비스 전반에서 요청 추적
* [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) - Vercel AI SDK, LangChain 등으로 구축한 AI 에이전트 모니터링
* [Connect GitHub + Seer](https://docs.sentry.io/organization/integrations/source-code-mgmt/github.md#installing-github) - AI 기반 [근본 원인 분석](https://docs.sentry.io/product/ai-in-sentry/seer.md) 활성화
* [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration.md) - 확장된 SDK 설정 옵션 살펴보기

