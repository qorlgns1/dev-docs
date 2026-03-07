---
title: "네이티브 데이터베이스 타입"
description: "Prisma Migrate는 Prisma schema에 정의된 모델을 데이터베이스 기능으로 변환합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types

# 네이티브 데이터베이스 타입

네이티브 데이터베이스 타입

Prisma Migrate는 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에 정의된 모델을 데이터베이스 기능으로 변환합니다.

![왼쪽에 Prisma schema(레이블: Prisma schema, models), 오른쪽에 데이터베이스(레이블: Database, tables)가 있는 다이어그램입니다. 스키마와 데이터베이스를 연결하는 두 개의 평행 화살표가 `@unique`가 `UNIQUE`로, `@id`가 `PRIMARY KEY`로 매핑되는 방식을 보여줍니다.](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/migrate-mapping.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

[데이터 모델](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models)의 모든¹ 기능은 기본 데이터베이스의 해당 기능에 매핑됩니다. **Prisma schema에서 기능을 정의할 수 있다면, Prisma Migrate에서 지원됩니다.**

Prisma schema 기능의 전체 목록은 다음을 참고하세요.

- 데이터베이스 기능 목록과 Prisma schema에서 무엇으로 매핑되는지 보려면 [Database features matrix](https://docs.prisma.io/docs/orm/reference/database-features)를 참고하세요.
- 필드 타입, 속성, 함수를 포함한 모든 Prisma schema 기능 목록은 [Prisma schema reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference)를 참고하세요.

Prisma Migrate는 각 필드를 [특정 네이티브 타입](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types#mapping-fields-to-a-specific-native-type)으로 매핑하는 것도 지원하며, [Prisma schema에 대응 항목이 없는 기능을 데이터베이스에 포함](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-types#handling-unsupported-database-features)하는 방법도 있습니다.

주석과 Prisma ORM 레벨 함수(`uuid()` 및 `cuid()`)는 데이터베이스 기능으로 매핑되지 않습니다.

## 필드를 특정 네이티브 타입으로 매핑

각 Prisma ORM 타입은 기본 데이터베이스 타입에 매핑됩니다. 예를 들어 PostgreSQL 커넥터는 기본적으로 `String`을 `text`에 매핑합니다. [Native database type attributes](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)는 데이터베이스에 어떤 _구체적인_ 네이티브 타입을 생성할지 결정합니다.

일부 Prisma ORM 타입은 하나의 네이티브 타입에만 매핑됩니다.

다음 예시에서 `name` 및 `title` 필드는 `@db.VarChar(X)` 타입 속성을 가집니다.

schema.prisma

```
    datasource db {
      provider = "postgresql"
    }

    model User {
      id    Int    @id @default(autoincrement())
      name  String @db.VarChar(200)
      posts Post[]
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String  @db.VarChar(150)
      published Boolean @default(true)
      authorId  Int
      author    User    @relation(fields: [authorId], references: [id])
    }
```

Prisma Migrate는 마이그레이션을 생성할 때 지정된 타입을 사용합니다.

migration.sql

```
      -- CreateTable
    CREATE TABLE "User" (
        "id" SERIAL,
        "name" VARCHAR(200) NOT NULL,
        PRIMARY KEY ("id")
    );
      -- CreateTable
    CREATE TABLE "Post" (
        "id" SERIAL,
        "title" VARCHAR(150) NOT NULL,
        "published" BOOLEAN NOT NULL DEFAULT true,
        "authorId" INTEGER NOT NULL,
        PRIMARY KEY ("id")
    );

      -- AddForeignKey
    ALTER TABLE "Post" ADD FOREIGN KEY("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

- Prisma ORM 타입별 매핑

Prisma ORM 타입 기준으로 정리된 타입 매핑은 [Prisma schema reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types) 문서를 참고하세요.

- 데이터베이스 제공자별 매핑

데이터베이스 제공자 기준으로 정리된 타입 매핑은 다음을 참고하세요.

- PostgreSQL mappings
- MySQL mappings
- Microsoft SQL Server mappings
- SQLite mappings

## 지원되지 않는 데이터베이스 기능 처리

Prisma Migrate는 Prisma Schema Language(PSL)에 해당 표현이 없는 데이터베이스 기능을 자동으로 생성할 수 없습니다. 예를 들어 현재 PSL에서는 저장 프로시저나 트리거를 정의할 방법이 없습니다. 하지만 Prisma Migrate를 사용해 지원되지 않는 기능을 데이터베이스에 추가하는 방법은 있습니다.

- `circle` 같은 [지원되지 않는 필드 타입 처리](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#unsupported-field-types)
- 저장 프로시저 같은 [지원되지 않는 기능 처리](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#unsupported-database-features)
- 네이티브 데이터베이스 함수 사용 방법
