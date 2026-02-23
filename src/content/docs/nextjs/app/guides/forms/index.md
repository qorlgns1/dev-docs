---
title: '가이드: 폼'
description: 'React Server Actions는 서버에서 실행되는 Server Functions입니다. 서버 및 클라이언트 컴포넌트에서 호출해 폼 제출을 처리할 수 있습니다. 이 가이드는 Server Actions를 사용해 Next.js에서 폼을 만드는 과정을 단계별로 안내합니...'
---

# 가이드: 폼 | Next.js

Source URL: https://nextjs.org/docs/app/guides/forms

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)폼

페이지 복사

# Server Actions로 폼을 만드는 방법

마지막 업데이트: 2026년 2월 20일

React Server Actions는 서버에서 실행되는 [Server Functions](https://react.dev/reference/rsc/server-functions)입니다. 서버 및 클라이언트 컴포넌트에서 호출해 폼 제출을 처리할 수 있습니다. 이 가이드는 Server Actions를 사용해 Next.js에서 폼을 만드는 과정을 단계별로 안내합니다.

## 작동 방식[](https://nextjs.org/docs/app/guides/forms#how-it-works)

React는 HTML [`<form>`](https://developer.mozilla.org/docs/Web/HTML/Element/form) 요소를 확장해 [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action) 속성으로 Server Actions를 호출할 수 있도록 합니다.

폼 안에서 사용하면 함수는 자동으로 [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData/FormData) 객체를 받습니다. 이후 네이티브 [`FormData` 메서드](https://developer.mozilla.org/en-US/docs/Web/API/FormData#instance_methods)를 사용해 데이터를 추출할 수 있습니다:

app/invoices/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      async function createInvoice(formData: FormData) {
        'use server'
     
        const rawFormData = {
          customerId: formData.get('customerId'),
          amount: formData.get('amount'),
          status: formData.get('status'),
        }
     
        // mutate data
        // revalidate the cache
      }
     
      return <form action={createInvoice}>...</form>
    }
[/code]

> **알아두면 좋은 점:** 필드가 많은 폼에서는 JavaScript [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries)를 사용하세요. 예: `const rawFormData = Object.fromEntries(formData)`. 이 객체에는 `$ACTION_` 접두사가 붙은 추가 속성이 포함됩니다.

## 추가 인수 전달[](https://nextjs.org/docs/app/guides/forms#passing-additional-arguments)

폼 필드 외에도 JavaScript [`bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) 메서드를 이용해 Server Function에 추가 인수를 전달할 수 있습니다. 예를 들어 `updateUser` Server Function에 `userId` 인수를 넘기려면 다음과 같이 합니다:

app/client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { updateUser } from './actions'
     
    export function UserProfile({ userId }: { userId: string }) {
      const updateUserWithId = updateUser.bind(null, userId)
     
      return (
        <form action={updateUserWithId}>
          <input type="text" name="name" />
          <button type="submit">Update User Name</button>
        </form>
      )
    }
[/code]

Server Function은 추가 인수로 `userId`를 받습니다:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function updateUser(userId: string, formData: FormData) {}
[/code]

> **알아두면 좋은 점** :
> 
>   * 대안으로 폼의 hidden input 필드에 인수를 전달할 수 있습니다(예: `<input type="hidden" name="userId" value={userId} />`). 하지만 이 값은 렌더링된 HTML의 일부이며 인코딩되지 않습니다.
>   * `bind`는 서버 및 클라이언트 컴포넌트 모두에서 작동하며 점진적 향상을 지원합니다.
> 

## 폼 유효성 검사[](https://nextjs.org/docs/app/guides/forms#form-validation)

폼은 클라이언트 또는 서버에서 검증할 수 있습니다.

  * **클라이언트 측 검증** 의 경우 기본 검증을 위해 `required`, `type="email"`과 같은 HTML 속성을 사용할 수 있습니다.
  * **서버 측 검증** 의 경우 [zod](https://zod.dev/)와 같은 라이브러리를 사용해 폼 필드를 검증할 수 있습니다. 예:



app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { z } from 'zod'
     
    const schema = z.object({
      email: z.string({
        invalid_type_error: 'Invalid Email',
      }),
    })
     
    export default async function createUser(formData: FormData) {
      const validatedFields = schema.safeParse({
        email: formData.get('email'),
      })
     
      // Return early if the form data is invalid
      if (!validatedFields.success) {
        return {
          errors: validatedFields.error.flatten().fieldErrors,
        }
      }
     
      // Mutate data
    }
[/code]

## 검증 오류[](https://nextjs.org/docs/app/guides/forms#validation-errors)

검증 오류나 메시지를 표시하려면 `<form>`을 정의하는 컴포넌트를 클라이언트 컴포넌트로 전환하고 React [`useActionState`](https://react.dev/reference/react/useActionState)를 사용하세요.

`useActionState`를 사용할 때는 Server Function 시그니처가 변경되어 첫 번째 인수로 새 `prevState` 또는 `initialState`를 받습니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { z } from 'zod'
     
    export async function createUser(initialState: any, formData: FormData) {
      const validatedFields = schema.safeParse({
        email: formData.get('email'),
      })
      // ...
    }
[/code]

그런 다음 `state` 객체를 기반으로 오류 메시지를 조건부로 렌더링할 수 있습니다.

app/ui/signup.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState } from 'react'
    import { createUser } from '@/app/actions'
     
    const initialState = {
      message: '',
    }
     
    export function Signup() {
      const [state, formAction, pending] = useActionState(createUser, initialState)
     
      return (
        <form action={formAction}>
          <label htmlFor="email">Email</label>
          <input type="text" id="email" name="email" required />
          {/* ... */}
          <p aria-live="polite">{state?.message}</p>
          <button disabled={pending}>Sign up</button>
        </form>
      )
    }
[/code]

## 대기 상태[](https://nextjs.org/docs/app/guides/forms#pending-states)

[`useActionState`](https://react.dev/reference/react/useActionState) 훅은 `pending` 불리언을 제공하므로, 액션 실행 중 로딩 인디케이터를 표시하거나 제출 버튼을 비활성화할 수 있습니다.

app/ui/signup.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState } from 'react'
    import { createUser } from '@/app/actions'
     
    export function Signup() {
      const [state, formAction, pending] = useActionState(createUser, initialState)
     
      return (
        <form action={formAction}>
          {/* Other form elements */}
          <button disabled={pending}>Sign up</button>
        </form>
      )
    }
[/code]

또는 [`useFormStatus`](https://react.dev/reference/react-dom/hooks/useFormStatus) 훅을 사용해 액션 실행 중 로딩 인디케이터를 표시할 수 있습니다. 이 훅을 사용할 때는 로딩 인디케이터를 렌더링할 별도의 컴포넌트를 만들어야 합니다. 예를 들어 액션이 대기 중일 때 버튼을 비활성화하려면 다음과 같습니다:

app/ui/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useFormStatus } from 'react-dom'
     
    export function SubmitButton() {
      const { pending } = useFormStatus()
     
      return (
        <button disabled={pending} type="submit">
          Sign Up
        </button>
      )
    }
[/code]

그런 다음 `SubmitButton` 컴포넌트를 폼 내부에 중첩시킬 수 있습니다:

app/ui/signup.tsx

JavaScriptTypeScript
[code]
    import { SubmitButton } from './button'
    import { createUser } from '@/app/actions'
     
    export function Signup() {
      return (
        <form action={createUser}>
          {/* Other form elements */}
          <SubmitButton />
        </form>
      )
    }
[/code]

> **알아두면 좋은 점:** React 19에서는 `useFormStatus`가 data, method, action과 같은 추가 키를 반환 객체에 포함합니다. React 19를 사용하지 않는다면 `pending` 키만 제공됩니다.

## 낙관적 업데이트[](https://nextjs.org/docs/app/guides/forms#optimistic-updates)

React [`useOptimistic`](https://react.dev/reference/react/useOptimistic) 훅을 사용하면 서버 함수가 완료될 때까지 기다리지 않고, 먼저 UI를 낙관적으로 업데이트할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useOptimistic } from 'react'
    import { send } from './actions'
     
    type Message = {
      message: string
    }
     
    export function Thread({ messages }: { messages: Message[] }) {
      const [optimisticMessages, addOptimisticMessage] = useOptimistic<
        Message[],
        string
      >(messages, (state, newMessage) => [...state, { message: newMessage }])
     
      const formAction = async (formData: FormData) => {
        const message = formData.get('message') as string
        addOptimisticMessage(message)
        await send(message)
      }
     
      return (
        <div>
          {optimisticMessages.map((m, i) => (
            <div key={i}>{m.message}</div>
          ))}
          <form action={formAction}>
            <input type="text" name="message" />
            <button type="submit">Send</button>
          </form>
        </div>
      )
    }
[/code]

## 중첩된 폼 요소[](https://nextjs.org/docs/app/guides/forms#nested-form-elements)

`<button>`, `<input type="submit">`, `<input type="image">`처럼 `<form>` 내부에 중첩된 요소에서도 Server Actions를 호출할 수 있습니다. 이러한 요소는 `formAction` prop 또는 이벤트 핸들러를 받을 수 있습니다.

이 방식은 하나의 폼 안에서 여러 Server Actions를 호출해야 할 때 유용합니다. 예를 들어 게시물을 게시하는 버튼 외에 초안을 저장하는 전용 `<button>` 요소를 만들 수 있습니다. 자세한 내용은 [React `<form>` 문서](https://react.dev/reference/react-dom/components/form#handling-multiple-submission-types)를 참고하세요.

## 프로그래밍 방식의 폼 제출[](https://nextjs.org/docs/app/guides/forms#programmatic-form-submission)

[`requestSubmit()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit) 메서드를 사용해 프로그래밍 방식으로 폼 제출을 트리거할 수 있습니다. 예를 들어 사용자가 `⌘` + `Enter` 키보드 단축키로 폼을 제출할 때 `onKeyDown` 이벤트를 리스닝할 수 있습니다:

app/entry.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export function Entry() {
      const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
        if (
          (e.ctrlKey || e.metaKey) &&
          (e.key === 'Enter' || e.key === 'NumpadEnter')
        ) {
          e.preventDefault()
          e.currentTarget.form?.requestSubmit()
        }
      }
     
      return (
        <div>
          <textarea name="entry" rows={20} required onKeyDown={handleKeyDown} />
        </div>
      )
    }
[/code]

이렇게 하면 가장 가까운 `<form>` 조상 요소의 제출이 트리거되어 Server Function이 호출됩니다.

도움이 되었나요?

지원됨.

전송
