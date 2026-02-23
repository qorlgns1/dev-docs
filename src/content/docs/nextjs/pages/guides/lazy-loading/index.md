---
title: '가이드: 지연 로딩'
description: 'Next.js의 지연 로딩은 경로를 렌더링하는 데 필요한 JavaScript 양을 줄여 애플리케이션의 초기 로딩 성능을 향상합니다.'
---

# 가이드: 지연 로딩 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/lazy-loading

[Pages Router](https://nextjs.org/docs/pages)[가이드](https://nextjs.org/docs/pages/guides)지연 로딩

페이지 복사

# 클라이언트 컴포넌트와 라이브러리를 지연 로딩하는 방법

마지막 업데이트 2026년 2월 20일

Next.js의 [지연 로딩](https://developer.mozilla.org/docs/Web/Performance/Lazy_loading)은 경로를 렌더링하는 데 필요한 JavaScript 양을 줄여 애플리케이션의 초기 로딩 성능을 향상합니다.

## `next/dynamic`[](https://nextjs.org/docs/pages/guides/lazy-loading#nextdynamic-1)

`next/dynamic`은 [`React.lazy()`](https://react.dev/reference/react/lazy)와 [Suspense](https://react.dev/reference/react/Suspense)의 조합입니다. 점진적 마이그레이션을 허용하기 위해 `app` 및 `pages` 디렉터리에서 동일하게 동작합니다.

아래 예제에서는 `next/dynamic`을 사용하면 헤더 컴포넌트가 페이지의 초기 JavaScript 번들에 포함되지 않습니다. 페이지는 먼저 Suspense `fallback`을 렌더링한 뒤, `Suspense` 경계가 해제되면 `Header` 컴포넌트를 렌더링합니다.
[code]
    import dynamic from 'next/dynamic'
     
    const DynamicHeader = dynamic(() => import('../components/header'), {
      loading: () => <p>Loading...</p>,
    })
     
    export default function Home() {
      return <DynamicHeader />
    }
[/code]

> **알아두면 좋습니다** : `import('path/to/component')`에서는 경로를 명시적으로 작성해야 합니다. 템플릿 문자열이나 변수를 사용할 수 없습니다. 또한 Next.js가 특정 `dynamic()` 호출에 webpack 번들/모듈 ID를 매칭하고 렌더링 전에 미리 로드할 수 있도록 `import()`는 반드시 `dynamic()` 호출 내부에 있어야 합니다. `dynamic()`은 프리로딩이 작동하려면 모듈의 최상위에서 표시되어야 하므로 React 렌더링 내부에서 사용할 수 없으며, 이는 `React.lazy`와 유사합니다.

## 예시[](https://nextjs.org/docs/pages/guides/lazy-loading#examples-1)

### 이름이 있는 export 사용[](https://nextjs.org/docs/pages/guides/lazy-loading#with-named-exports)

이름이 있는 export를 동적 import하려면 [`import()`](https://github.com/tc39/proposal-dynamic-import#example)가 반환하는 [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)에서 해당 export를 반환하면 됩니다:

components/hello.js
[code]
    export function Hello() {
      return <p>Hello!</p>
    }
     
    // pages/index.js
    import dynamic from 'next/dynamic'
     
    const DynamicComponent = dynamic(() =>
      import('../components/hello').then((mod) => mod.Hello)
    )
[/code]

### SSR 없이 사용[](https://nextjs.org/docs/pages/guides/lazy-loading#with-no-ssr)

클라이언트 측에서 컴포넌트를 동적으로 로드하려면 `ssr` 옵션을 사용해 서버 렌더링을 비활성화할 수 있습니다. 외부 종속성이나 컴포넌트가 `window`와 같은 브라우저 API에 의존하는 경우 유용합니다.
[code]
    'use client'
     
    import dynamic from 'next/dynamic'
     
    const DynamicHeader = dynamic(() => import('../components/header'), {
      ssr: false,
    })
[/code]

### 외부 라이브러리와 함께 사용[](https://nextjs.org/docs/pages/guides/lazy-loading#with-external-libraries)

이 예시는 퍼지 검색을 위해 외부 라이브러리 `fuse.js`를 사용합니다. 사용자가 검색 입력에 텍스트를 입력한 후에만 브라우저에서 모듈이 로드됩니다.
[code]
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
[/code]

도움이 되었나요?

지원됨.

보내기
