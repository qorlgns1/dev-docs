---
title: 'Functions: usePathname'
description: '은 현재 URL의 pathname을 읽을 수 있게 해주는 클라이언트 컴포넌트 훅입니다.'
---

# Functions: usePathname | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/use-pathname

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)usePathname

Copy page

# usePathname

마지막 업데이트 2026년 2월 20일

`usePathname`은 현재 URL의 **pathname**을 읽을 수 있게 해주는 **클라이언트 컴포넌트** 훅입니다.

> **알아두면 좋아요**: [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)를 활성화하면 라우트에 동적 매개변수가 있는 경우 `usePathname` 주변에 `Suspense` 경계가 필요할 수 있습니다. `generateStaticParams`를 사용하면 `Suspense` 경계는 선택 사항입니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { usePathname } from 'next/navigation'
     
    export default function ExampleClientComponent() {
      const pathname = usePathname()
      return <p>Current pathname: {pathname}</p>
    }
[/code]

`usePathname`은 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 사용을 의도적으로 요구합니다. 클라이언트 컴포넌트는 비최적화 요소가 아니라 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 아키텍처의 필수 요소임을 기억하세요.

예를 들어 `usePathname`을 사용하는 클라이언트 컴포넌트는 초기 페이지 로드 시 HTML로 렌더링됩니다. 새 라우트로 이동할 때 이 컴포넌트를 다시 가져올 필요가 없습니다. 대신 컴포넌트는 한 번(클라이언트 JavaScript 번들에서) 다운로드되고 현재 상태에 따라 다시 렌더링됩니다.

> **알아두면 좋아요** :
> 
>   * [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 현재 URL을 읽는 것은 지원되지 않습니다. 이 설계는 페이지 탐색 전체에서 레이아웃 상태 보존을 지원하기 위한 의도적인 결정입니다.
>   * 페이지가 정적으로 사전 렌더링되고 앱에 `next.config`의 [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) 또는 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) 파일이 있는 경우, `usePathname()`으로 pathname을 읽으면 수화 불일치 오류가 발생할 수 있습니다. 초기 값은 서버에서 오기 때문에 라우팅 후 실제 브라우저 pathname과 일치하지 않을 수 있습니다. 이 문제를 완화하는 방법은 [예제](https://nextjs.org/docs/app/api-reference/functions/use-pathname#avoid-hydration-mismatch-with-rewrites)를 참고하세요.
> 

Pages Router와의 호환성

`usePathname`을 사용하는 컴포넌트를 Pages Router 내 라우트에 가져오면 라우터가 아직 초기화되지 않은 경우 `usePathname`이 `null`을 반환할 수 있습니다. 이는 [fallback 라우트](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)나 Pages Router에서 [자동 정적 최적화](https://nextjs.org/docs/pages/building-your-application/rendering/static#automatic-static-optimization) 중에 발생할 수 있습니다.

라우팅 시스템 간 호환성을 높이기 위해 프로젝트에 `app`과 `pages` 디렉터리가 모두 존재하면 Next.js가 `usePathname`의 반환 타입을 자동으로 조정합니다.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#parameters)
[code] 
    const pathname = usePathname()
[/code]

`usePathname`은 매개변수를 받지 않습니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#returns)

`usePathname`은 현재 URL의 pathname 문자열을 반환합니다. 예:

URL| 반환 값  
---|---  
`/`| `'/'`  
`/dashboard`| `'/dashboard'`  
`/dashboard?v=2`| `'/dashboard'`  
`/blog/hello-world`| `'/blog/hello-world'`  
  
## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#examples)

### 라우트 변경에 대응하여 작업 수행[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#do-something-in-response-to-a-route-change)

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useEffect } from 'react'
    import { usePathname, useSearchParams } from 'next/navigation'
     
    function ExampleClientComponent() {
      const pathname = usePathname()
      const searchParams = useSearchParams()
      useEffect(() => {
        // Do something here...
      }, [pathname, searchParams])
    }
[/code]

### rewrites로 인한 수화 불일치 방지[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#avoid-hydration-mismatch-with-rewrites)

페이지가 사전 렌더링되면 HTML은 원본 pathname을 기준으로 생성됩니다. 이후 `next.config` 또는 `Proxy`를 사용한 rewrite를 통해 페이지에 도달하면 브라우저 URL이 달라질 수 있고, 클라이언트에서 `usePathname()`은 rewrite된 pathname을 읽습니다.

수화 불일치를 피하려면 클라이언트 pathname에만 의존하는 UI 부분을 작고 독립적으로 설계하세요. 서버에서는 안정적인 폴백을 렌더링하고 마운트 후 해당 부분만 업데이트합니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useEffect, useState } from 'react'
    import { usePathname } from 'next/navigation'
     
    export default function PathnameBadge() {
      const pathname = usePathname()
      const [clientPathname, setClientPathname] = useState('')
     
      useEffect(() => {
        setClientPathname(pathname)
      }, [pathname])
     
      return (
        <p>
          Current pathname: <span>{clientPathname}</span>
        </p>
      )
    }
[/code]

Version| 변경 사항  
---|---  
`v13.0.0`| `usePathname` 도입.  
  
Was this helpful?

supported.

Send
