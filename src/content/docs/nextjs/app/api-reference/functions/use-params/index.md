---
title: 'Functions: useParams'
description: '2026년 2월 20일에 마지막으로 업데이트됨'
---

# Functions: useParams | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/use-params

Copy page

# useParams

2026년 2월 20일에 마지막으로 업데이트됨

`useParams`는 현재 URL이 채운 라우트의 [동적 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 읽을 수 있게 해주는 **클라이언트 컴포넌트** 훅입니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'

    import { useParams } from 'next/navigation'

    export default function ExampleClientComponent() {
      const params = useParams<{ tag: string; item: string }>()

      // Route -> /shop/[tag]/[item]
      // URL -> /shop/shoes/nike-air-max-97
      // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
      console.log(params)

      return '...'
    }
[/code]

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/use-params#parameters)
[code]
    const params = useParams()
[/code]

`useParams`는 어떠한 매개변수도 받지 않습니다.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-params#returns)

`useParams`는 현재 라우트에 채워진 [동적 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 담은 객체를 반환합니다.

  * 객체의 각 속성은 활성화된 동적 세그먼트입니다.
  * 속성 이름은 세그먼트의 이름이며, 속성 값은 해당 세그먼트에 채워진 값입니다.
  * 속성 값은 [동적 세그먼트 유형](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)에 따라 `string` 또는 `string` 배열입니다.
  * 라우트에 동적 매개변수가 없으면 `useParams`는 빈 객체를 반환합니다.
  * Pages Router에서 사용하면, 최초 렌더링 시 `useParams`가 `null`을 반환하고 라우터가 준비되면 위 규칙에 따라 속성으로 업데이트됩니다.

예를 들면:

Route| URL| `useParams()`
---|---|---
`app/shop/page.js`| `/shop`| `{}`
`app/shop/[slug]/page.js`| `/shop/1`| `{ slug: '1' }`
`app/shop/[tag]/[item]/page.js`| `/shop/1/2`| `{ tag: '1', item: '2' }`
`app/shop/[...slug]/page.js`| `/shop/1/2`| `{ slug: ['1', '2'] }`

## Version History[](https://nextjs.org/docs/app/api-reference/functions/use-params#version-history)

Version| Changes
---|---
`v13.3.0`| `useParams` 도입.

supported.

Send
