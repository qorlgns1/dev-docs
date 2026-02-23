---
title: 'next.config.js 옵션: poweredByHeader'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: poweredByHeader | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)poweredByHeader

페이지 복사

# poweredByHeader

마지막 업데이트 2026년 2월 20일

기본적으로 Next.js는 `x-powered-by` 헤더를 추가합니다. 이를 비활성화하려면 `next.config.js`를 열고 `poweredByHeader` 설정을 꺼 주세요:

next.config.js
[code]
    module.exports = {
      poweredByHeader: false,
    }
[/code]

도움이 되었나요?

지원됨.

전송
