---
title: 'next.config.js: cssChunking'
description: '이 기능은 현재 실험 중이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: cssChunking | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking

# cssChunking

이 기능은 현재 실험 중이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

최종 업데이트: 2026년 2월 20일

CSS Chunking은 CSS 파일을 청킹하고 재정렬하여 웹 애플리케이션 성능을 개선하는 전략입니다. 이를 통해 애플리케이션의 모든 CSS를 한 번에 로드하는 대신 특정 라우트에 필요한 CSS만 로드할 수 있습니다.

`next.config.js` 파일의 `experimental.cssChunking` 옵션으로 CSS 파일을 어떻게 청킹할지 제어할 수 있습니다:

next.config.ts

JavaScriptTypeScript
```
import type { NextConfig } from 'next'

const nextConfig = {
  experimental: {
    cssChunking: true, // default
  },
} satisfies NextConfig

export default nextConfig
```

## 옵션[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking#options)

  * **`true` (기본값)**: Next.js가 가능할 때마다 CSS 파일을 병합하려 시도하며, 파일 간 명시적·암묵적 의존성을 import 순서로 파악해 청크 수와 요청 수를 줄입니다.
  * **`false`**: Next.js가 CSS 파일을 병합하거나 재정렬하지 않습니다.
  * **`'strict'`**: Next.js가 파일에 import된 순서 그대로 CSS를 로드하며, 그 결과 더 많은 청크와 요청이 발생할 수 있습니다.

예상치 못한 CSS 동작이 발생한다면 `'strict'` 사용을 고려해 보세요. 예를 들어 서로 다른 파일에서 `a.css`와 `b.css`를 다른 `import` 순서(`a` 뒤 `b` 또는 그 반대)로 가져오면, `true`는 파일 간 의존성이 없다고 가정하고 임의 순서로 병합합니다. 그러나 `b.css`가 `a.css`에 의존한다면 파일이 병합되지 않고 import된 순서로 로드되도록 `'strict'`를 사용해 더 많은 청크와 요청을 감수할 수 있습니다.

대부분의 애플리케이션에는 요청 수가 적고 성능이 더 나은 `true`를 권장합니다.
