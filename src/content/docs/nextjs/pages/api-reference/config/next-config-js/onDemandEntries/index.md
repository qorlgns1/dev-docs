---
title: 'next.config.js 옵션: onDemandEntries'
description: 'Next.js는 개발 환경에서 서버가 빌드된 페이지를 메모리에 유지하거나 제거하는 방식을 제어할 수 있는 몇 가지 옵션을 제공합니다.'
---

# next.config.js 옵션: onDemandEntries | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)onDemandEntries

Copy page

# onDemandEntries

마지막 업데이트 2026년 2월 20일

Next.js는 개발 환경에서 서버가 빌드된 페이지를 메모리에 유지하거나 제거하는 방식을 제어할 수 있는 몇 가지 옵션을 제공합니다.

기본값을 변경하려면 `next.config.js`를 열고 `onDemandEntries` 구성을 추가하세요:

next.config.js
[code]
    module.exports = {
      onDemandEntries: {
        // period (in ms) where the server will keep pages in the buffer
        maxInactiveAge: 25 * 1000,
        // number of pages that should be kept simultaneously without being disposed
        pagesBufferLength: 2,
      },
    }
[/code]

도움이 되었나요?

supported.

Send
