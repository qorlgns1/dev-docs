---
title: '가이드: 환경 변수'
description: 'Next.js는 환경 변수를 위한 기본 제공 지원을 제공하며, 다음 작업을 수행할 수 있습니다.'
---

# 가이드: 환경 변수 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/environment-variables

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)환경 변수

Copy page

# Next.js에서 환경 변수를 사용하는 방법

마지막 업데이트 2026년 2월 20일

Next.js는 환경 변수를 위한 기본 제공 지원을 제공하며, 다음 작업을 수행할 수 있습니다.

  * [`.env`로 환경 변수 로드](https://nextjs.org/docs/pages/guides/environment-variables#loading-environment-variables)
  * [`NEXT_PUBLIC_` 접두사를 사용해 브라우저용으로 환경 변수 번들링](https://nextjs.org/docs/pages/guides/environment-variables#bundling-environment-variables-for-the-browser)

> **Warning:** 기본 `create-next-app` 템플릿은 모든 `.env` 파일이 `.gitignore`에 추가되도록 합니다. 이러한 파일을 저장소에 커밋해야 하는 경우는 거의 없습니다.

## 환경 변수 로드[](https://nextjs.org/docs/pages/guides/environment-variables#loading-environment-variables)

Next.js는 `.env*` 파일의 환경 변수를 `process.env`로 불러오는 기능을 기본으로 제공합니다.

.env
[code]
    DB_HOST=localhost
    DB_USER=myuser
    DB_PASS=mypassword
[/code]

이렇게 하면 `process.env.DB_HOST`, `process.env.DB_USER`, `process.env.DB_PASS`가 Node.js 환경에 자동으로 로드되어 [Next.js 데이터 패칭 메서드](https://nextjs.org/docs/pages/building-your-application/data-fetching)와 [API 라우트](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)에서 사용할 수 있습니다.

예를 들어 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 사용할 때는 다음과 같습니다.

pages/index.js
[code]
    export async function getStaticProps() {
      const db = await myDB.connect({
        host: process.env.DB_HOST,
        username: process.env.DB_USER,
        password: process.env.DB_PASS,
      })
      // ...
    }
[/code]

### `@next/env`로 환경 변수 로드[](https://nextjs.org/docs/pages/guides/environment-variables#loading-environment-variables-with-nextenv)

ORM이나 테스트 러너용 루트 구성 파일처럼 Next.js 런타임 외부에서 환경 변수를 로드해야 하는 경우 `@next/env` 패키지를 사용할 수 있습니다.

이 패키지는 Next.js 내부에서 `.env*` 파일의 환경 변수를 로드하는 데 사용됩니다.

사용하려면 패키지를 설치한 뒤 `loadEnvConfig` 함수를 호출해 환경 변수를 로드합니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add @next/env
[/code]

envConfig.ts

JavaScriptTypeScript
[code]
    import { loadEnvConfig } from '@next/env'

    const projectDir = process.cwd()
    loadEnvConfig(projectDir)
[/code]

그런 다음 필요한 위치에서 구성을 임포트하면 됩니다. 예:

orm.config.ts

JavaScriptTypeScript
[code]
    import './envConfig.ts'

    export default defineConfig({
      dbCredentials: {
        connectionString: process.env.DATABASE_URL!,
      },
    })
[/code]

### 다른 변수를 참조하기[](https://nextjs.org/docs/pages/guides/environment-variables#referencing-other-variables)

Next.js는 `.env*` 파일 안에서 `$VARIABLE`처럼 `$`를 사용해 다른 변수를 참조하는 값을 자동으로 확장합니다. 즉, 다른 시크릿을 참조할 수 있습니다. 예:

.env
[code]
    TWITTER_USER=nextjs
    TWITTER_URL=https://x.com/$TWITTER_USER
[/code]

위 예시에서 `process.env.TWITTER_URL`은 `https://x.com/nextjs`로 설정됩니다.

> **Good to know** : 실제 값에 `$`가 포함되어야 한다면 `\$`처럼 이스케이프해야 합니다.

## 브라우저용 환경 변수 번들링[](https://nextjs.org/docs/pages/guides/environment-variables#bundling-environment-variables-for-the-browser)

`NEXT_PUBLIC_`이 없는 환경 변수는 Node.js 환경에서만 사용할 수 있으며, 브라우저에서는 접근할 수 없습니다(클라이언트는 다른 _environment_에서 실행되므로).

브라우저에서 환경 변수 값을 사용할 수 있도록 하려면 Next.js가 빌드 시점에 클라이언트로 전달되는 JS 번들에 값을 “인라인”하도록 할 수 있습니다. 즉, `process.env.[variable]`에 대한 모든 참조를 하드코딩된 값으로 대체합니다. 이를 지시하려면 변수에 `NEXT_PUBLIC_` 접두사를 붙이면 됩니다. 예:

.env
[code]
    NEXT_PUBLIC_ANALYTICS_ID=abcdefghijk
[/code]

이렇게 하면 Next.js는 Node.js 환경에서 `process.env.NEXT_PUBLIC_ANALYTICS_ID`에 대한 모든 참조를 `next build`를 실행한 환경의 값으로 대체하므로 코드 어디서든 사용할 수 있습니다. 브라우저로 전송되는 모든 JavaScript에도 인라인됩니다.

> **Note** : 빌드가 끝난 뒤에는 이러한 환경 변수를 변경해도 앱이 반응하지 않습니다. 예를 들어 하나의 환경에서 빌드한 슬러그를 다른 환경으로 승격하는 Heroku 파이프라인을 사용하거나 단일 Docker 이미지를 여러 환경에 배포하는 경우, 모든 `NEXT_PUBLIC_` 변수는 빌드 시점의 값으로 고정됩니다. 따라서 프로젝트를 빌드할 때 이 값들을 적절히 설정해야 합니다. 런타임 환경 값을 사용하려면 클라이언트가 필요 시(온디맨드) 또는 초기화 중에 해당 값을 제공하는 자체 API를 설정해야 합니다.

pages/index.js
[code]
    import setupAnalyticsService from '../lib/my-analytics-service'

    // 'NEXT_PUBLIC_ANALYTICS_ID' can be used here as it's prefixed by 'NEXT_PUBLIC_'.
    // It will be transformed at build time to `setupAnalyticsService('abcdefghijk')`.
    setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID)

    function HomePage() {
      return <h1>Hello World</h1>
    }

    export default HomePage
[/code]

다음과 같은 동적 조회는 인라인되지 않습니다.
[code]
    // This will NOT be inlined, because it uses a variable
    const varName = 'NEXT_PUBLIC_ANALYTICS_ID'
    setupAnalyticsService(process.env[varName])

    // This will NOT be inlined, because it uses a variable
    const env = process.env
    setupAnalyticsService(env.NEXT_PUBLIC_ANALYTICS_ID)
[/code]

### 런타임 환경 변수[](https://nextjs.org/docs/pages/guides/environment-variables#runtime-environment-variables)

Next.js는 빌드 타임과 런타임 환경 변수를 모두 지원합니다.

**기본적으로 환경 변수는 서버에서만 사용할 수 있습니다.** 브라우저에 노출하려면 `NEXT_PUBLIC_` 접두사를 붙여야 합니다. 하지만 이러한 공개 환경 변수는 `next build` 중 JavaScript 번들에 인라인됩니다.

런타임 환경 변수를 읽으려면 `getServerSideProps`를 사용하거나 [App Router를 점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 것이 좋습니다.

이렇게 하면 서로 다른 값을 가진 여러 환경에서 단일 Docker 이미지를 승격할 수 있습니다.

**Good to know:**

  * [`register` 함수](https://nextjs.org/docs/app/guides/instrumentation)를 사용해 서버 시작 시 코드를 실행할 수 있습니다.

## 테스트 환경 변수[](https://nextjs.org/docs/pages/guides/environment-variables#test-environment-variables)

`development`, `production` 외에 `test`라는 세 번째 옵션이 있습니다. 개발 또는 프로덕션 환경에서 기본값을 지정할 수 있는 것과 동일하게 `testing` 환경용 `.env.test` 파일을 사용할 수 있습니다(다만 앞선 두 환경만큼 흔하지는 않습니다). Next.js는 `testing` 환경에서 `.env.development` 또는 `.env.production`의 환경 변수를 로드하지 않습니다.

`jest`, `cypress` 같은 도구로 테스트를 실행할 때 테스트에만 필요한 환경 변수를 설정해야 하는 경우 유용합니다. `NODE_ENV`가 `test`로 설정되어 있으면 테스트 기본값이 로드되며, 일반적으로 테스트 도구가 자동으로 처리하므로 수동으로 설정할 필요가 없습니다.

`test` 환경과 `development`, `production` 사이에는 알아두어야 할 작은 차이가 있습니다. `.env.local`은 로드되지 않습니다. 테스트는 모든 사람이 동일한 결과를 얻어야 하므로 `.env.local`(기본값을 덮어쓰도록 의도된 파일)을 무시하여 실행마다 동일한 환경 기본값을 사용하도록 합니다.

> **Good to know** : 기본 환경 변수와 마찬가지로 `.env.test` 파일은 저장소에 포함해야 하지만 `.env.test.local`은 포함하지 말아야 합니다. `.env*.local`은 `.gitignore`로 무시하도록 설계되었기 때문입니다.

유닛 테스트를 실행하는 동안에도 `@next/env` 패키지의 `loadEnvConfig` 함수를 활용하여 Next.js와 동일한 방식으로 환경 변수를 로드할 수 있습니다.
[code]
    // The below can be used in a Jest global setup file or similar for your testing set-up
    import { loadEnvConfig } from '@next/env'

    export default async () => {
      const projectDir = process.cwd()
      loadEnvConfig(projectDir)
    }
[/code]

## 환경 변수 로드 순서[](https://nextjs.org/docs/pages/guides/environment-variables#environment-variable-load-order)

환경 변수는 아래 순서대로 검색되며, 값을 찾으면 중단합니다.

  1. `process.env`
  2. `.env.$(NODE_ENV).local`
  3. `.env.local` (`NODE_ENV`가 `test`일 때는 확인하지 않음.)
  4. `.env.$(NODE_ENV)`
  5. `.env`

예를 들어 `NODE_ENV`가 `development`이고 `.env.development.local`과 `.env` 모두에 변수를 정의했다면 `.env.development.local` 값을 사용합니다.

> **Good to know** : `NODE_ENV`에 허용되는 값은 `production`, `development`, `test`입니다.

## 알아두면 좋은 사항[](https://nextjs.org/docs/pages/guides/environment-variables#good-to-know)

  * [`/src` 디렉터리](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)를 사용한다면 `.env.*` 파일은 프로젝트 루트에 그대로 보관해야 합니다.
  * 환경 변수 `NODE_ENV`가 지정되지 않은 경우, Next.js는 `next dev` 명령 실행 시 자동으로 `development`를, 그 외 모든 명령에는 `production`을 설정합니다.

## 버전 기록[](https://nextjs.org/docs/pages/guides/environment-variables#version-history)

Version| Changes
---|---
`v9.4.0`| `.env`와 `NEXT_PUBLIC_` 지원이 도입됨.

Was this helpful?

supported.

Send
