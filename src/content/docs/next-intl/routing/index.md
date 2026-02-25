---
title: 'index'
description: '은 Next.js의 라우팅 시스템 두 곳에 통합됩니다:'
---

Source URL: https://next-intl.dev/docs/routing

[문서](https://next-intl.dev/docs/getting-started "문서")라우팅

# 라우팅

`next-intl`은 Next.js의 라우팅 시스템 두 곳에 통합됩니다:

  1. **Proxy / middleware** : 로캘을 협상하고 리디렉션 및 리라이트를 처리합니다 (예: `/` → `/en`)
  2. **Navigation APIs** : `<Link />` 같은 Next.js 내비게이션 API를 감싼 경량 래퍼입니다

이를 통해 `<Link href="/about">` 같은 API로 앱을 표현할 수 있으며, 로캘과 사용자에게 보이는 경로명 같은 요소는 내부적으로 자동 처리됩니다 (예: `/de/über-uns`).

[라우팅 설정→](https://next-intl.dev/docs/routing/setup)[구성→](https://next-intl.dev/docs/routing/configuration)[Proxy / middleware→](https://next-intl.dev/docs/routing/middleware)[Navigation APIs→](https://next-intl.dev/docs/routing/navigation)

동영상을 보는 편을 선호하시나요?

[로캘 기반 라우팅](https://learn.next-intl.dev/chapters/06-routing/01-setup)

