---
title: "CRUD 작업"
description: "생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 작업을 수행하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/queries/crud

# CRUD 작업

생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 작업을 수행하는 방법을 알아보세요.

이 페이지에서는 Prisma Client로 CRUD 작업을 수행하는 방법을 설명합니다:

- [생성(Create)](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#create) \- 레코드 삽입
- [조회(Read)](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#read) \- 레코드 조회
- [수정(Update)](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#update) \- 레코드 수정
- [삭제(Delete)](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#delete) \- 레코드 삭제

자세한 메서드 문서는 [Prisma Client API 레퍼런스](https://docs.prisma.io/docs/orm/reference/prisma-client-reference)를 참고하세요.

## 생성

- 단일 레코드 생성

```
    const user = await prisma.user.create({
      data: {
        email: "elsa@prisma.io",
        name: "Elsa Prisma",
      },
    });
```

`id`는 자동 생성됩니다. 어떤 필드가 필수인지는 스키마에 따라 결정됩니다.

- 여러 레코드 생성

```
    const createMany = await prisma.user.createMany({
      data: [
        { name: "Bob", email: "bob@prisma.io" },
        { name: "Yewande", email: "yewande@prisma.io" },
      ],
      skipDuplicates: true, // Skip records with duplicate unique fields
    });
    // Returns: { count: 2 }
```

`skipDuplicates`는 MongoDB, SQLServer, SQLite에서 지원되지 않습니다.

- 여러 레코드를 생성하고 반환

PostgreSQL, CockroachDB, SQLite에서 지원됩니다.

```
    const users = await prisma.user.createManyAndReturn({
      data: [
        { name: "Alice", email: "alice@prisma.io" },
        { name: "Bob", email: "bob@prisma.io" },
      ],
    });
```

관계가 있는 레코드를 생성하는 방법은 [Nested writes](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes)를 참고하세요.

## 조회

- ID 또는 고유 필드로 레코드 가져오기

```
    // By unique field
    const user = await prisma.user.findUnique({
      where: { email: "elsa@prisma.io" },
    });

    // By ID
    const user = await prisma.user.findUnique({
      where: { id: 99 },
    });
```

- 모든 레코드 가져오기

```
    const users = await prisma.user.findMany();
```

- 첫 번째 일치 레코드 가져오기

```
    const user = await prisma.user.findFirst({
      where: { posts: { some: { likes: { gt: 100 } } } },
      orderBy: { id: "desc" },
    });
```

- 레코드 필터링

```
    // Single field filter
    const users = await prisma.user.findMany({
      where: { email: { endsWith: "prisma.io" } },
    });

    // Multiple conditions with OR/AND
    const users = await prisma.user.findMany({
      where: {
        OR: [{ name: { startsWith: "E" } }, { AND: { profileViews: { gt: 0 }, role: "ADMIN" } }],
      },
    });

    // Filter by related records
    const users = await prisma.user.findMany({
      where: {
        email: { endsWith: "prisma.io" },
        posts: { some: { published: false } },
      },
    });
```

더 많은 예시는 [Filtering and sorting](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting)를 참고하세요.

- 필드 선택

```
    const user = await prisma.user.findUnique({
      where: { email: "emma@prisma.io" },
      select: { email: true, name: true },
    });
    // Returns: { email: 'emma@prisma.io', name: "Emma" }
```

- 관련 레코드 포함

```
    const users = await prisma.user.findMany({
      where: { role: "ADMIN" },
      include: { posts: true },
    });
```

자세한 내용은 [Select fields](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields)와 [Relation queries](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)를 참고하세요.

## 수정

- 단일 레코드 업데이트

```
    const updateUser = await prisma.user.update({
      where: { email: "viola@prisma.io" },
      data: { name: "Viola the Magnificent" },
    });
```

- 여러 레코드 업데이트

```
    const updateUsers = await prisma.user.updateMany({
      where: { email: { contains: "prisma.io" } },
      data: { role: "ADMIN" },
    });
    // Returns: { count: 19 }
```

- 여러 레코드를 업데이트하고 반환

PostgreSQL, CockroachDB, SQLite에서 지원됩니다.

```
    const users = await prisma.user.updateManyAndReturn({
      where: { email: { contains: "prisma.io" } },
      data: { role: "ADMIN" },
    });
```

- Upsert (업데이트 또는 생성)

```
    const upsertUser = await prisma.user.upsert({
      where: { email: "viola@prisma.io" },
      update: { name: "Viola the Magnificent" },
      create: { email: "viola@prisma.io", name: "Viola the Magnificent" },
    });
```

`findOrCreate()`를 에뮬레이션하려면 빈 `update` 파라미터와 함께 `upsert()`를 사용하세요.

- 원자적 숫자 연산

```
    await prisma.post.updateMany({
      data: {
        views: { increment: 1 },
        likes: { increment: 1 },
      },
    });
```

관련 레코드 연결 및 연결 해제는 [Relation queries](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)를 참고하세요.

## 삭제

- 단일 레코드 삭제

다음 쿼리는 단일 `User` 레코드를 삭제하기 위해 [`delete()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#delete)를 사용합니다:

```
    const deleteUser = await prisma.user.delete({
      where: {
        email: "bert@prisma.io",
      },
    });
```

모든 `Post`에는 작성자가 필요하므로, 하나 이상의 게시물이 있는 사용자를 삭제하려고 하면 오류가 발생합니다. [cascading deletes](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#cascading-deletes-deleting-related-records)를 참고하세요.

- 여러 레코드 삭제

다음 쿼리는 `email`에 `prisma.io`가 포함된 모든 `User` 레코드를 삭제하기 위해 [`deleteMany()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#deletemany)를 사용합니다:

```
    const deleteUsers = await prisma.user.deleteMany({
      where: {
        email: {
          contains: "prisma.io",
        },
      },
    });
```

모든 `Post`에는 작성자가 필요하므로, 하나 이상의 게시물이 있는 사용자를 삭제하려고 하면 오류가 발생합니다. [cascading deletes](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#cascading-deletes-deleting-related-records)를 참고하세요.

- 모든 레코드 삭제

다음 쿼리는 모든 `User` 레코드를 삭제하기 위해 [`deleteMany()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#deletemany)를 사용합니다:

```
    const deleteUsers = await prisma.user.deleteMany({});
```

사용자에게 관련 레코드(예: 게시물)가 있으면 이 쿼리는 실패합니다. 이 경우 [먼저 관련 레코드를 삭제](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#cascading-deletes-deleting-related-records)해야 합니다.

- 연쇄 삭제(관련 레코드 삭제)

[referential actions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)를 사용해 연쇄 삭제를 구성할 수 있습니다.

다음 쿼리는 단일 `User` 레코드를 삭제하기 위해 [`delete()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#delete)를 사용합니다:

```
    const deleteUser = await prisma.user.delete({
      where: {
        email: "bert@prisma.io",
      },
    });
```

하지만 예제 스키마에는 `Post`와 `User` 사이에 **필수 관계**가 포함되어 있으므로, 게시물이 있는 사용자는 삭제할 수 없습니다:

```
    The change you are trying to make would violate the required relation 'PostToUser' between the `Post` and `User` models.
```

이 오류를 해결하려면 다음 방법을 사용할 수 있습니다:

- 관계를 선택 사항으로 변경:

```
model Post {
          id       Int   @id @default(autoincrement())
          author   User? @relation(fields: [authorId], references: [id])
          authorId Int?
          author   User  @relation(fields: [authorId], references: [id])
          authorId Int
        }
```

- 사용자를 삭제하기 전에 게시물의 작성자를 다른 사용자로 변경합니다.

- 트랜잭션에서 두 개의 별도 쿼리로 사용자와 해당 사용자의 모든 게시물을 삭제합니다(모든 쿼리가 성공해야 함):

```
const deletePosts = prisma.post.deleteMany({
          where: {
            authorId: 7,
          },
        });

        const deleteUser = prisma.user.delete({
          where: {
            id: 7,
          },
        });

        const transaction = await prisma.$transaction([deletePosts, deleteUser]);
```

- 모든 테이블에서 모든 레코드 삭제

때로는 실제 테이블은 유지한 채 모든 테이블의 모든 데이터를 제거하고 싶을 수 있습니다. 이는 개발 환경이나 테스트 중에 특히 유용합니다.

다음은 Prisma Client와 Prisma Migrate로 모든 테이블의 모든 레코드를 삭제하는 방법입니다.

#

- `deleteMany()`로 모든 데이터 삭제

테이블을 삭제해야 하는 순서를 알고 있다면 [`deleteMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#deletemany) 함수를 사용할 수 있습니다. 이는 [`$transaction`](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions)에서 동기적으로 실행되며, 모든 유형의 데이터베이스에서 사용할 수 있습니다.

```
    const deletePosts = prisma.post.deleteMany();
    const deleteProfile = prisma.profile.deleteMany();
    const deleteUsers = prisma.user.deleteMany();

    // The transaction runs synchronously so deleteUsers must run last.
    await prisma.$transaction([deleteProfile, deletePosts, deleteUsers]);
```

✅ **장점** :

- 스키마 구조를 미리 알고 있을 때 잘 동작함
- 각 테이블의 데이터를 동기적으로 삭제함

❌ **단점** :

- 관계형 데이터베이스에서 이 함수는 관계 제약 조건과 관계없이 테이블을 조회해 `TRUNCATE`하는 더 일반적인 솔루션만큼 확장성이 좋지 않습니다. MongoDB 커넥터를 사용할 때는 이 확장성 이슈가 적용되지 않습니다.

> **참고** : `$transaction`은 각 모델 테이블에서 연쇄 삭제를 수행하므로 순서대로 호출해야 합니다.

#

- raw SQL / `TRUNCATE`로 모든 데이터 삭제

raw SQL 작업에 익숙하다면 [`$executeRawUnsafe`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#executerawunsafe)를 사용해 테이블에 `TRUNCATE` 쿼리를 수행할 수 있습니다.

다음 예시에서 첫 번째 탭은 `$queryRaw` 조회를 사용해 Postgres 데이터베이스에서 테이블을 매핑하고, 단일 쿼리로 모든 테이블을 `TRUNCATE`하는 방법을 보여줍니다.

두 번째 탭은 MySQL 데이터베이스에서 동일한 기능을 수행하는 방법을 보여줍니다. 이 경우 `TRUNCATE`를 실행하기 전에 제약 조건을 제거하고, 완료 후 다시 복구해야 합니다. 전체 과정은 `$transaction`으로 실행됩니다.

PostgreSQL

MySQL

```
    const tablenames = await prisma.$queryRaw<
      Array<{ tablename: string }>
    >`SELECT tablename FROM pg_tables WHERE schemaname='public'`;

    const tables = tablenames
      .map(({ tablename }) => tablename)
      .filter((name) => name !== "_prisma_migrations")
      .map((name) => `"public"."${name}"`)
      .join(", ");

    try {
      await prisma.$executeRawUnsafe(`TRUNCATE TABLE ${tables} CASCADE;`);
    } catch (error) {
      console.log({ error });
    }
```

✅ **장점** :

- 확장 가능
- 매우 빠름

❌ **단점** :

- 작업을 되돌릴 수 없음
- 테이블 이름에 예약된 SQL 키워드를 사용하면 raw 쿼리 실행 시 문제가 발생할 수 있음

#

- Prisma Migrate로 모든 레코드 삭제

Prisma Migrate를 사용한다면 `migrate reset`을 사용할 수 있으며, 이 명령은 다음을 수행합니다:

1. 데이터베이스 삭제
2. 새 데이터베이스 생성
3. 마이그레이션 적용
4. 데이터로 데이터베이스 시드

## 고급 쿼리 예시

- 깊게 중첩된 레코드 트리 생성
  - 단일 `User`
  - 새로 생성된 서로 관련된 `Post` 레코드 2개
  - 게시물별 `Category`를 connect 또는 create

```
    const u = await prisma.user.create({
      include: {
        posts: {
          include: {
            categories: true,
          },
        },
      },
      data: {
        email: "emma@prisma.io",
        posts: {
          create: [
            {
              title: "My first post",
              categories: {
                connectOrCreate: [
                  {
                    create: { name: "Introductions" },
                    where: {
                      name: "Introductions",
                    },
                  },
                  {
                    create: { name: "Social" },
                    where: {
                      name: "Social",
                    },
                  },
                ],
              },
            },
            {
              title: "How to make cookies",
              categories: {
                connectOrCreate: [
                  {
                    create: { name: "Social" },
                    where: {
                      name: "Social",
                    },
                  },
                  {
                    create: { name: "Cooking" },
                    where: {
                      name: "Cooking",
                    },
                  },
                ],
              },
            },
          ],
        },
      },
    });
```
