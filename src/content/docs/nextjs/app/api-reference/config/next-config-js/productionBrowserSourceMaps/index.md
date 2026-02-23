---
title: 'next.config.js: productionBrowserSourceMaps'
description: '개발 중에는 소스 맵이 기본적으로 활성화됩니다. 프로덕션 빌드에서는 별도로 이 구성 플래그를 통해 옵트인하지 않는 한, 클라이언트 측에 소스가 노출되는 일을 막기 위해 비활성화됩니다.'
---

# next.config.js: productionBrowserSourceMaps | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps

# productionBrowserSourceMaps

2026년 2월 20일 업데이트

개발 중에는 소스 맵이 기본적으로 활성화됩니다. 프로덕션 빌드에서는 별도로 이 구성 플래그를 통해 옵트인하지 않는 한, 클라이언트 측에 소스가 노출되는 일을 막기 위해 비활성화됩니다.

Next.js는 프로덕션 빌드 중 브라우저 소스 맵 생성을 활성화할 수 있는 구성 플래그를 제공합니다.

next.config.js
[code]
    module.exports = {
      productionBrowserSourceMaps: true,
    }
[/code]

`productionBrowserSourceMaps` 옵션을 활성화하면 소스 맵이 JavaScript 파일과 동일한 디렉터리에 출력됩니다. Next.js는 요청 시 이러한 파일을 자동으로 제공합니다.

  * 소스 맵을 추가하면 `next build` 시간이 늘어날 수 있습니다.
  * `next build` 중 메모리 사용량이 증가합니다.

보내기
