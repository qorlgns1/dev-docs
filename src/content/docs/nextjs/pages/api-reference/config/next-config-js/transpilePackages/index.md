---
title: 'next.config.js 옵션: transpilePackages'
description: 'Next.js는 로컬 패키지(예: 모노레포)나 외부 의존성()에서 오는 의존성을 자동으로 트랜스파일하고 번들링할 수 있습니다. 이는  패키지를 대체합니다.'
---

# next.config.js 옵션: transpilePackages | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages

# transpilePackages

마지막 업데이트 2026년 2월 20일

Next.js는 로컬 패키지(예: 모노레포)나 외부 의존성(`node_modules`)에서 오는 의존성을 자동으로 트랜스파일하고 번들링할 수 있습니다. 이는 `next-transpile-modules` 패키지를 대체합니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      transpilePackages: ['package-name'],
    }

    module.exports = nextConfig
[/code]

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages#version-history)

버전| 변경 사항
---|---
`v13.0.0`| `transpilePackages`가 추가되었습니다.
