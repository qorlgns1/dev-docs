---
title: 'trpcMiddleware | Next.js용 Sentry'
description: '이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc

# trpcMiddleware | Next.js용 Sentry

이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.

*Import name: `Sentry.trpcMiddleware`*

Sentry tRPC 미들웨어는 자동으로 span을 생성하고 tRPC 핸들러의 에러 캡처를 개선합니다.

`trpcMiddleware`는 전통적인 SDK 통합과는 달리 `integrations` 옵션에 추가하는 방식이 **아닙니다**. 대신 tRPC 라우터에 미들웨어로 추가하세요.

```javascript
import * as Sentry from "@sentry/node";
import { initTRPC } from "@trpc/server";

const t = initTRPC.context().create();

const sentryMiddleware = t.middleware(
  Sentry.trpcMiddleware({
    attachRpcInput: true,
  }),
);

const sentrifiedProcedure = t.procedure.use(sentryMiddleware);
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md#options)

- [`attachRpcInput`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md#attachrpcinput)

*유형: `boolean`*

기본값은 `false`입니다. 활성화하면 RPC 입력이 에러 이벤트의 `trpc` 컨텍스트로 캡처됩니다.

##### 잘린 입력

`trpc` 컨텍스트의 중첩 객체가 "`[Object]`"로 잘려 보인다면, 컨텍스트에서 더 깊게 중첩된 객체를 허용하도록 [`normalizeDepth` 값](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#normalizeDepth)을 정의할 수 있습니다. `trpc` 컨텍스트의 기본 깊이는 5입니다.

