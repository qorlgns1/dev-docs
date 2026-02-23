---
title: '함수: headers'
description: '는 Server Component에서 들어오는 HTTP 요청 헤더를 읽을 수 있게 해 주는 비동기 함수입니다.'
---

# 함수: headers | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/headers

Copy page

# headers

최종 업데이트 2026년 2월 20일

`headers`는 [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 들어오는 HTTP 요청 헤더를 **읽을** 수 있게 해 주는 **비동기** 함수입니다.

app/page.tsx

JavaScriptTypeScript
```
    import { headers } from 'next/headers'

    export default async function Page() {
      const headersList = await headers()
      const userAgent = headersList.get('user-agent')
    }
```

## 참조[](https://nextjs.org/docs/app/api-reference/functions/headers#reference)

### 매개변수[](https://nextjs.org/docs/app/api-reference/functions/headers#parameters)

`headers`는 어떠한 매개변수도 받지 않습니다.

### 반환값[](https://nextjs.org/docs/app/api-reference/functions/headers#returns)

`headers`는 **읽기 전용** [Web Headers](https://developer.mozilla.org/docs/Web/API/Headers) 객체를 반환합니다.

  * [`Headers.entries()`](https://developer.mozilla.org/docs/Web/API/Headers/entries): 이 객체에 포함된 모든 키/값 쌍을 순회할 수 있는 [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols)를 반환합니다.
  * [`Headers.forEach()`](https://developer.mozilla.org/docs/Web/API/Headers/forEach): 이 `Headers` 객체의 각 키/값 쌍에 대해 한 번씩 제공된 함수를 실행합니다.
  * [`Headers.get()`](https://developer.mozilla.org/docs/Web/API/Headers/get): 주어진 이름의 `Headers` 객체 안에서 해당 헤더의 모든 값을 담은 [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) 시퀀스를 반환합니다.
  * [`Headers.has()`](https://developer.mozilla.org/docs/Web/API/Headers/has): `Headers` 객체에 특정 헤더가 포함되어 있는지를 나타내는 불리언을 반환합니다.
  * [`Headers.keys()`](https://developer.mozilla.org/docs/Web/API/Headers/keys): 이 객체에 포함된 키/값 쌍의 모든 키를 순회할 수 있는 [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols)를 반환합니다.
  * [`Headers.values()`](https://developer.mozilla.org/docs/Web/API/Headers/values): 이 객체에 포함된 키/값 쌍의 모든 값을 순회할 수 있는 [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols)를 반환합니다.

## 알아두기[](https://nextjs.org/docs/app/api-reference/functions/headers#good-to-know)

  * `headers`는 **비동기** 함수이며 promise를 반환합니다. `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 14 이전 버전에서는 `headers`가 동기 함수였습니다. 하위 호환을 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 앞으로 사용 중단될 예정입니다.
  * `headers`는 읽기 전용이므로 나가는 요청 헤더에 대해 `set`이나 `delete`를 사용할 수 없습니다.
  * `headers`는 반환값을 사전에 알 수 없는 [동적 API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)입니다. 이를 사용하면 해당 라우트는 **[동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)**을 선택하게 됩니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/headers#examples)

### Authorization 헤더 사용[](https://nextjs.org/docs/app/api-reference/functions/headers#using-the-authorization-header)

app/page.js
```
    import { headers } from 'next/headers'

    export default async function Page() {
      const authorization = (await headers()).get('authorization')
      const res = await fetch('...', {
        headers: { authorization }, // Forward the authorization header
      })
      const user = await res.json()

      return <h1>{user.name}</h1>
    }
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/headers#version-history)

Version| Changes
---|---
`v15.0.0-RC`| `headers`가 이제 비동기 함수입니다. [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150)를 사용할 수 있습니다.
`v13.0.0`| `headers` 도입.

supported.

Send