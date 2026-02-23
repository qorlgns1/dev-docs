---
title: 'Functions: notFound'
description: '마지막 업데이트: 2026년 2월 20일'
---

# Functions: notFound | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/not-found

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)notFound

Copy page

# notFound

마지막 업데이트: 2026년 2월 20일

`notFound` 함수는 라우트 세그먼트 내에서 [`not-found` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)을 렌더링하고 `<meta name="robots" content="noindex" />` 태그를 삽입할 수 있도록 해줍니다.

## `notFound()`[](https://nextjs.org/docs/app/api-reference/functions/not-found#notfound)

`notFound()` 함수를 호출하면 `NEXT_HTTP_ERROR_FALLBACK;404` 오류가 발생하고, 해당 오류가 발생한 라우트 세그먼트의 렌더링이 종료됩니다. [**not-found** 파일](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)을 지정하면 세그먼트 내에서 Not Found UI를 렌더링하여 이러한 오류를 우아하게 처리할 수 있습니다.

app/user/[id]/page.js
[code]
    import { notFound } from 'next/navigation'
     
    async function fetchUser(id) {
      const res = await fetch('https://...')
      if (!res.ok) return undefined
      return res.json()
    }
     
    export default async function Profile({ params }) {
      const { id } = await params
      const user = await fetchUser(id)
     
      if (!user) {
        notFound()
      }
     
      // ...
    }
[/code]

> **알아두면 좋은 점** : TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) 타입 덕분에 `notFound()`는 `return notFound()`를 사용할 필요가 없습니다.

## Version History[](https://nextjs.org/docs/app/api-reference/functions/not-found#version-history)

Version| Changes  
---|---  
`v13.0.0`| `notFound`가 도입되었습니다.  
  
Was this helpful?

supported.

Send
