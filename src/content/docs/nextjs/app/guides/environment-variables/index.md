---
title: '가이드: 환경 변수'
description: '최종 업데이트: 2026년 2월 20일'
---

# 가이드: 환경 변수 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/environment-variables

[App Router](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)환경 변수

페이지 복사

# Next.js에서 환경 변수를 사용하는 방법

최종 업데이트: 2026년 2월 20일

Next.js에는 환경 변수를 위한 기본 지원이 포함되어 있어 다음을 수행할 수 있습니다.

  * [`.env`를 사용해 환경 변수 로드](https://nextjs.org/docs/app/guides/environment-variables#loading-environment-variables)
  * [`NEXT_PUBLIC_` 접두사를 붙여 브라우저용으로 환경 변수 번들링](https://nextjs.org/docs/app/guides/environment-variables#bundling-environment-variables-for-the-browser)



> **경고:** 기본 `create-next-app` 템플릿은 모든 `.env` 파일이 `.gitignore`에 포함되도록 보장합니다. 이러한 파일을 저장소에 커밋하는 일은 거의 없어야 합니다.

## 환경 변수 로드[](https://nextjs.org/docs/app/guides/environment-variables#loading-environment-variables)

Next.js는 `.env*` 파일의 환경 변수를 `process.env`로 불러오는 기능을 기본적으로 제공합니다.

.env
[code]
    DB_HOST=localhost
    DB_USER=myuser
    DB_PASS=mypassword
[/code]

> **참고**: Next.js는 `.env*` 파일 안에서 여러 줄로 된 변수를 지원합니다.
[code] 
>     # .env
>      
>     # 줄바꿈을 포함해 작성할 수 있습니다
>     PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
>     ...
>     Kh9NV...
>     ...
>     -----END DSA PRIVATE KEY-----"
>      
>     # 또는 큰따옴표 안에 `\n`을 사용할 수 있습니다
>     PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\nKh9NV...\n-----END DSA PRIVATE KEY-----\n"
[/code]

> **참고**: `/src` 폴더를 사용하는 경우, Next.js는 `/src` 폴더가 아니라 부모 폴더의 .env 파일만 로드한다는 점에 유의하세요. 이렇게 하면 `process.env.DB_HOST`, `process.env.DB_USER`, `process.env.DB_PASS`가 Node.js 환경에 자동으로 로드되어 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 바로 사용할 수 있습니다.

예시는 다음과 같습니다.

app/api/route.js
[code]
    export async function GET() {
      const db = await myDB.connect({
        host: process.env.DB_HOST,
        username: process.env.DB_USER,
        password: process.env.DB_PASS,
      })
      // ...
    }
[/code]

### `@next/env`로 환경 변수 로드하기[](https://nextjs.org/docs/app/guides/environment-variables#loading-environment-variables-with-nextenv)

ORM이나 테스트 러너의 루트 설정 파일처럼 Next.js 런타임 바깥에서 환경 변수를 로드해야 한다면 `@next/env` 패키지를 사용할 수 있습니다.

이 패키지는 Next.js 내부에서 `.env*` 파일의 환경 변수를 로드하는 데 사용됩니다.

사용하려면 패키지를 설치한 뒤 `loadEnvConfig` 함수를 호출해 환경 변수를 불러오면 됩니다.

pnpmnpmyarnbun

터미널
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

그런 다음 필요한 곳에서 이 구성을 import하면 됩니다. 예를 들어:

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

### 다른 변수를 참조하기[](https://nextjs.org/docs/app/guides/environment-variables#referencing-other-variables)

Next.js는 `.env*` 파일에서 `$VARIABLE`처럼 `$`로 다른 변수를 참조하는 값을 자동으로 확장합니다. 이를 통해 다른 시크릿을 참조할 수 있습니다. 예를 들어:

.env
[code]
    TWITTER_USER=nextjs
    TWITTER_URL=https://x.com/$TWITTER_USER
[/code]

위 예시에서 `process.env.TWITTER_URL`은 `https://x.com/nextjs`로 설정됩니다.

> **알아두면 좋아요**: 실제 값에 `$`를 포함해야 한다면 `\$`처럼 이스케이프해야 합니다.

## 브라우저용 환경 변수 번들링[](https://nextjs.org/docs/app/guides/environment-variables#bundling-environment-variables-for-the-browser)

`NEXT_PUBLIC_`이 아닌 환경 변수는 Node.js 환경에서만 사용 가능하므로 브라우저에서는 접근할 수 없습니다(클라이언트는 별도의 _환경_에서 실행됨).

환경 변수 값을 브라우저에서 사용할 수 있도록 하려면, Next.js가 빌드 시점에 값을 클라이언트로 전달되는 js 번들에 "인라인"해 `process.env.[variable]` 참조를 상수 값으로 대체할 수 있습니다. 이를 지정하려면 변수에 `NEXT_PUBLIC_` 접두사만 붙이면 됩니다. 예를 들면:

.env
[code]
    NEXT_PUBLIC_ANALYTICS_ID=abcdefghijk
[/code]

이렇게 하면 Next.js는 Node.js 환경에서 `process.env.NEXT_PUBLIC_ANALYTICS_ID`에 대한 모든 참조를 `next build`를 실행하는 환경의 값으로 교체하므로 코드 어디에서든 사용할 수 있습니다. 해당 값은 브라우저로 전송되는 모든 JavaScript에 인라인됩니다.

> **참고**: 빌드가 완료된 후에는 이러한 환경 변수 변경에 앱이 반응하지 않습니다. 예를 들어, 하나의 환경에서 빌드한 슬러그를 다른 환경으로 승격하는 Heroku 파이프라인을 사용하거나 단일 Docker 이미지를 여러 환경에 배포하는 경우, 모든 `NEXT_PUBLIC_` 변수는 빌드 시점의 값으로 고정됩니다. 따라서 프로젝트를 빌드할 때 이 값들이 올바르게 설정되어야 합니다. 런타임 환경 값을 사용해야 한다면, 클라이언트가 요청 시 또는 초기화 중에 값을 받을 수 있도록 자체 API를 설정해야 합니다.

pages/index.js
[code]
    import setupAnalyticsService from '../lib/my-analytics-service'
     
    // 'NEXT_PUBLIC_ANALYTICS_ID'는 'NEXT_PUBLIC_' 접두사가 붙었으므로 여기서 사용할 수 있습니다.
    // 빌드 시 `setupAnalyticsService('abcdefghijk')`로 변환됩니다.
    setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID)
     
    function HomePage() {
      return <h1>Hello World</h1>
    }
     
    export default HomePage
[/code]

다음과 같은 동적 조회는 인라인되지 않습니다.
[code] 
    // 변수명을 사용하므로 인라인되지 않습니다.
    const varName = 'NEXT_PUBLIC_ANALYTICS_ID'
    setupAnalyticsService(process.env[varName])
     
    // 객체를 사용하므로 인라인되지 않습니다.
    const env = process.env
    setupAnalyticsService(env.NEXT_PUBLIC_ANALYTICS_ID)
[/code]

### 런타임 환경 변수[](https://nextjs.org/docs/app/guides/environment-variables#runtime-environment-variables)

Next.js는 빌드 타임과 런타임 환경 변수를 모두 지원합니다.

**기본적으로 환경 변수는 서버에서만 사용할 수 있습니다.** 브라우저에서 환경 변수를 노출하려면 반드시 `NEXT_PUBLIC_` 접두사를 붙여야 합니다. 다만 이러한 공개 환경 변수는 `next build` 중에 JavaScript 번들에 인라인됩니다.

동적 렌더링 중에는 서버에서 환경 변수를 안전하게 읽을 수 있습니다.

app/page.ts

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
     
    export default async function Component() {
      await connection()
      // cookies, headers 등 기타 Dynamic API도
      // 동적 렌더링에 참여하므로
      // 이 env 변수는 런타임에 평가됩니다
      const value = process.env.MY_VALUE
      // ...
    }
[/code]

이를 통해 단일 Docker 이미지를 사용하더라도 서로 다른 값의 여러 환경으로 승격할 수 있습니다.

**알아두면 좋아요:**

  * [`register` 함수](https://nextjs.org/docs/app/guides/instrumentation)를 사용해 서버 시작 시 코드를 실행할 수 있습니다.



## 테스트 환경 변수[](https://nextjs.org/docs/app/guides/environment-variables#test-environment-variables)

`development`와 `production` 외에도 `test`라는 세 번째 옵션이 있습니다. 개발 또는 프로덕션 환경의 기본값을 설정하듯이, `testing` 환경을 위해 `.env.test` 파일에 기본값을 설정할 수 있습니다(앞선 둘만큼 일반적이진 않음). `testing` 환경에서는 `.env.development`나 `.env.production`에서 환경 변수를 로드하지 않습니다.

이는 `jest`나 `cypress`처럼 테스트 전용 환경 변수가 필요한 도구로 테스트를 실행할 때 유용합니다. `NODE_ENV`를 `test`로 설정하면 테스트 기본값이 로드되지만, 대부분의 경우 테스트 도구가 자동으로 처리하므로 수동으로 설정할 필요는 없습니다.

`test` 환경과 `development`, `production` 사이에는 기억해야 할 작은 차이가 있습니다. `.env.local`은 로드되지 않는데, 이는 테스트가 모두에게 동일한 결과를 내야 하기 때문입니다. 이렇게 하면 `.env.local`(기본값을 덮어쓰도록 설계됨)을 무시하여 각 테스트 실행이 항상 동일한 환경 기본값을 사용합니다.

> **알아두면 좋아요**: 기본 환경 변수와 마찬가지로 `.env.test` 파일은 저장소에 포함되어야 하지만, `.env*.local`이 `.gitignore`로 무시되도록 되어 있으므로 `.env.test.local`은 포함하지 않아야 합니다.

단위 테스트를 실행할 때는 `@next/env` 패키지의 `loadEnvConfig` 함수를 활용해 Next.js와 동일한 방식으로 환경 변수를 로드할 수 있습니다.
[code] 
    // 아래 코드는 Jest 전역 설정 파일 등에서 테스트 설정용으로 사용할 수 있습니다.
    import { loadEnvConfig } from '@next/env'
     
    export default async () => {
      const projectDir = process.cwd()
      loadEnvConfig(projectDir)
    }
[/code]

## 환경 변수 로드 순서[](https://nextjs.org/docs/app/guides/environment-variables#environment-variable-load-order)

환경 변수는 다음 순서로 검색되며, 변수가 발견되면 탐색을 중단합니다.

  1. `process.env`
  2. `.env.$(NODE_ENV).local`
  3. `.env.local` (`NODE_ENV`가 `test`일 때는 확인하지 않음)
  4. `.env.$(NODE_ENV)`
  5. `.env`



예를 들어 `NODE_ENV`가 `development`이고 `.env.development.local`과 `.env` 둘 다에 변수를 정의하면 `.env.development.local`의 값이 사용됩니다.

> **알아두면 좋아요**: `NODE_ENV`의 허용 값은 `production`, `development`, `test`입니다.

## 알아두면 좋은 사항[](https://nextjs.org/docs/app/guides/environment-variables#good-to-know)

  * [`/src` 디렉터리](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)를 사용하는 경우 `.env.*` 파일은 프로젝트 루트에 두어야 합니다.
  * 환경 변수 `NODE_ENV`가 지정되지 않은 경우 Next.js는 `next dev` 명령에는 자동으로 `development`를, 다른 모든 명령에는 `production`을 할당합니다.



## 버전 기록[](https://nextjs.org/docs/app/guides/environment-variables#version-history)

Version| Changes  
---|---  
`v9.4.0`| `.env` 및 `NEXT_PUBLIC_` 지원을 도입했습니다.  
  
도움이 되었나요?

지원됨.

Send
