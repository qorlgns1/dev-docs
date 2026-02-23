---
title: '함수: getInitialProps'
description: '> 알아두면 좋아요 : 는 레거시 API입니다. 대신  또는 를 사용하는 것을 권장합니다.'
---

# 함수: getInitialProps | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/functions/get-initial-props

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)getInitialProps

페이지 복사

# getInitialProps

마지막 업데이트: 2026년 2월 20일

> **알아두면 좋아요** : `getInitialProps`는 레거시 API입니다. 대신 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) 또는 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)를 사용하는 것을 권장합니다.

`getInitialProps`는 페이지에 기본으로 export되는 React 컴포넌트에 추가할 수 있는 `async` 함수입니다. 이 함수는 서버 측과 페이지 전환 중의 클라이언트 측에서 모두 실행되며, 함수의 반환값은 `props`로 React 컴포넌트에 전달됩니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import { NextPageContext } from 'next'
     
    Page.getInitialProps = async (ctx: NextPageContext) => {
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const json = await res.json()
      return { stars: json.stargazers_count }
    }
     
    export default function Page({ stars }: { stars: number }) {
      return stars
    }
[/code]

> **알아두면 좋아요** :
> 
>   * `getInitialProps`에서 반환된 데이터는 서버 렌더링 시 직렬화됩니다. `getInitialProps`에서 반환하는 객체는 순수한 `Object`여야 하며 `Date`, `Map`, `Set`을 사용하지 않아야 합니다.
>   * 초기 페이지 로드 시 `getInitialProps`는 서버에서만 실행됩니다. 이후 [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) 컴포넌트로 다른 경로로 이동하거나 [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router`)를 사용할 때 클라이언트에서도 실행됩니다.
>   * 커스텀 `_app.js`에서 `getInitialProps`를 사용하고, 이동하려는 페이지가 `getServerSideProps`를 사용한다면 `getInitialProps`는 **서버에서만** 실행됩니다.
> 

## Context Object[](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#context-object)

`getInitialProps`는 `context`라고 불리는 단일 인수를 받으며, 이 객체는 다음 속성들을 포함합니다:

Name| Description  
---|---  
`pathname`| 현재 라우트, `/pages` 내 페이지의 경로  
`query`| URL의 쿼리 문자열을 객체로 파싱한 값  
`asPath`| 브라우저에 표시되는 실제 경로(쿼리 포함)의 `String` 값  
`req`| [HTTP request object](https://nodejs.org/api/http.html#http_class_http_incomingmessage) (서버 전용)  
`res`| [HTTP response object](https://nodejs.org/api/http.html#http_class_http_serverresponse) (서버 전용)  
`err`| 렌더링 중 오류가 발생한 경우의 에러 객체  
  
## 주의사항[](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#caveats)

  * `getInitialProps`는 `pages/` 최상위 파일에서만 사용할 수 있으며, 중첩된 컴포넌트에서는 사용할 수 없습니다. 컴포넌트 수준에서 중첩 데이터 패칭이 필요하다면 [App Router](https://nextjs.org/docs/app/getting-started/fetching-data)를 검토하세요.
  * 라우트가 정적이든 동적이든 관계없이, `getInitialProps`에서 `props`로 반환된 모든 데이터는 초기 HTML에서 클라이언트 측에서 확인할 수 있습니다. 이는 페이지가 올바르게 [hydrate](https://react.dev/reference/react-dom/hydrate)되도록 하기 위한 것입니다. 클라이언트에서 볼 수 없어야 하는 민감한 정보를 `props`로 전달하지 않도록 주의하세요.



도움이 되었나요?

지원됨.

보내기
