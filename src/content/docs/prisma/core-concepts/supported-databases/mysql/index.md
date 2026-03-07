---
title: "MySQL"
description: "자체 호스팅 MySQL/MariaDB 및 서버리스 PlanetScale을 포함한 MySQL 데이터베이스와 함께 Prisma ORM을 사용하세요."
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql

# MySQL

자체 호스팅 MySQL/MariaDB 및 서버리스 PlanetScale을 포함한 MySQL 데이터베이스와 함께 Prisma ORM을 사용하세요.

Prisma ORM은 자체 호스팅 서버와 서버리스 PlanetScale을 포함해 MySQL 및 MariaDB 데이터베이스를 지원합니다.

## 설정

Prisma 스키마에서 MySQL provider를 구성합니다:

schema.prisma

```
    datasource db {
      provider = "mysql"
    }
```

**자체 호스팅 MySQL/MariaDB:**

prisma.config.ts

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"), // mysql://user:pass@host:3306/db
      },
    });
```

**PlanetScale:**

prisma.config.ts

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"), // Uses connection string from PlanetScale
      },
    });
```

## 드라이버 어댑터 사용

[driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 통해 JavaScript 데이터베이스 드라이버를 사용하세요:

**`mariadb` 드라이버 사용 시:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-mariadb
```

```
    import { PrismaMariaDb } from "@prisma/adapter-mariadb";
    import { PrismaClient } from "./generated/prisma";

    const adapter = new PrismaMariaDb({
      host: "localhost",
      port: 3306,
      connectionLimit: 5,
    });
    const prisma = new PrismaClient({ adapter });
```

**PlanetScale 서버리스:**

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-planetscale undici
```

```
    import { PrismaPlanetScale } from "@prisma/adapter-planetscale";
    import { PrismaClient } from "./generated/prisma";
    import { fetch as undiciFetch } from "undici"; // Only for Node.js <18

    const adapter = new PrismaPlanetScale({
      url: process.env.DATABASE_URL,
      fetch: undiciFetch,
    });
    const prisma = new PrismaClient({ adapter });
```

## 지원되는 변형

- 자체 호스팅 MySQL/MariaDB

표준 MySQL (5.6+) 또는 MariaDB (10.0+) 서버.

- 연결 URL: `mysql://user:pass@host:3306/database`
- Prisma Migrate 완전 지원
- 개발에는 `prisma migrate dev` 사용
- MySQL과 MariaDB 모두 동일한 `mysql` provider 사용

**연결 문자열 인수:**

| Argument          | Default                | Description        |
| ----------------- | ---------------------- | ------------------ |
| `connect_timeout` | `5`                    | 연결 대기 시간(초) |
| `sslcert`         |                        | 서버 인증서 경로   |
| `sslidentity`     |                        | PKCS12 인증서 경로 |
| `sslaccept`       | `accept_invalid_certs` | 인증서 검증 모드   |

- PlanetScale

Vitess 클러스터링 시스템 기반의 서버리스 MySQL 호환 데이터베이스.

- 연결 URL: 호스트를 `aws.connect.psdb.cloud`로 변경
- 수평 확장을 위해 Vitess 사용
- 데이터베이스 브랜치 워크플로(개발/프로덕션 브랜치)
- 논블로킹 스키마 변경

**주요 기능:**

- 여러 서버에 걸친 엔터프라이즈급 확장성
- 스키마 테스트용 데이터베이스 브랜치
- 논블로킹 스키마 배포
- 서버리스 최적화(연결 제한 회피)

**브랜치 워크플로:**

1. **개발 브랜치** \- 스키마 변경을 자유롭게 테스트
2. **프로덕션 브랜치** \- 보호됨, deploy request 필요
3. **Deploy requests** \- 개발 변경 사항을 프로덕션에 병합

**스키마 변경:**

`prisma migrate`가 아닌 `prisma db push`를 사용하세요:

npm

pnpm

yarn

bun

```
    npx prisma db push
```

PlanetScale은 브랜치 병합 시 자체적으로 스키마 diff를 생성합니다.

**참조 무결성 옵션:**

**옵션 1: 관계 에뮬레이션(default PlanetScale에 권장)**

Prisma Client에서 관계를 처리하려면 `relationMode = "prisma"`를 설정하세요:

schema.prisma

```
    datasource db {
      provider     = "mysql"
      relationMode = "prisma"
    }
```

외래 키에 대한 인덱스를 수동으로 추가하세요:

```
    model Post {
      id       Int       @id @default(autoincrement())
      title    String
      comments Comment[]
    }

    model Comment {
      id     Int    @id @default(autoincrement())
      postId Int
      post   Post   @relation(fields: [postId], references: [id])

      @@index([postId]) // Required when using relationMode = "prisma"
    }
```

**옵션 2: 외래 키 제약 활성화**

`relationMode = "prisma"` 없이 표준 관계를 사용하려면 PlanetScale 설정에서 [외래 키 제약](https://planetscale.com/docs/concepts/foreign-key-constraints)을 활성화하세요.

**리소스:** [PlanetScale docs](https://planetscale.com/docs) • [Prisma integration](https://planetscale.com/docs/prisma/automatic-prisma-migrations)

## 타입 매핑

- MySQL과 Prisma 스키마 간 타입 매핑

| Prisma     | MySQL/MariaDB    |
| ---------- | ---------------- |
| `String`   | `VARCHAR(191)`   |
| `Boolean`  | `TINYINT(1)`     |
| `Int`      | `INT`            |
| `BigInt`   | `BIGINT`         |
| `Float`    | `DOUBLE`         |
| `Decimal`  | `DECIMAL(65,30)` |
| `DateTime` | `DATETIME(3)`    |
| `Json`     | `JSON`           |
| `Bytes`    | `LONGBLOB`       |

전체 세부 사항은 [전체 타입 매핑 레퍼런스](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)를 참고하세요.

## 일반 패턴

**SSL 연결:**

```
    DATABASE_URL="mysql://user:pass@host:3306/db?sslcert=./cert.pem&sslaccept=strict"
```

**Unix 소켓 연결:**

```
    DATABASE_URL="mysql://user:pass@localhost/db?socket=/var/run/mysqld/mysqld.sock"
```

**PlanetScale 샤딩(Preview):**

스키마에서 샤드 키를 정의하세요:

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated/prisma"
      previewFeatures = ["shardKeys"]
    }

    model User {
      id     String @default(uuid())
      region String @shardKey
    }
```

**연결 문제 해결:**

PlanetScale 프로덕션 브랜치는 직접 DDL에 대해 읽기 전용입니다. P3022 오류가 발생하면 다음을 확인하세요:

- `prisma migrate` 대신 `prisma db push`를 사용 중인지
- 개발 브랜치에서 작업 중인지, 또는
- deploy request를 사용해 프로덕션을 업데이트하고 있는지
