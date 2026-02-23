---
title: 'next.config.js: viewTransition'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: viewTransition | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition

Copy page

# viewTransition

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

`viewTransition`은 React에서 새로운 [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)를 활성화하는 실험적 플래그입니다. 이 API를 사용하면 브라우저의 기본 View Transitions API를 활용해 UI 상태 간 전환을 매끄럽게 만들 수 있습니다.

이 기능을 활성화하려면 `next.config.js` 파일에서 `viewTransition` 속성을 `true`로 설정해야 합니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        viewTransition: true,
      },
    }

    module.exports = nextConfig
```

> 중요 공지: `<ViewTransition>` 컴포넌트는 이미 React의 Canary 릴리스 채널에서 제공됩니다. `experimental.viewTransition`은 Next.js 기능과의 더 깊은 통합(예: 내비게이션 시 [Transition types 추가](https://react.dev/reference/react/addTransitionType)를 자동으로 처리)을 활성화하는 데만 필요합니다. Next.js 전용 전환 타입은 아직 구현되지 않았습니다.

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition#usage)

애플리케이션에서 React의 [`<ViewTransition>` 컴포넌트](https://react.dev/reference/react/ViewTransition)를 import하여 사용할 수 있습니다:
```
    import { ViewTransition } from 'react'
```

### Live Demo[](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition#live-demo)

이 기능이 어떻게 작동하는지 확인하려면 [Next.js View Transition Demo](https://view-transition-example.vercel.app)를 살펴보세요.

이 API가 발전함에 따라 문서를 업데이트하고 더 많은 예제를 공유할 예정입니다. 다만 현재로서는 프로덕션 환경에서 이 기능을 사용하는 것을 강력히 권장하지 않습니다.

Was this helpful?

supported.

Send