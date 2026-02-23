---
title: '동적 API는 비동기입니다'
description: '특정 API에 동기적으로 접근하면 이제 경고가 발생하는 이유를 살펴보세요.'
---

# 동적 API는 비동기입니다 | Next.js

출처 URL: https://nextjs.org/docs/messages/sync-dynamic-apis

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)동적 API는 비동기입니다

# 동적 API는 비동기입니다

특정 API에 동기적으로 접근하면 이제 경고가 발생하는 이유를 살펴보세요.

## 경고가 발생한 이유[](https://nextjs.org/docs/messages/sync-dynamic-apis#why-this-warning-occurred)

코드 어딘가에서 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)을 선택한 API를 사용했습니다.

동적 API에는 다음이 포함됩니다:

  * 페이지, 레이아웃, 메타데이터 API, 라우트 핸들러에 제공되는 `params` 및 `searchParams` props
  * `next/headers`의 `cookies()`, `draftMode()`, `headers()`

Next 15에서는 이러한 API가 비동기화되었습니다. 자세한 내용은 Next.js 15 [업그레이드 가이드](https://nextjs.org/docs/app/guides/upgrading/version-15)를 참고하세요.

예를 들어, 다음 코드는 경고를 발생시킵니다:

app/[id]/page.js
[code]
    function Page({ params }) {
      // direct access of `params.id`.
      return <p>ID: {params.id}</p>
    }
[/code]

여기에는 이러한 API의 반환값을 열거(예: `{...params}` 또는 `Object.keys(params)`)하거나 반복(예: `[...headers()]`, `for (const cookie of cookies())`, `cookies()[Symbol.iterator]()` 호출)하는 경우도 포함됩니다.

## 해결 가능한 방법[](https://nextjs.org/docs/messages/sync-dynamic-apis#possible-ways-to-fix-it)

[`next-async-request-api` 코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#next-async-request-api)는 이러한 사례의 상당수를 자동으로 고쳐줍니다:

Terminal
[code]
    npx @next/codemod@canary next-async-request-api .
[/code]

코드모드가 모든 경우를 처리할 수 있는 것은 아니므로 일부 코드는 수동으로 조정해야 합니다.

경고가 서버(예: 라우트 핸들러나 서버 컴포넌트)에서 발생했다면, 해당 동적 API를 `await`하여 속성에 접근해야 합니다:

app/[id]/page.js
[code]
    async function Page({ params }) {
      // asynchronous access of `params.id`.
      const { id } = await params
      return <p>ID: {id}</p>
    }
[/code]

경고가 동기 컴포넌트(예: 클라이언트 컴포넌트)에서 발생했다면, 먼저 `React.use()`로 Promise를 해제해야 합니다:

app/[id]/page.js
[code]
    'use client'
    import * as React from 'react'
     
    function Page({ params }) {
      // asynchronous access of `params.id`.
      const { id } = React.use(params)
      return <p>ID: {id}</p>
    }
[/code]

### 마이그레이션할 수 없는 사례[](https://nextjs.org/docs/messages/sync-dynamic-apis#unmigratable-cases)

코드모드가 마이그레이션할 수 없는 항목을 발견하면 `@next-codemod-error` 접두사가 포함된 주석과 권장 조치를 남깁니다. 예를 들어, 이 경우에는 `cookies()` 호출을 수동으로 `await`하고 함수를 async로 변경한 뒤 함수 사용처를 적절히 `await`하도록 리팩터링해야 합니다:
[code] 
    export function MyCookiesComponent() {
      const c =
        /* @next-codemod-error Manually await this call and refactor the function to be async */
        cookies()
      return c.get('name')
    }
[/code]

### 린터로 강제되는 마이그레이션[](https://nextjs.org/docs/messages/sync-dynamic-apis#enforced-migration-with-linter)

코드모드가 남긴 `@next-codemod-error`로 시작하는 주석을 해결하지 않으면, Next.js는 dev와 build 모두에서 오류를 발생시켜 해당 문제를 해결하도록 강제합니다. 변경 사항을 검토하고 주석의 제안을 따르세요. 필요한 수정을 한 뒤 주석을 제거하거나, 수행할 작업이 없다면 `@next-codemod-error` 접두사를 `@next-codemod-ignore`로 바꿔 빌드 오류를 우회할 수 있습니다.
[code] 
    - /* @next-codemod-error <suggested message> */
    + /* @next-codemod-ignore */
[/code]

> **알아두면 좋아요** :
> 
> Promise를 해제(`await` 또는 `React.use`)하는 시점을 실제로 값이 필요할 때까지 미룰 수 있습니다. 이렇게 하면 Next.js가 페이지의 더 많은 부분을 정적으로 렌더링할 수 있습니다.

도움이 되었나요?

지원됨.

보내기
