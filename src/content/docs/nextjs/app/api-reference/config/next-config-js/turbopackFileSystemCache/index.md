---
title: 'next.config.js: turbopackFileSystemCache'
description: 'Turbopack 파일시스템 캐시는  또는  명령 전반에서 Turbopack의 작업량을 줄일 수 있도록 합니다. 이 기능을 활성화하면 Turbopack은 빌드 사이에  폴더에 데이터를 저장하고 복원하여 이후 빌드와 개발 세션을 크게 가속할 수 있습니다.'
---

# next.config.js: turbopackFileSystemCache | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)turbopackFileSystemCache

페이지 복사

# Turbopack 파일시스템 캐싱

최종 업데이트 2026년 2월 20일

## 사용 방법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache#usage)

Turbopack 파일시스템 캐시는 `next dev` 또는 `next build` 명령 전반에서 Turbopack의 작업량을 줄일 수 있도록 합니다. 이 기능을 활성화하면 Turbopack은 빌드 사이에 `.next` 폴더에 데이터를 저장하고 복원하여 이후 빌드와 개발 세션을 크게 가속할 수 있습니다.

> **알아두면 좋아요:** FileSystem Cache 기능은 개발 환경에서는 안정적으로 간주되며 프로덕션 빌드에서는 실험 단계입니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        // Enable filesystem caching for `next dev`
        turbopackFileSystemCacheForDev: true,
        // Enable filesystem caching for `next build`
        turbopackFileSystemCacheForBuild: true,
      },
    }
     
    export default nextConfig
[/code]

## 버전 변경 사항[](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache#version-changes)

버전|변경 사항  
---|---  
`v16.1.0`| 개발 환경에서 기본적으로 파일시스템 캐싱이 활성화됨  
`v16.0.0`| 빌드와 개발을 위한 개별 플래그를 포함한 베타 릴리스  
`v15.5.0`| 카나리 릴리스에서 실험적으로 지속형 캐싱 출시  
  
도움이 되었나요?

지원됨.

보내기
