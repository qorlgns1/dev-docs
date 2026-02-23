---
title: '업그레이드: Codemods'
description: '마지막 업데이트 2026년 2월 20일'
---

# 업그레이드: Codemods | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/upgrading/codemods

[가이드](https://nextjs.org/docs/pages/guides)[업그레이드](https://nextjs.org/docs/pages/guides/upgrading)Codemods

페이지 복사

# Codemods

마지막 업데이트 2026년 2월 20일

Codemod은 코드베이스에서 프로그램적으로 실행되는 변환으로, 모든 파일을 수동으로 확인하지 않아도 대규모 변경을 자동으로 적용할 수 있습니다.

Next.js는 API가 업데이트되거나 사용 중단될 때 Next.js 코드베이스 업그레이드를 돕기 위한 Codemod 변환을 제공합니다.

## 사용법[](https://nextjs.org/docs/pages/guides/upgrading/codemods#usage)

터미널에서 프로젝트 폴더로 이동(`cd`)한 다음 다음을 실행합니다:

터미널
[code]
    npx @next/codemod <transform> <path>
[/code]

`<transform>`과 `<path>`를 알맞은 값으로 바꿉니다.

  * `transform` - 변환 이름
  * `path` - 변환할 파일 또는 디렉터리
  * `--dry` 실제 코드를 수정하지 않는 드라이런 수행
  * `--print` 비교용으로 변경된 출력 내용을 표시



## 업그레이드[](https://nextjs.org/docs/pages/guides/upgrading/codemods#upgrade)

Next.js, React, React DOM을 업데이트하고 codemod를 자동으로 실행해 Next.js 애플리케이션을 업그레이드합니다.

터미널
[code]
    npx @next/codemod upgrade [revision]
[/code]

### 옵션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#options)

  * `revision`(선택 사항): 업그레이드 유형(`patch`, `minor`, `major`), NPM dist 태그(예: `latest`, `canary`, `rc`), 또는 정확한 버전(예: `15.0.0`)을 지정합니다. 안정 버전의 기본값은 `minor`입니다.
  * `--verbose`: 업그레이드 과정에서 더 자세한 출력을 표시합니다.



예:

터미널
[code]
    # 최신 패치로 업그레이드 (예: 16.0.7 -> 16.0.8)
    npx @next/codemod upgrade patch
     
    # 최신 마이너로 업그레이드 (예: 15.3.7 -> 15.4.8). 기본값입니다.
    npx @next/codemod upgrade minor
     
    # 최신 메이저로 업그레이드 (예: 15.5.7 -> 16.0.7)
    npx @next/codemod upgrade major
     
    # 특정 버전으로 업그레이드
    npx @next/codemod upgrade 16
     
    # 카나리 릴리스로 업그레이드
    npx @next/codemod upgrade canary
[/code]

> **알아두면 좋아요** :
> 
>   * 대상 버전이 현재 버전과 같거나 낮으면 명령은 아무 변경 없이 종료됩니다.
>   * 업그레이드 중 Next.js codemod 적용 여부나 React 업그레이드 시 React 19 codemod 실행 여부를 묻는 프롬프트가 나타날 수 있습니다.
> 


## Codemods[](https://nextjs.org/docs/pages/guides/upgrading/codemods#codemods)

### 16.0[](https://nextjs.org/docs/pages/guides/upgrading/codemods#160)

#### App Router 페이지와 레이아웃에서 `experimental_ppr` 라우트 세그먼트 구성 제거[](https://nextjs.org/docs/pages/guides/upgrading/codemods#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts)

##### `remove-experimental-ppr`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#remove-experimental-ppr)

터미널
[code]
    npx @next/codemod@latest remove-experimental-ppr .
[/code]

이 codemod는 App Router 페이지와 레이아웃에서 `experimental_ppr` 라우트 세그먼트 구성을 제거합니다.

app/page.tsx
[code]
    - export const experimental_ppr = true;
[/code]

#### 안정화된 API에서 `unstable_` 접두사 제거[](https://nextjs.org/docs/pages/guides/upgrading/codemods#remove-unstable_-prefix-from-stabilized-api)

##### `remove-unstable-prefix`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#remove-unstable-prefix)

터미널
[code]
    npx @next/codemod@latest remove-unstable-prefix .
[/code]

이 codemod는 안정화된 API에서 `unstable_` 접두사를 제거합니다.

예:
[code] 
    import { unstable_cacheTag as cacheTag } from 'next/cache'
     
    cacheTag()
[/code]

다음으로 변환됩니다:
[code] 
    import { cacheTag } from 'next/cache'
     
    cacheTag()
[/code]

#### 사용 중단된 `middleware` 규약에서 `proxy`로 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-from-deprecated-middleware-convention-to-proxy)

##### `middleware-to-proxy`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#middleware-to-proxy)

터미널
[code]
    npx @next/codemod@latest middleware-to-proxy .
[/code]

이 codemod는 사용 중단된 `middleware` 규약을 사용하는 프로젝트를 `proxy` 규약으로 마이그레이션합니다. 수행 작업:

  * `middleware.<extension>`을 `proxy.<extension>`으로 이름 변경(예: `middleware.ts` → `proxy.ts`)
  * 이름이 지정된 export `middleware`를 `proxy`로 변경
  * Next.js 구성 속성 `experimental.middlewarePrefetch`를 `experimental.proxyPrefetch`로 변경
  * Next.js 구성 속성 `experimental.middlewareClientMaxBodySize`를 `experimental.proxyClientMaxBodySize`로 변경
  * Next.js 구성 속성 `experimental.externalMiddlewareRewritesResolve`를 `experimental.externalProxyRewritesResolve`로 변경
  * Next.js 구성 속성 `skipMiddlewareUrlNormalize`를 `skipProxyUrlNormalize`로 변경



예:

middleware.ts
[code]
    import { NextResponse } from 'next/server'
     
    export function middleware() {
      return NextResponse.next()
    }
[/code]

다음으로 변환됩니다:

proxy.ts
[code]
    import { NextResponse } from 'next/server'
     
    export function proxy() {
      return NextResponse.next()
    }
[/code]

#### `next lint`에서 ESLint CLI로 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-from-next-lint-to-eslint-cli)

##### `next-lint-to-eslint-cli`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-lint-to-eslint-cli)

터미널
[code]
    npx @next/codemod@canary next-lint-to-eslint-cli .
[/code]

이 codemod는 `next lint`를 사용하는 프로젝트를 로컬 ESLint 설정과 함께 ESLint CLI를 사용하도록 마이그레이션합니다. 수행 작업:

  * Next.js 권장 구성이 포함된 `eslint.config.mjs` 파일 생성
  * `package.json` 스크립트를 `next lint` 대신 `eslint .`으로 업데이트
  * 필요한 ESLint 의존성을 `package.json`에 추가
  * 기존 ESLint 구성이 있으면 그대로 유지



예:

package.json
[code]
    {
      "scripts": {
        "lint": "next lint"
      }
    }
[/code]

다음으로 변경됩니다:

package.json
[code]
    {
      "scripts": {
        "lint": "eslint ."
      }
    }
[/code]

그리고 다음 파일을 생성합니다:

eslint.config.mjs
[code]
    import { dirname } from 'path'
    import { fileURLToPath } from 'url'
    import { FlatCompat } from '@eslint/eslintrc'
     
    const __filename = fileURLToPath(import.meta.url)
    const __dirname = dirname(__filename)
     
    const compat = new FlatCompat({
      baseDirectory: __dirname,
    })
     
    const eslintConfig = [
      ...compat.extends('next/core-web-vitals', 'next/typescript'),
      {
        ignores: [
          'node_modules/**',
          '.next/**',
          'out/**',
          'build/**',
          'next-env.d.ts',
        ],
      },
    ]
     
    export default eslintConfig
[/code]

### 15.0[](https://nextjs.org/docs/pages/guides/upgrading/codemods#150)

#### App Router 라우트 세그먼트 구성 `runtime` 값을 `experimental-edge`에서 `edge`로 변환[](https://nextjs.org/docs/pages/guides/upgrading/codemods#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge)

##### `app-dir-runtime-config-experimental-edge`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#app-dir-runtime-config-experimental-edge)

> **참고** : 이 codemod는 App Router 전용입니다.

터미널
[code]
    npx @next/codemod@latest app-dir-runtime-config-experimental-edge .
[/code]

이 codemod는 [Route Segment Config `runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) 값 `experimental-edge`를 `edge`로 변환합니다.

예:
[code] 
    export const runtime = 'experimental-edge'
[/code]

다음으로 변환됩니다:
[code] 
    export const runtime = 'edge'
[/code]

#### 비동기 Dynamic API로 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-to-async-dynamic-apis)

기존에 동적 렌더링을 선택해 동기 접근을 지원하던 API가 이제 비동기 방식이 되었습니다. 이 파괴적 변경 사항에 대한 자세한 내용은 [업그레이드 가이드](https://nextjs.org/docs/app/guides/upgrading/version-15)에서 확인하세요.

##### `next-async-request-api`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-async-request-api)

터미널
[code]
    npx @next/codemod@latest next-async-request-api .
[/code]

이 codemod는 이제 비동기로 전환된 동적 API(`next/headers`의 `cookies()`, `headers()`, `draftMode()`)를 적절하게 `await`하거나 필요 시 `React.use()`로 래핑합니다. 자동 마이그레이션이 불가능한 경우 TypeScript 파일이면 타입 캐스트를, 그 외에는 수동 검토 및 업데이트가 필요하다는 주석을 추가합니다.

예:
[code] 
    import { cookies, headers } from 'next/headers'
    const token = cookies().get('token')
     
    function useToken() {
      const token = cookies().get('token')
      return token
    }
     
    export default function Page() {
      const name = cookies().get('name')
    }
     
    function getHeader() {
      return headers().get('x-foo')
    }
[/code]

다음으로 변환됩니다:
[code] 
    import { use } from 'react'
    import {
      cookies,
      headers,
      type UnsafeUnwrappedCookies,
      type UnsafeUnwrappedHeaders,
    } from 'next/headers'
    const token = (cookies() as unknown as UnsafeUnwrappedCookies).get('token')
     
    function useToken() {
      const token = use(cookies()).get('token')
      return token
    }
     
    export default async function Page() {
      const name = (await cookies()).get('name')
    }
     
    function getHeader() {
      return (headers() as unknown as UnsafeUnwrappedHeaders).get('x-foo')
    }
[/code]

`page.js`, `layout.js`, `route.js`, `default.js`와 같은 페이지/라우트 항목 또는 `generateMetadata` / `generateViewport` API에서 `params`나 `searchParams` props에 대한 프로퍼티 접근을 감지하면 동기 호출부를 비동기 함수로 변환하고 프로퍼티 접근을 `await`하려고 시도합니다. 클라이언트 컴포넌트처럼 비동기로 만들 수 없는 경우 `React.use`를 사용해 프로미스를 언래핑합니다.

예:
[code] 
    // page.tsx
    export default function Page({
      params,
      searchParams,
    }: {
      params: { slug: string }
      searchParams: { [key: string]: string | string[] | undefined }
    }) {
      const { value } = searchParams
      if (value === 'foo') {
        // ...
      }
    }
     
    export function generateMetadata({ params }: { params: { slug: string } }) {
      const { slug } = params
      return {
        title: `My Page - ${slug}`,
      }
    }
[/code]

다음으로 변환됩니다:
[code] 
    // page.tsx
    export default async function Page(props: {
      params: Promise<{ slug: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const searchParams = await props.searchParams
      const { value } = searchParams
      if (value === 'foo') {
        // ...
      }
    }
     
    export async function generateMetadata(props: {
      params: Promise<{ slug: string }>
    }) {
      const params = await props.params
      const { slug } = params
      return {
        title: `My Page - ${slug}`,
      }
    }
[/code]

> **알아두면 좋아요:** 이 codemod가 수동 개입이 필요할 가능성을 감지했지만 정확한 수정 방법을 결정할 수 없는 경우, 코드에 주석이나 타입 캐스트를 추가해 수동 업데이트가 필요함을 알립니다. 이 주석에는 **@next/codemod** 접두사가 붙고, 타입 캐스트에는 `UnsafeUnwrapped` 접두사가 붙습니다. 이러한 주석을 명시적으로 제거하기 전까지는 빌드가 실패합니다. [자세히 보기](https://nextjs.org/docs/messages/sync-dynamic-apis).

#### `NextRequest`의 `geo` 및 `ip` 프로퍼티를 `@vercel/functions`로 대체[](https://nextjs.org/docs/pages/guides/upgrading/codemods#replace-geo-and-ip-properties-of-nextrequest-with-vercelfunctions)

##### `next-request-geo-ip`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-request-geo-ip)

터미널
[code]
    npx @next/codemod@latest next-request-geo-ip .
[/code]

이 코드를 사용하면 `@vercel/functions`가 설치되고 `NextRequest`의 `geo` 및 `ip` 속성이 해당 `@vercel/functions` 기능으로 변환됩니다.

예시:
[code] 
    import type { NextRequest } from 'next/server'
     
    export function GET(req: NextRequest) {
      const { geo, ip } = req
    }
[/code]

다음과 같이 변환됩니다:
[code] 
    import type { NextRequest } from 'next/server'
    import { geolocation, ipAddress } from '@vercel/functions'
     
    export function GET(req: NextRequest) {
      const geo = geolocation(req)
      const ip = ipAddress(req)
    }
[/code]

### 14.0[](https://nextjs.org/docs/pages/guides/upgrading/codemods#140)

#### `ImageResponse` 가져오기 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-imageresponse-imports)

##### `next-og-import`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-og-import)

터미널
[code]
    npx @next/codemod@latest next-og-import .
[/code]

이 코드는 [동적 OG 이미지 생성](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-open-graph-images) 사용을 위해 `next/server`에서 `next/og`로 가져오기를 이동하고 변환합니다.

예시:
[code] 
    import { ImageResponse } from 'next/server'
[/code]

다음과 같이 변환됩니다:
[code] 
    import { ImageResponse } from 'next/og'
[/code]

#### `viewport` 내보내기 사용[](https://nextjs.org/docs/pages/guides/upgrading/codemods#use-viewport-export)

##### `metadata-to-viewport-export`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#metadata-to-viewport-export)

터미널
[code]
    npx @next/codemod@latest metadata-to-viewport-export .
[/code]

이 코드는 특정 뷰포트 메타데이터를 `viewport` 내보내기로 마이그레이션합니다.

예시:
[code] 
    export const metadata = {
      title: 'My App',
      themeColor: 'dark',
      viewport: {
        width: 1,
      },
    }
[/code]

다음과 같이 변환됩니다:
[code] 
    export const metadata = {
      title: 'My App',
    }
     
    export const viewport = {
      width: 1,
      themeColor: 'dark',
    }
[/code]

### 13.2[](https://nextjs.org/docs/pages/guides/upgrading/codemods#132)

#### 기본 제공 글꼴 사용[](https://nextjs.org/docs/pages/guides/upgrading/codemods#use-built-in-font)

##### `built-in-next-font`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#built-in-next-font)

터미널
[code]
    npx @next/codemod@latest built-in-next-font .
[/code]

이 코드는 `@next/font` 패키지를 제거하고 `@next/font` 가져오기를 기본 제공 `next/font`로 변환합니다.

예시:
[code] 
    import { Inter } from '@next/font/google'
[/code]

다음과 같이 변환됩니다:
[code] 
    import { Inter } from 'next/font/google'
[/code]

### 13.0[](https://nextjs.org/docs/pages/guides/upgrading/codemods#130)

#### Next Image 가져오기 이름 변경[](https://nextjs.org/docs/pages/guides/upgrading/codemods#rename-next-image-imports)

##### `next-image-to-legacy-image`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-to-legacy-image)

터미널
[code]
    npx @next/codemod@latest next-image-to-legacy-image .
[/code]

기존 Next.js 10, 11, 12 애플리케이션의 `next/image` 가져오기를 Next.js 13의 `next/legacy/image`로 안전하게 이름을 변경합니다. 또한 `next/future/image`를 `next/image`로 이름을 바꿉니다.

예시:

pages/index.js
[code]
    import Image1 from 'next/image'
    import Image2 from 'next/future/image'
     
    export default function Home() {
      return (
        <div>
          <Image1 src="/test.jpg" width="200" height="300" />
          <Image2 src="/test.png" width="500" height="400" />
        </div>
      )
    }
[/code]

다음과 같이 변환됩니다:

pages/index.js
[code]
    // 'next/image' becomes 'next/legacy/image'
    import Image1 from 'next/legacy/image'
    // 'next/future/image' becomes 'next/image'
    import Image2 from 'next/image'
     
    export default function Home() {
      return (
        <div>
          <Image1 src="/test.jpg" width="200" height="300" />
          <Image2 src="/test.png" width="500" height="400" />
        </div>
      )
    }
[/code]

#### 새로운 Image 컴포넌트로 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-to-the-new-image-component)

##### `next-image-experimental`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-experimental)

터미널
[code]
    npx @next/codemod@latest next-image-experimental .
[/code]

`next/legacy/image`에서 새로운 `next/image`로 위험도가 높은 마이그레이션을 수행하며, 인라인 스타일을 추가하고 사용되지 않는 props를 제거합니다.

  * `layout` prop을 제거하고 `style`을 추가합니다.
  * `objectFit` prop을 제거하고 `style`을 추가합니다.
  * `objectPosition` prop을 제거하고 `style`을 추가합니다.
  * `lazyBoundary` prop을 제거합니다.
  * `lazyRoot` prop을 제거합니다.



#### Link 컴포넌트에서 `<a>` 태그 제거[](https://nextjs.org/docs/pages/guides/upgrading/codemods#remove-a-tags-from-link-components)

##### `new-link`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#new-link)

터미널
[code]
    npx @next/codemod@latest new-link .
[/code]

[Link 컴포넌트](https://nextjs.org/docs/pages/api-reference/components/link) 안의 `<a>` 태그를 제거합니다.

예시:
[code] 
    <Link href="/about">
      <a>About</a>
    </Link>
    // transforms into
    <Link href="/about">
      About
    </Link>
     
    <Link href="/about">
      <a onClick={() => console.log('clicked')}>About</a>
    </Link>
    // transforms into
    <Link href="/about" onClick={() => console.log('clicked')}>
      About
    </Link>
[/code]

### 11[](https://nextjs.org/docs/pages/guides/upgrading/codemods#11)

#### CRA에서 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/codemods#migrate-from-cra)

##### `cra-to-next`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#cra-to-next)

터미널
[code]
    npx @next/codemod cra-to-next
[/code]

Create React App 프로젝트를 Next.js로 마이그레이션하면서 Pages Router와 필요한 구성을 생성해 동작을 맞춥니다. 초기에는 SSR 중 `window` 사용으로 인한 호환성 깨짐을 막기 위해 클라이언트 사이드 전용 렌더링을 활용하며, 이후 Next.js 고유 기능을 점진적으로 도입할 수 있습니다.

이 변환에 대한 피드백은 [이 토론](https://github.com/vercel/next.js/discussions/25858)에 공유해 주세요.

### 10[](https://nextjs.org/docs/pages/guides/upgrading/codemods#10)

#### React 가져오기 추가[](https://nextjs.org/docs/pages/guides/upgrading/codemods#add-react-imports)

##### `add-missing-react-import`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#add-missing-react-import)

터미널
[code]
    npx @next/codemod add-missing-react-import
[/code]

`React`를 가져오지 않는 파일에 가져오기를 추가하여 새로운 [React JSX 변환](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)이 동작하도록 합니다.

예시:

my-component.js
[code]
    export default class Home extends React.Component {
      render() {
        return <div>Hello World</div>
      }
    }
[/code]

다음과 같이 변환됩니다:

my-component.js
[code]
    import React from 'react'
    export default class Home extends React.Component {
      render() {
        return <div>Hello World</div>
      }
    }
[/code]

### 9[](https://nextjs.org/docs/pages/guides/upgrading/codemods#9)

#### 익명 컴포넌트를 명명된 컴포넌트로 변환[](https://nextjs.org/docs/pages/guides/upgrading/codemods#transform-anonymous-components-into-named-components)

##### `name-default-component`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#name-default-component)

터미널
[code]
    npx @next/codemod name-default-component
[/code]

**버전 9 이상.**

익명 컴포넌트를 명명된 컴포넌트로 변환하여 [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh)와 함께 동작하도록 합니다.

예시:

my-component.js
[code]
    export default function () {
      return <div>Hello World</div>
    }
[/code]

다음과 같이 변환됩니다:

my-component.js
[code]
    export default function MyComponent() {
      return <div>Hello World</div>
    }
[/code]

컴포넌트 이름은 파일 이름을 기반으로 카멜 케이스로 지정되며, 화살표 함수에도 동일하게 작동합니다.

### 8[](https://nextjs.org/docs/pages/guides/upgrading/codemods#8)

> **참고**: 기본 제공 AMP 지원과 이 코드는 Next.js 16에서 제거되었습니다.

#### AMP HOC를 페이지 구성으로 변환[](https://nextjs.org/docs/pages/guides/upgrading/codemods#transform-amp-hoc-into-page-config)

##### `withamp-to-config`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#withamp-to-config)

터미널
[code]
    npx @next/codemod withamp-to-config
[/code]

`withAmp` HOC를 Next.js 9 페이지 구성으로 변환합니다.

예시:
[code] 
    // Before
    import { withAmp } from 'next/amp'
     
    function Home() {
      return <h1>My AMP Page</h1>
    }
     
    export default withAmp(Home)
[/code]
[code] 
    // After
    export default function Home() {
      return <h1>My AMP Page</h1>
    }
     
    export const config = {
      amp: true,
    }
[/code]

### 6[](https://nextjs.org/docs/pages/guides/upgrading/codemods#6)

#### `withRouter` 사용[](https://nextjs.org/docs/pages/guides/upgrading/codemods#use-withrouter)

##### `url-to-withrouter`[](https://nextjs.org/docs/pages/guides/upgrading/codemods#url-to-withrouter)

터미널
[code]
    npx @next/codemod url-to-withrouter
[/code]

더 이상 사용되지 않는 최상위 페이지의 자동 주입 `url` 속성을 `withRouter`와 그가 주입하는 `router` 속성으로 변환합니다. 자세한 내용: <https://nextjs.org/docs/messages/url-deprecated>

예시:

변환 전
[code]
    import React from 'react'
    export default class extends React.Component {
      render() {
        const { pathname } = this.props.url
        return <div>Current pathname: {pathname}</div>
      }
    }
[/code]

변환 후
[code]
    import React from 'react'
    import { withRouter } from 'next/router'
    export default withRouter(
      class extends React.Component {
        render() {
          const { pathname } = this.props.router
          return <div>Current pathname: {pathname}</div>
        }
      }
    )
[/code]

이 사례를 포함한 모든 변환(및 테스트)은 [`__testfixtures__` 디렉터리](https://github.com/vercel/next.js/tree/canary/packages/next-codemod/transforms/__testfixtures__/url-to-withrouter)에 있습니다.

도움이 되었나요?

지원됨.

보내기
