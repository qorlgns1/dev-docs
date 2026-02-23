---
title: 'next.config.js: authInterrupts'
description: '이 기능은 현재 카나리 채널에서만 사용할 수 있으며 변경될 수 있습니다. Next.js를 업그레이드해 체험해 보고, GitHub에서 의견을 공유해 주세요.'
---

# next.config.js: authInterrupts | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts

Copy page

# authInterrupts

이 기능은 현재 카나리 채널에서만 사용할 수 있으며 변경될 수 있습니다. [Next.js를 업그레이드](https://nextjs.org/docs/app/getting-started/upgrading#canary-version)해 체험해 보고, [GitHub](https://github.com/vercel/next.js/issues)에서 의견을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

`authInterrupts` 구성 옵션을 사용하면 애플리케이션에서 [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden) 및 [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) API를 활용할 수 있습니다. 이러한 함수는 실험적 기능이므로, 사용하려면 `next.config.js` 파일에서 `authInterrupts` 옵션을 활성화해야 합니다:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        authInterrupts: true,
      },
    }

    export default nextConfig
```

##

- [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
  - 금지 함수에 대한 API Reference입니다.

- [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
  - unauthorized 함수에 대한 API Reference입니다.

- [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
  - forbidden.js 특수 파일에 대한 API Reference입니다.

- [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
  - unauthorized.js 특수 파일에 대한 API Reference입니다.

Was this helpful?

supported.

Send