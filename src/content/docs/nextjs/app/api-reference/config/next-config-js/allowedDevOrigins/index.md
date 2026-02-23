---
title: 'next.config.js: allowedDevOrigins'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js: allowedDevOrigins | Next.js
Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)allowedDevOrigins

Copy page

# allowedDevOrigins

마지막 업데이트 2026년 2월 20일

Next.js는 개발 중 교차 출처 요청을 자동으로 차단하지 않지만, 향후 메이저 버전에서는 개발 모드에서 노출되는 내부 자산/엔드포인트에 대한 무단 요청을 방지하기 위해 기본적으로 차단할 예정입니다.

서버가 초기화된 호스트명(기본값은 `localhost`) 이외의 출처에서 요청을 허용하도록 Next.js 애플리케이션을 구성하려면 `allowedDevOrigins` 구성 옵션을 사용할 수 있습니다.

`allowedDevOrigins`를 사용하면 개발 모드에서 사용할 수 있는 추가 출처를 지정할 수 있습니다. 예를 들어 `localhost` 대신 `local-origin.dev`를 사용하려면 `next.config.js`를 열고 다음과 같이 `allowedDevOrigins` 구성을 추가하세요.

next.config.js
```
    module.exports = {
      allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
    }
```

Was this helpful?

supported.

Send
