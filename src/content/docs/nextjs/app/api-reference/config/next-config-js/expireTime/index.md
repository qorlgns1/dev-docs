---
title: 'next.config.js: expireTime'
description: '최종 업데이트: 2026년 2월 20일'
---

# next.config.js: expireTime | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)expireTime 구성 항목

페이지 복사

# expireTime

최종 업데이트: 2026년 2월 20일

ISR이 활성화된 페이지에서 CDN이 `Cache-Control` 헤더로 활용할 사용자 정의 `stale-while-revalidate` 만료 시간을 지정할 수 있습니다.

`next.config.js`를 열고 `expireTime` 구성을 추가하세요:

next.config.js
```code
    module.exports = {
      // one hour in seconds
      expireTime: 3600,
    }
```

이제 `Cache-Control` 헤더를 전송할 때 만료 시간은 특정 재검증 기간에 따라 계산됩니다.

예를 들어 어떤 경로에 15분의 재검증 주기와 1시간의 만료 시간을 설정했다면 생성되는 `Cache-Control` 헤더는 `s-maxage=900, stale-while-revalidate=2700`이 되어, 구성된 만료 시간보다 15분 덜 오래된 상태로 유지할 수 있습니다.

도움이 되었나요?

지원됨.

보내기
