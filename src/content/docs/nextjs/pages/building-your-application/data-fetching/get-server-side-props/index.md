---
title: '데이터 페칭: getServerSideProps'
description: '는 Next.js 함수로, 요청 시점에 데이터를 가져와 페이지 내용을 렌더링할 때 사용할 수 있습니다.'
---

# 데이터 페칭: getServerSideProps | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props

# getServerSideProps

마지막 업데이트 2026년 2월 20일

`getServerSideProps`는 Next.js 함수로, 요청 시점에 데이터를 가져와 페이지 내용을 렌더링할 때 사용할 수 있습니다.

## 예시[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#example)

Page 컴포넌트에서 `getServerSideProps`를 export해 사용할 수 있습니다. 아래 예시는 `getServerSideProps`에서 3rd party API로부터 데이터를 가져와 props로 페이지에 전달하는 방법을 보여줍니다.

pages/index.tsx

JavaScriptTypeScript
```
    import type { InferGetServerSidePropsType, GetServerSideProps } from 'next'

    type Repo = {
      name: string
      stargazers_count: number
    }

    export const getServerSideProps = (async () => {
      // Fetch data from external API
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const repo: Repo = await res.json()
      // Pass data to the page via props
      return { props: { repo } }
    }) satisfies GetServerSideProps<{ repo: Repo }>

    export default function Page({
      repo,
    }: InferGetServerSidePropsType<typeof getServerSideProps>) {
      return (
        <main>
          <p>{repo.stargazers_count}</p>
        </main>
      )
    }
```

## 언제 `getServerSideProps`를 사용해야 하나요?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#when-should-i-use-getserversideprops)

개인화된 사용자 데이터나 요청 시점에만 알 수 있는 정보(예: `authorization` 헤더, 지리 정보)에 의존하는 페이지를 렌더링해야 한다면 `getServerSideProps`를 사용하세요.

요청 시점에 데이터를 가져올 필요가 없거나, 데이터를 캐시하고 HTML을 사전 렌더링하는 쪽이 더 좋다면 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) 사용을 권장합니다.

## 동작 방식[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#behavior)

  * `getServerSideProps`는 서버에서 실행됩니다.
  * `getServerSideProps`는 **페이지**에서만 export할 수 있습니다.
  * `getServerSideProps`는 JSON을 반환합니다.
  * 사용자가 페이지를 방문하면 `getServerSideProps`가 요청 시점에 데이터를 가져오고, 해당 데이터로 초기 HTML을 렌더링합니다.
  * 페이지 컴포넌트에 전달된 `props`는 초기 HTML의 일부로 클라이언트에서 확인할 수 있으며, 이는 페이지가 올바르게 [수화](https://react.dev/reference/react-dom/hydrate)되도록 하기 위함입니다. 클라이언트에 노출되면 안 되는 민감한 정보를 `props`에 넣지 않도록 주의하세요.
  * 사용자가 [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) 또는 [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 통해 페이지를 방문하면 Next.js는 서버로 API 요청을 보내고, 서버에서 `getServerSideProps`가 실행됩니다.
  * `getServerSideProps`는 서버에서 실행되므로 데이터를 가져오기 위해 Next.js [API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)를 호출할 필요가 없습니다. 대신 `getServerSideProps` 내부에서 CMS, 데이터베이스, 기타 서드파티 API를 직접 호출할 수 있습니다.

> **알아두면 좋아요:**
>
>   * `getServerSideProps`와 함께 사용할 수 있는 매개변수와 props는 [`getServerSideProps` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)를 참고하세요.
>   * [next-code-elimination 도구](https://next-code-elimination.vercel.app/)를 사용해 Next.js가 클라이언트 번들에서 어떤 코드를 제거하는지 확인할 수 있습니다.
>

## 에러 처리[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#error-handling)

`getServerSideProps` 내부에서 에러가 발생하면 `pages/500.js` 파일이 표시됩니다. 해당 파일을 만드는 방법은 [500 페이지](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page) 문서를 참고하세요. 개발 환경에서는 이 파일이 사용되지 않으며, 대신 개발용 에러 오버레이가 표시됩니다.

## 에지 케이스[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#edge-cases)

### 서버 사이드 렌더링(SSR)에서의 캐싱[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#caching-with-server-side-rendering-ssr)

`getServerSideProps` 내부에서 캐싱 헤더(`Cache-Control`)를 사용해 동적 응답을 캐싱할 수 있습니다. 예를 들어 [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/)를 사용할 수 있습니다.
```
    // This value is considered fresh for ten seconds (s-maxage=10).
    // If a request is repeated within the next 10 seconds, the previously
    // cached value will still be fresh. If the request is repeated before 59 seconds,
    // the cached value will be stale but still render (stale-while-revalidate=59).
    //
    // In the background, a revalidation request will be made to populate the cache
    // with a fresh value. If you refresh the page, you will see the new value.
    export async function getServerSideProps({ req, res }) {
      res.setHeader(
        'Cache-Control',
        'public, s-maxage=10, stale-while-revalidate=59'
      )

      return {
        props: {},
      }
    }
```

다만 `cache-control`을 사용하기 전에, [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)와 [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)이 상황에 더욱 적합한지 먼저 검토하는 것을 권장합니다.