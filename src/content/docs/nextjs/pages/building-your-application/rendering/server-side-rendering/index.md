---
title: '렌더링: 서버 사이드 렌더링 (SSR)'
description: '마지막 업데이트 2026년 2월 20일'
---

# 렌더링: 서버 사이드 렌더링 (SSR) | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)Server-side Rendering (SSR)

Copy page

# 서버 사이드 렌더링 (SSR)

마지막 업데이트 2026년 2월 20일

> "SSR" 또는 "동적 렌더링"이라고도 합니다.

페이지가 **서버 사이드 렌더링**을 사용하면 페이지 HTML이 **모든 요청마다** 생성됩니다.

페이지에 서버 사이드 렌더링을 사용하려면 `getServerSideProps`라는 `async` 함수를 `export`해야 합니다. 이 함수는 모든 요청 시 서버에서 호출됩니다.

예를 들어, 페이지가 (외부 API에서 가져오는) 자주 업데이트되는 데이터를 사전 렌더링해야 한다고 가정해 보겠습니다. 아래와 같이 이 데이터를 가져와 `Page`에 전달하는 `getServerSideProps`를 작성할 수 있습니다:
[code] 
    export default function Page({ data }) {
      // Render data...
    }
     
    // This gets called on every request
    export async function getServerSideProps() {
      // Fetch data from external API
      const res = await fetch(`https://.../data`)
      const data = await res.json()
     
      // Pass data to the page via props
      return { props: { data } }
    }
[/code]

보시다시피 `getServerSideProps`는 `getStaticProps`와 비슷하지만, `getServerSideProps`는 빌드 시점이 아니라 모든 요청마다 실행된다는 점이 다릅니다.

`getServerSideProps`가 어떻게 동작하는지 더 알아보려면 [데이터 가져오기 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 확인하세요.

Was this helpful?

supported.

Send
