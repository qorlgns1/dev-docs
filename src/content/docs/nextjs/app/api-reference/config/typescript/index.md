---
title: '구성: TypeScript'
description: 'Next.js는 내장 TypeScript를 제공하므로 으로 새 프로젝트를 만들 때 필요한 패키지를 자동으로 설치하고 적절한 설정을 구성합니다.'
---

# 구성: TypeScript | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/typescript

# TypeScript

최종 업데이트 2026년 2월 20일

Next.js는 내장 TypeScript를 제공하므로 `create-next-app`으로 새 프로젝트를 만들 때 필요한 패키지를 자동으로 설치하고 적절한 설정을 구성합니다.

기존 프로젝트에 TypeScript를 추가하려면 파일을 `.ts` / `.tsx`로 이름만 바꾸면 됩니다. 그런 다음 `next dev`와 `next build`를 실행하면 필요한 종속성이 자동으로 설치되고 권장 구성 옵션이 포함된 `tsconfig.json` 파일이 추가됩니다.

> **알아두면 좋아요** : 이미 `jsconfig.json` 파일이 있다면, 기존 `jsconfig.json`의 `paths` 컴파일러 옵션을 새 `tsconfig.json`으로 복사하고, 이전 `jsconfig.json` 파일은 삭제하세요.

## IDE 플러그인[](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin)

Next.js에는 VSCode 등 코드 편집기에서 고급 타입 검사와 자동 완성을 활용할 수 있는 맞춤형 TypeScript 플러그인과 타입 체커가 포함되어 있습니다.

VS Code에서 플러그인을 활성화하려면 다음을 수행하세요:

  1. 명령 팔레트 열기 (`Ctrl/⌘` \+ `Shift` \+ `P`)
  2. "TypeScript: Select TypeScript Version" 검색
  3. "Use Workspace Version" 선택

이제 파일을 편집할 때 맞춤형 플러그인이 활성화됩니다. `next build`를 실행하면 맞춤형 타입 체커가 사용됩니다.

TypeScript 플러그인은 다음을 도와줍니다:

  * [세그먼트 구성 옵션](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)에 잘못된 값이 전달되면 경고합니다.
  * 사용 가능한 옵션과 상황별 문서를 표시합니다.
  * `'use client'` 지시문이 올바르게 사용되도록 보장합니다.
  * `useState` 같은 클라이언트 훅이 클라이언트 컴포넌트에서만 사용되도록 보장합니다.

> **🎥 시청:** 내장 TypeScript 플러그인 알아보기 → [YouTube (3분)](https://www.youtube.com/watch?v=pqMqn9fKEf8)

## 종단 간 타입 안전성[](https://nextjs.org/docs/app/api-reference/config/typescript#end-to-end-type-safety)

Next.js App Router는 **향상된 타입 안전성**을 제공합니다. 여기에는 다음이 포함됩니다:

  1. **데이터 직렬화 없음** : 서버에서 컴포넌트, 레이아웃, 페이지 내부에서 `fetch`를 직접 호출할 수 있습니다. 이 데이터는 클라이언트에서 React로 소비하기 위해 문자열로 직렬화할 필요가 없습니다. 대신 `app`이 기본적으로 서버 컴포넌트를 사용하므로 `Date`, `Map`, `Set` 등의 값을 추가 작업 없이 사용할 수 있습니다. 과거에는 서버와 클라이언트 사이 경계를 Next.js 전용 타입으로 수동 지정해야 했습니다.
  2. **컴포넌트 간 데이터 흐름 간소화** : 루트 레이아웃으로 `_app`이 대체되면서 컴포넌트와 페이지 간 데이터 흐름을 더 쉽게 파악할 수 있습니다. 예전에는 개별 `pages`와 `_app` 사이로 흐르는 데이터를 타입으로 표현하기 어려워 혼란스러운 버그를 유발할 수 있었습니다. App Router의 [공동 위치 데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data)으로 이러한 문제가 사라집니다.

[Next.js의 데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data)은 데이터베이스나 콘텐츠 공급자 선택을 강제하지 않으면서 가능한 한 종단 간 타입 안전성을 제공합니다.

일반 TypeScript에서 기대하는 방식으로 응답 데이터를 타입 지정할 수 있습니다. 예를 들어:

app/page.tsx

JavaScriptTypeScript
[code]
    async function getData() {
      const res = await fetch('https://api.example.com/...')
      // The return value is *not* serialized
      // You can return Date, Map, Set, etc.
      return res.json()
    }

    export default async function Page() {
      const name = await getData()

      return '...'
    }
[/code]

완전한 종단 간 타입 안전성을 얻으려면 데이터베이스나 콘텐츠 공급자 역시 TypeScript를 지원해야 합니다. 이는 [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) 또는 타입 안전 쿼리 빌더를 사용해 구현할 수 있습니다.

## 라우트 인지 타입 헬퍼[](https://nextjs.org/docs/app/api-reference/config/typescript#route-aware-type-helpers)

Next.js는 App Router 라우트 타입을 위한 전역 헬퍼를 생성합니다. 이들은 `next dev`, `next build`, 또는 [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options) 실행 중에 생성되며 import 없이 사용할 수 있습니다:

  * [`PageProps`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)
  * [`LayoutProps`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)
  * [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)

## `next-env.d.ts`[](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts)

Next.js는 프로젝트 루트에 `next-env.d.ts` 파일을 생성합니다. 이 파일은 Next.js 타입 정의를 참조하여 TypeScript가 코드가 아닌 import(이미지, 스타일시트 등)와 Next.js 전용 타입을 인식할 수 있게 합니다.

`next dev`, `next build`, 또는 [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)을 실행하면 이 파일이 다시 생성됩니다.

> **알아두면 좋아요** :
>
>   * `next-env.d.ts`를 `.gitignore`에 추가하는 것이 좋습니다.
>   * 이 파일은 `tsconfig.json`의 `include` 배열에 있어야 합니다 (`create-next-app`은 자동으로 설정합니다).
>

## 예제[](https://nextjs.org/docs/app/api-reference/config/typescript#examples)

### Next.js 구성 파일 타입 검사[](https://nextjs.org/docs/app/api-reference/config/typescript#type-checking-nextjs-configuration-files)

Next.js 구성에서 `next.config.ts`를 사용하면 TypeScript와 타입 import를 활용할 수 있습니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      /* config options here */
    }

    export default nextConfig
