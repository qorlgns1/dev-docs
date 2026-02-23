---
title: '함수: getStaticPaths'
description: 'pages/repo/[name].tsx'
---

# 함수: getStaticPaths | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/functions/get-static-paths

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)getStaticPaths

페이지 복사

# getStaticPaths

최종 업데이트 2026년 2월 20일

[Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 사용하는 페이지에서 `getStaticPaths`라는 함수를 export하면, Next.js는 `getStaticPaths`가 지정한 모든 경로를 정적으로 사전 렌더링합니다.

pages/repo/[name].tsx

JavaScript TypeScript
[code]
    import type {
      InferGetStaticPropsType,
      GetStaticProps,
      GetStaticPaths,
    } from 'next'
     
    type Repo = {
      name: string
      stargazers_count: number
    }
     
    export const getStaticPaths = (async () => {
      return {
        paths: [
          {
            params: {
              name: 'next.js',
            },
          }, // See the "paths" section below
        ],
        fallback: true, // false or "blocking"
      }
    }) satisfies GetStaticPaths
     
    export const getStaticProps = (async (context) => {
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const repo = await res.json()
      return { props: { repo } }
    }) satisfies GetStaticProps<{
      repo: Repo
    }>
     
    export default function Page({
      repo,
    }: InferGetStaticPropsType<typeof getStaticProps>) {
      return repo.stargazers_count
    }
[/code]

## getStaticPaths 반환 값[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#getstaticpaths-return-values)

`getStaticPaths` 함수는 다음과 같은 **필수** 속성을 포함한 객체를 반환해야 합니다.

### `paths`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#paths)

`paths` 키는 어떤 경로를 사전 렌더링할지를 결정합니다. 예를 들어 `pages/posts/[id].js` 이름의 [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 사용하는 페이지가 있다고 가정해 봅시다. 이 페이지에서 `getStaticPaths`를 export하고 `paths`에 다음을 반환하면:
[code] 
    return {
      paths: [
        { params: { id: '1' }},
        {
          params: { id: '2' },
          // with i18n configured the locale for the path can be returned as well
          locale: "en",
        },
      ],
      fallback: ...
    }
[/code]

Next.js는 `pages/posts/[id].js`의 페이지 컴포넌트를 사용하여 `next build` 중에 `/posts/1`과 `/posts/2`를 정적으로 생성합니다.

각 `params` 객체의 값은 페이지 이름에서 사용한 매개변수와 일치해야 합니다.

  * 페이지 이름이 `pages/posts/[postId]/[commentId]`라면, `params`에는 `postId`와 `commentId`가 포함되어야 합니다.
  * `pages/[...slug]`처럼 [catch-all routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)를 사용하면 `params`에는 (배열인) `slug`가 포함되어야 합니다. 이 배열이 `['hello', 'world']`라면, Next.js는 `/hello/world` 경로의 페이지를 정적으로 생성합니다.
  * 페이지가 [optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)를 사용한다면 최상위 경로를 렌더링하기 위해 `null`, `[]`, `undefined`, `false` 중 하나를 사용합니다. 예를 들어 `pages/[[...slug]]`에 `slug: false`를 제공하면 Next.js는 `/` 페이지를 정적으로 생성합니다.

`params` 문자열은 **대소문자를 구분**하므로 경로가 올바르게 생성되도록 정규화하는 것이 좋습니다. 예를 들어 매개변수로 `WoRLD`를 반환하면 실제 방문 경로도 `WoRLD`일 때만 일치하며, `world`나 `World`와는 일치하지 않습니다.

`params` 객체와 별도로, [i18n을 구성](https://nextjs.org/docs/pages/guides/internationalization)한 경우 경로의 로케일을 설정하는 `locale` 필드를 반환할 수 있습니다.

### `fallback: false`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false)

`fallback`이 `false`이면 `getStaticPaths`가 반환하지 않은 경로는 **404 페이지**가 됩니다.

`next build`를 실행할 때 `getStaticPaths`가 `fallback: false`를 반환하면 Next.js는 `getStaticPaths`가 반환한 경로만 빌드합니다. 생성해야 할 경로가 적거나 새로운 페이지 데이터가 자주 추가되지 않을 때 유용합니다. 더 많은 경로를 추가해야 하고 `fallback: false`로 설정되어 있다면, 새로운 경로를 생성하려면 다시 `next build`를 실행해야 합니다.

다음 예제는 `pages/posts/[id].js`라는 페이지마다 하나의 블로그 글을 사전 렌더링합니다. 블로그 글 목록은 CMS에서 가져와 `getStaticPaths`가 반환하며, 각 페이지는 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 사용해 CMS에서 글 데이터를 가져옵니다.

pages/posts/[id].js
[code]
    function Post({ post }) {
      // Render post...
    }
     
    // This function gets called at build time
    export async function getStaticPaths() {
      // Call an external API endpoint to get posts
      const res = await fetch('https://.../posts')
      const posts = await res.json()
     
      // Get the paths we want to pre-render based on posts
      const paths = posts.map((post) => ({
        params: { id: post.id },
      }))
     
      // We'll pre-render only these paths at build time.
      // { fallback: false } means other routes should 404.
      return { paths, fallback: false }
    }
     
    // This also gets called at build time
    export async function getStaticProps({ params }) {
      // params contains the post `id`.
      // If the route is like /posts/1, then params.id is 1
      const res = await fetch(`https://.../posts/${params.id}`)
      const post = await res.json()
     
      // Pass post data to the page via props
      return { props: { post } }
    }
     
    export default Post
[/code]

### `fallback: true`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)

예시

  * [Static generation of a large number of pages](https://react-tweet.vercel.app/)

`fallback`이 `true`이면 `getStaticProps`의 동작이 다음과 같이 바뀝니다.

  * `getStaticPaths`가 반환한 경로는 `getStaticProps`에 의해 빌드 시점에 `HTML`로 렌더링됩니다.
  * 빌드 시점에 생성되지 않은 경로는 404 페이지가 되지 않습니다. 대신 해당 경로에 최초 요청이 들어오면 Next.js가 페이지의 [“fallback”](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-pages) 버전을 제공합니다. Google과 같은 웹 크롤러에는 fallback이 제공되지 않고 [`fallback: 'blocking'`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)과 동일하게 동작합니다.
  * `fallback: true` 페이지를 `next/link`나 `next/router`(클라이언트 측)로 탐색하면 Next.js는 fallback을 제공하지 않고 [`fallback: 'blocking'`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)처럼 동작합니다.
  * 백그라운드에서 Next.js는 요청된 경로의 `HTML`과 `JSON`을 정적으로 생성하며, 여기에는 `getStaticProps` 실행이 포함됩니다.
  * 완료되면 브라우저는 생성된 경로의 `JSON`을 수신하고, 이를 사용해 필요한 props로 페이지를 자동 렌더링합니다. 사용자 입장에서는 fallback 페이지에서 완전한 페이지로 전환됩니다.
  * 동시에 Next.js는 해당 경로를 사전 렌더링된 페이지 목록에 추가합니다. 이후 동일한 경로에 대한 요청은 빌드 시점에 사전 렌더링된 다른 페이지처럼 생성된 페이지를 제공합니다.

> **알아두면 좋아요**: [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports)를 사용할 때는 `fallback: true`를 지원하지 않습니다.

#### `fallback: true`는 언제 유용할까요?[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#when-is-fallback-true-useful)

`fallback: true`는 데이터에 의존하는 정적 페이지가 매우 많을 때(대규모 전자상거래 사이트 등) 유용합니다. 모든 상품 페이지를 사전 렌더링하면 빌드 시간이 매우 길어지기 때문입니다.

대신 일부 페이지만 정적으로 생성하고 나머지는 `fallback: true`를 사용해 처리할 수 있습니다. 아직 생성되지 않은 페이지를 누군가 요청하면 로딩 인디케이터나 스켈레톤 컴포넌트가 있는 페이지를 보게 됩니다.

곧이어 `getStaticProps`가 완료되면 요청된 데이터로 페이지가 렌더링됩니다. 이후 동일한 페이지를 요청하는 모든 사용자는 정적으로 사전 렌더링된 페이지를 받습니다.

이 방식은 정적 생성을 통한 빠른 사용자 경험과 빠른 빌드 시간을 모두 유지해 줍니다.

`fallback: true`는 생성된 페이지를 _업데이트_하지 않습니다. 업데이트가 필요하면 [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)을 확인하세요.

### `fallback: 'blocking'`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)

`fallback`이 `'blocking'`이면 `getStaticPaths`가 반환하지 않은 새로운 경로는 SSR과 동일하게 `HTML` 생성이 완료될 때까지 대기(_blocking_)하고, 생성된 후에는 미래 요청을 위해 캐시되어 경로마다 한 번만 발생합니다.

`getStaticProps`는 다음과 같이 동작합니다.

  * `getStaticPaths`가 반환한 경로는 빌드 시점에 `getStaticProps`로 `HTML`로 렌더링됩니다.
  * 빌드 시점에 생성되지 않은 경로는 404 페이지가 되지 않습니다. 대신 Next.js가 최초 요청에서 SSR로 `HTML`을 생성해 반환합니다.
  * 완료되면 브라우저는 생성된 경로의 `HTML`을 수신하며, 사용자 입장에서는 “페이지 요청 중” 상태에서 “전체 페이지 로드 완료” 상태로 전환됩니다. 로딩이나 fallback 상태가 깜박이지 않습니다.
  * 동시에 Next.js는 해당 경로를 사전 렌더링된 페이지 목록에 추가합니다. 이후 동일한 경로는 빌드 시점에 사전 렌더링된 다른 페이지처럼 생성된 페이지를 제공합니다.

`fallback: 'blocking'`은 기본적으로 생성된 페이지를 _업데이트_하지 않습니다. 페이지를 업데이트하려면 `fallback: 'blocking'`과 함께 [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)을 사용하세요.

> **알아두면 좋아요**: [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports`)를 사용할 때는 `fallback: 'blocking'`을 지원하지 않습니다.

### Fallback 페이지[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-pages)

페이지의 “fallback” 버전에서는 다음과 같습니다.

  * 페이지 props는 비어 있습니다.
  * [router](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 사용해 fallback이 렌더링 중인지 감지할 수 있으며, `router.isFallback`이 `true`가 됩니다.

다음 예시는 `isFallback` 사용법을 보여 줍니다.

pages/posts/[id].js
[code]
    import { useRouter } from 'next/router'
     
    function Post({ post }) {
      const router = useRouter()
     
      // If the page is not yet generated, this will be displayed
      // initially until getStaticProps() finishes running
      if (router.isFallback) {
        return <div>Loading...</div>
      }
     
      // Render post...
    }
     
    // This function gets called at build time
    export async function getStaticPaths() {
      return {
        // Only `/posts/1` and `/posts/2` are generated at build time
        paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
        // Enable statically generating additional pages
        // For example: `/posts/3`
        fallback: true,
      }
    }
     
    // This also gets called at build time
    export async function getStaticProps({ params }) {
      // params contains the post `id`.
      // If the route is like /posts/1, then params.id is 1
      const res = await fetch(`https://.../posts/${params.id}`)

const post = await res.json()
     
      // Pass post data to the page via props
      return {
        props: { post },
        // Re-generate the post at most once per second
        // if a request comes in
        revalidate: 1,
      }
    }
     
    export default Post
[/code]

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#version-history)

버전| 변경 사항  
---|---  
`v13.4.0`| 단순화된 데이터 패칭(예: [`generateStaticParams()`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params))과 함께 [App Router](https://nextjs.org/docs/app/getting-started/fetching-data)가 이제 안정화되었습니다.  
`v12.2.0`| [온디맨드 Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)가 안정화되었습니다.  
`v12.1.0`| [온디맨드 Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)가 추가되었습니다(베타).  
`v9.5.0`| [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)가 안정화되었습니다.  
`v9.3.0`| `getStaticPaths`가 도입되었습니다.  
  
도움이 되었나요?

지원됨.

전송
