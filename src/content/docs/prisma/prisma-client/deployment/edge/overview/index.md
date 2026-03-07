---
title: "Prisma ORM으로 edge function 배포하기"
description: "Cloudflare Workers 또는 Vercel Edge Functions 같은 edge function에 Prisma 기반 앱을 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/overview

# Prisma ORM으로 edge function 배포하기

Cloudflare Workers 또는 Vercel Edge Functions 같은 edge function에 Prisma 기반 앱을 배포하는 방법을 알아보세요.

Prisma ORM을 사용하는 애플리케이션을 edge에 배포할 수 있습니다. 어떤 edge function 제공자와 어떤 데이터베이스를 사용하는지에 따라 고려해야 할 사항과 주의점이 달라집니다.

이 페이지에서 답하는 질문

- edge에서 어떤 데이터베이스 드라이버가 동작하나요?
- driver adapter가 연결에 어떤 영향을 주나요?
- Prisma Postgres 또는 Accelerate는 언제 사용해야 하나요?

다음은 현재 Prisma ORM이 지원하는 모든 edge function 제공자에 대한 간단한 개요입니다.

| Provider / Product     | Supported natively with Prisma ORM                                 | Supported with Prisma Postgres (and Prisma Accelerate) |
| ---------------------- | ------------------------------------------------------------------ | ------------------------------------------------------ |
| Vercel Edge Functions  | ✅ (Preview; only compatible drivers)                              | ✅                                                     |
| Vercel Edge Middleware | ✅ (Preview; only compatible drivers)                              | ✅                                                     |
| Cloudflare Workers     | ✅ (Preview; only compatible drivers)                              | ✅                                                     |
| Cloudflare Pages       | ✅ (Preview; only compatible drivers)                              | ✅                                                     |
| Deno Deploy            | [아직 지원되지 않음](https://github.com/prisma/prisma/issues/2452) | ✅                                                     |

현재 Cloudflare 및 Vercel에서 Prisma ORM을 사용하는 edge function 배포는 [Preview](https://docs.prisma.io/docs/orm/more/releases#preview) 상태입니다.

## 데이터베이스 드라이버의 Edge 호환성

- edge function에서 데이터베이스 드라이버 관련 제약이 있는 이유는 무엇인가요?

edge function은 일반적으로 표준 Node.js 런타임을 사용하지 않습니다. 예를 들어, Vercel Edge Functions와 Cloudflare Workers는 [V8 isolates](https://v8docs.nodesource.com/node-0.8/d5/dda/classv8_1_1_isolate.html)에서 코드를 실행합니다. Deno Deploy는 [Deno](https://deno.com/) JavaScript 런타임을 사용합니다. 그 결과, 이러한 edge function은 표준 Node.js API의 일부만 사용할 수 있고, 컴퓨팅 리소스(CPU 및 메모리)도 제한됩니다.

특히 TCP 연결을 자유롭게 열 수 없다는 제약 때문에 edge function에서 전통적인 데이터베이스와 통신하기가 어렵습니다. Cloudflare가 제한적인 TCP 연결을 가능하게 하는 [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) API를 도입했지만, 이 경우에도 해당 API와 호환되는 특정 데이터베이스 드라이버를 사용해야만 데이터베이스에 접근할 수 있습니다.

[Prisma Postgres](https://docs.prisma.io/docs/postgres) 사용을 권장합니다. edge 런타임에서 완전히 지원되며, 별도의 edge 호환 전용 드라이버가 필요하지 않습니다.

- 어떤 데이터베이스 드라이버가 edge와 호환되나요?

다음은 다양한 데이터베이스 드라이버와 각 edge function 환경에서의 호환성 개요입니다.

- [Neon Serverless](https://neon.tech/docs/serverless/serverless-driver)는 HTTP로 데이터베이스에 접근합니다. Cloudflare Workers 및 Vercel Edge Functions에서 동작합니다.
- [PlanetScale Serverless](https://planetscale.com/docs/tutorials/planetscale-serverless-driver)는 HTTP로 데이터베이스에 접근합니다. Cloudflare Workers 및 Vercel Edge Functions에서 동작합니다.
- [`node-postgres`](https://node-postgres.com/) (`pg`)는 Cloudflare의 `connect()` (TCP)를 사용해 데이터베이스에 접근합니다. Cloudflare Workers에서만 호환되며, Vercel Edge Functions에서는 호환되지 않습니다.
- [`@libsql/client`](https://github.com/tursodatabase/libsql-client-ts)는 Turso 데이터베이스 접근에 사용됩니다. Cloudflare Workers 및 Vercel Edge Functions에서 동작합니다.
- [Cloudflare D1](https://developers.cloudflare.com/d1/)은 D1 데이터베이스 접근에 사용됩니다. Cloudflare Workers에서만 호환되며, Vercel Edge Functions에서는 호환되지 않습니다.
- [Prisma Postgres](https://docs.prisma.io/docs/postgres)는 unikernels를 기반으로 bare-metal에서 구축된 PostgreSQL 데이터베이스에 접근하는 데 사용됩니다. Cloudflare Workers와 Vercel 모두에서 지원됩니다.

향후 Cloudflare Workers와 Pages에서도 전통적인 MySQL 데이터베이스에 접근할 수 있도록 `node-mysql2` 드라이버에 대한 [작업도 진행 중](https://github.com/sidorares/node-mysql2/pull/2289)입니다.

이 모든 드라이버는 해당 [driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)를 사용해 Prisma ORM과 함께 사용할 수 있습니다.

사용하는 배포 제공자와 데이터베이스/드라이버 조합에 따라 특별한 고려 사항이 있을 수 있습니다. 애플리케이션을 성공적으로 배포하려면 각 시나리오에 맞는 배포 문서를 확인하세요.

- Cloudflare
  - PostgreSQL (traditional)
  - PlanetScale
  - Neon
  - Cloudflare D1
  - Prisma Postgres
- Vercel
  - Vercel Postgres
  - Neon
  - PlanetScale
  - Prisma Postgres

Turso를 사용하는 앱을 배포하려면 [여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite#using-driver-adapters)의 안내를 따르세요.
