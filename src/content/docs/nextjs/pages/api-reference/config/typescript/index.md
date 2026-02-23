---
title: '구성: TypeScript'
description: '소스 URL: https://nextjs.org/docs/pages/api-reference/config/typescript'
---

# 구성: TypeScript | Next.js

소스 URL: https://nextjs.org/docs/pages/api-reference/config/typescript

[API Reference](https://nextjs.org/docs/pages/api-reference)[Configuration](https://nextjs.org/docs/pages/api-reference/config)타입스크립트

페이지 복사

# 타입스크립트

마지막 업데이트: 2026년 2월 20일

Next.js에는 기본적으로 TypeScript가 포함되어 있어 `create-next-app`으로 새 프로젝트를 만들 때 필요한 패키지를 자동으로 설치하고 적절한 설정을 구성합니다.

기존 프로젝트에 TypeScript를 추가하려면 파일 확장자를 `.ts` / `.tsx`로 바꾸십시오. 그런 다음 `next dev`와 `next build`를 실행하면 필요한 의존성이 자동으로 설치되고 권장 구성 옵션이 포함된 `tsconfig.json` 파일이 추가됩니다.

> **알아두면 좋은 점** : 이미 `jsconfig.json` 파일이 있다면 `paths` 컴파일러 옵션을 새 `tsconfig.json`으로 복사한 뒤 기존 `jsconfig.json`을 삭제하세요.

## `next-env.d.ts`[](https://nextjs.org/docs/pages/api-reference/config/typescript#next-envdts)

Next.js는 프로젝트 루트에 `next-env.d.ts` 파일을 생성합니다. 이 파일은 Next.js 타입 정의를 참조하여 TypeScript가 비코드 임포트(이미지, 스타일시트 등)와 Next.js 전용 타입을 인식할 수 있게 해줍니다.

`next dev`, `next build`, [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)을 실행하면 이 파일이 다시 생성됩니다.

> **알아두면 좋은 점** :
> 
>   * `next-env.d.ts`를 `.gitignore`에 추가하는 것이 좋습니다.
>   * 이 파일은 `tsconfig.json`의 `include` 배열에 반드시 포함되어야 합니다(`create-next-app`은 자동으로 처리합니다).
> 

## 예시[](https://nextjs.org/docs/pages/api-reference/config/typescript#examples)

### Next.js 구성 파일 타입 검사[](https://nextjs.org/docs/pages/api-reference/config/typescript#type-checking-nextjs-configuration-files)

`next.config.ts`를 사용하면 Next.js 구성에서 TypeScript와 타입 임포트를 사용할 수 있습니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      /* config options here */
    }
     
    export default nextConfig
[/code]

현재 `next.config.ts`의 모듈 해석은 CommonJS로 제한됩니다. 그러나 Node.js v22.10.0 이상에서 [Node.js 기본 TypeScript 리졸버](https://nextjs.org/docs/pages/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts)를 사용할 때는 ECMAScript Modules(ESM) 문법을 사용할 수 있습니다.

`next.config.js` 파일을 사용할 경우 아래와 같이 JSDoc을 통해 IDE에서 일부 타입 검사를 추가할 수 있습니다.

next.config.js
[code]
    // @ts-check
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }
     
    module.exports = nextConfig
[/code]

### `next.config.ts`를 위한 Node.js 기본 TypeScript 리졸버 사용[](https://nextjs.org/docs/pages/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts)

> **참고** : Node.js v22.10.0+에서 사용 가능하며 기능을 직접 활성화해야 합니다. Next.js는 기본적으로 활성화하지 않습니다.

