---
title: 'next.config.js: useLightningcss'
description: '이 기능은 현재 실험적이며 향후 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. GitHub에서 사용해 보고 피드백을 공유하세요.'
---

# next.config.js: useLightningcss | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)useLightningcss

페이지 복사

# useLightningcss

이 기능은 현재 실험적이며 향후 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에서 사용해 보고 피드백을 공유하세요.

마지막 업데이트: 2026년 2월 20일

webpack에서 [Lightning CSS](https://lightningcss.dev)를 사용할 수 있는 실험적 지원입니다. Lightning CSS는 Rust로 작성된 빠른 CSS 변환 및 압축기입니다.

이 옵션을 설정하지 않으면, webpack을 사용하는 Next.js는 기본적으로 [PostCSS](https://postcss.org/)와 [`postcss-preset-env`](https://www.npmjs.com/package/postcss-preset-env)를 사용합니다.

Next 14.2부터 Turbopack은 기본적으로 Lightning CSS를 사용합니다. 이 구성 옵션은 Turbopack에는 아무런 영향을 주지 않습니다. Turbopack은 항상 Lightning CSS를 사용합니다.

next.config.ts

JavaScriptTypeScript
```ts
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    useLightningcss: false, // default, ignored on Turbopack
  },
}
 
export default nextConfig
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss#version-history)

버전| 변경 사항  
---|---  
`15.1.0`| Turbopack에서 `useSwcCss` 지원이 제거되었습니다.  
`14.2.0`| Turbopack의 기본 CSS 프로세서가 `@swc/css`에서 Lightning CSS로 변경되었습니다. Turbopack에서는 `useLightningcss`가 무시되며, 레거시 옵션인 `experimental.turbo.useSwcCss`가 추가되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
