---
title: '"use cache"에서 cookies() 또는 headers()에 접근할 수 없음'
description: '함수 하나가  주석이 달린 함수의 범위 안에서 현재 들어오는 요청을 읽으려고 했습니다. 이렇게 하면 요청마다 캐시가 무효화되어 의도한 동작이 아니기 때문에 지원되지 않습니다.'
---

# `"use cache"`에서 `cookies()` 또는 `headers()`에 접근할 수 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/next-request-in-use-cache

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)`"use cache"`에서 `cookies()` 또는 `headers()`에 접근할 수 없음

# `"use cache"`에서 `cookies()` 또는 `headers()`에 접근할 수 없음

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/next-request-in-use-cache#why-this-error-occurred)

함수 하나가 `"use cache"` 주석이 달린 함수의 범위 안에서 현재 들어오는 요청을 읽으려고 했습니다. 이렇게 하면 요청마다 캐시가 무효화되어 의도한 동작이 아니기 때문에 지원되지 않습니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/next-request-in-use-cache#possible-ways-to-fix-it)

`"use cache"` 함수 내부에서 호출하는 대신, 함수를 벗어난 곳으로 이동시키고 값을 인자로 전달하세요. 이렇게 하면 전달된 특정 값이 인자를 통해 캐시 키의 일부가 됩니다.

Before:

app/page.js
[code]
    import { cookies } from 'next/headers'

    async function getExampleData() {
      "use cache"
      const isLoggedIn = (await cookies()).has('token')
      ...
    }

    export default async function Page() {
      const data = await getExampleData()
      return ...
    }
[/code]

After:

app/page.js
[code]
    import { cookies } from 'next/headers'

    async function getExampleData(isLoggedIn) {
      "use cache"
      ...
    }

    export default async function Page() {
      const isLoggedIn = (await cookies()).has('token')
      const data = await getExampleData(isLoggedIn)
      return ...
    }
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/next-request-in-use-cache#useful-links)

  * [`headers()` function](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`cookies()` function](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`draftMode()` function](https://nextjs.org/docs/app/api-reference/functions/draft-mode)

supported.

Send
