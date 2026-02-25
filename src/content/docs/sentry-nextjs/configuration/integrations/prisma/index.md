---
title: 'Prisma | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma

# Prisma | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*임포트 이름: `Sentry.prismaIntegration`*

Sentry는 Prisma 통합을 통해 [Prisma ORM](https://www.prisma.io/) 쿼리 추적을 지원합니다.

Prisma Integration은 각 쿼리에 대한 span을 생성하며, 가능한 경우 `description` 내 관련 세부 정보를 포함해 Sentry로 보고합니다.

이 통합은 기본적으로 활성화되어 있으며 Prisma 버전 5, 6, 7을 지원합니다. Prisma v5에서는 추적을 활성화하려면 아래 지침을 따라야 합니다.

기본 통합을 수정하는 방법을 알아보려면 [Modifying Default Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations) 문서를 참고하세요.

## [Prisma 버전 6 및 7](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#prisma-version-6--7)

Prisma 버전 6 또는 7에서 이 통합을 사용하려면 별도 설정이 필요하지 않습니다. 추적은 기본적으로 활성화되어 있습니다.

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [Prisma 버전 5](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#prisma-version-5)

Prisma 버전 5에서 통합을 설정하려면 먼저 Prisma 스키마의 `generator` 블록에 `tracing` 기능 플래그를 추가하세요.

`schema.prisma`

```txt
generator client {
  provider        = "prisma-client-js"

  previewFeatures = ["tracing"]

}
```

그다음 `prismaIntegration`이 Prisma 쿼리에 대한 span을 자동으로 수집합니다.

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [지원되는 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#supported-versions)

* `prisma`: `5.x`, `6.x`, `7.x`

## [더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#learn-more)

Prisma의 OpenTelemetry 추적이 생성하는 span 구조(예: `prisma:client:operation`, `prisma:engine:db_query`)에 대한 자세한 내용은 [Prisma trace output documentation](https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#trace-output)을 참고하세요.

