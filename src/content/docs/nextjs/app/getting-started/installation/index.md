---
title: '시작하기: 설치'
description: '최종 업데이트: 2026년 2월 20일'
---

# 시작하기: 설치 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/installation

# 설치

최종 업데이트: 2026년 2월 20일

새로운 Next.js 앱을 생성하고 로컬에서 실행하세요.

## 빠른 시작[](https://nextjs.org/docs/app/getting-started/installation#quick-start)

  1. `my-app`이라는 이름의 새 Next.js 앱을 생성합니다.
  2. `cd my-app`으로 이동해 개발 서버를 시작합니다.
  3. `http://localhost:3000`에 접속합니다.

pnpmnpmyarnbun

터미널
[code]
    pnpm create next-app@latest my-app --yes
    cd my-app
    pnpm dev
[/code]

  * `--yes`는 저장된 기본값으로 프롬프트를 건너뜁니다. 기본 설정은 TypeScript, Tailwind, ESLint, App Router, Turbopack, `@/*` 임포트 별칭을 활성화합니다.

## 시스템 요구 사항[](https://nextjs.org/docs/app/getting-started/installation#system-requirements)

시작하기 전에 개발 환경이 아래 요구 사항을 충족하는지 확인하세요.

  * 최소 Node.js 버전: [20.9](https://nodejs.org/)
  * 지원 OS: macOS, Windows(WSL 포함), Linux

## 지원 브라우저[](https://nextjs.org/docs/app/getting-started/installation#supported-browsers)

Next.js는 추가 설정 없이 최신 브라우저를 지원합니다.

  * Chrome 111+
  * Edge 111+
  * Firefox 111+
  * Safari 16.4+

폴리필 구성 및 특정 브라우저 타깃팅 방법을 포함해 [브라우저 지원](https://nextjs.org/docs/architecture/supported-browsers)에 대해 자세히 알아보세요.

## CLI로 생성하기[](https://nextjs.org/docs/app/getting-started/installation#create-with-the-cli)

[`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app)을 사용하면 새로운 Next.js 앱을 가장 빠르게 만들 수 있으며 필요한 구성이 자동으로 완료됩니다. 프로젝트를 만들려면 다음 명령을 실행하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm create next-app
[/code]

설치 시 다음과 같은 프롬프트가 표시됩니다.

터미널
[code]
    What is your project named? my-app
    Would you like to use the recommended Next.js defaults?
        Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
        No, reuse previous settings
        No, customize settings - Choose your own preferences
[/code]

`customize settings`를 선택하면 아래 프롬프트가 이어집니다.

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

프롬프트가 끝나면 [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app)이 프로젝트 이름으로 폴더를 만들고 필요한 의존성을 설치합니다.

## 수동 설치[](https://nextjs.org/docs/app/getting-started/installation#manual-installation)

수동으로 새 Next.js 앱을 만들려면 필요한 패키지를 설치하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm i next@latest react@latest react-dom@latest
[/code]

> **알아두면 좋아요** : App Router는 [React Canary 릴리스](https://react.dev/blog/2023/05/03/react-canaries)를 기본으로 사용하며, 안정화된 React 19 변경 사항과 프레임워크에서 검증 중인 신규 기능을 모두 포함합니다. Pages Router는 `package.json`에 설치한 React 버전을 사용합니다.

그런 다음 `package.json`에 다음 스크립트를 추가하세요.

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

이 스크립트는 애플리케이션 개발의 다양한 단계를 나타냅니다.

  * `next dev`: Turbopack(기본 번들러)으로 개발 서버를 시작합니다.
  * `next build`: 프로덕션용 애플리케이션을 빌드합니다.
  * `next start`: 프로덕션 서버를 시작합니다.
  * `eslint`: ESLint를 실행합니다.

Turbopack이 기본 번들러입니다. Webpack을 사용하려면 `next dev --webpack` 또는 `next build --webpack`을 실행하세요. 구성은 [Turbopack 문서](https://nextjs.org/docs/app/api-reference/turbopack)를 참조하세요.

### `app` 디렉터리 만들기[](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory)

Next.js는 파일 시스템 라우팅을 사용하므로 애플리케이션의 경로는 파일 구조로 결정됩니다.

`app` 폴더를 만들고, 그 안에 `layout.tsx` 파일을 생성하세요. 이 파일은 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)으로 `<html>`과 `<body>` 태그를 반드시 포함해야 합니다.

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
[/code]

다음으로 초기 콘텐츠가 있는 홈 페이지 `app/page.tsx`를 만드세요.

app/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }
[/code]

`layout.tsx`와 `page.tsx`는 사용자가 애플리케이션 루트(`/`)에 접근할 때 함께 렌더링됩니다.

> **알아두면 좋아요** :
>
>   * 루트 레이아웃을 만들지 않아도 `next dev`로 개발 서버를 실행하면 Next.js가 자동으로 생성합니다.
>   * 프로젝트 루트에 [`src` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)를 두어 애플리케이션 코드와 설정 파일을 분리할 수도 있습니다.
>

### `public` 폴더 만들기(선택)[](https://nextjs.org/docs/app/getting-started/installation#create-the-public-folder-optional)

이미지, 폰트 등 정적 자산을 저장하려면 프로젝트 루트에 [`public` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)를 만드세요. `public` 내부 파일은 기본 URL(`/`)을 기준으로 코드에서 참조할 수 있습니다.

이 자산은 루트 경로(`/`)로 참조합니다. 예를 들어 `public/profile.png`는 `/profile.png`로 사용할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'

    export default function Page() {
      return <Image src="/profile.png" alt="Profile" width={100} height={100} />
    }
[/code]

## 개발 서버 실행[](https://nextjs.org/docs/app/getting-started/installation#run-the-development-server)

  1. `npm run dev`로 개발 서버를 실행합니다.
  2. `http://localhost:3000`에서 애플리케이션을 확인합니다.
  3. `app/page.tsx`를 수정하고 저장하면 브라우저에 변경 내용이 반영됩니다.

## TypeScript 설정[](https://nextjs.org/docs/app/getting-started/installation#set-up-typescript)

> 최소 TypeScript 버전: `v5.1.0`

Next.js는 TypeScript를 기본 지원합니다. 프로젝트에 TypeScript를 추가하려면 파일 확장자를 `.ts` / `.tsx`로 변경하고 `next dev`를 실행하세요. Next.js가 필요한 의존성을 설치하고 권장 설정이 담긴 `tsconfig.json`을 추가합니다.

### IDE 플러그인[](https://nextjs.org/docs/app/getting-started/installation#ide-plugin)

Next.js에는 VS Code 등 코드 에디터에서 고급 타입 검사와 자동 완성에 사용할 수 있는 커스텀 TypeScript 플러그인과 타입 체커가 포함되어 있습니다.

VS Code에서 플러그인을 활성화하려면:

  1. 명령 팔레트(`Ctrl/⌘` + `Shift` + `P`)를 엽니다.
  2. "TypeScript: Select TypeScript Version"을 검색합니다.
  3. "Use Workspace Version"을 선택합니다.

자세한 내용은 [TypeScript 레퍼런스](https://nextjs.org/docs/app/api-reference/config/typescript)를 확인하세요.

## 린팅 설정[](https://nextjs.org/docs/app/getting-started/installation#set-up-linting)

Next.js는 ESLint 또는 Biome으로 린팅을 지원합니다. 린터를 선택하고 `package.json` 스크립트로 실행하세요.

  * **ESLint**(포괄적 규칙) 사용:

package.json
[code]
    {
      "scripts": {
        "lint": "eslint",
        "lint:fix": "eslint --fix"
      }
    }
[/code]

  * **Biome**(빠른 린터 + 포매터) 사용:

package.json
[code]
    {
      "scripts": {
        "lint": "biome check",
        "format": "biome format --write"
      }
    }
[/code]

과거에 `next lint`를 사용했다면 codemod로 ESLint CLI 스크립트로 마이그레이션하세요.

터미널
[code]
    npx @next/codemod@canary next-lint-to-eslint-cli .
[/code]

ESLint를 사용하는 경우 명시적인 설정 파일(권장: `eslint.config.mjs`)을 생성하세요. ESLint는 [기존 `.eslintrc.*`와 새로운 `eslint.config.mjs`](https://eslint.org/docs/latest/use/configure/configuration-files#configuring-eslint) 형식을 모두 지원합니다. 권장 설정은 [ESLint API 레퍼런스](https://nextjs.org/docs/app/api-reference/config/eslint#with-core-web-vitals)를 참조하세요.

> **알아두면 좋아요** : Next.js 16부터 `next build`는 린터를 자동 실행하지 않습니다. 대신 NPM 스크립트로 린터를 실행하세요.

자세한 내용은 [ESLint 플러그인](https://nextjs.org/docs/app/api-reference/config/eslint) 페이지를 확인하세요.

## 절대 경로 임포트와 모듈 경로 별칭 설정[](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)

Next.js는 `tsconfig.json`과 `jsconfig.json` 파일의 `"paths"`와 `"baseUrl"` 옵션을 기본 지원합니다.

이 옵션은 프로젝트 디렉터리를 절대 경로로 별칭 처리하여 모듈 임포트를 더 깔끔하게 만듭니다. 예:

[code]
    // Before
    import { Button } from '../../../components/button'

    // After
    import { Button } from '@/components/button'
[/code]

절대 임포트를 설정하려면 `tsconfig.json` 또는 `jsconfig.json`에 `baseUrl` 옵션을 추가하세요. 예:

tsconfig.json 또는 jsconfig.json
[code]
    {
      "compilerOptions": {
        "baseUrl": "src/"
      }
    }
[/code]

`baseUrl` 경로를 지정한 뒤 `"paths"` 옵션으로 모듈 경로를 `"alias"`로 매핑할 수 있습니다.

아래 설정은 `@/components/*`를 `components/*`에 매핑합니다.

tsconfig.json 또는 jsconfig.json
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

각 `"paths"`는 `baseUrl` 위치를 기준으로 합니다.

보내기
