---
title: '컴포넌트: Form 컴포넌트'
description: '마지막 업데이트 2026년 2월 20일'
---

# 컴포넌트: Form 컴포넌트 | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/components/form

[API 참조](https://nextjs.org/docs/app/api-reference)[컴포넌트](https://nextjs.org/docs/app/api-reference/components)Form 컴포넌트

페이지 복사

# Form 컴포넌트

마지막 업데이트 2026년 2월 20일

`<Form>` 컴포넌트는 HTML `<form>` 요소를 확장해 [로딩 UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading)의 [**사전 가져오기**](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching), 제출 시 **클라이언트 측 내비게이션**, **점진적 향상**을 제공합니다.

URL 검색 매개변수를 업데이트하는 폼에 적합하며, 위 기능을 구현하는 데 필요한 보일러플레이트 코드를 줄여 줍니다.

기본 사용법:

/app/ui/search.tsx

JavaScriptTypeScript
[code]
    import Form from 'next/form'
     
    export default function Page() {
      return (
        <Form action="/search">
          {/* On submission, the input value will be appended to
              the URL, e.g. /search?query=abc */}
          <input name="query" />
          <button type="submit">Submit</button>
        </Form>
      )
    }
[/code]

## 참고[](https://nextjs.org/docs/app/api-reference/components/form#reference)

`<Form>` 컴포넌트의 동작은 `action` prop에 `string`을 전달했는지 `function`을 전달했는지에 따라 달라집니다.

  * `action`이 **문자열**이면 `<Form>`은 **`GET`** 메서드를 사용하는 네이티브 HTML 폼처럼 동작합니다. 폼 데이터는 검색 매개변수 형태로 URL에 인코딩되고, 제출 시 지정된 URL로 이동합니다. 추가로 Next.js는 다음을 수행합니다.
    * 폼이 화면에 나타나면 경로를 [사전 가져오기](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)해 공유 UI(`layout.js`, `loading.js` 등)를 미리 로드하여 더 빠른 내비게이션을 제공합니다.
    * 폼 제출 시 전체 페이지 리로드 대신 [클라이언트 측 내비게이션](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 수행해 공유 UI와 클라이언트 상태를 유지합니다.
  * `action`이 **함수**(Server Action)이면 `<Form>`은 폼 제출 시 해당 액션을 실행하는 [React 폼](https://react.dev/reference/react-dom/components/form)처럼 동작합니다.

### `action` (string) 프로퍼티[](https://nextjs.org/docs/app/api-reference/components/form#action-string-props)

`action`이 문자열일 때 `<Form>` 컴포넌트는 다음 프로퍼티를 지원합니다.

Prop| 예시| 타입| 필수  
---|---|---|---  
`action`| `action="/search"`| `string` (URL 또는 상대 경로)| 예  
`replace`| `replace={false}`| `boolean`| -  
`scroll`| `scroll={true}`| `boolean`| -  
`prefetch`| `prefetch={true}`| `boolean`| -  
  
  * **`action`**: 폼이 제출될 때 이동할 URL 또는 경로입니다.
    * 빈 문자열 `""`을 전달하면 동일한 라우트에서 검색 매개변수만 갱신합니다.
  * **`replace`**: [브라우저 히스토리](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 스택에 새 항목을 추가하지 않고 현재 히스토리 상태를 교체합니다. 기본값은 `false`입니다.
  * **`scroll`**: 내비게이션 중 스크롤 동작을 제어합니다. 기본값은 `true`이며, 새 라우트의 상단으로 스크롤하고 앞/뒤로 탐색할 때 스크롤 위치를 유지합니다.
  * **`prefetch`**: 폼이 사용자 뷰포트에 보여질 때 경로를 사전 가져올지 제어합니다. 기본값은 `true`입니다.

### `action` (function) 프로퍼티[](https://nextjs.org/docs/app/api-reference/components/form#action-function-props)

`action`이 함수일 때 `<Form>` 컴포넌트는 다음 프로퍼티를 지원합니다.

Prop| 예시| 타입| 필수  
---|---|---|---  
`action`| `action={myAction}`| `function` (Server Action)| 예  
  
  * **`action`**: 폼 제출 시 호출되는 Server Action입니다. 자세한 내용은 [React 문서](https://react.dev/reference/react-dom/components/form#props)를 참고하세요.

> **알아두면 좋아요**: `action`이 함수일 때는 `replace`와 `scroll` 프로퍼티가 무시됩니다.

### 주의사항[](https://nextjs.org/docs/app/api-reference/components/form#caveats)

  * **`formAction`**: `<button>`이나 `<input type="submit">` 필드에서 `action` prop을 재정의할 수 있습니다. Next.js는 클라이언트 측 내비게이션을 수행하지만, 이 방식은 사전 가져오기를 지원하지 않습니다.
    * [`basePath`](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)를 사용하는 경우 `formAction` 경로에도 반드시 포함해야 합니다. 예: `formAction="/base-path/search"`.
  * **`key`**: 문자열 `action`에 `key` prop을 전달하는 것은 지원되지 않습니다. 리렌더링이나 변이를 트리거하려면 함수 `action`을 사용하는 것이 좋습니다.

  * **`onSubmit`**: 폼 제출 로직을 처리할 수 있지만, `event.preventDefault()`를 호출하면 지정된 URL로 내비게이션하는 `<Form>` 동작이 덮어씌워집니다.
  * **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: `<Form>` 동작을 대체하므로 지원되지 않습니다.
    * 마찬가지로 `formMethod`, `formEncType`, `formTarget`으로 각각 `method`, `encType`, `target`을 재정의할 수 있으며, 이 경우 네이티브 브라우저 동작으로 돌아갑니다.
    * 이 프로퍼티가 꼭 필요하다면 HTML `<form>` 요소를 사용하세요.
  * **`<input type="file">`**: `action`이 문자열일 때 이 입력 유형을 사용하면 파일 객체 대신 파일 이름을 제출하는 브라우저 동작과 동일하게 작동합니다.

## 예시[](https://nextjs.org/docs/app/api-reference/components/form#examples)

### 검색 결과 페이지로 이동하는 검색 폼[](https://nextjs.org/docs/app/api-reference/components/form#search-form-that-leads-to-a-search-result-page)

경로를 `action`으로 전달해 검색 결과 페이지로 이동하는 검색 폼을 만들 수 있습니다.

/app/page.tsx

JavaScriptTypeScript
[code]
    import Form from 'next/form'
     
    export default function Page() {
      return (
        <Form action="/search">
          <input name="query" />
          <button type="submit">Submit</button>
        </Form>
      )
    }
[/code]

사용자가 입력 필드를 수정한 뒤 폼을 제출하면 폼 데이터가 `/search?query=abc`처럼 검색 매개변수로 URL에 인코딩됩니다.

> **알아두면 좋아요**: `action`에 빈 문자열 `""`을 전달하면 동일한 라우트에서 검색 매개변수만 갱신합니다.

결과 페이지에서는 [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) `page.js` prop을 통해 쿼리를 받아 외부 소스에서 데이터를 가져올 수 있습니다.

/app/search/page.tsx

JavaScriptTypeScript
[code]
    import { getSearchResults } from '@/lib/search'
     
    export default async function SearchPage({
      searchParams,
    }: {
      searchParams: Promise<{ [key: string]: string | string[] | undefined }>
    }) {
      const results = await getSearchResults((await searchParams).query)
     
      return <div>...</div>
    }
[/code]

`<Form>`이 사용자 뷰포트에 들어오면 `/search` 페이지의 공유 UI(`layout.js`, `loading.js` 등)가 사전 가져오기 됩니다. 제출과 동시에 폼은 새 라우트로 즉시 이동하며 결과를 가져오는 동안 로딩 UI를 표시합니다. [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)를 사용해 폴백 UI를 설계할 수 있습니다.

/app/search/loading.tsx

JavaScriptTypeScript
[code]
    export default function Loading() {
      return <div>Loading...</div>
    }
[/code]

공유 UI가 아직 로드되지 않은 경우에 대비해 [`useFormStatus`](https://react.dev/reference/react-dom/hooks/useFormStatus)를 사용해 사용자에게 즉각적인 피드백을 제공할 수 있습니다.

먼저, 폼이 대기 중일 때 로딩 상태를 표시하는 컴포넌트를 만듭니다.

/app/ui/search-button.tsx

JavaScriptTypeScript
[code]
    'use client'
    import { useFormStatus } from 'react-dom'
     
    export default function SearchButton() {
      const status = useFormStatus()
      return (
        <button type="submit">{status.pending ? 'Searching...' : 'Search'}</button>
      )
    }
[/code]

그런 다음 검색 폼 페이지를 업데이트해 `SearchButton` 컴포넌트를 사용합니다.

/app/page.tsx

JavaScriptTypeScript
[code]
    import Form from 'next/form'
    import { SearchButton } from '@/ui/search-button'
     
    export default function Page() {
      return (
        <Form action="/search">
          <input name="query" />
          <SearchButton />
        </Form>
      )
    }
[/code]

### Server Action을 통한 변이[](https://nextjs.org/docs/app/api-reference/components/form#mutations-with-server-actions)

`action` prop에 함수를 전달해 변이를 수행할 수 있습니다.

/app/posts/create/page.tsx

JavaScriptTypeScript
[code]
    import Form from 'next/form'
    import { createPost } from '@/posts/actions'
     
    export default function Page() {
      return (
        <Form action={createPost}>
          <input name="title" />
          {/* ... */}
          <button type="submit">Create Post</button>
        </Form>
      )
    }
[/code]

변이 후에는 새 리소스로 리디렉션하는 경우가 많습니다. `next/navigation`의 [`redirect`](https://nextjs.org/docs/app/guides/redirecting) 함수를 사용해 새 게시물 페이지로 이동할 수 있습니다.

> **알아두면 좋아요**: 폼 제출의 "목적지"는 액션이 실행되어야만 알 수 있으므로, `<Form>`은 공유 UI를 자동으로 사전 가져올 수 없습니다.

/app/posts/actions.ts

JavaScriptTypeScript
[code]
    'use server'
    import { redirect } from 'next/navigation'
     
    export async function createPost(formData: FormData) {
      // Create a new post
      // ...
     
      // Redirect to the new post
      redirect(`/posts/${data.id}`)
    }
[/code]

새 페이지에서는 `params` prop을 사용해 데이터를 가져올 수 있습니다.

/app/posts/[id]/page.tsx

JavaScriptTypeScript
[code]
    import { getPost } from '@/posts/data'
     
    export default async function PostPage({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const data = await getPost(id)
     
      return (
        <div>
          <h1>{data.title}</h1>
          {/* ... */}
        </div>
      )
    }
[/code]

더 많은 예시는 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) 문서를 참고하세요.

도움이 되었나요?

지원됨.

전송
