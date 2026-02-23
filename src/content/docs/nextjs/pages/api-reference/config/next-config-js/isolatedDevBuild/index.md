---
title: 'next.config.js Options: isolatedDevBuild'
description: '실험적 옵션인 는 개발 및 프로덕션 빌드 출력을 서로 다른 디렉터리로 분리합니다. 이 기능을 활성화하면 개발 서버()는  대신 에 출력을 기록하므로 와 를 동시에 실행할 때 충돌을 방지합니다.'
---

# next.config.js Options: isolatedDevBuild | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild

Copy page

# isolatedDevBuild

Last updated February 20, 2026

실험적 옵션인 `isolatedDevBuild`는 개발 및 프로덕션 빌드 출력을 서로 다른 디렉터리로 분리합니다. 이 기능을 활성화하면 개발 서버(`next dev`)는 `.next` 대신 `.next/dev`에 출력을 기록하므로 `next dev`와 `next build`를 동시에 실행할 때 충돌을 방지합니다.

이는 자동화 도구(예: AI 에이전트)가 변경 사항을 검증하기 위해 `next build`를 실행하는 동안 개발 서버가 실행 중인 경우, 빌드 프로세스에서 발생한 변경이 개발 서버에 영향을 주지 않도록 할 때 특히 유용합니다.

이 기능은 개발 및 프로덕션 출력을 분리하고 충돌을 방지하기 위해 **기본적으로 활성화**되어 있습니다.

## Configuration[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild#configuration)

이 기능을 옵트아웃하려면 설정에서 `isolatedDevBuild`를 `false`로 지정하세요:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        isolatedDevBuild: false, // defaults to true
      },
    }

    export default nextConfig
```

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild#version-history)

Version| Changes
---|---
`v16.0.0`| `experimental.isolatedDevBuild`가 도입되었습니다.

Was this helpful?

supported.

Send