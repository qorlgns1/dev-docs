---
title: 'Next.js에서 "App Container Deprecated" 오류 해결'
description: '이 문서는 사용자 정의 App 컴포넌트를 업데이트하여 Next.js의 "App Container Deprecated" 오류를 해결하는 방법을 안내합니다.'
---

# Next.js에서 "App Container Deprecated" 오류 해결 | Next.js

출처 URL: https://nextjs.org/docs/messages/app-container-deprecated

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Next.js에서 "App Container Deprecated" 오류 해결

# Next.js에서 "App Container Deprecated" 오류 해결

이 문서는 사용자 정의 App 컴포넌트를 업데이트하여 Next.js의 "App Container Deprecated" 오류를 해결하는 방법을 안내합니다.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/app-container-deprecated#why-this-error-occurred)

"App Container Deprecated" 오류는 사용자 정의 `<App>`(`pages/_app.js`)에서 `<Container>` 컴포넌트를 사용할 때 흔히 발생합니다. Next.js `9.0.4` 버전 이전에는 해시 스크롤을 처리하기 위해 `<Container>` 컴포넌트를 사용했습니다.

버전 `9.0.4`부터는 이 기능이 컴포넌트 트리 상위로 이동했으며, 그 결과 사용자 정의 `<App>`에서 `<Container>` 컴포넌트가 더 이상 필요하지 않습니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/app-container-deprecated#possible-ways-to-fix-it)

이 문제를 해결하려면 사용자 정의 `<App>`(`pages/_app.js`)에서 `<Container>` 컴포넌트를 제거하면 됩니다.

**Before**

pages/_app.js
```
    import React from 'react'
    import App, { Container } from 'next/app'

    class MyApp extends App {
      render() {
        const { Component, pageProps } = this.props
        return (
          <Container>
            <Component {...pageProps} />
          </Container>
        )
      }
    }

    export default MyApp
```

**After**

pages/_app.js
```
    import React from 'react'
    import App from 'next/app'

    class MyApp extends App {
      render() {
        const { Component, pageProps } = this.props
        return <Component {...pageProps} />
      }
    }

    export default MyApp
```

이 변경을 적용하면 `<Container>` 컴포넌트 없이도 사용자 정의 `<App>`이 예상대로 동작합니다.

## 유용한 링크[](https://nextjs.org/docs/messages/app-container-deprecated#useful-links)

  * [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)

보내기