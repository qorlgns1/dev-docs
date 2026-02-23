---
title: 'next.config.js: sassOptions'
description: '를 사용하면 Sass 컴파일러를 구성할 수 있습니다.'
---

# next.config.js: sassOptions | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)sassOptions

페이지 복사

# sassOptions

마지막 업데이트 2026년 2월 20일

`sassOptions`를 사용하면 Sass 컴파일러를 구성할 수 있습니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const sassOptions = {
      additionalData: `
        $var: red;
      `,
    }
     
    const nextConfig: NextConfig = {
      sassOptions: {
        ...sassOptions,
        implementation: 'sass-embedded',
      },
    }
     
    export default nextConfig
[/code]

> **알아두면 좋은 점:**
> 
>   * Next.js가 다른 가능한 속성들을 관리하지 않기 때문에 `implementation` 외부에서는 `sassOptions`가 타입으로 정의되지 않습니다.
>   * 사용자 정의 Sass 함수를 정의하기 위한 `functions` 속성은 webpack에서만 지원됩니다. Turbopack을 사용할 때는 Turbopack의 Rust 기반 아키텍처가 이 옵션을 통해 전달되는 JavaScript 함수를 직접 실행할 수 없으므로 사용자 정의 Sass 함수를 사용할 수 없습니다.
> 

도움이 되었나요?

지원됨.

보내기
