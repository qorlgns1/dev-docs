---
title: '업그레이드: 버전 11'
description: '버전 11로 업그레이드하려면 다음 명령을 실행하세요:'
---

# 업그레이드: 버전 11 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/upgrading/version-11

[Guides](https://nextjs.org/docs/pages/guides)[Upgrading](https://nextjs.org/docs/pages/guides/upgrading)Version 11

Copy page

# 버전 11로 업그레이드하는 방법

최종 업데이트 2026년 2월 20일

버전 11로 업그레이드하려면 다음 명령을 실행하세요:

Terminal
```
    npm i next@11 react@17 react-dom@17
```

Terminal
```
    yarn add next@11 react@17 react-dom@17
```

Terminal
```
    pnpm up next@11 react@17 react-dom@17
```

Terminal
```
    bun add next@11 react@17 react-dom@17
```

> **참고:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 해당 버전에 맞춰 업그레이드하세요.

### Webpack 5[](https://nextjs.org/docs/pages/guides/upgrading/version-11#webpack-5)

Webpack 5는 이제 모든 Next.js 애플리케이션의 기본값입니다. 커스텀 webpack 구성이 없다면 이미 webpack 5를 사용 중입니다. 커스텀 구성이 있다면 [Next.js webpack 5 문서](https://nextjs.org/docs/messages/webpack5)를 참고해 업그레이드 가이드를 확인하세요.

### 이제 `distDir` 정리가 기본값[](https://nextjs.org/docs/pages/guides/upgrading/version-11#cleaning-the-distdir-is-now-a-default)

빌드 출력 디렉터리(기본값 `.next`)가 이제 Next.js 캐시를 제외하고 기본적으로 정리됩니다. 자세한 내용은 [cleaning `distDir` RFC](https://github.com/vercel/next.js/discussions/6009)를 참고하세요.

이전 동작에 의존하던 애플리케이션이라면 `next.config.js`에서 `cleanDistDir: false` 플래그를 추가해 새 기본 동작을 비활성화할 수 있습니다.

### 이제 `PORT`가 `next dev` 및 `next start`에서 지원됨[](https://nextjs.org/docs/pages/guides/upgrading/version-11#port-is-now-supported-for-next-dev-and-next-start)

Next.js 11은 애플리케이션이 실행될 포트를 설정하기 위해 `PORT` 환경 변수를 지원합니다. 여전히 `-p`/`--port` 사용을 권장하지만, 어떤 이유로든 `-p`를 사용할 수 없었다면 이제 대안으로 `PORT`를 사용할 수 있습니다:

Example:
```
    PORT=4000 next start

```

### 이미지를 가져오기 위한 `next.config.js` 커스터마이징[](https://nextjs.org/docs/pages/guides/upgrading/version-11#nextconfigjs-customization-to-import-images)

Next.js 11은 `next/image`로 정적 이미지 import를 지원합니다. 이 새 기능은 이미지 import를 처리할 수 있어야 합니다. 이전에 `next-images`나 `next-optimized-images` 패키지를 추가했다면 `next/image`를 사용하는 새 기본 지원으로 이동하거나 기능을 비활성화할 수 있습니다:

next.config.js
```
    module.exports = {
      images: {
        disableStaticImages: true,
      },
    }
```

### `pages/_app.js`에서 `super.componentDidCatch()` 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-supercomponentdidcatch-from-pages_appjs)

`next/app` 컴포넌트의 `componentDidCatch`는 더 이상 필요하지 않아 Next.js 9에서 사용 중단되었고 이후로 no-op이었습니다. Next.js 11에서 제거되었습니다.

`pages/_app.js`에 커스텀 `componentDidCatch` 메서드가 있다면 더 이상 필요하지 않으므로 `super.componentDidCatch`를 제거하세요.

### `pages/_app.js`에서 `Container` 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-container-from-pages_appjs)

이 export는 더 이상 필요하지 않아 Next.js 9에서 사용 중단되었고 개발 중 경고만 표시되는 no-op이었습니다. Next.js 11에서 제거되었습니다.

`pages/_app.js`가 `next/app`에서 `Container`를 import한다면 이제 제거하세요. 자세한 내용은 [문서](https://nextjs.org/docs/messages/app-container-deprecated)를 참고하세요.

### 페이지 컴포넌트에서 `props.url` 사용 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-propsurl-usage-from-page-components)

이 속성은 Next.js 4에서 사용 중단되었고 개발 중 경고가 표시되었습니다. `getStaticProps` / `getServerSideProps` 도입 이후 이미 `props.url` 사용이 금지되었습니다. Next.js 11에서는 완전히 제거되었습니다.

자세한 내용은 [문서](https://nextjs.org/docs/messages/url-deprecated)를 참고하세요.

### `next/image`의 `unsized` 속성 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-unsized-property-on-nextimage)

`next/image`의 `unsized` 속성은 Next.js 10.0.1에서 사용 중단되었습니다. 대신 `layout="fill"`을 사용할 수 있습니다. Next.js 11에서 `unsized`가 제거되었습니다.

### `next/dynamic`의 `modules` 속성 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-modules-property-on-nextdynamic)

`next/dynamic`의 `modules`와 `render` 옵션은 Next.js 9.5에서 사용 중단되었습니다. 이는 `next/dynamic` API를 `React.lazy`와 더욱 가깝게 만들기 위해서였습니다. Next.js 11에서 `modules`와 `render` 옵션이 제거되었습니다.

이 옵션은 Next.js 8 이후 문서에서 다뤄지지 않았으므로 애플리케이션에서 사용하고 있을 가능성은 낮습니다.

애플리케이션에서 `modules`와 `render`를 사용 중이라면 [문서](https://nextjs.org/docs/messages/next-dynamic-modules)를 참고하세요.

### `Head.rewind` 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-11#remove-headrewind)

`Head.rewind`는 Next.js 9.5부터 no-op이었으며, Next.js 11에서 제거되었습니다. 안전하게 사용을 중단할 수 있습니다.

### 기본적으로 Moment.js 로케일 제외[](https://nextjs.org/docs/pages/guides/upgrading/version-11#momentjs-locales-excluded-by-default)

Moment.js는 기본적으로 많은 로케일 번역을 포함합니다. Next.js는 이제 Moment.js를 사용하는 애플리케이션의 번들 크기를 최적화하기 위해 기본적으로 이러한 로케일을 제외합니다.

특정 로케일을 로드하려면 다음 스니펫을 사용하세요:
```
    import moment from 'moment'
    import 'moment/locale/ja'

    moment.locale('ja')
```

이 새 기본 동작을 원하지 않는다면 `next.config.js`에 `excludeDefaultMomentLocales: false`를 추가해 옵트아웃할 수 있지만, Moment.js 크기를 크게 줄이므로 이 최적화를 비활성화하지 않는 것이 강력히 권장됩니다.

### `router.events` 사용 업데이트[](https://nextjs.org/docs/pages/guides/upgrading/version-11#update-usage-of-routerevents)

렌더링 중 `router.events`에 접근하고 있다면, Next.js 11에서는 사전 렌더링 동안 `router.events`가 더 이상 제공되지 않습니다. `useEffect`에서 `router.events`에 접근하도록 하세요:
```
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
```

비공개였던 내부 속성 `router.router.events`를 사용 중이었다면 `router.events`를 사용하도록 변경하세요.

## React 16에서 17로[](https://nextjs.org/docs/pages/guides/upgrading/version-11#react-16-to-17)

React 17은 [새로운 JSX 변환](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)을 도입해 오랫동안 Next.js 기능이었던 “JSX를 사용할 때 `import React from 'react'`를 하지 않아도 되는” 기능을 React 생태계 전체에 제공합니다. React 17을 사용할 때 Next.js는 자동으로 새 변환을 사용합니다. 이 변환은 이전 Next.js 구현의 의도치 않은 부작용이었던 `React` 변수를 전역으로 만들지 않습니다. [코드모드](https://nextjs.org/docs/pages/guides/upgrading/codemods#add-missing-react-import)를 사용하면 import 없이 `React`를 사용한 사례를 자동으로 수정할 수 있습니다.

대부분의 애플리케이션이 이미 최신 React 버전을 사용하고 있으며, Next.js 11에서는 최소 React 버전이 17.0.2로 업데이트되었습니다.

업그레이드하려면 다음 명령을 실행하세요:
```
    npm install react@latest react-dom@latest

```

또는 `yarn` 사용 시:
```
    yarn add react@latest react-dom@latest

```

Was this helpful?

supported.

Send