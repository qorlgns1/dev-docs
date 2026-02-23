---
title: '라우팅: Custom App'
description: 'Next.js는  컴포넌트를 사용해 페이지를 초기화합니다. 이를 오버라이드해 페이지 초기화를 제어하면 다음을 수행할 수 있습니다.'
---

# 라우팅: Custom App | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/custom-app

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)[라우팅](https://nextjs.org/docs/pages/building-your-application/routing)커스텀 앱

# 커스텀 앱

마지막 업데이트 2026년 2월 20일

Next.js는 `App` 컴포넌트를 사용해 페이지를 초기화합니다. 이를 오버라이드해 페이지 초기화를 제어하면 다음을 수행할 수 있습니다.

  * 페이지 전환 간 공유 레이아웃 생성
  * 페이지에 추가 데이터 주입
  * [글로벌 CSS 추가](https://nextjs.org/docs/app/getting-started/css)

## 사용 방법[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#usage)

기본 `App`을 오버라이드하려면 아래와 같이 `pages/_app` 파일을 생성하세요.

pages/_app.tsx

JavaScriptTypeScript
```
    import type { AppProps } from 'next/app'

    export default function MyApp({ Component, pageProps }: AppProps) {
      return <Component {...pageProps} />
    }
```

`Component` prop은 활성 `page`이므로 라우트를 이동할 때마다 `Component`가 새 `page`로 바뀝니다. 따라서 `Component`에 전달한 모든 props는 해당 `page`에서 받을 수 있습니다.

`pageProps`는 [데이터 패칭 메서드](https://nextjs.org/docs/pages/building-your-application/data-fetching) 중 하나가 페이지용으로 미리 로드한 초기 props 객체이며, 그렇지 않다면 빈 객체입니다.

> **알아두면 좋아요** :
>
>   * 앱이 실행 중인 상태에서 커스텀 `App`을 추가했다면 개발 서버를 재시작해야 합니다. 이는 이전에 `pages/_app.js`가 없었을 때만 필요합니다.
>   * `App`은 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)나 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 같은 Next.js [데이터 패칭 메서드](https://nextjs.org/docs/pages/building-your-application/data-fetching)를 지원하지 않습니다.
>

## `App`에서 `getInitialProps` 사용[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#getinitialprops-with-app)

`App`에서 [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)를 사용하면 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)가 없는 페이지에서 [자동 정적 최적화](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)가 비활성화됩니다.

**이 패턴은 권장하지 않습니다.** 대신 페이지와 레이아웃에서 데이터를 더 쉽게 가져올 수 있는 App Router를 [점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 것을 고려하세요.

pages/_app.tsx

JavaScriptTypeScript
```
    import App, { AppContext, AppInitialProps, AppProps } from 'next/app'

    type AppOwnProps = { example: string }

    export default function MyApp({
      Component,
      pageProps,
      example,
    }: AppProps & AppOwnProps) {
      return (
        <>
          <p>Data: {example}</p>
          <Component {...pageProps} />
        </>
      )
    }

    MyApp.getInitialProps = async (
      context: AppContext
    ): Promise<AppOwnProps & AppInitialProps> => {
      const ctx = await App.getInitialProps(context)

      return { ...ctx, example: 'data' }
    }
```