---
title: "네이티브 데이터베이스 함수"
description: "Prisma Migrate를 사용하는 프로젝트에서 PostgreSQL 네이티브 데이터베이스 함수를 활성화하는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions

# 네이티브 데이터베이스 함수

Prisma Migrate를 사용하는 프로젝트에서 PostgreSQL 네이티브 데이터베이스 함수를 활성화하는 방법입니다.

PostgreSQL에서는 일부 [네이티브 데이터베이스 함수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#native-database-functions)가 선택적 익스텐션의 일부입니다. 예를 들어 PostgreSQL 12.13 이하 버전에서는 `gen_random_uuid()` 함수가 [`pgcrypto`](https://www.postgresql.org/docs/10/pgcrypto.html) 익스텐션에 포함되어 있습니다.

PostgreSQL 익스텐션을 사용하려면 데이터베이스 서버의 파일 시스템에 이를 설치한 다음 익스텐션을 활성화해야 합니다. Prisma Migrate를 사용하는 경우, 이 작업은 마이그레이션의 일부로 수행되어야 합니다.

Prisma Migrate를 사용하는 경우 마이그레이션 파일 외부에서 익스텐션을 활성화하지 마세요. [섀도 데이터베이스](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)에도 동일한 익스텐션이 필요합니다. Prisma Migrate는 섀도 데이터베이스를 자동으로 생성하고 삭제하므로, 익스텐션을 활성화하는 유일한 방법은 이를 마이그레이션 파일에 포함하는 것입니다.

Prisma ORM 4.5.0 이상 버전에서는 Prisma 스키마에서 [`postgresqlExtensions` preview feature](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions)를 선언해 익스텐션을 활성화할 수 있습니다.

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["postgresqlExtensions"]
    }

    datasource db {
      provider   = "postgresql"
      extensions = [pgcrypto]
    }
```

그런 다음 Prisma Migrate로 이 변경 사항을 데이터베이스에 적용할 수 있습니다. 자세한 내용은 [How to migrate PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions)를 참고하세요.

Prisma ORM 이전 버전에서는 대신 마이그레이션 파일에 SQL 명령을 추가해 익스텐션을 활성화해야 합니다. [How to install a PostgreSQL extension as part of a migration](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions#how-to-install-a-postgresql-extension-as-part-of-a-migration)을 참고하세요.

## 마이그레이션의 일부로 PostgreSQL 익스텐션 설치하기

이 섹션에서는 PostgreSQL 익스텐션을 활성화하기 위해 마이그레이션 파일에 SQL 명령을 추가하는 방법을 설명합니다. 대신 `postgresqlExtensions` preview feature를 사용해 Prisma Schema에서 PostgreSQL 익스텐션을 관리하는 경우 [How to migrate PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions)를 참고하세요.

다음 예시는 마이그레이션의 일부로 `pgcrypto` 익스텐션을 설치하는 방법을 보여줍니다.

- 스키마에 네이티브 데이터베이스 함수를 사용하는 필드를 추가합니다:

schema.prisma

```
    model User {
     id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
    }
```

캐스트 연산자(예: `::TEXT`)를 포함하는 경우 함수 전체를 괄호로 감싸야 합니다:

schema.prisma

```
    @default(dbgenerated("(gen_random_uuid()::TEXT)"))
```

- `--create-only` 플래그를 사용해 적용하지 않고 새 마이그레이션을 생성합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- 생성된 `migration.sql` 파일을 열고 `pgcrypto` 모듈을 활성화합니다:

migration.sql

```
    CREATE EXTENSION IF NOT EXISTS pgcrypto;

    ADD COLUMN "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    ADD PRIMARY KEY ("id");
```

- 마이그레이션을 적용합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

데이터베이스를 재설정하거나 팀에 새 구성원을 추가할 때마다 필요한 모든 함수가 마이그레이션 이력에 포함됩니다.
