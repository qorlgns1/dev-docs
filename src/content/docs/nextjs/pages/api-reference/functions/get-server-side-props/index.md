---
title: '함수: getServerSideProps'
description: '마지막 업데이트 2026년 2월 20일'
---

# 함수: getServerSideProps | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props

[API 레퍼런스](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)getServerSideProps

페이지 복사

# getServerSideProps

마지막 업데이트 2026년 2월 20일

페이지에서 `getServerSideProps`(서버 사이드 렌더링)라는 함수를 내보내면, Next.js는 각 요청마다 `getServerSideProps`가 반환한 데이터를 사용해 이 페이지를 사전 렌더링합니다. 자주 변경되는 데이터를 가져와 페이지가 최신 데이터를 보여 주도록 하고 싶을 때 유용합니다.

pages/index.tsx

JavaScriptTypeScript
[code]
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
[/code]

`getServerSideProps`에서 사용할 모듈을 최상위 스코프에 임포트할 수 있습니다. 이렇게 임포트한 항목은 **클라이언트 번들에 포함되지 않습니다**. 따라서 데이터베이스에서 데이터를 가져오는 등 **서버 사이드 코드를 `getServerSideProps` 안에 직접 작성**할 수 있습니다.

## Context parameter[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#context-parameter)

`context` 매개변수는 다음 키를 포함하는 객체입니다.

Name| Description  
---|---  
`params`| 이 페이지가 [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 사용한다면 `params`에 라우트 매개변수가 들어갑니다. 페이지 이름이 `[id].js`이면 `params`는 `{ id: ... }`처럼 표시됩니다.  
`req`| [`HTTP` IncomingMessage 객체](https://nodejs.org/api/http.html#http_class_http_incomingmessage)에 문자열 키를 해당 쿠키 문자열 값에 매핑하는 `cookies` prop이 추가된 형태입니다.  
`res`| [`HTTP` response 객체](https://nodejs.org/api/http.html#http_class_http_serverresponse)입니다.  
`query`| 동적 라우트 매개변수를 포함한 쿼리 문자열을 표현하는 객체입니다.  
`preview`| (`draftMode`에서 더 이상 사용되지 않음) 페이지가 [프리뷰 모드](https://nextjs.org/docs/pages/guides/preview-mode)일 경우 `true`, 아니면 `false`입니다.  
`previewData`| (`draftMode`에서 더 이상 사용되지 않음) `setPreviewData`로 설정한 [프리뷰](https://nextjs.org/docs/pages/guides/preview-mode) 데이터입니다.  
`draftMode`| 페이지가 [드래프트 모드](https://nextjs.org/docs/pages/guides/draft-mode)일 경우 `true`, 아니면 `false`입니다.  
`resolvedUrl`| 클라이언트 전환 시 `_next/data` 접두사를 제거하고 원래 쿼리 값을 포함하는 요청 `URL`의 정규화 버전입니다.  
`locale`| 활성 로케일(활성화된 경우)을 포함합니다.  
`locales`| 지원되는 모든 로케일(활성화된 경우)을 포함합니다.  
`defaultLocale`| 구성된 기본 로케일(활성화된 경우)을 포함합니다.  
  
## getServerSideProps return values[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#getserversideprops-return-values)

`getServerSideProps` 함수는 **다음 속성 중 하나**를 가진 객체를 반환해야 합니다.

### `props`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#props)

`props` 객체는 키-값 쌍이며, 각 값은 페이지 컴포넌트가 받습니다. 전달된 props는 [`JSON.stringify`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)로 직렬화할 수 있도록 [직렬화 가능한 객체](https://developer.mozilla.org/docs/Glossary/Serialization)여야 합니다.
[code] 
    export async function getServerSideProps(context) {
      return {
        props: { message: `Next.js is awesome` }, // will be passed to the page component as props
      }
    }
[/code]

### `notFound`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#notfound)

`notFound` 불리언을 사용하면 페이지가 `404` 상태와 [404 페이지](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)를 반환할 수 있습니다. `notFound: true`이면 이전에 페이지가 성공적으로 생성되었더라도 `404`를 반환합니다. 이는 사용자가 생성한 콘텐츠가 작성자에 의해 제거되는 등의 사용 사례를 지원하기 위한 것입니다.
[code] 
    export async function getServerSideProps(context) {
      const res = await fetch(`https://.../data`)
      const data = await res.json()
     
      if (!data) {
        return {
          notFound: true,
        }
      }
     
      return {
        props: { data }, // will be passed to the page component as props
      }
    }
[/code]

### `redirect`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#redirect)

`redirect` 객체를 사용하면 내부 및 외부 리소스로 리다이렉트할 수 있습니다. `{ destination: string, permanent: boolean }` 형태와 일치해야 합니다. 드물게는 오래된 `HTTP` 클라이언트에서 올바르게 리다이렉트하려면 사용자 지정 상태 코드를 지정해야 할 수 있습니다. 이 경우 `permanent` 대신 `statusCode` 속성을 사용할 수 있지만 두 속성을 동시에 사용할 수는 없습니다.
[code] 
    export async function getServerSideProps(context) {
      const res = await fetch(`https://.../data`)
      const data = await res.json()
     
      if (!data) {
        return {
          redirect: {
            destination: '/',
            permanent: false,
          },
        }
      }
     
      return {
        props: {}, // will be passed to the page component as props
      }
    }
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#version-history)

Version| Changes  
---|---  
`v13.4.0`| [App Router](https://nextjs.org/docs/app/getting-started/fetching-data)가 단순화된 데이터 페칭과 함께 안정화되었습니다.  
`v10.0.0`| `locale`, `locales`, `defaultLocale`, `notFound` 옵션이 추가되었습니다.  
`v9.3.0`| `getServerSideProps`가 도입되었습니다.  
  
도움이 되었나요?

지원됨.

전송
