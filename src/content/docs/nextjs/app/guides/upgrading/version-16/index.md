---
title: '업그레이드: 버전 16'
description: '각 코딩 에이전트에 대해 MCP 클라이언트에 다음 구성을 추가하세요. 구성 세부 정보는 이 섹션을 참고하세요.'
---

# 업그레이드: 버전 16 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/upgrading/version-16

[가이드](https://nextjs.org/docs/app/guides)[업그레이드](https://nextjs.org/docs/app/guides/upgrading)버전 16

페이지 복사

# 버전 16으로 업그레이드하는 방법

마지막 업데이트: 2026년 2월 20일

## 15에서 16으로 업그레이드하기[](https://nextjs.org/docs/app/guides/upgrading/version-16#upgrading-from-15-to-16)

### Next.js DevTools MCP에서 AI 에이전트 사용하기[](https://nextjs.org/docs/app/guides/upgrading/version-16#using-ai-agents-with-nextjs-devtools-mcp)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io)을 지원하는 AI 코딩 보조 도구를 사용 중이라면 **Next.js DevTools MCP** 로 업그레이드와 마이그레이션 작업을 자동화할 수 있습니다.

#### 설정[](https://nextjs.org/docs/app/guides/upgrading/version-16#setup)

각 코딩 에이전트에 대해 MCP 클라이언트에 다음 구성을 추가하세요. 구성 세부 정보는 [이 섹션](https://github.com/vercel/next-devtools-mcp#mcp-client-configuration)을 참고하세요.

**예시:**

.mcp.json
[code]
    {
      "mcpServers": {
        "next-devtools": {
          "command": "npx",
          "args": ["-y", "next-devtools-mcp@latest"]
        }
      }
    }
[/code]

자세한 내용은 [`next-devtools-mcp`](https://github.com/vercel/next-devtools-mcp) 문서를 참조해 MCP 클라이언트를 구성하세요.

> **참고:** `next-devtools-mcp@latest` 를 사용하면 MCP 클라이언트가 항상 최신 Next.js DevTools MCP 서버 버전을 사용합니다.

#### 예시 프롬프트[](https://nextjs.org/docs/app/guides/upgrading/version-16#example-prompts)

구성이 끝나면 자연어 프롬프트로 Next.js 앱을 업그레이드할 수 있습니다.

**Next.js 16으로 업그레이드하려면:**

코딩 에이전트에 연결한 뒤 다음을 입력하세요:
[code] 
    Next Devtools, help me upgrade my Next.js app to version 16
[/code]

**Cache Components로 마이그레이션하려면(v16 업그레이드 이후):**

코딩 에이전트에 연결한 뒤 다음을 입력하세요:
[code] 
    Next Devtools, migrate my Next.js app to cache components
[/code]

문서의 [이곳](https://nextjs.org/docs/app/guides/mcp)에서 더 자세히 알아보세요.

### 코드모드 사용하기[](https://nextjs.org/docs/app/guides/upgrading/version-16#using-the-codemod)

Next.js 버전 16으로 업데이트하려면 `upgrade` [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#160)를 사용할 수 있습니다.

pnpmnpmyarnbun

터미널
[code]
    pnpm dlx @next/codemod@canary upgrade latest
[/code]

해당 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#160)는 다음을 수행합니다:

  * `next.config.js` 를 새 `turbopack` 구성으로 업데이트
  * `next lint` 에서 ESLint CLI로 마이그레이션
  * 사용 중단된 `middleware` 규칙을 `proxy` 로 마이그레이션
  * 안정화된 API에서 `unstable_` 접두사 제거
  * 페이지와 레이아웃에서 `experimental_ppr` Route Segment Config 제거



수동으로 진행하고 싶다면 최신 Next.js 및 React 버전을 설치하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add next@latest react@latest react-dom@latest
[/code]

TypeScript를 사용한다면 `@types/react` 와 `@types/react-dom` 도 최신 버전으로 업그레이드해야 합니다.

## Node.js 런타임 및 브라우저 지원[](https://nextjs.org/docs/app/guides/upgrading/version-16#nodejs-runtime-and-browser-support)

Requirement| Change / Details  
---|---  
Node.js 20.9+| 최소 버전이 `20.9.0`(LTS)로 상향; Node.js 18은 더 이상 지원되지 않음  
TypeScript 5+| 최소 버전이 `5.1.0`으로 상향  
Browsers| Chrome 111+, Edge 111+, Firefox 111+, Safari 16.4+  
  
## 기본 Turbopack[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-by-default)

**Next.js 16** 부터 Turbopack이 안정화되었으며 `next dev` 와 `next build` 에서 기본으로 사용됩니다.

이전에는 Turbopack을 사용하려면 `--turbopack` 또는 `--turbo` 플래그를 켜야 했습니다.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev --turbopack",
        "build": "next build --turbopack",
        "start": "next start"
      }
    }
[/code]

이제 더 이상 필요하지 않습니다. `package.json` 스크립트를 다음과 같이 업데이트할 수 있습니다.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start"
      }
    }
[/code]

프로젝트에 [커스텀 `webpack`](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack) 구성이 있고 `next build` (이제 기본적으로 Turbopack 사용)를 실행하면 잘못된 구성을 방지하기 위해 빌드가 **실패** 합니다.

이를 해결하는 방법은 다음과 같습니다:

  * **그대로 Turbopack 사용:** `next build --turbopack` 으로 실행해 Turbopack으로 빌드하고 `webpack` 구성을 무시합니다.
  * **완전히 Turbopack으로 전환:** `webpack` 구성을 Turbopack 호환 옵션으로 마이그레이션합니다.
  * **Webpack 유지 사용:** `--webpack` 플래그로 Turbopack을 비활성화하고 Webpack으로 빌드합니다.



> **알아두면 좋아요**: 직접 `webpack` 구성을 정의하지 않았는데도 해당 설정으로 인해 빌드가 실패한다면, 플러그인이 `webpack` 옵션을 추가했을 가능성이 큽니다.

### Turbopack 옵트아웃[](https://nextjs.org/docs/app/guides/upgrading/version-16#opting-out-of-turbopack)

Webpack을 계속 사용해야 한다면 `--webpack` 플래그로 옵트아웃할 수 있습니다. 예를 들어 개발에서는 Turbopack을 사용하고 프로덕션 빌드에서는 Webpack을 사용하려면 다음과 같이 설정합니다:

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build --webpack",
        "start": "next start"
      }
    }
