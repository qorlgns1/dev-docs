---
title: '함수: generateViewport'
description: '정적  객체나 동적  함수를 사용해 페이지의 초기 뷰포트를 사용자 지정할 수 있습니다.'
---

# 함수: generateViewport | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/generate-viewport

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)generateViewport

Copy page

# generateViewport

최종 업데이트 2026년 2월 20일

정적 `viewport` 객체나 동적 `generateViewport` 함수를 사용해 페이지의 초기 뷰포트를 사용자 지정할 수 있습니다.

> **알아두면 좋은 점** :
> 
>   * `viewport` 객체와 `generateViewport` 함수 export는 **Server Components에서만 지원**됩니다.
>   * 동일한 라우트 세그먼트에서 `viewport` 객체와 `generateViewport` 함수를 동시에 export할 수 없습니다.
>   * `metadata` export에서 마이그레이션하는 경우 [metadata-to-viewport-export codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#metadata-to-viewport-export)으로 변경 사항을 업데이트할 수 있습니다.
> 


## The `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object)

뷰포트 옵션을 정의하려면 `layout.jsx` 또는 `page.jsx` 파일에서 `viewport` 객체를 export하세요.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
     
    export default function Page() {}
[/code]

## `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function)

`generateViewport`는 하나 이상의 뷰포트 필드를 포함하는 [`Viewport` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields)를 반환해야 합니다.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    export function generateViewport({ params }) {
      return {
        themeColor: '...',
      }
    }
[/code]

TypeScript에서는 `generateViewport`가 정의된 위치에 따라 `params` 인수를 [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper) 또는 [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)로 타이핑할 수 있습니다.

> **알아두면 좋은 점** :
> 
>   * 뷰포트가 런타임 정보에 의존하지 않는다면 `generateViewport` 대신 정적 [`viewport` 객체](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#the-viewport-object)에 정의해야 합니다.
> 


## Viewport Fields[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-fields)

### `themeColor`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#themecolor)

[`theme-color`](https://developer.mozilla.org/docs/Web/HTML/Element/meta/name/theme-color)에 대해 더 알아보기.

**단순 테마 색상**

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
[/code]

<head> output
[code]
    <meta name="theme-color" content="black" />
[/code]

**미디어 속성 사용**

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: [
        { media: '(prefers-color-scheme: light)', color: 'cyan' },
        { media: '(prefers-color-scheme: dark)', color: 'black' },
      ],
    }
[/code]

<head> output
[code]
    <meta name="theme-color" media="(prefers-color-scheme: light)" content="cyan" />
    <meta name="theme-color" media="(prefers-color-scheme: dark)" content="black" />
[/code]

### `width`, `initialScale`, `maximumScale` 및 `userScalable`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#width-initialscale-maximumscale-and-userscalable)

> **알아두면 좋은 점** : `viewport` 메타 태그는 자동으로 설정되며 기본값으로 충분하므로 수동 구성은 대부분 불필요합니다. 다만 참고용으로 정보를 제공합니다.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      width: 'device-width',
      initialScale: 1,
      maximumScale: 1,
      userScalable: false,
      // Also supported but less commonly used
      // interactiveWidget: 'resizes-visual',
    }
[/code]

<head> output
[code]
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
    />
[/code]

### `colorScheme`[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#colorscheme)

[`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name#:~:text=color%2Dscheme%3A%20specifies,of%20the%20following%3A)에 대해 더 알아보기.

layout.tsx | page.tsx

JavaScriptTypeScript
[code]
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      colorScheme: 'dark',
    }
[/code]

<head> output
[code]
    <meta name="color-scheme" content="dark" />
[/code]

## With Cache Components[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-cache-components)

[Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 활성화하면 `generateViewport`는 다른 컴포넌트와 동일한 규칙을 따릅니다. 뷰포트가 런타임 데이터(`cookies()`, `headers()`, `params`, `searchParams`)에 접근하거나 캐시되지 않은 데이터 페치를 수행하면 요청 시점으로 연기됩니다.

메타데이터와 달리 뷰포트는 초기 페이지 로드 UI에 영향을 주므로 스트리밍할 수 없습니다. `generateViewport`가 요청 시점으로 연기되면 페이지는 해결될 때까지 블로킹됩니다.

뷰포트가 외부 데이터에는 의존하지만 런타임 데이터에는 의존하지 않는다면 `use cache`를 사용하세요:

app/layout.tsx
[code]
    export async function generateViewport() {
      'use cache'
      const { width, initialScale } = await db.query('viewport-size')
      return { width, initialScale }
    }
[/code]

뷰포트가 실제로 런타임 데이터를 필요로 한다면 문서 `<body>`를 Suspense 경계로 감싸 전체 라우트가 동적으로 처리되어야 함을 알리세요:

app/layout.tsx
[code]
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'
     
    export async function generateViewport() {
      const cookieJar = await cookies()
      return {
        themeColor: cookieJar.get('theme-color')?.value,
      }
    }
     
    export default function RootLayout({ children }) {
      return (
        <Suspense>
          <html>
            <body>{children}</body>
          </html>
        </Suspense>
      )
    }
[/code]

캐싱은 정적 셸 생성을 가능하게 하므로 선호됩니다. 문서 `body`를 Suspense로 감싸면 요청이 도착했을 때 즉시 보낼 정적 셸이나 콘텐츠가 없고, 모든 요청마다 준비될 때까지 전체 라우트가 블로킹됩니다.

> **알아두면 좋은 점** : [여러 개의 루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)을 사용해 완전히 동적인 뷰포트를 특정 라우트로 격리하면서 다른 라우트는 정적 셸을 생성하도록 유지할 수 있습니다.

## Types[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#types)

`Viewport` 타입을 사용하면 뷰포트 객체에 타입 안전성을 추가할 수 있습니다. IDE에서 [내장 TypeScript 플러그인](https://nextjs.org/docs/app/api-reference/config/typescript)을 사용하는 경우 타입을 수동으로 추가할 필요는 없지만 원한다면 명시적으로 추가할 수 있습니다.

### `viewport` object[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#viewport-object)
[code] 
    import type { Viewport } from 'next'
     
    export const viewport: Viewport = {
      themeColor: 'black',
    }
[/code]

### `generateViewport` function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#generateviewport-function-1)

#### Regular function[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#regular-function)
[code] 
    import type { Viewport } from 'next'
     
    export function generateViewport(): Viewport {
      return {
        themeColor: 'black',
      }
    }
[/code]

#### With segment props[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#with-segment-props)
[code] 
    import type { Viewport } from 'next'
     
    type Props = {
      params: Promise<{ id: string }>
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }
     
    export function generateViewport({ params, searchParams }: Props): Viewport {
      return {
        themeColor: 'black',
      }
    }
     
    export default function Page({ params, searchParams }: Props) {}
[/code]

#### JavaScript Projects[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#javascript-projects)

JavaScript 프로젝트에서는 JSDoc을 사용해 타입 안전성을 추가할 수 있습니다.
[code] 
    /** @type {import("next").Viewport} */
    export const viewport = {
      themeColor: 'black',
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#version-history)

Version| Changes  
---|---  
`v14.0.0`| `viewport` 및 `generateViewport` 도입.  
  
## Next Steps

모든 Metadata API 옵션을 확인하세요.

### [Metadata Files메타데이터 파일 컨벤션에 대한 API 문서.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)### [Cache ComponentsCache Components를 사용하고 정적·동적 렌더링의 장점을 결합하는 방법 알아보기.](https://nextjs.org/docs/app/getting-started/cache-components)### [cacheComponentsNext.js에서 cacheComponents 플래그를 활성화하는 방법 알아보기.](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)

Was this helpful?

supported.

Send
