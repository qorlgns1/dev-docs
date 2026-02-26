---
title: 'OnUncaughtException | Next.js용 Sentry'
description: '이 통합은 서버 환경(Node.js, Bun, Deno) 내부에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception

# OnUncaughtException | Next.js용 Sentry

이 통합은 서버 환경(Node.js, Bun, Deno) 내부에서만 동작합니다.

*Import name: `Sentry.onUncaughtExceptionIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하고 싶다면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`onUncaughtExceptionIntegration`은 프로세스를 종료시킬 수 있는 전역의 처리되지 않은 예외를 캡처하기 위해 핸들러를 등록합니다.

이 통합은 프로세스 종료를 *막지 않습니다*! 프로세스가 종료되지 않게 하려면 직접 uncaught exception 핸들러를 등록하고, 통합 옵션에서 `exitEvenIfOtherHandlersAreRegistered: false`로 설정해야 합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.onUncaughtExceptionIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#options)

- [`exitEvenIfOtherHandlersAreRegistered`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#exitevenifotherhandlersareregistered)

*Type: `boolean`*

false로 설정하면, 다른 uncaught exception 핸들러가 등록되어 있는 것이 감지될 경우 SDK는 종료되지 *않습니다*.

- [`onFatalError`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#onfatalerror)

*Type: `(firstError: Error, secondError: Error | undefined) => void`*

이 메서드는 처리되지 않은 오류로 인해 프로세스가 종료될 상황에서 호출됩니다. 핸들러가 여러 번 호출된 경우 `secondError`가 설정됩니다. 이는 `onFatalError` 자체에서 예외가 발생했거나, `onFatalError`가 실행되는 동안 다른 위치에서 독립적인 오류가 발생했기 때문일 수 있습니다.

