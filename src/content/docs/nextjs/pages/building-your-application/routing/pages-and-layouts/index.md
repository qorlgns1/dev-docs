---
title: '라우팅: 페이지와 레이아웃'
description: '마지막 업데이트 2026년 2월 20일'
---

# 라우팅: 페이지와 레이아웃 | Next.js
출처 URL: https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[라우팅](https://nextjs.org/docs/pages/building-your-application/routing)페이지와 레이아웃

페이지 복사

# 페이지와 레이아웃

마지막 업데이트 2026년 2월 20일

Pages Router는 페이지 개념을 기반으로 한 파일 시스템 기반 라우터를 제공합니다.

`pages` 디렉터리에 파일을 추가하면 자동으로 라우트로 사용할 수 있게 됩니다.

Next.js에서 **페이지**는 `pages` 디렉터리에 있는 `.js`, `.jsx`, `.ts`, `.tsx` 파일에서 내보내는 [React 컴포넌트](https://react.dev/learn/your-first-component)입니다. 각 페이지는 파일 이름을 기반으로 한 라우트와 연결됩니다.

**예시**: 아래와 같이 React 컴포넌트를 내보내는 `pages/about.js`를 만들면 `/about`에서 접근할 수 있습니다.
[code] 
    export default function About() {
      return <div>About</div>
    }
[/code]

## 인덱스 경로[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)

라우터는 `index`라는 이름의 파일을 디렉터리 루트로 자동 라우팅합니다.

  * `pages/index.js` → `/`
  * `pages/blog/index.js` → `/blog`

## 중첩 경로[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#nested-routes)

라우터는 중첩 파일을 지원합니다. 폴더 구조를 중첩해 만들면 파일이 동일한 방식으로 자동 라우팅됩니다.

  * `pages/blog/first-post.js` → `/blog/first-post`
  * `pages/dashboard/settings/username.js` → `/dashboard/settings/username`

## 동적 경로가 있는 페이지[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#pages-with-dynamic-routes)

Next.js는 동적 경로를 갖는 페이지를 지원합니다. 예를 들어 `pages/posts/[id].js` 파일을 만들면 `posts/1`, `posts/2` 등으로 접근할 수 있습니다.

> 동적 라우팅에 대해 더 알아보려면 [Dynamic Routing 문서](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 확인하세요.

## 레이아웃 패턴[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)

React 모델은 하나의 [페이지](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)를 여러 컴포넌트로 분해할 수 있게 해줍니다. 이 컴포넌트 중 다수는 페이지 간에 자주 재사용됩니다. 예를 들어 모든 페이지에 동일한 내비게이션 바와 푸터가 있을 수 있습니다.

components/layout.js
[code]
    import Navbar from './navbar'
    import Footer from './footer'
     
    export default function Layout({ children }) {
      return (
        <>
          <Navbar />
          <main>{children}</main>
          <Footer />
        </>
      )
    }
[/code]

## 예제[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#examples)

### Custom App을 통한 단일 공유 레이아웃[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#single-shared-layout-with-custom-app)

애플리케이션 전체에 레이아웃이 하나뿐이라면 [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)을 만들고 애플리케이션을 해당 레이아웃으로 감쌀 수 있습니다. `<Layout />` 컴포넌트가 페이지 전환 시 재사용되므로 입력 값과 같은 컴포넌트 상태가 유지됩니다.

pages/_app.js
[code]
    import Layout from '../components/layout'
     
    export default function MyApp({ Component, pageProps }) {
      return (
        <Layout>
          <Component {...pageProps} />
        </Layout>
      )
    }
[/code]

### 페이지별 레이아웃[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#per-page-layouts)

레이아웃이 여러 개 필요하면 페이지에 `getLayout` 속성을 추가해 레이아웃용 React 컴포넌트를 반환할 수 있습니다. 이를 통해 _페이지별로_ 레이아웃을 정의할 수 있습니다. 함수를 반환하므로 필요하면 복잡한 중첩 레이아웃도 구성할 수 있습니다.

pages/index.js
[code]
     
    import Layout from '../components/layout'
    import NestedLayout from '../components/nested-layout'
     
    export default function Page() {
      return (
        /** Your content */
      )
    }
     
    Page.getLayout = function getLayout(page) {
      return (
        <Layout>
          <NestedLayout>{page}</NestedLayout>
        </Layout>
      )
    }
[/code]

pages/_app.js
[code]
    export default function MyApp({ Component, pageProps }) {
      // Use the layout defined at the page level, if available
      const getLayout = Component.getLayout ?? ((page) => page)
     
      return getLayout(<Component {...pageProps} />)
    }
[/code]

페이지 간 내비게이션 시 단일 페이지 애플리케이션(SPA) 경험을 위해 입력 값, 스크롤 위치 등 페이지 상태를 _지속_ 시키고 싶습니다.

이 레이아웃 패턴은 페이지 전환 중에도 React 컴포넌트 트리가 유지되기 때문에 상태 지속을 가능하게 합니다. 컴포넌트 트리를 통해 React는 변경된 요소를 파악해 상태를 보존할 수 있습니다.

> **참고**: 이 프로세스는 [reconciliation](https://react.dev/learn/preserving-and-resetting-state)이라 하며, React가 변경된 요소를 파악하는 방식입니다.

### TypeScript 사용 시[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#with-typescript)

TypeScript를 사용할 때는 `getLayout` 함수를 포함하는 페이지용 새 타입을 먼저 생성해야 합니다. 그런 다음 `AppProps`에서 `Component` 속성을 앞서 만든 타입으로 덮어쓰는 새 타입을 만들어야 합니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    import type { ReactElement } from 'react'
    import Layout from '../components/layout'
    import NestedLayout from '../components/nested-layout'
    import type { NextPageWithLayout } from './_app'
     
    const Page: NextPageWithLayout = () => {
      return <p>hello world</p>
    }
     
    Page.getLayout = function getLayout(page: ReactElement) {
      return (
        <Layout>
          <NestedLayout>{page}</NestedLayout>
        </Layout>
      )
    }
     
    export default Page
[/code]

pages/_app.tsx

JavaScriptTypeScript
[code]
    import type { ReactElement, ReactNode } from 'react'
    import type { NextPage } from 'next'
    import type { AppProps } from 'next/app'
     
    export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
      getLayout?: (page: ReactElement) => ReactNode
    }
     
    type AppPropsWithLayout = AppProps & {
      Component: NextPageWithLayout
    }
     
    export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
      // Use the layout defined at the page level, if available
      const getLayout = Component.getLayout ?? ((page) => page)
     
      return getLayout(<Component {...pageProps} />)
    }
[/code]

### 데이터 패칭[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#data-fetching)

레이아웃 내부에서는 `useEffect`나 [SWR](https://swr.vercel.app/) 같은 라이브러리를 사용해 클라이언트 측에서 데이터를 패칭할 수 있습니다. 이 파일은 [페이지](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)가 아니므로 지금은 `getStaticProps`나 `getServerSideProps`를 사용할 수 없습니다.

components/layout.js
[code]
    import useSWR from 'swr'
    import Navbar from './navbar'
    import Footer from './footer'
     
    export default function Layout({ children }) {
      const { data, error } = useSWR('/api/navigation', fetcher)
     
      if (error) return <div>Failed to load</div>
      if (!data) return <div>Loading...</div>
     
      return (
        <>
          <Navbar links={data.links} />
          <main>{children}</main>
          <Footer />
        </>
      )
    }
[/code]

도움이 되었나요?

지원됨.

전송
