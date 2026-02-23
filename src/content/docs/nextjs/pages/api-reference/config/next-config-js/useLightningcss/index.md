---
title: 'next.config.js 옵션: useLightningcss'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js 옵션: useLightningcss | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss

# useLightningcss

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

webpack과 함께 [Lightning CSS](https://lightningcss.dev)를 사용할 수 있는 실험적 지원입니다. Lightning CSS는 Rust로 작성된 빠른 CSS 변환기이자 최소화 도구입니다.

이 옵션을 설정하지 않으면 webpack 기반 Next.js는 기본적으로 [`postcss-preset-env`](https://www.npmjs.com/package/postcss-preset-env)를 포함한 [PostCSS](https://postcss.org/)를 사용합니다.

Next 14.2부터 Turbopack은 기본적으로 Lightning CSS를 사용합니다. 이 구성 옵션은 Turbopack에 아무런 영향을 주지 않습니다. Turbopack은 항상 Lightning CSS를 사용합니다.

next.config.ts

JavaScript TypeScript
```tsx
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    useLightningcss: false, // default, ignored on Turbopack
  },
}

export default nextConfig
```

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss#version-history)

Version| Changes
---|---
`15.1.0`| Turbopack에서 `useSwcCss` 지원이 제거되었습니다.
`14.2.0`| Turbopack의 기본 CSS 프로세서가 `@swc/css`에서 Lightning CSS로 변경되었습니다. `useLightningcss`는 Turbopack에서 무시되며, 레거시 옵션 `experimental.turbo.useSwcCss`가 추가되었습니다.

보내기