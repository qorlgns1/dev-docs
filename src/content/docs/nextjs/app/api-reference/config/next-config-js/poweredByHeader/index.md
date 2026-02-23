---
title: 'next.config.js: poweredByHeader'
description: '기본적으로 Next.js는  헤더를 추가합니다. 이를 사용하지 않으려면 를 열어  설정을 비활성화하세요.'
---

# next.config.js: poweredByHeader | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader

Copy page

# poweredByHeader

2026년 2월 20일 최종 업데이트

기본적으로 Next.js는 `x-powered-by` 헤더를 추가합니다. 이를 사용하지 않으려면 `next.config.js`를 열어 `poweredByHeader` 설정을 비활성화하세요.

next.config.js
[code]
    module.exports = {
      poweredByHeader: false,
    }
[/code]

supported.

Send
