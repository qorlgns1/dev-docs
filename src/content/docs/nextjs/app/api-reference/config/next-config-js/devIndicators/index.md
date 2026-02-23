---
title: 'next.config.js: devIndicators'
description: '마지막 업데이트: 2026년 2월 20일'
---

# next.config.js: devIndicators | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)devIndicators

Copy page

# devIndicators

마지막 업데이트: 2026년 2월 20일

`devIndicators`는 개발 중에 현재 보고 있는 경로에 대한 컨텍스트를 제공하는 화면 표시기를 구성할 수 있게 해줍니다.

Types
[code]
      devIndicators: false | {
        position?: 'bottom-right'
        | 'bottom-left'
        | 'top-right'
        | 'top-left', // defaults to 'bottom-left',
      },
[/code]

`devIndicators`를 `false`로 설정하면 표시기가 숨겨지지만, Next.js는 계속해서 발생한 빌드 또는 런타임 오류를 표시합니다.

## Troubleshooting[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#troubleshooting)

### Indicator not marking a route as static[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#indicator-not-marking-a-route-as-static)

경로가 정적일 것으로 예상했는데 표시기가 동적으로 표시한다면, 해당 경로가 정적 렌더링에서 제외되었을 가능성이 높습니다.

`next build --debug`로 애플리케이션을 빌드한 뒤 터미널 출력에서 경로가 [정적](https://nextjs.org/docs/app/guides/caching#static-rendering)인지 [동적](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)인지 확인할 수 있습니다. 정적(프리렌더링) 경로는 `○` 기호로 표시되고, 동적 경로는 `ƒ` 기호로 표시됩니다. 예:

Build Output
[code]
    Route (app)
    ┌ ○ /_not-found
    └ ƒ /products/[id]
     
    ○  (Static)   prerendered as static content
    ƒ  (Dynamic)  server-rendered on demand
[/code]

경로가 정적 렌더링을 포기하는 이유는 두 가지입니다:

  * 런타임 정보에 의존하는 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)가 존재하는 경우.
  * ORM이나 데이터베이스 드라이버 호출과 같은 [캐시되지 않은 데이터 요청](https://nextjs.org/docs/app/getting-started/fetching-data)이 있는 경우.

경로에서 이러한 조건을 확인하고, 정적으로 렌더링할 수 없다면 [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)나 [`<Suspense />`](https://react.dev/reference/react/Suspense)를 사용해 [스트리밍](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming)을 활용하는 것을 고려하세요.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators#version-history)

Version| Changes  
---|---  
`v16.0.0`| `appIsrStatus`, `buildActivity`, `buildActivityPosition` 옵션이 제거되었습니다.  
`v15.2.0`| 새로운 `position` 옵션이 포함된 화면 표시기가 개선되었습니다. `appIsrStatus`, `buildActivity`, `buildActivityPosition` 옵션이 더는 권장되지 않습니다.  
`v15.0.0`| `appIsrStatus` 옵션과 함께 정적 화면 표시기가 추가되었습니다.  
  
Was this helpful?

supported.

Send
