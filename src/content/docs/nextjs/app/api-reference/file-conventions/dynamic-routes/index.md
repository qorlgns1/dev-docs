---
title: '파일 시스템 규칙: 동적 세그먼트'
description: '요청 시점에 채워지거나 빌드 시 사전 렌더링되는 동적 데이터를 이용해 라우트를 만들고 싶은데 정확한 라우트 세그먼트 이름을 미리 알 수 없다면, 동적 세그먼트를 사용할 수 있습니다.'
---

# 파일 시스템 규칙: 동적 세그먼트 | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)Dynamic Segments

# 동적 라우트 세그먼트

마지막 업데이트 2026년 2월 20일

요청 시점에 채워지거나 빌드 시 사전 렌더링되는 동적 데이터를 이용해 라우트를 만들고 싶은데 정확한 라우트 세그먼트 이름을 미리 알 수 없다면, 동적 세그먼트를 사용할 수 있습니다.

## 규칙[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#convention)

폴더 이름을 대괄호로 감싸면 동적 세그먼트를 만들 수 있습니다: `[folderName]`. 예를 들어 블로그는 `app/blog/[slug]/page.js` 라우트를 포함할 수 있으며, 여기서 `[slug]`가 블로그 게시물을 위한 동적 세그먼트입니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
```
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      return <div>My Post: {slug}</div>
    }
```

동적 세그먼트는 [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) 함수에 `params` prop으로 전달됩니다.

경로| 예시 URL| `params`
---|---|---
`app/blog/[slug]/page.js`| `/blog/a`| `{ slug: 'a' }`
`app/blog/[slug]/page.js`| `/blog/b`| `{ slug: 'b' }`
`app/blog/[slug]/page.js`| `/blog/c`| `{ slug: 'c' }`

### 클라이언트 컴포넌트에서[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#in-client-components)

