---
title: 'next.config.js: serverComponentsHmrCache'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 로컬 개발에서 사용해 보고 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: serverComponentsHmrCache | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache

# serverComponentsHmrCache

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 로컬 개발에서 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

실험적 옵션인 `serverComponentsHmrCache`를 사용하면 로컬 개발에서 핫 모듈 교체(HMR) 새로 고침 간에 Server Components의 `fetch` 응답을 캐시할 수 있습니다. 그 결과 응답이 더 빨라지고 과금되는 API 호출 비용이 줄어듭니다.

기본적으로 HMR 캐시는 `cache: 'no-store'` 옵션이 있는 요청을 포함해 모든 `fetch` 요청에 적용됩니다. 즉, 캐시되지 않은 요청도 HMR 새로 고침 사이에서 최신 데이터를 표시하지 않습니다. 그러나 탐색하거나 전체 페이지를 다시 로드하면 캐시가 비워집니다.

`next.config.js` 파일에서 `serverComponentsHmrCache`를 `false`로 설정하면 HMR 캐시를 비활성화할 수 있습니다:

next.config.ts

JavaScriptTypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}

export default nextConfig
```

> **참고:** 관측성을 높이려면 개발 중 콘솔에서 fetch 캐시 적중/미스를 기록해 주는 [`logging.fetches`](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging) 옵션 사용을 권장합니다.
