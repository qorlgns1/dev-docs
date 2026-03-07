---
title: "PostgreSQL"
description: "자체 호스팅, 서버리스(Neon, Supabase), CockroachDB를 포함한 PostgreSQL 데이터베이스에서 Prisma ORM을 사용하세요"
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql

# PostgreSQL

자체 호스팅, 서버리스(Neon, Supabase), CockroachDB를 포함한 PostgreSQL 데이터베이스에서 Prisma ORM을 사용하세요

Prisma ORM은 자체 호스팅 PostgreSQL, 서버리스 제공자(Neon, Supabase), CockroachDB를 포함한 PostgreSQL 및 PostgreSQL 호환 데이터베이스를 지원합니다.

## 설정

Prisma 스키마에서 provider를 구성합니다:

schema.prisma

```
    datasource db {
      provider = "postgresql" // or "cockroachdb" for CockroachDB
    }
```

**자체 호스팅 PostgreSQL:**

prisma.config.ts

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"), // postgres://user:pass@host:5432/db
      },
    });
```

**서버리스(Neon/Supabase):**

CLI(직접 연결)와 런타임(풀링)에 대해 별도의 URL을 사용합니다:

.env

```
    DATABASE_URL="postgres://user:pass@host-pooler:6543/db?pgbouncer=true"
    DIRECT_URL="postgres://user:pass@host:5432/db"
```

prisma.config.ts

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DIRECT_URL"), // CLI uses direct connection
      },
    });
```

## 드라이버 어댑터 사용

[driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 통해 JavaScript 데이터베이스 드라이버를 사용합니다:

**`pg`를 사용하는 표준 PostgreSQL:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-pg
```

```
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });
```

**Neon 서버리스:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-neon
```

```
    import { PrismaNeon } from "@prisma/adapter-neon";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaNeon({ connectionString: process.env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });
```

## 지원되는 변형

- 자체 호스팅 PostgreSQL

표준 PostgreSQL 서버(9.6+).

- Connection URL: `postgresql://user:pass@host:5432/database`
- Prisma Migrate 완전 지원
- 개발 환경에서는 `prisma migrate dev` 사용
- 연결 문자열 파라미터를 통한 TLS/SSL 구성

**연결 문자열 인수:**

| Argument          | Default  | Description                              |
| ----------------- | -------- | ---------------------------------------- |
| `schema`          | `public` | 사용할 PostgreSQL 스키마                 |
| `connect_timeout` | `5`      | 연결 대기 시간(초) (0 = 타임아웃 없음)   |
| `sslmode`         | `prefer` | TLS 모드: `prefer`, `disable`, `require` |
| `sslcert`         |          | 서버 인증서 경로                         |
| `sslidentity`     |          | PKCS12 인증서 경로                       |

- Neon

자동 스케일링과 브랜칭을 제공하는 서버리스 PostgreSQL.

- Connection URL: `postgres://user:pass@host-pooler.region.aws.neon.tech:5432/db`
- 연결 풀링(PgBouncer, 10k connections)을 위해 호스트명에 `-pooler` 추가
- 5분 비활성 상태 후 컴퓨트가 scale to zero
- 콜드 스타트: 500ms - 수 초
- 개발 워크플로를 위한 데이터베이스 브랜칭

**타임아웃 구성:** [driver adapter](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)에서 연결 및 풀 타임아웃을 구성합니다(예: `pg`의 `connectionTimeoutMillis`).

**리소스:** [Neon docs](https://neon.tech/docs) • [Connection pooling](https://neon.tech/docs/connect/connection-pooling)

- Supabase

인증, 스토리지, 실시간 기능이 내장된 PostgreSQL 호스팅.

**연결 유형:**

- **직접 연결:** `db.[project-ref].supabase.co:5432`
- **트랜잭션 풀러:** `?pgbouncer=true`와 함께 포트 `6543`
- **세션 풀러:** 풀러 호스트의 포트 `5432`

**주요 기능:**

- Supavisor 연결 풀링
- 내장 PostgreSQL 확장
- Supabase 생태계와 통합
- 자동 백업

**리소스:** [Supabase docs](https://supabase.com/docs) • [Prisma integration](https://supabase.com/partners/integrations/prisma)

- CockroachDB

확장성과 고가용성을 위해 설계된 분산형 PostgreSQL 호환 데이터베이스.

- 스키마에서 `provider = "cockroachdb"` 사용
- Connection URL: `postgresql://user:pass@host:26257/database`
- 내장 복제 및 자동 장애 조치
- 단일 장애 지점 없는 수평 확장

**주요 차이점:**

| Feature        | PostgreSQL        | CockroachDB                            |
| -------------- | ----------------- | -------------------------------------- |
| Native types   | `VARCHAR(n)`      | `STRING(n)`                            |
| ID generation  | `autoincrement()` | `unique_rowid()` 사용                  |
| Sequential IDs | 권장              | 피해야 함(`autoincrement()` 사용 권장) |

**ID 생성 예시:**

```
    model User {
      id   BigInt @id @default(autoincrement()) // Uses unique_rowid()
      name String
    }
```

기존 데이터베이스와의 호환성을 위해 `sequence()`를 사용합니다:

```
    model User {
      id   Int    @id @default(sequence())
      name String
    }
```

**리소스:** [CockroachDB docs](https://www.cockroachlabs.com/docs/) • [Primary key best practices](https://www.cockroachlabs.com/docs/stable/schema-design-table#primary-key-best-practices)

## 타입 매핑

- Prisma to PostgreSQL

| Prisma     | PostgreSQL         | CockroachDB |
| ---------- | ------------------ | ----------- |
| `String`   | `text`             | `STRING`    |
| `Boolean`  | `boolean`          | `BOOL`      |
| `Int`      | `integer`          | `INT4`      |
| `BigInt`   | `bigint`           | `INT8`      |
| `Float`    | `double precision` | `FLOAT8`    |
| `Decimal`  | `decimal(65,30)`   | `DECIMAL`   |
| `DateTime` | `timestamp(3)`     | `TIMESTAMP` |
| `Json`     | `jsonb`            | `JSONB`     |
| `Bytes`    | `bytea`            | `BYTES`     |

전체 상세 내용은 [full type mapping reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)를 참조하세요.

## 일반적인 패턴

**SSL 연결:**

```
    DATABASE_URL="postgresql://user:pass@host:5432/db?sslmode=require&sslcert=./cert.pem"
```

- `sslmode=prefer` (기본값) - 가능하면 TLS 사용
- `sslmode=require` \- TLS 필수, 아니면 실패
- `sslmode=disable` \- TLS 사용 안 함

**소켓 연결:**

```
    DATABASE_URL="postgresql://user:pass@localhost/db?host=/var/run/postgresql/"
```

**드라이버 어댑터로 스키마 지정:**

```
    const adapter = new PrismaPg(
      { connectionString: process.env.DATABASE_URL },
      { schema: "mySchema" }
    );
```

**연결 풀 기본값(Prisma ORM v7):**

드라이버 어댑터는 v6와 다른 `pg` 기본값을 사용합니다:

- **연결 타임아웃:** `0`(타임아웃 없음), v6의 `5s`와 다름
- **유휴 타임아웃:** `10s`, v6의 `300s`와 다름

구성 방법은 [connection pool guide](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool#postgresql-using-the-pg-driver-adapter)를 참조하세요.
