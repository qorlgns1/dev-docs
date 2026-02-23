---
title: 'next.config.js 옵션: allowedDevOrigins'
description: 'Next.js는 개발 중 교차 출처 요청을 자동으로 차단하지 않지만, 향후 메이저 버전에서는 개발 모드에서 접근 가능한 내부 자산/엔드포인트에 대한 무단 요청을 방지하기 위해 기본적으로 차단할 예정입니다.'
---

# next.config.js 옵션: allowedDevOrigins | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins

# allowedDevOrigins

마지막 업데이트 2026년 2월 20일

Next.js는 개발 중 교차 출처 요청을 자동으로 차단하지 않지만, 향후 메이저 버전에서는 개발 모드에서 접근 가능한 내부 자산/엔드포인트에 대한 무단 요청을 방지하기 위해 기본적으로 차단할 예정입니다.

서버가 초기화된 호스트 이름(기본값은 `localhost`) 이외의 출처에서 요청을 허용하도록 Next.js 애플리케이션을 구성하려면 `allowedDevOrigins` 설정 옵션을 사용하면 됩니다.

`allowedDevOrigins`는 개발 모드에서 사용할 수 있는 추가 출처를 설정할 수 있게 해줍니다. 예를 들어 `localhost` 대신 `local-origin.dev`를 사용하려면 `next.config.js`를 열고 `allowedDevOrigins` 설정을 추가하세요.

next.config.js
```
// code block remains same
    module.exports = {
      allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
    }
```