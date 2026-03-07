---
title: "데이터베이스의 관계"
description: "관계는 Prisma 스키마에서 두 모델 간의 연결입니다. 이 페이지에서는 Prisma에서 일대일, 일대다, 다대다 관계를 정의하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations

# 관계

관계는 Prisma 스키마에서 두 모델 간의 연결입니다. 이 페이지에서는 Prisma에서 일대일, 일대다, 다대다 관계를 정의하는 방법을 설명합니다.

관계는 Prisma 스키마에서 두 모델 간의 _연결_ 입니다. 예를 들어, 한 사용자는 여러 블로그 게시물을 가질 수 있으므로 `User` 와 `Post` 사이에는 일대다 관계가 있습니다:

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }

    model Post {
      id       Int  @id @default(autoincrement())
      author   User @relation(fields: [authorId], references: [id])
      authorId Int  // Foreign key connecting Post to User
      title    String
    }
```

Prisma ORM 수준에서 `User` / `Post` 관계는 다음으로 구성됩니다:

- **관계 필드** (`author` 및 `posts`): Prisma ORM 수준에서 연결을 정의하며, 데이터베이스에는 존재하지 않음
- **관계 스칼라 필드** (`authorId`): 데이터베이스에 존재하는 외래 키

## 데이터베이스의 관계

- 관계형 데이터베이스

SQL에서는 _외래 키_ 를 사용해 두 테이블 간 관계를 생성합니다:

- `Post` 의 외래 키 컬럼(`authorId`)이 `User` 의 기본 키(`id`)를 참조함

```
    author     User        @relation(fields: [authorId], references: [id])
```

Prisma 스키마의 관계는 데이터베이스 테이블 간에 존재하는 관계를 나타냅니다.

- MongoDB

MongoDB는 문서가 ID로 서로를 참조하는 정규화된 데이터 모델 설계를 사용합니다:

```
    // User document
    { "_id": { "$oid": "60d5922d00581b8f0062e3a8" }, "name": "Ella" }

    // Post documents referencing the user
    { "_id": "...", "title": "How to make sushi", "authorId": { "$oid": "60d5922d00581b8f0062e3a8" } }
```

`ObjectId` 를 사용하는 경우, 모델 ID와 관계 스칼라 필드 모두에 `@db.ObjectId` 를 추가하세요:

```
    model Post {
      id       String @id @default(auto()) @map("_id") @db.ObjectId
      author   User   @relation(fields: [authorId], references: [id])
      authorId String @db.ObjectId
    }
```

## Prisma Client의 관계

- 중첩 관계로 레코드 생성

```
    const userAndPosts = await prisma.user.create({
      data: {
        posts: {
          create: [{ title: "Prisma Day 2020" }, { title: "How to write a Prisma schema" }],
        },
      },
    });
```

- 관련 데이터를 포함해 레코드 조회

```
    const getAuthor = await prisma.user.findUnique({
      where: { id: "20" },
      include: { posts: true },
    });
```

- 기존 레코드 연결

```
    await prisma.user.update({
      where: { id: 20 },
      data: {
        posts: { connect: { id: 4 } },
      },
    });
