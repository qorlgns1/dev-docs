---
title: 'OnUnhandledRejection | Next.js용 Sentry'
description: '이 통합은 서버 환경(Node.js, Bun, Deno) 내부에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection

# OnUnhandledRejection | Next.js용 Sentry

이 통합은 서버 환경(Node.js, Bun, Deno) 내부에서만 동작합니다.

*가져오기 이름: `Sentry.onUnhandledRejectionIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`onUnhandledRejectionIntegration`은 전역에서 처리되지 않은 Promise rejection을 캡처하기 위한 핸들러를 등록합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.onUnhandledRejectionIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md#options)

- [`mode`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md#mode)

*유형: `'none' | 'warn' | 'strict'`*

이 옵션은 처리되지 않은 rejection을 캡처한 뒤 무엇을 할지 정의하며, [Node](https://nodejs.org/api/cli.html#--unhandled-rejectionsmode)의 `--unhandled-rejection` 플래그 동작을 모방합니다.

* `strict`: 처리되지 않은 rejection을 포착되지 않은 예외로 발생시킵니다. 예외가 처리되면 unhandledRejection이 emit됩니다.
* `warn`: unhandledRejection hook 설정 여부와 관계없이 항상 경고를 트리거하지만, deprecation 경고는 출력하지 않습니다.
* `none`: 모든 경고를 숨깁니다.

기본값은 `warn`입니다.

