---
title: 'next.config.js: isolatedDevBuild'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. GitHub에서 사용해 보고 피드백을 공유해주세요.'
---

# next.config.js: isolatedDevBuild | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)isolatedDevBuild

Copy page

# isolatedDevBuild

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에서 사용해 보고 피드백을 공유해주세요.

마지막 업데이트 2026년 2월 20일

실험적 옵션인 `isolatedDevBuild`는 개발과 프로덕션 빌드 출력을 서로 다른 디렉터리로 분리합니다. 활성화하면 개발 서버(`next dev`)가 출력을 `.next` 대신 `.next/dev`에 기록하여 `next dev`와 `next build`를 동시에 실행할 때 충돌을 방지합니다.

이 기능은 자동화 도구(예: AI 에이전트)가 변경 사항을 검증하기 위해 `next build`를 실행하는 동안 개발 서버가 실행 중인 경우 특히 유용하며, 빌드 프로세스에서 발생한 변경으로 인해 개발 서버가 영향을 받지 않도록 합니다.

이 기능은 개발과 프로덕션 출력을 분리하고 충돌을 방지하기 위해 **기본적으로 활성화**되어 있습니다.

## Configuration[](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild#configuration)

이 기능을 사용하지 않으려면 설정에서 `isolatedDevBuild`를 `false`로 지정하세요.

next.config.ts

JavaScriptTypeScript
```ts
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    isolatedDevBuild: false, // defaults to true
  },
}
 
export default nextConfig
```

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild#version-history)

Version| Changes  
---|---  
`v16.0.0`| `experimental.isolatedDevBuild`가 도입되었습니다.  
  
Was this helpful?

supported.

Send
