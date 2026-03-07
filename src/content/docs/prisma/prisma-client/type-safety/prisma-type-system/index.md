---
title: "Prisma ORM의 타입 시스템 사용 방법"
description: "Prisma ORM의 타입 시스템 사용 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/type-safety/prisma-type-system

# Prisma ORM의 타입 시스템 사용 방법

Prisma ORM의 타입 시스템 사용 방법

이 가이드는 Prisma ORM의 타입 시스템을 소개하고, 데이터베이스의 기존 네이티브 타입을 introspect하는 방법과 Prisma Migrate 또는 `db push`로 데이터베이스에 스키마 변경을 적용할 때 타입을 사용하는 방법을 설명합니다.

## Prisma ORM의 타입 시스템은 어떻게 동작하나요?

Prisma ORM은 필드가 담을 수 있는 데이터의 종류를 정의하기 위해 *타입*을 사용합니다. 시작을 쉽게 할 수 있도록 Prisma ORM은 대부분의 기본 사용 사례를 커버하는 소수의 핵심 [스칼라 타입](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)을 제공합니다. 예를 들어, 다음 블로그 게시물 모델을 보겠습니다.

schema.prisma

```
    datasource db {
      provider = "postgresql"
    }

    model Post {
      id        Int      @id
      title     String
      createdAt DateTime
    }
```

`Post` 모델의 `title` 필드는 `String` 스칼라 타입을 사용하고, `createdAt` 필드는 `DateTime` 스칼라 타입을 사용합니다.

데이터베이스에도 자체 타입 시스템이 있으며, 이는 컬럼이 담을 수 있는 값의 타입을 정의합니다. 대부분의 데이터베이스는 컬럼이 정확히 무엇을 저장할 수 있는지 세밀하게 제어할 수 있도록 많은 데이터 타입을 제공합니다. 예를 들어, 데이터베이스는 여러 크기의 정수나 XML 데이터에 대한 내장 지원을 제공할 수 있습니다. 이러한 타입의 이름은 데이터베이스마다 다릅니다. 예를 들어 PostgreSQL에서는 boolean용 컬럼 타입이 `boolean`이지만, MySQL에서는 일반적으로 `tinyint(1)` 타입을 사용합니다.

위 블로그 게시물 예시에서는 PostgreSQL 커넥터를 사용합니다. 이는 Prisma 스키마의 `datasource` 블록에서 지정됩니다.

- 기본 타입 매핑

핵심 스칼라 타입으로 바로 시작할 수 있도록, Prisma ORM은 각 스칼라 타입을 기반 데이터베이스의 기본 타입에 매핑하는 *기본 타입 매핑*을 제공합니다. 예를 들면:

- 기본적으로 Prisma ORM의 `String` 타입은 PostgreSQL의 `text` 타입 및 MySQL의 `varchar` 타입에 매핑됩니다.
- 기본적으로 Prisma ORM의 `DateTime` 타입은 PostgreSQL의 `timestamp(3)` 타입 및 SQL Server의 `datetime2` 타입에 매핑됩니다.

