---
title: '함수: redirect'
description: '함수는 사용자를 다른 URL로 리디렉션할 수 있게 해 줍니다. 는 서버 및 클라이언트 컴포넌트, 라우트 핸들러, 서버 함수에서 렌더링 중에 사용할 수 있습니다.'
---

# 함수: redirect | Next.js
Source URL: https://nextjs.org/docs/app/api-reference/functions/redirect

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[함수](https://nextjs.org/docs/app/api-reference/functions)redirect

페이지 복사

# redirect

마지막 업데이트 2026년 2월 20일

`redirect` 함수는 사용자를 다른 URL로 리디렉션할 수 있게 해 줍니다. `redirect`는 [서버 및 클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components), [라우트 핸들러](https://nextjs.org/docs/app/api-reference/file-conventions/route), [서버 함수](https://nextjs.org/docs/app/getting-started/updating-data)에서 렌더링 중에 사용할 수 있습니다.

[스트리밍 컨텍스트](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)에서 사용하면 클라이언트 측에서 리디렉션을 발생시키는 메타 태그를 삽입합니다. 서버 액션에서 사용하면 호출자에게 303 HTTP 리디렉션 응답을 반환합니다. 그 밖의 경우에는 호출자에게 307 HTTP 리디렉션 응답을 반환합니다.

리소스가 존재하지 않을 때는 [`notFound` 함수](https://nextjs.org/docs/app/api-reference/functions/not-found)를 대신 사용할 수 있습니다.

## Reference[](https://nextjs.org/docs/app/api-reference/functions/redirect#reference)

### Parameters[](https://nextjs.org/docs/app/api-reference/functions/redirect#parameters)

`redirect` 함수는 두 개의 인수를 받습니다:
[code] 
    redirect(path, type)
[/code]

Parameter| Type| Description  
---|---|---  
`path`| `string`| 리디렉션할 URL입니다. 상대 경로나 절대 경로 모두 사용할 수 있습니다.  
`type`| `'replace'`(기본값) 또는 `'push'`(서버 액션의 기본값)| 수행할 리디렉션 유형입니다.  
  
기본적으로 `redirect`는 [서버 액션](https://nextjs.org/docs/app/getting-started/updating-data)에서는 `push`(브라우저 히스토리 스택에 새 항목 추가)를 사용하고, 그 외 모든 곳에서는 `replace`(브라우저 히스토리 스택의 현재 URL 교체)를 사용합니다. `type` 매개변수를 지정해 이 동작을 재정의할 수 있습니다.

`RedirectType` 객체는 `type` 매개변수에 사용 가능한 옵션을 포함합니다.
[code] 
    import { redirect, RedirectType } from 'next/navigation'
     
    redirect('/redirect-to', RedirectType.replace)
    // or
    redirect('/redirect-to', RedirectType.push)
[/code]

`type` 매개변수는 서버 컴포넌트에서 사용할 때는 아무 효과가 없습니다.

### Returns[](https://nextjs.org/docs/app/api-reference/functions/redirect#returns)

`redirect`는 값을 반환하지 않습니다.

## Behavior[](https://nextjs.org/docs/app/api-reference/functions/redirect#behavior)

  * 서버 액션과 라우트 핸들러에서 `try/catch` 문을 사용할 때는 리디렉션을 `try` 블록 **외부**에서 호출해야 합니다.
  * 307(임시) 대신 308(영구) HTTP 리디렉션을 반환하고 싶다면 [`permanentRedirect` 함수](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)를 사용하세요.
  * `redirect`는 에러를 던지므로 `try/catch` 문을 쓸 때는 반드시 `try` 블록 **외부**에서 호출해야 합니다.
  * `redirect`는 클라이언트 컴포넌트의 렌더링 과정에서 호출할 수 있지만 이벤트 핸들러에서는 사용할 수 없습니다. 대신 [`useRouter` 훅](https://nextjs.org/docs/app/api-reference/functions/use-router)을 사용할 수 있습니다.
  * `redirect`는 절대 URL도 허용하며 외부 링크로 리디렉션하는 데 사용할 수 있습니다.
  * 렌더 과정 이전에 리디렉션하고 싶다면 [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) 또는 [프록시](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy)를 사용하세요.



## Example[](https://nextjs.org/docs/app/api-reference/functions/redirect#example)

### Server Component[](https://nextjs.org/docs/app/api-reference/functions/redirect#server-component)

`redirect()` 함수를 호출하면 `NEXT_REDIRECT` 오류가 발생하고, 오류가 발생한 라우트 세그먼트의 렌더링이 종료됩니다.

app/team/[id]/page.tsx

JavaScriptTypeScript
[code]
    import { redirect } from 'next/navigation'
     
    async function fetchTeam(id: string) {
      const res = await fetch('https://...')
      if (!res.ok) return undefined
      return res.json()
    }
     
    export default async function Profile({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const team = await fetchTeam(id)
     
      if (!team) {
        redirect('/login')
      }
     
      // ...
    }
[/code]

> **알아두면 좋은 점** : `redirect`는 TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) 타입을 사용하므로 `return redirect()` 형태로 쓸 필요가 없습니다.

### Client Component[](https://nextjs.org/docs/app/api-reference/functions/redirect#client-component)

`redirect`는 클라이언트 컴포넌트에서도 바로 사용할 수 있습니다.

components/client-redirect.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { redirect, usePathname } from 'next/navigation'
     
    export function ClientRedirect() {
      const pathname = usePathname()
     
      if (pathname.startsWith('/admin') && !pathname.includes('/login')) {
        redirect('/admin/login')
      }
     
      return <div>Login Page</div>
    }
[/code]

> **알아두면 좋은 점** : 클라이언트 컴포넌트에서 서버 사이드 렌더링(SSR) 중 초기 페이지 로드 시 `redirect`를 사용하면 서버 측 리디렉션이 수행됩니다.

`redirect`는 서버 액션을 통해 클라이언트 컴포넌트에서 사용할 수도 있습니다. 이벤트 핸들러에서 사용자를 리디렉션해야 한다면 [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) 훅을 사용하세요.

app/client-redirect.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { navigate } from './actions'
     
    export function ClientRedirect() {
      return (
        <form action={navigate}>
          <input type="text" name="id" />
          <button>Submit</button>
        </form>
      )
    }
[/code]

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { redirect } from 'next/navigation'
     
    export async function navigate(data: FormData) {
      redirect(`/posts/${data.get('id')}`)
    }
[/code]

## FAQ[](https://nextjs.org/docs/app/api-reference/functions/redirect#faq)

### 왜 `redirect`는 307과 308을 사용하나요?[](https://nextjs.org/docs/app/api-reference/functions/redirect#why-does-redirect-use-307-and-308)

`redirect()`를 사용할 때 상태 코드가 임시 리디렉션에는 `307`, 영구 리디렉션에는 `308`이라는 점을 확인할 수 있습니다. 전통적으로는 임시 리디렉션에 `302`, 영구 리디렉션에 `301`을 사용했지만, 많은 브라우저가 `302`를 사용할 때 원래 요청 메서드와 상관없이 리디렉션 요청 메서드를 `POST`에서 `GET`으로 변경했습니다.

`/users`에서 `/people`로 리디렉션하는 아래 예시에서, 새로운 사용자를 만들기 위해 `/users`에 `POST` 요청을 보내고 `302` 임시 리디렉션을 따르면, 요청 메서드는 `POST`에서 `GET`으로 바뀝니다. 그러나 새 사용자를 만들려면 `/people`에 `POST` 요청을 보내야 하며, `GET` 요청으로는 의미가 없습니다.

`307` 상태 코드가 도입되면서 요청 메서드를 `POST` 그대로 유지할 수 있게 되었습니다.

  * `302` - 임시 리디렉션이며 요청 메서드를 `POST`에서 `GET`으로 변경합니다.
  * `307` - 임시 리디렉션이며 요청 메서드를 `POST`로 유지합니다.



`redirect()` 메서드는 기본적으로 `302` 대신 `307` 임시 리디렉션을 사용하므로, 요청이 항상 `POST`로 유지됩니다.

HTTP 리디렉션에 대해 [더 알아보기](https://developer.mozilla.org/docs/Web/HTTP/Redirections).

## Version History[](https://nextjs.org/docs/app/api-reference/functions/redirect#version-history)

Version| Changes  
---|---  
`v13.0.0`| `redirect`가 도입되었습니다.  
  
## 

### [permanentRedirect 함수의 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)

도움이 되었나요?

지원됨.

전송
