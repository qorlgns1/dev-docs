---
title: 'Rollup | Next.js용 Sentry'
description: '이 가이드는 Sentry SDK 버전  이상을 사용하고 있다고 가정합니다. 이전 버전을 사용 중이고 소스 맵을 업로드하려면 SDK를 최신 버전으로 업그레이드하는 것을 권장합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/rollup

# Rollup | Next.js용 Sentry

이 가이드는 **Sentry SDK 버전 `7.47.0` 이상**을 사용하고 있다고 가정합니다. 이전 버전을 사용 중이고 소스 맵을 업로드하려면 SDK를 최신 버전으로 업그레이드하는 것을 권장합니다.

앱을 번들링할 때 Sentry Rollup 플러그인을 사용해 릴리스를 자동으로 생성하고 소스 맵을 Sentry에 업로드할 수 있습니다.

## [자동 설정](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#automatic-setup)

rollup에서 소스 맵 업로드를 설정하는 가장 쉬운 방법은 Sentry Wizard를 사용하는 것입니다:

```bash
npx @sentry/wizard@latest -i sourcemaps
```

Wizard는 다음 단계를 안내합니다:

* Sentry에 로그인하고 프로젝트 선택
* 필요한 Sentry 패키지 설치
* 소스 맵 생성 및 업로드를 위한 빌드 도구 설정
* 소스 맵 업로드를 위한 CI 설정

CLI로 소스 맵 업로드를 수동 설정하려면 아래 단계를 따르세요.

## [수동 설정](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#manual-setup)

Sentry Rollup 플러그인을 설치합니다:

```bash
npm install @sentry/rollup-plugin --save-dev
```

- [구성](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#configuration)

소스 맵을 업로드하려면 [Organization Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/)을 설정해야 합니다.

또는 "Project: Read & Write" 및 "Release: Admin" 권한이 있는 [Personal Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/account/api/auth-tokens/)을 사용할 수도 있습니다.

인증 토큰은 플러그인의 `authToken` 옵션으로 직접 전달하거나, `SENTRY_AUTH_TOKEN` 환경 변수로 전달하거나, 프로젝트 빌드 시 작업 디렉터리에 있는 `.env.sentry-build-plugin` 파일로 전달할 수 있습니다(민감한 데이터이므로 `.gitignore` 파일에 추가하는 것을 잊지 마세요). 인증 토큰은 CI/CD 환경 변수로 추가하는 것을 권장합니다.

플러그인 구성에 대한 자세한 내용은 [Sentry Rollup Plugin documentation](https://www.npmjs.com/package/@sentry/rollup-plugin)을 참고하세요.

`.env.sentry-build-plugin`

```bash
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

예시:

`rollup.config.js`

```javascript
import { sentryRollupPlugin } from "@sentry/rollup-plugin";

export default {
  output: {
    sourcemap: "hidden", // Source map generation must be turned on ("hidden", true, etc.)
  },
  plugins: [
    // Put the Sentry rollup plugin after all other plugins
    sentryRollupPlugin({
      org: "___ORG_SLUG___",
      project: "___PROJECT_SLUG___",
      authToken: process.env.SENTRY_AUTH_TOKEN,
      sourcemaps: {
        // As you're enabling client source maps, you probably want to delete them after they're uploaded to Sentry.
        // Set the appropriate glob pattern for your output folder - some glob examples below:
        filesToDeleteAfterUpload: [
          "./**/*.map",
          ".*/**/public/**/*.map",
          "./dist/**/client/**/*.map",
        ],
      },
    }),
  ],
};
```

소스 맵을 생성하면 **공개적으로 노출될 수 있어**, 잠재적으로 소스 코드가 유출될 수 있습니다. 이를 방지하려면 서버에서 `.js.map` 파일 접근을 차단하도록 설정하거나, Sentry에 업로드한 뒤 소스 맵을 삭제하는 [Sentry Rollup Plugin의 `sourcemaps.filesToDeleteAfterUpload`](https://www.npmjs.com/package/@sentry/rollup-plugin#sourcemapsfilestodeleteafterupload) 옵션을 사용하세요.

