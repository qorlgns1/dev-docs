---
title: 'next.config.js: generateEtags'
description: 'Next.js는 기본적으로 모든 페이지에 대해 etags를 생성합니다. 캐시 전략에 따라 HTML 페이지에서 etag 생성을 비활성화하고 싶을 수 있습니다.'
---

# next.config.js: generateEtags | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)generateEtags

Copy page

# generateEtags

Last updated February 20, 2026

Next.js는 기본적으로 모든 페이지에 대해 [etags](https://en.wikipedia.org/wiki/HTTP_ETag)를 생성합니다. 캐시 전략에 따라 HTML 페이지에서 etag 생성을 비활성화하고 싶을 수 있습니다.

`next.config.js`를 열고 `generateEtags` 옵션을 비활성화하세요:

next.config.js
[code]
    module.exports = {
      generateEtags: false,
    }
[/code]

Was this helpful?

supported.

Send
