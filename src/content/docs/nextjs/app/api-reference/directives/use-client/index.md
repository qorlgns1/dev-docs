---
title: '지시문: use client'
description: '마지막 업데이트 2026년 2월 20일'
---

# 지시문: use client | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/directives/use-client

[API Reference](https://nextjs.org/docs/app/api-reference)[Directives](https://nextjs.org/docs/app/api-reference/directives)use client

페이지 복사

# use client

마지막 업데이트 2026년 2월 20일

`'use client'` 지시문은 **클라이언트 측**에서 렌더링될 컴포넌트의 진입점을 선언하며, 상태 관리, 이벤트 처리, 브라우저 API 접근처럼 클라이언트 측 JavaScript 기능이 필요한 대화형 사용자 인터페이스(UI)를 만들 때 사용해야 합니다. 이는 React 기능입니다.

> **알아 두면 좋아요:**
>
> 모든 Client Component가 있는 파일마다 `'use client'` 지시문을 추가할 필요는 없습니다. Server Component 안에서 직접 렌더링하려는 컴포넌트가 있는 파일에만 추가하면 됩니다. `'use client'` 지시문은 클라이언트-서버 [경계](https://nextjs.org/docs/app/building-your-application/rendering#network-boundary)를 정의하며, 해당 파일에서 export된 컴포넌트는 클라이언트에 대한 진입점 역할을 합니다.

## 사용 방법[](https://nextjs.org/docs/app/api-reference/directives/use-client#usage)

Client Component의 진입점을 선언하려면 `'use client'` 지시문을 **파일 최상단**에, 어떤 import보다도 먼저 추가하세요:

app/components/counter.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useState } from 'react'
     
    export default function Counter() {
      const [count, setCount] = useState(0)
     
      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
      )
    }
[/code]

`'use client'` 지시문을 사용할 때 Client Component의 props는 [직렬화 가능](https://react.dev/reference/rsc/use-client#serializable-types)해야 합니다. 즉, 서버에서 클라이언트로 데이터를 보낼 때 React가 직렬화할 수 있는 형식이어야 합니다.

app/components/counter.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function Counter({
      onClick /* ❌ Function is not serializable */,
    }) {
      return (
        <div>
          <button onClick={onClick}>Increment</button>
        </div>
      )
    }
[/code]

## Server Component 안에 Client Component 중첩하기[](https://nextjs.org/docs/app/api-reference/directives/use-client#nesting-client-components-within-server-components)

Server Component와 Client Component를 조합하면 성능과 상호작용성을 모두 갖춘 애플리케이션을 만들 수 있습니다:

  1. **Server Components**: 정적 콘텐츠, 데이터 패칭, SEO 친화적 요소에 사용합니다.
  2. **Client Components**: 상태, 이펙트, 브라우저 API가 필요한 대화형 요소에 사용합니다.
  3. **컴포넌트 합성**: 필요한 경우 Client Component를 Server Component 안에 중첩하여 서버와 클라이언트 로직을 명확히 분리하세요.

다음 예시에서:

  * `Header`는 정적 콘텐츠를 처리하는 Server Component입니다.
  * `Counter`는 페이지 안에서 상호작용성을 제공하는 Client Component입니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Header from './header'
    import Counter from './counter' // This is a Client Component
     
    export default function Page() {
      return (
        <div>
          <Header />
          <Counter />
        </div>
      )
    }
[/code]

## 참고자료[](https://nextjs.org/docs/app/api-reference/directives/use-client#reference)

`'use client'`에 대한 자세한 내용은 [React 문서](https://react.dev/reference/rsc/use-client)를 참고하세요.

도움이 되었나요?

지원됨.

보내기
