---
title: 'ZodErrors | Next.js용 Sentry'
description: 'Zod Errors 통합은 Zod 스키마 검증을 사용하는 애플리케이션의 오류 보고를 강화합니다. Zod 검증이 실패하면, 이 통합은 상세한 검증 오류( 인스턴스)를 수집하고 이를 Sentry 이벤트에 추가 데이터로 첨부합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors

# ZodErrors | Next.js용 Sentry

*가져오기 이름: `Sentry.zodErrorsIntegration`*

Zod Errors 통합은 [Zod](https://zod.dev/) 스키마 검증을 사용하는 애플리케이션의 오류 보고를 강화합니다. Zod 검증이 실패하면, 이 통합은 상세한 검증 오류(`ZodError` 인스턴스)를 수집하고 이를 Sentry 이벤트에 추가 데이터로 첨부합니다.

Zod Errors 통합은 기본적으로 활성화되어 있지 않습니다. Sentry 설정에 이를 추가해야 합니다:

```javascript
Sentry.init({
  integrations: [Sentry.zodErrorsIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#options)

`zodErrorsIntegration`은 다음 옵션을 받습니다:

- [`limit`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#limit)

*유형: `number`* *기본값: `10`*

각 Sentry 이벤트에 인라인으로 포함되는 Zod 오류의 수를 제한합니다.

- [`saveZodIssuesAsAttachment`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#savezodissuesasattachment)

*유형: `boolean`* *기본값: `false`*

Zod 이슈 전체 목록을 Sentry에서 JSON 첨부 파일로 저장합니다.

## [추가 오류 데이터 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md#example-additional-error-data)

Zod 검증 오류가 발생하면, Sentry에서 다음과 같이 강화된 오류 정보를 볼 수 있습니다:

```json
[
  {
    "code": "too_small",
    "path": ["name"],
    "message": "Name is required",
    "minimum": 1,
    "type": "string",
    "inclusive": true,
    "received": ""
  },
  {
    "code": "invalid_string",
    "path": ["email"],
    "message": "Invalid email format",
    "validation": "email",
    "received": "invalid-email"
  }
]
```

