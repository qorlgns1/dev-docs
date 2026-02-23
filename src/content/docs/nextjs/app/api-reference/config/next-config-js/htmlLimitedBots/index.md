---
title: 'next.config.js: htmlLimitedBots'
description: '구성은 스트리밍 메타데이터 대신 차단 메타데이터를 받아야 하는 사용자 에이전트 목록을 지정할 수 있도록 합니다.'
---

# next.config.js: htmlLimitedBots | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)htmlLimitedBots

페이지 복사

# htmlLimitedBots

최종 업데이트 2026년 2월 20일

`htmlLimitedBots` 구성은 [스트리밍 메타데이터](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata) 대신 차단 메타데이터를 받아야 하는 사용자 에이전트 목록을 지정할 수 있도록 합니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
[/code]

## 기본 목록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#default-list)

Next.js에는 다음을 포함한 기본 HTML 제한 봇 목록이 포함되어 있습니다:

  * Google 크롤러(예: Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
  * Bingbot
  * Twitterbot
  * Slackbot

전체 목록은 [여기](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts)에서 확인하세요.

`htmlLimitedBots` 구성을 지정하면 Next.js의 기본 목록을 덮어씁니다. 다만 이는 고급 동작이며 대부분의 경우 기본값이면 충분합니다.

next.config.ts

JavaScriptTypeScript
[code]
    const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
[/code]

## 비활성화[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#disabling)

스트리밍 메타데이터를 완전히 비활성화하려면:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /.*/,
    }
     
    export default config
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#version-history)

버전| 변경 사항  
---|---  
15.2.0| `htmlLimitedBots` 옵션 도입.  
  
도움이 되었나요?

지원됨.

전송