클라이언트 컴포넌트 **page** 의 props에서 온 동적 세그먼트는 [`use`](https://react.dev/reference/react/use) API를 사용해 접근할 수 있습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
```
    'use client'
    import { use } from 'react'

    export default function BlogPostPage({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = use(params)

      return (
        <div>
          <p>{slug}</p>
        </div>
      )
    }
```

또는 클라이언트 컴포넌트는 [`useParams`](https://nextjs.org/docs/app/api-reference/functions/use-params) 훅을 사용해 클라이언트 컴포넌트 트리 어디서든 `params`에 접근할 수 있습니다.

### 캐치올 세그먼트[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)

대괄호 안에 생략 부호를 추가해 `[...folderName]` 형태로 만들면 이후 모든 세그먼트를 **캐치올** 방식으로 확장할 수 있습니다.

예를 들어 `app/shop/[...slug]/page.js`는 `/shop/clothes`뿐만 아니라 `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts` 등도 매칭합니다.

경로| 예시 URL| `params`
---|---|---
`app/shop/[...slug]/page.js`| `/shop/a`| `{ slug: ['a'] }`
`app/shop/[...slug]/page.js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`
`app/shop/[...slug]/page.js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`

### 선택적 캐치올 세그먼트[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments)

대괄호를 이중으로 감싸 `[[...folderName]]` 형태로 만들면 캐치올 세그먼트를 **선택적**으로 만들 수 있습니다.

예를 들어 `app/shop/[[...slug]]/page.js`는 `/shop`뿐 아니라 `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`도 매칭합니다.

**캐치올**과 **선택적 캐치올** 세그먼트의 차이는 선택적 세그먼트의 경우 파라미터가 없는 라우트(`/shop`)도 함께 매칭된다는 점입니다.

경로| 예시 URL| `params`
---|---|---
`app/shop/[[...slug]]/page.js`| `/shop`| `{ slug: undefined }`
`app/shop/[[...slug]]/page.js`| `/shop/a`| `{ slug: ['a'] }`
`app/shop/[[...slug]]/page.js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`
`app/shop/[[...slug]]/page.js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`

### TypeScript[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#typescript)

TypeScript를 사용할 때는 설정된 라우트 세그먼트에 따라 `params` 타입을 추가할 수 있습니다. `page`, `layout`, `route` 각각에 대해 [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper), [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper), [`RouteContext<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)를 사용해 `params`를 타이핑하세요.

라우트 `params` 값은 런타임까지 알 수 없으므로 `string`, `string[]`, `undefined`(선택적 캐치올 세그먼트)로 타입이 지정됩니다. 사용자는 주소창에 어떤 URL이든 입력할 수 있고, 이러한 폭넓은 타입을 통해 애플리케이션 코드가 가능한 모든 경우를 처리하도록 돕습니다.

경로| `params` 타입 정의
---|---
`app/blog/[slug]/page.js`| `{ slug: string }`
`app/shop/[...slug]/page.js`| `{ slug: string[] }`
`app/shop/[[...slug]]/page.js`| `{ slug?: string[] }`
`app/[categoryId]/[itemId]/page.js`| `{ categoryId: string, itemId: string }`

`params`가 유효한 값 집합 중 하나로만 제한되는 라우트를 작업 중이라면(예: 알려진 언어 코드 집합을 갖는 `[locale]` 파라미터), 런타임 검증을 사용해 사용자가 입력한 잘못된 파라미터를 처리하고, 애플리케이션의 나머지는 알려진 집합에서 온 더 좁은 타입으로 작업할 수 있습니다.

/app/[locale]/page.tsx
```
    import { notFound } from 'next/navigation'
    import type { Locale } from '@i18n/types'
    import { isValidLocale } from '@i18n/utils'

    function assertValidLocale(value: string): asserts value is Locale {
      if (!isValidLocale(value)) notFound()
    }

    export default async function Page(props: PageProps<'/[locale]'>) {
      const { locale } = await props.params // locale is typed as string
      assertValidLocale(locale)
      // locale is now typed as Locale
    }
```

## 동작[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#behavior)

  * `params` prop은 프로미스이므로 값을 읽으려면 `async`/`await` 또는 React의 use 함수를 사용해야 합니다.
    * 14 버전 이전에는 `params`가 동기 prop이었습니다. 하위 호환을 돕기 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 향후 더 이상 지원되지 않습니다.

### Cache Components와 함께 사용할 때[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)

동적 라우트 세그먼트와 함께 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용할 때 `params`를 다루는 방식은 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 사용하는지 여부에 따라 달라집니다.

`generateStaticParams` 없이 사용하면 파라미터 값은 사전 렌더링 시점에 알 수 없으므로 런타임 데이터입니다. 파라미터 접근을 `<Suspense>` 경계로 감싸서 폴백 UI를 제공해야 합니다.

`generateStaticParams`를 사용하면 빌드 시 사용할 샘플 파라미터 값을 제공합니다. 빌드 과정은 동적 콘텐츠 및 다른 런타임 API가 올바르게 처리되었는지 검증한 뒤 샘플에 대한 정적 HTML 파일을 생성합니다. 런타임 파라미터로 렌더링된 페이지는 첫 요청이 성공하면 디스크에 저장됩니다.

아래 섹션에서는 두 패턴을 모두 보여줍니다.

#### `generateStaticParams` 없이[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#without-generatestaticparams)

모든 파라미터가 런타임 데이터입니다. 파라미터 접근은 Suspense 폴백 UI로 감싸야 합니다. Next.js는 빌드 시 정적 셸을 생성하며 콘텐츠는 각 요청마다 로드됩니다.

> **알아두면 좋은 내용** : 페이지 수준 폴백 UI로 [`loading.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)를 사용할 수도 있습니다.

app/blog/[slug]/page.tsx
```
    import { Suspense } from 'react'

    export default function Page({ params }: PageProps<'/blog/[slug]'>) {
      return (
        <div>
          <h1>Blog Post</h1>
          <Suspense fallback={<div>Loading...</div>}>
            {params.then(({ slug }) => (
              <Content slug={slug} />
            ))}
          </Suspense>
        </div>
      )
    }

    async function Content({ slug }: { slug: string }) {
      const res = await fetch(`https://api.vercel.app/blog/${slug}`)
      const post = await res.json()

      return (
        <article>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      )
    }
```

#### `generateStaticParams`와 함께[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-generatestaticparams)

파라미터를 미리 제공해 빌드 시 페이지를 사전 렌더링합니다. 필요에 따라 모든 라우트나 일부만 사전 렌더링할 수 있습니다.

빌드 과정에서 라우트는 각 샘플 파라미터로 실행되어 HTML 결과를 수집합니다. 동적 콘텐츠나 런타임 데이터를 잘못 접근하면 빌드가 실패합니다.

app/blog/[slug]/page.tsx
```
    import { Suspense } from 'react'

    export async function generateStaticParams() {
      return [{ slug: '1' }, { slug: '2' }, { slug: '3' }]
    }

    export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
      const { slug } = await params

      return (
        <div>
          <h1>Blog Post</h1>
          <Content slug={slug} />
        </div>
      )
    }

    async function Content({ slug }: { slug: string }) {
      const post = await getPost(slug)
      return (
        <article>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      )
    }

    async function getPost(slug: string) {
      'use cache'
      const res = await fetch(`https://api.vercel.app/blog/${slug}`)
      return res.json()
    }
