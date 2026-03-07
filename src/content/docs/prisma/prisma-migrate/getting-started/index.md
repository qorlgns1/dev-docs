---
title: "Prisma Migrate 시작하기"
description: "Prisma Migrate를 사용해 개발 환경에서 스키마를 마이그레이션하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/getting-started

# Prisma Migrate 시작하기

Prisma Migrate를 사용해 개발 환경에서 스키마를 마이그레이션하는 방법을 알아보세요.

## 새 프로젝트에 추가하기

Prisma Migrate를 시작하려면 먼저 `schema.prisma`에 몇 가지 모델을 추가하세요.

schema.prisma

```
    datasource db {
      provider = "postgresql"
    }

    model User {
      id    Int    @id @default(autoincrement())
      name  String
      posts Post[]
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      published Boolean @default(true)
      authorId  Int
      author    User    @relation(fields: [authorId], references: [id])
    }
```

스키마에서 [네이티브 타입 매핑 속성](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types)을 사용해 정확히 어떤 데이터베이스 타입을 생성할지 결정할 수 있습니다(예: `String`을 `varchar(100)` 또는 `text`로 매핑).

- 초기 마이그레이션 생성

`prisma migrate` 명령을 사용해 초기 마이그레이션을 생성하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name init
```

이렇게 하면 데이터베이스에 맞는 적절한 명령이 포함된 마이그레이션이 생성됩니다.

migration.sql

```
    CREATE TABLE "User" (
      "id" SERIAL,
      "name" TEXT NOT NULL,
      PRIMARY KEY ("id")
    );
    -- CreateTable
    CREATE TABLE "Post" (
      "id" SERIAL,
      "title" TEXT NOT NULL,
      "published" BOOLEAN NOT NULL DEFAULT true,
      "authorId" INTEGER NOT NULL,
      PRIMARY KEY ("id")
    );
    -- AddForeignKey
    ALTER TABLE
      "Post"
    ADD
      FOREIGN KEY("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

이제 Prisma 스키마가 데이터베이스 스키마와 동기화되었고, 마이그레이션 히스토리가 초기화되었습니다.

```
    migrations/
      └─ 20210313140442_init/
        └─ migration.sql
```

> **참고**: 폴더 이름은 사용자마다 다릅니다. 폴더 이름 형식은 YYYYMMDDHHMMSS_your_text_from_name_flag 입니다.

- 추가 마이그레이션

이제 모델에 필드를 추가했다고 가정해 보겠습니다.

schema.prisma

```
    model User {
      id       Int    @id @default(autoincrement())
      jobTitle String
      name     String
      posts    Post[]
    }
```

마이그레이션을 업데이트하려면 `prisma migrate`를 다시 실행할 수 있습니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name added_job_title
```

migration.sql

```
      -- AlterTable
    ALTER TABLE
      "User"
    ADD
      COLUMN "jobTitle" TEXT NOT NULL;
```

Prisma 스키마는 다시 데이터베이스 스키마와 동기화되며, 마이그레이션 히스토리에는 두 개의 마이그레이션이 포함됩니다.

```
    migrations/
      └─ 20210313140442_init/
        └─ migration.sql
      └─ 20210313140442_added_job_title/
        └─ migration.sql
```

- 버전 관리에 커밋하기

마이그레이션 히스토리는 [버전 관리에 커밋](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories#committing-the-migration-history-to-source-control)할 수 있으며, 이를 사용해 [테스트 환경과 프로덕션에 변경 사항을 배포](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production#production-and-testing-environments)할 수 있습니다.

## 기존 프로젝트에 추가하기

기존 프로젝트에 Prisma 마이그레이션을 통합할 수 있습니다.

- Prisma 스키마를 생성하거나 업데이트하기 위해 인트로스펙션 실행

Prisma 스키마가 데이터베이스 스키마와 동기화되어 있는지 확인하세요. 이전 버전의 Prisma Migrate를 사용 중이라면 이미 동기화되어 있어야 합니다.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

- 베이스라인 마이그레이션 생성

Prisma migrate를 사용하기 전에 데이터베이스의 초기 히스토리를 만드는 베이스라인 마이그레이션을 생성하세요. 이 마이그레이션에는 반드시 유지되어야 하는 데이터가 포함되므로 데이터베이스를 재설정할 수 없습니다. 이를 통해 Prisma migrate는 하나 이상의 마이그레이션이 **이미 적용되었다고** 가정합니다. 이렇게 하면 이미 존재하는 테이블과 필드를 생성하려고 할 때 생성된 마이그레이션이 실패하는 것을 방지할 수 있습니다.

베이스라인 마이그레이션을 생성하려면:

- 이미 `prisma/migrations` 폴더가 있다면 해당 폴더를 삭제, 이동, 이름 변경 또는 보관하세요.
- 새 `prisma/migrations` 디렉터리를 생성하세요.
- 그런 다음 원하는 이름으로 새 디렉터리를 하나 더 생성하세요. 중요한 점은 Prisma migrate가 [사전식 순서](https://en.wikipedia.org/wiki/Lexicographic_order)로 마이그레이션을 적용하도록 `0_` 접두사를 사용하는 것입니다. 현재 타임스탬프와 같은 다른 값을 사용할 수도 있습니다.
- `prisma migrate diff`를 사용해 마이그레이션을 생성하고 파일로 저장하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate diff \
      --from-empty \
      --to-schema prisma/schema.prisma \
      --script > prisma/migrations/0_init/migration.sql
```

- 생성된 마이그레이션을 검토하세요.

* Prisma Schema Language에서 지원되지 않는 기능 우회하기

데이터베이스에 이미 존재하는 [지원되지 않는 데이터베이스 기능](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features)을 포함하려면, 초기 마이그레이션 SQL을 교체하거나 수정해야 합니다.

- [베이스라인 마이그레이션 생성](https://docs.prisma.io/docs/orm/prisma-migrate/getting-started#create-a-baseline-migration) 섹션에서 생성한 `migration.sql` 파일을 여세요.

- 생성된 SQL을 수정하세요. 예를 들어:
  - 변경 사항이 작다면 생성된 마이그레이션에 추가 커스텀 SQL을 덧붙일 수 있습니다. 다음 예시는 트리거 함수를 생성합니다.

migration.sql

```
    /* Generated migration SQL */

    CREATE OR REPLACE FUNCTION notify_on_insert()
    RETURNS TRIGGER AS $$
    BEGIN
      PERFORM pg_notify('new_record', NEW.id::text);
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
```

- 변경 사항이 크다면 데이터베이스 덤프 결과로 전체 마이그레이션 파일을 교체하는 것이 더 쉬울 수 있습니다.
  - `mysqldump`
  - [`pg_dump`](https://www.postgresql.org/docs/12/app-pgdump.html).

이를 위해 `pg_dump`를 사용할 때는 다음 명령으로 `search_path`를 업데이트해야 합니다: `SELECT pg_catalog.set_config('search_path', '', false);` 그렇지 않으면 다음 오류가 발생합니다: `The underlying table for model '_prisma_migrations' does not exist.`

모든 테이블을 한 번에 생성할 때는 외래 키도 같은 단계에서 생성되므로 테이블 순서가 중요합니다. 따라서 테이블 순서를 재정렬하거나, 모든 테이블 생성 후 마지막 단계로 제약 조건 생성을 옮겨 `can't create constraint` 오류를 피해야 합니다.

- 초기 마이그레이션 적용

초기 마이그레이션을 적용하려면:

- 데이터베이스를 대상으로 다음 명령을 실행하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --applied 0_init
```

- 마이그레이션이 원하는 최종 상태로 이어지는지 확인하기 위해 데이터베이스 스키마를 검토하세요(예: 스키마를 프로덕션 데이터베이스와 비교).

이제 새 마이그레이션 히스토리와 데이터베이스 스키마가 Prisma 스키마와 동기화되어야 합니다.

- 마이그레이션 히스토리와 Prisma 스키마 커밋

다음을 소스 컨트롤에 커밋하세요.

- 전체 마이그레이션 히스토리 폴더
- `schema.prisma` 파일

## 더 알아보기

- 프로덕션에 마이그레이션을 배포하는 방법에 대한 자세한 내용은 [Prisma Migrate로 데이터베이스 변경 배포하기](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate) 가이드를 참고하세요.
- `prisma migrate diff`, `prisma db execute`, `prisma migrate resolve`를 사용해 프로덕션에서 실패한 마이그레이션을 디버깅하고 해결하는 방법은 [프로덕션 문제 해결](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing#fixing-failed-migrations-with-migrate-diff-and-db-execute) 가이드를 참고하세요.
