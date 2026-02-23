---
title: '시작하기: 데이터 업데이트'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: 데이터 업데이트 | Next.js
출처 URL: https://nextjs.org/docs/app/getting-started/updating-data

[App Router](https://nextjs.org/docs/app)[시작하기](https://nextjs.org/docs/app/getting-started)데이터 업데이트

페이지 복사

# 데이터 업데이트

마지막 업데이트 2026년 2월 20일

Next.js에서는 React의 [Server Functions](https://react.dev/reference/rsc/server-functions)을 사용해 데이터를 업데이트할 수 있습니다. 이 페이지에서는 Server Function을 [생성](https://nextjs.org/docs/app/getting-started/updating-data#creating-server-functions)하고 [호출](https://nextjs.org/docs/app/getting-started/updating-data#invoking-server-functions)하는 방법을 다룹니다.

## Server Function이란?[](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions)

**Server Function**은 서버에서 실행되는 비동기 함수입니다. 클라이언트에서 네트워크 요청을 통해 호출되기 때문에 반드시 비동기 함수여야 합니다.

`action` 또는 변경 작업 컨텍스트에서는 **Server Action**이라고도 불립니다.

> **참고:** Server Action은 Server Function을 특정 방식(폼 제출과 변경 작업 처리)에 사용한 것입니다. Server Function이 더 넓은 개념입니다.

관례적으로 Server Action은 [`startTransition`](https://react.dev/reference/react/startTransition)과 함께 사용하는 async 함수입니다. 함수가 다음과 같은 경우 자동으로 해당 동작이 적용됩니다.

  * `action` prop을 사용해 `<form>`에 전달된 경우
  * `formAction` prop을 사용해 `<button>`에 전달된 경우

Next.js에서는 Server Action이 프레임워크의 [캐싱](https://nextjs.org/docs/app/guides/caching) 아키텍처와 통합됩니다. 액션이 호출되면 Next.js는 업데이트된 UI와 새 데이터를 단일 서버 라운드트립으로 반환할 수 있습니다.

내부적으로 액션은 `POST` 메서드를 사용하며, 이 HTTP 메서드만 액션을 호출할 수 있습니다.

## Server Function 생성하기[](https://nextjs.org/docs/app/getting-started/updating-data#creating-server-functions)

Server Function은 [`use server`](https://react.dev/reference/rsc/use-server) 지시어로 정의할 수 있습니다. **비동기** 함수 상단에 지시어를 배치해 해당 함수를 Server Function으로 표시하거나, 별도 파일 상단에 배치해 그 파일의 모든 export를 Server Function으로 표시할 수 있습니다.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    export async function createPost(formData: FormData) {
      'use server'
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Update data
      // Revalidate cache
    }
     
    export async function deletePost(formData: FormData) {
      'use server'
      const id = formData.get('id')
     
      // Update data
      // Revalidate cache
    }
[/code]

### Server Components[](https://nextjs.org/docs/app/getting-started/updating-data#server-components)

Server Function은 함수 본문 상단에 `"use server"` 지시어를 추가해 Server Component 안에 인라인으로 작성할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      // Server Action
      async function createPost(formData: FormData) {
        'use server'
        // ...
      }
     
      return <></>
    }
[/code]

> **참고:** Server Component는 기본적으로 단계별 향상을 지원하므로, JavaScript가 아직 로드되지 않았거나 비활성화되어 있어도 Server Action을 호출하는 폼은 제출됩니다.

### Client Components[](https://nextjs.org/docs/app/getting-started/updating-data#client-components)

Client Component 안에서는 Server Function을 정의할 수 없습니다. 그러나 파일 상단에 `"use server"` 지시어가 선언된 파일에서 import하여 Client Component에서 호출할 수 있습니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost() {}
[/code]

app/ui/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { createPost } from '@/app/actions'
     
    export function Button() {
      return <button formAction={createPost}>Create</button>
    }
[/code]

> **참고:** Client Component에서 Server Action을 호출하는 폼은 JavaScript가 아직 로드되지 않았을 때 제출을 대기열에 넣고, 수화(hydration) 우선순위를 갖습니다. 수화 이후에는 폼을 제출해도 브라우저가 새로 고침되지 않습니다.

### 액션을 prop으로 전달하기[](https://nextjs.org/docs/app/getting-started/updating-data#passing-actions-as-props)

액션을 Client Component에 prop으로 전달할 수도 있습니다.
[code] 
    <ClientComponent updateItemAction={updateItem} />
[/code]

app/client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function ClientComponent({
      updateItemAction,
    }: {
      updateItemAction: (formData: FormData) => void
    }) {
      return <form action={updateItemAction}>{/* ... */}</form>
    }
[/code]

## Server Function 호출하기[](https://nextjs.org/docs/app/getting-started/updating-data#invoking-server-functions)

Server Function을 호출하는 주요 방법은 두 가지입니다.

  1. Server 및 Client Component의 [폼](https://nextjs.org/docs/app/getting-started/updating-data#forms)
  2. Client Component의 [이벤트 핸들러](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers)와 [useEffect](https://nextjs.org/docs/app/getting-started/updating-data#useeffect)

> **참고:** Server Function은 서버 측 변경 작업을 위해 설계되었습니다. 현재 클라이언트는 이를 한 번에 하나씩 디스패치하고 대기합니다. 이는 구현 세부 사항이며 변경될 수 있습니다. 병렬 데이터 패칭이 필요하다면 Server Component에서 [데이터 패칭](https://nextjs.org/docs/app/getting-started/fetching-data#server-components)을 사용하거나, 단일 Server Function 또는 [Route Handler](https://nextjs.org/docs/app/guides/backend-for-frontend#manipulating-data) 내부에서 병렬 작업을 수행하세요.

### 폼[](https://nextjs.org/docs/app/getting-started/updating-data#forms)

React는 HTML [`<form>`](https://react.dev/reference/react-dom/components/form) 요소를 확장해 HTML `action` prop으로 Server Function을 호출할 수 있게 합니다.

폼에서 호출될 때 함수는 자동으로 [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData/FormData) 객체를 받습니다. 네이티브 [`FormData` 메서드](https://developer.mozilla.org/en-US/docs/Web/API/FormData#instance_methods)를 사용해 데이터를 추출할 수 있습니다.

app/ui/form.tsx

JavaScriptTypeScript
[code]
    import { createPost } from '@/app/actions'
     
    export function Form() {
      return (
        <form action={createPost}>
          <input type="text" name="title" />
          <input type="text" name="content" />
          <button type="submit">Create</button>
        </form>
      )
    }
[/code]

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Update data
      // Revalidate cache
    }
[/code]

### 이벤트 핸들러[](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers)

`onClick`과 같은 이벤트 핸들러를 사용하여 Client Component에서 Server Function을 호출할 수 있습니다.

app/like-button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { incrementLike } from './actions'
    import { useState } from 'react'
     
    export default function LikeButton({ initialLikes }: { initialLikes: number }) {
      const [likes, setLikes] = useState(initialLikes)
     
      return (
        <>
          <p>Total Likes: {likes}</p>
          <button
            onClick={async () => {
              const updatedLikes = await incrementLike()
              setLikes(updatedLikes)
            }}
          >
            Like
          </button>
        </>
      )
    }
[/code]

## 예시[](https://nextjs.org/docs/app/getting-started/updating-data#examples)

### 보류 상태 표시하기[](https://nextjs.org/docs/app/getting-started/updating-data#showing-a-pending-state)

Server Function을 실행하는 동안 React의 [`useActionState`](https://react.dev/reference/react/useActionState) 훅을 사용해 로딩 지시자를 표시할 수 있습니다. 이 훅은 `pending` 불리언을 반환합니다.

app/ui/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState, startTransition } from 'react'
    import { createPost } from '@/app/actions'
    import { LoadingSpinner } from '@/app/ui/loading-spinner'
     
    export function Button() {
      const [state, action, pending] = useActionState(createPost, false)
     
      return (
        <button onClick={() => startTransition(action)}>
          {pending ? <LoadingSpinner /> : 'Create Post'}
        </button>
      )
    }
[/code]

### 새로 고침하기[](https://nextjs.org/docs/app/getting-started/updating-data#refreshing)

변경 작업 후 최신 데이터를 표시하기 위해 현재 페이지를 새로 고칠 수 있습니다. Server Action에서 `next/cache`의 [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh)를 호출하면 됩니다.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { refresh } from 'next/cache'
     
    export async function updatePost(formData: FormData) {
      // Update data
      // ...
     
      refresh()
    }
[/code]

이 함수는 클라이언트 라우터를 새로 고쳐 UI가 최신 상태를 반영하도록 합니다. `refresh()` 함수는 태그된 데이터를 다시 검증하지 않습니다. 태그된 데이터를 다시 검증하려면 [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) 또는 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용하세요.

### 다시 검증하기[](https://nextjs.org/docs/app/getting-started/updating-data#revalidating)

업데이트를 수행한 후 Server Function 내에서 [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) 또는 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 호출해 Next.js 캐시를 다시 검증하고 업데이트된 데이터를 표시할 수 있습니다.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    import { revalidatePath } from 'next/cache'
     
    export async function createPost(formData: FormData) {
      'use server'
      // Update data
      // ...
     
      revalidatePath('/posts')
    }
[/code]

### 리디렉션하기[](https://nextjs.org/docs/app/getting-started/updating-data#redirecting)

업데이트 후 사용자를 다른 페이지로 리디렉션하고 싶다면 Server Function 내에서 [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect)를 호출하세요.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidatePath } from 'next/cache'
    import { redirect } from 'next/navigation'
     
    export async function createPost(formData: FormData) {
      // Update data
      // ...
     
      revalidatePath('/posts')
      redirect('/posts')
    }
[/code]

`redirect`를 호출하면 프레임워크가 처리하는 제어 흐름 예외가 [발생](https://nextjs.org/docs/app/api-reference/functions/redirect#behavior)하므로, 그 이후의 코드는 실행되지 않습니다. 최신 데이터가 필요하면 먼저 [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) 또는 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 호출하세요.

### 쿠키[](https://nextjs.org/docs/app/getting-started/updating-data#cookies)

Server Action 내부에서 [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API를 사용해 쿠키를 `get`, `set`, `delete`할 수 있습니다.

Server Action에서 쿠키를 [설정하거나 삭제](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-functions)하면 Next.js가 현재 페이지와 해당 레이아웃을 서버에서 다시 렌더링하여 **UI가 새로운 쿠키 값을 반영**하도록 합니다.

> **알아두면 좋아요** : 서버 업데이트는 현재 React 트리에 적용되어 필요에 따라 컴포넌트를 다시 렌더링하거나 마운트/언마운트합니다. 다시 렌더링된 컴포넌트의 클라이언트 상태는 유지되며, 의존성이 변경되면 effect가 다시 실행됩니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function exampleAction() {
      const cookieStore = await cookies()
     
      // Get cookie
      cookieStore.get('name')?.value
     
      // Set cookie
      cookieStore.set('name', 'Delba')
     
      // Delete cookie
      cookieStore.delete('name')
    }
[/code]

### useEffect[](https://nextjs.org/docs/app/getting-started/updating-data#useeffect)

컴포넌트가 마운트되거나 의존성이 변경될 때 서버 액션을 호출하려면 React [`useEffect`](https://react.dev/reference/react/useEffect) 훅을 사용할 수 있습니다. 이는 전역 이벤트에 의존하거나 자동으로 트리거되어야 하는 변경 작업에 유용합니다. 예를 들어 앱 단축키용 `onKeyDown`, 무한 스크롤을 위한 인터섹션 옵저버 훅, 또는 뷰 카운트를 업데이트하기 위해 컴포넌트가 마운트될 때 사용할 수 있습니다:

app/view-count.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { incrementViews } from './actions'
    import { useState, useEffect, useTransition } from 'react'
     
    export default function ViewCount({ initialViews }: { initialViews: number }) {
      const [views, setViews] = useState(initialViews)
      const [isPending, startTransition] = useTransition()
     
      useEffect(() => {
        startTransition(async () => {
          const updatedViews = await incrementViews()
          setViews(updatedViews)
        })
      }, [])
     
      // You can use `isPending` to give users feedback
      return <p>Total Views: {views}</p>
    }
[/code]

사용자에게 피드백을 제공하려면 `isPending`을 사용할 수 있습니다.

## API 레퍼런스

이 페이지에서 언급된 기능에 대해 더 알고 싶다면 API 레퍼런스를 읽어보세요.

### [revalidatePath revalidatePath 함수에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)### [revalidateTag revalidateTag 함수에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)### [redirect redirect 함수에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/functions/redirect)

도움이 되었나요?

지원됨.

보내기
