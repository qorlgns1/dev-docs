---
title: '업그레이드: 버전 9'
description: '버전 9로 업그레이드하려면 다음 명령을 실행하세요:'
---

# 업그레이드: 버전 9 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/upgrading/version-9

[Guides](https://nextjs.org/docs/pages/guides)[Upgrading](https://nextjs.org/docs/pages/guides/upgrading)Version 9

# 버전 9로 업그레이드하는 방법

마지막 업데이트 2026년 2월 20일

버전 9로 업그레이드하려면 다음 명령을 실행하세요:

터미널
[code]
    npm i next@9
[/code]

터미널
[code]
    yarn add next@9
[/code]

터미널
[code]
    pnpm up next@9
[/code]

터미널
[code]
    bun add next@9
[/code]

> **참고:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 해당 버전에 맞게 함께 업그레이드하세요.

## 사용자 지정 App 파일(`pages/_app.js`)을 확인하세요[](https://nextjs.org/docs/pages/guides/upgrading/version-9#check-your-custom-app-file-pages_appjs)

이전에 [사용자 지정 `<App>`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) 예제를 그대로 복사했다면 `getInitialProps`를 제거할 수 있을지도 모릅니다.

가능하다면 `pages/_app.js`에서 `getInitialProps`를 제거하는 것이 새로운 Next.js 기능을 활용하는 데 중요합니다!

다음 `getInitialProps`는 아무 작업도 하지 않으므로 제거할 수 있습니다:
[code]
    class MyApp extends App {
      // Remove me, I do nothing!
      static async getInitialProps({ Component, ctx }) {
        let pageProps = {}

        if (Component.getInitialProps) {
          pageProps = await Component.getInitialProps(ctx)
        }

        return { pageProps }
      }

      render() {
        // ... etc
      }
    }
[/code]

## 주요 변경 사항[](https://nextjs.org/docs/pages/guides/upgrading/version-9#breaking-changes)

### `@zeit/next-typescript`는 더 이상 필요하지 않습니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#zeitnext-typescript-is-no-longer-necessary)

Next.js는 이제 `@zeit/next-typescript` 사용을 무시하고 제거하라는 경고를 표시합니다. `next.config.js`에서 이 플러그인을 제거하세요.

사용자 지정 `.babelrc`(있는 경우)에서 `@zeit/next-typescript/babel`에 대한 참조도 삭제하세요.

[`fork-ts-checker-webpack-plugin`](https://github.com/Realytics/fork-ts-checker-webpack-plugin/issues)의 사용 역시 `next.config.js`에서 제거해야 합니다.

TypeScript 정의는 `next` 패키지에 함께 게시되므로 충돌을 피하려면 `@types/next`를 제거해야 합니다.

다음 타입들이 변경되었습니다:

> 이 목록은 커뮤니티가 업그레이드를 돕기 위해 만들었습니다. 다른 차이점을 발견하면 다른 사용자들에게 도움이 되도록 이 목록에 풀 리퀘스트를 보내 주세요.

이전:
[code]
    import { NextContext } from 'next'
    import { NextAppContext, DefaultAppIProps } from 'next/app'
    import { NextDocumentContext, DefaultDocumentIProps } from 'next/document'
[/code]

이후
[code]
    import { NextPageContext } from 'next'
    import { AppContext, AppInitialProps } from 'next/app'
    import { DocumentContext, DocumentInitialProps } from 'next/document'
[/code]

### `config` 키는 이제 페이지에서 export하는 항목입니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#the-config-key-is-now-an-export-on-a-page)

이제 페이지에서 `config`라는 이름의 사용자 정의 변수를 export(`export { config }` / `export const config ...`)할 수 없습니다. 이 export된 변수는 Opt-in AMP 및 API Route 기능 같은 페이지 수준 Next.js 구성을 지정하는 데 사용됩니다.

Next.js와 무관한 용도의 `config` export는 다른 이름으로 변경해야 합니다.

### `next/dynamic`은 로딩 중 기본으로 "loading..."을 렌더링하지 않습니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#nextdynamic-no-longer-renders-loading-by-default-while-loading)

동적 컴포넌트는 로딩 중 기본적으로 아무것도 렌더링하지 않습니다. `loading` 속성을 설정해 이 동작을 계속 사용자 정의할 수 있습니다:
[code]
    import dynamic from 'next/dynamic'

    const DynamicComponentWithCustomLoading = dynamic(
      () => import('../components/hello2'),
      {
        loading: () => <p>Loading</p>,
      }
    )
[/code]

### `withAmp`는 export된 구성 객체로 대체되었습니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#withamp-has-been-removed-in-favor-of-an-exported-configuration-object)

Next.js에는 이제 페이지 수준 구성 개념이 있으므로 일관성을 위해 `withAmp` 고차 컴포넌트가 제거되었습니다.

이 변경은 **Next.js 프로젝트 루트에서 다음 명령을 실행하면 자동으로 마이그레이션됩니다.**

터미널
[code]
    curl -L https://github.com/vercel/next-codemod/archive/master.tar.gz | tar -xz --strip=2 next-codemod-master/transforms/withamp-to-config.js npx jscodeshift -t ./withamp-to-config.js pages/**/*.js
[/code]

수동으로 마이그레이션하거나 codemod가 생성할 결과를 확인하려면 아래를 참고하세요:

**변경 전**
[code]
    import { withAmp } from 'next/amp'

    function Home() {
      return <h1>My AMP Page</h1>
    }

    export default withAmp(Home)
    // or
    export default withAmp(Home, { hybrid: true })
[/code]

**변경 후**
[code]
    export default function Home() {
      return <h1>My AMP Page</h1>
    }

    export const config = {
      amp: true,
      // or
      amp: 'hybrid',
    }
[/code]

### `next export`는 더 이상 페이지를 `index.html`로 내보내지 않습니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#next-export-no-longer-exports-pages-as-indexhtml)

이전에는 `pages/about.js`를 내보내면 `out/about/index.html`이 생성되었습니다. 이제 이 동작이 `out/about.html`을 생성하도록 변경되었습니다.

이전 동작으로 되돌리려면 다음 내용을 포함한 `next.config.js`를 생성하세요:

next.config.js
[code]
    module.exports = {
      trailingSlash: true,
    }
[/code]

### `pages/api/`는 다르게 취급됩니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#pagesapi-is-treated-differently)

`pages/api/`의 페이지는 이제 [API Routes](https://nextjs.org/blog/next-9#api-routes)로 간주됩니다. 이 디렉터리의 페이지는 더 이상 클라이언트 번들을 포함하지 않습니다.

## 사용 중단된 기능[](https://nextjs.org/docs/pages/guides/upgrading/version-9#deprecated-features)

### `next/dynamic`은 한 번에 여러 모듈 로드를 지원하지 않습니다[](https://nextjs.org/docs/pages/guides/upgrading/version-9#nextdynamic-has-deprecated-loading-multiple-modules-at-once)

한 번에 여러 모듈을 로드하는 기능은 `next/dynamic`에서 사용 중단되어 React(`React.lazy`, `Suspense`) 구현과 더 유사해졌습니다.

이 동작에 의존하는 코드를 업데이트하는 것은 비교적 간단합니다! 애플리케이션 마이그레이션을 돕기 위해 변경 전/후 예제를 제공했습니다:

**변경 전**
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

**변경 후**
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
