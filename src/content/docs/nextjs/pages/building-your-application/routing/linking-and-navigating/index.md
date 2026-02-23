---
title: '라우팅: 연결 및 내비게이션'
description: 'Next.js 라우터를 사용하면 단일 페이지 애플리케이션과 유사하게 페이지 간 클라이언트 사이드 라우트 전환을 수행할 수 있습니다.'
---

# 라우팅: 연결 및 내비게이션 | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating

[Building Your Application](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Linking and Navigating

# 링크 및 내비게이션

마지막 업데이트 2026년 2월 20일

Next.js 라우터를 사용하면 단일 페이지 애플리케이션과 유사하게 페이지 간 클라이언트 사이드 라우트 전환을 수행할 수 있습니다.

이러한 클라이언트 사이드 라우트 전환을 위해 `Link`라는 React 컴포넌트가 제공됩니다.
[code]
    import Link from 'next/link'

    function Home() {
      return (
        <ul>
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/about">About Us</Link>
          </li>
          <li>
            <Link href="/blog/hello-world">Blog Post</Link>
          </li>
        </ul>
      )
    }

    export default Home
[/code]

위 예제는 여러 링크를 사용하며, 각각은 경로(`href`)를 알려진 페이지에 매핑합니다.

  * `/` → `pages/index.js`
  * `/about` → `pages/about.js`
  * `/blog/hello-world` → `pages/blog/[slug].js`

뷰포트에 있는(초기 또는 스크롤로 나타난) 모든 `<Link />`는 [정적 생성](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)을 사용하는 페이지에 대해 기본적으로 해당 데이터까지 사전 로드됩니다. [서버 렌더링](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 라우트의 데이터는 `<Link />`를 클릭할 때에만 가져옵니다.

## 동적 경로로 연결하기[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#linking-to-dynamic-paths)

보간법을 사용해 경로를 만들 수도 있으며, 이는 [동적 라우트 세그먼트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)에 유용합니다. 예를 들어, 컴포넌트에 prop으로 전달된 게시물 목록을 보여주려면 다음과 같이 작성합니다:
[code]
    import Link from 'next/link'

    function Posts({ posts }) {
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>
              <Link href={`/blog/${encodeURIComponent(post.slug)}`}>
                {post.title}
              </Link>
            </li>
          ))}
        </ul>
      )
    }

    export default Posts
[/code]

> 이 예제에서는 경로를 UTF-8 호환으로 유지하기 위해 [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)를 사용합니다.

또는 URL 객체를 사용할 수도 있습니다:
[code]
    import Link from 'next/link'

    function Posts({ posts }) {
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>
              <Link
                href={{
                  pathname: '/blog/[slug]',
                  query: { slug: post.slug },
                }}
              >
                {post.title}
              </Link>
            </li>
          ))}
        </ul>
      )
    }

    export default Posts
[/code]

이제 보간 대신 `href`에 URL 객체를 사용하며, 그 구성은 다음과 같습니다.

  * `pathname`은 `pages` 디렉터리에 있는 페이지 이름입니다. 이 경우 `/blog/[slug]`입니다.
  * `query`는 동적 세그먼트를 담은 객체입니다. 이 경우 `slug`입니다.

## 라우터 주입하기[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#injecting-the-router)

React 컴포넌트에서 [`router` 객체](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)에 접근하려면 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) 또는 [`withRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)를 사용할 수 있습니다.

일반적으로는 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) 사용을 권장합니다.

## 명령형 라우팅[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#imperative-routing)

대부분의 라우팅 요구 사항은 [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link)로 해결할 수 있지만, 이를 사용하지 않고도 클라이언트 사이드 내비게이션을 수행할 수 있습니다. [ `next/router` 문서](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 참고하세요.

아래 예제는 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router)를 사용해 기본적인 페이지 내비게이션을 수행하는 방법을 보여줍니다:
[code]
    import { useRouter } from 'next/router'

    export default function ReadMore() {
      const router = useRouter()

      return (
        <button onClick={() => router.push('/about')}>
          Click here to read more
        </button>
      )
    }
[/code]

## 얕은 라우팅[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#shallow-routing)

예시

  * [Shallow Routing](https://github.com/vercel/next.js/tree/canary/examples/with-shallow-routing)

얕은 라우팅은 URL을 변경하면서 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props), [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props) 같은 데이터 패칭 메서드를 다시 실행하지 않도록 해 줍니다.

이 경우 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) 또는 [`withRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)가 추가하는 [`router` 객체](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)를 통해 업데이트된 `pathname`과 `query`를 전달받으며 상태는 유지됩니다.

얕은 라우팅을 활성화하려면 `shallow` 옵션을 `true`로 설정하세요. 다음 예제를 살펴보세요:
[code]
    import { useEffect } from 'react'
    import { useRouter } from 'next/router'

    // Current URL is '/'
    function Page() {
      const router = useRouter()

      useEffect(() => {
        // Always do navigations after the first render
        router.push('/?counter=10', undefined, { shallow: true })
      }, [])

      useEffect(() => {
        // The counter changed!
      }, [router.query.counter])
    }

    export default Page
[/code]

URL은 `/?counter=10`으로 업데이트되지만 페이지는 교체되지 않고 라우트 상태만 변경됩니다.

아래와 같이 [`componentDidUpdate`](https://react.dev/reference/react/Component#componentdidupdate)를 사용해 URL 변화를 감지할 수도 있습니다:
[code]
    componentDidUpdate(prevProps) {
      const { pathname, query } = this.props.router
      // verify props have changed to avoid an infinite loop
      if (query.counter !== prevProps.router.query.counter) {
        // fetch data based on the new query
      }
    }
[/code]

### 주의 사항[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#caveats)

얕은 라우팅은 현재 페이지 내의 URL 변경에 대해서만 **동작합니다**. 예를 들어 `pages/about.js`라는 다른 페이지가 있고 다음을 실행한다고 가정해 보겠습니다:
[code]
    router.push('/?counter=10', '/about?counter=10', { shallow: true })
[/code]

이는 새로운 페이지이므로, 현재 페이지를 언로드하고 새 페이지를 로드한 뒤 얕은 라우팅을 요청했더라도 데이터 패칭을 기다립니다.

프록시와 함께 얕은 라우팅을 사용하면, 이전처럼 새 페이지가 현재 페이지와 일치하는지 보장하지 않습니다. 프록시는 동적으로 리라이트할 수 있고, 얕은 라우팅에서는 건너뛰는 데이터 패칭 없이 클라이언트 측에서 이를 검증할 수 없으므로, 얕은 라우트 변경은 항상 얕은 변경으로 간주해야 합니다.
