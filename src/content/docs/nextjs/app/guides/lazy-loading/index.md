---
title: '가이드: Lazy Loading'
description: 'Next.js의 Lazy loading은 라우트를 렌더링하는 데 필요한 JavaScript 양을 줄여 애플리케이션의 초기 로딩 성능을 향상시킵니다.'
---

# 가이드: Lazy Loading | Next.js

Source URL: https://nextjs.org/docs/app/guides/lazy-loading

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Lazy Loading

Copy page

# 클라이언트 컴포넌트와 라이브러리를 지연 로드하는 방법

Last updated February 20, 2026

Next.js의 [Lazy loading](https://developer.mozilla.org/docs/Web/Performance/Lazy_loading)은 라우트를 렌더링하는 데 필요한 JavaScript 양을 줄여 애플리케이션의 초기 로딩 성능을 향상시킵니다.

이는 **Client Components**와 임포트한 라이브러리의 로딩을 뒤로 미루고, 실제로 필요할 때만 클라이언트 번들에 포함하도록 해줍니다. 예를 들어, 사용자가 모달을 열기 위해 클릭할 때까지 모달 로딩을 연기할 수 있습니다.

Next.js에서 지연 로딩을 구현하는 방법은 두 가지입니다.

  1. `next/dynamic`과 [Dynamic Imports](https://nextjs.org/docs/app/guides/lazy-loading#nextdynamic)를 사용하는 방법
  2. [`React.lazy()`](https://react.dev/reference/react/lazy)와 [Suspense](https://react.dev/reference/react/Suspense)를 사용하는 방법

기본적으로 Server Components는 자동으로 [코드 분할](https://developer.mozilla.org/docs/Glossary/Code_splitting)되며, [스트리밍](https://nextjs.org/docs/app/api-reference/file-conventions/loading)을 통해 서버에서 클라이언트로 UI 조각을 점진적으로 전송할 수 있습니다. Lazy loading은 Client Components에 적용됩니다.

## `next/dynamic`[](https://nextjs.org/docs/app/guides/lazy-loading#nextdynamic)

`next/dynamic`은 [`React.lazy()`](https://react.dev/reference/react/lazy)와 [Suspense](https://react.dev/reference/react/Suspense)의 조합입니다. 점진적 마이그레이션을 위해 `app` 디렉터리와 `pages` 디렉터리 모두에서 동일하게 동작합니다.

## 예시[](https://nextjs.org/docs/app/guides/lazy-loading#examples)

### Client Components 임포트하기[](https://nextjs.org/docs/app/guides/lazy-loading#importing-client-components)

app/page.js
```
    'use client'

    import { useState } from 'react'
    import dynamic from 'next/dynamic'

    // Client Components:
    const ComponentA = dynamic(() => import('../components/A'))
    const ComponentB = dynamic(() => import('../components/B'))
    const ComponentC = dynamic(() => import('../components/C'), { ssr: false })

    export default function ClientComponentExample() {
      const [showMore, setShowMore] = useState(false)

      return (
        <div>
          {/* Load immediately, but in a separate client bundle */}
          <ComponentA />

          {/* Load on demand, only when/if the condition is met */}
          {showMore && <ComponentB />}
          <button onClick={() => setShowMore(!showMore)}>Toggle</button>

          {/* Load only on the client side */}
          <ComponentC />
        </div>
      )
    }
```

> **참고:** Server Component가 Client Component를 동적으로 임포트할 때는 자동 [코드 분할](https://developer.mozilla.org/docs/Glossary/Code_splitting)이 현재 지원되지 않습니다.

### SSR 건너뛰기[](https://nextjs.org/docs/app/guides/lazy-loading#skipping-ssr)

`React.lazy()`와 Suspense를 사용할 때 Client Components는 기본적으로 [사전 렌더링](https://github.com/reactwg/server-components/discussions/4)(SSR)됩니다.

> **참고:** `ssr: false` 옵션은 Client Components에서만 작동하므로, 클라이언트 코드 분할이 제대로 이루어지도록 해당 옵션을 Client Component로 옮기세요.

Client Component에 대해 사전 렌더링을 비활성화하려면 `ssr` 옵션을 `false`로 설정하면 됩니다.
```
    const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
```

### Server Components 임포트하기[](https://nextjs.org/docs/app/guides/lazy-loading#importing-server-components)

Server Component를 동적으로 임포트하면, 해당 Server Component 자체가 아니라 그 자식인 Client Components만 지연 로드됩니다. 또한 Server Components에서 사용할 때 CSS 같은 정적 자산을 미리 로드하는 데도 도움이 됩니다.

app/page.js
```
    import dynamic from 'next/dynamic'

    // Server Component:
    const ServerComponent = dynamic(() => import('../components/ServerComponent'))

    export default function ServerComponentExample() {
      return (
        <div>
          <ServerComponent />
        </div>
      )
    }
```

> **참고:** Server Components에서는 `ssr: false` 옵션을 지원하지 않습니다. Server Components에서 사용하려 하면 오류가 발생합니다. `next/dynamic`을 사용할 때 `ssr: false`는 Client Component에서만 허용됩니다.

### 외부 라이브러리 로딩하기[](https://nextjs.org/docs/app/guides/lazy-loading#loading-external-libraries)

외부 라이브러리는 [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) 함수를 통해 필요할 때 로드할 수 있습니다. 다음 예시는 퍼지 검색을 위해 외부 라이브러리 `fuse.js`를 사용하며, 사용자가 검색 입력란에 값을 입력한 후에야 클라이언트에서 모듈이 로드됩니다.

app/page.js
```
    'use client'

    import { useState } from 'react'

    const names = ['Tim', 'Joe', 'Bel', 'Lee']

    export default function Page() {
      const [results, setResults] = useState()

      return (
        <div>
          <input
            type="text"
            placeholder="Search"
            onChange={async (e) => {
              const { value } = e.currentTarget
              // Dynamically load fuse.js
              const Fuse = (await import('fuse.js')).default
              const fuse = new Fuse(names)

              setResults(fuse.search(value))
            }}
          />
          <pre>Results: {JSON.stringify(results, null, 2)}</pre>
        </div>
      )
    }
```

### 사용자 정의 로딩 컴포넌트 추가하기[](https://nextjs.org/docs/app/guides/lazy-loading#adding-a-custom-loading-component)

app/page.js
```
    'use client'

    import dynamic from 'next/dynamic'

    const WithCustomLoading = dynamic(
      () => import('../components/WithCustomLoading'),
      {
        loading: () => <p>Loading...</p>,
      }
    )

    export default function Page() {
      return (
        <div>
          {/* The loading component will be rendered while  <WithCustomLoading/> is loading */}
          <WithCustomLoading />
        </div>
      )
    }
```

### Named Export 임포트하기[](https://nextjs.org/docs/app/guides/lazy-loading#importing-named-exports)

Named export를 동적으로 임포트하려면 [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) 함수가 반환하는 Promise에서 해당 export를 반환하면 됩니다.

components/hello.js
```
    'use client'

    export function Hello() {
      return <p>Hello!</p>
    }
```

app/page.js
```
    import dynamic from 'next/dynamic'

    const ClientComponent = dynamic(() =>
      import('../components/hello').then((mod) => mod.Hello)
    )
```

Was this helpful?

supported.

Send