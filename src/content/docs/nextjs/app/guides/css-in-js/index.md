---
title: '가이드: CSS-in-JS'
description: '> 경고: Server Components와 Streaming 같은 최신 React 기능과 함께 CSS-in-JS를 사용하려면 라이브러리 작성자가 동시 렌더링을 포함한 최신 React 버전을 지원해야 합니다.'
---

# 가이드: CSS-in-JS | Next.js

Source URL: https://nextjs.org/docs/app/guides/css-in-js

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)CSS-in-JS

Copy page

# CSS-in-JS 라이브러리 사용 방법

최종 업데이트 2026년 2월 20일

> **경고:** Server Components와 Streaming 같은 최신 React 기능과 함께 CSS-in-JS를 사용하려면 라이브러리 작성자가 [동시 렌더링](https://react.dev/blog/2022/03/29/react-v18#what-is-concurrent-react)을 포함한 최신 React 버전을 지원해야 합니다.

다음 라이브러리는 `app` 디렉터리의 클라이언트 컴포넌트에서 지원됩니다(알파벳 순):

  * [`ant-design`](https://ant.design/docs/react/use-with-next#using-app-router)
  * [`chakra-ui`](https://chakra-ui.com/getting-started/nextjs-app-guide)
  * [`@fluentui/react-components`](https://react.fluentui.dev/?path=/docs/concepts-developer-server-side-rendering-next-js-appdir-setup--page)
  * [`kuma-ui`](https://kuma-ui.com)
  * [`@mui/material`](https://mui.com/material-ui/guides/next-js-app-router/)
  * [`@mui/joy`](https://mui.com/joy-ui/integrations/next-js-app-router/)
  * [`pandacss`](https://panda-css.com)
  * [`styled-jsx`](https://nextjs.org/docs/app/guides/css-in-js#styled-jsx)
  * [`styled-components`](https://nextjs.org/docs/app/guides/css-in-js#styled-components)
  * [`stylex`](https://stylexjs.com)
  * [`tamagui`](https://tamagui.dev/docs/guides/next-js#server-components)
  * [`tss-react`](https://tss-react.dev/)
  * [`vanilla-extract`](https://vanilla-extract.style)

다음 라이브러리는 현재 지원을 준비 중입니다:

  * [`emotion`](https://github.com/emotion-js/emotion/issues/2928)

> **알아두면 좋은 정보** : 다양한 CSS-in-JS 라이브러리를 테스트 중이며, React 18 기능 및/또는 `app` 디렉터리를 지원하는 라이브러리에 대한 예제를 계속 추가할 예정입니다.

## `app`에서 CSS-in-JS 구성하기[](https://nextjs.org/docs/app/guides/css-in-js#configuring-css-in-js-in-app)

CSS-in-JS 구성은 다음 세 단계의 옵트인 프로세스로 이루어집니다:

  1. 렌더링 중 모든 CSS 규칙을 수집하는 **스타일 레지스트리**.
  2. 해당 규칙을 사용할 수 있는 콘텐츠 전에 주입하기 위한 새로운 `useServerInsertedHTML` 훅.
  3. 초기 서버 사이드 렌더링 동안 앱을 스타일 레지스트리로 감싸는 클라이언트 컴포넌트.

### `styled-jsx`[](https://nextjs.org/docs/app/guides/css-in-js#styled-jsx)

클라이언트 컴포넌트에서 `styled-jsx`를 사용하려면 `v5.1.0`을 사용해야 합니다. 먼저 새 레지스트리를 만듭니다:

app/registry.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import React, { useState } from 'react'
    import { useServerInsertedHTML } from 'next/navigation'
    import { StyleRegistry, createStyleRegistry } from 'styled-jsx'
     
    export default function StyledJsxRegistry({
      children,
    }: {
      children: React.ReactNode
    }) {
      // Only create stylesheet once with lazy initial state
      // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
      const [jsxStyleRegistry] = useState(() => createStyleRegistry())
     
      useServerInsertedHTML(() => {
        const styles = jsxStyleRegistry.styles()
        jsxStyleRegistry.flush()
        return <>{styles}</>
      })
     
      return <StyleRegistry registry={jsxStyleRegistry}>{children}</StyleRegistry>
    }
[/code]

그런 다음 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)을 레지스트리로 감쌉니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import StyledJsxRegistry from './registry'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html>
          <body>
            <StyledJsxRegistry>{children}</StyledJsxRegistry>
          </body>
        </html>
      )
    }
[/code]

[예시는 여기에서 확인하세요](https://github.com/vercel/next.js/tree/canary/examples/with-styled-jsx).

### Styled Components[](https://nextjs.org/docs/app/guides/css-in-js#styled-components)

다음은 `styled-components@6` 이상을 구성하는 예시입니다:

먼저 `next.config.js`에서 styled-components를 활성화합니다.

next.config.js
[code]
    module.exports = {
      compiler: {
        styledComponents: true,
      },
    }
[/code]

그다음 렌더링 중 생성된 모든 CSS 스타일 규칙을 수집하는 전역 레지스트리 컴포넌트를 만들고, 해당 규칙을 반환하는 함수를 `styled-components` API로 작성합니다. 이어서 `useServerInsertedHTML` 훅을 사용해 레지스트리에 수집된 스타일을 루트 레이아웃의 `<head>` HTML 태그에 주입합니다.

lib/registry.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import React, { useState } from 'react'
    import { useServerInsertedHTML } from 'next/navigation'
    import { ServerStyleSheet, StyleSheetManager } from 'styled-components'
     
    export default function StyledComponentsRegistry({
      children,
    }: {
      children: React.ReactNode
    }) {
      // Only create stylesheet once with lazy initial state
      // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
      const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet())
     
      useServerInsertedHTML(() => {
        const styles = styledComponentsStyleSheet.getStyleElement()
        styledComponentsStyleSheet.instance.clearTag()
        return <>{styles}</>
      })
     
      if (typeof window !== 'undefined') return <>{children}</>
     
      return (
        <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>
          {children}
        </StyleSheetManager>
      )
    }
[/code]

루트 레이아웃의 `children`을 스타일 레지스트리 컴포넌트로 감쌉니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import StyledComponentsRegistry from './lib/registry'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html>
          <body>
            <StyledComponentsRegistry>{children}</StyledComponentsRegistry>
          </body>
        </html>
      )
    }
[/code]

[예시는 여기에서 확인하세요](https://github.com/vercel/next.js/tree/canary/examples/with-styled-components).

> **알아두면 좋은 정보** :
> 
>   * 서버 렌더링 동안 스타일은 전역 레지스트리로 추출되어 HTML의 `<head>`에 플러시됩니다. 이렇게 하면 스타일 규칙이 해당 규칙을 사용할 수 있는 콘텐츠보다 먼저 위치하게 됩니다. 앞으로는 스타일을 어디에 주입할지 결정하기 위해 곧 공개될 React 기능을 사용할 수도 있습니다.
>   * 스트리밍 중에는 각 청크의 스타일이 수집되어 기존 스타일에 추가됩니다. 클라이언트 측 하이드레이션이 완료되면 `styled-components`가 기존 방식대로 동적 스타일을 계속 주입합니다.
>   * 트리 최상위에 클라이언트 컴포넌트를 사용해 스타일 레지스트리를 두는 이유는 CSS 규칙을 추출하는 더 효율적인 방법이기 때문입니다. 이렇게 하면 이후 서버 렌더에서 스타일을 다시 생성하지 않아도 되고, 서버 컴포넌트 페이로드에 스타일이 포함되는 것도 방지할 수 있습니다.
>   * styled-components 컴파일의 개별 속성을 구성해야 하는 고급 사용 사례에서는 [Next.js styled-components API 레퍼런스](https://nextjs.org/docs/architecture/nextjs-compiler#styled-components)를 참고하세요.
> 

Was this helpful?

supported.

Send
