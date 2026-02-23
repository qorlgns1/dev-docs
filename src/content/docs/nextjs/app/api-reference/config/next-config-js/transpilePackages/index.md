---
title: 'next.config.js: transpilePackages'
description: '마지막 업데이트: 2026년 2월 20일'
---

# next.config.js: transpilePackages | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)transpilePackages

페이지 복사

# transpilePackages

마지막 업데이트: 2026년 2월 20일

Next.js는 로컬 패키지(모노레포 등)나 외부 의존성(`node_modules`)에서 종속성을 자동으로 트랜스파일하고 번들할 수 있습니다. 이는 `next-transpile-modules` 패키지를 대체합니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      transpilePackages: ['package-name'],
    }
     
    module.exports = nextConfig
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages#version-history)

Version| Changes  
---|---  
`v13.0.0`| `transpilePackages` added.  
  
도움이 되었나요?

지원됨.

전송
