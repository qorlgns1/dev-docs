---
title: '함수: useRouter'
description: '원본 URL: https://nextjs.org/docs/pages/api-reference/functions/use-router'
---

# 함수: useRouter | Next.js

원본 URL: https://nextjs.org/docs/pages/api-reference/functions/use-router

# useRouter

마지막 업데이트 2026년 2월 20일

앱의 어떤 함수 컴포넌트 안에서도 [`router` 객체](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)에 접근하고 싶다면 `useRouter` 훅을 사용할 수 있습니다. 아래 예제를 확인하세요:
```
    import { useRouter } from 'next/router'

    function ActiveLink({ children, href }) {
      const router = useRouter()
      const style = {
        marginRight: 10,
        color: router.asPath === href ? 'red' : 'black',
      }

      const handleClick = (e) => {
        e.preventDefault()
        router.push(href)
      }

      return (
        <a href={href} onClick={handleClick} style={style}>
          {children}
        </a>
      )
    }

    export default ActiveLink
```

> `useRouter`는 [React Hook](https://react.dev/learn#using-hooks)이므로 클래스와 함께 사용할 수 없습니다. [withRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)를 사용하거나 클래스를 함수 컴포넌트로 감싸세요.

## `router` 객체[](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)

다음은 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#top)와 [`withRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)가 반환하는 `router` 객체 정의입니다.

  * `pathname`: `String` \- `/pages` 뒤에 오는 현재 라우트 파일의 경로입니다. 따라서 `basePath`, `locale`, 그리고 끝 슬래시(`trailingSlash: true`)는 포함되지 않습니다.
  * `query`: `Object` \- [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) 매개변수를 포함해 객체로 파싱된 쿼리 문자열입니다. 페이지가 [Server-side Rendering](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)을 사용하지 않는다면 프리렌더링 중에는 빈 객체입니다. 기본값은 `{}`입니다.
  * `asPath`: `String` \- 검색 매개변수를 포함하고 `trailingSlash` 설정을 따르는, 브라우저에 표시되는 경로입니다. `basePath`와 `locale`은 포함되지 않습니다.
  * `isFallback`: `boolean` \- 현재 페이지가 [fallback 모드](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)에 있는지 여부입니다.
  * `basePath`: `String` \- 활성화된 [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) (설정된 경우)입니다.
  * `locale`: `String` \- 활성 로케일(설정된 경우)입니다.
  * `locales`: `String[]` \- 지원되는 모든 로케일(설정된 경우)입니다.
  * `defaultLocale`: `String` \- 현재 기본 로케일(설정된 경우)입니다.
  * `domainLocales`: `Array<{domain, defaultLocale, locales}>` \- 구성된 도메인 로케일입니다.
  * `isReady`: `boolean` \- 라우터 필드가 클라이언트 측에서 업데이트되어 사용할 준비가 되었는지 여부입니다. 서버에서 조건부 렌더링하는 용도가 아니라 `useEffect` 내부에서만 사용해야 합니다. [자동 정적 최적화 페이지](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 사례를 참고하세요.
  * `isPreview`: `boolean` \- 애플리케이션이 현재 [미리 보기 모드](https://nextjs.org/docs/pages/guides/preview-mode)에 있는지 여부입니다.

> 페이지를 서버 사이드 렌더링 또는 [자동 정적 최적화](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)로 렌더링하는 경우 `asPath` 필드를 사용하면 클라이언트와 서버 사이의 불일치가 발생할 수 있습니다. `isReady` 필드가 `true`가 될 때까지 `asPath` 사용을 피하세요.

`router`에는 다음 메서드가 포함되어 있습니다.

### router.push[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush)

클라이언트 측 전환을 처리하며, [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link)만으로 충분하지 않은 상황에서 유용합니다.
```
    router.push(url, as, options)
```

  * `url`: `UrlObject | String` \- 이동할 URL입니다. `UrlObject` 속성은 [Node.js URL 모듈 문서](https://nodejs.org/api/url.html#legacy-urlobject)를 참고하세요.
  * `as`: `UrlObject | String` \- 브라우저 URL 표시줄에 나타날 경로에 대한 선택적 데코레이터입니다. Next.js 9.5.3 이전에는 동적 라우트를 위해 사용했습니다.
  * `options` \- 다음 설정을 포함할 수 있는 선택적 객체입니다.
    * `scroll` \- 선택적 boolean으로, 내비게이션 이후 페이지 맨 위로 스크롤할지를 제어합니다. 기본값은 `true`입니다.
    * [`shallow`](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#shallow-routing): [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)를 다시 실행하지 않고 현재 페이지의 경로만 업데이트합니다. 기본값은 `false`입니다.
    * `locale` \- 선택적 문자열로, 새 페이지의 로케일을 지정합니다.

> 외부 URL에는 `router.push`를 사용할 필요가 없습니다. 그런 경우에는 [window.location](https://developer.mozilla.org/docs/Web/API/Window/location)이 더 적합합니다.

사전에 정의된 라우트인 `pages/about.js`로 이동하기:
```
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.push('/about')}>
          Click me
        </button>
      )
    }
```

동적 라우트인 `pages/post/[pid].js`로 이동하기:
```
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.push('/post/abc')}>
          Click me
        </button>
      )
    }
```

[인증](https://nextjs.org/docs/pages/guides/authentication)이 필요한 페이지에서 사용자를 `pages/login.js`로 리디렉션하기:
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    // Here you would fetch and return the user
    const useUser = () => ({ user: null, loading: false })

    export default function Page() {
      const { user, loading } = useUser()
      const router = useRouter()

      useEffect(() => {
        if (!(user || loading)) {
          router.push('/login')
        }
      }, [user, loading])

      return <p>Redirecting...</p>
    }
```

#### 내비게이션 후 상태 초기화[](https://nextjs.org/docs/pages/api-reference/functions/use-router#resetting-state-after-navigation)

Next.js에서 동일한 페이지로 이동할 때는 기본적으로 페이지 상태가 **초기화되지 않습니다**. 부모 컴포넌트가 변경되지 않는 한 React가 언마운트하지 않기 때문입니다.

pages/[slug].js
```
    import Link from 'next/link'
    import { useState } from 'react'
    import { useRouter } from 'next/router'

    export default function Page(props) {
      const router = useRouter()
      const [count, setCount] = useState(0)
      return (
        <div>
          <h1>Page: {router.query.slug}</h1>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increase count</button>
          <Link href="/one">one</Link> <Link href="/two">two</Link>
        </div>
      )
    }
```

위 예제에서 `/one`과 `/two` 사이를 이동하더라도 카운트는 **초기화되지 않습니다**. 최상위 React 컴포넌트인 `Page`가 동일하기 때문에 `useState`가 렌더 사이에 유지됩니다.

이 동작을 원하지 않는다면 다음과 같은 선택지가 있습니다.

  * `useEffect`를 사용해 각 상태가 갱신되도록 수동으로 보장합니다. 위 예제에서는 다음과 같이 작성할 수 있습니다.
```
useEffect(() => {
          setCount(0)
        }, [router.query.slug])
```

  * React `key`를 사용해 [React가 컴포넌트를 다시 마운트하도록](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key) 지시합니다. 모든 페이지에 이 동작을 적용하려면 커스텀 앱을 사용할 수 있습니다.

pages/_app.js
```
import { useRouter } from 'next/router'

        export default function MyApp({ Component, pageProps }) {
          const router = useRouter()
          return <Component key={router.asPath} {...pageProps} />
        }
```

#### URL 객체 사용[](https://nextjs.org/docs/pages/api-reference/functions/use-router#with-url-object)

[`next/link`](https://nextjs.org/docs/pages/api-reference/components/link#passing-a-url-object)에 URL 객체를 전달하는 것과 동일한 방식으로 사용할 수 있습니다. `url`과 `as` 매개변수 모두에서 동작합니다.
```
    import { useRouter } from 'next/router'

    export default function ReadMore({ post }) {
      const router = useRouter()

      return (
        <button
          type="button"
          onClick={() => {
            router.push({
              pathname: '/post/[pid]',
              query: { pid: post.id },
            })
          }}
        >
          Click here to read more
        </button>
      )
    }
```

### router.replace[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerreplace)

[`next/link`](https://nextjs.org/docs/pages/api-reference/components/link)의 `replace` prop과 유사하게, `router.replace`는 `history` 스택에 새로운 URL 항목을 추가하지 않습니다.
```
    router.replace(url, as, options)
```

  * `router.replace`의 API는 [`router.push`](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush)와 완전히 동일합니다.

다음 예제를 살펴보세요.
```
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.replace('/home')}>
          Click me
        </button>
      )
    }
```

### router.prefetch[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerprefetch)

더 빠른 클라이언트 측 전환을 위해 페이지를 사전 가져옵니다. 이 메서드는 [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) 없이 내비게이션할 때만 유용하며, `next/link`는 페이지 사전 가져오기를 자동으로 처리합니다.

> 이는 프로덕션 전용 기능입니다. Next.js는 개발 환경에서 페이지를 사전 가져오지 않습니다.
```
    router.prefetch(url, as, options)
```

  * `url` \- `/dashboard` 같은 명시적 라우트와 `/product/[id]` 같은 동적 라우트를 포함해 사전 가져올 URL입니다.
  * `as` \- `url`에 대한 선택적 데코레이터입니다. Next.js 9.5.3 이전에는 동적 라우트를 사전 가져오기 위해 사용했습니다.
  * `options` \- 다음 필드를 허용하는 선택적 객체입니다.
    * `locale` \- 활성 로케일과 다른 로케일을 제공할 수 있습니다. `false`이면 `url`에 로케일을 포함해야 하며, 활성 로케일은 사용되지 않습니다.

로그인 페이지가 있고 로그인 후 사용자에게 대시보드를 보여준다고 가정해 보겠습니다. 다음 예시처럼 대시보드를 사전 가져오면 더 빠르게 전환할 수 있습니다.
```
    import { useCallback, useEffect } from 'react'
    import { useRouter } from 'next/router'

    export default function Login() {
      const router = useRouter()
      const handleSubmit = useCallback((e) => {
        e.preventDefault()

        fetch('/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            /* Form data */
          }),
        }).then((res) => {
          // Do a fast client-side transition to the already prefetched dashboard page
          if (res.ok) router.push('/dashboard')
        })
      }, [])

      useEffect(() => {
```

// Prefetch the dashboard page
        router.prefetch('/dashboard')
      }, [router])

      return (
        <form onSubmit={handleSubmit}>
          {/* Form fields */}
          <button type="submit">Login</button>
        </form>
      )
    }

### router.beforePopState[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerbeforepopstate)

일부 경우(예: [Custom Server](https://nextjs.org/docs/pages/guides/custom-server)를 사용하는 경우)에는 [popstate](https://developer.mozilla.org/docs/Web/API/Window/popstate_event) 이벤트를 수신하고 라우터가 이를 처리하기 전에 작업을 수행하고 싶을 수 있습니다.
```
    router.beforePopState(cb)
```

  * `cb` \- 들어오는 `popstate` 이벤트에서 실행할 함수입니다. 이 함수는 다음 속성을 가진 객체 형태로 이벤트의 상태를 전달받습니다:
    * `url`: `String` \- 새 상태에 대한 라우트로, 일반적으로 `page` 이름입니다.
    * `as`: `String` \- 브라우저에 표시될 URL입니다.
    * `options`: `Object` \- [router.push](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerpush)에서 전달된 추가 옵션입니다.

`cb`가 `false`를 반환하면 Next.js 라우터는 `popstate`를 처리하지 않으므로, 해당 상황을 직접 처리해야 합니다. 자세한 내용은 [파일 시스템 라우팅 비활성화](https://nextjs.org/docs/pages/guides/custom-server#disabling-file-system-routing)를 참고하세요.

다음 예시처럼 요청을 조작하거나 SSR 새로고침을 강제하기 위해 `beforePopState`를 사용할 수 있습니다:
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      useEffect(() => {
        router.beforePopState(({ url, as, options }) => {
          // I only want to allow these two routes!
          if (as !== '/' && as !== '/other') {
            // Have SSR render bad routes as a 404.
            window.location.href = as
            return false
          }

          return true
        })
      }, [router])

      return <p>Welcome to the page</p>
    }
```

### router.back[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerback)

히스토리에서 뒤로 이동합니다. 브라우저의 뒤로 가기 버튼을 클릭하는 것과 동일하며 `window.history.back()`을 실행합니다.
```
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.back()}>
          Click here to go back
        </button>
      )
    }
```

### router.reload[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerreload)

현재 URL을 다시 로드합니다. 브라우저의 새로고침 버튼을 클릭하는 것과 동일하며 `window.location.reload()`를 실행합니다.
```
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()

      return (
        <button type="button" onClick={() => router.reload()}>
          Click here to reload
        </button>
      )
    }
```

### router.events[](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerevents)

Next.js Router 내부에서 발생하는 다양한 이벤트를 수신할 수 있습니다. 지원되는 이벤트 목록은 다음과 같습니다:

  * `routeChangeStart(url, { shallow })` \- 라우트 변경이 시작될 때 발생
  * `routeChangeComplete(url, { shallow })` \- 라우트 변경이 완료되면 발생
  * `routeChangeError(err, url, { shallow })` \- 라우트를 변경하거나 로드하는 중 오류가 발생하거나 라우트 로드가 취소되면 발생
    * `err.cancelled` \- 탐색이 취소되었는지 나타냅니다.
  * `beforeHistoryChange(url, { shallow })` \- 브라우저 히스토리를 변경하기 전에 발생
  * `hashChangeStart(url, { shallow })` \- 페이지는 그대로 두고 해시가 바뀌려 할 때 발생
  * `hashChangeComplete(url, { shallow })` \- 페이지는 그대로 두고 해시가 변경된 뒤 발생

> **알아두면 좋아요**: 여기서 `url`은 [`basePath`](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)를 포함한 브라우저에 표시되는 URL입니다.

예를 들어 `routeChangeStart` 이벤트를 수신하려면 `pages/_app.js`를 열거나 생성하고 다음과 같이 이벤트에 구독하세요:
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    export default function MyApp({ Component, pageProps }) {
      const router = useRouter()

      useEffect(() => {
        const handleRouteChange = (url, { shallow }) => {
          console.log(
            `App is changing to ${url} ${
              shallow ? 'with' : 'without'
            } shallow routing`
          )
        }

        router.events.on('routeChangeStart', handleRouteChange)

        // If the component is unmounted, unsubscribe
        // from the event with the `off` method:
        return () => {
          router.events.off('routeChangeStart', handleRouteChange)
        }
      }, [router])

      return <Component {...pageProps} />
    }
```

> 이 예시에서는 페이지 이동 시 언마운트되지 않는 [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)(`pages/_app.js`)을 사용해 이벤트에 구독하지만, 애플리케이션의 어떤 컴포넌트에서도 라우터 이벤트를 구독할 수 있습니다.

라우터 이벤트는 컴포넌트가 마운트될 때([useEffect](https://react.dev/reference/react/useEffect) 또는 [componentDidMount](https://react.dev/reference/react/Component#componentdidmount) / [componentWillUnmount](https://react.dev/reference/react/Component#componentwillunmount)) 등록하거나, 특정 이벤트가 발생했을 때 명령형으로 등록해야 합니다.

라우트 로드가 취소되면(예: 연속으로 두 개의 링크를 빠르게 클릭하는 경우) `routeChangeError`가 발생하며, 전달되는 `err`에는 `cancelled` 속성이 `true`로 설정됩니다. 다음 예시를 참고하세요:
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    export default function MyApp({ Component, pageProps }) {
      const router = useRouter()

      useEffect(() => {
        const handleRouteChangeError = (err, url) => {
          if (err.cancelled) {
            console.log(`Route to ${url} was cancelled!`)
          }
        }

        router.events.on('routeChangeError', handleRouteChangeError)

        // If the component is unmounted, unsubscribe
        // from the event with the `off` method:
        return () => {
          router.events.off('routeChangeError', handleRouteChangeError)
        }
      }, [router])

      return <Component {...pageProps} />
    }
```

## The `next/compat/router` export[](https://nextjs.org/docs/pages/api-reference/functions/use-router#the-nextcompatrouter-export)

동일한 `useRouter` 훅이지만 `app`과 `pages` 디렉터리 모두에서 사용할 수 있습니다.

`next/router`와 달리 페이지 라우터가 마운트되지 않았을 때 오류를 던지지 않고, 반환 타입이 `NextRouter | null`입니다. 이를 통해 개발자는 `app` 라우터로 전환하는 동안 컴포넌트를 변환하여 `app`과 `pages` 양쪽에서 실행하도록 만들 수 있습니다.

기존 컴포넌트가 다음과 같았다면:
```
    import { useRouter } from 'next/router'
    const MyComponent = () => {
      const { isReady, query } = useRouter()
      // ...
    }
```

`null`은 비구조화할 수 없으므로 이를 `next/compat/router`로 변환하면 오류가 발생합니다. 대신 개발자는 새로운 훅을 활용할 수 있습니다:
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/compat/router'
    import { useSearchParams } from 'next/navigation'
    const MyComponent = () => {
      const router = useRouter() // may be null or a NextRouter instance
      const searchParams = useSearchParams()
      useEffect(() => {
        if (router && !router.isReady) {
          return
        }
        // In `app/`, searchParams will be ready immediately with the values, in
        // `pages/` it will be available after the router is ready.
        const search = searchParams.get('search')
        // ...
      }, [router, searchParams])
      // ...
    }
```

이제 해당 컴포넌트는 `pages`와 `app` 디렉터리 모두에서 동작합니다. 컴포넌트가 더 이상 `pages`에서 사용되지 않으면 compat router에 대한 참조를 제거할 수 있습니다:
```
    import { useSearchParams } from 'next/navigation'
    const MyComponent = () => {
      const searchParams = useSearchParams()
      // As this component is only used in `app/`, the compat router can be removed.
      const search = searchParams.get('search')
      // ...
    }
```

### Using `useRouter` outside of Next.js context in pages[](https://nextjs.org/docs/pages/api-reference/functions/use-router#using-userouter-outside-of-nextjs-context-in-pages)

또 다른 구체적인 사용 사례는 `pages` 디렉터리의 `getServerSideProps` 내부처럼 Next.js 애플리케이션 컨텍스트 외부에서 컴포넌트를 렌더링하는 경우입니다. 이때 compat router를 사용하면 오류를 방지할 수 있습니다:
```
    import { renderToString } from 'react-dom/server'
    import { useRouter } from 'next/compat/router'
    const MyComponent = () => {
      const router = useRouter() // may be null or a NextRouter instance
      // ...
    }
    export async function getServerSideProps() {
      const renderedComponent = renderToString(<MyComponent />)
      return {
        props: {
          renderedComponent,
        },
      }
    }
```

## Potential ESLint errors[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-eslint-errors)

`router` 객체에서 접근 가능한 특정 메서드는 Promise를 반환합니다. ESLint 규칙 [no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises)를 활성화했다면, 이를 전역에서 또는 영향을 받는 줄에 대해 비활성화하는 것을 고려하세요.

애플리케이션에서 이 규칙이 꼭 필요하다면 Promise에 `void`를 적용하거나, `async` 함수를 사용해 Promise를 `await`한 뒤 함수 호출에 `void`를 적용해야 합니다. **이 규칙은 `onClick` 핸들러 내부에서 메서드를 호출하는 경우에는 해당되지 않습니다.**

영향을 받는 메서드는 다음과 같습니다:

  * `router.push`
  * `router.replace`
  * `router.prefetch`

### Potential solutions[](https://nextjs.org/docs/pages/api-reference/functions/use-router#potential-solutions)
```
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    // Here you would fetch and return the user
    const useUser = () => ({ user: null, loading: false })

    export default function Page() {
      const { user, loading } = useUser()
      const router = useRouter()

      useEffect(() => {
        // disable the linting on the next line - This is the cleanest solution
        // eslint-disable-next-line no-floating-promises
        router.push('/login')

        // void the Promise returned by router.push
        if (!(user || loading)) {
          void router.push('/login')
        }
        // or use an async function, await the Promise, then void the function call
        async function handleRouteChange() {
          if (!(user || loading)) {
            await router.push('/login')
          }
        }
        void handleRouteChange()
      }, [user, loading])

      return <p>Redirecting...</p>
    }
```

## withRouter[](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)

[`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)가 최선의 선택이 아니라면, `withRouter`를 사용하여 동일한 [`router` 객체](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)를 어떤 컴포넌트에도 주입할 수 있습니다.

### Usage[](https://nextjs.org/docs/pages/api-reference/functions/use-router#usage)
```
    import { withRouter } from 'next/router'

    function Page({ router }) {
      return <p>{router.pathname}</p>
    }

    export default withRouter(Page)
```

### TypeScript[](https://nextjs.org/docs/pages/api-reference/functions/use-router#typescript)

클래스 컴포넌트를 `withRouter`와 함께 사용하려면, 컴포넌트가 router prop을 받아야 합니다:
```
    import React from 'react'
    import { withRouter, NextRouter } from 'next/router'

    interface WithRouterProps {
      router: NextRouter
    }

    interface MyComponentProps extends WithRouterProps {}

    class MyComponent extends React.Component<MyComponentProps> {
      render() {
        return <p>{this.props.router.pathname}</p>
      }
    }

    export default withRouter(MyComponent)
```

보내기