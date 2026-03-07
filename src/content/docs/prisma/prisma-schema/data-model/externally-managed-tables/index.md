---
title: "외부 테이블"
description: "Prisma ORM에서 외부 관리 테이블을 선언하고 사용하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables

# 외부 테이블

Prisma ORM에서 외부 관리 테이블을 선언하고 사용하는 방법

## 개요

Prisma ORM의 _외부에서 관리되는 테이블_(_externally managed tables_, 줄여서 _external tables_)은 **Prisma Client를 통해 쿼리할 수 있지만**, **Prisma Migrate에서는 무시되는** 테이블입니다.

경우에 따라 Prisma ORM이 특정 테이블을 관리하지 않기를 원할 수 있습니다. 예를 들어, 다른 팀이나 서비스가 관리하는 테이블이 그렇습니다.

대표적인 사용 사례는 다음과 같습니다.

- 사용자 및 세션 데이터를 담은 특정 테이블을 관리하는 Clerk 또는 Auth0 같은 인증 서비스
- 버킷 및 객체 메타데이터 저장용 테이블을 사용하는 Supabase Storage 같은 스토리지 서비스
- 데이터베이스 내 특정 테이블을 각 팀이 소유하는 마이크로서비스 기반 조직

그 밖에도 조직의 제약이나 선호에 따라 Prisma ORM이 특정 테이블을 관리하지 않도록 하려는 다양한 시나리오가 있을 수 있습니다.

외부 관리 테이블은 현재 [Preview](https://docs.prisma.io/docs/orm/more/releases#preview) 상태입니다.

외부 관리 테이블은 [multi-schema](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema) 데이터베이스 구성과 함께 자주 사용됩니다. 하지만 이는 필수 조건이 아닙니다. 데이터베이스에 스키마가 하나만 있어도 그 안에서 외부 관리 테이블을 선언할 수 있습니다.

Prisma ORM은 데이터베이스 테이블 구조와 Prisma 모델 구조가 실제로 일치하는지 검증하지 않습니다. 한편으로는 Prisma 스키마를 업데이트할 때 개발자의 꼼꼼함이 필요합니다(가장 안전한 방법은 `prisma db pull` 사용). 다른 한편으로는 이런 유연성 덕분에 데이터베이스의 실제 테이블 중 일부만 표현할 수 있고(예: 모든 컬럼을 _전부_ 노출하지 않음) 필요한 범위만 모델링할 수 있습니다.

## 워크플로

외부 테이블을 사용하려면 주요 워크플로는 다음과 같습니다.

1. [Prisma Config file](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)에 외부 테이블 이름을 선언합니다.
2. Prisma 스키마를 업데이트합니다(예: `npx prisma db pull`).
3. `npx prisma generate`로 Prisma Client를 다시 생성합니다.
4. 이제 Prisma Client로 외부 테이블을 쿼리할 수 있지만 Prisma Migrate에서는 무시됩니다.
5. 테이블이 변경되면(해당 테이블 소유 주체에 의해):
   1. `npx prisma db pull`로 데이터베이스를 다시 인트로스펙션하거나 prisma 파일의 모델을 수동으로 업데이트합니다.
   2. `npx prisma generate`로 Prisma Client를 다시 생성합니다.

## Prisma Config 구문

[Prisma Config](https://docs.prisma.io/docs/orm/reference/prisma-config-reference) 파일의 `tables.external` 속성으로 외부 관리 테이블을 지정할 수 있습니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      // required when using unstable features
      experimental: {
        externalTables: true,
      },
      // declare the `users` table and `role` enum as external
      tables: {
        external: ["public.users"],
      },
      enums: {
        external: ["public.role"],
      },
    });
```

- 테이블과 마찬가지로 외부 관리 _enum_ 도 지정할 수 있습니다.
- PostgreSQL 및 SQL Server에서는 스키마 이름을 포함한 완전 수식 테이블/enum 이름을 지정해야 합니다. 예: `public.products` 또는 `auth.users`.
- MySQL 및 SQLite에서는 테이블 이름만 지정하면 됩니다.

## 관계

Prisma는 Prisma가 관리하는 테이블에서 외부 관리 테이블로의 관계를 생성하고 업데이트할 수 있습니다.

다만 이를 위해 Prisma는 마이그레이션 생성 시점에 외부 관리 테이블의 구조를 알고 있어야 합니다. 마이그레이션 생성 전에 Prisma가 [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)에서 실행할 SQL 스크립트를 제공하면, 외부 테이블과 enum을 에뮬레이션할 수 있습니다.

생성되는 플레이스홀더 테이블은 실제 테이블의 전체 구조를 가질 필요는 없지만 기본 키는 반드시 있어야 합니다.

외부 테이블이 어떤 관리 테이블에서도 참조되지 않는 경우, 즉 관리 테이블 중 어느 것도 외부 테이블에 대한 외래 키 제약을 포함하지 않는 경우에는 `migrations.initShadowDb`에 해당 테이블용 SQL을 제공할 필요가 없습니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
      // required when using unstable features
      experimental: {
        externalTables: true,
      },
      // declare a `users` table
      tables: {
        external: ["public.users"],
      },
      migrations: {
        path: "prisma/migrations",
        // setup the users table for the shadow database
        initShadowDb: ` // [!code ++]
          CREATE TABLE public.users (id SERIAL PRIMARY KEY); // [!code ++]
        `,
      },
    });
```

