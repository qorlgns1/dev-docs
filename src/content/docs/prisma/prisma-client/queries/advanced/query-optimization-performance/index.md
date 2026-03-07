---
title: "Prisma Optimize를 사용한 쿼리 최적화"
description: "Prisma가 내부적으로 쿼리를 최적화하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance

# Prisma Optimize를 사용한 쿼리 최적화

Prisma가 내부적으로 쿼리를 최적화하는 방법

이 가이드는 쿼리 성능을 식별하고 최적화하는 방법을 다룹니다.

## 성능 이슈 디버깅

쿼리가 느려지는 일반적인 원인:

- 데이터 과다 조회
- 인덱스 누락
- 반복 쿼리 미캐싱
- 전체 테이블 스캔

[Prisma Optimize](https://docs.prisma.io/docs/optimize)는 이러한 문제를 해결하기 위한 [권장 사항](https://docs.prisma.io/docs/optimize/recommendations)을 제공합니다. 시작하려면 [통합 가이드](https://docs.prisma.io/docs/optimize/getting-started)를 따르세요.

## 대량 쿼리 사용

일반적으로 대량의 데이터를 읽고 쓸 때는 배치 방식이 더 높은 성능을 냅니다. 예를 들어 `50,000`개의 레코드를 `50,000`번 개별 insert하는 대신 `1000`개씩 배치로 insert하는 방식입니다. `PrismaClient`는 다음 대량 쿼리를 지원합니다:

- `createMany()`
- `createManyAndReturn()`
- `deleteMany()`
- `updateMany()`
- `updateManyAndReturn()`
- `findMany()`

## 데이터베이스 커넥션 풀 고갈을 피하려면 `PrismaClient`를 재사용하거나 커넥션 풀링을 사용하세요

`PrismaClient` 인스턴스를 여러 개 생성하면, 특히 serverless 또는 edge 환경에서 데이터베이스 커넥션 풀이 고갈되어 다른 쿼리도 느려질 수 있습니다. 자세한 내용은 [serverless challenge](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#the-serverless-challenge)를 참고하세요.

전통적인 서버 기반 애플리케이션에서는 `PrismaClient`를 한 번만 인스턴스화하고 앱 전반에서 재사용하세요. 여러 인스턴스를 만드는 대신, 예를 들어 다음과 같이 하지 말고:

query.ts

```
    async function getPosts() {
      const prisma = new PrismaClient();
      await prisma.post.findMany();
    }

    async function getUsers() {
      const prisma = new PrismaClient();
      await prisma.user.findMany();
    }
```

재사용을 위해 전용 파일에 단일 `PrismaClient` 인스턴스를 정의하고 다시 export하세요:

db.ts

```
    export const prisma = new PrismaClient();
```

그다음 공유 인스턴스를 import하세요:

query.ts

```
    import { prisma } from "db.ts";

    async function getPosts() {
      await prisma.post.findMany();
    }

    async function getUsers() {
      await prisma.user.findMany();
    }
```

HMR(Hot Module Replacement)을 사용하는 프레임워크 기반 serverless 개발 환경에서는 [개발 환경에서 Prisma 단일 인스턴스 사용](https://docs.prisma.io/docs/orm/more/troubleshooting/nextjs#best-practices-for-using-prisma-client-in-development)을 올바르게 처리해야 합니다.

## n+1 문제 해결

n+1 문제는 쿼리 결과를 순회하면서 **결과마다** 추가 쿼리를 1회씩 실행할 때 발생합니다.

- fluent API와 함께 `findUnique()` 사용

Prisma의 dataloader는 동일한 tick 내 `findUnique()` 쿼리를 자동으로 배치 처리합니다. 관련 데이터를 반환하려면 fluent API를 사용하세요:

```
    // Instead of findMany per user, use:
    return context.prisma.user
      .findUnique({ where: { id: parent.id } })
      .posts();
```

- `relationLoadStrategy`로 JOIN 사용

```
    const posts = await prisma.post.findMany({
      relationLoadStrategy: "join",
      where: { authorId: parent.id },
    });
```

- `where` 필터의 모든 조건이 현재 쿼리 중인 동일 모델의 scalar 필드(고유/비고유)에 있어야 합니다.
- 모든 조건이 축약 문법 또는 명시적 문법 `(where: { field: <val>, field1: { equals: <val> } })`을 통한 `equal` 필터를 사용해야 합니다.
- boolean 연산자나 relation 필터가 없어야 합니다.

`findUnique()`의 자동 배치 처리는 **GraphQL 컨텍스트**에서 특히 유용합니다. GraphQL은 필드마다 별도의 resolver 함수를 실행하므로 중첩 쿼리를 최적화하기 어려울 수 있습니다.

예를 들어 다음 GraphQL은 모든 사용자를 가져오기 위해 `allUsers` resolver를 실행하고, 각 사용자의 게시물을 가져오기 위해 사용자마다 `posts` resolver를 **한 번씩** 실행합니다(n+1):

```
    query {
      allUsers {
        id,
        posts {
          id
        }
      }
    }
```

`allUsers` 쿼리는 `user.findMany(..)`를 사용해 모든 사용자를 반환합니다:

```
    const Query = objectType({
      name: "Query",
      definition(t) {
        t.nonNull.list.nonNull.field("allUsers", {
          type: "User",
          resolve: (_parent, _args, context) => {
            return context.prisma.user.findMany();
          },
        });
      },
    });
```

이 경우 단일 SQL 쿼리가 생성됩니다:

```
    {
      timestamp: 2021-02-19T09:43:06.332Z,
      query: 'SELECT `dev`.`User`.`id`, `dev`.`User`.`email`, `dev`.`User`.`name` FROM `dev`.`User` WHERE 1=1 LIMIT ? OFFSET ?',
      params: '[-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
```

하지만 이후 `posts` resolver 함수는 사용자마다 **한 번씩** 호출됩니다. 그 결과 모든 사용자의 게시물을 한 번의 `findMany()`로 가져오는 대신, 사용자마다 `findMany()` 쿼리가 **✘ 실행**됩니다(쿼리를 보려면 CLI 출력을 펼치세요).

```
    const User = objectType({
      name: "User",
      definition(t) {
        t.nonNull.int("id");
        t.string("name");
        t.nonNull.string("email");
        t.nonNull.list.nonNull.field("posts", {
          type: "Post",
          resolve: (parent, _, context) => {
            return context.prisma.post.findMany({
              where: { authorId: parent.id || undefined },
            });
          },
        });
      },
    });
```

```
    {
      timestamp: 2021-02-19T09:43:06.343Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
      params: '[1,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:43:06.347Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
      params: '[3,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:43:06.348Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
      params: '[2,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:43:06.348Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
      params: '[4,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:43:06.348Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` = ? LIMIT ? OFFSET ?',
      params: '[5,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    // And so on
```

#

- 해결 방법 1: fluent API로 쿼리 배치 처리

사용자의 게시물을 반환하려면, 예시처럼 `findUnique()`와 [fluent API](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#fluent-api)(`.posts()`)를 함께 사용하세요. resolver가 사용자마다 한 번씩 호출되더라도 Prisma Client의 Prisma dataloader가 **✔ `findUnique()` 쿼리를 배치 처리**합니다.

게시물을 반환할 때 `prisma.posts.findMany()` 대신 `prisma.user.findUnique(...).posts()` 쿼리를 사용하는 것이 직관에 반할 수 있습니다. 특히 전자가 한 번이 아니라 두 번의 쿼리를 발생시키기 때문입니다.

게시물을 반환할 때 fluent API(`user.findUnique(...).posts()`)를 써야 하는 **유일한** 이유는 Prisma Client의 dataloader가 `findUnique()` 쿼리는 배치 처리하지만 현재는 [ `findMany()` 쿼리를 배치 처리하지 않기](https://github.com/prisma/prisma/issues/1477) 때문입니다.

dataloader가 `findMany()` 쿼리를 배치 처리하게 되거나, 쿼리에 `relationStrategy`가 `join`으로 설정되면, 더 이상 이런 방식으로 fluent API와 `findUnique()`를 함께 사용할 필요가 없습니다.

```
    const User = objectType({
      name: "User",
      definition(t) {
        t.nonNull.int("id");
        t.string("name");
        t.nonNull.string("email");
        t.nonNull.list.nonNull.field("posts", {
          type: "Post",
          resolve: (parent, _, context) => {
            return context.prisma.post.findMany({
              where: { authorId: parent.id || undefined },
            });
            return context.prisma.user
              .findUnique({
                where: { id: parent.id || undefined },
              })
              .posts();
          },
        });
      },
    });
```

```
    {
      timestamp: 2021-02-19T09:59:46.340Z,
      query: 'SELECT `dev`.`User`.`id`, `dev`.`User`.`email`, `dev`.`User`.`name` FROM `dev`.`User` WHERE 1=1 LIMIT ? OFFSET ?',
      params: '[-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:59:46.350Z,
      query: 'SELECT `dev`.`User`.`id` FROM `dev`.`User` WHERE `dev`.`User`.`id` IN (?,?,?) LIMIT ? OFFSET ?',
      params: '[1,2,3,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
    {
      timestamp: 2021-02-19T09:59:46.350Z,
      query: 'SELECT `dev`.`Post`.`id`, `dev`.`Post`.`createdAt`, `dev`.`Post`.`updatedAt`, `dev`.`Post`.`title`, `dev`.`Post`.`content`, `dev`.`Post`.`published`, `dev`.`Post`.`viewCount`, `dev`.`Post`.`authorId` FROM `dev`.`Post` WHERE `dev`.`Post`.`authorId` IN (?,?,?) LIMIT ? OFFSET ?',
      params: '[1,2,3,-1,0]',
      duration: 0,
      target: 'quaint::connector::metrics'
    }
```

`posts` resolver가 사용자마다 한 번씩 호출되면, Prisma Client의 dataloader는 동일한 파라미터와 selection set을 가진 `findUnique()` 쿼리를 그룹화합니다. 각 그룹은 단일 `findMany()`로 최적화됩니다.

#

- 해결 방법 2: JOIN으로 쿼리 수행

`relationLoadStrategy`를 `"join"`으로 설정하면 [database join](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)으로 쿼리를 수행할 수 있으며, 데이터베이스에 **한 번의** 쿼리만 실행되도록 보장할 수 있습니다.

```
    const User = objectType({
      name: "User",
      definition(t) {
        t.nonNull.int("id");
        t.string("name");
        t.nonNull.string("email");
        t.nonNull.list.nonNull.field("posts", {
          type: "Post",
          resolve: (parent, _, context) => {
            return context.prisma.post.findMany({
              relationLoadStrategy: "join",
              where: { authorId: parent.id || undefined },
            });
          },
        });
      },
    });
```

- 루프에서 n+1 피하기

별도 쿼리로 루프를 돌리지 마세요:

```
    // BAD: n+1 queries
    const users = await prisma.user.findMany({});
    users.forEach(async (usr) => {
      const posts = await prisma.post.findMany({ where: { authorId: usr.id } });
    });
```

대신 `include` 또는 `in` 필터를 사용하세요:

```
    // GOOD: 2 queries with include
    const usersWithPosts = await prisma.user.findMany({
      include: { posts: true },
    });

    // GOOD: 2 queries with in filter
    const users = await prisma.user.findMany({});
    const posts = await prisma.post.findMany({
      where: { authorId: { in: users.map(u => u.id) } },
    });

    // BEST: 1 query with join
    const posts = await prisma.post.findMany({
      relationLoadStrategy: "join",
      where: { authorId: { in: users.map(u => u.id) } },
    });
```

이는 효율적인 쿼리 방식이 아닙니다. 대신 다음 방법을 사용할 수 있습니다:

- 중첩 조회([`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include))를 사용해 사용자와 관련 게시물을 함께 반환
- [`in`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#in) 필터 사용
- [`relationLoadStrategy`](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)를 `"join"`으로 설정

#

- `include`로 n+1 해결

`include`를 사용하면 각 사용자의 게시물을 함께 반환할 수 있습니다. 이 경우 SQL 쿼리는 **두 번만** 실행됩니다. 한 번은 사용자를 가져오고, 한 번은 게시물을 가져옵니다. 이를 [중첩 조회](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads)라고 합니다.

```
    const usersWithPosts = await prisma.user.findMany({
      include: {
        posts: true,
      },
    });
```

```
    SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
    SELECT "public"."Post"."id", "public"."Post"."title", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
```

#

- `in`으로 n+1 해결

사용자 ID 목록이 있다면, `in` 필터를 사용해 `authorId`가 해당 ID 목록에 `in`인 모든 게시물을 반환할 수 있습니다:

```
    const users = await prisma.user.findMany({});

    const userIds = users.map((x) => x.id);

    const posts = await prisma.post.findMany({
      where: {
        authorId: {
          in: userIds,
        },
      },
    });
```

```
    SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
    SELECT "public"."Post"."id", "public"."Post"."createdAt", "public"."Post"."updatedAt", "public"."Post"."title", "public"."Post"."content", "public"."Post"."published", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
```

#

- `relationLoadStrategy: "join"`으로 n+1 해결

`relationLoadStrategy`를 `"join"`으로 설정하면 [database join](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)으로 쿼리를 수행할 수 있으며, 데이터베이스에 **한 번의** 쿼리만 실행되도록 보장할 수 있습니다.

```
    const users = await prisma.user.findMany({});

    const userIds = users.map((x) => x.id);

    const posts = await prisma.post.findMany({
      relationLoadStrategy: "join",
      where: {
        authorId: {
          in: userIds,
        },
      },
    });
```
