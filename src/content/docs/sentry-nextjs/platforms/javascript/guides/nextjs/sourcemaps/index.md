---
title: '소스 맵 | Next.js용 Sentry'
description: '소스 맵은 최소화된 프로덕션 코드를 원본 소스로 다시 매핑해, 이해하기 어려운 줄 번호 대신 읽기 쉬운 스택 트레이스를 제공합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps

# 소스 맵 | Next.js용 Sentry

소스 맵은 최소화된 프로덕션 코드를 원본 소스로 다시 매핑해, 이해하기 어려운 줄 번호 대신 읽기 쉬운 스택 트레이스를 제공합니다.

**SDK가 이 과정을 자동으로 처리합니다.** `next build`를 실행하면 소스 맵이 생성되어 Sentry로 업로드됩니다. [Sentry Wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs.md#step-1-install)를 사용했다면 추가 설정이 필요하지 않습니다.

소스 맵은 **프로덕션 빌드**(`next build`)에서만 업로드됩니다. 개발 빌드(`next dev`)에서는 업로드가 생성되지 않습니다.

**Vercel로 배포하시나요?** 배포 중 자동 업로드를 위해 [Vercel integration](https://docs.sentry.io/organization/integrations/deployment/vercel.md)도 사용할 수 있습니다.

소스 맵이 오류 리포트를 어떻게 바꿔주는지 확인해 보세요:

- [수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#manual-configuration)

SDK를 수동으로 설치했거나 wizard가 완료되지 않았다면, 소스 맵 업로드를 설정하세요:

#
- [인증 토큰 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#add-auth-token)

Sentry 인증 토큰을 환경에 추가하세요. CI에도 반드시 추가해야 합니다.

`.env.local`

```bash
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

#
- [Next.js 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#configure-nextjs)

org, project, auth token과 함께 Next.js 설정에 `withSentryConfig`를 추가하세요.

**Turbopack**(Next.js 15+ 기본값)에서는 빌드가 완료된 후 소스 맵이 업로드됩니다.

`@sentry/nextjs@10.13.0+` 및 `next@15.4.1+`가 필요합니다.

`next.config.ts`

```typescript
import type { NextConfig } from "next";
import { withSentryConfig } from "@sentry/nextjs";

const nextConfig: NextConfig = {
  // your existing Next.js config
};

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",
  authToken: process.env.SENTRY_AUTH_TOKEN,
});
```

- [일반 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#common-options)

| 옵션                                   | 기본값 | 설명                                                                                               |
| ---------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| `sourcemaps.deleteSourcemapsAfterUpload` | `true`  | 업로드 후 **클라이언트 측** 소스 맵을 삭제합니다. 서버 소스 맵은 런타임 오류 리포팅을 위해 유지됩니다. |
| `widenClientFileUpload`                  | `false` | `[native code]` 프레임을 해결하기 위해 의존성 소스 맵을 업로드합니다.                                               |

사용 가능한 모든 옵션은 [Build Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#source-maps-options)를 참고하세요.

- [Webpack 사용 중인가요?](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#using-webpack)

Turbopack 대신 Webpack을 사용하는 경우, 소스 맵은 빌드 **중에** 업로드됩니다(빌드 후가 아님). 설정은 동일하지만 추가 옵션을 사용할 수 있습니다:

* **빌드 후 업로드 모드:** `useRunAfterProductionCompileHook: true`를 설정하면 빌드 후 업로드됩니다(Next.js 15.4.1+ 필요).
* **고급 플러그인 옵션:** `webpack.unstable_sentryWebpackPluginOptions`를 사용해 Sentry Webpack Plugin에 옵션을 전달합니다.

완전한 Webpack 설정은 [Webpack Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/webpack-setup.md#source-map-upload)을 참고하세요.

- [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#troubleshooting)

스택 트레이스에 최소화된 코드가 보인다면, CI 환경에 `SENTRY_AUTH_TOKEN`이 설정되어 있는지 확인하세요.

자세한 디버깅 단계는 [Troubleshooting Source Maps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md)를 참고하세요.

## [추가 리소스](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md#additional-resources)

* [sentry-cli를 사용해 소스 맵 업로드하기](https://docs.sentry.io/cli/releases.md#sentry-cli-sourcemaps)
* [소스 맵이 깨지는 4가지 이유](https://blog.sentry.io/2018/10/18/4-reasons-why-your-source-maps-are-broken)

## 이 섹션의 페이지

- [소스 맵 문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md)

