---
title: "지원되지 않는 데이터베이스 기능 (Prisma Schema)"
description: "Prisma Schema Language에 해당 문법이 없는 데이터베이스 기능을 지원하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features

# 지원되지 않는 데이터베이스 기능 (Prisma Schema)

Prisma Schema Language에 해당 문법이 없는 데이터베이스 기능을 지원하는 방법

Prisma ORM이 지원하는 데이터베이스의 모든 기능이 Prisma Schema Language에 대응되는 것은 아닙니다. 지원되는 기능의 전체 목록은 [database features matrix](https://docs.prisma.io/docs/orm/reference/database-features)를 참고하세요.

## 네이티브 데이터베이스 함수

Prisma Schema Language는 필드의 기본값을 설정할 때 사용할 수 있는 여러 [functions](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)를 지원합니다. 다음 예제에서는 Prisma ORM 수준의 `uuid()` 함수를 사용해 `id` 필드 값을 설정합니다:

```
    model Post {
      id String @id @default(uuid())
    }
```

하지만 관계형 데이터베이스에서는 [`dbgenerated(...)`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#dbgenerated)를 사용해 **네이티브 데이터베이스 함수**로 기본값을 정의할 수도 있습니다(MongoDB에는 데이터베이스 수준 함수 개념이 없습니다). 다음 예제에서는 PostgreSQL의 `gen_random_uuid()` 함수를 사용해 `id` 필드를 채웁니다:

```
    model User {
      id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
    }
```

- 데이터베이스 수준 함수를 사용해야 하는 경우

데이터베이스 수준 함수를 사용하는 이유는 두 가지입니다:

- Prisma ORM에 동등한 함수가 없는 경우(예: PostgreSQL의 `gen_random_bytes`).

- Prisma ORM 수준에서만 구현되어 데이터베이스에는 반영되지 않는 `uuid()` 및 `cuid()` 같은 함수에 의존할 수 없거나 의존하고 싶지 않은 경우.

다음 예제를 보세요. `id` 필드를 무작위로 생성된 `UUID`로 설정합니다:

```
model Post {
          id String @id @default(uuid())
        }
```

이 UUID는 `Post`를 생성할 때 Prisma Client를 사용하는 경우에만 생성됩니다. 일반 SQL로 작성된 대량 임포트 스크립트처럼 다른 방식으로 posts를 생성한다면, UUID를 직접 생성해야 합니다.

- 네이티브 데이터베이스 함수를 위해 PostgreSQL 확장 활성화

PostgreSQL에서는 일부 네이티브 데이터베이스 함수가 확장의 일부입니다. 예를 들어 PostgreSQL 12.13 이하 버전에서 `gen_random_uuid()` 함수는 [`pgcrypto`](https://www.postgresql.org/docs/10/pgcrypto.html) 확장에 포함됩니다.

PostgreSQL 확장을 사용하려면 먼저 데이터베이스 서버의 파일 시스템에 해당 확장을 설치해야 합니다.

그런 다음 [customized migration](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)을 통해 확장을 설치하여 활성화할 수 있습니다. 마이그레이션 파일에 다음 SQL을 추가하세요:

```
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

프로젝트에서 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용한다면, [마이그레이션의 일부로 확장을 설치](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions)해야 합니다. 섀도 데이터베이스에도 필요하므로 확장을 수동으로 설치하지 마세요.

확장을 사용할 수 없으면 Prisma Migrate는 다음 오류를 반환합니다:

```
    Migration `20210221102106_failed_migration` failed to apply cleanly to a temporary database.
    Database error: Error querying the database: db error: ERROR: type "pgcrypto" does not exist
```

## 지원되지 않는 필드 타입

`polygon` 또는 `geometry` 같은 일부 관계형 데이터베이스 타입은 Prisma Schema Language에 대응되는 타입이 없습니다. Prisma 스키마에서 해당 필드를 나타내려면 [`Unsupported`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported) 필드 타입을 사용하세요:

```
    model Star {
      id       Int                    @id @default(autoincrement())
      position Unsupported("circle")? @default(dbgenerated("'<(10,4),11>'::circle"))
    }
```

`prisma migrate dev`와 `prisma db push` 명령은 둘 다 데이터베이스에 `circle` 타입의 `position` 필드를 생성합니다. 하지만 생성된 Prisma Client에서는 해당 필드를 사용할 수 없습니다.

## 지원되지 않는 데이터베이스 기능

SQL 뷰 같은 일부 기능은 Prisma 스키마로 표현할 수 없습니다. 프로젝트에서 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용한다면, [지원되지 않는 기능을 마이그레이션의 일부로 포함](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features)해야 합니다.

부분 인덱스는 이제 `@@index`, `@@unique`, `@unique`의 `where` 인자를 통해 Prisma Schema Language에서 지원됩니다. 자세한 내용은 [Configuring partial indexes](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)를 참고하세요.
