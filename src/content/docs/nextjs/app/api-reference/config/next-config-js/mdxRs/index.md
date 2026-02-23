---
title: 'next.config.js: mdxRs'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 사용해 본 뒤 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: mdxRs | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)mdxRs

페이지 복사

# mdxRs

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 사용해 본 뒤 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트: 2026년 2월 20일

`@next/mdx`와 함께 실험적으로 사용합니다. 새로운 Rust 컴파일러를 사용해 MDX 파일을 컴파일합니다.

next.config.js
[code]
    const withMDX = require('@next/mdx')()
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['ts', 'tsx', 'mdx'],
      experimental: {
        mdxRs: true,
      },
    }
     
    module.exports = withMDX(nextConfig)
[/code]

도움이 되었나요?

지원됨.

보내기
