---
title: 'ExtraErrorData | Next.js용 Sentry'
description: '이 통합은 에러 객체에서 네이티브가 아닌 모든 속성을 추출하여 이벤트에 추가 데이터로 첨부합니다. 에러 객체에  메서드가 있으면 ExtraErrorData 통합이 이를 실행해 추가 정보를 추출합니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata

# ExtraErrorData | Next.js용 Sentry

*Import 이름: `Sentry.extraErrorDataIntegration`*

이 통합은 에러 객체에서 네이티브가 아닌 모든 속성을 추출하여 이벤트에 추가 데이터로 첨부합니다. 에러 객체에 `.toJSON()` 메서드가 있으면 ExtraErrorData 통합이 이를 실행해 추가 정보를 추출합니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.extraErrorDataIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#options)

- [`depth`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#depth)

*유형: `number`*

객체 serializer가 어느 깊이까지 탐색할지 제한합니다. 기본값은 3입니다. 설정한 제한보다 더 깊은 값은 표준 Node.js REPL 표기인 \[Object], \[Array], \[Function] 또는 원시 값으로 대체됩니다.

- [`captureErrorCause`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md#captureerrorcause)

*유형: `boolean`*

serializer가 에러의 `cause`를 수집할지 여부를 나타냅니다. 기본값은 true입니다. 자세한 내용은 [Error: cause MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)를 참고하세요.

