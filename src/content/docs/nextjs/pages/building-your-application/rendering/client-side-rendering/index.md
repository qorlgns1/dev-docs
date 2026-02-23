---
title: '렌더링: 클라이언트 사이드 렌더링 (CSR)'
description: '최종 업데이트: 2026년 2월 20일'
---

# 렌더링: 클라이언트 사이드 렌더링 (CSR) | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering

[애플리케이션 구축](https://nextjs.org/docs/pages/building-your-application)[렌더링](https://nextjs.org/docs/pages/building-your-application/rendering)클라이언트 사이드 렌더링 (CSR)

페이지 복사

# 클라이언트 사이드 렌더링 (CSR)

최종 업데이트: 2026년 2월 20일

React로 클라이언트 사이드 렌더링(CSR)을 사용할 때 브라우저는 최소한의 HTML 페이지와 해당 페이지에 필요한 JavaScript만 다운로드합니다. 그런 다음 그 JavaScript가 DOM을 업데이트하고 페이지를 렌더링하는 데 사용됩니다. 애플리케이션을 처음 로드하면 전체 페이지를 보기 전에 약간의 지연이 있을 수 있는데, 모든 JavaScript가 다운로드되고 파싱되어 실행될 때까지 페이지가 완전히 렌더링되지 않기 때문입니다.

페이지가 한 번 로드되고 나면 같은 웹사이트의 다른 페이지로 이동하는 속도는 일반적으로 더 빠릅니다. 필요한 데이터만 가져오면 되고, JavaScript가 전체 페이지 새로고침 없이 페이지의 일부만 다시 렌더링할 수 있기 때문입니다.

Next.js에서 클라이언트 사이드 렌더링을 구현하는 방법은 두 가지가 있습니다.

  1. 서버 사이드 렌더링 메서드([`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) 및 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)) 대신 페이지 내부에서 React의 `useEffect()` 훅을 사용합니다.
  2. [SWR](https://swr.vercel.app/) 또는 [TanStack Query](https://tanstack.com/query/latest/) 같은 데이터 패칭 라이브러리를 사용해 클라이언트에서 데이터를 가져옵니다(권장).

다음은 Next.js 페이지 내부에서 `useEffect()`를 사용하는 예시입니다.

pages/index.js
[code]
    import React, { useState, useEffect } from 'react'
     
    export function Page() {
      const [data, setData] = useState(null)
     
      useEffect(() => {
        const fetchData = async () => {
          const response = await fetch('https://api.example.com/data')
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
          }
          const result = await response.json()
          setData(result)
        }
     
        fetchData().catch((e) => {
          // handle the error as needed
          console.error('An error occurred while fetching the data: ', e)
        })
      }, [])
     
      return <p>{data ? `Your data: ${data}` : 'Loading...'}</p>
    }
[/code]

위 예시에서 컴포넌트는 먼저 `Loading...`을 렌더링합니다. 이후 데이터를 가져오면 다시 렌더링되어 데이터를 표시합니다.

`useEffect`에서 데이터를 가져오는 패턴은 오래된 React 애플리케이션에서 볼 수 있지만, 더 나은 성능, 캐싱, 낙관적 업데이트 등을 위해 데이터 패칭 라이브러리 사용을 권장합니다. 다음은 클라이언트에서 데이터를 가져오기 위해 [SWR](https://swr.vercel.app/)을 사용하는 최소 예시입니다.

pages/index.js
[code]
    import useSWR from 'swr'
     
    export function Page() {
      const { data, error, isLoading } = useSWR(
        'https://api.example.com/data',
        fetcher
      )
     
      if (error) return <p>Failed to load.</p>
      if (isLoading) return <p>Loading...</p>
     
      return <p>Your Data: {data}</p>
    }
[/code]

> **알아두면 좋아요** :
>
> CSR은 SEO에 영향을 줄 수 있습니다. 일부 검색 엔진 크롤러는 JavaScript를 실행하지 않기 때문에 애플리케이션의 초기 비어 있거나 로딩 상태만 확인할 수 있습니다. 또한 느린 인터넷 연결이나 기기를 사용하는 사용자에게는 모든 JavaScript가 로드되고 실행될 때까지 전체 페이지를 볼 수 없어 성능 문제가 발생할 수 있습니다. Next.js는 애플리케이션의 각 페이지 **필요에 따라** [서버 사이드 렌더링](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering), [정적 사이트 생성](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation), 클라이언트 사이드 렌더링을 조합해 사용하는 하이브리드 방식을 권장합니다. App Router에서는 페이지가 렌더링되는 동안 [Suspense를 활용한 Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading)를 사용해 로딩 인디케이터를 표시할 수도 있습니다.

## 

Next.js의 다른 렌더링 방식을 살펴보세요.

### [서버 사이드 렌더링 (SSR) 각 요청마다 페이지를 렌더링하려면 서버 사이드 렌더링을 사용하세요.](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
### [정적 사이트 생성 (SSG) 빌드 시점에 페이지를 미리 렌더링하려면 정적 사이트 생성을 사용하세요.](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)
### [ISR 증분 정적 재생성을 사용해 런타임에 정적 페이지를 생성하거나 업데이트하는 방법을 알아보세요.](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)

도움이 되었나요?

지원됨.

보내기
