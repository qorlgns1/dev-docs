---
title: '시작하기: 레이아웃과 페이지'
description: '원본 URL: https://nextjs.org/docs/app/getting-started/layouts-and-pages'
---

# 시작하기: 레이아웃과 페이지 | Next.js

원본 URL: https://nextjs.org/docs/app/getting-started/layouts-and-pages

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Layouts and Pages

# 레이아웃과 페이지

마지막 업데이트 2026년 2월 20일

Next.js는 **파일 시스템 기반 라우팅** 을 사용하므로 폴더와 파일로 라우트를 정의할 수 있습니다. 이 문서는 레이아웃과 페이지를 만드는 방법과 서로 연결하는 방법을 안내합니다.

## 페이지 만들기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-page)

**페이지** 는 특정 라우트에서 렌더링되는 UI입니다. 페이지를 만들려면 `app` 디렉터리 안에 [`page` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/page)을 추가하고 React 컴포넌트를 기본 내보내기(default export)하세요. 예를 들어 인덱스 페이지(`/`)를 만들려면 다음과 같이 합니다:

app/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1>Hello Next.js!</h1>
    }
[/code]

## 레이아웃 만들기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-layout)

레이아웃은 여러 페이지 간에 **공유되는** UI입니다. 네비게이션 시 레이아웃은 상태를 유지하고, 상호작용성을 잃지 않으며, 다시 렌더링되지 않습니다.

[`layout` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/layout)에서 React 컴포넌트를 기본 내보내면 레이아웃을 정의할 수 있습니다. 해당 컴포넌트는 페이지나 다른 [레이아웃](https://nextjs.org/docs/app/getting-started/layouts-and-pages#nesting-layouts)이 될 수 있는 `children` prop을 받아야 합니다.

예를 들어 인덱스 페이지를 자식으로 받는 레이아웃을 만들려면 `app` 디렉터리에 `layout` 파일을 추가합니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function DashboardLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>
            {/* Layout UI */}
            {/* Place children where you want to render a page or nested layout */}
            <main>{children}</main>
          </body>
        </html>
      )
    }
[/code]

위 레이아웃은 `app` 디렉터리의 루트에 정의되어 있기 때문에 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)이라고 합니다. 루트 레이아웃은 **필수** 이며 `html` 및 `body` 태그를 포함해야 합니다.

## 중첩 라우트 만들기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-nested-route)

중첩 라우트는 여러 URL 세그먼트로 구성된 라우트입니다. 예를 들어 `/blog/[slug]` 라우트는 다음 세 세그먼트로 구성됩니다:

  * `/` (루트 세그먼트)
  * `blog` (세그먼트)
  * `[slug]` (리프 세그먼트)

Next.js에서는:

  * **폴더** 를 사용해 URL 세그먼트에 매핑되는 라우트 세그먼트를 정의합니다.
  * `page`나 `layout`처럼 **파일** 을 사용해 해당 세그먼트에 표시되는 UI를 만듭니다.

중첩 라우트를 만들려면 폴더를 서로 중첩하면 됩니다. 예를 들어 `/blog` 라우트를 추가하려면 `app` 디렉터리에 `blog`라는 폴더를 만듭니다. 그런 다음 `/blog`를 공개하려면 `page.tsx` 파일을 추가합니다:

app/blog/page.tsx

JavaScriptTypeScript
[code]
    // Dummy imports
    import { getPosts } from '@/lib/posts'
    import { Post } from '@/ui/post'

    export default async function Page() {
      const posts = await getPosts()

      return (
        <ul>
          {posts.map((post) => (
            <Post key={post.id} post={post} />
          ))}
        </ul>
      )
    }
[/code]

폴더를 계속 중첩해 중첩 라우트를 만들 수 있습니다. 예를 들어 특정 블로그 게시물용 라우트를 만들려면 `blog` 안에 새로운 `[slug]` 폴더를 만들고 `page` 파일을 추가합니다:

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    function generateStaticParams() {}

    export default function Page() {
      return <h1>Hello, Blog Post Page!</h1>
    }
[/code]

폴더 이름을 대괄호(예: `[slug]`)로 감싸면 [동적 라우트 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)가 생성되어 데이터로부터 여러 페이지를 만들 수 있습니다. 예: 블로그 게시물, 제품 페이지 등.

## 레이아웃 중첩하기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#nesting-layouts)

기본적으로 폴더 계층의 레이아웃은 중첩되어 `children` prop을 통해 하위 레이아웃을 감쌉니다. 특정 라우트 세그먼트(폴더)에 `layout`을 추가해 레이아웃을 중첩할 수 있습니다.

예를 들어 `/blog` 라우트의 레이아웃을 만들려면 `blog` 폴더 안에 새로운 `layout` 파일을 추가합니다.

app/blog/layout.tsx

JavaScriptTypeScript
[code]
    export default function BlogLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return <section>{children}</section>
    }
[/code]

위 두 레이아웃을 결합하면 루트 레이아웃(`app/layout.js`)이 블로그 레이아웃(`app/blog/layout.js`)을 감싸고, 블로그(`app/blog/page.js`)와 블로그 게시물 페이지(`app/blog/[slug]/page.js`)를 순서대로 감싸게 됩니다.

## 동적 세그먼트 만들기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-dynamic-segment)

