---
title: 'ReportingObserver | Next.js용 Sentry'
description: '이 통합은 브라우저 환경에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver

# ReportingObserver | Next.js용 Sentry

이 통합은 브라우저 환경에서만 작동합니다.

*Import name: `Sentry.reportingObserverIntegration`*

이 통합은 [Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API)에 연결되어 캡처된 이벤트를 Sentry로 전송합니다. 특정 이슈 유형만 처리하도록 구성할 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.reportingObserverIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md#options)

- [`types`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md#types)

*Type: `('crash'|'deprecation'|'intervention')[]`*

지정된 이슈 유형만 처리합니다. 기본적으로 모든 이슈 유형이 처리됩니다.

