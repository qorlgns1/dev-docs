---
title: '함수: permanentRedirect'
description: '함수는 사용자를 다른 URL로 리디렉션하도록 해 줍니다. 는 서버 컴포넌트, 클라이언트 컴포넌트, 라우트 핸들러, 서버 함수에서 사용할 수 있습니다.'
---

# 함수: permanentRedirect | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/permanentRedirect

[API 참조](https://nextjs.org/docs/app/api-reference)[함수](https://nextjs.org/docs/app/api-reference/functions)permanentRedirect

페이지 복사

# permanentRedirect

마지막 업데이트 2026년 2월 20일

`permanentRedirect` 함수는 사용자를 다른 URL로 리디렉션하도록 해 줍니다. `permanentRedirect`는 서버 컴포넌트, 클라이언트 컴포넌트, [라우트 핸들러](https://nextjs.org/docs/app/api-reference/file-conventions/route), [서버 함수](https://nextjs.org/docs/app/getting-started/updating-data)에서 사용할 수 있습니다.

스트리밍 컨텍스트에서 사용되면 클라이언트에서 리디렉션을 발생시키는 메타 태그를 삽입합니다. 서버 액션에서 사용되면 호출자에게 303 HTTP 리디렉션 응답을 제공합니다. 그 밖에는 호출자에게 308(영구) HTTP 리디렉션 응답을 제공합니다.

리소스가 존재하지 않는다면, 대신 [`notFound` 함수](https://nextjs.org/docs/app/api-reference/functions/not-found)를 사용할 수 있습니다.

> **알아두면 좋아요** : 308(영구) 대신 307(임시) HTTP 리디렉션을 반환하고 싶다면 [`redirect` 함수](https://nextjs.org/docs/app/api-reference/functions/redirect)를 사용할 수 있습니다.

## 매개변수[](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect#parameters)

`permanentRedirect` 함수는 두 개의 인수를 받습니다:
[code] 
    permanentRedirect(path, type)
[/code]

Parameter| Type| Description  
---|---|---  
`path`| `string`| 리디렉션할 URL입니다. 상대 또는 절대 경로 모두 가능합니다.  
`type`| `'replace'` (기본값) 또는 `'push'` (서버 액션의 기본값)| 수행할 리디렉션 유형입니다.  
  
기본적으로 `permanentRedirect`는 [서버 액션](https://nextjs.org/docs/app/getting-started/updating-data)에서 `push`(브라우저 히스토리 스택에 새 항목 추가)를, 다른 모든 곳에서는 `replace`(브라우저 히스토리 스택의 현재 URL 교체)를 사용합니다. `type` 매개변수를 지정해 이 동작을 덮어쓸 수 있습니다.

`RedirectType` 객체에는 `type` 매개변수에 사용할 수 있는 옵션이 포함되어 있습니다.
[code] 
    import { permanentRedirect, RedirectType } from 'next/navigation'
     
    permanentRedirect('/redirect-to', RedirectType.replace)
    // or
    permanentRedirect('/redirect-to', RedirectType.push)
[/code]

`type` 매개변수는 서버 컴포넌트에서 사용될 때는 영향을 주지 않습니다.

## 반환값[](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect#returns)

`permanentRedirect`는 값을 반환하지 않습니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect#example)

`permanentRedirect()` 함수를 호출하면 `NEXT_REDIRECT` 오류가 발생하고, 오류가 발생한 라우트 세그먼트의 렌더링이 종료됩니다.

app/team/[id]/page.js
[code]
    import { permanentRedirect } from 'next/navigation'
     
    async function fetchTeam(id) {
      const res = await fetch('https://...')
      if (!res.ok) return undefined
      return res.json()
    }
     
    export default async function Profile({ params }) {
      const { id } = await params
      const team = await fetchTeam(id)
      if (!team) {
        permanentRedirect('/login')
      }
     
      // ...
    }
[/code]

> **알아두면 좋아요** : `permanentRedirect`는 TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) 타입을 사용하기 때문에 `return permanentRedirect()`를 사용할 필요가 없습니다.

## 

### [redirect 함수에 대한 API 참조.](https://nextjs.org/docs/app/api-reference/functions/redirect)

도움이 되었나요?

지원됨.

보내기
