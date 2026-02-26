---
title: 'ContextLines | Next.js용 Sentry'
description: '이 통합은 현재 페이지 HTML의 인라인 JavaScript 소스 코드(예:  태그 안의 JS)를 캡처된 오류의 스택 트레이스에 추가합니다. HTML에서 참조하는 에셋의 소스 코드(예: )는 수집할 수 *없습니다*.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines

# ContextLines | Next.js용 Sentry

*Import 이름: `Sentry.contextLinesIntegration`*

이 통합은 현재 페이지 HTML의 인라인 JavaScript 소스 코드(예: `<script>` 태그 안의 JS)를 캡처된 오류의 스택 트레이스에 추가합니다. HTML에서 참조하는 에셋의 소스 코드(예: `<script src="..." />`)는 수집할 수 *없습니다*.

`ContextLines` 통합은 로그인 보호 페이지처럼 Sentry 백엔드에서 접근할 수 없는 HTML 페이지에 인라인 JS 코드가 있을 때 유용합니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.contextLinesIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md#options)

- [`frameContextLines`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md#framecontextlines)

*유형: `number`*

각 스택 프레임의 라인 번호 주변에서 수집할 줄 수입니다. 기본값은 7입니다.

