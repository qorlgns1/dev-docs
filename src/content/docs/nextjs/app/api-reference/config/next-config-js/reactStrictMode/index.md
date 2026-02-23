---
title: 'next.config.js: reactStrictMode'
description: '> 알아두면 좋아요 : Next.js 13.5.1부터  라우터에서는 Strict Mode가 기본값으로 이므로, 위 설정은 에서만 필요합니다. 로 설정해 Strict Mode를 비활성화할 수도 있습니다.'
---

# next.config.js: reactStrictMode | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode

# reactStrictMode

마지막 업데이트 2026년 2월 20일

> **알아두면 좋아요** : Next.js 13.5.1부터 `app` 라우터에서는 Strict Mode가 기본값으로 `true`이므로, 위 설정은 `pages`에서만 필요합니다. `reactStrictMode: false`로 설정해 Strict Mode를 비활성화할 수도 있습니다.

> **권장** : React의 미래에 대비하기 위해 Next.js 애플리케이션에서 Strict Mode를 활성화할 것을 강력히 권장합니다.

React의 [Strict Mode](https://react.dev/reference/react/StrictMode)는 애플리케이션의 잠재적 문제를 강조하기 위한 개발 모드 전용 기능입니다. 안전하지 않은 라이프사이클, 레거시 API 사용, 기타 다양한 기능을 식별하는 데 도움이 됩니다.

Next.js 런타임은 Strict Mode를 준수합니다. Strict Mode를 선택하려면 `next.config.js`에서 다음 옵션을 구성하세요:

next.config.js
```
    module.exports = {
      reactStrictMode: true,
    }
```

본인이나 팀이 애플리케이션 전체에서 Strict Mode를 사용할 준비가 아직 되지 않았다면 괜찮습니다! `<React.StrictMode>`를 사용해 페이지 단위로 점진적으로 마이그레이션할 수 있습니다.
