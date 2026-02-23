---
title: '데이터 페칭: getStaticProps'
description: '페이지에서 (정적 사이트 생성)라는 함수를 export하면, Next.js는 빌드 시점에 가 반환한 props를 사용해 해당 페이지를 사전 렌더링합니다.'
---

# 데이터 페칭: getStaticProps | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props

# getStaticProps

마지막 업데이트: 2026년 2월 20일

페이지에서 `getStaticProps`(정적 사이트 생성)라는 함수를 export하면, Next.js는 빌드 시점에 `getStaticProps`가 반환한 props를 사용해 해당 페이지를 사전 렌더링합니다.

pages/index.tsx

JavaScriptTypeScript
```
    import type { InferGetStaticPropsType, GetStaticProps } from 'next'

    type Repo = {
      name: string
      stargazers_count: number
    }

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
```

> 렌더링 방식과 관계없이 모든 `props`는 페이지 컴포넌트로 전달되어 초기 HTML에서 클라이언트 측으로 노출됩니다. 이는 페이지가 올바르게 [hydrated](https://react.dev/reference/react-dom/hydrate)되도록 하기 위한 것입니다. 클라이언트에서 공개되면 안 되는 민감한 정보를 `props`로 전달하지 않도록 주의하세요.

[`getStaticProps` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)는 `getStaticProps`에서 사용할 수 있는 모든 매개변수와 props를 다룹니다.

## When should I use getStaticProps?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#when-should-i-use-getstaticprops)

`getStaticProps`를 사용해야 하는 경우:

- 페이지를 렌더링하는 데 필요한 데이터가 사용자의 요청 이전, 빌드 시점에 준비되어 있을 때
- 데이터가 헤드리스 CMS에서 올 때
- 페이지를 (SEO를 위해) 사전 렌더링하고 매우 빠르게 제공해야 할 때 — `getStaticProps`는 `HTML`과 `JSON` 파일을 생성하며, 둘 다 CDN이 캐시하여 성능을 높일 수 있음
- 데이터가 공개 캐시 가능(사용자별이 아님)할 때. 특정 상황에서는 프록시로 경로를 다시 작성해 이 조건을 우회할 수 있음.

## When does getStaticProps run[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#when-does-getstaticprops-run)

`getStaticProps`는 항상 서버에서만 실행되며 클라이언트에서는 실행되지 않습니다. [이 도구](https://next-code-elimination.vercel.app/)로 `getStaticProps` 내부에 작성한 코드가 클라이언트 번들에서 제거되는지 확인할 수 있습니다.

- `getStaticProps`는 항상 `next build` 동안 실행됩니다.
- [`fallback: true`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)를 사용할 때 백그라운드에서 실행됩니다.
- [`fallback: blocking`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)을 사용할 때 초기 렌더 전에 호출됩니다.
- `revalidate`를 사용할 때 백그라운드에서 실행됩니다.
- [`revalidate()`](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)를 사용할 때 백그라운드에서 온디맨드로 실행됩니다.

[Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)과 결합하면, 오래된 페이지가 재검증되는 동안 `getStaticProps`가 백그라운드에서 실행되고, 최신 페이지가 브라우저에 제공됩니다.

정적 HTML을 생성하기 때문에 `getStaticProps`는 들어오는 요청(예: 쿼리 매개변수, HTTP 헤더)에 접근할 수 없습니다. 페이지에서 요청 정보가 필요하다면, `getStaticProps`와 함께 [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy) 사용을 고려하세요.

## Using getStaticProps to fetch data from a CMS[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#using-getstaticprops-to-fetch-data-from-a-cms)

다음 예시는 CMS에서 블로그 글 목록을 가져오는 방법을 보여줍니다.

pages/blog.tsx

JavaScriptTypeScript
```
    // posts will be populated at build time by getStaticProps()
    export default function Blog({ posts }) {
      return (
        <ul>
          {posts.map((post) => (
            <li>{post.title}</li>
          ))}
        </ul>
      )
    }

    // This function gets called at build time on server-side.
    // It won't be called on client-side, so you can even do
    // direct database queries.
    export async function getStaticProps() {
      // Call an external API endpoint to get posts.
      // You can use any data fetching library
      const res = await fetch('https://.../posts')
      const posts = await res.json()

      // By returning { props: { posts } }, the Blog component
      // will receive `posts` as a prop at build time
      return {
        props: {
          posts,
        },
      }
    }
```

[`getStaticProps` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)는 `getStaticProps`에서 사용할 수 있는 모든 매개변수와 props를 다룹니다.

## Write server-side code directly[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#write-server-side-code-directly)

`getStaticProps`는 서버 측에서만 실행되므로 클라이언트에서는 절대 실행되지 않습니다. 브라우저를 위한 JS 번들에도 포함되지 않으므로, 클라이언트로 전송되지 않고 직접 데이터베이스 쿼리를 작성할 수 있습니다.

즉, 외부 소스에서 데이터를 가져오는 **API 라우트**를 `getStaticProps`에서 호출하는 대신, 서버 측 코드를 `getStaticProps` 안에 직접 작성할 수 있습니다.

다음 예제를 살펴보세요. API 라우트가 CMS에서 데이터를 가져오는 데 사용되고, 그 API 라우트를 `getStaticProps`에서 다시 호출합니다. 이로 인해 호출이 하나 더 늘어나 성능이 저하됩니다. 대신 `lib/` 디렉터리를 사용해 CMS에서 데이터를 가져오는 로직을 공유하면, 이를 `getStaticProps`에서도 재사용할 수 있습니다.

lib/load-posts.js
```
    // The following function is shared
    // with getStaticProps and API routes
    // from a `lib/` directory
    export async function loadPosts() {
      // Call an external API endpoint to get posts
      const res = await fetch('https://.../posts/')
      const data = await res.json()

      return data
    }
```

pages/blog.js
```
    // pages/blog.js
    import { loadPosts } from '../lib/load-posts'

    // This function runs only on the server side
    export async function getStaticProps() {
      // Instead of fetching your `/api` route you can call the same
      // function directly in `getStaticProps`
      const posts = await loadPosts()

      // Props returned will be passed to the page component
      return { props: { posts } }
    }
```

또는 데이터를 가져오는 데 API 라우트를 사용하지 않는다면, [`fetch()`](https://developer.mozilla.org/docs/Web/API/Fetch_API) API를 `getStaticProps` 안에서 직접 사용해 데이터를 가져올 수 있습니다.

Next.js가 클라이언트 번들에서 무엇을 제거했는지 확인하려면 [next-code-elimination 도구](https://next-code-elimination.vercel.app/)를 사용할 수 있습니다.

## Statically generates both HTML and JSON[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#statically-generates-both-html-and-json)

`getStaticProps`가 있는 페이지가 빌드 시점에 사전 렌더링되면, 페이지 HTML 파일과 함께 `getStaticProps` 실행 결과를 담고 있는 JSON 파일도 생성됩니다.

이 JSON 파일은 [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) 또는 [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 통한 클라이언트 측 라우팅에 사용됩니다. `getStaticProps`로 사전 렌더링된 페이지로 이동하면, Next.js는 빌드 시점에 미리 계산된 이 JSON 파일을 가져와 페이지 컴포넌트의 props로 사용합니다. 즉, 클라이언트 측 페이지 전환에서는 내보낸 JSON만 사용되므로 `getStaticProps`를 호출하지 않습니다.

Incremental Static Generation을 사용할 때는, 클라이언트 측 내비게이션에 필요한 JSON을 생성하기 위해 `getStaticProps`가 백그라운드에서 실행됩니다. 동일한 페이지에 대해 여러 요청이 발생하는 것처럼 보일 수 있지만, 이는 의도된 동작이며 최종 사용자 성능에는 영향을 주지 않습니다.

## Where can I use getStaticProps[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#where-can-i-use-getstaticprops)

`getStaticProps`는 **페이지**에서만 export할 수 있습니다. 페이지가 아닌 파일, `_app`, `_document`, `_error`에서는 export할 수 없습니다.

이 제한의 이유 중 하나는 React가 페이지를 렌더링하기 전에 필요한 모든 데이터를 확보해야 하기 때문입니다.

또한 `getStaticProps`를 독립 함수로 export해야 하며, 페이지 컴포넌트의 속성으로 추가하면 동작하지 않습니다.

> **알아두면 좋아요**: [커스텀 앱](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)을 만들었다면, 링크된 문서에 나온 것처럼 `pageProps`를 페이지 컴포넌트에 전달해야 합니다. 그렇지 않으면 props가 비어 있게 됩니다.

## Runs on every request in development[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#runs-on-every-request-in-development)

개발 환경(`next dev`)에서는 `getStaticProps`가 요청마다 호출됩니다.

## Preview Mode[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#preview-mode)

[**프리뷰 모드**](https://nextjs.org/docs/pages/guides/preview-mode)를 사용하면 정적 생성을 임시로 우회하여 빌드 시점 대신 **요청 시점**에 페이지를 렌더링할 수 있습니다. 예를 들어, 헤드리스 CMS를 사용하면서 발행 전 초안 상태를 미리 보고 싶을 때 유용합니다.

보내기