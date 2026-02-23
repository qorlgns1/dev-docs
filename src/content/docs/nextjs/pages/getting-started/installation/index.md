---
title: '시작하기: 설치'
description: '시작하기 전에 개발 환경이 다음 요구 사항을 충족하는지 확인하세요.'
---

# 시작하기: 설치 | Next.js

출처 URL: https://nextjs.org/docs/pages/getting-started/installation

# 새로운 Next.js 애플리케이션 만들기

마지막 업데이트 2026년 2월 20일

## 시스템 요구 사항[](https://nextjs.org/docs/pages/getting-started/installation#system-requirements)

시작하기 전에 개발 환경이 다음 요구 사항을 충족하는지 확인하세요.

  * 최소 Node.js 버전: [20.9](https://nodejs.org/)
  * 운영 체제: macOS, Windows(WSL 포함), Linux

## 지원되는 브라우저[](https://nextjs.org/docs/pages/getting-started/installation#supported-browsers)

Next.js는 추가 설정 없이 최신 브라우저를 지원합니다.

  * Chrome 111+
  * Edge 111+
  * Firefox 111+
  * Safari 16.4+

폴리필 구성 및 특정 브라우저 타깃팅 방법을 포함한 [브라우저 지원](https://nextjs.org/docs/architecture/supported-browsers)에 대해 더 알아보세요.

## CLI로 생성하기[](https://nextjs.org/docs/pages/getting-started/installation#create-with-the-cli)

가장 빠르게 새로운 Next.js 앱을 만드는 방법은 모든 것을 자동으로 설정해 주는 [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app)을 사용하는 것입니다. 프로젝트를 만들려면 다음을 실행하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm create next-app
[/code]

설치 중 다음과 같은 프롬프트가 표시됩니다.

터미널
[code]
    What is your project named? my-app
    Would you like to use the recommended Next.js defaults?
        Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
        No, reuse previous settings
        No, customize settings - Choose your own preferences
[/code]

`customize settings`를 선택하면 다음 프롬프트가 이어집니다.

터미널
[code]
    Would you like to use TypeScript? No / Yes
    Which linter would you like to use? ESLint / Biome / None
    Would you like to use React Compiler? No / Yes
    Would you like to use Tailwind CSS? No / Yes
    Would you like your code inside a `src/` directory? No / Yes
    Would you like to use App Router? (recommended) No / Yes
    Would you like to customize the import alias (`@/*` by default)? No / Yes
    What import alias would you like configured? @/*
[/code]

프롬프트가 끝나면 [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app)이 프로젝트 이름의 폴더를 생성하고 필요한 의존성을 설치합니다.

## 수동 설치[](https://nextjs.org/docs/pages/getting-started/installation#manual-installation)

새로운 Next.js 앱을 수동으로 만들려면 필요한 패키지를 설치하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm i next@latest react@latest react-dom@latest
[/code]

> **알아두면 좋아요** : App Router는 모든 안정적인 React 19 변경 사항과 프레임워크에서 검증 중인 최신 기능을 포함한 [React canary 릴리스](https://react.dev/blog/2023/05/03/react-canaries)를 기본으로 사용합니다. Pages Router는 `package.json`에 설치한 React 버전을 사용합니다.

그런 다음 `package.json` 파일에 다음 스크립트를 추가하세요.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "eslint",
        "lint:fix": "eslint --fix"
      }
    }
[/code]

이 스크립트는 애플리케이션 개발 단계마다 다음 작업을 수행합니다.

  * `next dev`: Turbopack(기본 번들러)을 사용해 개발 서버를 시작합니다.
  * `next build`: 애플리케이션을 프로덕션용으로 빌드합니다.
  * `next start`: 프로덕션 서버를 시작합니다.
  * `eslint`: ESLint를 실행합니다.

Turbopack이 기본 번들러입니다. Webpack을 사용하려면 `next dev --webpack` 또는 `next build --webpack`을 실행하세요. 구성 세부 정보는 [Turbopack 문서](https://nextjs.org/docs/app/api-reference/turbopack)를 참고하세요.

### `pages` 디렉터리 만들기[](https://nextjs.org/docs/pages/getting-started/installation#create-the-pages-directory)

Next.js는 파일 시스템 라우팅을 사용하므로 애플리케이션의 라우트는 파일 구조에 따라 결정됩니다.

프로젝트 루트에 `pages` 디렉터리를 만든 다음 그 안에 `index.tsx` 파일을 추가하세요. 이 파일이 홈 페이지(`/`)가 됩니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }
[/code]

이후 전역 레이아웃을 정의하기 위해 `pages/`에 `_app.tsx` 파일을 추가하세요. [사용자 정의 App 파일](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)에 대해 더 알아보세요.

pages/_app.tsx

JavaScriptTypeScript
[code]
    import type { AppProps } from 'next/app'

    export default function App({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
[/code]

마지막으로 서버의 초기 응답을 제어하려면 `pages/`에 `_document.tsx` 파일을 추가하세요. [사용자 정의 Document 파일](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)에 대해 더 알아보세요.

pages/_document.tsx

JavaScriptTypeScript
[code]
    import { Html, Head, Main, NextScript } from 'next/document'

    export default function Document() {
      return (
        <Html>
          <Head />
          <body>
            <Main />
            <NextScript />
          </body>
        </Html>
      )
    }
[/code]

### `public` 폴더 만들기(선택 사항)[](https://nextjs.org/docs/pages/getting-started/installation#create-the-public-folder-optional)

이미지, 폰트 등의 정적 자산을 저장하려면 프로젝트 루트에 [`public` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)를 만드세요. `public` 안의 파일은 기본 URL(`/`)을 기준으로 코드에서 참조할 수 있습니다.

이후 루트 경로(`/`)를 사용해 자산을 참조하면 됩니다. 예를 들어 `public/profile.png`는 `/profile.png`로 참조할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'

    export default function Page() {
      return <Image src="/profile.png" alt="Profile" width={100} height={100} />
    }
[/code]

## 개발 서버 실행[](https://nextjs.org/docs/pages/getting-started/installation#run-the-development-server)

  1. `npm run dev`를 실행해 개발 서버를 시작합니다.
  2. `http://localhost:3000`에 접속해 애플리케이션을 확인합니다.
  3. `pages/index.tsx` 파일을 수정 후 저장하면 브라우저에서 업데이트된 결과를 볼 수 있습니다.

## TypeScript 설정[](https://nextjs.org/docs/pages/getting-started/installation#set-up-typescript)

> 최소 TypeScript 버전: `v5.1.0`

Next.js에는 TypeScript 지원이 내장되어 있습니다. 프로젝트에 TypeScript를 추가하려면 파일 확장자를 `.ts` / `.tsx`로 변경하고 `next dev`를 실행하세요. Next.js가 필요한 의존성을 자동으로 설치하고 권장 설정이 포함된 `tsconfig.json` 파일을 추가합니다.

자세한 내용은 [TypeScript 참고 문서](https://nextjs.org/docs/app/api-reference/config/typescript)를 확인하세요.

## 린팅 설정[](https://nextjs.org/docs/pages/getting-started/installation#set-up-linting)

Next.js는 ESLint 또는 Biome을 사용한 린팅을 지원합니다. 원하는 린터를 선택하고 `package.json` 스크립트로 직접 실행하세요.

  * **ESLint**(포괄적인 규칙) 사용:

package.json
[code]
    {
      "scripts": {
        "lint": "eslint",
        "lint:fix": "eslint --fix"
      }
    }
[/code]

  * 또는 **Biome**(빠른 린터 + 포매터) 사용:

package.json
[code]
    {
      "scripts": {
        "lint": "biome check",
        "format": "biome format --write"
      }
    }
[/code]

기존에 `next lint`를 사용했다면 다음 코드를 이용해 스크립트를 ESLint CLI로 마이그레이션하세요.

터미널
[code]
    npx @next/codemod@canary next-lint-to-eslint-cli .
[/code]

ESLint를 사용한다면 명시적인 구성(권장: `eslint.config.mjs`)을 생성하세요. ESLint는 [기존 `.eslintrc.*`와 새로운 `eslint.config.mjs` 형식](https://eslint.org/docs/latest/use/configure/configuration-files#configuring-eslint)을 모두 지원합니다. 권장 설정은 [ESLint API 레퍼런스](https://nextjs.org/docs/app/api-reference/config/eslint#with-core-web-vitals)를 참조하세요.

> **알아두면 좋아요** : Next.js 16부터 `next build`는 린터를 자동으로 실행하지 않습니다. 대신 NPM 스크립트를 통해 린터를 실행하세요.

자세한 내용은 [ESLint 플러그인](https://nextjs.org/docs/app/api-reference/config/eslint) 페이지를 확인하세요.

## 절대 경로 임포트 및 모듈 경로 별칭 설정[](https://nextjs.org/docs/pages/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)

Next.js는 `tsconfig.json`과 `jsconfig.json` 파일의 `"paths"` 및 `"baseUrl"` 옵션을 기본 지원합니다.

이 옵션을 사용하면 프로젝트 디렉터리를 절대 경로로 별칭 처리해 모듈을 더 쉽게, 깔끔하게 임포트할 수 있습니다. 예:

[code]
    // Before
    import { Button } from '../../../components/button'

    // After
    import { Button } from '@/components/button'
[/code]

절대 경로 임포트를 구성하려면 `tsconfig.json` 또는 `jsconfig.json` 파일에 `baseUrl` 옵션을 추가하세요. 예:

tsconfig.json or jsconfig.json
[code]
    {
      "compilerOptions": {
        "baseUrl": "src/"
      }
    }
[/code]

`baseUrl` 경로를 설정하는 것 외에도 `"paths"` 옵션을 사용해 모듈 경로를 `"alias"`로 매핑할 수 있습니다.

예를 들어 다음 구성은 `@/components/*`를 `components/*`에 매핑합니다.

tsconfig.json or jsconfig.json
[code]
    {
      "compilerOptions": {
        "baseUrl": "src/",
        "paths": {
          "@/styles/*": ["styles/*"],
          "@/components/*": ["components/*"]
        }
      }
    }
[/code]

각 `"paths"` 값은 `baseUrl` 위치를 기준으로 합니다.

보내기
