---
title: 'Vite | Next.js용 Sentry'
description: '이 가이드는 Sentry SDK 버전  이상을 사용한다고 가정합니다. 이전 버전을 사용 중이고 source map을 업로드하려면, SDK를 최신 버전으로 업그레이드하는 것을 권장합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/vite

# Vite | Next.js용 Sentry

이 가이드는 Sentry **SDK 버전 `7.47.0` 이상**을 사용한다고 가정합니다. 이전 버전을 사용 중이고 source map을 업로드하려면, SDK를 최신 버전으로 업그레이드하는 것을 권장합니다.

앱을 번들링할 때 Sentry Vite 플러그인을 사용해 릴리스를 자동으로 생성하고 source map을 Sentry에 업로드할 수 있습니다.

## [자동 설정](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/vite.md#automatic-setup)

Vite에서 source map 업로드를 구성하는 가장 쉬운 방법은 Sentry Wizard를 사용하는 것입니다.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

Wizard는 다음 단계를 안내합니다.

* Sentry에 로그인하고 프로젝트 선택
* 필요한 Sentry 패키지 설치
* source map 생성 및 업로드를 위해 빌드 도구 구성
* source map 업로드를 위해 CI 구성

Vite에서 source map 업로드를 수동으로 구성하려면 아래 단계를 따르세요.

## [수동 설정](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/vite.md#manual-setup)

Sentry Vite 플러그인을 설치하세요.

```bash
npm install @sentry/vite-plugin --save-dev
```

- [구성](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/vite.md#configuration)

source map을 업로드하려면 [Organization Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/)을 구성해야 합니다.

또는 "Project: Read & Write" 및 "Release: Admin" 권한이 있는 [Personal Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/account/api/auth-tokens/)을 사용할 수도 있습니다.

인증 토큰은 플러그인 `authToken` 옵션으로 직접 전달하거나, `SENTRY_AUTH_TOKEN` 환경 변수로 전달하거나, 프로젝트 빌드 시 작업 디렉터리에 `.env.sentry-build-plugin` 파일로 전달할 수 있습니다(민감한 데이터이므로 `.gitignore` 파일에 반드시 추가하세요). 인증 토큰은 CI/CD 환경에 환경 변수로 추가하는 것을 권장합니다.

플러그인 구성에 대한 자세한 내용은 [Sentry Vite Plugin 문서](https://www.npmjs.com/package/@sentry/vite-plugin)를 참고하세요.

`.env.sentry-build-plugin`

```bash
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

##### 플러그인 순서가 중요합니다

`plugins` 배열에서 Sentry Vite 플러그인을 **다른 모든 플러그인 뒤에** 배치하세요. 이렇게 해야 source map이 올바르게 생성되고 tree-shaking이 Sentry 계측 코드를 제거하지 않습니다.

예시:

`vite.config.js`

```javascript
import { defineConfig } from "vite";
import { sentryVitePlugin } from "@sentry/vite-plugin";

export default defineConfig({
  build: {
    sourcemap: "hidden", // Source map generation must be turned on ("hidden", true, etc.)
  },
  plugins: [
    // Put the Sentry Vite plugin after all other plugins
    sentryVitePlugin({
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
});
```

source map 생성은 **공개로 노출될 수 있으며**, 잠재적으로 소스 코드 유출로 이어질 수 있습니다. 이를 방지하려면 서버에서 `.js.map` 파일 접근을 차단하도록 구성하거나, [Sentry Vite Plugin의 `sourcemaps.filesToDeleteAfterUpload` 옵션](https://www.npmjs.com/package/@sentry/vite-plugin#sourcemapsfilestodeleteafterupload)을 사용해 Sentry 업로드 후 source map을 삭제할 수 있습니다.

Sentry Vite 플러그인은 watch-mode/development-mode에서는 source map을 업로드하지 않습니다. 구성이 올바른지 확인하려면 프로덕션 빌드를 실행해 테스트하는 것을 권장합니다.