외부 테이블에서 관리 테이블로 향하는 관계(외부 테이블이 관리 테이블에 대한 외래 키 제약을 가지는 경우)는 외부 테이블을 수정하게 되므로 Prisma가 **관리하지 않습니다**.

## 예시

`posts` 테이블만 포함한 다음 Prisma 스키마가 있다고 가정해 보겠습니다.

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
      // ...
    }

    datasource db {
      provider = "postgresql"
      // ...
    }

    model posts {
      id          Int       @id @default(autoincrement())
      created_at  DateTime  @default(now())
      title       String
      content     String?
    }
```

`posts` 테이블은 이전 마이그레이션으로 이미 생성되어 있습니다. 이제 데이터베이스에 `users` 테이블과 `role` enum도 있으며, 이를 외부 관리 대상으로 취급하고자 합니다.

따라서 기본 `public` 스키마의 PostgreSQL 데이터베이스 테이블은 다음과 같습니다.

```
    -- Enum used by users table
    CREATE TYPE role AS ENUM ('customer', 'support', 'admin');

    -- Users table
    CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) NOT NULL UNIQUE,
      email VARCHAR(100) NOT NULL UNIQUE,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      role role
    );

    -- Posts table
    CREATE TABLE posts (
      id SERIAL PRIMARY KEY,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      title VARCHAR(200) NOT NULL,
      content TEXT
    );
```

- 1\. Prisma Config에서 외부 관리 테이블 선언

`tables.external` 속성으로 외부 관리 테이블 사용을 활성화합니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      // declare the `users` table and `role` enum as external
      tables: {
        external: ["public.users"],
      },
      enums: {
        external: ["public.role"],
      },
    });
```

- 2\. Prisma 스키마 업데이트

다음으로 Prisma 스키마를 업데이트해야 합니다. 방법은 다음 중 하나입니다.

- 모델을 수동으로 생성
- 또는 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 사용

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

이제 `users` 테이블이 Prisma 스키마에 포함됩니다.

```
    model posts {
      id         Int       @id @default(autoincrement())
      created_at DateTime? @default(now()) @db.Timestamp(6)
      title      String    @db.VarChar(200)
      content    String?
    }

    model users {
      id         Int       @id @default(autoincrement())
      username   String    @unique @db.VarChar(50)
      email      String    @unique @db.VarChar(100)
      created_at DateTime? @default(now()) @db.Timestamp(6)
      role       role
    }

    enum role {
      customer
      support
      admin
    }
```

- 3\. Prisma Client 다시 생성

`users` 테이블을 쿼리할 수 있으려면 Prisma Client를 다시 생성해야 합니다.

npm

pnpm

yarn

bun

```
    npx prisma generate
```

- 4\. Prisma Client로 `users` 테이블 쿼리

이제 Prisma Client로 외부 `users` 테이블을 쿼리할 수 있습니다.

```
    await prisma.users.findMany();
```

- 5\. 관계 추가

이제 `posts`에서 `users`로 작성자 관계를 추가하려고 한다고 가정해 보겠습니다.

먼저 Prisma 스키마를 업데이트합니다.

```
    model posts {
      id         Int       @id @default(autoincrement())
      created_at DateTime? @default(now()) @db.Timestamp(6)
      title      String    @db.VarChar(200)
      content    String?
      author     users @relation(fields: [author_id], references: [id])
      author_id  Int
    }

    model users {
      id         Int       @id @default(autoincrement())
      username   String    @unique @db.VarChar(50)
      email      String    @unique @db.VarChar(100)
      created_at DateTime? @default(now()) @db.Timestamp(6)
      role       role
      posts      posts[]
    }

    enum role {
      customer
      support
      admin
    }
```

그다음 마이그레이션 중 Prisma가 `users` 테이블을 인식하도록 `migrations.initShadowDb` 스크립트를 추가합니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      tables: {
        external: ["public.users"],
      },
      migrations: {
        path: "prisma/migrations",
        // setup the users table for the shadow database
        initShadowDb: ` // [!code ++]
          CREATE TABLE public.users (id SERIAL PRIMARY KEY); // [!code ++]
        `,
      },
    });
```

이제 `prisma migrate dev` 명령을 실행할 수 있습니다.
