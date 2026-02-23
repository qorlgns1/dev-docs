---
title: '함수: cookies'
description: '는 Server Components에서 들어오는 HTTP 요청의 쿠키를 읽고, Server Functions 또는 Route Handlers에서 나가는 요청 쿠키를 읽거나 쓸 수 있도록 해주는 비동기 함수입니다.'
---

# 함수: cookies | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/functions/cookies

# cookies

마지막 업데이트 2026년 2월 20일

`cookies`는 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 들어오는 HTTP 요청의 쿠키를 읽고, [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data) 또는 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 나가는 요청 쿠키를 읽거나 쓸 수 있도록 해주는 **비동기** 함수입니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'

    export default async function Page() {
      const cookieStore = await cookies()
      const theme = cookieStore.get('theme')
      return '...'
    }
[/code]

## 참조[](https://nextjs.org/docs/app/api-reference/functions/cookies#reference)

### 메서드[](https://nextjs.org/docs/app/api-reference/functions/cookies#methods)

다음 메서드를 사용할 수 있습니다:

메서드| 반환 타입| 설명
---|---|---
`get('name')`| Object| 쿠키 이름을 받아 이름과 값을 담은 객체를 반환합니다.
`getAll()`| 객체 배열| 지정한 이름과 일치하는 모든 쿠키 목록을 반환합니다.
`has('name')`| Boolean| 쿠키 이름을 받아 해당 쿠키의 존재 여부를 boolean으로 반환합니다.
`set(name, value, options)`| -| 쿠키 이름, 값, 옵션을 받아 나가는 요청 쿠키를 설정합니다.
`delete(name)`| -| 쿠키 이름을 받아 해당 쿠키를 삭제합니다.
`toString()`| String| 쿠키의 문자열 표현을 반환합니다.

### 옵션[](https://nextjs.org/docs/app/api-reference/functions/cookies#options)

쿠키를 설정할 때는 `options` 객체에서 다음 속성을 지원합니다:

옵션| 타입| 설명
---|---|---
`name`| String| 쿠키 이름을 지정합니다.
`value`| String| 쿠키에 저장할 값을 지정합니다.
`expires`| Date| 쿠키가 만료될 정확한 날짜를 정의합니다.
`maxAge`| Number| 쿠키의 수명을 초 단위로 설정합니다.
`domain`| String| 쿠키를 사용할 수 있는 도메인을 지정합니다.
`path`| String, 기본값: `'/'`| 도메인 내에서 쿠키의 적용 범위를 특정 경로로 제한합니다.
`secure`| Boolean| HTTPS 연결에서만 쿠키를 전송하도록 보안을 강화합니다.
`httpOnly`| Boolean| 쿠키를 HTTP 요청으로만 제한하여 클라이언트 측 접근을 차단합니다.
`sameSite`| Boolean, `'lax'`, `'strict'`, `'none'`| 쿠키의 크로스 사이트 요청 동작을 제어합니다.
`priority`| String (`"low"`, `"medium"`, `"high"`)| 쿠키의 우선순위를 지정합니다.
`partitioned`| Boolean| 쿠키가 [partitioned](https://github.com/privacycg/CHIPS)인지 나타냅니다.

기본값이 있는 옵션은 `path`뿐입니다.

옵션에 대한 자세한 내용은 [MDN 문서](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)를 참조하세요.

## 알아두면 좋은 점[](https://nextjs.org/docs/app/api-reference/functions/cookies#good-to-know)

  * `cookies`는 Promise를 반환하는 **비동기** 함수입니다. 쿠키에 접근하려면 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 14 버전 이하에서는 `cookies`가 동기 함수였습니다. 하위 호환을 위해 Next.js 15에서도 동기식 접근이 가능하지만, 향후 폐기될 예정입니다.
  * `cookies`는 반환 값을 미리 알 수 없는 [동적 API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)입니다. 레이아웃이나 페이지에서 사용하면 해당 라우트가 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)을 사용하게 됩니다.
  * `.delete` 메서드는 다음 조건에서만 호출할 수 있습니다:
    * [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) 또는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) 내부.
    * `.set`을 호출하는 도메인과 동일한 도메인에 속할 때. 와일드카드 도메인은 특정 서브도메인이 정확히 일치해야 합니다. 또한 삭제하려는 쿠키와 동일한 프로토콜(HTTP 또는 HTTPS)에서 코드를 실행해야 합니다.
  * HTTP는 스트리밍이 시작된 뒤 쿠키 설정을 허용하지 않으므로, `.set`은 [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) 또는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 사용해야 합니다.

## Server Components에서의 쿠키 동작 이해하기[](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-components)

