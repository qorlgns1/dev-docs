---
title: 'next.config.js: staticGeneration*'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 직접 사용해 보고 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: staticGeneration* | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration

Copy page

# staticGeneration*

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 직접 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트: 2026년 2월 20일

`staticGeneration*` 옵션을 사용하면 고급 사용 사례를 위해 정적 생성 프로세스를 구성할 수 있습니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        staticGenerationRetryCount: 1,
        staticGenerationMaxConcurrency: 8,
        staticGenerationMinPagesPerWorker: 25,
      },
    }

    export default nextConfig
[/code]

## Config Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration#config-options)

사용할 수 있는 옵션은 다음과 같습니다.

  * `staticGenerationRetryCount`: 빌드가 실패하기 전에 페이지 생성을 재시도하는 횟수입니다.
  * `staticGenerationMaxConcurrency`: 워커 한 개가 동시에 처리할 수 있는 최대 페이지 수입니다.
  * `staticGenerationMinPagesPerWorker`: 새 워커를 시작하기 전에 워커가 처리해야 하는 최소 페이지 수입니다.

이 내용이 도움이 되었나요?

supported.

Send
