---
title: 'next.config.js Options: generateEtags'
description: 'Next.js는 기본적으로 모든 페이지에 대해 etag를 생성합니다. 캐시 전략에 따라 HTML 페이지의 etag 생성을 비활성화하고 싶을 수 있습니다.'
---

# next.config.js Options: generateEtags | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags

# generateEtags

마지막 업데이트: 2026년 2월 20일

Next.js는 기본적으로 모든 페이지에 대해 [etag](https://en.wikipedia.org/wiki/HTTP_ETag)를 생성합니다. 캐시 전략에 따라 HTML 페이지의 etag 생성을 비활성화하고 싶을 수 있습니다.

`next.config.js`를 열어 `generateEtags` 옵션을 비활성화하세요:

next.config.js
[code]
    module.exports = {
      generateEtags: false,
    }
[/code]
