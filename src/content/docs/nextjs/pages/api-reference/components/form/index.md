---
title: '컴포넌트: Form'
description: '컴포넌트는 HTML  요소를 확장해 제출 시 클라이언트 측 내비게이션과 점진적 향상을 제공합니다.'
---

# 컴포넌트: Form | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/form

Copy page

# Form

마지막 업데이트 2026년 2월 20일

`<Form>` 컴포넌트는 HTML `<form>` 요소를 확장해 제출 시 **클라이언트 측 내비게이션**과 **점진적 향상**을 제공합니다.

URL 검색 매개변수를 업데이트하는 폼에 유용하며, 위 동작을 위해 필요한 보일러플레이트 코드를 줄여 줍니다.

기본 사용법:

/ui/search.js

JavaScriptTypeScript
```
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
```

## Reference[](https://nextjs.org/docs/pages/api-reference/components/form#reference)

`<Form>` 컴포넌트의 동작은 `action` 프롭에 `string` 또는 `function`을 전달했는지에 따라 달라집니다.

  * `action`이 **문자열**이면 `<Form>`은 **`GET`** 메서드를 사용하는 네이티브 HTML 폼처럼 동작합니다. 폼 데이터는 URL 검색 매개변수로 인코딩되며, 폼 제출 시 지정된 URL로 이동합니다. 추가로, Next.js는 다음을 수행합니다:
    * 폼 제출 시 전체 페이지 새로고침 대신 [클라이언트 측 내비게이션](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)을 수행해 공유 UI와 클라이언트 상태를 유지합니다.

### `action` (string) Props[](https://nextjs.org/docs/pages/api-reference/components/form#action-string-props)

`action`이 문자열일 때 `<Form>` 컴포넌트는 다음 프롭을 지원합니다:

Prop| Example| Type| Required
---|---|---|---
`action`| `action="/search"`| `string` (URL 또는 상대 경로)| Yes
`replace`| `replace={false}`| `boolean`| -
`scroll`| `scroll={true}`| `boolean`| -

  * **`action`**: 폼이 제출될 때 이동할 URL 또는 경로입니다.
    * 빈 문자열 `""`은 동일한 라우트에서 검색 매개변수만 갱신합니다.
  * **`replace`**: [브라우저 기록](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 스택에 새로운 항목을 푸시하는 대신 현재 기록 상태를 교체합니다. 기본값은 `false`입니다.
  * **`scroll`**: 내비게이션 중 스크롤 동작을 제어합니다. 기본값은 `true`이며, 이는 새 라우트 상단으로 스크롤하고, 앞으로/뒤로 내비게이션 시 스크롤 위치를 유지함을 의미합니다.

### Caveats[](https://nextjs.org/docs/pages/api-reference/components/form#caveats)

  * **`onSubmit`**: 폼 제출 로직을 처리하는 데 사용할 수 있습니다. 다만 `event.preventDefault()`를 호출하면 지정된 URL로 이동하는 등의 `<Form>` 동작이 무시됩니다.
  * **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: `<Form>` 동작을 덮어쓰므로 지원되지 않습니다.
    * 마찬가지로 `formMethod`, `formEncType`, `formTarget`은 각각 `method`, `encType`, `target` 프롭을 덮어쓸 때 사용할 수 있으며, 이를 사용하면 네이티브 브라우저 동작으로 돌아갑니다.
    * 이러한 프롭이 필요하다면 HTML `<form>` 요소를 사용하세요.
  * **`<input type="file">`**: `action`이 문자열일 때 이 입력 타입을 사용하면 파일 객체 대신 파일 이름을 제출하는 브라우저 동작과 동일하게 작동합니다.

Was this helpful?

supported.

Send