```

## 관계 유형

Prisma ORM에는 세 가지 관계 유형(또는 [카디널리티](<https://en.wikipedia.org/wiki/Cardinality_(data_modeling)>))이 있습니다:

- [일대일](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations) (1-1 관계라고도 함)
- [일대다](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-many-relations) (1-n 관계라고도 함)
- [다대다](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations) (m-n 관계라고도 함)

다음 Prisma 스키마에는 모든 관계 유형이 포함되어 있습니다:

- 일대일: `User` ↔ `Profile`
- 일대다: `User` ↔ `Post`
- 다대다: `Post` ↔ `Category`

관계형 데이터베이스

MongoDB

```
    model User {
      id      Int      @id @default(autoincrement())
      posts   Post[]
      profile Profile?
    }

    model Profile {
      id     Int  @id @default(autoincrement())
      user   User @relation(fields: [userId], references: [id])
      userId Int  @unique // relation scalar field (used in the `@relation` attribute above)
    }

    model Post {
      id         Int        @id @default(autoincrement())
      author     User       @relation(fields: [authorId], references: [id])
      authorId   Int // relation scalar field  (used in the `@relation` attribute above)
      categories Category[]
    }

    model Category {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

이 스키마는 [예제 데이터 모델](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models)과 동일하지만, [관계 필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)에 집중할 수 있도록 모든 [스칼라 필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields) (필수 [관계 스칼라 필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields) 제외)를 제거했습니다.

이 예제는 [암시적 다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations)를 사용합니다. 이러한 관계는 [관계 모호성 해소](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#disambiguating-relations)가 필요한 경우를 제외하면 `@relation` 속성이 필요하지 않습니다.

관계형 데이터베이스와 MongoDB 간에는 문법이 약간 다르다는 점에 유의하세요. 특히 [다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations)에서 그렇습니다.

관계형 데이터베이스의 경우, 다음 엔터티 관계 다이어그램은 샘플 Prisma 스키마에 대응하는 데이터베이스를 나타냅니다:

![엔터티 관계 다이어그램으로 표현한 샘플 스키마](https://docs.prisma.io/docs/img/orm/prisma-schema/data-model/relations/sample-schema.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

MongoDB의 경우 Prisma ORM은 [정규화된 데이터 모델 설계](https://www.mongodb.com/docs/manual/data-modeling/)를 사용합니다. 즉, 관계형 데이터베이스와 유사하게 문서가 ID로 서로를 참조합니다. 자세한 내용은 [MongoDB 섹션](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#mongodb)을 참조하세요.

- 암시적 및 명시적 다대다 관계

관계형 데이터베이스의 다대다 관계는 두 가지 방식으로 모델링할 수 있습니다:

- [명시적 다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#explicit-many-to-many-relations): 관계 테이블이 Prisma 스키마에서 명시적 모델로 표현됨
- [암시적 다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations): Prisma ORM이 관계 테이블을 관리하며 Prisma 스키마에는 나타나지 않음

암시적 다대다 관계에서는 두 모델 모두 단일 `@id` 를 가져야 합니다. 다음 사항에 유의하세요:

- [다중 필드 ID](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference)를 사용할 수 없음
- `@id` 대신 `@unique` 를 사용할 수 없음

이 기능들 중 하나라도 사용하려면 대신 명시적 다대다 관계를 설정해야 합니다.

암시적 다대다 관계도 기본 데이터베이스에서는 관계 테이블로 나타납니다. 다만 이 관계 테이블은 Prisma ORM이 관리합니다.

명시적 관계 대신 암시적 다대다 관계를 사용하면 [Prisma Client API](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction)가 더 단순해집니다(예: [중첩 쓰기](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes) 내부의 중첩 수준이 하나 줄어듦).

Prisma Migrate를 사용하지 않고 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection)으로 데이터 모델을 가져오는 경우에도, Prisma ORM의 [관계 테이블 규칙](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#relation-table-conventions)을 따르면 암시적 다대다 관계를 사용할 수 있습니다.

## 관계 필드

관계 필드는 타입이 다른 모델(스칼라 타입 아님)인 Prisma 모델의 필드입니다. 모든 관계에는 각 모델에 하나씩, 정확히 두 개의 관계 필드가 필요합니다.

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[] // relation field
    }

    model Post {
      id       Int    @id @default(autoincrement())
      author   User   @relation(fields: [authorId], references: [id]) // annotated relation field
      authorId Int    // relation scalar field (foreign key)
    }
```

**핵심 개념:**

- `posts` 와 `author` 는 관계 필드임(Prisma ORM 수준에만 존재)
- `authorId` 는 관계 스칼라 필드임(외래 키로 데이터베이스에 존재)

* 주석이 지정된 관계 필드

`@relation` 속성으로 주석이 지정된 관계(일대일, 일대다, MongoDB의 다대다)는 외래 키를 저장하는 쪽을 나타냅니다:

```
    author     User    @relation(fields: [authorId], references: [id])
    authorId   Int     // relation scalar field
```

**네이밍 규칙:** 관계 스칼라 필드는 일반적으로 `fieldName` + `Id` 패턴을 사용합니다(예: `author` → `authorId`).

## `@relation` 속성

`@relation` 속성은 다음 경우에 필요합니다:

- 일대일 또는 일대다 관계를 정의할 때
- 동일한 모델 간 여러 관계를 구분할 때
- [자기 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/self-relations)를 정의할 때
- MongoDB용 다대다 관계를 정의할 때

관계형 데이터베이스의 [암시적 다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations)에는 `@relation` 이 필요하지 않습니다.

## 관계 구분하기

동일한 모델 사이에 두 개의 관계가 있는 경우, `@relation` 의 `name` 인수를 사용해 구분하세요:

```
    model User {
      id           Int     @id @default(autoincrement())
      writtenPosts Post[]  @relation("WrittenPosts")
      pinnedPost   Post?   @relation("PinnedPost")
    }

    model Post {
      id         Int     @id @default(autoincrement())
      author     User    @relation("WrittenPosts", fields: [authorId], references: [id])
      authorId   Int
      pinnedBy   User?   @relation("PinnedPost", fields: [pinnedById], references: [id])
      pinnedById Int?    @unique
    }
```

`name` 은 관계의 양쪽에서 동일해야 합니다.
