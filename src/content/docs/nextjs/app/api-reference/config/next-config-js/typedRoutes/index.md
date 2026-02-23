---
title: 'next.config.js: typedRoutes'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js: typedRoutes | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)typedRoutes

페이지 복사

# typedRoutes

마지막 업데이트 2026년 2월 20일

> **참고**: 이 옵션은 안정(stable) 버전으로 지정되었으므로 `experimental.typedRoutes` 대신 `typedRoutes`를 사용해야 합니다.

[정적으로 타입이 지정된 링크](https://nextjs.org/docs/app/api-reference/config/typescript#statically-typed-links)에 대한 지원입니다. 이 기능을 사용하려면 프로젝트에서 TypeScript를 사용해야 합니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      typedRoutes: true,
    }
     
    module.exports = nextConfig
[/code]

도움이 되었나요?

지원됨.

보내기
