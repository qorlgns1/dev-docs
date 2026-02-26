---
title: 'Prisma | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x

# Prisma | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*Import name: `Sentry.prismaIntegration`*

Sentry는 Prisma 통합을 통해 [Prisma ORM](https://www.prisma.io/) 쿼리 추적을 지원합니다.

Prisma 통합은 각 쿼리에 대한 span을 생성하고, 가능한 경우 관련 세부 정보를 `description`에 담아 Sentry로 보고합니다.

## [Prisma 버전 6](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prisma-version-6)

Sentry Prisma 통합은 기본적으로 Prisma 버전 5를 지원합니다. Prisma 버전 6과의 호환을 위해서는 Prisma instrumentation의 특정 버전을 Sentry Prisma 통합에 전달해야 합니다.

Prisma 버전 6에서 이 통합을 사용하려면, 먼저 `@prisma/instrumentation` 패키지의 버전 6을 설치하세요(가능하면 `prisma` 및 `@prisma/client` 패키지와 정확히 동일한 버전 권장).

그다음 아래와 같이 Sentry 초기화에 `prismaIntegration`을 추가하세요:

```javascript
import { PrismaInstrumentation } from "@prisma/instrumentation";

Sentry.init({
  tracesSampleRate: 1.0,
  integrations: [

    Sentry.prismaIntegration({
      // Override the default instrumentation that Sentry uses
      prismaInstrumentation: new PrismaInstrumentation(),
    }),

  ],
});
```

## [Prisma 버전 5](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prisma-version-5)

Prisma 버전 5용 통합을 구성하려면, 먼저 Prisma 스키마의 `generator` 블록에 `tracing` 기능 플래그를 추가하세요:

`schema.prisma`

```txt
generator client {
  provider        = "prisma-client-js"

  previewFeatures = ["tracing"]

}
```

그다음 아래와 같이 Sentry 초기화에 `prismaIntegration`을 추가하세요:

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#options)

- [`prismaInstrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prismainstrumentation)

*Type: `Instrumentation`* (OpenTelemetry 타입)

Sentry SDK에서 사용하는 instrumentation을, 전달된 instrumentation 인스턴스로 재정의합니다.

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#supported-versions)

* `prisma`: `>=5`

