---
title: '@next/third-parties/google를 통한 Next.js에서의 Google Analytics 사용'
description: '> Google Analytics와 Tag Manager를 위해 인라인 스크립트를 사용할 때는 를 우선적으로 사용하세요.'
---

# `@next/third-parties/google`를 통한 Next.js에서의 Google Analytics 사용 | Next.js

Source URL: https://nextjs.org/docs/messages/next-script-for-ga

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)`@next/third-parties/google`를 통한 Next.js에서의 Google Analytics 사용

# `@next/third-parties/google`를 통한 Next.js에서의 Google Analytics 사용

> Google Analytics와 Tag Manager를 위해 인라인 스크립트를 사용할 때는 `@next/third-parties/google`를 우선적으로 사용하세요.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/next-script-for-ga#why-this-error-occurred)

Google Analytics를 위해 인라인 스크립트가 사용되어 웹페이지 성능에 영향을 줄 수 있습니다. 대신 `@next/third-parties` 라이브러리의 `next/script` 사용을 권장합니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/next-script-for-ga#possible-ways-to-fix-it)

### Google Analytics를 추가하려면 `@next/third-parties`를 사용하세요[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-analytics)

**`@next/third-parties`**는 Next.js 애플리케이션에서 널리 사용되는 서드파티 라이브러리를 로드할 때 성능과 개발자 경험을 개선하는 컴포넌트 및 유틸리티 모음입니다. Next.js 14( `next@latest` 설치)에서 사용할 수 있습니다.

`GoogleAnalytics` 컴포넌트는 Google 태그(`gtag.js`)를 통해 페이지에 [Google Analytics 4](https://developers.google.com/analytics/devguides/collection/ga4)를 포함할 때 사용할 수 있습니다. 기본적으로 페이지에서 하이드레이션이 완료된 후 원본 스크립트를 가져옵니다.

> **권장 사항**: 애플리케이션에 이미 Google Tag Manager가 포함되어 있다면 Google Analytics를 별도 컴포넌트로 추가하는 대신 Tag Manager 안에서 직접 구성할 수 있습니다. Tag Manager와 `gtag.js`의 차이점은 [문서](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm)를 참고하세요.

모든 라우트에서 Google Analytics를 로드하려면 루트 레이아웃에 컴포넌트를 직접 포함하고 측정 ID를 전달하세요:

app/layout.tsx

JavaScriptTypeScript
```
    import { GoogleAnalytics } from '@next/third-parties/google'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
          <GoogleAnalytics gaId="G-XYZ" />
        </html>
      )
    }
```

단일 라우트에서 Google Analytics를 로드하려면 페이지 파일에 컴포넌트를 포함하세요:

app/page.js
```
    import { GoogleAnalytics } from '@next/third-parties/google'

    export default function Page() {
      return <GoogleAnalytics gaId="G-XYZ" />
    }
```

### Google Tag Manager를 추가하려면 `@next/third-parties`를 사용하세요[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-tag-manager)

`GoogleTagManager` 컴포넌트는 페이지에 [Google Tag Manager](https://developers.google.com/tag-manager/quickstart)를 추가할 때 사용할 수 있습니다.

app/layout.tsx

JavaScriptTypeScript
```
    import { GoogleTagManager } from '@next/third-parties/google'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <GoogleTagManager gtmId="GTM-XYZ" />
          <body>{children}</body>
        </html>
      )
    }
```

단일 라우트에서 Google Tag Manager를 로드하려면 페이지 파일에 컴포넌트를 포함하세요:

app/page.js
```
    import { GoogleTagManager } from '@next/third-parties/google'

    export default function Page() {
      return <GoogleTagManager gtmId="GTM-XYZ" />
    }
```

## 알아두면 좋은 점[](https://nextjs.org/docs/messages/next-script-for-ga#good-to-know)

- Pages Router를 사용하는 경우 [`pages/` 문서](https://nextjs.org/docs/pages/guides/third-party-libraries)를 참고하세요.
- `@next/third-parties`는 [다른 서드파티](https://nextjs.org/docs/app/guides/third-party-libraries#google-tag-manager)도 지원합니다.
- `@next/third-parties` 사용은 필수가 아닙니다. `next/script` 컴포넌트를 직접 사용할 수도 있습니다. 자세한 내용은 [`next/script` 문서](https://nextjs.org/docs/app/guides/scripts)를 참조하세요.

## 유용한 링크[](https://nextjs.org/docs/messages/next-script-for-ga#useful-links)

- [`@next/third-parties` 문서](https://nextjs.org/docs/app/guides/third-party-libraries)
- [`next/script` 문서](https://nextjs.org/docs/app/guides/scripts)

Was this helpful?

supported.

Send