---
title: '파일 시스템 규칙: instrumentation-client.js'
description: '파일을 사용하면 애플리케이션이 인터랙티브 상태가 되기 전에 실행되는 모니터링, 분석 코드, 기타 부수 효과를 추가할 수 있습니다. 이는 성능 추적, 오류 모니터링, 폴리필 또는 그 밖의 클라이언트 측 관측 도구를 설정하는 데 유용합니다.'
---

# 파일 시스템 규칙: instrumentation-client.js | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)instrumentation-client.js

페이지 복사

# instrumentation-client.js

마지막 업데이트: 2026년 2월 20일

`instrumentation-client.js|ts` 파일을 사용하면 애플리케이션이 인터랙티브 상태가 되기 전에 실행되는 모니터링, 분석 코드, 기타 부수 효과를 추가할 수 있습니다. 이는 성능 추적, 오류 모니터링, 폴리필 또는 그 밖의 클라이언트 측 관측 도구를 설정하는 데 유용합니다.

사용하려면 애플리케이션 **루트** 또는 `src` 폴더 안에 파일을 배치하세요.

## 사용 방법[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#usage)

[서버 측 계측](https://nextjs.org/docs/app/guides/instrumentation)과 달리 특정 함수를 내보낼 필요가 없습니다. 이 파일에 모니터링 코드를 직접 작성하면 됩니다:

instrumentation-client.ts

JavaScriptTypeScript
[code]
    // Set up performance monitoring
    performance.mark('app-init')
     
    // Initialize analytics
    console.log('Analytics initialized')
     
    // Set up error tracking
    window.addEventListener('error', (event) => {
      // Send to your error tracking service
      reportError(event.error)
    })
[/code]

**오류 처리:** 모니터링을 견고하게 유지하려면 계측 코드에 try-catch 블록을 구현하세요. 이렇게 하면 개별 추적 실패가 다른 계측 기능에 영향을 주지 않습니다.

## 라우터 탐색 추적[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#router-navigation-tracking)

탐색이 시작될 때 알림을 받으려면 `onRouterTransitionStart` 함수를 내보낼 수 있습니다:

instrumentation-client.ts

JavaScriptTypeScript
[code]
    performance.mark('app-init')
     
    export function onRouterTransitionStart(
      url: string,
      navigationType: 'push' | 'replace' | 'traverse'
    ) {
      console.log(`Navigation started: ${navigationType} to ${url}`)
      performance.mark(`nav-start-${Date.now()}`)
    }
[/code]

`onRouterTransitionStart` 함수는 두 개의 매개변수를 받습니다:

  * `url: string` \- 이동하려는 URL
  * `navigationType: 'push' | 'replace' | 'traverse'` \- 탐색 유형

## 성능 고려 사항[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#performance-considerations)

계측 코드를 가볍게 유지하세요.

Next.js는 개발 환경에서 초기화 시간을 모니터링하며, 16ms를 초과하면 부드러운 페이지 로딩에 영향을 줄 수 있다고 경고를 기록합니다.

## 실행 타이밍[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#execution-timing)

`instrumentation-client.js` 파일은 애플리케이션 라이프사이클의 특정 지점에서 실행됩니다:

  1. **HTML 문서가 로드된 후**
  2. **React 하이드레이션이 시작되기 전에**
  3. **사용자 상호 작용이 가능해지기 전에**

이 타이밍 덕분에 초기 라이프사이클 이벤트를 캡처해야 하는 오류 추적, 분석, 성능 모니터링을 설정하기에 이상적입니다.

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#examples)

### 오류 추적[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#error-tracking)

React가 시작되기 전에 오류 추적을 초기화하고, 탐색 브레드크럼을 추가해 디버깅 컨텍스트를 향상하세요.

instrumentation-client.ts

JavaScriptTypeScript
[code]
    import Monitor from './lib/monitoring'
     
    Monitor.initialize()
     
    export function onRouterTransitionStart(url: string) {
      Monitor.pushEvent({
        message: `Navigation to ${url}`,
        category: 'navigation',
      })
    }
[/code]

### 분석 추적[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#analytics-tracking)

분석을 초기화하고, 사용자 행동 분석을 위해 세부 메타데이터를 포함한 탐색 이벤트를 추적하세요.

instrumentation-client.ts

JavaScriptTypeScript
[code]
    import { analytics } from './lib/analytics'
     
    analytics.init()
     
    export function onRouterTransitionStart(url: string, navigationType: string) {
      analytics.track('page_navigation', {
        url,
        type: navigationType,
        timestamp: Date.now(),
      })
    }
[/code]

### 성능 모니터링[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#performance-monitoring)

Performance Observer API와 퍼포먼스 마크를 사용해 Time to Interactive와 탐색 성능을 추적하세요.

instrumentation-client.ts

JavaScriptTypeScript
[code]
    const startTime = performance.now()
     
    const observer = new PerformanceObserver(
      (list: PerformanceObserverEntryList) => {
        for (const entry of list.getEntries()) {
          if (entry instanceof PerformanceNavigationTiming) {
            console.log('Time to Interactive:', entry.loadEventEnd - startTime)
          }
        }
      }
    )
     
    observer.observe({ entryTypes: ['navigation'] })
     
    export function onRouterTransitionStart(url: string) {
      performance.mark(`nav-start-${url}`)
    }
[/code]

### 폴리필[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#polyfills)

애플리케이션 코드가 실행되기 전에 폴리필을 로드하세요. 즉시 로딩이 필요하면 정적 import를, 기능 감지 결과에 따라 조건부 로딩이 필요하면 동적 import를 사용합니다.

instrumentation-client.ts

JavaScriptTypeScript
[code]
    import './lib/polyfills'
     
    if (!window.ResizeObserver) {
      import('./lib/polyfills/resize-observer').then((mod) => {
        window.ResizeObserver = mod.default
      })
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#version-history)

버전| 변경 사항  
---|---  
`v15.3`| `instrumentation-client` 도입  

도움이 되었나요?

지원됨.

전송
