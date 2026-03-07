---
title: "SQLite"
description: "로컬 SQLite, Turso (libSQL), Cloudflare D1을 포함한 SQLite 데이터베이스와 함께 Prisma ORM을 사용하세요"
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite

# SQLite

로컬 SQLite, Turso (libSQL), Cloudflare D1을 포함한 SQLite 데이터베이스와 함께 Prisma ORM을 사용하세요

Prisma ORM은 SQLite 및 SQLite 호환 데이터베이스를 지원합니다. 여기에는 로컬 SQLite 파일, Turso의 분산형 libSQL, Cloudflare의 서버리스 D1이 포함됩니다.

## 설정

Prisma 스키마에서 SQLite provider를 구성합니다:

schema.prisma

```
    datasource db {
      provider = "sqlite"
    }
```

`prisma.config.ts`에서 연결 URL을 설정합니다:

prisma.config.ts

```
    import { defineConfig } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: "file:./dev.db", // or libsql:// for Turso
      },
    });
```

## 드라이버 어댑터 사용

Prisma의 내장 드라이버 대신, [driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 통해 JavaScript 데이터베이스 드라이버를 사용할 수 있습니다:

**`better-sqlite3`를 사용하는 로컬 SQLite:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-better-sqlite3
```

```
    import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaBetterSqlite3({ url: "file:./prisma/dev.db" });
    const prisma = new PrismaClient({ adapter });
```

**`@prisma/adapter-libsql`를 사용하는 Turso:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-libsql
```

```
    import { PrismaLibSQL } from "@prisma/adapter-libsql";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaLibSQL({
      url: process.env.TURSO_DATABASE_URL,
      authToken: process.env.TURSO_AUTH_TOKEN,
    });
    const prisma = new PrismaClient({ adapter });
```

**`@prisma/adapter-d1`를 사용하는 Cloudflare D1:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-d1
```

```
    import { PrismaD1 } from "@prisma/adapter-d1";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaD1(env.DB); // D1 binding in Workers
    const prisma = new PrismaClient({ adapter });
```

## 지원되는 변형

- 로컬 SQLite

표준 SQLite 데이터베이스 파일(`.db`)입니다. 연결 URL 형식: `file:./path/to/database.db`

- 스키마 변경에는 `prisma migrate dev`를 사용합니다
- 파일 시스템 내 어디에나 데이터베이스 파일을 저장할 수 있습니다
- 개발 및 소규모 애플리케이션에 가장 적합합니다

* Turso (libSQL)

엣지에서 호스팅되는 분산형 SQLite 호환 데이터베이스입니다.

- 연결 URL 형식: `libsql://[hostname]`
- 인증 토큰이 필요합니다
- 더 빠른 로컬 읽기를 위해 임베디드 복제본을 지원합니다
- 마이그레이션에는 로컬 SQLite 파일 + Turso CLI를 사용합니다([Turso docs](https://docs.turso.tech/) 참고)

**주요 차이점:**

- HTTP를 통한 원격 액세스
- 복제 및 자동 백업
- `prisma migrate diff` \+ Turso CLI를 통한 스키마 변경

* Cloudflare D1

Cloudflare Workers용 서버리스 SQLite 데이터베이스입니다.

- 리전 간 자동 읽기 복제를 지원합니다
- Wrangler CLI + `prisma migrate diff`를 통한 스키마 변경
- 로컬(`.wrangler/state`) 및 원격 버전을 사용할 수 있습니다

**주요 차이점:**

- 현재 트랜잭션을 지원하지 않습니다
- Wrangler를 통한 마이그레이션: `wrangler d1 migrations apply`
- Cloudflare Workers로 배포

## 타입 매핑

| Prisma ORM | SQLite    |
| ---------- | --------- |
| `String`   | `TEXT`    |
| `Boolean`  | `BOOLEAN` |
| `Int`      | `INTEGER` |
| `BigInt`   | `INTEGER` |
| `Float`    | `REAL`    |
| `Decimal`  | `DECIMAL` |
| `DateTime` | `NUMERIC` |
| `Json`     | `JSONB`   |
| `Bytes`    | `BLOB`    |
| `Enum`     | `TEXT`    |

SQLite는 불리언 값을 `0`(false) 또는 `1`(true)로 저장합니다. 자세한 내용은 [SQLite type affinity](https://www.sqlite.org/datatype3.html#boolean)를 참고하세요.

## 일반적인 고려 사항

**드라이버 어댑터 사용 시 타임스탬프 형식:**

`DateTime` 값이 저장되는 방식을 구성합니다:

```
    const adapter = new PrismaBetterSqlite3(
      { url: "file:./dev.db" },
      { timestampFormat: "unixepoch-ms" } // For backward compatibility
    );
```

- **ISO 8601 (기본값)** : 새 프로젝트에 가장 적합
- **`unixepoch-ms`** : Prisma 네이티브 드라이버에서 마이그레이션할 때 필요

**Enum 유효성 검사:**

SQLite는 데이터베이스 수준에서 enum 값을 강제하지 않습니다. 유효하지 않은 값은 런타임에 Prisma Client 쿼리 실패를 유발합니다.

**정수 오버플로:**

Prisma ORM은 숫자가 정수 경계 내에 맞는지 검증합니다. 값이 한계를 초과하면 P2023 오류가 발생합니다.
