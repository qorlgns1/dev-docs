---
title: "멀티 스키마"
description: "여러 데이터베이스 스키마와 함께 Prisma ORM을 사용하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema

# 멀티 스키마

여러 데이터베이스 스키마와 함께 Prisma ORM을 사용하는 방법

## 개요

PostgreSQL, CockroachDB, SQL Server에서는 데이터베이스 테이블을 이름이 있는 그룹으로 구성할 수 있습니다. 이러한 그룹을 _스키마_ 라고 하며, 테이블을 논리적으로 그룹화하기 위한 _네임스페이스_ 역할을 합니다(예: 이름 충돌 방지 또는 더 명확한 도메인 분리). 또한 스키마 간 외래 키 제약 조건을 정의할 수 있습니다. 모호함을 피하기 위해, 이 페이지에서는 이러한 네임스페이스를 _데이터베이스 스키마_ 라고 지칭합니다.

이 페이지에서는 다음을 설명합니다:

- Prisma 스키마에 여러 데이터베이스 스키마를 포함하는 방법
- Prisma Migrate로 스키마 변경 사항을 데이터베이스에 적용하는 방법
- 여러 데이터베이스 스키마가 있는 기존 데이터베이스를 introspect하는 방법
- Prisma Client로 여러 데이터베이스 스키마를 가로질러 쿼리하는 방법

멀티 스키마 기능은 PostgreSQL, CockroachDB, SQL Server에서만 지원됩니다. SQLite와 MySQL은 _네임스페이스로서의 스키마_ 개념이 동일하지 않기 때문에 사용할 수 없습니다.

## Prisma 스키마에 여러 데이터베이스 스키마를 포함하는 방법

Prisma 스키마 파일에서 여러 데이터베이스 스키마를 사용하려면 `datasource` 블록의 `schemas` 필드 배열에 데이터베이스 스키마 이름을 추가하세요. 다음 예시는 `"base"`와 `"shop"` 스키마를 추가합니다:

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
    }

    datasource db {
      provider = "postgresql"
      schemas  = ["base", "shop"]
    }
```

연결 문자열을 변경할 필요는 없습니다. 연결 문자열의 `schema` 값은 Prisma Client가 연결하고 raw query에 사용하는 기본 데이터베이스 스키마입니다. 그 외의 모든 Prisma Client 쿼리는 쿼리 대상 모델 또는 enum의 스키마를 사용합니다.

모델 또는 enum이 특정 데이터베이스 스키마에 속하도록 지정하려면, 데이터베이스 스키마 이름을 매개변수로 하는 `@@schema` 속성을 추가하세요. 다음 예시에서 `User` 모델은 `"base"` 스키마에 속하고, `Order` 모델과 `Size` enum은 `"shop"` 스키마에 속합니다:

schema.prisma

```
    model User {
      id     Int     @id
      orders Order[]

      @@schema("base")
    }

    model Order {
      id      Int  @id
      user    User @relation(fields: [userId], references: [id])
      userId  Int

      @@schema("shop")
    }

    enum Size {
      Small
      Medium
      Large

      @@schema("shop")
    }
```

- 서로 다른 데이터베이스 스키마에서 동일한 이름의 테이블

서로 다른 데이터베이스 스키마에 같은 이름의 테이블이 있다면, Prisma 스키마에서 테이블 이름을 고유한 모델 이름에 매핑해야 합니다. 이렇게 하면 Prisma Client에서 모델을 쿼리할 때 이름 충돌을 방지할 수 있습니다.

예를 들어 `base` 데이터베이스 스키마의 `Config` 테이블과 `users` 데이터베이스 스키마의 `Config` 테이블이 같은 이름을 가진 상황을 생각해 봅시다. 이름 충돌을 피하려면 Prisma 스키마의 모델에 고유한 이름(`BaseConfig`와 `UserConfig`)을 부여하고, `@@map` 속성을 사용해 각 모델을 해당 테이블 이름에 매핑하세요:

schema.prisma

```
    model BaseConfig {
      id Int @id

      @@map("Config")
      @@schema("base")
    }

    model UserConfig {
      id Int @id

      @@map("Config")
      @@schema("users")
    }
```

## Prisma Migrate로 스키마 변경 사항을 적용하는 방법

Prisma Migrate(또는 `prisma db push`)를 사용해 여러 데이터베이스 스키마가 있는 Prisma 스키마의 변경 사항을 적용할 수 있습니다.

예를 들어, 위의 `base` 스키마에 `Profile` 모델을 추가해 보겠습니다:

schema.prisma

```
    model User {
      id      Int      @id
      orders  Order[]
      profile Profile?

      @@schema("base")
    }

    model Profile {
      id     Int    @id @default(autoincrement())
      bio    String
      user   User   @relation(fields: [userId], references: [id])
      userId Int    @unique

      @@schema("base")
    }

    model Order {
      id      Int  @id
      user    User @relation(fields: [userId], references: [id])
      userId  Int

      @@schema("shop")
    }

    enum Size {
      Small
      Medium
      Large

      @@schema("shop")
    }
```

그런 다음 이 스키마 변경 사항을 데이터베이스에 적용할 수 있습니다. 예를 들어 `migrate dev`를 사용해 migration으로 스키마 변경 사항을 생성하고 적용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name add_profile
```

모델 또는 enum을 한 스키마에서 다른 스키마로 이동하면, Prisma ORM은 원본 스키마에서 해당 모델 또는 enum을 삭제하고 대상 스키마에 새로 생성한다는 점에 유의하세요.

## 여러 데이터베이스 스키마가 있는 기존 데이터베이스를 introspect하는 방법

`prisma db pull`을 사용하면, 단일 데이터베이스 스키마를 가진 데이터베이스를 introspect할 때와 동일한 방식으로 여러 데이터베이스 스키마를 가진 기존 데이터베이스를 introspect할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

이 작업은 Prisma 스키마를 데이터베이스의 현재 상태와 일치하도록 업데이트합니다.

서로 다른 데이터베이스 스키마에 같은 이름의 테이블이 있으면 Prisma ORM이 충돌을 알려주는 유효성 검사 오류를 표시합니다. 이를 해결하려면 [`@map` 속성으로 introspect된 모델의 이름을 변경하세요](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema#tables-with-the-same-name-in-different-database-schemas).

## Prisma Client로 여러 데이터베이스 스키마를 가로질러 쿼리하는 방법

Prisma Client 쿼리 문법을 변경하지 않고도 여러 데이터베이스 스키마의 모델을 쿼리할 수 있습니다. 예를 들어, 다음 쿼리는 위 Prisma 스키마를 사용해 특정 사용자의 모든 주문을 찾습니다:

```
    const orders = await prisma.order.findMany({
      where: {
        user: {
          id: 42,
        },
      },
    });
```

- 외부에서 관리되는 테이블

경우에 따라 다른 팀이나 서비스가 처리하는 테이블(예: Auth0 또는 Clerk 테이블)처럼 Prisma ORM이 특정 테이블을 관리하지 않기를 원할 수 있습니다. 이런 경우 [Prisma Config file](https://docs.prisma.io/docs/orm/reference/prisma-config-reference#tablesexternal-and-enumsexternal)의 `tables.external` 설정 옵션을 사용해 이를 **외부에서 관리되는 테이블**로 표시할 수 있습니다. [외부에서 관리되는 테이블](https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables)에 대해 더 알아보세요.
