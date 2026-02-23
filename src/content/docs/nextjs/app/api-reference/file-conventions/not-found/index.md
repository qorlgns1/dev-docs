---
title: '파일 시스템 규칙: not-found.js'
description: '최종 업데이트: 2026년 2월 20일'
---

# 파일 시스템 규칙: not-found.js | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/not-found

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)not-found.js

페이지 복사

# not-found.js

최종 업데이트: 2026년 2월 20일

Next.js는 찾을 수 없는 상황을 처리하기 위해 두 가지 규칙을 제공합니다.

  * **`not-found.js`** : 라우트 세그먼트에서 [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) 함수를 호출할 때 사용됩니다.
  * **`global-not-found.js`** : 앱 전체에서 일치하지 않는 라우트에 대한 전역 404 페이지를 정의할 때 사용됩니다. 이는 라우팅 단계에서 처리되며 레이아웃이나 페이지 렌더링에 의존하지 않습니다.



## `not-found.js`[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#not-foundjs)

**not-found** 파일은 라우트 세그먼트 내에서 [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) 함수가 throw될 때 UI를 렌더링하는 데 사용됩니다. 커스텀 UI를 제공하는 것과 함께, Next.js는 스트리밍 응답에는 `200` HTTP 상태 코드를, 비스트리밍 응답에는 `404`를 반환합니다.

app/not-found.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'
     
    export default function NotFound() {
      return (
        <div>
          <h2>Not Found</h2>
          <p>Could not find requested resource</p>
          <Link href="/">Return Home</Link>
        </div>
      )
    }
```

## `global-not-found.js` (experimental)[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#global-not-foundjs-experimental)

`global-not-found.js` 파일을 사용하면 애플리케이션 전체에 대한 404 페이지를 정의할 수 있습니다. 라우트 수준에서 동작하는 `not-found.js`와 달리, 이 파일은 요청한 URL이 어떤 라우트와도 일치하지 않을 때 사용됩니다. Next.js는 **렌더링을 건너뛰고** 이 전역 페이지를 바로 반환합니다.

`global-not-found.js` 파일은 앱의 일반적인 렌더링 경로를 우회하므로, 404 페이지에서 필요한 전역 스타일, 폰트 또는 기타 의존성을 직접 import해야 합니다.

> **알아 두면 좋아요** : 전역 스타일의 축소 버전과 더 단순한 폰트 패밀리를 사용하면 이 페이지의 성능을 개선할 수 있습니다.

`global-not-found.js`는 `layout.js`와 `not-found.js`의 조합으로 404 페이지를 구성할 수 없을 때 유용합니다. 이런 상황은 다음 두 가지 경우에 발생할 수 있습니다.

  * 앱에 여러 루트 레이아웃(예: `app/(admin)/layout.tsx`, `app/(shop)/layout.tsx`)이 있어 단일 레이아웃로 전역 404를 구성할 수 없는 경우
  * 루트 레이아웃이 최상위 동적 세그먼트(예: `app/[country]/layout.tsx`)로 정의되어 일관된 404 페이지 구성 자체가 어려운 경우



이를 활성화하려면 `next.config.ts`에 `globalNotFound` 플래그를 추가합니다.

next.config.ts
```
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        globalNotFound: true,
      },
    }
     
    export default nextConfig
```

그런 다음 `app` 디렉터리 루트에 `app/global-not-found.js` 파일을 생성합니다.

app/global-not-found.tsx

JavaScriptTypeScript
```
    // Import global styles and fonts
    import './globals.css'
    import { Inter } from 'next/font/google'
    import type { Metadata } from 'next'
     
    const inter = Inter({ subsets: ['latin'] })
     
    export const metadata: Metadata = {
      title: '404 - Page Not Found',
      description: 'The page you are looking for does not exist.',
    }
     
    export default function GlobalNotFound() {
      return (
        <html lang="en" className={inter.className}>
          <body>
            <h1>404 - Page Not Found</h1>
            <p>This page does not exist.</p>
          </body>
        </html>
      )
    }
```

`not-found.js`와 달리, 이 파일은 `<html>`과 `<body>` 태그를 포함한 전체 HTML 문서를 반환해야 합니다.

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#props)

`not-found.js` 또는 `global-not-found.js` 컴포넌트는 어떤 props도 받지 않습니다.

> **알아 두면 좋아요** : 예상되는 `notFound()` 오류를 포착하는 것 외에도, 루트 `app/not-found.js`와 `app/global-not-found.js` 파일은 애플리케이션 전체에서 일치하지 않는 모든 URL을 처리합니다. 즉, 앱이 처리하지 않는 URL을 방문한 사용자는 해당 파일에서 export한 UI를 보게 됩니다.

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#examples)

### Data Fetching[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#data-fetching)

기본적으로 `not-found`는 서버 컴포넌트입니다. 데이터를 가져와 표시하려면 `async`로 선언할 수 있습니다.

app/not-found.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'
    import { headers } from 'next/headers'
     
    export default async function NotFound() {
      const headersList = await headers()
      const domain = headersList.get('host')
      const data = await getSiteData(domain)
      return (
        <div>
          <h2>Not Found: {data.name}</h2>
          <p>Could not find requested resource</p>
          <p>
            View <Link href="/blog">all posts</Link>
          </p>
        </div>
      )
    }
```

`usePathname` 같은 클라이언트 컴포넌트 훅으로 경로 기반 콘텐츠를 표시해야 한다면, 데이터를 클라이언트 측에서 가져와야 합니다.

### Metadata[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#metadata)

`global-not-found.js`에서는 `metadata` 객체나 [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) 함수를 export하여 404 페이지의 `<title>`, `<meta>` 및 기타 head 태그를 커스터마이즈할 수 있습니다.

> **알아 두면 좋아요** : Next.js는 `global-not-found.js` 페이지를 포함해 404 상태 코드를 반환하는 페이지에 `<meta name="robots" content="noindex" />`를 자동으로 주입합니다.

app/global-not-found.tsx

JavaScriptTypeScript
```
    import type { Metadata } from 'next'
     
    export const metadata: Metadata = {
      title: 'Not Found',
      description: 'The page you are looking for does not exist.',
    }
     
    export default function GlobalNotFound() {
      return (
        <html lang="en">
          <body>
            <div>
              <h1>Not Found</h1>
              <p>The page you are looking for does not exist.</p>
            </div>
          </body>
        </html>
      )
    }
```

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#version-history)

Version| Changes  
---|---  
`v15.4.0`| `global-not-found.js` 도입(실험 기능).  
`v13.3.0`| 루트 `app/not-found`가 전역 일치하지 않는 URL을 처리.  
`v13.0.0`| `not-found` 도입.  
  
도움이 되었나요?

지원됨.

보내기
