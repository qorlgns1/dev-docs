---
title: '함수: useSelectedLayoutSegments'
description: '는 호출된 Layout 아래의 활성 라우트 세그먼트를 읽을 수 있게 해주는 Client Component 훅입니다.'
---

# 함수: useSelectedLayoutSegments | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments

Copy page

# useSelectedLayoutSegments

Last updated February 20, 2026

`useSelectedLayoutSegments`는 호출된 Layout **아래**의 활성 라우트 세그먼트를 읽을 수 있게 해주는 **Client Component** 훅입니다.

이 훅은 예를 들어 브레드크럼처럼 활성 하위 세그먼트 정보를 필요로 하는 상위 Layout의 UI를 만들 때 유용합니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useSelectedLayoutSegments } from 'next/navigation'

    export default function ExampleClientComponent() {
      const segments = useSelectedLayoutSegments()

      return (
        <ul>
          {segments.map((segment, index) => (
            <li key={index}>{segment}</li>
          ))}
        </ul>
      )
    }
[/code]

> **알아 두면 좋아요** :
>
>   * `useSelectedLayoutSegments`는 [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) 훅이고 Layout은 기본적으로 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)이므로, 보통 Layout에 import된 Client Component 안에서 `useSelectedLayoutSegments`를 호출합니다.
>   * 반환된 세그먼트에는 [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups)가 포함되므로 UI에 표시하고 싶지 않다면 대괄호로 시작하는 항목을 [`filter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) 배열 메서드로 제거할 수 있습니다.
>   * [catch-all](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments) 라우트의 경우 매칭된 세그먼트를 배열 안에서 하나의 문자열로 결합해 반환합니다. 예를 들어 `app/blog/[...slug]/page.js`가 있고 `/blog/a/b/c`에 방문한 상태에서 `app/layout.js`에서 호출하면 `['blog', 'a/b/c']`를 반환하고 `['blog', 'a', 'b', 'c']`를 반환하지 않습니다.
>

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments#parameters)
[code]
    const segments = useSelectedLayoutSegments(parallelRoutesKey?: string)
[/code]

`useSelectedLayoutSegments`는 선택적으로 [`parallelRoutesKey`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#with-useselectedlayoutsegments)를 받아 해당 슬롯 내 활성 라우트 세그먼트를 읽을 수 있게 해줍니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments#returns)

`useSelectedLayoutSegments`는 훅이 호출된 Layout 바로 한 단계 아래의 활성 세그먼트를 문자열 배열로 반환합니다. 존재하지 않으면 빈 배열을 반환합니다.

아래 Layout과 URL 예시에 대해 반환되는 세그먼트는 다음과 같습니다:

Layout| Visited URL| Returned Segments
---|---|---
`app/layout.js`| `/`| `[]`
`app/layout.js`| `/dashboard`| `['dashboard']`
`app/layout.js`| `/dashboard/settings`| `['dashboard', 'settings']`
`app/dashboard/layout.js`| `/dashboard`| `[]`
`app/dashboard/layout.js`| `/dashboard/settings`| `['settings']`

catch-all 라우트(`[...]`)에서는 매칭된 모든 경로 세그먼트를 배열 내 하나의 문자열로 결합해 반환합니다:

Layout| Visited URL| Returned Segments
---|---|---
`app/layout.js`| `/blog/a/b/c`| `['blog', 'a/b/c']`
`app/blog/layout.js`| `/blog/a/b/c`| `['a/b/c']`

## Version History[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments#version-history)

Version| Changes
---|---
`v13.0.0`| `useSelectedLayoutSegments` 도입.

Was this helpful?

supported.

Send