```

빌드 시 검증은 샘플 파라미터로 실행되는 코드 경로만 다룹니다. 특정 파라미터 값에 대해 런타임 API를 호출하는 조건부 로직이 라우트에 있는 경우, 샘플에 없는 값으로 들어가는 분기는 빌드 타임에 검증되지 않습니다:

app/blog/[slug]/page.tsx
```
    import { cookies } from 'next/headers'

    export async function generateStaticParams() {
      return [{ slug: 'public-post' }, { slug: 'hello-world' }]
    }

    export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
      const { slug } = await params

      if (slug.startsWith('private-')) {
        // This branch is never executed at build time
        // Runtime requests for 'private-*' slugs will error
        return <PrivatePost slug={slug} />
      }

      return <PublicPost slug={slug} />
    }

    async function PrivatePost({ slug }: { slug: string }) {
      const token = (await cookies()).get('token')
      // ... fetch and render private post using token for auth
    }
```

`generateStaticParams`가 반환하지 않은 런타임 파라미터에 대해서는 첫 요청 시 검증이 이루어집니다. 위 예시에서 `private-`로 시작하는 슬러그는 `PrivatePost`가 `cookies()`를 Suspense 경계 없이 호출하기 때문에 실패합니다. 조건부 분기를 타지 않는 다른 런타임 파라미터는 정상적으로 렌더링되고 이후 요청을 위해 디스크에 저장됩니다.

이를 해결하려면 `PrivatePost`를 Suspense로 감싸세요:

app/blog/[slug]/page.tsx
```
    import { Suspense } from 'react'
    import { cookies } from 'next/headers'

    export async function generateStaticParams() {
      return [{ slug: 'public-post' }, { slug: 'hello-world' }]
    }

    export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
      const { slug } = await params

      if (slug.startsWith('private-')) {
        return (
```

<Suspense fallback={<div>Loading...</div>}>
            <PrivatePost slug={slug} />
          </Suspense>
        )
      }

      return <PublicPost slug={slug} />
    }

    async function PrivatePost({ slug }: { slug: string }) {
      const token = (await cookies()).get('token')
      // ... fetch and render private post using token for auth
    }

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#examples)

### `generateStaticParams` 사용하기[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-generatestaticparams-1)

[`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) 함수는 요청 시점의 온디맨드 처리 대신, 빌드 시점에 라우트를 [정적으로 생성](https://nextjs.org/docs/app/guides/caching#static-rendering)하는 데 사용할 수 있습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
```
    export async function generateStaticParams() {
      const posts = await fetch('https://.../posts').then((res) => res.json())

      return posts.map((post) => ({
        slug: post.slug,
      }))
    }
```

`generateStaticParams` 함수 내부에서 `fetch`를 사용할 때 요청은 [자동으로 중복 제거](https://nextjs.org/docs/app/guides/caching#request-memoization)됩니다. 덕분에 동일한 데이터에 대해 레이아웃, 페이지, 다른 `generateStaticParams` 함수에서 여러 번 네트워크 호출을 하지 않아도 되어 빌드 시간이 빨라집니다.

### `generateStaticParams`를 사용하는 동적 GET Route Handler[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#dynamic-get-route-handlers-with-generatestaticparams)

`generateStaticParams`는 동적 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서도 작동하여 빌드 시점에 API 응답을 정적으로 생성합니다.

app/api/posts/[id]/route.ts

JavaScriptTypeScript
```
    export async function generateStaticParams() {
      const posts: { id: number }[] = await fetch(
        'https://api.vercel.app/blog'
      ).then((res) => res.json())

      return posts.map((post) => ({
        id: `${post.id}`,
      }))
    }

    export async function GET(
      request: Request,
      { params }: RouteContext<'/api/posts/[id]'>
    ) {
      const { id } = await params
      const res = await fetch(`https://api.vercel.app/blog/${id}`)

      if (!res.ok) {
        return Response.json({ error: 'Post not found' }, { status: 404 })
      }

      const post = await res.json()
      return Response.json(post)
    }
```

이 예제에서는 `generateStaticParams`가 반환한 모든 블로그 게시물 ID에 대한 Route Handler가 빌드 시점에 정적으로 생성됩니다. 다른 ID에 대한 요청은 요청 시점에 동적으로 처리됩니다.

## 다음 단계

다음에 무엇을 해야 하는지 더 자세히 알고 싶다면 아래 섹션을 참고하세요.

- [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
  - 함수에 대한 generateStaticParams API reference.

보내기