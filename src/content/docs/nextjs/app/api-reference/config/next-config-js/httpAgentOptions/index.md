---
title: 'next.config.js: httpAgentOptions'
description: 'Node.js 18 이전 버전에서는 Next.js가 자동으로 undici를 사용해 를 폴리필하고 기본적으로 HTTP Keep-Alive를 활성화합니다.'
---

# next.config.js: httpAgentOptions | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions

# httpAgentOptions

최종 업데이트 2026년 2월 20일

Node.js 18 이전 버전에서는 Next.js가 자동으로 [undici](https://nextjs.org/docs/architecture/supported-browsers#polyfills)를 사용해 `fetch()`를 폴리필하고 기본적으로 [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive)를 활성화합니다.

서버 측의 모든 `fetch()` 호출에서 HTTP Keep-Alive를 비활성화하려면 `next.config.js`를 열고 `httpAgentOptions` 설정을 추가하세요:

next.config.js
```javascript
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```

보내기