---
title: 'next.config.js 옵션: productionBrowserSourceMaps'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: productionBrowserSourceMaps | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)productionBrowserSourceMaps

페이지 복사

# productionBrowserSourceMaps

마지막 업데이트 2026년 2월 20일

개발 중에는 소스 맵이 기본적으로 활성화됩니다. 프로덕션 빌드에서는 클라이언트에 소스가 유출되는 것을 막기 위해 비활성화되며, 구성 플래그로 명시적으로 옵트인하지 않는 한 그대로 유지됩니다.

Next.js는 프로덕션 빌드 동안 브라우저 소스 맵 생성을 활성화할 수 있는 구성 플래그를 제공합니다:

next.config.js
[code]
    module.exports = {
      productionBrowserSourceMaps: true,
    }
[/code]

`productionBrowserSourceMaps` 옵션을 활성화하면 JavaScript 파일과 동일한 디렉터리에 소스 맵이 출력됩니다. Next.js는 요청이 들어오면 이러한 파일을 자동으로 제공합니다.

  * 소스 맵을 추가하면 `next build` 시간이 늘어날 수 있습니다
  * `next build` 중 메모리 사용량이 증가합니다



도움이 되었나요?

지원됨.

보내기
