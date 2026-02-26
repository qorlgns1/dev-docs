---
title: 'Pino | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 작동합니다. SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino

# Pino | Next.js용 Sentry

이 통합은 Node.js 런타임에서만 작동합니다. SDK 버전 `10.18.0` 이상이 필요합니다.

*임포트 이름: `Sentry.pinoIntegration`*

`pinoIntegration`은 `pino` 라이브러리에 계측을 추가하여 pino 로거 호출을 로그로 캡처합니다. 선택적으로, pino 로거 호출을 오류로 캡처할 수도 있습니다.

```JavaScript
Sentry.init({
  enableLogs: true,
  integrations: [Sentry.pinoIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#options)

- [`error`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#error)

pino 로그를 Sentry 오류로 캡처하는 방법을 구성합니다.

#
- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#levels)

* 유형: `Array<'trace' | 'debug' | 'info' | 'warn' | 'error' | 'fatal'>`
* 기본값: `[]`

이벤트 캡처를 트리거하는 레벨입니다. pino 로그 메시지가 이 레벨 중 하나로 기록되면 Sentry 오류 이벤트로 캡처됩니다.

#
- [`handled`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#handled)

* 유형: `boolean`
* 기본값: `true`

기본적으로 Sentry는 캡처된 오류를 handled로 표시합니다. 대신 unhandled로 표시하려면 이를 `false`로 설정하세요.

- [`log`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#log)

pino 로그를 Sentry 로그로 캡처하는 방법을 구성합니다.

#
- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#levels-1)

* 유형: `Array<'trace' | 'debug' | 'info' | 'warn' | 'error' | 'fatal'>`
* 기본값: `["trace", "debug", "info", "warn", "error", "fatal"]`

로그 캡처를 트리거하는 레벨입니다. 로그는 Sentry 구성에서 `enableLogs`가 활성화된 경우에만 캡처됩니다.

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#supported-versions)

* `pino`: `>=8.0.0 <11`

## [예제](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#examples)

- [info, error, warn 로그 레벨만 Sentry로 전송](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#send-only-info-error-and-warn-log-levels-to-sentry)

```js
Sentry.init({
  enableLogs: true,
  integrations: [
    Sentry.pinoIntegration({ log: { levels: ["info", "warn", "error"] } }),
  ],
});
```

- [오류를 Sentry로 전송](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#send-errors-to-sentry)

```js
Sentry.init({
  enableLogs: true,
  integrations: [
    Sentry.pinoIntegration({ error: { levels: ["warn", "error"] } }),
  ],
});
```