[동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 사용하면 데이터로부터 생성되는 라우트를 만들 수 있습니다. 예를 들어 각 블로그 게시물마다 라우트를 수동으로 만드는 대신, 동적 세그먼트를 만들어 게시물 데이터에 기반해 라우트를 생성할 수 있습니다.

동적 세그먼트를 만들려면 세그먼트(폴더) 이름을 대괄호로 감싸세요: `[segmentName]`. 예를 들어 `app/blog/[slug]/page.tsx` 라우트에서 `[slug]`가 동적 세그먼트입니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    export default async function BlogPostPage({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      const post = await getPost(slug)

      return (
        <div>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
        </div>
      )
    }
[/code]

[동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)와 [`params`](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional) props에 대해 더 알아보세요.

동적 세그먼트 안의 중첩 [레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#params-optional) 역시 `params` props에 접근할 수 있습니다.

## 검색 파라미터로 렌더링하기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#rendering-with-search-params)

서버 컴포넌트 **페이지** 에서 [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop을 사용해 검색 파라미터에 접근할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      searchParams,
    }: {
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const filters = (await searchParams).filters
    }
[/code]

`searchParams`를 사용하면 검색 파라미터를 읽기 위해 들어오는 요청이 필요하므로 페이지가 [**동적 렌더링**](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)에 참여하게 됩니다.

클라이언트 컴포넌트는 [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) 훅을 사용해 검색 파라미터를 읽을 수 있습니다.

[정적 렌더링](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering) 및 [동적 렌더링](https://nextjs.org/docs/app/api-reference/functions/use-search-params#dynamic-rendering) 라우트에서의 `useSearchParams` 사용법을 알아보세요.

### 언제 무엇을 사용할까[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#what-to-use-and-when)

  * 검색 파라미터로 **페이지용 데이터를 로드** 해야 할 때는 `searchParams` prop을 사용하세요(예: 페이지네이션, 데이터베이스 필터링).
  * 검색 파라미터가 **클라이언트에서만** 사용될 때는 `useSearchParams`를 사용하세요(예: props로 이미 로드한 목록 필터링).
  * 작은 최적화로, **콜백이나 이벤트 핸들러** 안에서는 `new URLSearchParams(window.location.search)`를 사용해 리렌더링 없이 검색 파라미터를 읽을 수 있습니다.

## 페이지 간 링크 연결하기[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#linking-between-pages)

[`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)를 사용해 라우트 간을 이동할 수 있습니다. `<Link>`는 HTML `<a>` 태그를 확장하여 [프리패칭](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)과 [클라이언트 측 네비게이션](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 제공하는 Next.js 내장 컴포넌트입니다.

예를 들어 블로그 게시물 목록을 생성하려면 `next/link`에서 `<Link>`를 가져오고 `href` prop을 전달합니다:

app/ui/post.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'

    export default async function Post({ post }) {
      const posts = await getPosts()

      return (
        <ul>
          {posts.map((post) => (
            <li key={post.slug}>
              <Link href={`/blog/${post.slug}`}>{post.title}</Link>
            </li>
          ))}
        </ul>
      )
    }
[/code]

> **알아두면 좋아요** : `<Link>`는 Next.js에서 라우트 간 이동의 기본 방식입니다. 보다 고급 네비게이션이 필요하면 [`useRouter` 훅](https://nextjs.org/docs/app/api-reference/functions/use-router)을 사용할 수 있습니다.

## 라우트 Props 헬퍼[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#route-props-helpers)

Next.js는 라우트 구조로부터 `params`와 명명된 슬롯을 추론하는 유틸리티 타입을 제공합니다:

  * [**PageProps**](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper): `page` 컴포넌트용 props로 `params`와 `searchParams`를 포함합니다.
  * [**LayoutProps**](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper): `layout` 컴포넌트용 props로 `children`과 `@analytics` 같은 명명된 슬롯을 포함합니다.

이 헬퍼는 전역에서 사용 가능하며 `next dev`, `next build`, 또는 [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)을 실행할 때 생성됩니다.

app/blog/[slug]/page.tsx
[code]
    export default async function Page(props: PageProps<'/blog/[slug]'>) {
      const { slug } = await props.params
      return <h1>Blog post: {slug}</h1>
    }
[/code]

app/dashboard/layout.tsx
[code]
    export default function Layout(props: LayoutProps<'/dashboard'>) {
      return (
        <section>
          {props.children}
          {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
          {/* {props.analytics} */}
        </section>
      )
    }
[/code]

> **알아두면 좋아요**
>
>   * 정적 라우트는 `params`가 `{}`로 해석됩니다.
>   * `PageProps`, `LayoutProps`는 전역 헬퍼이므로 import가 필요 없습니다.
>   * 타입은 `next dev`, `next build`, `next typegen` 실행 중 생성됩니다.
>

## API Reference

API Reference를 읽어 이 페이지에서 언급된 기능을 더 알아보세요.

- [링크 및 탐색](https://nextjs.org/docs/app/getting-started/linking-and-navigating)
  - 링크 및 네비게이션내장 네비게이션 최적화(프리패칭, 프리렌더링, 클라이언트 사이드 네비게이션 등) 작동 방식과 동적 라우트·느린 네트워크에 대한 최적화 방법을 알아보세요.

- [layout.js](https://nextjs.org/docs/app/api-reference/file-conventions/layout)
  - layout.js 파일에 대한 API 레퍼런스입니다.

- [page.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)
  - page.js 파일에 대한 API 레퍼런스입니다.

- [링크 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)
  - Link 컴포넌트내장 `next/link` 컴포넌트로 빠른 클라이언트 사이드 네비게이션을 구현하세요.

- [동적 세그먼트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
  - 동적 데이터로부터 라우트 세그먼트를 프로그래밍 방식으로 생성할 수 있는 Dynamic Route Segments를 활용하세요.