Next.js는 **v22.10.0**에 추가된 [`process.features.typescript`](https://nodejs.org/api/process.html#processfeaturestypescript)를 통해 [Node.js 기본 TypeScript 리졸버](https://nodejs.org/api/typescript.html)를 감지합니다. 이를 사용할 수 있을 때 `next.config.ts`는 최상위 `await`와 동적 `import()`를 포함한 네이티브 ESM을 사용할 수 있습니다. 이 메커니즘은 Node 리졸버의 기능과 제한을 그대로 따릅니다.

Node.js **v22.18.0+**에서는 `process.features.typescript`가 기본 활성화됩니다. **v22.10.0**부터 **22.17.x**까지의 버전에서는 `NODE_OPTIONS=--experimental-transform-types`로 옵트인해야 합니다.

Terminal
[code]
    NODE_OPTIONS=--experimental-transform-types next <command>
[/code]

#### CommonJS 프로젝트(기본값)용[](https://nextjs.org/docs/pages/api-reference/config/typescript#for-commonjs-projects-default)

`next.config.ts`가 CommonJS 프로젝트에서 네이티브 ESM 문법을 지원하더라도 Node.js는 기본적으로 `next.config.ts`를 CommonJS 파일로 간주하므로 모듈 문법을 감지하면 파일을 ESM으로 다시 파싱합니다. 따라서 CommonJS 프로젝트에서는 해당 파일이 ESM 모듈임을 명시적으로 나타내기 위해 `next.config.mts` 파일을 사용하는 것이 좋습니다.

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

#### ESM 프로젝트용[](https://nextjs.org/docs/pages/api-reference/config/typescript#for-esm-projects)

`package.json`에서 `"type"`이 `"module"`로 설정되어 있으면 프로젝트는 ESM을 사용합니다. 이 설정에 대해 [Node.js 문서](https://nodejs.org/api/packages.html#type)에서 자세히 알아보세요. 이 경우 `next.config.ts`를 그대로 ESM 문법으로 작성하면 됩니다.

> **알아두면 좋은 점** : `package.json`에 `"type": "module"`을 사용하면 프로젝트의 모든 `.js`와 `.ts` 파일이 기본적으로 ESM 모듈로 처리됩니다. CommonJS 문법을 사용하는 파일은 필요에 따라 `.cjs` 또는 `.cts` 확장자로 이름을 바꿔야 할 수 있습니다.

### 정적 타입 링크[](https://nextjs.org/docs/pages/api-reference/config/typescript#statically-typed-links)

Next.js는 `next/link`를 사용할 때 링크를 정적으로 타입 지정하여 페이지 간 이동 시 오타 및 기타 오류를 방지하고 타입 안정성을 높여줍니다.

Pages와 App Router 모두에서 `next/link`의 `href` prop에 적용됩니다. App Router에서는 `push`, `replace`, `prefetch` 같은 `next/navigation` 메서드에도 타입을 제공합니다. Pages Router의 `next/router` 메서드에는 타입을 제공하지 않습니다.

리터럴 `href` 문자열은 검증되며, 비리터럴 `href`는 `as Route` 캐스트가 필요할 수 있습니다.

이 기능을 사용하려면 `typedRoutes`를 활성화하고 프로젝트가 TypeScript를 사용해야 합니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      typedRoutes: true,
    }
     
    export default nextConfig
[/code]

Next.js는 애플리케이션의 모든 기존 라우트 정보를 담은 링크 정의를 `.next/types`에 생성하며, TypeScript는 이를 사용해 에디터에서 잘못된 링크에 대한 피드백을 제공합니다.

> **알아두면 좋은 점** : `create-next-app` 없이 프로젝트를 설정했다면, 생성된 Next.js 타입이 포함되도록 `tsconfig.json`의 `include` 배열에 `.next/types/**/*.ts`를 추가하세요.

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

현재는 동적 세그먼트를 포함한 모든 문자열 리터럴이 지원됩니다. 비리터럴 문자열은 `as Route`로 직접 캐스트해야 합니다. 아래 예시는 `next/link`와 `next/navigation` 모두의 사용법을 보여줍니다.

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

프록시로 정의한 리디렉션 라우트에도 동일하게 적용됩니다.

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

`next/link`를 래핑하는 커스텀 컴포넌트에서 `href`를 허용하려면 제네릭을 사용하세요.
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

간단한 데이터 구조에 타입을 지정하고 반복 렌더링으로 링크를 만들 수도 있습니다.

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

그런 다음 항목을 순회하며 `Link`를 렌더링합니다.

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

> **작동 방식은 무엇인가요?**
> 
> `next dev` 또는 `next build`를 실행하면 Next.js가 애플리케이션의 모든 기존 라우트 정보를 담은 숨김 `.d.ts` 파일을 `.next` 내부에 생성합니다(`Link`의 `href` 타입으로 모든 유효한 라우트가 포함됨). 이 `.d.ts` 파일은 `tsconfig.json`에 포함되며 TypeScript 컴파일러가 이를 확인해 에디터에서 잘못된 링크를 알려줍니다.

### 환경 변수 타입 IntelliSense[](https://nextjs.org/docs/pages/api-reference/config/typescript#type-intellisense-for-environment-variables)

개발 중 Next.js는 `.next/types`에 로드된 환경 변수 정보를 담은 `.d.ts` 파일을 생성하여 에디터 IntelliSense를 제공합니다. 동일한 환경 변수 키가 여러 파일에 정의된 경우 [환경 변수 로드 순서](https://nextjs.org/docs/app/guides/environment-variables#environment-variable-load-order)에 따라 중복이 제거됩니다.

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

> **알아두면 좋은 점** : 타입은 개발 런타임에서 로드된 환경 변수를 기반으로 생성되므로 기본적으로 `.env.production*` 파일의 변수는 제외됩니다. 프로덕션 전용 변수를 포함하려면 `NODE_ENV=production`으로 `next dev`를 실행하세요.

### 정적 생성과 서버 사이드 렌더링[](https://nextjs.org/docs/pages/api-reference/config/typescript#static-generation-and-server-side-rendering)

[`getStaticProps`](https://nextjs.org/docs/pages/api-reference/functions/get-static-props), [`getStaticPaths`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths), [`getServerSideProps`](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)에 각각 `GetStaticProps`, `GetStaticPaths`, `GetServerSideProps` 타입을 사용할 수 있습니다.

pages/blog/[slug].tsx
[code]
[/code]

import type { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'
     
    export const getStaticProps = (async (context) => {
      // ...
    }) satisfies GetStaticProps
     
    export const getStaticPaths = (async () => {
      // ...
    }) satisfies GetStaticPaths
     
    export const getServerSideProps = (async (context) => {
      // ...
    }) satisfies GetServerSideProps
[/code]

> **알아두면 좋아요:** `satisfies`는 TypeScript [4.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html)에서 추가되었습니다. TypeScript 최신 버전으로 업그레이드하는 것을 권장합니다.

### API Routes와 함께[](https://nextjs.org/docs/pages/api-reference/config/typescript#with-api-routes)

다음은 API 경로에서 내장 타입을 사용하는 방법의 예시입니다.

pages/api/hello.ts
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      res.status(200).json({ name: 'John Doe' })
    }
[/code]

응답 데이터에도 타입을 지정할 수 있습니다.

pages/api/hello.ts
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    type Data = {
      name: string
    }
     
    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<Data>
    ) {
      res.status(200).json({ name: 'John Doe' })
    }
[/code]

### 커스텀 `App` 사용하기[](https://nextjs.org/docs/pages/api-reference/config/typescript#with-custom-app)

[커스텀 `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)을 사용하는 경우 내장 타입 `AppProps`를 활용하고 파일 이름을 `./pages/_app.tsx`로 변경할 수 있습니다.
[code]
    import type { AppProps } from 'next/app'
     
    export default function MyApp({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
[/code]

### 증분 타입 검사[](https://nextjs.org/docs/pages/api-reference/config/typescript#incremental-type-checking)

`v10.2.1`부터 Next.js는 `tsconfig.json`에서 활성화했을 때 [증분 타입 검사](https://www.typescriptlang.org/tsconfig#incremental)를 지원하므로, 대규모 애플리케이션의 타입 검사 속도를 높일 수 있습니다.

### 사용자 지정 `tsconfig` 경로[](https://nextjs.org/docs/pages/api-reference/config/typescript#custom-tsconfig-path)

빌드나 도구용으로 다른 TypeScript 구성을 사용하고 싶다면 `next.config.ts`에서 `typescript.tsconfigPath`를 설정하여 Next.js가 다른 `tsconfig` 파일을 가리키도록 하면 됩니다.

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

예를 들어, 프로덕션 빌드 시 다른 구성을 사용하도록 전환할 수 있습니다.

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

빌드 전용 별도의 `tsconfig`를 사용하는 이유

모노레포처럼 빌드가 프로젝트 표준과 맞지 않는 공유 의존성을 검사해야 하거나, CI에서는 느슨한 검사를 유지하면서 로컬에서는 더 엄격한 TypeScript 설정으로 마이그레이션하고 IDE 경고는 계속 받고 싶을 때 검사 강도를 완화할 필요가 있을 수 있습니다.

예를 들어 프로젝트에서 `useUnknownInCatchVariables`를 사용하지만 일부 모노레포 의존성은 여전히 `any`를 가정하는 경우:

tsconfig.build.json
[code]
    {
      "extends": "./tsconfig.json",
      "compilerOptions": {
        "useUnknownInCatchVariables": false
      }
    }
[/code]

이렇게 하면 `tsconfig.json`을 통해 에디터는 엄격함을 유지하면서 프로덕션 빌드는 완화된 설정을 사용할 수 있습니다.

> **알아두면 좋아요** :
> 
>   * IDE는 보통 진단과 IntelliSense를 위해 `tsconfig.json`을 읽으므로, 프로덕션 빌드가 다른 구성을 사용해도 IDE 경고를 계속 볼 수 있습니다. 에디터와 동등한 동작을 원하면 핵심 옵션을 맞춰 주세요.
>   * 개발 모드에서는 `tsconfig.json`만 변경 감지 대상입니다. `typescript.tsconfigPath`로 다른 파일 이름을 편집했다면 변경 사항을 적용하려면 개발 서버를 재시작하세요.
>   * 구성한 파일은 `next dev`, `next build`, `next typegen`에서 사용됩니다.
> 

### 프로덕션에서 TypeScript 오류 비활성화[](https://nextjs.org/docs/pages/api-reference/config/typescript#disabling-typescript-errors-in-production)

프로젝트에 TypeScript 오류가 있으면 Next.js는 **프로덕션 빌드**(`next build`)를 실패시킵니다.

애플리케이션에 오류가 있더라도 위험을 감수하고 Next.js가 프로덕션 코드를 생성하도록 하려면 내장 타입 검사 단계를 비활성화할 수 있습니다.

비활성화하는 경우 빌드 또는 배포 과정의 일부로 타입 검사를 실행하고 있는지 반드시 확인하세요. 그렇지 않으면 매우 위험할 수 있습니다.

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

> **알아두면 좋아요** : 배포 전에 직접 TypeScript 오류를 확인하려면 `tsc --noEmit`을 실행할 수 있습니다. 이는 배포 전에 TypeScript 오류를 확인하고 싶은 CI/CD 파이프라인에 유용합니다.

### 사용자 지정 타입 선언[](https://nextjs.org/docs/pages/api-reference/config/typescript#custom-type-declarations)

사용자 지정 타입을 선언해야 할 때 `next-env.d.ts`를 수정하고 싶을 수 있지만, 이 파일은 자동으로 생성되므로 수정 사항이 덮어쓰여집니다. 대신 `new-types.d.ts`와 같은 새 파일을 만들고 `tsconfig.json`에 참조를 추가하세요:

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

## 버전 변경 사항[](https://nextjs.org/docs/pages/api-reference/config/typescript#version-changes)

Version| Changes  
---|---  
`v15.0.0`| TypeScript 프로젝트에 [`next.config.ts`](https://nextjs.org/docs/pages/api-reference/config/typescript#type-checking-nextjs-configuration-files) 지원이 추가되었습니다.  
`v13.2.0`| 정적으로 타입이 지정된 링크가 베타로 제공됩니다.  
`v12.0.0`| [SWC](https://nextjs.org/docs/architecture/nextjs-compiler)가 기본값으로 TypeScript와 TSX를 컴파일하여 빌드를 더 빠르게 합니다.  
`v10.2.1`| `tsconfig.json`에서 활성화했을 때 [증분 타입 검사](https://www.typescriptlang.org/tsconfig#incremental) 지원이 추가되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
