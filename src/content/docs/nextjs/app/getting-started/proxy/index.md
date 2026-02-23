---
title: '시작하기: 프록시'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: 프록시 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/proxy

[앱 라우터](https://nextjs.org/docs/app)[시작하기](https://nextjs.org/docs/app/getting-started)Proxy

페이지 복사

# 프록시

마지막 업데이트 2026년 2월 20일

## 프록시[](https://nextjs.org/docs/app/getting-started/proxy#proxy)

> **알아두면 좋아요** : Next.js 16부터 Middleware가 목적을 더 잘 드러내도록 Proxy로 이름이 변경되었습니다. 기능은 동일하게 유지됩니다.

프록시는 요청이 완료되기 전에 코드를 실행할 수 있게 해 줍니다. 이후 들어오는 요청을 기반으로, 재작성, 리디렉션, 요청/응답 헤더 수정 또는 직접 응답을 통해 응답을 변경할 수 있습니다.

### 사용 사례[](https://nextjs.org/docs/app/getting-started/proxy#use-cases)

프록시가 효과적인 대표적인 시나리오는 다음과 같습니다.

  * 모든 페이지 또는 일부 페이지에 대해 헤더를 수정
  * A/B 테스트나 실험 결과에 따라 다른 페이지로 재작성
  * 들어오는 요청 속성에 따른 프로그래밍 방식 리디렉션



간단한 리디렉션에는 먼저 `next.config.ts`의 [`redirects`](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects) 구성을 사용하는 것을 고려하세요. 요청 데이터에 접근하거나 더 복잡한 로직이 필요할 때 프록시를 사용하면 됩니다.

프록시는 느린 데이터 패칭 용도가 아닙니다. 권한 기반 리디렉션 같은 [낙관적 검사](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)에 프록시가 유용할 수 있지만, 완전한 세션 관리나 인증 솔루션으로 사용해서는 안 됩니다.

`options.cache`, `options.next.revalidate`, `options.next.tags`와 함께 fetch를 사용해도 프록시에서는 효과가 없습니다.

### 규칙[](https://nextjs.org/docs/app/getting-started/proxy#convention)

프로젝트 루트(또는 해당하는 경우 `src`)에 `proxy.ts`(또는 `.js`) 파일을 생성하여 `pages`나 `app`과 동일한 수준에 위치하도록 합니다.

> **참고** : 프로젝트당 지원되는 `proxy.ts` 파일은 하나뿐이지만, 프록시 로직을 모듈로 구성할 수는 있습니다. 프록시 기능을 개별 `.ts` 또는 `.js` 파일로 분리한 뒤 기본 `proxy.ts` 파일에서 가져오세요. 이렇게 하면 라우트별 프록시를 깔끔히 관리하면서 `proxy.ts`에 집계해 중앙에서 제어할 수 있습니다. 단일 프록시 파일을 강제하면 구성이 단순해지고 잠재적 충돌을 방지하며 여러 프록시 레이어로 인한 성능 저하를 피할 수 있습니다.

### 예시[](https://nextjs.org/docs/app/getting-started/proxy#example)

프록시 함수를 기본 내보내기 또는 이름이 지정된 `proxy` 내보내기로 export할 수 있습니다.

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'
     
    // This function can be marked `async` if using `await` inside
    export function proxy(request: NextRequest) {
      return NextResponse.redirect(new URL('/home', request.url))
    }
     
    // Alternatively, you can use a default export:
    // export default function proxy(request: NextRequest) { ... }
     
    export const config = {
      matcher: '/about/:path*',
    }
[/code]

`matcher` 구성은 특정 경로에서만 프록시가 실행되도록 필터링할 수 있게 해 줍니다. 경로 매칭에 대한 자세한 내용은 [Matcher](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher) 문서를 참조하세요.

[`proxy` 사용](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)에 대해 더 읽거나, `proxy` [API 레퍼런스](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 참고하세요.

## API Reference

프록시에 대해 더 알아보기

### [proxy.js프록시 파일에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)### [Backend for FrontendNext.js를 백엔드 프레임워크로 사용하는 방법을 알아보세요](https://nextjs.org/docs/app/guides/backend-for-frontend)

도움이 되었나요?

지원됨.

보내기
