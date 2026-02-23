---
title: '파일 시스템 규칙: loading.js'
description: '특수 파일 는 React Suspense를 사용해 의미 있는 로딩 UI를 만들도록 도와줍니다. 이 규칙을 사용하면 경로 세그먼트의 콘텐츠가 스트리밍되는 동안 서버에서 즉시 로딩 상태를 표시할 수 있습니다. 새 콘텐츠가 완료되면 자동으로 교체됩니다.'
---

# 파일 시스템 규칙: loading.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/loading

# loading.js

마지막 업데이트 2026년 2월 20일

특수 파일 `loading.js`는 [React Suspense](https://react.dev/reference/react/Suspense)를 사용해 의미 있는 로딩 UI를 만들도록 도와줍니다. 이 규칙을 사용하면 경로 세그먼트의 콘텐츠가 스트리밍되는 동안 서버에서 [즉시 로딩 상태](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states)를 표시할 수 있습니다. 새 콘텐츠가 완료되면 자동으로 교체됩니다.

app/feed/loading.tsx

JavaScriptTypeScript
```
    export default function Loading() {
      // Or a custom loading skeleton component
      return <p>Loading...</p>
    }
```

`loading.js` 파일 내부에는 가벼운 로딩 UI를 자유롭게 추가할 수 있습니다. [React Developer Tools](https://react.dev/learn/react-developer-tools)를 사용해 직접 Suspense 경계를 토글해 보는 것도 도움이 됩니다.

기본적으로 이 파일은 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)이지만 `"use client"` 지시문을 통해 클라이언트 컴포넌트로도 사용할 수 있습니다.

## 참고[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#reference)

### 매개변수[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#parameters)

로딩 UI 컴포넌트는 매개변수를 받지 않습니다.

## 동작[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#behavior)

### 내비게이션[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#navigation)

- Fallback UI는 [사전 패치](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)되어, 사전 패치가 완료되지 않은 경우를 제외하곤 즉시 내비게이션이 이뤄집니다.
- 내비게이션은 중단 가능하므로, 다른 경로로 이동하기 전에 현재 경로 콘텐츠가 완전히 로드될 때까지 기다릴 필요가 없습니다.
- 공유 레이아웃은 새로운 경로 세그먼트가 로드되는 동안에도 상호작용 상태를 유지합니다.

### Instant Loading States[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states)

Instant loading state는 내비게이션 직후 즉시 표시되는 Fallback UI입니다. 스켈레톤이나 스피너 같은 로딩 인디케이터, 혹은 커버 사진이나 제목처럼 미래 화면의 작지만 의미 있는 일부를 사전 렌더링할 수 있습니다. 이는 앱이 응답 중임을 사용자에게 알려 더 나은 경험을 제공합니다.

폴더 안에 `loading.js` 파일을 추가해 로딩 상태를 만듭니다.

app/dashboard/loading.tsx

JavaScriptTypeScript
```
    export default function Loading() {
      // You can add any UI inside Loading, including a Skeleton.
      return <LoadingSkeleton />
    }
```

같은 폴더에서 `loading.js`는 `layout.js` 안에 중첩됩니다. 이는 `page.js` 및 그 하위 자식을 `<Suspense>` 경계로 자동 래핑합니다.

### SEO[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#seo)

- 전체 브라우저처럼 JavaScript를 실행하지 못하고 정적 HTML만 수집하는 Twitterbot 등의 봇에 대해서는, 스트리밍 UI 전에 Next.js가 [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)를 해결하고, 초기 HTML의 `<head>`에 메타데이터를 배치합니다.
- 그 외 경우에는 [스트리밍 메타데이터](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata)를 사용할 수 있습니다. Next.js는 사용자 에이전트를 자동 감지해 차단(blocking) 또는 스트리밍 동작을 선택합니다.
- 스트리밍은 서버 렌더링이므로 SEO에 영향을 주지 않습니다. Google의 [Rich Results Test](https://search.google.com/test/rich-results) 도구를 사용해 페이지가 Google 웹 크롤러에 어떻게 표시되는지 확인하고 직렬화된 HTML을 볼 수 있습니다([출처](https://web.dev/rendering-on-the-web/#seo-considerations)).

### 상태 코드[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#status-codes)

스트리밍 시 요청 성공을 알리기 위해 `200` 상태 코드가 반환됩니다.

서버는 [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect)나 [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found)를 사용할 때처럼 스트리밍된 콘텐츠 내에서 여전히 오류나 문제를 클라이언트에 전달할 수 있습니다. 응답 헤더가 이미 클라이언트로 전송된 이후에는 상태 코드를 갱신할 수 없습니다.

예를 들어 404 페이지가 클라이언트로 스트리밍될 때 Next.js는 스트리밍된 HTML에 `<meta name="robots" content="noindex">` 태그를 포함합니다. 이는 HTTP 상태가 200이라도 검색 엔진이 해당 URL을 색인하지 못하도록 합니다. [`robots` 메타 태그](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)에 대한 Google 지침을 참고하세요.

일부 크롤러는 이러한 응답을 “soft 404”로 표시할 수 있습니다. 스트리밍의 경우 HTML에서 명시적으로 `noindex`로 지정되므로 인덱싱으로 이어지지 않습니다.

규정 준수나 분석을 위해 404 상태가 필요하다면, 응답 본문을 스트리밍하기 전에 리소스 존재 여부를 확인해 서버가 HTTP 상태 코드를 설정할 수 있도록 하세요.

누락된 슬러그를 not-found 경로로 리라이트하거나 [404 응답을 생성](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#producing-a-response)하려면 [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 이 검사를 실행할 수 있습니다. proxy 검사는 빠르게 유지하고, 전체 콘텐츠를 가져오는 작업은 피하세요.

응답 본문은 언제 스트리밍되나요?

응답 본문은 Suspense Fallback(`loading.tsx` 등)이 렌더링되거나, 서버 컴포넌트가 `Suspense` 경계 안에서 suspend할 때 스트리밍을 시작합니다. 이러한 경계 이전, 그리고 suspend할 수 있는 `await` 이전에 `notFound()`를 배치하세요.

스트리밍을 시작하려면 응답 헤더가 설정되어야 합니다. 이 때문에 스트리밍이 시작된 후에는 상태 코드를 변경할 수 없습니다.

### 브라우저 한계[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#browser-limits)

[일부 브라우저](https://bugs.webkit.org/show_bug.cgi?id=252413)는 스트리밍 응답을 버퍼링합니다. 응답이 1024바이트를 넘을 때까지 스트리밍된 응답이 보이지 않을 수 있습니다. 이는 보통 “hello world” 수준의 애플리케이션에만 영향을 주며, 실제 애플리케이션에는 거의 영향을 주지 않습니다.

## 플랫폼 지원[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#platform-support)

배포 옵션| 지원 여부
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 예
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| 예
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 아니오
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별

Next.js를 셀프 호스팅할 때 [스트리밍 구성](https://nextjs.org/docs/app/guides/self-hosting#streaming-and-suspense) 방법을 알아보세요.

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples)

### Suspense와 함께하는 스트리밍[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#streaming-with-suspense)

`loading.js` 외에도 자체 UI 컴포넌트를 위해 직접 Suspense 경계를 만들 수 있습니다. App Router는 [Suspense](https://react.dev/reference/react/Suspense)와 함께 스트리밍을 지원합니다.

`<Suspense>`는 비동기 작업(예: 데이터 패치)을 수행하는 컴포넌트를 래핑하고, 작업 중에는 Fallback UI(예: 스켈레톤, 스피너)를 표시한 뒤, 작업이 완료되면 컴포넌트를 교체하는 방식으로 동작합니다.

app/dashboard/page.tsx

JavaScriptTypeScript
```
    import { Suspense } from 'react'
    import { PostFeed, Weather } from './Components'

    export default function Posts() {
      return (
        <section>
          <Suspense fallback={<p>Loading feed...</p>}>
            <PostFeed />
          </Suspense>
          <Suspense fallback={<p>Loading weather...</p>}>
            <Weather />
          </Suspense>
        </section>
      )
    }
```

Suspense를 사용하면 다음과 같은 이점을 얻습니다.

1. **Streaming Server Rendering** - 서버에서 클라이언트로 HTML을 점진적으로 렌더링합니다.
2. **Selective Hydration** - React가 사용자 상호작용에 따라 우선적으로 상호작용성을 부여할 컴포넌트를 결정합니다.

Suspense의 추가 예제와 사용 사례는 [React 문서](https://react.dev/reference/react/Suspense)를 참고하세요.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#version-history)

버전| 변경 사항
---|---
`v13.0.0`| `loading` 도입.