[/code]

현재 `next.config.ts`의 모듈 해석은 CommonJS로 제한됩니다. 그러나 Node.js v22.10.0 이상에서 [Node.js 기본 TypeScript 리졸버](https://nextjs.org/docs/app/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts)를 사용할 때는 ECMAScript Modules(ESM) 문법을 사용할 수 있습니다.

`next.config.js` 파일을 사용할 때는 아래와 같이 JSDoc을 통해 IDE에서 일부 타입 검사를 추가할 수 있습니다:

next.config.js
[code]
    // @ts-check

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }

    module.exports = nextConfig
[/code]

### `next.config.ts`에서 Node.js 기본 TypeScript 리졸버 사용[](https://nextjs.org/docs/app/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts)

> **참고** : Node.js v22.10.0+에서 사용 가능하며 기능을 활성화한 경우에만 작동합니다. Next.js는 기본적으로 활성화하지 않습니다.

Next.js는 **v22.10.0**에 추가된 [`process.features.typescript`](https://nodejs.org/api/process.html#processfeaturestypescript)를 통해 [Node.js 기본 TypeScript 리졸버](https://nodejs.org/api/typescript.html)를 감지합니다. 감지되면 `next.config.ts`에서 상위 수준 `await`와 동적 `import()`를 포함한 기본 ESM을 사용할 수 있습니다. 이 메커니즘은 Node 리졸버의 기능과 제약을 그대로 따릅니다.

Node.js **v22.18.0+**에서는 `process.features.typescript`가 기본 활성화됩니다. **v22.10.0** 이상 **22.17.x** 이하 버전에서는 `NODE_OPTIONS=--experimental-transform-types`로 옵트인하세요:

Terminal
[code]
    NODE_OPTIONS=--experimental-transform-types next <command>
[/code]

#### CommonJS 프로젝트(기본)용[](https://nextjs.org/docs/app/api-reference/config/typescript#for-commonjs-projects-default)

`next.config.ts`가 CommonJS 프로젝트에서 네이티브 ESM 문법을 지원하더라도, Node.js는 기본적으로 `next.config.ts`를 CommonJS 파일로 간주하므로 모듈 문법을 감지하면 파일을 ESM으로 다시 파싱합니다. 따라서 CommonJS 프로젝트에서는 파일이 ESM 모듈임을 명시하기 위해 `next.config.mts` 파일 사용을 권장합니다:

next.config.mts
[code]
    import type { NextConfig } from 'next'

    // Top-level await and dynamic import are supported
    const flags = await import('./flags.js').then((m) => m.default ?? m)

    const nextConfig: NextConfig = {
      /* config options here */
      typedRoutes: Boolean(flags?.typedRoutes),
    }

    export default nextConfig
[/code]

#### ESM 프로젝트용[](https://nextjs.org/docs/app/api-reference/config/typescript#for-esm-projects)

`package.json`에서 `"type"`을 `"module"`로 설정하면 프로젝트가 ESM을 사용합니다. 이 설정에 대해 더 알아보려면 [Node.js 문서](https://nodejs.org/api/packages.html#type)를 참고하세요. 이 경우 `next.config.ts`를 ESM 문법으로 바로 작성할 수 있습니다.

> **알아두면 좋아요** : `package.json`에서 `"type": "module"`을 사용할 때 프로젝트의 모든 `.js`와 `.ts` 파일은 기본적으로 ESM 모듈로 취급됩니다. 필요하다면 CommonJS 문법을 사용하는 파일을 `.cjs` 또는 `.cts` 확장자로 변경해야 할 수도 있습니다.

### 정적 타입의 링크[](https://nextjs.org/docs/app/api-reference/config/typescript#statically-typed-links)

Next.js는 `next/link`를 사용할 때 오타 및 기타 오류를 방지하기 위해 링크를 정적으로 타입 지정하여 페이지 간 탐색 시 타입 안전성을 향상합니다.

Pages Router와 App Router 모두에서 `next/link`의 `href` prop에 대해 작동합니다. App Router에서는 `push`, `replace`, `prefetch` 같은 `next/navigation` 메서드에도 타입을 제공합니다. Pages Router의 `next/router` 메서드에는 타입을 제공하지 않습니다.

문자열 리터럴 `href`는 검증되며, 리터럴이 아닌 `href`는 `as Route`로 캐스팅해야 할 수 있습니다.

이 기능을 사용하려면 `typedRoutes`를 활성화하고 프로젝트가 TypeScript를 사용해야 합니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      typedRoutes: true,
    }

    export default nextConfig
[/code]

Next.js는 `.next/types`에 애플리케이션의 모든 기존 라우트 정보를 포함하는 링크 정의를 생성하며, 이를 통해 TypeScript가 에디터에서 잘못된 링크에 대한 피드백을 제공할 수 있습니다.

> **알아두면 좋아요** : `create-next-app` 없이 프로젝트를 설정했다면, 생성된 Next.js 타입이 `tsconfig.json`의 `include` 배열에 포함되도록 `.next/types/**/*.ts`를 추가하세요:

tsconfig.json
[code]
    {
      "include": [
        "next-env.d.ts",
        ".next/types/**/*.ts",
        "**/*.ts",
        "**/*.tsx"
      ],
      "exclude": ["node_modules"]
    }
[/code]

현재 지원은 동적 세그먼트를 포함한 모든 문자열 리터럴에 적용됩니다. 리터럴이 아닌 문자열은 `as Route`로 수동 캐스팅해야 합니다. 아래 예시는 `next/link`와 `next/navigation` 사용을 모두 보여줍니다:

app/example-client.tsx
[code]
    'use client'

    import type { Route } from 'next'
    import Link from 'next/link'
    import { useRouter } from 'next/navigation'

    export default function Example() {
      const router = useRouter()
      const slug = 'nextjs'

      return (
        <>
          {/* Link: literal and dynamic */}
          <Link href="/about" />
          <Link href={`/blog/${slug}`} />
          <Link href={('/blog/' + slug) as Route} />
          {/* TypeScript error if href is not a valid route */}
          <Link href="/aboot" />

          {/* Router: literal and dynamic strings are validated */}
          <button onClick={() => router.push('/about')}>Push About</button>
          <button onClick={() => router.replace(`/blog/${slug}`)}>
            Replace Blog
          </button>
          <button onClick={() => router.prefetch('/contact')}>
            Prefetch Contact
          </button>

          {/* For non-literal strings, cast to Route */}
          <button onClick={() => router.push(('/blog/' + slug) as Route)}>
            Push Non-literal Blog
          </button>
        </>
      )
    }
[/code]

프록시가 정의한 리디렉션 라우트에도 동일하게 적용됩니다.

proxy.ts
[code]
    import { NextRequest, NextResponse } from 'next/server'

    export function proxy(request: NextRequest) {
      if (request.nextUrl.pathname === '/proxy-redirect') {
        return NextResponse.redirect(new URL('/', request.url))
      }

      return NextResponse.next()
    }
[/code]

app/some/page.tsx
[code]
    import type { Route } from 'next'

    export default function Page() {
      return <Link href={'/proxy-redirect' as Route}>Link Text</Link>
    }
[/code]

`next/link`을 감싸는 커스텀 컴포넌트에서 `href`를 허용하려면 제네릭을 사용하세요:
[code]
    import type { Route } from 'next'
    import Link from 'next/link'

    function Card<T extends string>({ href }: { href: Route<T> | URL }) {
      return (
        <Link href={href}>
          <div>My Card</div>
        </Link>
      )
    }
[/code]

단순한 데이터 구조에 타입을 지정하고 이를 순회하며 링크를 렌더링할 수도 있습니다:

components/nav-items.ts
[code]
    import type { Route } from 'next'

    type NavItem<T extends string = string> = {
      href: T
      label: string
    }

    export const navItems: NavItem<Route>[] = [
      { href: '/', label: 'Home' },
      { href: '/about', label: 'About' },
      { href: '/blog', label: 'Blog' },
    ]
[/code]

그런 다음 항목을 순회(map)하여 `Link`를 렌더링합니다:

components/nav.tsx
[code]
    import Link from 'next/link'
    import { navItems } from './nav-items'

    export function Nav() {
      return (
        <nav>
          {navItems.map((item) => (
            <Link key={item.href} href={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>
      )
    }
[/code]

> **어떻게 동작하나요?**
>
> `next dev` 또는 `next build`를 실행할 때 Next.js는 애플리케이션에 존재하는 모든 라우트 정보(`Link`의 `href` 타입에 해당하는 모든 유효한 라우트)를 포함한 숨겨진 `.d.ts` 파일을 `.next` 내부에 생성합니다. 이 `.d.ts` 파일은 `tsconfig.json`에 포함되며, TypeScript 컴파일러가 해당 `.d.ts`를 검사해 잘못된 링크를 에디터에서 바로 피드백합니다.

### 환경 변수용 타입 IntelliSense[](https://nextjs.org/docs/app/api-reference/config/typescript#type-intellisense-for-environment-variables)

개발 중 Next.js는 `.next/types`에 `.d.ts` 파일을 생성하여 로드된 환경 변수 정보를 에디터 IntelliSense에 제공합니다. 동일한 환경 변수 키가 여러 파일에 정의되어 있다면 [Environment Variable Load Order](https://nextjs.org/docs/app/guides/environment-variables#environment-variable-load-order)에 따라 중복이 제거됩니다.

이 기능을 사용하려면 `experimental.typedEnv`를 활성화하고 프로젝트가 TypeScript를 사용해야 합니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        typedEnv: true,
      },
    }

    export default nextConfig
[/code]

> **알아 두면 좋아요**: 타입은 개발 런타임에 로드된 환경 변수를 기반으로 생성되므로, 기본적으로 `.env.production*` 파일의 변수는 제외됩니다. 프로덕션 전용 변수를 포함하려면 `NODE_ENV=production`으로 `next dev`를 실행하세요.

### Async Server Components와 함께 사용할 때[](https://nextjs.org/docs/app/api-reference/config/typescript#with-async-server-components)

`async` Server Component를 TypeScript와 함께 사용하려면 TypeScript `5.1.3` 이상과 `@types/react` `18.2.8` 이상을 사용 중인지 확인하세요.

구버전 TypeScript를 사용하면 `'Promise<Element>' is not a valid JSX element` 타입 오류가 발생할 수 있습니다. TypeScript와 `@types/react`의 최신 버전으로 업데이트하면 이 문제가 해결됩니다.

### 증분 타입 검사[](https://nextjs.org/docs/app/api-reference/config/typescript#incremental-type-checking)

`v10.2.1`부터 Next.js는 `tsconfig.json`에서 활성화된 경우 [incremental type checking](https://www.typescriptlang.org/tsconfig#incremental)을 지원하며, 대규모 애플리케이션의 타입 검사 속도를 높이는 데 도움이 됩니다.

### 사용자 지정 `tsconfig` 경로[](https://nextjs.org/docs/app/api-reference/config/typescript#custom-tsconfig-path)

특정 빌드나 도구를 위해 다른 TypeScript 구성을 사용하고 싶다면, `next.config.ts`에서 `typescript.tsconfigPath`를 설정하여 Next.js가 다른 `tsconfig` 파일을 참조하도록 만들 수 있습니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }

    export default nextConfig
[/code]

예를 들어, 프로덕션 빌드에서 다른 구성을 사용하도록 전환할 수 있습니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const isProd = process.env.NODE_ENV === 'production'

    const nextConfig: NextConfig = {
      typescript: {
        tsconfigPath: isProd ? 'tsconfig.build.json' : 'tsconfig.json',
      },
    }

    export default nextConfig
[/code]

빌드를 위한 별도의 `tsconfig`를 사용할 수 있는 이유

모노레포처럼 빌드가 프로젝트 기준과 맞지 않는 공유 종속성을 함께 검증해야 하는 상황에서 검사 강도를 완화해야 할 수도 있고, 로컬에서는 더 엄격한 TypeScript 설정으로 마이그레이션하면서도 CI에서는 느슨한 검사를 유지해 배포를 이어가야 할 수도 있습니다(이때 IDE에서는 여전히 잘못된 사용을 강조 표시하길 원할 수 있습니다).

예를 들어 프로젝트는 `useUnknownInCatchVariables`를 사용하지만 어떤 모노레포 종속성은 여전히 `any`를 가정하는 경우:

tsconfig.build.json
[code]
    {
      "extends": "./tsconfig.json",
      "compilerOptions": {
        "useUnknownInCatchVariables": false
      }
    }
[/code]

이렇게 하면 `tsconfig.json`을 통해 에디터는 엄격한 상태를 유지하면서도 프로덕션 빌드는 완화된 설정을 사용할 수 있습니다.

> **알아 두면 좋아요** :
>
>   * IDE는 일반적으로 진단과 IntelliSense를 위해 `tsconfig.json`을 읽으므로, 프로덕션 빌드가 다른 구성을 사용하더라도 IDE 경고를 계속 확인할 수 있습니다. 편집기와 동일한 동작을 원하면 핵심 옵션을 동일하게 맞추세요.
>   * 개발 중에는 `tsconfig.json`만 변경 감지 대상입니다. `typescript.tsconfigPath`로 다른 파일 이름을 편집했다면 변경 사항을 적용하려면 개발 서버를 재시작하세요.
>   * 구성된 파일은 `next dev`, `next build`, `next typegen`에서 사용됩니다.
>

### 프로덕션에서 TypeScript 오류 비활성화[](https://nextjs.org/docs/app/api-reference/config/typescript#disabling-typescript-errors-in-production)

프로젝트에 TypeScript 오류가 있으면 Next.js는 **프로덕션 빌드**(`next build`)를 실패 처리합니다.

애플리케이션에 오류가 있어도 위험을 감수하고 프로덕션 코드를 생성하고 싶다면, 내장 타입 검사 단계를 비활성화할 수 있습니다.

비활성화할 경우 빌드나 배포 프로세스의 일부로 반드시 타입 검사를 수행해야 합니다. 그렇지 않으면 매우 위험할 수 있습니다.

`next.config.ts`를 열고 [`typescript`](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript) 구성에서 `ignoreBuildErrors` 옵션을 활성화하세요:

next.config.ts
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }

    export default nextConfig
[/code]

> **알아 두면 좋아요** : 빌드 전에 직접 TypeScript 오류를 확인하려면 `tsc --noEmit`을 실행할 수 있습니다. 이는 배포 전에 TypeScript 오류를 확인하고 싶은 CI/CD 파이프라인에 유용합니다.

### 사용자 지정 타입 선언[](https://nextjs.org/docs/app/api-reference/config/typescript#custom-type-declarations)

커스텀 타입을 선언해야 할 때 `next-env.d.ts`를 수정하고 싶어질 수 있지만, 이 파일은 자동 생성되므로 수정 사항이 덮어쓰여집니다. 대신 `new-types.d.ts` 같은 새 파일을 만들고 `tsconfig.json`에 참조를 추가하세요:

tsconfig.json
[code]
    {
      "compilerOptions": {
        "skipLibCheck": true
        //...truncated...
      },
      "include": [
        "new-types.d.ts",
        "next-env.d.ts",
        ".next/types/**/*.ts",
        "**/*.ts",
        "**/*.tsx"
      ],
      "exclude": ["node_modules"]
    }
[/code]

## 버전 변경 사항[](https://nextjs.org/docs/app/api-reference/config/typescript#version-changes)

Version| 변경 내용
---|---
`v15.0.0`| TypeScript 프로젝트에서 [`next.config.ts`](https://nextjs.org/docs/app/api-reference/config/typescript#type-checking-nextjs-configuration-files) 지원이 추가되었습니다.
`v13.2.0`| 정적 타입의 링크가 베타로 제공됩니다.
`v12.0.0`| [SWC](https://nextjs.org/docs/architecture/nextjs-compiler)가 기본 TypeScript/TSX 컴파일러가 되어 빌드 속도가 향상되었습니다.
`v10.2.1`| `tsconfig.json`에서 활성화된 경우 [incremental type checking](https://www.typescriptlang.org/tsconfig#incremental) 지원이 추가되었습니다.

보내기