특정 데이터베이스의 기본 타입 매핑은 Prisma ORM의 [데이터베이스 커넥터 페이지](https://docs.prisma.io/docs/orm/core-concepts/supported-databases)에서 확인할 수 있습니다. 예를 들어, [이 표](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#prisma-to-postgresql)는 PostgreSQL의 기본 타입 매핑을 보여줍니다.
특정 Prisma ORM 타입에 대해 모든 데이터베이스의 기본 타입 매핑을 보려면 Prisma 스키마 레퍼런스의 [모델 필드 스칼라 타입 섹션](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)을 참고하세요. 예를 들어, [이 표](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#float)는 `Float` 스칼라 타입의 기본 타입 매핑을 보여줍니다.

- 네이티브 타입 매핑

때로는 Prisma ORM 타입의 기본 타입 매핑에 포함되지 않은, 더 구체적인 데이터베이스 타입을 사용해야 할 수 있습니다. 이를 위해 Prisma ORM은 핵심 스칼라 타입을 세분화할 수 있는 [네이티브 타입 속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)을 제공합니다. 예를 들어, 위 `Post` 모델의 `createdAt` 필드에서 기본 타입 매핑인 `timestamp(3)` 대신 기반 PostgreSQL 데이터베이스의 날짜 전용 컬럼인 `date` 타입을 사용하고 싶을 수 있습니다. 이를 위해 `createdAt` 필드에 `@db.Date` 네이티브 타입 속성을 추가합니다.

schema.prisma

```
    model Post {
      id        Int      @id
      title     String
      createdAt DateTime @db.Date
    }
```

네이티브 타입 매핑을 사용하면 데이터베이스의 모든 타입을 표현할 수 있습니다. 하지만 Prisma ORM 기본값이 요구사항을 충족한다면 반드시 사용할 필요는 없습니다. 이렇게 하면 일반적인 사용 사례에서 Prisma 스키마를 더 짧고 읽기 쉽게 유지할 수 있습니다.

## 데이터베이스 타입 introspect 방법

기존 데이터베이스를 [introspect](https://docs.prisma.io/docs/orm/prisma-schema/introspection)하면 Prisma ORM은 각 테이블 컬럼의 데이터베이스 타입을 가져와, 해당 모델 필드에 맞는 Prisma ORM 타입으로 Prisma 스키마에 표현합니다. 데이터베이스 타입이 해당 Prisma ORM 스칼라 타입의 기본 데이터베이스 타입이 아닌 경우, Prisma ORM은 네이티브 타입 속성도 함께 추가합니다.

예시로 PostgreSQL 데이터베이스의 `User` 테이블을 보겠습니다. 다음과 같이 구성되어 있다고 가정합니다.

- 데이터 타입이 `serial`인 `id` 컬럼
- 데이터 타입이 `text`인 `name` 컬럼
- 데이터 타입이 `boolean`인 `isActive` 컬럼

다음 SQL 명령으로 이를 생성할 수 있습니다.

```
    CREATE TABLE "public"."User" (
      id serial PRIMARY KEY NOT NULL,
      name text NOT NULL,
      "isActive" boolean NOT NULL
    );
```

프로젝트 루트 디렉터리에서 다음 명령을 실행하여 데이터베이스를 introspect하세요.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

다음과 같은 Prisma 스키마를 얻게 됩니다.

schema.prisma

```
    model User {
      id       Int     @id @default(autoincrement())
      name     String
      isActive Boolean
    }
```

데이터베이스의 `id`, `name`, `isActive` 컬럼은 각각 `Int`, `String`, `Boolean` Prisma ORM 타입으로 매핑됩니다. 이 데이터베이스 타입들은 해당 Prisma ORM 타입의 _기본_ 데이터베이스 타입이므로, Prisma ORM은 네이티브 타입 속성을 추가하지 않습니다.

이제 다음 SQL 명령을 실행해 데이터 타입이 `date`인 `createdAt` 컬럼을 데이터베이스에 추가합니다.

```
    ALTER TABLE "public"."User"
    ADD COLUMN "createdAt" date NOT NULL;
```

데이터베이스를 다시 introspect합니다.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

이제 Prisma 스키마에는 Prisma ORM 타입이 `DateTime`인 새 `createdAt` 필드가 포함됩니다. 또한 PostgreSQL의 `date`는 `DateTime` 타입의 기본 타입이 아니므로, `createdAt` 필드에는 `@db.Date` 네이티브 타입 속성도 추가됩니다.

schema.prisma

```
    model User {
      id        Int      @id @default(autoincrement())
      name      String
      isActive  Boolean
      createdAt DateTime @db.Date
    }
```

## 데이터베이스에 스키마 변경을 적용할 때 타입을 사용하는 방법

Prisma Migrate 또는 `db push`를 사용해 데이터베이스에 스키마 변경을 적용할 때, Prisma ORM은 각 필드의 Prisma ORM 스칼라 타입과 해당 필드가 가진 네이티브 속성을 모두 사용해 데이터베이스의 대응 컬럼에 맞는 정확한 데이터베이스 타입을 결정합니다.

예시로 다음 `Post` 모델이 있는 Prisma 스키마를 만듭니다.

schema.prisma

```
    model Post {
      id        Int      @id
      title     String
      createdAt DateTime
      updatedAt DateTime @db.Date
    }
```

이 `Post` 모델은 다음을 가집니다.

- Prisma ORM 타입이 `Int`인 `id` 필드
- Prisma ORM 타입이 `String`인 `title` 필드
- Prisma ORM 타입이 `DateTime`인 `createdAt` 필드
- Prisma ORM 타입이 `DateTime`이고 `@db.Date` 네이티브 타입 속성이 있는 `updatedAt` 필드

이제 프로젝트 루트 디렉터리에서 다음 명령을 실행해, 비어 있는 PostgreSQL 데이터베이스에 이 변경 사항을 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma db push
```

데이터베이스에 새 `Post` 테이블이 생성되며, 다음과 같이 표시됩니다.

- 데이터베이스 타입이 `integer`인 `id` 컬럼
- 데이터베이스 타입이 `text`인 `title` 컬럼
- 데이터베이스 타입이 `timestamp(3)`인 `createdAt` 컬럼
- 데이터베이스 타입이 `date`인 `updatedAt` 컬럼

`@db.Date` 네이티브 타입 속성이 `updatedAt` 컬럼의 데이터베이스 타입을 기본값인 `timestamp(3)` 대신 `date`로 변경한다는 점에 주목하세요.

## Prisma ORM 타입 시스템 활용 더 알아보기

Prisma ORM 타입 시스템 사용에 대한 추가 레퍼런스 정보는 다음 리소스를 참고하세요.

- 각 데이터베이스 제공자의 [데이터베이스 커넥터](https://docs.prisma.io/docs/orm/core-concepts/supported-databases) 페이지에는 Prisma ORM 타입과 데이터베이스 타입 간 기본 타입 매핑 표, 그리고 각 데이터베이스 타입과 Prisma ORM의 대응 네이티브 타입 속성 표가 포함된 타입 매핑 섹션이 있습니다. 예를 들어 PostgreSQL의 타입 매핑 섹션은 [여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#prisma-to-postgresql)에서 확인할 수 있습니다.
- Prisma 스키마 레퍼런스의 [모델 필드 스칼라 타입](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types) 섹션에는 각 Prisma ORM 스칼라 타입별 하위 섹션이 있습니다. 여기에는 각 데이터베이스에서 해당 Prisma ORM 타입의 기본 매핑 표와, 각 데이터베이스의 대응 데이터베이스 타입 및 Prisma ORM 네이티브 타입 속성 표가 포함됩니다. 예를 들어 `String` Prisma ORM 타입 항목은 [여기](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#string)에서 볼 수 있습니다.