Server Components에서 쿠키를 다룰 때는 쿠키가 근본적으로 클라이언트 측 저장 메커니즘임을 이해해야 합니다:

  * **쿠키 읽기**는 클라이언트 브라우저가 HTTP 요청 헤더에 담아 서버로 전송한 쿠키 데이터를 읽는 것이기 때문에 Server Components에서도 동작합니다.
  * **쿠키 설정**은 Server Component 렌더링 중에는 지원되지 않습니다. 쿠키를 수정하려면 클라이언트에서 Server Function을 호출하거나 Route Handler를 사용하세요.

서버는 브라우저에 쿠키 저장을 지시하는 `Set-Cookie` 헤더만 보낼 수 있고, 실제 저장은 클라이언트에서 이루어집니다. 따라서 상태를 변경하는 쿠키 작업(`.set`, `.delete`)은 응답 헤더를 제대로 설정할 수 있는 Server Function 또는 Route Handler 내에서 수행해야 합니다.

## Server Functions에서의 쿠키 동작 이해하기[](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-functions)

Server Function에서 쿠키를 설정하거나 삭제한 뒤, 해당 함수가 [Server Action](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions)으로 사용되고 있다면 Next.js는 하나의 서버 라운드트립으로 업데이트된 UI와 새로운 데이터를 동시에 반환할 수 있습니다. 자세한 내용은 [캐싱 가이드](https://nextjs.org/docs/app/guides/caching#cookies)를 참고하세요.

UI는 언마운트되지 않지만, 서버에서 온 데이터에 의존하는 이펙트는 다시 실행됩니다.

캐시된 데이터까지 새로 고치려면 함수 내부에서 [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) 또는 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 호출하세요.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/cookies#examples)

### 쿠키 하나 가져오기[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-a-cookie)

단일 쿠키를 가져오려면 `(await cookies()).get('name')` 메서드를 사용할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'

    export default async function Page() {
      const cookieStore = await cookies()
      const theme = cookieStore.get('theme')
      return '...'
    }
[/code]

### 모든 쿠키 가져오기[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-all-cookies)

지정한 이름과 일치하는 모든 쿠키를 가져오려면 `(await cookies()).getAll()` 메서드를 사용할 수 있습니다. `name`을 지정하지 않으면 사용 가능한 모든 쿠키를 반환합니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'

    export default async function Page() {
      const cookieStore = await cookies()
      return cookieStore.getAll().map((cookie) => (
        <div key={cookie.name}>
          <p>Name: {cookie.name}</p>
          <p>Value: {cookie.value}</p>
        </div>
      ))
    }
[/code]

### 쿠키 설정하기[](https://nextjs.org/docs/app/api-reference/functions/cookies#setting-a-cookie)

쿠키를 설정하려면 [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) 또는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 `(await cookies()).set(name, value, options)` 메서드를 사용할 수 있습니다. [`options` 객체](https://nextjs.org/docs/app/api-reference/functions/cookies#options)는 선택 사항입니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { cookies } from 'next/headers'

    export async function create(data) {
      const cookieStore = await cookies()

      cookieStore.set('name', 'lee')
      // or
      cookieStore.set('name', 'lee', { secure: true })
      // or
      cookieStore.set({
        name: 'name',
        value: 'lee',
        httpOnly: true,
        path: '/',
      })
    }
[/code]

### 쿠키 존재 여부 확인하기[](https://nextjs.org/docs/app/api-reference/functions/cookies#checking-if-a-cookie-exists)

쿠키가 존재하는지 확인하려면 `(await cookies()).has(name)` 메서드를 사용할 수 있습니다:

app/page.ts

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'

    export default async function Page() {
      const cookieStore = await cookies()
      const hasCookie = cookieStore.has('theme')
      return '...'
    }
[/code]

### 쿠키 삭제하기[](https://nextjs.org/docs/app/api-reference/functions/cookies#deleting-cookies)

쿠키를 삭제하는 방법은 세 가지입니다.

`delete()` 메서드 사용:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { cookies } from 'next/headers'

    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.delete('name')
    }
[/code]

동일한 이름과 빈 값으로 새 쿠키 설정:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { cookies } from 'next/headers'

    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.set('name', '')
    }
[/code]

`maxAge`를 0으로 설정하면 쿠키가 즉시 만료됩니다. `maxAge`는 초 단위 값을 받습니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { cookies } from 'next/headers'

    export async function deleteCookie(data) {
      const cookieStore = await cookies()
      cookieStore.set('name', 'value', { maxAge: 0 })
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/cookies#version-history)

버전| 변경 사항
---|---
`v15.0.0-RC`| `cookies`가 이제 비동기 함수입니다. [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#150)를 사용할 수 있습니다.
`v13.0.0`| `cookies` 도입.

보내기