[/code]

개발과 프로덕션 모두에서 Turbopack 사용을 권장합니다. Turbopack으로 전환할 수 없다면 [이 스레드](https://github.com/vercel/next.js/discussions/77721)에 의견을 남겨주세요.

### Turbopack 구성 위치[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-configuration-location)

`experimental.turbopack` 구성은 이제 실험 단계가 아닙니다.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    // Next.js 15 - experimental.turbopack
    const nextConfig: NextConfig = {
      experimental: {
        turbopack: {
          // options
        },
      },
    }
     
    export default nextConfig
[/code]

이제 최상위 `turbopack` 옵션으로 사용할 수 있습니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    // Next.js 16 - turbopack at the top level of nextConfig
    const nextConfig: NextConfig = {
      turbopack: {
        // options
      },
    }
     
    export default nextConfig
[/code]

`Turbopack` 구성 [옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)을 반드시 검토하세요. **Next.js 16** 에서는 예를 들어 다음과 같은 다양한 개선 및 신규 옵션을 제공합니다:

  * [고급 Webpack 로더 조건](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#advanced-webpack-loader-conditions)
  * [debugIds](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#debug-ids)



### resolve alias 폴백[](https://nextjs.org/docs/app/guides/upgrading/version-16#resolve-alias-fallback)

일부 프로젝트에서는 클라이언트 측 코드가 Node.js 네이티브 모듈을 포함하는 파일을 가져올 수 있습니다. 이 경우 `Module not found: Can't resolve 'fs'` 같은 오류가 발생합니다.

이럴 때는 클라이언트 번들이 이러한 Node.js 네이티브 모듈을 참조하지 않도록 코드를 리팩터링해야 합니다.

그러나 불가능한 경우도 있습니다. Webpack에서는 이러한 오류를 **무시** 하기 위해 보통 `resolve.fallback` 옵션을 사용했습니다. Turbopack에서도 `turbopack.resolveAlias` 로 유사한 옵션을 제공합니다. 이 경우 브라우저에서 `fs` 가 요청되면 빈 모듈을 로드하도록 Turbopack에 지시하세요.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      turbopack: {
        resolveAlias: {
          fs: {
            browser: './empty.ts', // We recommend to fix code imports before using this method
          },
        },
      },
    }
     
    export default nextConfig
[/code]

가능하다면 클라이언트 코드가 Node.js 네이티브 모듈을 사용하는 모듈을 절대 가져오지 않도록 리팩터링하는 것이 좋습니다.

### Sass node_modules import[](https://nextjs.org/docs/app/guides/upgrading/version-16#sass-node_modules-imports)

Turbopack은 `node_modules` 에서 Sass 파일을 가져오는 기능을 완전히 지원합니다. Webpack은 레거시 물결표(`~`) 접두사를 허용했지만 Turbopack은 이 문법을 지원하지 않습니다.

Webpack에서:

styles/globals.scss
[code]
    @import '~bootstrap/dist/css/bootstrap.min.css';
[/code]

Turbopack에서:

styles/globals.scss
[code]
    @import 'bootstrap/dist/css/bootstrap.min.css';
[/code]

임포트를 변경할 수 없다면 `turbopack.resolveAlias` 를 사용할 수 있습니다. 예를 들면 다음과 같습니다:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      turbopack: {
        resolveAlias: {
          '~*': '*',
        },
      },
    }
     
    export default nextConfig
[/code]

### Turbopack 파일 시스템 캐싱(베타)[](https://nextjs.org/docs/app/guides/upgrading/version-16#turbopack-file-system-caching-beta)

Turbopack은 이제 개발 환경에서 파일 시스템 캐싱을 지원하여 실행 간 디스크에 컴파일러 아티팩트를 저장하고 재시작 시 컴파일 시간을 크게 줄여 줍니다.

구성에서 파일 시스템 캐싱을 활성화하세요:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        turbopackFileSystemCacheForDev: true,
      },
    }
     
    export default nextConfig
