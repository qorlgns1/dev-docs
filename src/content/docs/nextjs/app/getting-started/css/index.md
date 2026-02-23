---
title: '시작하기: CSS'
description: 'Next.js는 다음과 같이 애플리케이션을 CSS로 스타일링할 수 있는 여러 방법을 제공합니다:'
---

# 시작하기: CSS | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/css

Copy page

# CSS

최종 업데이트 2026년 2월 20일

Next.js는 다음과 같이 애플리케이션을 CSS로 스타일링할 수 있는 여러 방법을 제공합니다:

  * [Tailwind CSS](https://nextjs.org/docs/app/getting-started/css#tailwind-css)
  * [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)
  * [Global CSS](https://nextjs.org/docs/app/getting-started/css#global-css)
  * [External Stylesheets](https://nextjs.org/docs/app/getting-started/css#external-stylesheets)
  * [Sass](https://nextjs.org/docs/app/guides/sass)
  * [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)

## Tailwind CSS[](https://nextjs.org/docs/app/getting-started/css#tailwind-css)

[Tailwind CSS](https://tailwindcss.com/)는 커스텀 디자인을 구축할 수 있도록 저수준 유틸리티 클래스를 제공하는 유틸리티 우선 CSS 프레임워크입니다.

Tailwind CSS 설치:

pnpmnpmyarnbun

터미널
```
    pnpm add -D tailwindcss @tailwindcss/postcss
```

`postcss.config.mjs` 파일에 PostCSS 플러그인을 추가하세요:

postcss.config.mjs
```
    export default {
      plugins: {
        '@tailwindcss/postcss': {},
      },
    }
```

글로벌 CSS 파일에서 Tailwind를 가져옵니다:

app/globals.css
```
    @import 'tailwindcss';
```

루트 레이아웃에서 해당 CSS 파일을 가져옵니다:

app/layout.tsx

JavaScriptTypeScript
```
    import './globals.css'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
```

이제 애플리케이션에서 Tailwind 유틸리티 클래스를 사용할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
```
    export default function Page() {
      return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
          <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
        </main>
      )
    }
```

> **알아두면 좋아요:** 매우 오래된 브라우저까지 폭넓게 지원해야 한다면 [Tailwind CSS v3 설정 가이드](https://nextjs.org/docs/app/guides/tailwind-v3-css)를 확인하세요.

## CSS Modules[](https://nextjs.org/docs/app/getting-started/css#css-modules)

CSS Modules는 고유한 클래스 이름을 생성해 CSS를 로컬 범위로 제한합니다. 이를 통해 이름 충돌을 걱정하지 않고 서로 다른 파일에서 동일한 클래스를 사용할 수 있습니다.

CSS Modules를 시작하려면 `.module.css` 확장자를 가진 새 파일을 만들고 `app` 디렉터리 내부의 컴포넌트에서 가져오면 됩니다:

app/blog/blog.module.css
```
    .blog {
      padding: 24px;
    }
```

app/blog/page.tsx

JavaScriptTypeScript
```
    import styles from './blog.module.css'

    export default function Page() {
      return <main className={styles.blog}></main>
    }
```

## Global CSS[](https://nextjs.org/docs/app/getting-started/css#global-css)

글로벌 CSS를 사용해 애플리케이션 전반에 스타일을 적용할 수 있습니다.

`app/global.css` 파일을 만들고 루트 레이아웃에서 가져오면 애플리케이션의 **모든 라우트**에 스타일이 적용됩니다:

app/global.css
```
    body {
      padding: 20px 20px 60px;
      max-width: 680px;
      margin: 0 auto;
    }
```

app/layout.tsx

JavaScriptTypeScript
```
    // These styles apply to every route in the application
    import './global.css'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
```

> **알아두면 좋아요:** 글로벌 스타일은 `app` 디렉터리 안의 어떤 레이아웃, 페이지, 컴포넌트에서도 가져올 수 있습니다. 하지만 Next.js는 Suspense와 통합하기 위해 React에 내장된 스타일시트 지원을 사용하므로, 라우트 간 내비게이션 시 스타일시트가 제거되지 않아 충돌이 발생할 수 있습니다. 진정한 글로벌 CSS(예: Tailwind의 기본 스타일)에는 글로벌 스타일을, 컴포넌트 스타일링에는 [Tailwind CSS](https://nextjs.org/docs/app/getting-started/css#tailwind-css)를, 필요할 때 커스텀 범위 CSS에는 [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)을 사용하는 것을 권장합니다.

## External stylesheets[](https://nextjs.org/docs/app/getting-started/css#external-stylesheets)

외부 패키지가 배포한 스타일시트는 `app` 디렉터리 어디에서나, 코로케이션된 컴포넌트를 포함해 가져올 수 있습니다:

app/layout.tsx

JavaScriptTypeScript
```
    import 'bootstrap/dist/css/bootstrap.css'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body className="container">{children}</body>
        </html>
      )
    }
```

> **알아두면 좋아요:** React 19에서는 `<link rel="stylesheet" href="..." />`도 사용할 수 있습니다. 자세한 내용은 [React `link` 문서](https://react.dev/reference/react-dom/components/link)를 참고하세요.

## Ordering and Merging[](https://nextjs.org/docs/app/getting-started/css#ordering-and-merging)

Next.js는 프로덕션 빌드 중 스타일시트를 자동으로 청킹(병합)하여 CSS를 최적화합니다. **CSS의 순서**는 코드에서 **스타일을 가져오는 순서**에 따라 결정됩니다.

예를 들어 `<BaseButton>`을 `page.module.css`보다 먼저 가져오므로 `base-button.module.css`가 `page.module.css`보다 먼저 정렬됩니다:

page.tsx

JavaScriptTypeScript
```
    import { BaseButton } from './base-button'
    import styles from './page.module.css'

    export default function Page() {
      return <BaseButton className={styles.primary} />
    }
```

base-button.tsx

JavaScriptTypeScript
```
    import styles from './base-button.module.css'

    export function BaseButton() {
      return <button className={styles.primary} />
    }
```

### Recommendations[](https://nextjs.org/docs/app/getting-started/css#recommendations)

CSS 순서를 예측 가능하게 유지하려면:

  * CSS 가져오기를 단일 JavaScript 또는 TypeScript 엔트리 파일로 모으려고 노력하세요.
  * 애플리케이션 루트에서 글로벌 스타일과 Tailwind 스타일시트를 가져오세요.
  * 대부분의 스타일링에는 유틸리티 클래스로 일반적인 디자인 패턴을 다루는 **Tailwind CSS를 사용**하세요.
  * Tailwind 유틸리티만으로 충분하지 않을 때 컴포넌트 전용 스타일은 CSS Modules를 활용하세요.
  * CSS 모듈에 일관된 네이밍 규칙을 사용하세요. 예를 들어 `<name>.tsx` 대신 `<name>.module.css`를 사용하세요.
  * 중복 가져오기를 피하려면 공용 스타일을 공용 컴포넌트로 추출하세요.
  * ESLint의 [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports)처럼 가져오기를 자동 정렬하는 린터나 포매터는 끄세요.
  * CSS 청킹 방식을 제어하려면 `next.config.js`에서 [`cssChunking`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking) 옵션을 사용할 수 있습니다.

## Development vs Production[](https://nextjs.org/docs/app/getting-started/css#development-vs-production)

  * 개발(`next dev`)에서는 [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh) 덕분에 CSS 업데이트가 즉시 적용됩니다.
  * 프로덕션(`next build`)에서는 모든 CSS 파일이 자동으로 **여러 개의 최소화되고 코드가 분할된** `.css` 파일로 병합되어 라우트에 필요한 최소한의 CSS만 로드됩니다.
  * 프로덕션에서는 JavaScript가 비활성화되어도 CSS가 로드되지만, 개발에서는 Fast Refresh를 위해 JavaScript가 필요합니다.
  * 개발과 프로덕션 간에 CSS 순서가 다르게 동작할 수 있으니, 최종 CSS 순서를 확인하려면 항상 빌드(`next build`)를 점검하세요.

## Next Steps

애플리케이션에서 CSS를 사용하는 다양한 방법을 더 알아보세요.

- [Tailwind CSS v3](https://nextjs.org/docs/app/guides/tailwind-v3-css)
  - Tailwind CSS v3를 사용해 Next.js 애플리케이션을 스타일링하고 더 넓은 브라우저 호환성을 확보하세요.

- [Sass](https://nextjs.org/docs/app/guides/sass)
  - Sass를 사용해 Next.js 애플리케이션을 스타일링하세요.

- [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)
  - CSS-in-JS 라이브러리를 Next.js와 함께 사용하세요

supported.

Send