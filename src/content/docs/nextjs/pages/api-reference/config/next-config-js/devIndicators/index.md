---
title: 'next.config.js Options: devIndicators'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js Options: devIndicators | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)devIndicators

Copy page

# devIndicators

마지막 업데이트 2026년 2월 20일

`devIndicators`는 개발 중에 보고 있는 현재 라우트에 대한 컨텍스트를 제공하는 화면 상의 인디케이터를 구성할 수 있게 합니다.

Types
[code]
      devIndicators: false | {
        position?: 'bottom-right'
        | 'bottom-left'
        | 'top-right'
        | 'top-left', // defaults to 'bottom-left',
      },
[/code]

`devIndicators`를 `false`로 설정하면 인디케이터가 숨겨지지만, Next.js는 발견된 빌드 또는 런타임 오류를 계속 표시합니다.

## Troubleshooting[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators#troubleshooting)

### Indicator not marking a route as static[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators#indicator-not-marking-a-route-as-static)

라우트를 정적이라고 예상했는데 인디케이터가 동적으로 표시한다면, 해당 라우트가 정적 렌더링에서 제외되었을 가능성이 큽니다.

`next build --debug`로 애플리케이션을 빌드하고 터미널 출력에서 라우트가 [static](https://nextjs.org/docs/app/guides/caching#static-rendering)인지 [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)인지 확인할 수 있습니다. 정적(또는 사전 렌더링된) 라우트는 `○` 기호를, 동적 라우트는 `ƒ` 기호를 표시합니다. 예:

Build Output
[code]
    Route (app)
    ┌ ○ /_not-found
    └ ƒ /products/[id]
     
    ○  (Static)   prerendered as static content
    ƒ  (Dynamic)  server-rendered on demand
[/code]

페이지에서 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 또는 [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)를 내보내면 해당 페이지는 동적으로 표시됩니다.

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators#version-history)

Version| Changes  
---|---  
`v16.0.0`| `appIsrStatus`, `buildActivity`, `buildActivityPosition` 옵션이 제거되었습니다.  
`v15.2.0`| 새로운 `position` 옵션과 함께 화면 인디케이터가 개선되었습니다. `appIsrStatus`, `buildActivity`, `buildActivityPosition` 옵션은 사용 중단되었습니다.  
`v15.0.0`| `appIsrStatus` 옵션과 함께 정적 화면 인디케이터가 추가되었습니다.  
  
Was this helpful?

supported.

Send