[/code]

## 비동기 요청 API(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-request-apis-breaking-change)

버전 15에서는 **임시** 동기 호환성과 함께 [비동기 요청 API](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change)를 호환성 깨짐 변경 사항으로 도입했습니다.

**Next.js 16** 부터 동기 접근이 완전히 제거되어, 이 API들은 비동기 방식으로만 접근할 수 있습니다.

  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default), [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image), [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image), [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon), [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)의 `params`
  * [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)의 `searchParams`



비동기 Dynamic API로 마이그레이션하려면 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-to-async-dynamic-apis)를 사용하세요.

### 비동기 Dynamic API용 타입 마이그레이션[](https://nextjs.org/docs/app/guides/upgrading/version-16#migrating-types-for-async-dynamic-apis)

비동기 `params` 및 `searchParams` 로 마이그레이션하는 데 도움이 되도록 [`npx next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)을 실행해 전역적으로 사용할 수 있는 다음 타입 헬퍼를 자동 생성할 수 있습니다:

  * [`PageProps`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)
  * [`LayoutProps`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)
  * [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)

> **알아두면 좋아요** : `typegen`은 Next.js 15.5에서 도입되었습니다.

이는 새로운 비동기 API 패턴으로 타입 안전하게 마이그레이션하도록 단순화하고, 다음과 같이 컴포넌트를 완전한 타입 안전성으로 업데이트할 수 있게 해줍니다:

/app/blog/[slug]/page.tsx
```
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  const query = await props.searchParams
  return <h1>Blog Post: {slug}</h1>
}
```

이 방식은 `props.params`(예: `slug`)와 `searchParams`에 페이지 내부에서 완전한 타입 안전 접근을 제공합니다.

## Async parameters for icon, and open-graph Image (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-parameters-for-icon-and-open-graph-image-breaking-change)

> 이제 `opengraph-image`, `twitter-image`, `icon`, `apple-icon`의 이미지 생성 함수에 전달되는 props가 Promise입니다.

이전 버전에서는 `Image`(이미지 생성 함수)와 `generateImageMetadata` 모두 `params` 객체를 받았습니다. `generateImageMetadata`가 반환한 `id`는 문자열로 이미지 생성 함수에 전달되었습니다.

app/shop/[slug]/opengraph-image.js
```
 // Next.js 15 - synchronous params access
 export function generateImageMetadata({ params }) {
   const { slug } = params
   return [{ id: '1' }, { id: '2' }]
 }
  
 // Next.js 15 - synchronous params and id access
 export default function Image({ params, id }) {
   const slug = params.slug
   const imageId = id // string
   // ...
 }
```

**Next.js 16**부터 [Async Request APIs](https://nextjs.org/docs/app/guides/upgrading/version-16#async-request-apis-breaking-change) 변경과 일치하도록 이미지 생성 함수가 `params`와 `id`를 Promise로 받습니다. `generateImageMetadata` 함수는 계속 동기 `params`를 받습니다.

app/shop/[slug]/opengraph-image.js
```
export async function generateImageMetadata({ params }) {
  const { slug } = params
  return [{ id: '1' }, { id: '2' }]
}
 
// Next.js 16 - asynchronous params and id access
export default async function Image({ params, id }) {
  const { slug } = await params // params now async
  const imageId = await id // id is now Promise<string> when using generateImageMetadata
  // ...
}
```

## Async `id` parameter for `sitemap` (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-id-parameter-for-sitemap-breaking-change)

이전에는 [`generateSitemaps`](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)가 반환한 `id` 값이 `sitemap` 생성 함수에 바로 전달되었습니다.

app/product/sitemap.js
```
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}
 
// Next.js 15 - synchronous id access
export default async function sitemap({ id }) {
  const start = id * 50000 // id is a number
  // ...
}
```

**Next.js 16**부터 `sitemap` 생성 함수는 `id`를 Promise로 받습니다.

app/product/sitemap.js
```
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}
 
// Next.js 16 - asynchronous id access
export default async function sitemap({ id }) {
  const resolvedId = await id // id is now Promise<string>
  const start = Number(resolvedId) * 50000
  // ...
}
```

## React 19.2[](https://nextjs.org/docs/app/guides/upgrading/version-16#react-192)

**Next.js 16**의 App Router는 최신 React [Canary 릴리스](https://react.dev/blog/2023/05/03/react-canaries)를 사용하며, 새롭게 공개된 React 19.2 기능과 점진적으로 안정화 중인 기능을 포함합니다. 주요 사항:

  * **[View Transitions](https://react.dev/reference/react/ViewTransition)** : Transition 또는 내비게이션 중 업데이트되는 요소를 애니메이션 처리
  * **[`useEffectEvent`](https://react.dev/reference/react/useEffectEvent)** : 반응형이 아닌 로직을 Effect에서 추출하여 재사용 가능한 Effect Event 함수로 구성
  * **[Activity](https://react.dev/reference/react/Activity)** : `display: none`으로 UI를 숨기면서 상태를 유지하고 Effect를 정리해 “백그라운드 활동” 렌더링

자세한 내용은 [React 19.2 발표](https://react.dev/blog/2025/10/01/react-19-2)를 참고하세요.

## React Compiler Support[](https://nextjs.org/docs/app/guides/upgrading/version-16#react-compiler-support)

React Compiler 1.0 릴리스 이후 **Next.js 16**에서 React Compiler에 대한 기본 지원이 안정화되었습니다. React Compiler는 컴포넌트를 자동으로 메모이제이션하여 수동 코드 변경 없이 불필요한 재렌더를 줄입니다.

`reactCompiler` 설정 옵션이 `experimental`에서 stable로 승격되었습니다. 다양한 애플리케이션 유형에서 빌드 성능 데이터를 수집 중이므로 기본값은 비활성 상태입니다.

next.config.ts

JavaScriptTypeScript
```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  reactCompiler: true,
}
 
