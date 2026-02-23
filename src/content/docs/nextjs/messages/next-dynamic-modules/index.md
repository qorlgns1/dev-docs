---
title: 'next/dynamic는 동시에 여러 모듈을 로드하는 기능을 더 이상 지원하지 않습니다'
description: '에서 여러 모듈을 한 번에 로드하는 기능이 React 구현( 및 )에 더 가깝게 맞추기 위해 더 이상 지원되지 않습니다.'
---

# `next/dynamic`는 동시에 여러 모듈을 로드하는 기능을 더 이상 지원하지 않습니다 | Next.js

출처 URL: https://nextjs.org/docs/messages/next-dynamic-modules

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)`next/dynamic`는 동시에 여러 모듈을 로드하는 기능을 더 이상 지원하지 않습니다

# `next/dynamic`는 동시에 여러 모듈을 로드하는 기능을 더 이상 지원하지 않습니다

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/next-dynamic-modules#why-this-error-occurred)

`next/dynamic`에서 여러 모듈을 한 번에 로드하는 기능이 React 구현(`React.lazy` 및 `Suspense`)에 더 가깝게 맞추기 위해 더 이상 지원되지 않습니다.

이 동작에 의존하는 코드를 업데이트하는 일은 비교적 간단합니다! 애플리케이션을 마이그레이션할 수 있도록 이전과 이후 예시를 제공했습니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/next-dynamic-modules#possible-ways-to-fix-it)

각 모듈마다 별도의 dynamic 호출을 사용하도록 마이그레이션하세요.

**Before**

example.js
[code]
    import dynamic from 'next/dynamic'

    const HelloBundle = dynamic({
      modules: () => {
        const components = {
          Hello1: () => import('../components/hello1').then((m) => m.default),
          Hello2: () => import('../components/hello2').then((m) => m.default),
        }

        return components
      },
      render: (props, { Hello1, Hello2 }) => (
        <div>
          <h1>{props.title}</h1>
          <Hello1 />
          <Hello2 />
        </div>
      ),
    })

    function DynamicBundle() {
      return <HelloBundle title="Dynamic Bundle" />
    }

    export default DynamicBundle
[/code]

**After**

example.js
[code]
    import dynamic from 'next/dynamic'

    const Hello1 = dynamic(() => import('../components/hello1'))
    const Hello2 = dynamic(() => import('../components/hello2'))

    function HelloBundle({ title }) {
      return (
        <div>
          <h1>{title}</h1>
          <Hello1 />
          <Hello2 />
        </div>
      )
    }

    function DynamicBundle() {
      return <HelloBundle title="Dynamic Bundle" />
    }

    export default DynamicBundle
[/code]
