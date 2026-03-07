---
title: "데이터베이스 드라이버"
description: "드라이버 어댑터를 사용해 Prisma가 데이터베이스에 연결하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers

# 데이터베이스 드라이버

드라이버 어댑터를 사용해 Prisma가 데이터베이스에 연결하는 방법을 알아보세요.

## 드라이버 어댑터

Prisma Client는 **드라이버 어댑터**를 통해 JavaScript 데이터베이스 드라이버를 사용하여 데이터베이스에 연결하고 쿼리를 실행할 수 있습니다. 어댑터는 Prisma Client와 JavaScript 데이터베이스 드라이버 사이에서 _변환기_ 역할을 합니다.

Prisma Client는 Query Engine을 사용해 Prisma Client 쿼리를 SQL로 변환하고, 생성된 SQL 쿼리를 JavaScript 데이터베이스 드라이버를 통해 실행합니다.

![Prisma Client와 드라이버 어댑터를 사용했을 때 사용자 애플리케이션에서 데이터베이스로 이어지는 쿼리 흐름](https://docs.prisma.io/docs/img/orm/core-concepts/databases/images/drivers/qe-query-engine-adapter.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

드라이버 어댑터에는 두 가지 유형이 있습니다.

- 데이터베이스 드라이버 어댑터
- 서버리스 드라이버 어댑터

> **참고** : 드라이버 어댑터를 사용하면 Prisma ORM을 사용하는 애플리케이션을 [edge deployments](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/overview)할 수 있습니다.

- 데이터베이스 드라이버 어댑터

데이터베이스 드라이버 어댑터를 사용하면 Prisma Client에서 Node.js 기반 드라이버로 데이터베이스에 연결할 수 있습니다. Prisma는 다음 드라이버에 대한 어댑터를 유지관리합니다.

- PostgreSQL
  - `pg`
- Prisma Postgres
  - `@prisma/adapter-ppg`
- MySQL/MariaDB
  - `mariadb`
- SQLite
  - `better-sqlite3`
  - [`libSQL`](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite#using-driver-adapters) (Turso)
- MS SQL Server
  - `node-mssql`

* 서버리스 드라이버 어댑터

Neon 및 PlanetScale 같은 데이터베이스 제공업체는 TCP 외에도 HTTP, WebSockets 같은 다른 프로토콜로 데이터베이스에 연결할 수 있게 해줍니다. 이러한 데이터베이스 드라이버는 서버리스 및 엣지 환경에서 데이터베이스 연결에 최적화되어 있습니다.

Prisma ORM은 다음 서버리스 드라이버 어댑터를 유지관리합니다.

- Prisma Postgres
- [Neon](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#neon) (및 Vercel Postgres)
- PlanetScale
- Cloudflare D1

* 커뮤니티 유지관리 데이터베이스 드라이버 어댑터

현재 사용 중인 데이터베이스를 위한 드라이버 어댑터를 직접 만들 수도 있습니다. 아래는 커뮤니티에서 유지관리하는 드라이버 어댑터 목록입니다.

- TiDB Cloud Serverless Driver
- PGlite - Postgres in WASM

## 드라이버 어댑터 사용 방법

특정 데이터베이스 제공업체에서 특정 드라이버 어댑터를 사용하는 방법은 아래 페이지를 참고하세요.

- PostgreSQL
- Prisma Postgres
- MySQL/MariaDB
- MS SQL Server
- Neon
- PlanetScale
- Turso
- Cloudflare D1
- CockroachDB

## 드라이버 어댑터 사용 시 참고 사항

- v6.6.0의 새로운 드라이버 어댑터 API

[v6.6.0](https://github.com/prisma/prisma/releases/tag/6.6.0)에서는 드라이버 어댑터 사용 시 Prisma Client를 초기화하는 간소화된 방식을 도입했습니다. 이제 드라이버/클라이언트 인스턴스를 만들어 드라이버 어댑터에 전달할 필요 없이, 드라이버 어댑터를 직접 생성하면 됩니다(필요한 경우 드라이버 옵션 전달).

다음은 `@prisma/adapter-libsql` 어댑터를 사용하는 예시입니다.

#

- 6.6.0 이전

이전 버전의 Prisma ORM에서는 먼저 드라이버 자체를 초기화한 뒤, 해당 인스턴스로 Prisma 드라이버 어댑터를 생성해야 했습니다. 아래는 LibSQL용 `@libsql/client` 드라이버를 사용하는 예시입니다.

```
    import { createClient } from "@libsql/client";
    import { PrismaLibSQL } from "@prisma/adapter-libsql";
    import { PrismaClient } from "../prisma/generated/client";

    // Old way of using driver adapters (before 6.6.0)
    const driver = createClient({
      url: env.LIBSQL_DATABASE_URL,
      authToken: env.LIBSQL_DATABASE_TOKEN,
    });
    const adapter = new PrismaLibSQL(driver);

    const prisma = new PrismaClient({ adapter });
```

#

- 6.6.0 이후

  6.6.0 릴리스부터는 선호하는 JS 네이티브 드라이버의 옵션으로 드라이버 어댑터를 _직접_ 초기화합니다.:

```
    import { PrismaLibSQL } from "@prisma/adapter-libsql";
    import { PrismaClient } from "../generated/prisma/client";

    const adapter = new PrismaLibSQL({
      url: env.LIBSQL_DATABASE_URL,
      authToken: env.LIBSQL_DATABASE_TOKEN,
    });

    const prisma = new PrismaClient({ adapter });
```

- 드라이버 어댑터와 데이터베이스 연결 구성

Prisma ORM 7에서는 데이터베이스 연결 URL을 [`prisma.config.ts`](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)에서 구성합니다. 하지만 드라이버 어댑터를 사용하는 경우, 연결 문자열은 드라이버 어댑터를 최초 설정할 때 *애플리케이션 코드*에서 제공해야 합니다.

다음은 `pg` 드라이버와 `@prisma/adapter-pg` 어댑터에서 이를 처리하는 방법입니다.

```
    import "dotenv/config";
    import { PrismaClient } from "../generated/prisma/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });
```

구체적인 설정 방법은 사용 중인 드라이버 어댑터 문서를 참고하세요.

풀 크기, 타임아웃 또는 기타 연결 매개변수 튜닝

Prisma ORM v7의 드라이버 어댑터 기본값과 Prisma ORM v6 URL 매개변수에서의 매핑 방식은 [connection pool guide](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)를 참고하세요.

Prisma 타임아웃

Prisma ORM에는 데이터베이스 드라이버 타임아웃과 별도로 설정 가능한 자체 타임아웃이 있습니다. 타임아웃 오류가 발생했을 때 원인이 드라이버인지 Prisma Client인지 확실하지 않다면 [Prisma Client timeouts and transaction options documentation](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#transaction-isolation-level)을 참고하세요.

- 드라이버 어댑터와 사용자 지정 출력 경로

Prisma ORM 7에서는 Prisma Client에 사용자 지정 출력 경로를 사용하는 방식을 권장합니다. 기본 출력 경로는 `../generated/prisma`입니다.

Prisma 스키마에서 `output`을 `../generated/prisma`로 설정했다고 가정해 보겠습니다.

```
    generator client {
      provider = "prisma-client"
      output   = "../src/generated/prisma"
    }
```

애플리케이션 코드에서 상대 경로를 사용해 Prisma Client를 참조할 수 있습니다.

```
    import { PrismaClient } from "./generated/prisma/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const client = new PrismaClient({ adapter });
```

또는 더 깔끔한 import를 위해 링크된 의존성을 사용할 수 있습니다.

npm

pnpm

yarn

bun

```
    npm add db@./generated/prisma
```

pnpm의 경우 `pnpm add db@link:./generated/prisma`를 사용하세요. yarn의 경우 `yarn add db@link:./generated/prisma`를 사용하세요.

이제 `db`를 사용해 생성된 client를 참조할 수 있습니다!

```
    import { PrismaClient } from "db";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const client = new PrismaClient({ adapter });
```

- 드라이버 어댑터와 특정 프레임워크

#

- Nuxt

[Nuxt](https://nuxt.com/)에서 드라이버 어댑터를 사용해 edge function 환경으로 배포하는 경우 기본 설정만으로는 동작하지 않지만, `nitro.experimental.wasm` 구성 옵션을 추가하면 해결됩니다.

```
    export default defineNuxtConfig({
      // ...
      nitro: {
        // ...
        experimental: {
          wasm: true,
        },
      },
      // ...
    });
```

- 드라이버 어댑터와 TypedSQL

[TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql)을 사용하면 Prisma Client와 직접 통합되는 완전한 타입 안전 SQL 쿼리를 작성할 수 있습니다. 이 기능은 SQL 작성의 유연성을 원하면서도 Prisma의 타입 안전성 이점을 유지하고 싶을 때 유용합니다.

또한 TypedSQL과 함께 드라이버 어댑터를 사용해 JavaScript 데이터베이스 드라이버로 연결할 수 있습니다. TypedSQL은 `@prisma/adapter-better-sqlite3`를 제외한 모든 지원 드라이버 어댑터에서 동작합니다. SQLite를 지원하려면 대신 [`@prisma/adapter-libsql`](https://www.npmjs.com/package/@prisma/adapter-libsql)을 사용하세요.