export default nextConfig
```

React Compiler 플러그인의 최신 버전을 설치하세요:

pnpmnpmyarnbun

Terminal
```
pnpm add -D babel-plugin-react-compiler
```

> **알아두면 좋아요:** React Compiler는 Babel에 의존하므로 이 옵션을 활성화하면 개발 및 빌드 시 컴파일 시간이 길어질 수 있습니다.

## Caching APIs[](https://nextjs.org/docs/app/guides/upgrading/version-16#caching-apis)

### revalidateTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#revalidatetag)

[`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)의 함수 시그니처가 변경되었습니다. 두 번째 인자로 [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#reference) 프로필을 전달할 수 있습니다.

app/actions.ts

JavaScriptTypeScript
```
'use server'
 
import { revalidateTag } from 'next/cache'
 
export async function updateArticle(articleId: string) {
  // Mark article data as stale - article readers see stale data while it revalidates
  revalidateTag(`article-${articleId}`, 'max')
}
```

`revalidateTag`는 블로그 글, 상품 카탈로그, 문서처럼 업데이트 지연이 허용되는 콘텐츠에 사용하세요. 사용자는 새 데이터가 백그라운드에서 로드되는 동안 오래된 콘텐츠를 받습니다.

### updateTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#updatetag)

[`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)는 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions) 전용 API로, 사용자가 변경을 수행하면 UI가 바로 최신 상태를 보여주는 **read-your-writes** 의미 체계를 제공합니다.

이는 동일한 요청 내에서 데이터를 만료시키고 즉시 새로고침합니다.

app/actions.ts

JavaScriptTypeScript
```
'use server'
 
import { updateTag } from 'next/cache'
 
export async function updateUserProfile(userId: string, profile: Profile) {
  await db.users.update(userId, profile)
 
  // Expire cache and refresh immediately - user sees their changes right away
  updateTag(`user-${userId}`)
}
```

이를 통해 폼, 사용자 설정 등 사용자 변경 사항이 즉시 반영되어야 하는 상호작용 기능에서 최신 상태를 보장합니다.

`updateTag`와 `revalidateTag`를 언제 사용할지에 대한 자세한 내용은 [여기](https://nextjs.org/docs/app/api-reference/functions/updateTag#when-to-use-updatetag)를 참고하세요.

### refresh[](https://nextjs.org/docs/app/guides/upgrading/version-16#refresh)

[`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh)는 Server Action 내부에서 클라이언트 라우터를 새로고침할 수 있게 해줍니다.

app/actions.ts

JavaScriptTypeScript
```
'use server'
 
import { refresh } from 'next/cache'
 
export async function markNotificationAsRead(notificationId: string) {
  // Update the notification in the database
  await db.notifications.markAsRead(notificationId)
 
  // Refresh the notification count displayed in the header
  refresh()
}
```

작업을 수행한 뒤 클라이언트 라우터를 새로고침해야 할 때 사용하세요.

### cacheLife and cacheTag[](https://nextjs.org/docs/app/guides/upgrading/version-16#cachelife-and-cachetag)

[`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife)와 [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)가 이제 안정화되었습니다. `unstable_` 접두사는 더 이상 필요하지 않습니다.

다음과 같이 별칭을 사용했다면:
```
import {
  unstable_cacheLife as cacheLife,
  unstable_cacheTag as cacheTag,
} from 'next/cache'
```

다음과 같이 업데이트할 수 있습니다:
```
import { cacheLife, cacheTag } from 'next/cache'
```

## Enhanced Routing and Navigation[](https://nextjs.org/docs/app/guides/upgrading/version-16#enhanced-routing-and-navigation)

**Next.js 16**은 라우팅과 내비게이션 시스템을 전면 개편하여 페이지 전환을 더 가볍고 빠르게 만들었습니다. Next.js가 내비게이션 데이터를 프리페치하고 캐시하는 방식을 최적화합니다:

  * **Layout deduplication** : 동일한 레이아웃을 공유하는 여러 URL을 프리페치할 때 해당 레이아웃을 한 번만 다운로드
  * **Incremental prefetching** : 전체 페이지 대신 캐시에 없는 부분만 프리페치

이러한 변경 사항은 **코드 수정 없이도** 모든 앱의 성능 향상을 목표로 합니다.

다만 총 전송량은 크게 줄어들면서 개별 프리페치 요청 수가 늘어날 수 있습니다. 이는 대부분의 애플리케이션에서 적절한 트레이드오프라고 판단합니다.

요청 수 증가로 문제가 발생하면 [issue](https://github.com/vercel/next.js/issues) 또는 [discussion](https://github.com/vercel/next.js/discussions)을 통해 알려주세요.

## Partial Pre-Rendering (PPR)[](https://nextjs.org/docs/app/guides/upgrading/version-16#partial-pre-rendering-ppr)

**Next.js 16**은 실험적 **Partial Pre-Rendering (PPR)** 플래그와 `experimental_ppr` 같은 구성 옵션을 제거했습니다.

**Next.js 16**부터 [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 설정을 사용해 PPR을 선택적으로 활성화할 수 있습니다.

next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}
 
module.exports = nextConfig
```

**Next.js 16**의 PPR은 **Next.js 15** 카나리아 빌드와 동작 방식이 다릅니다. 현재 PPR을 사용 중이라면 기존 Next.js 15 카나리아 버전을 유지하세요. Cache Components로 마이그레이션하는 가이드를 추후 제공할 예정입니다.

next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  // If you are using PPR today
  // stay in the current Next.js 15 canary
  experimental: {
    ppr: true,
  },
}
 
module.exports = nextConfig
```

## `middleware` to `proxy`[](https://nextjs.org/docs/app/guides/upgrading/version-16#middleware-to-proxy)

`middleware` 파일명이 더 이상 사용되지 않고, 네트워크 경계 및 라우팅 역할을 명확히 하기 위해 `proxy`로 변경되었습니다.

`proxy`에서는 `edge` 런타임을 지원하지 않습니다. `proxy` 런타임은 `nodejs`이며 설정할 수 없습니다. 계속 `edge` 런타임을 사용하려면 기존 `middleware`를 유지하세요. 향후 마이너 릴리스에서 추가 `edge` 런타임 지침을 제공할 예정입니다.

Terminal
```
# Rename your middleware file
mv middleware.ts proxy.ts
# or
mv middleware.js proxy.js
```

이름이 `middleware`인 내보내기도 더 이상 사용되지 않습니다. 함수를 `proxy`로 변경하세요.

proxy.ts

JavaScriptTypeScript
```
export function proxy(request: Request) {}
```

기본 내보내기를 사용하더라도 함수 이름을 `proxy`로 바꾸는 것이 좋습니다.

`middleware` 이름이 포함되어 있던 구성 플래그들도 함께 이름이 변경되었습니다. 예를 들어 `skipMiddlewareUrlNormalize` 는 이제 `skipProxyUrlNormalize` 입니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      skipProxyUrlNormalize: true,
    }
     
    export default nextConfig
[/code]

버전 16 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#160)는 이러한 플래그도 업데이트할 수 있습니다.

## `next/image` 변경 사항[](https://nextjs.org/docs/app/guides/upgrading/version-16#nextimage-changes)

### 쿼리 문자열이 있는 로컬 이미지(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#local-images-with-query-strings-breaking-change)

열거형 공격을 방지하기 위해 이제 쿼리 문자열이 포함된 로컬 이미지 소스에는 `images.localPatterns.search` 구성이 필요합니다.

app/page.tsx
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image src="/assets/photo?v=1" alt="Photo" width="100" height="100" />
    }
[/code]

로컬 이미지에서 쿼리 문자열을 사용해야 한다면, 구성에 다음 패턴을 추가하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        localPatterns: [
          {
            pathname: '/assets/**',
            search: '?v=1',
          },
        ],
      },
    }
     
    export default nextConfig
[/code]

### `minimumCacheTTL` 기본값(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#minimumcachettl-default-breaking-change)

`images.minimumCacheTTL`의 기본값이 `60 seconds`에서 `4 hours`(14400초)로 변경되었습니다. 이는 캐시 제어 헤더가 없는 이미지의 재검증 비용을 줄여 줍니다.

일부 Next.js 사용자에게서는 업스트림 소스 이미지에 `cache-control` 헤더가 없어서 이미지 재검증이 매우 자주 발생했습니다. 그 결과 매 `60`초마다 재검증이 수행되어 CPU 사용량과 비용이 증가했습니다.

대부분의 이미지는 자주 변경되지 않으므로, 이 짧은 간격은 비효율적입니다. 기본값을 4시간으로 설정하면 필요한 경우 하루에 몇 번씩 이미지를 업데이트할 수 있으면서도 기본적으로 더 오래 지속되는 캐시를 제공합니다.

이전 동작이 필요하다면 `minimumCacheTTL`을 낮은 값으로 조정하세요. 예를 들어 다시 `60`초로 되돌릴 수 있습니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        minimumCacheTTL: 60,
      },
    }
     
    export default nextConfig
[/code]

### `imageSizes` 기본값(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#imagesizes-default-breaking-change)

기본 `images.imageSizes` 배열에서 값 `16`이 제거되었습니다.

요청 분석 결과, 실제로 16픽셀 너비의 이미지를 제공하는 프로젝트는 거의 없었습니다. 이 설정을 제거하면 `next/image`가 브라우저로 전송하는 `srcset` 속성의 크기를 줄일 수 있습니다.

16px 이미지를 지원해야 한다면 다음을 참고하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
      },
    }
     
    export default nextConfig
[/code]

개발자 사용 부족 때문이 아니라, `devicePixelRatio: 2`가 실제로는 레티나 디스플레이의 흐릿함을 방지하기 위해 32px 이미지를 가져오기 때문에 16픽셀 너비 이미지가 덜 일반적이 되었다고 판단합니다.

### `qualities` 기본값(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#qualities-default-breaking-change)

`images.qualities`의 기본값이 모든 품질을 허용하던 것에서 `[75]`만 허용하도록 변경되었습니다.

여러 품질 수준을 지원해야 한다면 다음과 같이 구성하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        qualities: [50, 75, 100],
      },
    }
     
    export default nextConfig
[/code]

`image.qualities` 배열에 포함되지 않은 `quality` prop을 지정하면, 해당 품질은 `images.qualities`에서 가장 가까운 값으로 강제 변환됩니다. 예를 들어 위 구성에서 `quality` prop이 80이면 75로 변환됩니다.

### 로컬 IP 제한(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#local-ip-restriction-breaking-change)

새로운 보안 제한이 기본적으로 로컬 IP 최적화를 차단합니다. `images.dangerouslyAllowLocalIP`를 `true`로 설정하는 것은 비공개 네트워크에만 사용하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        dangerouslyAllowLocalIP: true, // 비공개 네트워크에서만 사용
      },
    }
     
    export default nextConfig
[/code]

### 최대 리디렉션(호환성 깨짐)[](https://nextjs.org/docs/app/guides/upgrading/version-16#maximum-redirects-breaking-change)

`images.maximumRedirects`의 기본값이 무제한에서 최대 3회 리디렉션으로 변경되었습니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      images: {
        maximumRedirects: 0, // 리디렉션 비활성화
        // 또는
        maximumRedirects: 5, // 에지 케이스에 대비해 증가
      },
    }
     
    export default nextConfig
[/code]

### `next/legacy/image` 컴포넌트(사용 중단)[](https://nextjs.org/docs/app/guides/upgrading/version-16#nextlegacyimage-component-deprecated)

`next/legacy/image` 컴포넌트는 사용 중단되었습니다. 대신 `next/image`를 사용하세요.
[code] 
    // Before
    import Image from 'next/legacy/image'
     
    // After
    import Image from 'next/image'
[/code]

### `images.domains` 구성(사용 중단)[](https://nextjs.org/docs/app/guides/upgrading/version-16#imagesdomains-configuration-deprecated)

`images.domains` 구성은 사용 중단되었습니다.

next.config.js
[code]
    // image.domains는 사용 중단되었습니다
    module.exports = {
      images: {
        domains: ['example.com'],
      },
    }
[/code]

보안 향상을 위해 대신 `images.remotePatterns`를 사용하세요.

next.config.js
[code]
    // image.remotePatterns를 사용하세요
    module.exports = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 'example.com',
          },
        ],
      },
    }
[/code]

## 동시 `dev` 및 `build`[](https://nextjs.org/docs/app/guides/upgrading/version-16#concurrent-dev-and-build)

`next dev`와 `next build`가 이제 별도의 출력 디렉터리를 사용하여 동시에 실행할 수 있습니다. `next dev` 명령은 `.next/dev`에 출력합니다. 이는 [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)로 제어되는 새로운 기본 동작입니다.

또한 잠금 파일 메커니즘이 동일 프로젝트에서 여러 `next dev` 또는 `next build` 인스턴스를 방지합니다.

개발 서버가 `.next/dev`에 출력하므로 [Turbopack 추적 명령](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing)은 다음과 같아야 합니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm next internal trace .next/dev/trace-turbopack
[/code]

## 병렬 라우트 `default.js` 요구 사항[](https://nextjs.org/docs/app/guides/upgrading/version-16#parallel-routes-defaultjs-requirement)

모든 [병렬 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes) 슬롯에 명시적인 `default.js` 파일이 필요합니다. 해당 파일이 없으면 빌드가 실패합니다.

이전 동작을 유지하려면 [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default) 파일을 만들고 `notFound()`를 호출하거나 `null`을 반환하도록 하세요.

app/@modal/default.tsx
[code]
    import { notFound } from 'next/navigation'
     
    export default function Default() {
      notFound()
    }
[/code]

또는 `null`을 반환할 수 있습니다.

app/@modal/default.tsx
[code]
    export default function Default() {
      return null
    }
[/code]

## ESLint Flat Config[](https://nextjs.org/docs/app/guides/upgrading/version-16#eslint-flat-config)

`@next/eslint-plugin-next`는 이제 기본적으로 ESLint Flat Config 형식을 사용하며, 레거시 구성 지원을 중단할 ESLint v10에 맞춰집니다.

[`@next/eslint-plugin-next`](https://nextjs.org/docs/app/api-reference/config/eslint#setup-eslint) 플러그인의 API 레퍼런스를 반드시 확인하세요.

레거시 `.eslintrc` 형식을 사용 중이라면 플랫 구성 형식으로 마이그레이션하는 것을 고려하세요. 자세한 내용은 [ESLint 마이그레이션 가이드](https://eslint.org/docs/latest/use/configure/migration-guide)를 참고하세요.

## 스크롤 동작 오버라이드[](https://nextjs.org/docs/app/guides/upgrading/version-16#scroll-behavior-override)

**이전 버전의 Next.js**에서는 CSS로 `<html>` 요소에 전역적으로 `scroll-behavior: smooth`를 설정해도 Next.js가 SPA 라우트 전환 중 다음과 같이 이를 오버라이드했습니다.

  1. 일시적으로 `scroll-behavior`를 `auto`로 설정
  2. 내비게이션 수행(즉시 맨 위로 스크롤)
  3. 원래 `scroll-behavior` 값 복원



이 동작은 페이지 내비게이션이 스무스 스크롤을 사용할 때에도 항상 빠르고 즉각적으로 느껴지도록 보장했습니다. 그러나 이러한 조작은 특히 내비게이션 시작 시 비용이 클 수 있었습니다.

**Next.js 16**에서는 이 동작이 변경되었습니다. 기본적으로 Next.js는 내비게이션 중 더 이상 `scroll-behavior` 설정을 오버라이드하지 않습니다.

**이전 기본 동작인 오버라이드를 원한다면**, `<html>` 요소에 `data-scroll-behavior="smooth"` 속성을 추가하세요.

app/layout.tsx
[code]
    export default function RootLayout({ children }) {
      return (
        <html lang="en" data-scroll-behavior="smooth">
          <body>{children}</body>
        </html>
      )
    }
[/code]

## 성능 향상[](https://nextjs.org/docs/app/guides/upgrading/version-16#performance-improvements)

`next dev` 및 `next start` 명령의 성능이 크게 최적화되었으며, 더 명확한 형식의 터미널 출력, 향상된 오류 메시지, 개선된 성능 지표가 제공됩니다.

**Next.js 16**은 `next build` 출력에서 `size`와 `First Load JS` 지표를 제거했습니다. 이는 React Server Components를 사용하는 서버 중심 아키텍처에서 부정확하다고 판단했기 때문입니다. Turbopack과 Webpack 구현 모두 문제가 있었고, 클라이언트 컴포넌트 페이로드를 계산하는 방식도 서로 달랐습니다.

실제 라우트 성능을 측정하는 가장 효과적인 방법은 [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)나 Core Web Vitals 및 다운로드된 리소스 크기에 집중하는 Vercel Analytics 같은 도구를 사용하는 것입니다.

### `next dev` 구성 로드[](https://nextjs.org/docs/app/guides/upgrading/version-16#next-dev-config-load)

이전 버전에서는 개발 중 Next 구성 파일이 두 번 로드되었습니다.

  * `next dev` 명령을 실행할 때
  * `next dev` 명령이 Next.js 서버를 시작할 때



`next dev` 명령이 Next.js 서버를 시작하기 위해 구성 파일을 필요로 하지 않기 때문에 이는 비효율적이었습니다.

이 변경의 결과로, `next dev` 실행 시 Next.js 구성 파일에서 `process.argv`에 `'dev'`가 포함되어 있는지 확인하면 `false`를 반환합니다.

> **알아두면 좋습니다** : `typegen` 및 `build` 명령은 여전히 `process.argv`에 표시됩니다.

이는 `next dev`에서 부작용을 트리거하는 플러그인에 특히 중요합니다. 그런 경우 `NODE_ENV`가 `development`로 설정되어 있는지만 확인해도 충분할 수 있습니다.

next.config.js
[code]
    import { startServer } from 'docs-lib/dev-server'
     
    const isDev = process.env.NODE_ENV === 'development'
     
    if (isDev) {
      startServer()
    }
     
    const nextConfig = {
      /* Your config options */
    }
     
    module.exports = nextConfig
[/code]

또는 구성이 로드되는 [`phase`](https://nextjs.org/docs/app/api-reference/config/next-config-js#phase)를 활용하세요.

## Build Adapters API (alpha)[](https://nextjs.org/docs/app/guides/upgrading/version-16#build-adapters-api-alpha)

[Build Adapters RFC](https://github.com/vercel/next.js/discussions/77740)에 따라 Build Adapters API의 첫 번째 알파 버전이 출시되었습니다.

Build Adapter를 사용하면 빌드 프로세스에 연결되는 맞춤형 어댑터를 만들 수 있어, 배포 플랫폼과 맞춤형 빌드 통합이 Next.js 구성을 수정하거나 빌드 출력을 처리할 수 있습니다.

next.config.js
[code]
    const nextConfig = {
      experimental: {
        adapterPath: require.resolve('./my-adapter.js'),
      },
    }
     
    module.exports = nextConfig
[/code]

[RFC 토론](https://github.com/vercel/next.js/discussions/77740)에서 의견을 공유해 주세요.

## Modern Sass API[](https://nextjs.org/docs/app/guides/upgrading/version-16#modern-sass-api)

`sass-loader`가 v16으로 올라가 [현대 Sass 문법](https://sass-lang.com/documentation/js-api/#md:usage)과 새로운 기능을 지원합니다.

## Removals[](https://nextjs.org/docs/app/guides/upgrading/version-16#removals)

이전 버전에서 사용 중단(deprecated)되었던 기능들이 이제 완전히 제거되었습니다.

### AMP Support[](https://nextjs.org/docs/app/guides/upgrading/version-16#amp-support)

AMP 채택률이 크게 감소했고, 이 기능을 유지하면 프레임워크 복잡도가 커지기 때문에 모든 AMP API와 구성이 제거되었습니다.

  * Next 구성 파일의 `amp` 설정
  * `next/amp` 훅 import 및 사용(`useAmp`)

[code] 
    // Removed
    import { useAmp } from 'next/amp'
     
    // Removed
    export const config = { amp: true }
[/code]

  * 페이지의 `export const config = { amp: true }` 선언

next.config.js
[code]
    const nextConfig = {
      // Removed
      amp: {
        canonicalBase: 'https://example.com',
      },
    }
     
    export default nextConfig
[/code]

AMP가 여전히 필요한지 평가해 보세요. 이제 대부분의 성능 이점은 Next.js의 기본 최적화와 최신 웹 표준으로 얻을 수 있습니다.

### `next lint` Command[](https://nextjs.org/docs/app/guides/upgrading/version-16#next-lint-command)

`next lint` 명령이 제거되었습니다. Biome 또는 ESLint를 직접 사용해 주세요. `next build`는 더 이상 린팅을 실행하지 않습니다.

마이그레이션 자동화를 위한 codemod가 제공됩니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm dlx @next/codemod@canary next-lint-to-eslint-cli .
[/code]

Next.js 구성 파일의 `eslint` 옵션도 제거되었습니다.

next.config.mjs
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // No longer supported
      // eslint: {},
    }
     
    export default nextConfig
[/code]

### Runtime Configuration[](https://nextjs.org/docs/app/guides/upgrading/version-16#runtime-configuration)

`serverRuntimeConfig`와 `publicRuntimeConfig`가 제거되었습니다. 대신 환경 변수를 사용하세요.

**이전(Next.js 15):**

next.config.js
[code]
    module.exports = {
      serverRuntimeConfig: {
        dbUrl: process.env.DATABASE_URL,
      },
      publicRuntimeConfig: {
        apiUrl: '/api',
      },
    }
[/code]

pages/index.tsx
[code]
    import getConfig from 'next/config'
     
    export default function Page() {
      const { publicRuntimeConfig } = getConfig()
      return <p>API URL: {publicRuntimeConfig.apiUrl}</p>
    }
[/code]

**이후(Next.js 16):**

서버 전용 값은 Server Component에서 환경 변수를 직접 읽으세요.

app/page.tsx
[code]
    async function fetchData() {
      const dbUrl = process.env.DATABASE_URL
      // Use for server-side operations only
      return await db.query(dbUrl, 'SELECT * FROM users')
    }
     
    export default async function Page() {
      const data = await fetchData()
      return <div>{/* render data */}</div>
    }
[/code]

> **알아두면 좋아요**: [taint API](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint)를 사용해 실수로 민감한 서버 값을 Client Component에 전달하지 않도록 하세요.

클라이언트에서 접근 가능한 값은 `NEXT_PUBLIC_` 접두사를 사용하세요.

.env.local
[code]
    NEXT_PUBLIC_API_URL="/api"
[/code]

app/components/client-component.tsx
[code]
    'use client'
     
    export default function ClientComponent() {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL
      return <p>API URL: {apiUrl}</p>
    }
[/code]

환경 변수가 런타임에 읽히도록(빌드 타임 번들 제외) 하려면 `process.env`에 접근하기 전에 [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) 함수를 호출하세요.

app/page.tsx
[code]
    import { connection } from 'next/server'
     
    export default async function Page() {
      await connection()
      const config = process.env.RUNTIME_CONFIG
      return <p>{config}</p>
    }
[/code]

[환경 변수](https://nextjs.org/docs/app/guides/environment-variables)에 대해 더 알아보세요.

### `devIndicators` Options[](https://nextjs.org/docs/app/guides/upgrading/version-16#devindicators-options)

[`devIndicators`](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)에서 다음 옵션이 제거되었습니다.

  * `appIsrStatus`
  * `buildActivity`
  * `buildActivityPosition`

인디케이터 자체는 계속 사용할 수 있습니다.

### `experimental.dynamicIO`[](https://nextjs.org/docs/app/guides/upgrading/version-16#experimentaldynamicio)

`experimental.dynamicIO` 플래그 이름이 `cacheComponents`로 변경되었습니다.

Next 구성 파일에서 `dynamicIO` 플래그를 제거하세요.

next.config.js
[code]
    // Next.js 15 - experimental.dynamicIO is now removed
    module.exports = {
      experimental: {
        dynamicIO: true,
      },
    }
[/code]

[`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) 플래그를 true로 추가하세요.

next.config.js
[code]
    // Next.js 16 - use cacheComponents instead
    module.exports = {
      cacheComponents: true,
    }
[/code]

### `unstable_rootParams`[](https://nextjs.org/docs/app/guides/upgrading/version-16#unstable_rootparams)

`unstable_rootParams` 함수가 제거되었습니다. 곧 출시될 마이너 릴리스에서 대체 API를 제공할 예정입니다.

도움이 되었나요?

지원됨.

보내기
