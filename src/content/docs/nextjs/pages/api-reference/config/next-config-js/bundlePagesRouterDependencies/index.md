---
title: 'next.config.js 옵션: bundlePagesRouterDependencies'
description: 'Pages Router 애플리케이션에서 서버 측 종속성을 자동으로 번들링합니다. App Router에서의 자동 종속성 번들링과 동일하게 동작합니다.'
---

# next.config.js 옵션: bundlePagesRouterDependencies | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies

# bundlePagesRouterDependencies

마지막 업데이트: 2026년 2월 20일

Pages Router 애플리케이션에서 서버 측 종속성을 자동으로 번들링합니다. App Router에서의 자동 종속성 번들링과 동일하게 동작합니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      bundlePagesRouterDependencies: true,
    }

    module.exports = nextConfig
```

[`serverExternalPackages`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages) 옵션을 사용해 특정 패키지를 번들 대상에서 명시적으로 제외할 수 있습니다.

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies#version-history)

버전| 변경 사항
---|---
`v15.0.0`| 실험적(experimental) 단계에서 안정(stable) 단계로 이동했습니다. `bundlePagesExternals`에서 `bundlePagesRouterDependencies`로 이름이 변경되었습니다.

supported.

Send