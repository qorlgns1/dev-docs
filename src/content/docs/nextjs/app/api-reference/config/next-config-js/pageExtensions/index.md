---
title: 'next.config.js: pageExtensions'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js: pageExtensions | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)pageExtensions

페이지 복사

# pageExtensions

마지막 업데이트 2026년 2월 20일

기본적으로 Next.js는 `.tsx`, `.ts`, `.jsx`, `.js` 확장자를 가진 파일을 허용합니다. 이는 마크다운(`.md`, `.mdx`)과 같은 다른 확장자를 포함하도록 수정할 수 있습니다.

next.config.js
[code]
    const withMDX = require('@next/mdx')()
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
    }
     
    module.exports = withMDX(nextConfig)
[/code]

도움이 되었나요?

지원됨.

전송
