---
title: "인스트로스펙션과 마이그레이션"
description: "Prisma로 데이터 모델을 구축하기 위한 개념을 알아보세요: 모델, 스칼라 타입, enum, 속성, 함수, ID, 기본값 등"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/models

# 모델

Prisma로 데이터 모델을 구축하기 위한 개념을 알아보세요: 모델, 스칼라 타입, enum, 속성, 함수, ID, 기본값 등

[Prisma 스키마](https://docs.prisma.io/docs/orm/prisma-schema/overview)의 데이터 모델 정의 부분은 애플리케이션 모델(또는 **Prisma 모델**)을 정의합니다. 모델은 다음과 같습니다:

- 애플리케이션 도메인의 **엔티티**를 나타냅니다.
- 데이터베이스의 **테이블**(PostgreSQL 같은 관계형 데이터베이스) 또는 **컬렉션**(MongoDB)에 매핑됩니다.
- 생성된 [Prisma Client API](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction)에서 사용 가능한 **쿼리**의 기반을 형성합니다.
- TypeScript와 함께 사용하면 Prisma Client는 모델과 해당 모델의 [변형](https://docs.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types)에 대한 생성된 **타입 정의**를 제공하여 데이터베이스 접근을 완전히 타입 안전하게 만듭니다.

다음 스키마는 블로깅 플랫폼을 설명하며, 데이터 모델 정의가 강조되어 있습니다:

관계형 데이터베이스

MongoDB

```
    datasource db {
      provider = "postgresql"
    }

    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    model User {
      id      Int      @id @default(autoincrement())
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }

    model Profile {
      id     Int    @id @default(autoincrement())
      bio    String
      user   User   @relation(fields: [userId], references: [id])
      userId Int    @unique
    }

    model Post {
      id         Int        @id @default(autoincrement())
      createdAt  DateTime   @default(now())
      updatedAt  DateTime   @updatedAt
      title      String
      published  Boolean    @default(false)
      author     User       @relation(fields: [authorId], references: [id])
      authorId   Int
      categories Category[]
    }

    model Category {
      id    Int    @id @default(autoincrement())
      name  String
      posts Post[]
    }

    enum Role {
      USER
      ADMIN
    }
```

데이터 모델 정의는 다음으로 구성됩니다:

- 여러 필드(모델 간 [관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#relation-fields) 포함)를 정의하는 [모델](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-models)([`model`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model) 프리미티브)
- [enum](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-enums)([`enum`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#enum) 프리미티브) (커넥터가 enum을 지원하는 경우)
- 필드와 모델의 동작을 변경하는 [속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-attributes)과 [함수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#using-functions)

해당 데이터베이스는 다음과 같습니다:

![샘플 데이터베이스](https://docs.prisma.io/docs/img/orm/sample-database.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

모델은 데이터 소스의 기본 구조에 매핑됩니다.

- PostgreSQL, MySQL 같은 관계형 데이터베이스에서는 `model`이 **테이블**에 매핑됩니다.
- MongoDB에서는 `model`이 **컬렉션**에 매핑됩니다.

> **참고** : 향후에는 비관계형 데이터베이스 및 기타 데이터 소스를 위한 커넥터가 추가될 수 있습니다. 예를 들어 REST API의 경우 *리소스*에 매핑됩니다.

다음 쿼리는 중첩된 `Post` 및 `Category` 레코드와 함께 `User`를 생성합니다:

```
    const user = await prisma.user.create({
      data: {
        email: "ariadne@prisma.io",
        name: "Ariadne",
        posts: {
          create: [
            {
              title: "My first day at Prisma",
              categories: { create: { name: "Office" } },
            },
            {
              title: "How to connect to a SQLite database",
              categories: { create: [{ name: "Databases" }, { name: "Tutorials" }] },
            },
          ],
        },
      },
    });
```

데이터 모델은 _여러분의_ 애플리케이션 도메인을 반영합니다. 예를 들면:

- **이커머스** 애플리케이션에서는 `Customer`, `Order`, `Item`, `Invoice` 같은 모델이 있을 가능성이 높습니다.
- **소셜 미디어** 애플리케이션에서는 `User`, `Post`, `Photo`, `Message` 같은 모델이 있을 가능성이 높습니다.

## 인스트로스펙션과 마이그레이션

데이터 모델을 정의하는 방법은 두 가지입니다:

- **데이터 모델을 수동으로 작성하고 Prisma Migrate 사용** : 데이터 모델을 수동으로 작성하고 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용해 데이터베이스에 매핑할 수 있습니다. 이 경우 데이터 모델이 애플리케이션 모델의 단일 진실 공급원(single source of truth)입니다.
- **인스트로스펙션으로 데이터 모델 생성** : 기존 데이터베이스가 있거나 SQL로 데이터베이스 스키마를 마이그레이션하는 방식을 선호한다면, 데이터베이스를 [인스트로스펙션](https://docs.prisma.io/docs/orm/prisma-schema/introspection)하여 데이터 모델을 생성합니다. 이 경우 데이터베이스 스키마가 애플리케이션 모델의 단일 진실 공급원입니다.

## 모델 정의

모델은 애플리케이션 도메인의 엔티티를 나타냅니다. 모델은 [`model`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model) 블록으로 표현되며 여러 [필드](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields)를 정의합니다. 위 예시 데이터 모델에서 `User`, `Profile`, `Post`, `Category`는 모델입니다.

블로깅 플랫폼은 다음 모델로 확장할 수 있습니다:

```
    model Comment {
      // Fields
    }

    model Tag {
      // Fields
    }
```

- 모델 이름을 테이블 또는 컬렉션에 매핑하기

Prisma 모델 [명명 규칙(단수형, PascalCase)](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#naming-conventions)은 데이터베이스의 테이블 이름과 항상 일치하지는 않습니다. 데이터베이스에서 테이블/컬렉션 이름을 지정할 때 흔히 복수형과 [snake_case](https://en.wikipedia.org/wiki/Snake_case) 표기법을 사용합니다. 예: `comments`. `comments`라는 테이블이 있는 데이터베이스를 인스트로스펙션하면 결과 Prisma 모델은 다음과 같습니다:

```
    model comments {
      // Fields
    }
```

하지만 [`@@map`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성을 사용하면 데이터베이스의 기본 `comments` 테이블 이름을 바꾸지 않고도 명명 규칙을 유지할 수 있습니다:

```
    model Comment {
      // Fields

      @@map("comments")
    }
```

이 모델 정의를 사용하면 Prisma ORM이 `Comment` 모델을 기본 데이터베이스의 `comments` 테이블에 자동으로 매핑합니다.

> **참고** : 컬럼 이름이나 enum 값에는 [`@map`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#map)을, enum 이름에는 `@@map`을 사용할 수도 있습니다.

`@map`과 `@@map`을 사용하면 기본 데이터베이스의 테이블/컬럼 이름과 모델/필드 이름을 분리하여 [Prisma Client API의 형태를 조정](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names#using-map-and-map-to-rename-fields-and-models-in-the-prisma-client-api)할 수 있습니다.

## 필드 정의

모델의 속성은 *필드*라고 하며, 다음으로 구성됩니다:

- **[필드 이름](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields)**
- **[필드 타입](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields)**
- 선택적 **[타입 수정자](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#type-modifiers)**
- [네이티브 데이터베이스 타입 속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)을 포함한 선택적 **[속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-attributes)**

필드의 타입은 해당 필드의 *구조*를 결정하며, 다음 두 범주 중 하나에 속합니다:

- 컬럼(관계형 데이터베이스) 또는 문서 필드(MongoDB)에 매핑되는 [스칼라 타입](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields)([enum](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-enums) 포함) - 예: [`String`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#string), [`Int`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#int)
- 모델 타입(이 경우 필드를 [관계 필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)라고 함) - 예: `Post`, `Comment[]`

* 스칼라 필드

다음 예시는 `Comment`와 `Tag` 모델을 여러 스칼라 타입으로 확장합니다. 일부 필드에는 [속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-attributes)이 포함되어 있습니다:

관계형 데이터베이스

MongoDB

```
    model Comment {
      id      Int    @id @default(autoincrement())
      title   String
      content String
    }

    model Tag {
      name String @id
    }
```

[스칼라 필드 타입 전체 목록](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)을 확인하세요.

- 관계 필드

관계 필드의 타입은 다른 모델입니다. 예를 들어 게시물(`Post`)은 여러 댓글(`Comment[]`)을 가질 수 있습니다:

관계형 데이터베이스

MongoDB

```
    model Post {
      id       Int       @id @default(autoincrement())
      // Other fields
      comments Comment[] // A post can have many comments
    }

    model Comment {
      id     Int
      // Other fields
      post   Post @relation(fields: [postId], references: [id]) // A comment can have one post
      postId Int
    }
```

모델 간 관계에 대한 더 많은 예시와 정보는 [relations 문서](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)를 참고하세요.

- 네이티브 타입 매핑

**네이티브 데이터베이스 타입 속성**은 기본 데이터베이스 타입을 설명합니다:

```
    model Post {
      id      Int    @id
      title   String @db.VarChar(200)
      content String
    }
```

타입 속성은 다음과 같습니다:

- 기본 provider에 따라 다릅니다(예: PostgreSQL은 `@db.Boolean`, MySQL은 `@db.TinyInt(1)` 사용).
- PascalCase로 작성되며 `@db` 접두사가 붙습니다.
- 네이티브 타입이 기본값과 다를 때만 [인스트로스펙션](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 중에 추가됩니다.

전체 목록은 [네이티브 데이터베이스 타입 속성](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)을 확인하세요.

- 타입 수정자

필드 타입은 두 가지 수정자 중 하나를 뒤에 붙여 변경할 수 있습니다:

- [`[]`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier) 필드를 리스트로 만듭니다.
- [`?`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier-1) 필드를 선택적으로 만듭니다.

> **참고** : 타입 수정자를 **결합할 수 없습니다**. 선택적 리스트는 지원되지 않습니다.

#

- 리스트

다음 예시는 스칼라 리스트와 관련 모델 리스트를 포함합니다:

```
    model Post {
      id       Int       @id @default(autoincrement())
      comments Comment[] // A list of comments
      keywords String[]  // A scalar list
    }
```

스칼라 리스트는 데이터베이스 커넥터가 이를 네이티브로 지원하거나 Prisma ORM 수준에서 지원하는 경우에만 사용할 수 있습니다.

#

- 선택 필드와 필수 필드

```
    model Comment {
      id      Int     @id @default(autoincrement())
      title   String       // Required field
      content String?      // Optional field (nullable)
    }
```

`?`가 없는 필드는 필수입니다:

- **관계형 데이터베이스** : `NOT NULL` 제약으로 표현됩니다.
- **Prisma Client** : TypeScript 타입이 컴파일 시점에 이러한 필드를 강제합니다.

* 지원되지 않는 타입

관계형 데이터베이스를 인스트로스펙션하면 지원되지 않는 데이터 타입은 [`Unsupported`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported)로 추가됩니다:

```
    location    Unsupported("POLYGON")?
```

`Unsupported` 타입 필드는 생성된 Prisma Client API에는 나타나지 않지만, [raw database access](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries)를 사용해 여전히 조회할 수 있습니다.

MongoDB 커넥터는 모든 스칼라 타입을 지원하므로 `Unsupported` 타입을 지원하지 않습니다.

## 속성 정의

속성은 필드 또는 모델 블록의 동작을 수정합니다. 다음 예시는 세 가지 필드 속성([`@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#id), [`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default), [`@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unique))과 하나의 블록 속성([`@@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference))을 포함합니다:

관계형 데이터베이스

MongoDB

```
    model User {
      id        Int     @id @default(autoincrement())
      firstName String
      lastName  String
      email     String  @unique
      isAdmin   Boolean @default(false)

      @@unique([firstName, lastName])
    }
```

일부 속성은 [인수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-argument-types)를 받습니다. 예를 들어 `@default`는 `true` 또는 `false`를 받습니다:

```
    isAdmin   Boolean @default(false) // short form of @default(value: false)
```

[필드 및 블록 속성 전체 목록](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attributes)을 확인하세요.

- ID 필드 정의

ID는 모델의 개별 레코드를 고유하게 식별합니다. 모델은 ID를 _하나만_ 가질 수 있습니다:

- **관계형 데이터베이스**에서는 ID가 단일 필드일 수도 있고 여러 필드를 기반으로 할 수도 있습니다. 모델에 `@id` 또는 `@@id`가 없다면, 대신 필수 `@unique` 필드 또는 `@@unique` 블록을 정의해야 합니다.
  - **MongoDB**에서는 ID가 `@id` 속성과 `@map("_id")` 속성을 정의하는 단일 필드여야 합니다.

#

- 관계형 데이터베이스에서 ID 정의하기

관계형 데이터베이스에서는 [`@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#id) 속성을 사용해 단일 필드로 ID를 정의하거나, [`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성을 사용해 여러 필드로 정의할 수 있습니다.

#

- 단일 필드 ID

다음 예시에서 `User` ID는 `id` 정수 필드로 표현됩니다:

```
    model User {
      id      Int      @id @default(autoincrement())
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

#

- 복합 ID

다음 예시에서 `User` ID는 `firstName` 및 `lastName` 필드의 조합으로 표현됩니다:

```
    model User {
      firstName String
      lastName  String
      email     String  @unique
      isAdmin   Boolean @default(false)

      @@id([firstName, lastName])
    }
```

기본적으로 Prisma Client 쿼리에서 이 필드의 이름은 `firstName_lastName`이 됩니다.

[`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성의 `name` 필드를 사용해 복합 ID에 사용자 지정 이름을 지정할 수도 있습니다:

```
    model User {
      firstName String
      lastName  String
      email     String  @unique
      isAdmin   Boolean @default(false)

      @@id(name: "fullName", fields: [firstName, lastName])
    }
```

이제 `firstName_lastName` 필드의 이름은 대신 `fullName`이 됩니다.

Prisma Client에서 복합 ID를 다루는 방법은 [복합 ID로 작업하기](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints) 문서를 참고하세요.

#

- 고유 식별자로서의 `@unique` 필드

다음 예시에서 사용자는 `@unique` 필드로 고유하게 식별됩니다. `email` 필드가 모델의 고유 식별자 역할을 하므로(필수), 반드시 필수 필드여야 합니다:

```
    model User {
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

**관계형 데이터베이스의 제약 조건 이름**
기본 데이터베이스에서 [사용자 지정 기본 키 제약 조건 이름](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names)을 선택적으로 정의할 수 있습니다.

#

- MongoDB에서 ID 정의하기

MongoDB 커넥터에는 관계형 데이터베이스와 다른 [ID 필드 정의를 위한 특정 규칙](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#mongodb)이 있습니다. ID는 [`@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#id) 속성을 사용한 단일 필드로 정의해야 하며, `@map("_id")`를 포함해야 합니다.

다음 예시에서 `User` ID는 자동 생성된 `ObjectId`를 허용하는 `id` 문자열 필드로 표현됩니다:

```
    model User {
      id      String   @id @default(auto()) @map("_id") @db.ObjectId
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

다음 예시에서 `User` ID는 `ObjectId`가 아닌 값(예: 고유 사용자 이름)을 허용하는 `id` 문자열 필드로 표현됩니다:

```
    model User {
      id      String   @id @map("_id")
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

**MongoDB는 `@@id`를 지원하지 않습니다**
MongoDB는 복합 ID를 지원하지 않으므로 `@@id` 블록으로 모델을 식별할 수 없습니다.

- 기본값 정의하기

[`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default) 속성을 사용하여 스칼라 필드의 기본값을 정의할 수 있습니다:

```
    model Post {
      id         Int        @id @default(autoincrement())
      createdAt  DateTime   @default(now())
      title      String
      published  Boolean    @default(false)
      data       Json       @default("{ \"hello\": \"world\" }")
    }
```

기본값은 다음과 같을 수 있습니다:

- **정적 값**: `5` (`Int`), `"Hello"` (`String`), `false` (`Boolean`)
- **리스트**: `[5, 6, 8]` (`Int[]`), `["Hello", "Goodbye"]` (`String[]`)
- **함수**: [`now()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#now), [`uuid()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#uuid), [`cuid()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#cuid)
- **JSON**: 이스케이프된 문자열 사용, 예: `@default("{ \"hello\": \"world\" }")`

커넥터 지원 세부 정보는 [속성 함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)를 참고하세요.

- 고유 필드 정의하기

고유 속성은 [`@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unique)를 사용해 단일 필드에 정의하거나, [`@@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference)를 사용해 여러 필드에 정의할 수 있습니다:

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique      // Single field unique
      name  String?
    }

    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      authorId Int

      @@unique([authorId, title]) // Composite unique
    }
```

`name` 필드로 제약 조건 이름을 사용자 지정할 수 있습니다: `@@unique(name: "authorTitle", [authorId, title])`

Prisma Client 사용법은 [복합 고유 식별자로 작업하기](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints)를 참고하세요.

#

- 복합 타입 고유 제약 조건 (MongoDB)

MongoDB 복합 타입의 경우 중첩 필드에 고유 제약 조건을 정의할 수 있습니다:

```
    type Address {
      street String
      number Int
    }

    model User {
      id      Int     @id
      email   String
      address Address

      @@unique([email, address.number])
    }
```

- 인덱스 정의하기

[`@@index`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#index)로 인덱스를 정의합니다:

```
    model Post {
      id      Int     @id @default(autoincrement())
      title   String
      content String?

      @@index([title, content])
    }
```

MongoDB 복합 타입에서는 점 표기법을 사용합니다: `@@index([address.city.name])`

이름 사용자 지정은 [사용자 지정 인덱스 이름](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names)을 참고하세요.

## enum 정의하기

Enums는 [데이터베이스에서 지원되는 경우](https://docs.prisma.io/docs/orm/reference/database-features#misc) [`enum`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#enum) 블록으로 정의됩니다:

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
      role  Role    @default(USER)
    }

    enum Role {
      USER
      ADMIN
    }
```

## 복합 타입 정의하기 (MongoDB)

복합 타입은 MongoDB에서만 사용할 수 있습니다.

복합 타입(임베디드 문서)을 사용하면 다른 레코드 내부에 레코드를 임베드할 수 있습니다:

```
    model Product {
      id     String  @id @default(auto()) @map("_id") @db.ObjectId
      name   String
      photos Photo[]
    }

    type Photo {
      height Int
      width  Int
      url    String
    }
```

**복합 타입에서 지원되는 속성:** `@default`, `@map`, 네이티브 타입 (`@db.ObjectId`)

**지원되지 않음:** `@unique`, `@id`, `@relation`, `@ignore`, `@updatedAt`

## 함수 사용하기

Prisma 스키마는 기본값을 위해 [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)를 지원합니다:

```
    model Post {
      id        Int      @id @default(autoincrement())
      createdAt DateTime @default(now())
      uuid      String   @default(uuid())
    }
```

자주 사용되는 함수: `now()`, `uuid()`, `cuid()`, `autoincrement()`, `auto()` (MongoDB ObjectId)

## 관계

관계 세부 사항은 [관계 문서](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)를 참고하세요.

## Prisma Client의 모델

- 쿼리 (CRUD)

모든 모델은 [Prisma Client API](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction)에서 CRUD 쿼리를 생성합니다:

`findMany()` | `findFirst()` | `findUnique()` | `create()` | `update()` | `upsert()` | `delete()` | `createMany()` | `updateMany()` | `deleteMany()`

소문자 모델 이름 속성을 통해 접근합니다: `prisma.user.create({ ... })`

- 타입 정의

Prisma Client는 모델에 대한 TypeScript 타입을 생성합니다:

```
    export type User = {
      id: number;
      email: string;
      name: string | null;
    };
```

이 타입들은 타입 안전한 데이터베이스 쿼리를 보장합니다.

## 제한 사항

모든 Prisma 모델에는 최소 하나의 고유 식별자가 있어야 합니다:

- 기본 키용 `@id` 또는 `@@id`
- 고유 제약 조건용 `@unique` 또는 `@@unique`
