---
title: '시작하기: CSS'
description: 'Next.js는 다음과 같이 CSS를 사용해 애플리케이션을 스타일링하는 여러 방법을 제공합니다.'
---

# 시작하기: CSS | Next.js

Source URL: https://nextjs.org/docs/pages/getting-started/css

# 애플리케이션에서 CSS 사용하는 방법

2026년 2월 20일 업데이트

Next.js는 다음과 같이 CSS를 사용해 애플리케이션을 스타일링하는 여러 방법을 제공합니다.

  * [Tailwind CSS](https://nextjs.org/docs/pages/getting-started/css#tailwind-css)
  * [CSS Modules](https://nextjs.org/docs/pages/getting-started/css#css-modules)
  * [Global CSS](https://nextjs.org/docs/pages/getting-started/css#global-css)
  * [External Stylesheets](https://nextjs.org/docs/pages/getting-started/css#external-stylesheets)
  * [Sass](https://nextjs.org/docs/app/guides/sass)
  * [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)

## Tailwind CSS[](https://nextjs.org/docs/pages/getting-started/css#tailwind-css)

[Tailwind CSS](https://tailwindcss.com/)는 커스텀 디자인을 만들 수 있도록 저수준 유틸리티 클래스를 제공하는 유틸리티 우선 CSS 프레임워크입니다.

Tailwind CSS 설치:

pnpmnpmyarnbun

터미널
[code]
    pnpm add -D tailwindcss @tailwindcss/postcss
[/code]

`postcss.config.mjs` 파일에 PostCSS 플러그인을 추가하세요.

postcss.config.mjs
[code]
    export default {
      plugins: {
        '@tailwindcss/postcss': {},
      },
    }
[/code]

글로벌 CSS 파일에서 Tailwind를 가져옵니다.

styles/globals.css
[code]
    @import 'tailwindcss';
[/code]

`pages/_app.js` 파일에서 해당 CSS 파일을 가져옵니다.

pages/_app.js
[code]
    import '@/styles/globals.css'

    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

이제 애플리케이션에서 Tailwind 유틸리티 클래스를 사용할 수 있습니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    export default function Home() {
      return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
          <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
        </main>
      )
    }
[/code]

> **알아두면 좋아요:** 매우 오래된 브라우저를 더 폭넓게 지원하려면 [Tailwind CSS v3 설정 지침](https://nextjs.org/docs/app/guides/tailwind-v3-css)을 확인하세요.

## CSS Modules[](https://nextjs.org/docs/pages/getting-started/css#css-modules)

CSS Modules는 고유한 클래스 이름을 생성해 CSS를 로컬 범위로 제한합니다. 이를 통해 서로 다른 파일에서 동일한 클래스를 이름 충돌 없이 사용할 수 있습니다.

CSS Modules를 사용하려면 `.module.css` 확장자를 가진 새 파일을 만들고 `pages` 디렉터리 내부의 임의의 컴포넌트에서 가져오세요.

./styles/blog.module.css
[code]
    .blog {
      padding: 24px;
    }
[/code]

pages/blog/index.tsx

JavaScriptTypeScript
[code]
    import styles from './blog.module.css'

    export default function Page() {
      return <main className={styles.blog}></main>
    }
[/code]

## Global CSS[](https://nextjs.org/docs/pages/getting-started/css#global-css)

글로벌 CSS를 사용해 애플리케이션 전반에 스타일을 적용할 수 있습니다.

애플리케이션의 **모든 경로**에 스타일을 적용하려면 `pages/_app.js` 파일에서 스타일시트를 가져오세요.

pages/_app.js
[code]
    import '@/styles/global.css'

    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

스타일시트의 글로벌 특성과 충돌을 방지하기 위해 [`pages/_app.js`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) 내부에서 가져오는 것이 좋습니다.

## External stylesheets[](https://nextjs.org/docs/pages/getting-started/css#external-stylesheets)

Next.js에서는 JavaScript 파일에서 CSS를 가져올 수 있습니다. 이는 Next.js가 [`import`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import)의 개념을 JavaScript 바깥으로 확장했기 때문입니다.

### `node_modules`에서 스타일 가져오기[](https://nextjs.org/docs/pages/getting-started/css#import-styles-from-node_modules)

Next.js **9.5.4** 이후에는 애플리케이션 어디에서나 `node_modules`의 CSS 파일을 가져올 수 있습니다.

`bootstrap`이나 `nprogress`처럼 글로벌 스타일시트는 `pages/_app.js` 내부에서 가져와야 합니다. 예시는 다음과 같습니다.

pages/_app.js
[code]
    import 'bootstrap/dist/css/bootstrap.css'

    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

서드파티 컴포넌트에 필요한 CSS를 가져오려면 해당 컴포넌트에서 가져올 수 있습니다. 예시는 다음과 같습니다.

components/example-dialog.js
[code]
    import { useState } from 'react'
    import { Dialog } from '@reach/dialog'
    import VisuallyHidden from '@reach/visually-hidden'
    import '@reach/dialog/styles.css'

    function ExampleDialog(props) {
      const [showDialog, setShowDialog] = useState(false)
      const open = () => setShowDialog(true)
      const close = () => setShowDialog(false)

      return (
        <div>
          <button onClick={open}>Open Dialog</button>
          <Dialog isOpen={showDialog} onDismiss={close}>
            <button className="close-button" onClick={close}>
              <VisuallyHidden>Close</VisuallyHidden>
              <span aria-hidden>×</span>
            </button>
            <p>Hello there. I am a dialog</p>
          </Dialog>
        </div>
      )
    }
[/code]

## Ordering and Merging[](https://nextjs.org/docs/pages/getting-started/css#ordering-and-merging)

Next.js는 프로덕션 빌드 중에 스타일시트를 자동으로 청크(병합)하여 CSS를 최적화합니다. **CSS의 순서**는 코드에서 스타일을 **가져오는 순서**에 따라 달라집니다.

예를 들어 `<BaseButton>`이 `page.module.css`보다 먼저 가져오므로 `base-button.module.css`가 `page.module.css`보다 앞서 정렬됩니다.

page.tsx

JavaScriptTypeScript
[code]
    import { BaseButton } from './base-button'
    import styles from './page.module.css'

    export default function Page() {
      return <BaseButton className={styles.primary} />
    }
[/code]

base-button.tsx

JavaScriptTypeScript
[code]
    import styles from './base-button.module.css'

    export function BaseButton() {
      return <button className={styles.primary} />
    }
[/code]

### 권장 사항[](https://nextjs.org/docs/pages/getting-started/css#recommendations)

CSS 순서를 예측 가능하게 유지하려면 다음을 권장합니다.

  * CSS 가져오기를 하나의 JavaScript 또는 TypeScript 엔트리 파일로 모으세요.
  * 글로벌 스타일과 Tailwind 스타일시트를 애플리케이션 루트에서 가져오세요.
  * 일반적인 디자인 패턴은 유틸리티 클래스로 제공되므로 **Tailwind CSS를 주로 사용**하세요.
  * Tailwind 유틸리티로 충분하지 않을 때는 컴포넌트 전용 스타일에 CSS Modules를 사용하세요.
  * `<name>.tsx` 대신 `<name>.module.css`처럼 CSS 모듈에 일관된 명명 규칙을 사용하세요.
  * 중복 가져오기를 피하려면 공유 스타일을 공유 컴포넌트로 추출하세요.
  * ESLint의 [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports)처럼 가져오기를 자동 정렬하는 린터나 포매터는 비활성화하세요.
  * `next.config.js`의 [`cssChunking`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking) 옵션으로 CSS 청킹 방식을 제어할 수 있습니다.

## 개발 vs 프로덕션[](https://nextjs.org/docs/pages/getting-started/css#development-vs-production)

  * 개발(`next dev`)에서는 [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh)로 CSS 변경이 즉시 반영됩니다.
  * 프로덕션(`next build`)에서는 모든 CSS 파일이 자동으로 **여러 개의 미니파이되고 코드 스플릿된** `.css` 파일로 연결되어 라우트별로 필요한 최소한의 CSS만 로드됩니다.
  * 프로덕션에서는 JavaScript를 비활성화해도 CSS가 로드되지만, Fast Refresh를 위해 개발 환경에서는 JavaScript가 필요합니다.
  * CSS 순서는 개발 환경에서 다르게 동작할 수 있으므로 최종 CSS 순서를 확인하려면 항상 `next build`를 실행하세요.

## 다음 단계

이 페이지에서 언급한 기능을 더 알아보세요.

- [Tailwind CSS](https://nextjs.org/docs/pages/guides/tailwind-v3-css)
  - Tailwind CSS를 사용해 Next.js 애플리케이션을 스타일링하세요.

- [Sass](https://nextjs.org/docs/pages/guides/sass)
  - Next.js 애플리케이션에서 Sass를 사용하는 방법을 알아보세요.

- [CSS-in-JS](https://nextjs.org/docs/pages/guides/css-in-js)
  - CSS-in-JS 라이브러리를 Next.js와 함께 사용하세요.
