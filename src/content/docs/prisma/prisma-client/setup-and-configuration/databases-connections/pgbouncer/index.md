---
title: "PgBouncer로 Prisma Client 구성하기"
description: "PgBouncer 및 기타 풀러로 Prisma Client 구성하기: 를 언제 사용해야 하는지, 필요한 트랜잭션 모드, prepared statements, Prisma Migrate 우회 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer

# PgBouncer로 Prisma Client 구성하기

PgBouncer 및 기타 풀러로 Prisma Client 구성하기: `pgbouncer=true`를 언제 사용해야 하는지, 필요한 트랜잭션 모드, prepared statements, Prisma Migrate 우회 방법

PgBouncer 같은 외부 연결 풀러는 데이터베이스에 대한 연결 풀을 유지하고, Prisma Client와 데이터베이스 사이에 위치해 들어오는 클라이언트 연결을 프록시합니다. 이를 통해 데이터베이스가 특정 시점에 처리해야 하는 프로세스 수를 줄일 수 있습니다.

보통은 이 과정이 투명하게 동작하지만, 일부 연결 풀러는 제한된 기능 집합만 지원합니다. 외부 연결 풀러가 흔히 지원하지 않는 기능 중 하나가 Prisma ORM에서 사용하는 named prepared statements입니다. 이런 경우 Prisma ORM이 다르게 동작하도록 구성할 수 있습니다.

이 페이지에서 답하는 질문

- Prisma를 PgBouncer와 어떻게 구성하나요?
- `pgbouncer=true`가 필요한가요? 필요하다면 언제인가요?
- Prisma Migrate는 PgBouncer와 함께 어떻게 동작하나요?

더 쉽고 인프라가 필요 없는 솔루션을 찾고 계신가요? [Prisma Accelerate](https://www.prisma.io/accelerate?utm_source=docs&utm_campaign=pgbouncer-help)를 사용해 보세요! 설정이 거의 또는 전혀 필요하지 않으며, Prisma ORM이 지원하는 모든 데이터베이스와 원활하게 동작합니다.

시작할 준비가 되셨나요? [여기](https://console.prisma.io?utm_source=docs&utm_campaign=pgbouncer-help)를 클릭해 Prisma Accelerate를 시작하세요.

## PgBouncer

- PgBouncer를 트랜잭션 모드로 설정

Prisma Client가 안정적으로 동작하려면 PgBouncer는 [**트랜잭션 모드**](https://www.pgbouncer.org/features.html)로 실행되어야 합니다.

트랜잭션 모드는 각 트랜잭션마다 연결을 제공하며, 이는 Prisma Client가 PgBouncer와 함께 동작하기 위한 필수 조건입니다.

- PgBouncer 버전이 `1.21.0` 미만이면 `pgbouncer=true` 추가

[PgBouncer `1.21.0`](https://github.com/prisma/prisma/issues/21531#issuecomment-1919059472) 이상을 사용 중이라면 데이터베이스 연결 문자열에 `pgbouncer=true`를 설정하지 않을 것을 권장합니다.

Prisma Client를 PgBouncer와 함께 사용하려면 PostgreSQL 연결 URL에 `?pgbouncer=true` 플래그를 추가하세요:

```
    postgresql://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true
```

PgBouncer 풀링에 지정되는 `PORT`는 기본 `5432` 포트와 다른 경우가 있습니다. 올바른 포트 번호는 데이터베이스 제공업체 문서를 확인하세요.

- PgBouncer에서 `max_prepared_statements`를 0보다 크게 설정

Prisma는 prepared statements를 사용하며, [`max_prepared_statements`](https://www.pgbouncer.org/config.html)를 `0`보다 큰 값으로 설정하면 PgBouncer가 해당 prepared statements를 사용할 수 있습니다.

PgBouncer 풀링에 지정되는 `PORT`는 기본 `5432` 포트와 다른 경우가 있습니다. 올바른 포트 번호는 데이터베이스 제공업체 문서를 확인하세요.

- Prisma Migrate 및 PgBouncer 우회 방법

Prisma Migrate는 데이터베이스와 마이그레이션 테이블의 현재 상태를 확인하기 위해 **데이터베이스 트랜잭션**을 사용합니다. 하지만 Schema Engine은 **데이터베이스에 대한 단일 연결을 사용**하도록 설계되어 있으며, PgBouncer를 통한 연결 풀링을 지원하지 않습니다. 연결 풀링에 PgBouncer를 사용하는 환경에서 Prisma Migrate 명령을 실행하려고 하면 다음과 같은 오류가 나타날 수 있습니다:

```
    Error: undefined: Database error
    Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

이 문제를 우회하려면 `prisma.config.ts`에서 Prisma CLI 명령용 **직접** 연결을 구성하고, Prisma Client는 드라이버 어댑터를 통해 계속 PgBouncer URL을 사용하도록 설정하세요.

.env

```
    # PgBouncer (pooled) connection string used by Prisma Client.
    DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true"

    # Direct database connection string used by Prisma CLI.
    DIRECT_URL="postgres://USER:PASSWORD@HOST:PORT/DATABASE"
```

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DIRECT_URL"),
      },
    });
```

src/db/client.ts

```
    import { PrismaClient } from "../prisma/generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    export const prisma = new PrismaClient({ adapter });
```

이 구성에서는 런타임 트래픽 경로에 PgBouncer가 계속 유지되는 반면, Prisma CLI 명령(`prisma migrate dev`, `prisma db push`, `prisma db pull` 등)은 항상 `prisma.config.ts`에 정의된 직접 연결 문자열을 사용합니다.

- 다양한 데이터베이스 제공업체에서의 PgBouncer

Postgres 데이터베이스에 직접 연결하는 방법에는 데이터베이스를 호스팅하는 제공업체에 따라 간혹 작은 차이가 있습니다.

아래는 이 문서에서 다루지 않은 별도 설정 단계가 있는 제공업체에 대해, 이러한 연결을 설정하는 방법을 안내하는 링크입니다:

- Digital Ocean에 호스팅된 PostgreSQL 데이터베이스에 직접 연결
- ScaleGrid에 호스팅된 PostgreSQL 데이터베이스에 직접 연결

## Supabase Supavisor

Supabase의 Supavisor는 [PgBouncer](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer#pgbouncer)와 유사하게 동작합니다. [Supabase 데이터베이스 설정](https://supabase.com/dashboard/project/_/settings/database)에서 확인할 수 있는 연결 풀링 연결 문자열에 `?pgbouncer=true`를 추가할 수 있습니다.

## 기타 외부 연결 풀러

Prisma ORM이 다른 연결 풀러를 명시적으로 지원하지는 않지만, 제한 사항이 [PgBouncer](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer#pgbouncer)와 유사하다면 연결 문자열에서 `pgbouncer=true`를 사용해 Prisma ORM을 해당 풀러와도 동작하는 모드로 전환할 수 있는 경우가 많습니다.
