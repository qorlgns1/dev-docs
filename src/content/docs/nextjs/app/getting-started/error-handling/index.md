---
title: '시작하기: 오류 처리'
description: '오류는 예상된 오류와 처리되지 않은 예외 두 가지 범주로 나눌 수 있습니다. 이 페이지에서는 Next.js 애플리케이션에서 이러한 오류를 처리하는 방법을 설명합니다.'
---

# 시작하기: 오류 처리 | Next.js

소스 URL: https://nextjs.org/docs/app/getting-started/error-handling

[앱 라우터](https://nextjs.org/docs/app)[시작하기](https://nextjs.org/docs/app/getting-started)오류 처리

페이지 복사

# 오류 처리

마지막 업데이트 2026년 2월 20일

오류는 [예상된 오류](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)와 [처리되지 않은 예외](https://nextjs.org/docs/app/getting-started/error-handling#handling-uncaught-exceptions) 두 가지 범주로 나눌 수 있습니다. 이 페이지에서는 Next.js 애플리케이션에서 이러한 오류를 처리하는 방법을 설명합니다.

## 예상된 오류 처리[](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)

예상된 오류는 [서버 측 폼 검증](https://nextjs.org/docs/app/guides/forms)이나 실패한 요청처럼 애플리케이션의 정상 동작 중에 발생할 수 있는 오류입니다. 이러한 오류는 명시적으로 처리하고 클라이언트에 반환해야 합니다.

### Server Functions[](https://nextjs.org/docs/app/getting-started/error-handling#server-functions)

[Server Functions](https://react.dev/reference/rsc/server-functions)에서 예상된 오류를 처리하려면 [`useActionState`](https://react.dev/reference/react/useActionState) 훅을 사용할 수 있습니다.

이러한 오류에 대해서는 `try`/`catch` 블록과 예외 던지기를 피하고, 대신 반환 값으로 모델링하세요.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost(prevState: any, formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      const res = await fetch('https://api.vercel.app/posts', {
        method: 'POST',
        body: { title, content },
      })
      const json = await res.json()
     
      if (!res.ok) {
        return { message: 'Failed to create post' }
      }
    }
[/code]

액션을 `useActionState` 훅에 전달하고 반환된 `state`를 사용해 오류 메시지를 표시할 수 있습니다.

app/ui/form.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState } from 'react'
    import { createPost } from '@/app/actions'
     
    const initialState = {
      message: '',
    }
     
    export function Form() {
      const [state, formAction, pending] = useActionState(createPost, initialState)
     
      return (
        <form action={formAction}>
          <label htmlFor="title">Title</label>
          <input type="text" id="title" name="title" required />
          <label htmlFor="content">Content</label>
          <textarea id="content" name="content" required />
          {state?.message && <p aria-live="polite">{state.message}</p>}
          <button disabled={pending}>Create Post</button>
        </form>
      )
    }
[/code]

### Server Components[](https://nextjs.org/docs/app/getting-started/error-handling#server-components)

Server Component 내부에서 데이터를 가져올 때 응답을 사용해 오류 메시지를 조건부로 렌더링하거나 [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect)할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const res = await fetch(`https://...`)
      const data = await res.json()
     
      if (!res.ok) {
        return 'There was an error.'
      }
     
      return '...'
    }
[/code]

### Not found[](https://nextjs.org/docs/app/getting-started/error-handling#not-found)

라우트 세그먼트에서 [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) 함수를 호출하고 [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) 파일을 사용해 404 UI를 표시할 수 있습니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    import { getPostBySlug } from '@/lib/posts'
     
    export default async function Page({ params }: { params: { slug: string } }) {
      const { slug } = await params
      const post = getPostBySlug(slug)
     
      if (!post) {
        notFound()
      }
     
      return <div>{post.title}</div>
    }
[/code]

app/blog/[slug]/not-found.tsx

JavaScriptTypeScript
[code]
    export default function NotFound() {
      return <div>404 - Page Not Found</div>
    }
[/code]

## 처리되지 않은 예외 처리[](https://nextjs.org/docs/app/getting-started/error-handling#handling-uncaught-exceptions)

처리되지 않은 예외는 정상적인 애플리케이션 흐름에서 발생해서는 안 되는 버그나 문제를 나타내는 예기치 않은 오류입니다. 이러한 오류는 예외를 던져서 처리하고, 오류 경계에서 잡도록 해야 합니다.

### 중첩 오류 경계[](https://nextjs.org/docs/app/getting-started/error-handling#nested-error-boundaries)

Next.js는 오류 경계를 사용해 처리되지 않은 예외를 처리합니다. 오류 경계는 자식 컴포넌트의 오류를 잡고, 충돌한 컴포넌트 트리 대신 폴백 UI를 표시합니다.

라우트 세그먼트 안에 [`error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error) 파일을 추가하고 React 컴포넌트를 export하여 오류 경계를 생성합니다.

app/dashboard/error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components
     
    import { useEffect } from 'react'
     
    export default function ErrorPage({
      error,
      reset,
    }: {
      error: Error & { digest?: string }
      reset: () => void
    }) {
      useEffect(() => {
        // Log the error to an error reporting service
        console.error(error)
      }, [error])
     
      return (
        <div>
          <h2>Something went wrong!</h2>
          <button
            onClick={
              // Attempt to recover by trying to re-render the segment
              () => reset()
            }
          >
            Try again
          </button>
        </div>
      )
    }
[/code]

오류는 가장 가까운 상위 오류 경계로 전파됩니다. 이를 통해 [라우트 계층](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy)의 다양한 수준에 `error.tsx` 파일을 배치해 세밀하게 오류를 처리할 수 있습니다.

오류 경계는 이벤트 핸들러 내부의 오류를 잡지 않습니다. 오류 경계는 [렌더링 중](https://react.dev/reference/react/Component#static-getderivedstatefromerror) 오류를 잡아 **폴백 UI**를 표시하도록 설계되었습니다.

일반적으로 이벤트 핸들러나 async 코드에서 발생하는 오류는 렌더링 이후 실행되기 때문에 오류 경계에서 처리되지 않습니다.

이러한 경우, 오류를 직접 잡고 `useState` 또는 `useReducer`에 저장한 다음 UI를 업데이트해 사용자에게 알리세요.
[code] 
    'use client'
     
    import { useState } from 'react'
     
    export function Button() {
      const [error, setError] = useState(null)
     
      const handleClick = () => {
        try {
          // do some work that might fail
          throw new Error('Exception')
        } catch (reason) {
          setError(reason)
        }
      }
     
      if (error) {
        /* render fallback UI */
      }
     
      return (
        <button type="button" onClick={handleClick}>
          Click me
        </button>
      )
    }
[/code]

`useTransition`의 `startTransition` 안에서 처리되지 않은 오류는 가장 가까운 오류 경계로 전파된다는 점에 유의하세요.
[code] 
    'use client'
     
    import { useTransition } from 'react'
     
    export function Button() {
      const [pending, startTransition] = useTransition()
     
      const handleClick = () =>
        startTransition(() => {
          throw new Error('Exception')
        })
     
      return (
        <button type="button" onClick={handleClick}>
          Click me
        </button>
      )
    }
[/code]

### 전역 오류[](https://nextjs.org/docs/app/getting-started/error-handling#global-errors)

드물지만, [국제화](https://nextjs.org/docs/app/guides/internationalization)를 사용하는 경우에도 루트 앱 디렉터리에 있는 [`global-error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error) 파일로 루트 레이아웃의 오류를 처리할 수 있습니다. 전역 오류 UI는 활성화 시 루트 레이아웃이나 템플릿을 대체하므로 자체 `<html>` 및 `<body>` 태그를 정의해야 합니다.

app/global-error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components
     
    export default function GlobalError({
      error,
      reset,
    }: {
      error: Error & { digest?: string }
      reset: () => void
    }) {
      return (
        // global-error must include html and body tags
        <html>
          <body>
            <h2>Something went wrong!</h2>
            <button onClick={() => reset()}>Try again</button>
          </body>
        </html>
      )
    }
[/code]

## API Reference

API Reference를 읽어 이 페이지에서 언급된 기능을 더 자세히 알아보세요.

### [redirect리디렉션 함수에 대한 API Reference.](https://nextjs.org/docs/app/api-reference/functions/redirect)### [error.jserror.js 특수 파일에 대한 API Reference.](https://nextjs.org/docs/app/api-reference/file-conventions/error)### [notFoundnotFound 함수에 대한 API Reference.](https://nextjs.org/docs/app/api-reference/functions/not-found)### [not-found.jsnot-found.js 파일에 대한 API Reference.](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)

도움이 되었나요?

지원됨.

보내기
