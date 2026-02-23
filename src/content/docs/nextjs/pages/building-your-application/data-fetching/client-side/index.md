---
title: '데이터 페칭: 클라이언트 측 페칭'
description: '클라이언트 측 데이터 페칭은 페이지가 SEO 인덱싱을 필요로 하지 않거나, 데이터를 사전 렌더링할 필요가 없거나, 페이지 콘텐츠를 자주 업데이트해야 할 때 유용합니다. 서버 측 렌더링 API와 달리 클라이언트 측 데이터 페칭은 컴포넌트 수준에서 사용할 수 있습니다.'
---

# 데이터 페칭: 클라이언트 측 페칭 | Next.js

소스 URL: https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[데이터 페칭](https://nextjs.org/docs/pages/building-your-application/data-fetching)클라이언트 측 페칭

페이지 복사

# 클라이언트 측 페칭

마지막 업데이트 2026년 2월 20일

클라이언트 측 데이터 페칭은 페이지가 SEO 인덱싱을 필요로 하지 않거나, 데이터를 사전 렌더링할 필요가 없거나, 페이지 콘텐츠를 자주 업데이트해야 할 때 유용합니다. 서버 측 렌더링 API와 달리 클라이언트 측 데이터 페칭은 컴포넌트 수준에서 사용할 수 있습니다.

페이지 수준에서 수행되면 데이터는 런타임에 가져오며 데이터가 변경될 때 페이지 콘텐츠가 업데이트됩니다. 컴포넌트 수준에서 사용하면 컴포넌트가 마운트되는 시점에 데이터를 가져오고, 데이터가 변경될 때 컴포넌트의 콘텐츠가 업데이트됩니다.

클라이언트 측 데이터 페칭을 사용하면 애플리케이션의 성능과 페이지 로딩 속도에 영향을 줄 수 있다는 점을 기억해야 합니다. 이는 데이터가 컴포넌트나 페이지가 마운트되는 시점에 가져와지고, 캐싱되지 않기 때문입니다.

## useEffect를 사용한 클라이언트 측 데이터 페칭[](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side#client-side-data-fetching-with-useeffect)

다음 예시는 useEffect 훅을 사용해 클라이언트 측에서 데이터를 가져오는 방법을 보여줍니다.
[code] 
    import { useState, useEffect } from 'react'
     
    function Profile() {
      const [data, setData] = useState(null)
      const [isLoading, setLoading] = useState(true)
     
      useEffect(() => {
        fetch('/api/profile-data')
          .then((res) => res.json())
          .then((data) => {
            setData(data)
            setLoading(false)
          })
      }, [])
     
      if (isLoading) return <p>Loading...</p>
      if (!data) return <p>No profile data</p>
     
      return (
        <div>
          <h1>{data.name}</h1>
          <p>{data.bio}</p>
        </div>
      )
    }
[/code]

## SWR을 사용한 클라이언트 측 데이터 페칭[](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side#client-side-data-fetching-with-swr)

Next.js 팀은 [**SWR**](https://swr.vercel.app/)이라는 데이터 페칭용 React 훅 라이브러리를 만들었습니다. 클라이언트 측에서 데이터를 가져온다면 **강력히 권장**됩니다. 캐싱, 재검증, 포커스 추적, 주기적 재요청 등 다양한 기능을 처리합니다.

앞선 예시와 동일한 패턴을 사용해 이번에는 SWR로 프로필 데이터를 가져올 수 있습니다. SWR은 데이터를 자동으로 캐시하고 데이터가 오래되면 재검증합니다.

SWR 사용 방법에 대한 자세한 내용은 [SWR 문서](https://swr.vercel.app/docs/getting-started)를 참고하세요.
[code] 
    import useSWR from 'swr'
     
    const fetcher = (...args) => fetch(...args).then((res) => res.json())
     
    function Profile() {
      const { data, error } = useSWR('/api/profile-data', fetcher)
     
      if (error) return <div>Failed to load</div>
      if (!data) return <div>Loading...</div>
     
      return (
        <div>
          <h1>{data.name}</h1>
          <p>{data.bio}</p>
        </div>
      )
    }
[/code]

도움이 되었나요?

지원됨.

보내기
