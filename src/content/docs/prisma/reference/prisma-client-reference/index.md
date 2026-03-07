---
title: "Prisma Client API 레퍼런스"
description: "Prisma Client 쿼리 및 작업을 위한 전체 API 참조"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/prisma-client-reference

# Prisma Client API 레퍼런스

Prisma Client 쿼리 및 작업을 위한 전체 API 참조

Prisma Client API 참조 문서는 다음 스키마를 기반으로 합니다:

```
    model User {
      id           Int              @id @default(autoincrement())
      name         String?
      email        String           @unique
      profileViews Int              @default(0)
      role         Role             @default(USER)
      coinflips    Boolean[]
      posts        Post[]
      city         String
      country      String
      profile      ExtendedProfile?
      pets         Json
    }

    model ExtendedProfile {
      id     Int     @id @default(autoincrement())
      userId Int?    @unique
      bio    String?
      User   User?   @relation(fields: [userId], references: [id])
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      published Boolean @default(true)
      author    User    @relation(fields: [authorId], references: [id])
      authorId  Int
      comments  Json
      views     Int     @default(0)
      likes     Int     @default(0)
    }

    enum Role {
      USER
      ADMIN
    }
```

생성된 모든 예시 타입(`UserSelect`, `UserWhereUniqueInput` 등)은 `User` 모델을 기반으로 합니다.

## `PrismaClient`

이 섹션에서는 `PrismaClient` 생성자와 해당 매개변수를 설명합니다.

- `adapter`

데이터베이스 연결을 위한 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 지정합니다. [`accelerateUrl`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#accelerateurl)을 사용하지 않는 경우 필수입니다.

#

- 예시

```
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "../prisma/generated/client";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });
```

- `accelerateUrl`

원격 쿼리 실행을 위한 [Prisma Accelerate](https://www.prisma.io/accelerate) URL을 지정합니다. [`adapter`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#adapter)를 사용하지 않는 경우 필수입니다.

#

- 예시

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({
      accelerateUrl: process.env.ACCELERATE_URL,
    });
```

- `log`

로깅의 유형과 수준을 결정합니다. 참고: [Logging](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/logging)

#

- 옵션

| 옵션           | 예시                                                                     |
| -------------- | ------------------------------------------------------------------------ |
| 로그 수준 배열 | `[ "info", "query" ]`                                                    |
| 로그 정의 배열 | `[ { level: "info", emit: "event" }, { level: "warn", emit: "stdout" }]` |

#

- 로그 수준

| 이름    | 예시                                      |
| ------- | ----------------------------------------- |
| `query` | Prisma에서 실행한 모든 쿼리를 기록합니다. |

관계형 데이터베이스의 경우 모든 SQL 쿼리를 기록합니다. 예시:
`prisma:query SELECT "public"."User"."id", "public"."User"."email" FROM "public"."User" WHERE ("public"."User"."id") IN (SELECT "t0"."id" FROM "public"."User" AS "t0" INNER JOIN "public"."Post" AS "j0" ON ("j0"."authorId") = ("t0"."id") WHERE ("j0"."views" > $1 AND "t0"."id" IS NOT NULL)) OFFSET $2`

MongoDB의 경우 [`mongosh` shell](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh) 형식으로 쿼리를 기록합니다. 예시:
`prisma:query db.User.deleteMany({ _id: ( $in: [ “6221ce49f756b0721fc00542”, ], }, })`
`info`| 예시:
`prisma:info Started http server on http://127.0.0.1:58471`
`warn`| 경고.
`error`| 오류.

#

- Emit 형식

| 이름     | 설명                                                           |
| -------- | -------------------------------------------------------------- |
| `stdout` | 참고: [stdout](https://en.wikipedia.org/wiki/Standard_streams) |
| `event`  | 구독할 수 있는 이벤트를 발생시킵니다.                          |

#

- 이벤트 타입

`query` 이벤트 타입:

index.d.ts

```
    export type QueryEvent = {
      timestamp: Date;
      query: string; // Query sent to the database
      params: string; // Query parameters
      duration: number; // Time elapsed (in milliseconds) between client issuing query and database responding - not only time taken to run query
      target: string;
    };
```

MongoDB의 경우 `params` 및 `duration` 필드는 undefined임에 유의하세요.

그 외 모든 로그 수준 이벤트 타입:

index.d.ts

```
    export type LogEvent = {
      timestamp: Date;
      message: string;
      target: string;
    };
```

#

- 예시

#

- `query` 및 `info`를 `stdout`으로 로깅

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({ log: ["query", "info"] });

    async function main() {
      const countUsers = await prisma.user.count({});
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

```
    prisma:info  Starting a postgresql pool with 13 connections.
    prisma:info  Started http server
    prisma:query SELECT COUNT(*) FROM (SELECT "public"."User"."id" FROM "public"."User" WHERE 1=1 ORDER BY "public"."User"."coinflips" ASC OFFSET $1) AS "sub"
```

#

- `query` 이벤트를 콘솔에 로깅

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({
      log: [{ level: "query", emit: "event" }],
    });

    prisma.$on("query", (e) => {
      console.log(e);
    });

    async function main() {
      const countUsers = await prisma.user.count({});
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

```
    {
      timestamp: 2020-11-17T10:32:10.898Z,
      query: 'SELECT COUNT(*) FROM (SELECT "public"."User"."id" FROM "public"."User" WHERE 1=1 OFFSET $1) AS "sub"',
      params: '[0]',
      duration: 5,
      target: 'quaint::connector::metrics'
    }
```

#

- `info`, `warn`, `error` 이벤트를 콘솔에 로깅](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#log-info-warn-and-error-events-to-console)

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({
      log: [
        { level: "warn", emit: "event" },
        { level: "info", emit: "event" },
        { level: "error", emit: "event" },
      ],
    });

    prisma.$on("warn", (e) => {
      console.log(e);
    });

    prisma.$on("info", (e) => {
      console.log(e);
    });

    prisma.$on("error", (e) => {
      console.log(e);
    });

    async function main() {
      const countUsers = await prisma.user.count({});
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

```
    {
      timestamp: 2020-11-17T10:33:24.592Z,
      message: 'Starting a postgresql pool with 13 connections.',
      target: 'quaint::pooled'
    }
    {
      timestamp: 2020-11-17T10:33:24.637Z,
      message: 'Started http server',
      target: 'query_engine::server'
    }
```

- `errorFormat`

Prisma Client가 반환하는 오류의 수준과 형식을 결정합니다.

#

- 오류 형식

| 이름                  | 설명                                      |
| --------------------- | ----------------------------------------- |
| `undefined`           | 정의하지 않으면 기본값은 colorless입니다. |
| `pretty`              | 보기 좋은 오류 형식을 활성화합니다.       |
| `colorless` (default) | 무색 오류 형식을 활성화합니다.            |
| `minimal`             | 최소 오류 형식을 활성화합니다.            |

#

- 예시

#

- 오류 형식 없음

```
    const prisma = new PrismaClient({
      // Defaults to colorless
    });
```

#

- `pretty` 오류 형식

```
    const prisma = new PrismaClient({
      errorFormat: "pretty",
    });
```

#

- `colorless` 오류 형식

```
    const prisma = new PrismaClient({
      errorFormat: "colorless",
    });
```

#

- `minimal` 오류 형식

```
    const prisma = new PrismaClient({
      errorFormat: "minimal",
    });
```

- `comments`

SQL 쿼리에 주석으로 메타데이터를 추가하는 [SQL commenter plugins](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/sql-comments) 배열을 정의합니다. 이는 observability, 디버깅, 그리고 애플리케이션 trace와의 쿼리 연관 분석에 유용합니다.

#

- 옵션

| 옵션                   | 설명                                                                                          |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| `SqlCommenterPlugin[]` | SQL commenter plugin 함수 배열입니다. 각 plugin은 쿼리 컨텍스트를 받아 키-값 쌍을 반환합니다. |

#

- 퍼스트 파티 플러그인

| 패키지                               | 설명                                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| `@prisma/sqlcommenter-query-tags`    | `AsyncLocalStorage`를 사용해 async 컨텍스트 내 쿼리에 임의의 태그를 추가합니다 |
| `@prisma/sqlcommenter-trace-context` | 분산 추적을 위해 W3C Trace Context(`traceparent`) 헤더를 추가합니다            |

#

- 예시

#

- 퍼스트 파티 플러그인 사용

```
    import { PrismaClient } from "../prisma/generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { queryTags } from "@prisma/sqlcommenter-query-tags";
    import { traceContext } from "@prisma/sqlcommenter-trace-context";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });

    const prisma = new PrismaClient({
      adapter,
      comments: [queryTags(), traceContext()],
    });
```

#

- 사용자 정의 플러그인 만들기

```
    import { PrismaClient } from "../prisma/generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";
    import type { SqlCommenterPlugin } from "@prisma/sqlcommenter";

    const appPlugin: SqlCommenterPlugin = (context) => ({
      application: "my-app",
      environment: process.env.NODE_ENV ?? "development",
      model: context.query.modelName,
      action: context.query.action,
    });

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });

    const prisma = new PrismaClient({
      adapter,
      comments: [appPlugin],
    });
```

이렇게 하면 다음과 같은 주석이 포함된 SQL 쿼리가 생성됩니다:

```
    SELECT "id", "name" FROM "User" /*action='findMany',application='my-app',environment='production',model='User'*/
```

자세한 내용은 [SQL comments](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/sql-comments)를 참고하세요.

- `transactionOptions`

기본 [transaction options](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#transaction-isolation-level)을 전역으로 설정합니다.

#

- 비고
  - 트랜잭션 수준은 트랜잭션별로 재정의할 수 있습니다.

#

- 옵션

| 옵션             | 설명                                                                                                                                                                                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `maxWait`        | Prisma Client가 데이터베이스에서 트랜잭션을 획득하기 위해 대기하는 최대 시간입니다. 기본값은 2초입니다.                                                                                                                                                               |
| `timeout`        | 인터랙티브 트랜잭션이 취소 및 롤백되기 전까지 실행될 수 있는 최대 시간입니다. 기본값은 5초입니다.                                                                                                                                                                     |
| `isolationLevel` | [transaction isolation level](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#transaction-isolation-level)을 설정합니다. 기본적으로 현재 데이터베이스에 설정된 값을 사용합니다. 사용 중인 데이터베이스에 따라 사용 가능한 수준이 다를 수 있습니다. |

#

- 예시

```
    const prisma = new PrismaClient({
      transactionOptions: {
        isolationLevel: Prisma.TransactionIsolationLevel.Serializable,
        maxWait: 5000, // default: 2000
        timeout: 10000, // default: 5000
      },
    });
```

## 모델 쿼리

모델 쿼리를 사용해 모델에서 CRUD 작업을 수행합니다. 참고: [CRUD](https://docs.prisma.io/docs/orm/prisma-client/queries/crud)

- `findUnique()`

`findUnique()` 쿼리를 사용하면 단일 데이터베이스 레코드를 조회할 수 있습니다:

- _ID_ 기준
- _unique_ 속성 기준

#

- 비고
  - Prisma Client의 dataloader는 동일한 `select` 및 `where` 매개변수를 가진 [`findUnique()` 쿼리를 자동으로 배치 처리](https://docs.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance#using-findunique-with-the-fluent-api)합니다.
  - 레코드를 찾지 못했을 때 쿼리에서 오류를 발생시키려면 [`findUniqueOrThrow`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#finduniqueorthrow) 사용을 고려하세요.
  - [JSON](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#json) 데이터 타입 필드를 필터링하기 위해 [필터 조건](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-conditions-and-operators)(예: `equals`, `contains`, `not`)을 사용할 수 없습니다. 필터 조건을 사용하면 해당 필드에 대해 `null` 응답이 반환될 가능성이 큽니다.

#

- 옵션

| 이름                   | 예시 타입 (`User`)       | 필수    | 설명                                                                                                                                                                                                     |
| ---------------------- | ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `where`                | `UserWhereUniqueInput`   | **Yes** | 레코드를 선택할 수 있도록 모델의 모든 필드를 래핑합니다([자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput)).         |
| `select`               | `XOR<UserSelect, null>`  | No      | 반환 객체에 [포함할 속성](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields)을 지정합니다.                                                                                          |
| `include`              | `XOR<UserInclude, null>` | No      | 반환 객체에서 [즉시 로드할 관계](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)를 지정합니다.                                                                                   |
| `omit`                 | `XOR<UserOmit, null>`    | No      | 반환 객체에서 제외할 속성을 지정합니다. 지정한 필드를 결과에서 제외합니다                                                                                                                                |
| `relationLoadStrategy` | `'join'` or `'query'`    | No      | **기본값:`join`**. 관계에 대한 [로드 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` preview feature가 필요합니다. |

#

- 반환 타입

| 반환 타입                 | 예시                       | 설명                                                     |
| ------------------------- | -------------------------- | -------------------------------------------------------- |
| JavaScript object (typed) | `User`                     |
| JavaScript object (plain) | `{ title: "Hello world" }` | `select` 및 `include`를 사용해 반환할 필드를 결정합니다. |
| `null`                    | `null`                     | 레코드를 찾을 수 없음                                    |

#

- 예시

#

- `id`가 `42`인 `User` 레코드 가져오기

```
    const result = await prisma.user.findUnique({
      where: {
        id: 42,
      },
    });
```

#

- `email`이 `alice@prisma.io`인 `User` 레코드 가져오기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-the-user-record-with-an-email-of-aliceprismaio)

```
    const result = await prisma.user.findUnique({
      where: {
        email: "alice@prisma.io",
      },
    });
```

#

- `firstName`이 `Alice`이고 `lastName`이 `Smith`인 `User` 레코드 가져오기 (`@@unique`)](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-the-user-record-with-firstname-of-alice-and-lastname-of-smith-unique)

예시 `@@unique` 블록이 있는 User 모델 펼치기

```
    model User {
      firstName String
      lastName  String

      @@unique(fields: [firstName, lastName], name: "fullname")
    }
```

```
    const result = await prisma.user.findUnique({
      where: {
        fullname: {
          // name property of @@unique attribute - default is firstname_lastname
          firstName: "Alice",
          lastName: "Smith",
        },
      },
    });
```

#

- `firstName`이 `Alice`이고 `lastName`이 `Smith`인 `User` 레코드 가져오기 (`@@id`)](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-the-user-record-with-firstname-of-alice-and-lastname-of-smith-id)

예시 `@@id` 블록이 있는 User 모델 펼치기

```
    model User {
      firstName String
      lastName  String

      @@id([firstName, lastName])
    }
```

```
    const result = await prisma.user.findUnique({
      where: {
        firstName_lastName: {
          firstName: "Alice",
          lastName: "Smith",
        },
      },
    });
```

- `findUniqueOrThrow()`

`findUniqueOrThrow()`는 [`findUnique()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findunique)와 동일한 방식으로 단일 레코드를 조회합니다. 하지만 쿼리에서 요청한 레코드를 찾지 못하면 `PrismaClientKnownRequestError`를 throw합니다.

사용 예시는 다음과 같습니다:

```
    await prisma.user.findUniqueOrThrow({
      where: { id: 1 },
    });
```

`findUniqueOrThrow()`는 다음과 같은 점에서 `findUnique()`와 다릅니다:

- 반환 타입이 nullable이 아닙니다. 예를 들어 `post.findUnique()`는 `post` 또는 `null`을 반환할 수 있지만, `post.findUniqueOrThrow()`는 항상 `post`를 반환합니다.

- [`$transaction` API](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#the-transaction-api)의 순차 작업과 호환되지 않습니다. 쿼리가 `PrismaClientKnownRequestError`를 throw하면 API는 호출 배열의 어떤 작업도 롤백하지 않습니다. 해결 방법으로, 다음과 같이 `$transaction` API에서 interactive transactions를 사용할 수 있습니다:

```
$transaction(async (prisma) => {
           await prisma.model.create({ data: { ... });
           await prisma.model.findUniqueOrThrow();
         })
```

- `findFirst()`

`findFirst`는 조건에 일치하는 목록의 첫 번째 레코드를 반환합니다.

#

- 비고
  - 레코드를 찾지 못했을 때 쿼리가 에러를 throw하도록 하려면, 대신 [`findFirstOrThrow`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findfirstorthrow)를 사용하는 것을 고려하세요.

#

- 옵션

| Name                   | Example type (`User`)                                 | Required | Description                                                                                                                                                                                                  |
| ---------------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `select`               | `XOR<UserSelect, null>`                               | No       | 반환 객체에 [포함할 속성을 지정](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields)합니다.                                                                                              |
| `include`              | `XOR<UserInclude, null>`                              | No       | 반환 객체에서 [eager loading할 relation을 지정](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)합니다.                                                                               |
| `omit`                 | `XOR<UserOmit, null>`                                 | No       | 반환 객체에서 제외할 속성을 지정합니다. 지정한 필드를 결과에서 제외합니다.                                                                                                                                   |
| `relationLoadStrategy` | `'join'` or `'query'`                                 | No       | **기본값:`join`**. relation에 대한 [로딩 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` preview feature가 필요합니다. |
| `where`                | `UserWhereInput`                                      | No       | 목록을 어떤 속성으로든 필터링할 수 있도록 _모든_ 모델 필드를 타입으로 감쌉니다.                                                                                                                              |
| `orderBy`              | `XOR<Enumerable<UserOrderByInput>, UserOrderByInput>` | No       | 반환 목록을 어떤 속성으로든 정렬할 수 있습니다.                                                                                                                                                              |

#

- 반환 타입

| Return type               | Example                    | Description                                                 |
| ------------------------- | -------------------------- | ----------------------------------------------------------- |
| JavaScript object (typed) | `User`                     | 반환 객체에 포함할 속성을 지정합니다.                       |
| JavaScript object (plain) | `{ title: "Hello world" }` | 반환할 필드를 결정하려면 `select`와 `include`를 사용하세요. |
| `null`                    | `null`                     | 레코드를 찾지 못함                                          |

#

- 비고
  - 내부적으로 `findFirst`는 `findMany`를 호출하며 동일한 쿼리 옵션을 받습니다.
  - `findFirst` 쿼리에서 음수 `take` 값을 전달하면 목록 순서가 반전됩니다.

#

- 예제

결과 필터링 방법 예시는 [Filter conditions and operators](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-conditions-and-operators)를 참고하세요.

#

- `name`이 `Alice`인 첫 번째 `User` 레코드 가져오기

```
    const user = await prisma.user.findFirst({
      where: { name: "Alice" },
    });
```

#

- `title`이 `A test`로 시작하는 첫 번째 `Post` 레코드를 가져오고, `take`로 목록 순서 반전하기

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({});

    async function main() {
      const a = await prisma.post.create({
        data: {
          title: "A test 1",
        },
      });

      const b = await prisma.post.create({
        data: {
          title: "A test 2",
        },
      });

      const c = await prisma.post.findFirst({
        where: {
          title: {
            startsWith: "A test",
          },
        },
        orderBy: {
          title: "asc",
        },
        take: -1, // Reverse the list
      });
    }

    main();
```

- `findFirstOrThrow()`

`findFirstOrThrow()`는 [`findFirst()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findfirst)와 동일한 방식으로 단일 데이터 레코드를 조회합니다. 하지만 쿼리에서 레코드를 찾지 못하면 `PrismaClientKnownRequestError`를 throw합니다.

`findFirstOrThrow()`는 다음과 같은 점에서 `findFirst()`와 다릅니다:

- 반환 타입이 nullable이 아닙니다. 예를 들어 `post.findFirst()`는 `post` 또는 `null`을 반환할 수 있지만, `post.findFirstOrThrow`는 항상 `post`를 반환합니다.

- [`$transaction` API](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#the-transaction-api)의 순차 작업과 호환되지 않습니다. 쿼리가 `PrismaClientKnownRequestError`를 반환하면 API는 호출 배열의 어떤 작업도 롤백하지 않습니다. 해결 방법으로, 다음과 같이 `$transaction` API에서 interactive transactions를 사용할 수 있습니다:

```
prisma.$transaction(async (tx) => {
          await tx.model.create({ data: { ... });
          await tx.model.findFirstOrThrow();
        })
```

- `findMany()`

`findMany`는 레코드 목록을 반환합니다.

#

- 옵션

| Name                          | Type                                | Required                                        | Description                                                                                                                                                                                                  |
| ----------------------------- | ----------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `select`                      | `XOR<PostSelect, null>`             | No                                              | 반환 객체에 [포함할 속성을 지정](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields)합니다.                                                                                              |
| `include`                     | `XOR<PostInclude, null>`            | No                                              | 반환 객체에서 [eager loading할 relation을 지정](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)합니다.                                                                               |
| `omit`                        | `XOR<PostOmit, null>`               | No                                              | 반환 객체에서 제외할 속성을 지정합니다. 지정한 필드를 결과에서 제외합니다                                                                                                                                    |
| `relationLoadStrategy`        | `'join'` or `'query'`               | No                                              | **기본값:`join`**. relation에 대한 [로딩 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` preview feature가 필요합니다. |
| `where`                       | `UserWhereInput`                    | No                                              | 목록을 어떤 속성으로든 필터링할 수 있도록 _모든_ 모델 필드를 타입으로 감쌉니다.                                                                                                                              |
| `orderBy`                     | `XOR<Enumerable<PostOrder`          |
| `ByInput>, PostOrderByInput>` | No                                  | 반환 목록을 어떤 속성으로든 정렬할 수 있습니다. |
| `cursor`                      | `UserWhereUniqueInput`              | No                                              | 목록의 위치를 지정합니다(일반적으로 값은 `id` 또는 다른 고유 값을 지정).                                                                                                                                     |
| `take`                        | `number`                            | No                                              | 목록에서 반환할 객체 수를 지정합니다(_앞쪽_ 기준(양수 값) 또는 _뒤쪽_ 기준(음수 값), 목록 자체 **또는** `cursor` 위치가 지정된 경우 그 위치 기준).                                                           |
| `skip`                        | `number`                            | No                                              | 목록에서 반환된 객체 중 건너뛸 개수를 지정합니다.                                                                                                                                                            |
| `distinct`                    | `Enumerable<UserDistinctFieldEnum>` | No                                              | 특정 필드 기준으로 중복 행을 제거할 수 있습니다. 예: 고유한 `Post` title만 반환.                                                                                                                             |

#

- 반환 타입

| Return type                     | Example                      | Description                                                 |
| ------------------------------- | ---------------------------- | ----------------------------------------------------------- |
| JavaScript array object (typed) | `User[]`                     |
| JavaScript array object (plain) | `[{ title: "Hello world" }]` | 반환할 필드를 결정하려면 `select`와 `include`를 사용하세요. |
| Empty array                     | `[]`                         | 일치하는 레코드를 찾지 못함.                                |

#

- 예제

결과 필터링 방법 예시는 [Filter conditions and operators](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-conditions-and-operators)를 참고하세요.

#

- `name`이 `Alice`인 모든 `User` 레코드 가져오기

```
    const user = await prisma.user.findMany({
      where: { name: "Alice" },
    });
```

- `create()`

`create`는 새 데이터베이스 레코드를 생성합니다.

#

- 옵션

| Name                                                                                   | Type                     | Required                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `data`                                                                                 | `XOR<UserCreateInput,`   |
| `UserUncheckedCreateInput>`                                                            | **Yes**                  | 새 레코드를 생성할 때 제공할 수 있도록 모든 모델 필드를 타입으로 감쌉니다. 또한 relation 필드도 포함되어 있어 (트랜잭션) 중첩 insert를 수행할 수 있습니다. 데이터 모델에서 optional로 표시되었거나 기본값이 있는 필드는 선택 사항입니다. |
| [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select)   | `XOR<UserSelect, null>`  | No                                                                                                                                                                                                                                       | 반환 객체에 [포함할 속성을 지정](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields)합니다.                                                                                              |
| [`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include) | `XOR<UserInclude, null>` | No                                                                                                                                                                                                                                       | 반환 객체에서 [eager loading할 relation을 지정](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)합니다.                                                                               |
| [`omit`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)       | `XOR<UserOmit, null>`    | No                                                                                                                                                                                                                                       | 반환 객체에서 제외할 속성을 지정합니다. 지정한 필드를 결과에서 제외합니다                                                                                                                                    |
| `relationLoadStrategy`                                                                 | `'join'` or `'query'`    | No                                                                                                                                                                                                                                       | **기본값:`join`**. relation에 대한 [로딩 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` preview feature가 필요합니다. |

#

- 반환 타입

| Return type               | Example                        | Description                                                 |
| ------------------------- | ------------------------------ | ----------------------------------------------------------- |
| JavaScript object (typed) | `User`                         |
| JavaScript object (plain) | `{ name: "Alice Wonderland" }` | 반환할 필드를 결정하려면 `select`와 `include`를 사용하세요. |

#

- 비고
  - 중첩 [`create`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#create)도 수행할 수 있습니다. 예를 들어 `User` 1개와 `Post` 레코드 2개를 동시에 추가할 수 있습니다.

#

- 예제

#

- 필수 필드가 `email` 하나뿐인 단일 새 레코드 생성

```
    const user = await prisma.user.create({
      data: { email: "alice@prisma.io" },
    });
```

#

- 여러 개의 새 레코드 생성

대부분의 경우 [`createMany()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmany) 또는 [`createManyAndReturn()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmanyandreturn) 쿼리로 배치 insert를 수행할 수 있습니다. 하지만 [여러 레코드를 insert할 때 `create()`가 최선인 시나리오](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#remarks-11)도 있습니다.

다음 예제는 **두 개의** `INSERT` 문을 생성합니다:

```
    import { Prisma, PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({ log: ["query"] });

    async function main() {
      let users: Prisma.UserCreateInput[] = [
        {
          email: "ariana@prisma.io",
          name: "Ari",
          profileViews: 20,
          coinflips: [true, false, false],
          role: "ADMIN",
        },
        {
          email: "elsa@prisma.io",
          name: "Elsa",
          profileViews: 20,
          coinflips: [true, false, false],
          role: "ADMIN",
        },
      ];

      await Promise.all(
        users.map(async (user) => {
          await prisma.user.create({
            data: user,
          });
        }),
      );
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

```
    prisma:query BEGIN
    prisma:query INSERT INTO "public"."User" ("name","email","profileViews","role","coinflips") VALUES ($1,$2,$3,$4,$5) RETURNING "public"."User"."id"
    prisma:query SELECT "public"."User"."id", "public"."User"."name", "public"."User"."email", "public"."User"."profileViews", "public"."User"."role", "public"."User"."coinflips" FROM "public"."User" WHERE "public"."User"."id" = $1 LIMIT $2 OFFSET $3
    prisma:query INSERT INTO "public"."User" ("name","email","profileViews","role","coinflips") VALUES ($1,$2,$3,$4,$5) RETURNING "public"."User"."id"
    prisma:query COMMIT
    prisma:query SELECT "public"."User"."id", "public"."User"."name", "public"."User"."email", "public"."User"."profileViews", "public"."User"."role", "public"."User"."coinflips" FROM "public"."User" WHERE "public"."User"."id" = $1 LIMIT $2 OFFSET $3
    prisma:query COMMIT
```

- `update()`

`update`는 기존 데이터베이스 레코드를 업데이트합니다.

#

- 옵션

| Name                        | Type                   | Required                                                                                                                                                | Description                                                                                                                                                                                    |
| --------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                      | `XOR<UserUpdateInput`  |
| `UserUncheckedUpdateInput>` | **Yes**                | 기존 레코드를 업데이트할 때 제공할 수 있도록 모델의 모든 필드를 감쌉니다. 데이터 모델에서 optional로 표시되었거나 기본값이 있는 필드는 선택 사항입니다. |
| `where`                     | `UserWhereUniqueInput` | **Yes**                                                                                                                                                 | 레코드를 선택할 수 있도록 모델의 모든 필드를 감쌉니다([자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput)). |

[`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select)| `XOR<UserSelect, null>`| 아니요| 반환된 객체에서 [포함할 속성을 지정합니다](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields).
[`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include)| `XOR<UserInclude, null>`| 아니요| 반환된 객체에서 [즉시 로드할 관계를 지정합니다](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries).
[`omit`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)| `XOR<UserOmit, null>`| 아니요| 반환된 객체에서 제외할 속성을 지정합니다. 지정된 필드를 결과에서 제외합니다.
`relationLoadStrategy`| `'join'` or `'query'`| 아니요| **기본값:`join`**. 관계에 대한 [로드 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` 프리뷰 기능이 필요합니다.

#

- 반환 타입

| 반환 타입                                      | 예시                           | 설명                                                                                                                                       |
| ---------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| JavaScript 객체(타입 지정)                     | `User`                         |
| JavaScript 객체(일반)                          | `{ name: "Alice Wonderland" }` | 반환할 필드를 결정하려면 `select`와 `include`를 사용하세요.                                                                                |
| `PrismaClientKnownRequestError` (코드 `P2025`) |                                | 업데이트할 레코드가 존재하지 않으면 발생합니다. [오류 참조](https://docs.prisma.io/docs/orm/reference/error-reference#p2025)를 확인하세요. |

#

- 비고
  - 업데이트 시 산술 연산(더하기, 빼기, 곱하기, 나누기)을 수행하려면 경쟁 상태를 방지하기 위해 [원자적 업데이트](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#atomic-number-operations)를 사용하세요.
  - 중첩 [`update`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#update-1)도 수행할 수 있습니다. 예를 들어 사용자와 해당 사용자의 게시물을 동시에 업데이트할 수 있습니다.

#

- 예시

#

- `id`가 `1`인 `User` 레코드의 `email`을 `alice@prisma.io`로 업데이트

```
    const user = await prisma.user.update({
      where: { id: 1 },
      data: { email: "alice@prisma.io" },
    });
```

- `upsert()`

이 섹션에서는 `upsert()` 작업의 사용법을 다룹니다. `update()` 내에서 [중첩 upsert 쿼리](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#upsert-1)를 사용하는 방법은 링크된 문서를 참고하세요.

`upsert`는 다음을 수행합니다.

- 기존 데이터베이스 레코드가 `where` 조건을 만족하면 해당 레코드를 업데이트합니다.
- 데이터베이스 레코드가 `where` 조건을 만족하지 않으면 새 데이터베이스 레코드를 생성합니다.

#

- 옵션

| 이름                                                                                   | 타입                     | 필수                                                                                                                                                                                                                   | 설명                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create`                                                                               | `XOR<UserCreateInput,`   |
| `UserUncheckedCreateInput>`                                                            | **예**                   | 새 레코드 생성 시 제공할 수 있도록 모델의 모든 필드를 감쌉니다. 또한 관계 필드도 포함하므로 (트랜잭션) 중첩 삽입을 수행할 수 있습니다. 데이터모델에서 선택 사항으로 표시되었거나 기본값이 있는 필드는 선택 사항입니다. |
| `update`                                                                               | `XOR<UserUpdateInput,`   |
| `UserUncheckedUpdateInput>`                                                            | **예**                   | 기존 레코드 업데이트 시 제공할 수 있도록 모델의 모든 필드를 감쌉니다. 데이터모델에서 선택 사항으로 표시되었거나 기본값이 있는 필드는 선택 사항입니다.                                                                  |
| `where`                                                                                | `UserWhereUniqueInput`   | **예**                                                                                                                                                                                                                 | 레코드를 선택할 수 있도록 모델의 모든 필드를 감쌉니다([자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput)).       |
| [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select)   | `XOR<UserSelect, null>`  | 아니요                                                                                                                                                                                                                 | 반환된 객체에서 [포함할 속성을 지정합니다](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields).                                                                                  |
| [`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include) | `XOR<UserInclude, null>` | 아니요                                                                                                                                                                                                                 | 반환된 객체에서 [즉시 로드할 관계를 지정합니다](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries).                                                                             |
| [`omit`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)       | `XOR<UserOmit, null>`    | 아니요                                                                                                                                                                                                                 | 반환된 객체에서 제외할 속성을 지정합니다. 지정된 필드를 결과에서 제외합니다.                                                                                                                         |
| `relationLoadStrategy`                                                                 | `'join'` or `'query'`    | 아니요                                                                                                                                                                                                                 | **기본값:`join`**. 관계에 대한 [로드 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` 프리뷰 기능이 필요합니다. |

#

- 반환 타입

| 반환 타입                  | 예시                           | 설명                                                        |
| -------------------------- | ------------------------------ | ----------------------------------------------------------- |
| JavaScript 객체(타입 지정) | `User`                         |
| JavaScript 객체(일반)      | `{ name: "Alice Wonderland" }` | 반환할 필드를 결정하려면 `select`와 `include`를 사용하세요. |

#

- 비고
  - 업데이트 시 산술 연산(더하기, 빼기, 곱하기, 나누기)을 수행하려면 경쟁 상태를 방지하기 위해 [원자적 업데이트](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#atomic-number-operations)를 사용하세요.
  - 둘 이상의 upsert 작업이 동시에 발생하고 레코드가 아직 존재하지 않으면 경쟁 상태가 발생할 수 있습니다. 그 결과 하나 이상의 upsert 작업에서 고유 키 제약 오류가 발생할 수 있습니다. 애플리케이션 코드에서 이 오류를 잡아 작업을 재시도할 수 있습니다. [자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#unique-key-constraint-errors-on-upserts).
  - Prisma ORM은 가능한 경우 upsert 쿼리를 데이터베이스에 위임합니다. [자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#database-upserts).

#

- 예시

#

- 기존에 있으면 업데이트하고, 없으면 `email`이 `alice@prisma.io`인 새 `User` 레코드 생성

```
    const user = await prisma.user.upsert({
      where: { id: 1 },
      update: { email: "alice@prisma.io" },
      create: { email: "alice@prisma.io" },
    });
```

#

- upsert에서의 고유 키 제약 오류

#

- 문제

여러 upsert 작업이 동시에 발생하고 레코드가 아직 존재하지 않으면, 하나 이상의 작업이 [고유 키 제약 오류](https://docs.prisma.io/docs/orm/reference/error-reference#p2002)를 반환할 수 있습니다.

#

- 원인

Prisma Client가 upsert를 수행할 때는 먼저 해당 레코드가 데이터베이스에 이미 존재하는지 확인합니다. 이 확인을 위해 Prisma Client는 upsert 작업의 `where` 절로 읽기 작업을 수행합니다. 가능한 결과는 다음 두 가지입니다.

- 레코드가 존재하지 않으면 Prisma Client가 해당 레코드를 생성합니다.
- 레코드가 존재하면 Prisma Client가 해당 레코드를 업데이트합니다.

애플리케이션이 동시에 두 개 이상의 upsert 작업을 수행하려고 하면, 두 개 이상의 작업이 레코드를 찾지 못해 해당 레코드를 생성하려고 시도하는 경쟁 상태가 발생할 수 있습니다. 이 상황에서는 한 작업이 새 레코드 생성에 성공하지만 다른 작업은 실패하고 고유 키 제약 오류를 반환합니다.

#

- 해결 방법

애플리케이션 코드에서 P2002 오류를 처리하세요. 오류가 발생하면 upsert 작업을 재시도해 행을 업데이트하세요.

#

- 데이터베이스 upsert

가능한 경우 Prisma Client는 `upsert` 쿼리를 데이터베이스에 위임합니다. 이를 *데이터베이스 upsert*라고 합니다.

데이터베이스 upsert의 장점은 다음과 같습니다.

- Prisma Client가 처리하는 upsert보다 더 빠릅니다.
- [고유 키 제약 오류](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#unique-key-constraint-errors-on-upserts)가 발생하지 않습니다.

Prisma Client는 [특정 기준](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#database-upsert-query-criteria)을 충족하면 자동으로 데이터베이스 upsert를 사용합니다. 이 기준을 충족하지 않으면 Prisma Client가 `upsert`를 처리합니다.

데이터베이스 upsert를 사용하려면 Prisma Client가 SQL 구문 [`INSERT ... ON CONFLICT SET .. WHERE`](https://www.prisma.io/dataguide/postgresql/inserting-and-modifying-data/insert-on-conflict)을 데이터베이스로 전송합니다.

#

- 데이터베이스 upsert 사전 요구 사항

Prisma Client는 CockroachDB, PostgreSQL 또는 SQLite 데이터 소스에서 데이터베이스 upsert를 사용합니다.

#

- 데이터베이스 upsert 쿼리 기준

Prisma Client는 `upsert` 쿼리가 다음 기준을 충족할 때 `upsert` 쿼리에 데이터베이스 upsert를 사용합니다.

- `upsert`의 `create` 및 `update` [옵션](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#options-7)에 중첩 쿼리가 없습니다.
- 쿼리에 [중첩 읽기](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads)를 사용하는 선택이 포함되지 않습니다.
- 쿼리가 하나의 모델만 수정합니다.
- `upsert`의 `where` 옵션에 고유 필드가 하나만 있습니다.
- `where` 옵션의 고유 필드와 `create` 옵션의 고유 필드 값이 동일합니다.

쿼리가 이 기준을 충족하지 않으면 Prisma Client가 upsert를 직접 처리합니다.

#

- 데이터베이스 upsert 예시

다음 예시는 이 스키마를 사용합니다.

```
    model User {
      id           Int    @id
      profileViews Int
      userName     String @unique
      email        String

      @@unique([id, profileViews])
    }
```

다음 `upsert` 쿼리는 모든 기준을 충족하므로 Prisma Client가 데이터베이스 upsert를 사용합니다.

```
    prisma.user.upsert({
      where: {
        userName: "Alice",
      },
      create: {
        id: 1,
        profileViews: 1,
        userName: "Alice",
        email: "alice@prisma.io",
      },
      update: {
        email: "updated@example.com",
      },
    });
```

이 상황에서 Prisma는 다음 SQL 쿼리를 사용합니다.

```
    INSERT INTO "public"."User" ("id","profileViews","userName","email") VALUES ($1,$2,$3,$4)
    ON CONFLICT ("userName") DO UPDATE
    SET "email" = $5 WHERE ("public"."User"."userName" = $6 AND 1=1) RETURNING "public"."User"."id", "public"."User"."profileViews", "public"."User"."userName", "public"."User"."email"
```

다음 쿼리는 `where` 절에 여러 고유 값을 가지므로 Prisma Client가 데이터베이스 upsert를 사용하지 _않습니다_.

```
    prisma.User.upsert({
      where: {
        userName: "Alice",
        profileViews: 1,
        id: 1,
      },
      create: {
        id: 1,
        profileViews: 1,
        userName: "Alice",
        email: "alice@prisma.io",
      },
      update: {
        email: "updated@example.com",
      },
    });
```

다음 쿼리에서는 `where`와 `create` 옵션의 `userName` 값이 서로 다르므로 Prisma Client가 데이터베이스 upsert를 사용하지 _않습니다_.

```
    prisma.User.upsert({
      where: {
        userName: "Alice",
      },
      create: {
        id: 1,
        profileViews: 1,
        userName: "AliceS",
        email: "alice@prisma.io",
      },
      update: {
        email: "updated@example.com",
      },
    });
```

다음 쿼리에서는 `posts`의 `title` 필드에 대한 선택이 중첩 읽기이므로 Prisma Client가 데이터베이스 upsert를 사용하지 _않습니다_.

```
    prisma.user.upsert({
      select: {
        email: true,
        id: true,
        posts: {
          select: {
            title: true,
          },
        },
      },
      where: {
        userName: "Alice",
      },

      create: {
        id: 1,
        profileViews: 1,
        userName: "Alice",
        email: "alice@prisma.io",
      },
      update: {
        email: "updated@example.com",
      },
    });
```

- `delete()`

`delete`는 기존 데이터베이스 레코드를 삭제합니다. 레코드는 다음 기준으로 삭제할 수 있습니다.

- _ID_ 기준
- _고유_ 속성 기준

특정 기준과 일치하는 레코드를 삭제하려면 필터와 함께 [`deleteMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#deletemany)를 사용하세요.

#

- 옵션

| 이름                                                                                 | 타입                    | 필수   | 설명                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------ | ----------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `where`                                                                              | `UserWhereUniqueInput`  | **예** | 레코드를 선택할 수 있도록 모델의 모든 필드를 감쌉니다([자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput)). |
| [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select) | `XOR<UserSelect, null>` | 아니요 | 반환된 객체에서 [포함할 속성을 지정합니다](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields).                                                                            |

[`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include)| `XOR<UserInclude, null>`| 아니요| 반환된 객체에서 어떤 관계를 즉시 로드할지 [지정합니다](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries).
[`omit`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)| `XOR<UserOmit, null>`| 아니요| 반환된 객체에서 제외할 속성을 지정합니다. 지정된 필드를 결과에서 제외합니다.
`relationLoadStrategy`| `'join'` 또는 `'query'`| 아니요| **기본값:`join`**. 관계에 대한 [로드 전략](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)입니다. `relationJoins` 프리뷰 기능이 필요합니다.

#

- 반환 타입

| 반환 타입                                      | 예시                           | 설명                                                                                                                                       |
| ---------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| JavaScript object (typed)                      | `User`                         | 삭제된 `User` 레코드입니다.                                                                                                                |
| JavaScript object (plain)                      | `{ name: "Alice Wonderland" }` | 삭제된 `User` 레코드의 데이터입니다. `select` 및 `include`를 사용해 반환할 필드를 결정합니다.                                              |
| `PrismaClientKnownRequestError` (code `P2025`) |                                | 삭제할 레코드가 존재하지 않으면 발생합니다. [에러 레퍼런스](https://docs.prisma.io/docs/orm/reference/error-reference#p2025)를 참고하세요. |

#

- 비고
  - 일부 조건에 따라 여러 레코드를 삭제하려면(예: `prisma.io` 이메일 주소를 가진 모든 `User` 레코드), `deleteMany`를 사용하세요.

#

- 예제

#

- `id`가 `1`인 `User` 레코드 삭제

```
    const user = await prisma.user.delete({
      where: { id: 1 },
    });
```

#

- `email`이 `elsa@prisma.io`와 같은 `User` 레코드 삭제

다음 쿼리는 특정 사용자 레코드를 삭제하고, `select`를 사용해 삭제된 사용자의 `name`과 `email`을 반환합니다:

```
    const deleteUser = await prisma.user.delete({
      where: {
        email: "elsa@prisma.io",
      },
      select: {
        email: true,
        name: true,
      },
    });
```

```
    { "email": "elsa@prisma.io", "name": "Elsa" }
```

- `createMany()`

`createMany`는 트랜잭션에서 여러 레코드를 생성합니다.

#

- 옵션

| 이름              | 타입                              | 필수   | 설명                                                                                                                                                                                                                                                |
| ----------------- | --------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`            | `Enumerable<UserCreateManyInput>` | **예** | 새 레코드를 생성할 때 제공할 수 있도록 모델의 모든 필드를 타입으로 감쌉니다. 데이터모델에서 선택 사항이거나 기본값이 있는 필드는 선택 사항입니다.                                                                                                   |
| `skipDuplicates?` | `boolean`                         | 아니요 | 이미 존재하는 고유 필드 또는 ID 필드가 있는 레코드는 삽입하지 않습니다. [`ON CONFLICT DO NOTHING`](https://www.postgresql.org/docs/9.5/sql-insert.html#SQL-ON-CONFLICT)을 지원하는 데이터베이스에서만 지원됩니다. MongoDB와 SQLServer는 제외됩니다. |

#

- 반환 타입

| 반환 타입      | 예시           | 설명                    |
| -------------- | -------------- | ----------------------- |
| `BatchPayload` | `{ count: 3 }` | 생성된 레코드 수입니다. |

#

- 비고
  - `createMany()`는 SQLite에서 지원됩니다.
  - `skipDuplicates` 옵션은 MongoDB, SQLServer, SQLite에서 지원되지 않습니다.
  - 최상위 `createMany()` 쿼리 내부에서 중첩 `create`, `createMany`, `connect`, `connectOrCreate` 쿼리를 사용해 관계를 생성하거나 연결할 수는 **없습니다**. [우회 방법](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#using-nested-createmany)을 참고하세요.
  - [`update()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#update) 또는 [`create()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#create) 쿼리 내부에서 중첩 [`createMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmany-1) 쿼리를 사용할 수 있습니다. 예를 들어 중첩 `createMany`로 `User` 하나와 `Post` 레코드 두 개를 동시에 추가할 수 있습니다.

#

- 예제

#

- 여러 새 사용자 생성

```
    const users = await prisma.user.createMany({
      data: [
        { name: "Sonali", email: "sonali@prisma.io" },
        { name: "Alex", email: "alex@prisma.io" },
      ],
    });
```

- `createManyAndReturn()`

`createManyAndReturn`은 여러 레코드를 생성하고 결과 객체를 반환합니다. PostgreSQL, CockroachDB, SQLite에서 지원됩니다.

#

- 옵션

| 이름                                                                                   | 타입                              | 필수   | 설명                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------- | --------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                 | `Enumerable<UserCreateManyInput>` | **예** | 새 레코드를 생성할 때 제공할 수 있도록 모델의 모든 필드를 타입으로 감쌉니다. 데이터모델에서 선택 사항이거나 기본값이 있는 필드는 선택 사항입니다.                                                                                                   |
| [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select)   | `XOR<UserSelect, null>`           | 아니요 | 반환된 객체에 포함할 속성을 [지정합니다](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields).                                                                                                                                   |
| [`omit`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)       | `XOR<UserOmit, null>`             | 아니요 | 반환된 객체에서 제외할 속성을 지정합니다. 지정된 필드를 결과에서 제외합니다. `select`와 상호 배타적입니다.                                                                                                                                          |
| [`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include) | `XOR<UserInclude, null>`          | 아니요 | 반환된 객체에서 어떤 관계를 즉시 로드할지 [지정합니다](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries).                                                                                                                     |
| `skipDuplicates?`                                                                      | `boolean`                         | 아니요 | 이미 존재하는 고유 필드 또는 ID 필드가 있는 레코드는 삽입하지 않습니다. [`ON CONFLICT DO NOTHING`](https://www.postgresql.org/docs/9.5/sql-insert.html#SQL-ON-CONFLICT)을 지원하는 데이터베이스에서만 지원됩니다. MongoDB와 SQLServer는 제외됩니다. |

#

- 비고
  - `skipDuplicates` 옵션은 SQLite에서 지원되지 않습니다.
  - `createManyAndReturn`이 반환하는 요소의 순서는 보장되지 않습니다.
  - 최상위 `createManyAndReturn()` 쿼리 내부에서 중첩 `create`, `createMany`, `connect`, `connectOrCreate` 쿼리를 사용해 관계를 생성하거나 연결할 수는 **없습니다**. [우회 방법](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#using-nested-createmany)을 참고하세요.
  - 관계를 `include`로 포함하면 관계마다 별도 쿼리가 생성됩니다.
  - `relationLoadStrategy: join`은 지원되지 않습니다.

#

- 반환 타입

| 반환 타입                       | 예시                   | 설명                                                           |
| ------------------------------- | ---------------------- | -------------------------------------------------------------- |
| JavaScript array object (typed) | `User[]`               |
| JavaScript array object (plain) | `[{ name: "Sonali" }]` | `select`, `omit`, `include`를 사용해 반환할 필드를 결정합니다. |

#

- 예제

#

- 여러 새 사용자 생성 후 반환

```
    const users = await prisma.user.createManyAndReturn({
      data: [
        { name: "Sonali", email: "sonali@prisma.io" },
        { name: "Alex", email: "alex@prisma.io" },
      ],
    });
```

```
    [
      { "id": 0, "name": "Sonali", "email": "sonali@prisma.io", "profileViews": 0 },
      { "id": 1, "name": "Alex", "email": "alex@prisma.io", "profileViews": 0 }
    ]
```

- `updateMany()`

`updateMany`는 기존 데이터베이스 레코드의 배치를 대량으로 업데이트하고, 업데이트된 레코드 수를 반환합니다.

#

- 옵션

| 이름                            | 타입                               | 필수                                                                                                                                                      | 설명                                                                                                                               |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `data`                          | `XOR<UserUpdateManyMutationInput,` |
| `UserUncheckedUpdateManyInput>` | **예**                             | 기존 레코드를 업데이트할 때 제공할 수 있도록 모델의 모든 필드를 감쌉니다. 데이터모델에서 선택 사항이거나 기본값이 있는 필드는 `data`에서 선택 사항입니다. |
| `where`                         | `UserWhereInput`                   | 아니요                                                                                                                                                    | 모델의 _모든_ 필드를 감싸서 임의의 속성으로 목록을 필터링할 수 있게 합니다. 목록을 필터링하지 않으면 모든 레코드가 업데이트됩니다. |
| `limit`                         | `number`                           | 아니요                                                                                                                                                    | 업데이트할 레코드 수를 제한합니다.                                                                                                 |

#

- 반환 타입

| 반환 타입      | 예시           | 설명                        |
| -------------- | -------------- | --------------------------- |
| `BatchPayload` | `{ count: 4 }` | 업데이트된 레코드 수입니다. |

```
    export type BatchPayload = {
      count: number;
    };
```

#

- 예제

#

- `name`이 `Alice`인 모든 `User` 레코드를 `ALICE`로 업데이트

```
    const updatedUserCount = await prisma.user.updateMany({
      where: { name: "Alice" },
      data: { name: "ALICE" },
    });
```

#

- `email`에 `prisma.io`가 포함되고 관련 `Post` 중 하나 이상이 좋아요 10개를 초과한 모든 `User` 레코드 업데이트

```
    const updatedUserCount = await prisma.user.updateMany({
      where: {
        email: {
          contains: "prisma.io",
        },
        posts: {
          some: {
            likes: {
              gt: 10,
            },
          },
        },
      },
      data: {
        role: "USER",
      },
    });
```

#

- `email`에 `prisma.io`가 포함된 `User` 레코드를 업데이트하되, 업데이트 레코드를 5개로 제한

```
    const updatedUserCount = await prisma.user.updateMany({
      where: {
        email: {
          contains: "prisma.io",
        },
      },
      data: {
        role: "USER",
      },
      limit: 5,
    });
```

- `updateManyAndReturn()`

`updateManyAndReturn`은 여러 레코드를 업데이트하고 결과 객체를 반환합니다. PostgreSQL, CockroachDB, SQLite에서 지원됩니다.

#

- 옵션

| 이름                            | 타입                               | 필수                                                                                                                                                      | 설명                                                                                                                               |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `data`                          | `XOR<UserUpdateManyMutationInput,` |
| `UserUncheckedUpdateManyInput>` | **예**                             | 기존 레코드를 업데이트할 때 제공할 수 있도록 모델의 모든 필드를 감쌉니다. 데이터모델에서 선택 사항이거나 기본값이 있는 필드는 `data`에서 선택 사항입니다. |
| `where`                         | `UserWhereInput`                   | 아니요                                                                                                                                                    | 모델의 _모든_ 필드를 감싸서 임의의 속성으로 목록을 필터링할 수 있게 합니다. 목록을 필터링하지 않으면 모든 레코드가 업데이트됩니다. |

#

- 반환 타입

| 반환 타입                       | 예시                   | 설명                                                           |
| ------------------------------- | ---------------------- | -------------------------------------------------------------- |
| JavaScript array object (typed) | `User[]`               |
| JavaScript array object (plain) | `[{ name: "Sonali" }]` | `select`, `omit`, `include`를 사용해 반환할 필드를 결정합니다. |

#

- 예제

#

- 여러 사용자 업데이트 후 반환

```
    const users = await prisma.user.updateManyAndReturn({
      where: {
        email: {
          contains: "prisma.io",
        },
      },
      data: {
        role: "ADMIN",
      },
    });
```

```
    [
      { "id": 0, "name": "Sonali", "email": "sonali@prisma.io", "role": "ADMIN", "profileViews": 0 },
      { "id": 1, "name": "Alex", "email": "alex@prisma.io", "role": "ADMIN", "profileViews": 0 }
    ]
```

- `deleteMany()`

`deleteMany`는 트랜잭션에서 여러 레코드를 삭제합니다.

#

- 옵션

| 이름    | 타입             | 필수   | 설명                                                                      |
| ------- | ---------------- | ------ | ------------------------------------------------------------------------- |
| `where` | `UserWhereInput` | 아니요 | 모델의 _모든_ 필드를 감싸서 임의의 필드로 목록을 필터링할 수 있게 합니다. |
| `limit` | `Int`            | 아니요 | 삭제할 레코드 수를 제한합니다.                                            |

#

- 반환 타입

| 반환 타입      | 예시           | 설명                    |
| -------------- | -------------- | ----------------------- |
| `BatchPayload` | `{ count: 4 }` | 삭제된 레코드 수입니다. |

```
    export type BatchPayload = {
      count: number;
    };
```

#

- 예제

#

- 모든 `User` 레코드 삭제

```
    const deletedUserCount = await prisma.user.deleteMany({});
```

#

- `name`이 `Alice`인 모든 `User` 레코드 삭제

```
    const deletedUserCount = await prisma.user.deleteMany({
      where: { name: "Alice" },
    });
```

#

- `email`에 `prisma.io`가 포함된 모든 `User` 레코드를 삭제하되, 삭제 레코드를 5개로 제한합니다.

```
    const deletedUserCount = await prisma.user.deleteMany({
      where: {
        email: {
          contains: "prisma.io",
        },
      },
      limit: 5,
    });
```

삭제할 레코드를 필터링하는 방법의 예시는 [Filter conditions and operators](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-conditions-and-operators)를 참고하세요.

- `count()`

#

- 옵션

| Name                          | Type                       | Required                                          | Description                                                                                                                          |
| ----------------------------- | -------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `where`                       | `UserWhereInput`           | No                                                | 목록을 모든 속성으로 필터링할 수 있도록 _all_ 모델 필드를 타입으로 래핑합니다.                                                       |
| `orderBy`                     | `XOR<Enumerable<PostOrder` |
| `ByInput>, PostOrderByInput>` | No                         | 반환된 목록을 임의의 속성으로 정렬할 수 있습니다. |
| `cursor`                      | `UserWhereUniqueInput`     | No                                                | 목록의 위치를 지정합니다(값은 일반적으로 `id` 또는 다른 고유 값을 지정함).                                                           |
| `take`                        | `number`                   | No                                                | 목록에서 반환할 객체 수를 지정합니다(목록의 _beginning_(양수) 또는 _end_(음수), **또는** `cursor`가 지정된 경우 `cursor` 위치 기준). |
| `skip`                        | `number`                   | No                                                | 목록에서 반환된 객체 중 건너뛸 개수를 지정합니다.                                                                                    |

#

- 반환 타입

| Return type                    | Example                  | Description                        |
| ------------------------------ | ------------------------ | ---------------------------------- |
| `number`                       | `29`                     | 레코드 수입니다.                   |
| `UserCountAggregateOutputType` | `{ _all: 27, name: 10 }` | `select`를 사용할 경우 반환됩니다. |

#

- 예시

#

- 모든 `User` 레코드 수 세기

```
    const result = await prisma.user.count();
```

#

- 게시된 `Post`가 하나 이상 있는 모든 `User` 레코드 수 세기

```
    const result = await prisma.user.count({
      where: {
        post: {
          some: {
            published: true,
          },
        },
      },
    });
```

#

- `select`를 사용해 세 가지 카운트를 각각 수행하기

다음 쿼리는 아래를 반환합니다:

- 모든 레코드 수 (`_all`)
- `name` 필드가 non-`null`인 모든 레코드 수
- `city` 필드가 non-`null`인 모든 레코드 수

```
    const c = await prisma.user.count({
      select: {
        _all: true,
        city: true,
        name: true,
      },
    });
```

- `aggregate()`

참고: [Aggregation, grouping, and summarizing](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#aggregate)

#

- 옵션

| Name                | Type                                | Required                                          | Description                                                                                                                          |
| ------------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `where`             | `UserWhereInput`                    | No                                                | 목록을 모든 속성으로 필터링할 수 있도록 _all_ 모델 필드를 타입으로 래핑합니다.                                                       |
| `orderBy`           | `XOR<Enumerable<UserOrderByInput>,` |
| `UserOrderByInput>` | No                                  | 반환된 목록을 임의의 속성으로 정렬할 수 있습니다. |
| `cursor`            | `UserWhereUniqueInput`              | No                                                | 목록의 위치를 지정합니다(값은 일반적으로 `id` 또는 다른 고유 값을 지정함).                                                           |
| `take`              | `number`                            | No                                                | 목록에서 반환할 객체 수를 지정합니다(목록의 _beginning_(양수) 또는 _end_(음수), **또는** `cursor`가 지정된 경우 `cursor` 위치 기준). |
| `skip`              | `number`                            | No                                                | 목록에서 반환된 객체 중 건너뛸 개수를 지정합니다.                                                                                    |
| `_count`            | `true`                              | No                                                | 일치하는 레코드 수 또는 non-`null` 필드 수를 반환합니다.                                                                             |
| `_avg`              | `UserAvgAggregateInputType`         | No                                                | 지정된 필드의 모든 값 평균을 반환합니다.                                                                                             |
| `_sum`              | `UserSumAggregateInputType`         | No                                                | 지정된 필드의 모든 값 합계를 반환합니다.                                                                                             |
| `_min`              | `UserMinAggregateInputType`         | No                                                | 지정된 필드에서 사용 가능한 가장 작은 값을 반환합니다.                                                                               |
| `_max`              | `UserMaxAggregateInputType`         | No                                                | 지정된 필드에서 사용 가능한 가장 큰 값을 반환합니다.                                                                                 |

#

- 예시

#

- 모든 `User` 레코드의 `profileViews`에 대해 `_min`, `_max`, `_count` 반환

```
    const minMaxAge = await prisma.user.aggregate({
      _count: {
        _all: true,
      },
      _max: {
        profileViews: true,
      },
      _min: {
        profileViews: true,
      },
    });
```

```
    {
      _count: { _all: 29 },
      _max: { profileViews: 90 },
      _min: { profileViews: 0 }
    }
```

#

- 모든 `User` 레코드의 모든 `profileViews`에 대한 `_sum` 반환

```
    const setValue = await prisma.user.aggregate({
      _sum: {
        profileViews: true,
      },
    });
```

```
    {
      "_sum": {
        "profileViews": 9493
      }
    }
```

- `groupBy()`

참고: [Aggregation, grouping, and summarizing](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#group-by)

#

- 옵션

| Name                | Type                                 | Required                                                        | Description                                                                                                                          |
| ------------------- | ------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| `where`             | `UserWhereInput`                     | No                                                              | 목록을 모든 속성으로 필터링할 수 있도록 _all_ 모델 필드를 타입으로 래핑합니다.                                                       |
| `orderBy`           | `XOR<Enumerable<UserOrderByInput>,`  |
| `UserOrderByInput>` | No                                   | `by`에도 포함된 임의의 속성으로 반환 목록을 정렬할 수 있습니다. |
| `by`                | `Array<UserScalarFieldEnum>`         | `string`                                                        | No                                                                                                                                   | 레코드를 그룹화할 필드 또는 필드 조합을 지정합니다.      |
| `having`            | `UserScalarWhereWithAggregatesInput` | No                                                              | 집계 값으로 그룹을 필터링할 수 있습니다. 예: 평균 나이가 50 미만인 그룹만 반환.                                                      |
| `take`              | `number`                             | No                                                              | 목록에서 반환할 객체 수를 지정합니다(목록의 _beginning_(양수) 또는 _end_(음수), **또는** `cursor`가 지정된 경우 `cursor` 위치 기준). |
| `skip`              | `number`                             | No                                                              | 목록에서 반환된 객체 중 건너뛸 개수를 지정합니다.                                                                                    |
| `_count`            | `true`                               | `UserCountAggregateInputType`                                   | No                                                                                                                                   | 일치하는 레코드 수 또는 non-`null` 필드 수를 반환합니다. |
| `_avg`              | `UserAvgAggregateInputType`          | No                                                              | 지정된 필드의 모든 값 평균을 반환합니다.                                                                                             |
| `_sum`              | `UserSumAggregateInputType`          | No                                                              | 지정된 필드의 모든 값 합계를 반환합니다.                                                                                             |
| `_min`              | `UserMinAggregateInputType`          | No                                                              | 지정된 필드에서 사용 가능한 가장 작은 값을 반환합니다.                                                                               |
| `_max`              | `UserMaxAggregateInputType`          | No                                                              | 지정된 필드에서 사용 가능한 가장 큰 값을 반환합니다.                                                                                 |

#

- 예시

#

- `profileViews` 평균이 `200`보다 큰 `country`/`city` 기준으로 그룹화하고, 각 그룹의 `profileViews` `_sum` 반환

이 쿼리는 각 그룹의 `_all` 레코드 수와, 각 그룹에서 `city` 필드 값이 non-`null`인 모든 레코드 수도 함께 반환합니다.

```
    const groupUsers = await prisma.user.groupBy({
      by: ["country", "city"],
      _count: {
        _all: true,
        city: true,
      },
      _sum: {
        profileViews: true,
      },
      orderBy: {
        country: "desc",
      },
      having: {
        profileViews: {
          _avg: {
            gt: 200,
          },
        },
      },
    });
```

```
    [
      {
        country: "Denmark",
        city: "Copenhagen",
        _sum: { profileViews: 490 },
        _count: {
          _all: 70,
          city: 8,
        },
      },
      {
        country: "Sweden",
        city: "Stockholm",
        _sum: { profileViews: 500 },
        _count: {
          _all: 50,
          city: 3,
        },
      },
    ];
```

- `findRaw()`

참고: [Using Raw SQL (`findRaw()`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#findraw).

- `aggregateRaw()`

참고: [Using Raw SQL (`aggregateRaw()`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#aggregateraw).

## 모델 쿼리 옵션

- `select`

`select`는 Prisma Client가 반환하는 객체에 어떤 필드를 포함할지 정의합니다. 참고: [Select fields and include relations](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields) .

#

- 비고
  - 같은 레벨에서 `select`와 `include`를 함께 사용할 수 없습니다.
  - [관계의 `_count`를 선택](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select-a-_count-of-relations)할 수 있습니다.

#

- 예시

#

- 단일 `User` 레코드의 `name` 및 `profileViews` 필드 선택

```
    const result = await prisma.user.findUnique({
      where: { id: 1 },
      select: {
        name: true,
        profileViews: true,
      },
    });
```

```
    {
      name: "Alice",
      profileViews: 0
    }
```

#

- 여러 `User` 레코드의 `email` 및 `role` 필드 선택

```
    const result = await prisma.user.findMany({
      select: {
        email: true,
        role: true,
      },
    });
```

```
    [
      {
        email: "alice@prisma.io",
        role: "ADMIN",
      },
      {
        email: "bob@prisma.io",
        role: "USER",
      },
    ];
```

#

- 관계의 `_count` 선택

```
    const usersWithCount = await prisma.user.findMany({
      select: {
        _count: {
          select: { posts: true },
        },
      },
    });
```

```
    {
      _count: {
        posts: 3;
      }
    }
```

#

- 관련 `Post` 레코드의 'id' 및 'title' 필드 선택

```
    const result = await prisma.user.findMany({
      select: {
        id: true,
        name: true,
        posts: {
          select: {
            id: true,
            title: true,
          },
        },
      },
    });
```

```
    [
      {
        id: 1,
        name: "Alice",
        posts: [
          { id: 1, title: "Hello World" },
          { id: 2, title: "Bye bye" },
        ],
      },
      {
        id: 2,
        name: "Bob",
        posts: [],
      },
    ];
```

#

- `select` 내부의 `include`

```
    const result = await prisma.user.findMany({
      select: {
        id: true,
        name: true,
        posts: {
          include: {
            author: true,
          },
        },
      },
    });
```

```
    [
      {
        id: 1,
        name: "Alice",
        posts: [
          {
            id: 1,
            title: "Hello World",
            published: true,
            author: {
              id: 1,
              name: "Alice",
              email: "alice@prisma.io",
              role: "ADMIN",
              coinflips: [true, false],
              profileViews: 0,
            },
          },
          {
            id: 2,
            title: "Bye bye",
            published: false,
            author: {
              id: 1,
              name: "Alice",
              email: "alice@prisma.io",
              role: "USER",
              coinflips: [],
              profileViews: 0,
            },
          },
        ],
      },
    ];
```

- `include`

`include`는 Prisma Client가 반환하는 결과에 어떤 관계를 포함할지 정의합니다. 참고: [Select fields and include relations](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields) .

#

- 비고
  - [`include`로 관계의 `_count`를 포함](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include-a-_count-of-relations)할 수 있습니다.

#

- 예시

#

- `User` 레코드를 로드할 때 `posts` 및 `profile` 관계 포함

```
    const users = await prisma.user.findMany({
      include: {
        posts: true, // Returns all fields for all posts
        profile: true, // Returns all Profile fields
      },
    });
```

#

- 두 개의 `Post` 레코드로 새 `User` 레코드를 생성할 때 반환 객체에 `posts` 관계 포함

```
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        posts: {
          create: [{ title: "This is my first post" }, { title: "Here comes a second post" }],
        },
      },
      include: { posts: true }, // Returns all fields for all posts
    });
```

#

- `include`의 생성된 타입

다음 예시는 TypeScript의 `satisfies` 연산자를 `include`와 함께 사용하는 방법을 보여줍니다:

```
    const includePosts = { posts: true } satisfies Prisma.UserInclude;
```

#

- 관계의 `_count` 포함

```
    const usersWithCount = await prisma.user.findMany({
      include: {
        _count: {
          select: { posts: true },
        },
      },
    });
```

```
    { id: 1, name: "Bob", email: "bob@prisma.io", _count: { posts: 3 } },
    { id: 2,  name: "Enya", email: "enya@prisma.io", _count: { posts: 2 } }
```

- `omit`

`omit`은 Prisma Client가 반환하는 객체에서 어떤 필드를 제외할지 정의합니다.

#

- 비고
  - `omit`과 `select`는 목적이 반대이므로 함께 사용할 수 없습니다.

#

- 예시

#

- 모든 `User` 레코드에서 `password` 필드 제외

```
    const result = await prisma.user.findMany({
      omit: {
        password: true,
      },
    });
```

```
    [
      {
        id: 1,
        email: "jenny@prisma.io",
        name: "Jenny",
      },
      {
        id: 2,
        email: "rose@prisma.io",
        name: "Rose",
      },
    ];
```

#

- 모든 `User`의 `posts` 관계에서 `title` 필드 제외

```
    const results = await prisma.user.findMany({
      omit: {
        password: true,
      },
      include: {
        posts: {
          omit: {
            title: true,
          },
        },
      },
    });
```

```
    [
      {
        id: 1,
        email: "jenny@prisma.io",
        name: "Jenny",
        posts: [
          {
            id: 1,
            author: {
              id: 1,
              email: "jenny@prisma.io",
              name: "Jenny",
            },
            authorId: 1,
          },
        ],
      },
      {
        id: 2,
        email: "rose@prisma.io",
        name: "Rose",
        posts: [
          {
            id: 2,
            author: {
              id: 2,
              email: "rose@prisma.io",
              name: "Rose",
            },
            authorId: 2,
          },
        ],
      },
    ];
```

#

- `omit`의 생성된 타입

다음 예시는 TypeScript의 `satisfies` 연산자를 `omit`과 함께 사용하는 방법을 보여줍니다:

```
    const omitPassword = { password: true } satisfies Prisma.UserOmit;
```

- `relationLoadStrategy` (Preview)

`relationLoadStrategy`는 데이터베이스에서 relation을 로드하는 방식을 지정합니다. 가능한 값은 두 가지입니다.

- `join` (기본값): 데이터베이스 수준 `LATERAL JOIN`(PostgreSQL) 또는 상관 서브쿼리(MySQL)를 사용해, 단일 쿼리로 모든 데이터를 데이터베이스에서 가져옵니다.
- `query`: 데이터베이스에 여러 쿼리(테이블당 하나)를 보내고, 애플리케이션 수준에서 이를 조인합니다.

> **참고** : `relationLoadStrategy`가 [Preview](https://docs.prisma.io/docs/orm/more/releases#preview)에서 [General Availability](https://docs.prisma.io/docs/orm/more/releases#generally-available-ga)로 전환되면, `join`이 모든 relation 쿼리의 기본값이 됩니다.

조인 전략에 대한 자세한 내용은 [여기](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-load-strategies-preview)에서 확인할 수 있습니다.

현재 `relationLoadStrategy` 옵션은 Preview 상태이므로, Prisma 스키마 파일에서 `relationJoins` preview feature flag를 활성화해야 합니다:

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["relationJoins"]
    }
```

이 플래그를 추가한 후에는 Prisma Client를 다시 생성하기 위해 `prisma generate`를 다시 실행해야 합니다. `relationJoins` 기능은 현재 PostgreSQL, CockroachDB, MySQL에서 사용할 수 있습니다.

#

- 비고
  - 대부분의 상황에서는 기본 `join` 전략이 더 효과적입니다. 데이터베이스 서버 리소스를 절약하고 싶거나, 프로파일링 결과 애플리케이션 수준 조인이 더 높은 성능을 보인다면 `query`를 사용하세요.
  - 쿼리의 최상위 수준에서만 `relationLoadStrategy`를 지정할 수 있습니다. 최상위 선택은 모든 중첩 하위 쿼리에 영향을 줍니다.

#

- 예제

#

- `include` 사용 시 데이터베이스 수준 JOIN으로 `posts` relation 로드

```
    const users = await prisma.user.findMany({
      relationLoadStrategy: "join",
      include: {
        posts: true,
      },
    });
```

#

- `select` 사용 시 데이터베이스 수준 JOIN으로 `posts` relation 로드

```
    const users = await prisma.user.findMany({
      relationLoadStrategy: "join",
      select: {
        posts: true,
      },
    });
```

- `where`

`where`는 하나 이상의 [필터](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-conditions-and-operators)를 정의하며, 레코드 속성(예: 사용자 이메일 주소)이나 관련 레코드 속성(예: 사용자의 최근 게시물 제목 상위 10개)을 필터링하는 데 사용할 수 있습니다.

#

- 예제

```
    const results = await prisma.user.findMany({
      where: {
        email: {
          endsWith: "prisma.io",
        },
      },
    });
```

#

- `where`에 대한 생성된 타입

다음 예제는 TypeScript의 `satisfies` 연산자를 `where`와 함께 사용하는 방법을 보여줍니다.

- `UserWhereInput`

```
// UserWhereInput
        const whereNameIs = { name: "Rich" } satisfies Prisma.UserWhereInput;

        // It can be combined with conditional operators too
        const whereNameIsWithAnd = {
          name: "Rich",
          AND: [
            {
              email: {
                contains: "rich@boop.com",
              },
            },
          ],
        } satisfies Prisma.UserWhereInput;
```

- `UserWhereUniqueInput` 이 타입은 모델의 모든 고유 필드를 노출하는 방식으로 동작합니다. `@id`가 지정된 필드는 고유한 것으로 간주되며, `@unique`가 지정된 필드도 마찬가지입니다.

이 타입은 모델의 모든 필드를 노출합니다. 즉, 고유 필드를 기준으로 단일 레코드를 필터링할 때 고유/비고유 추가 필드를 동시에 검사할 수 있습니다. [자세히 알아보기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput).

```
// UserWhereUniqueInput
        const whereEmailIsUnique = { email: "rich@boop.com" } satisfies Prisma.UserWhereUniqueInput;
```

- `PostScalarWhereInput`

```
const whereScalarTitleIs = { title: "boop" } satisfies Prisma.PostScalarWhereInput;
```

- `PostUpdateWithWhereUniqueWithoutAuthorInput` \- 이 타입은 고유한 `where` 필드(`@id` 또는 다른 `@unique` 지정 필드)를 받아 `Author`를 제외한 `Post` 모델의 모든 필드를 업데이트합니다. `Author`는 `Post` 모델의 스칼라 필드입니다.

```
const updatePostByIdWithoutAuthor = {
          where: { id: 1 },
          data: {
            content: "This is some updated content",
            published: true,
            title: "This is a new title",
          },
        } satisfies Prisma.PostUpdateWithWhereUniqueWithoutAuthorInput;
```

- `PostUpsertWithWhereUniqueWithoutAuthorInput` \- 이 타입은 id가 일치하는 경우 `Post` 레코드의 title 필드를 업데이트하고, 존재하지 않으면 대신 생성합니다.

```
const updatePostTitleOrCreateIfNotExist = {
          where: { id: 1 },
          update: { title: "This is a new title" },
          create: {
            id: 1,
            title: "If the title doesn't exist, then create one with this text",
          },
        } satisfies Prisma.PostUpsertWithWhereUniqueWithoutAuthorInput;
```

- `PostUpdateManyWithWhereWithoutAuthorInput` \- 이 타입은 published가 false로 설정된 모든 `Post` 레코드를 업데이트합니다.

```
const publishAllPosts = {
          where: { published: { equals: false } },
          data: { published: true },
        } satisfies Prisma.PostUpdateManyWithWhereWithoutAuthorInput;
```

- `orderBy`

레코드 목록을 정렬합니다. 참고: [Sorting](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting)

#

- 비고
  - [relation 필드로 정렬](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#sort-post-by-the-related-user-records-name)할 수 있습니다. 예를 들어 작성자 이름으로 게시물을 정렬할 수 있습니다.
  - PostgreSQL에서는 [관련도 기준 정렬](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#sort-post-by-relevance-of-the-title)이 가능합니다. 자세한 내용은 [Sort by relevance](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-by-relevance-postgresql-and-mysql)를 참조하세요.
  - [`null` 레코드를 먼저 또는 나중에 정렬](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#sort-post-by-the-related-user-records-name-with-null-records-first)할 수 있습니다. 자세한 내용은 [Sort with nulls first or last](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-with-null-records-first-or-last)를 참조하세요.

#

- `sort` 인자 입력값

| Name   | Description           |
| ------ | --------------------- |
| `asc`  | 오름차순 정렬 (A → Z) |
| `desc` | 내림차순 정렬 (Z → A) |

#

- `nulls` 인자 입력값

참고:

- 이 인자는 선택 사항입니다.
- 선택적 [scalar](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields) 필드에서만 사용할 수 있습니다. 필수 필드나 [relation](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#relation-fields) 필드에서 null 기준 정렬을 시도하면 Prisma Client가 [P2009 error](https://docs.prisma.io/docs/orm/reference/error-reference#p2009)를 발생시킵니다.

| Name    | Description                    |
| ------- | ------------------------------ |
| `first` | `null` 값을 먼저 정렬합니다.   |
| `last`  | `null` 값을 나중에 정렬합니다. |

#

- 예제

#

- `email` 필드로 `User` 정렬

다음 예제는 모든 `User` 레코드를 `email` 오름차순으로 정렬해 반환합니다:

```
    const users = await prisma.user.findMany({
      orderBy: {
        email: "asc",
      },
    });
```

다음 예제는 모든 `User` 레코드를 `email` 내림차순으로 정렬해 반환합니다:

```
    const users = await prisma.user.findMany({
      orderBy: {
        email: "desc",
      },
    });
```

#

- 관련 `User` 레코드의 `name`으로 `Post` 정렬

다음 쿼리는 사용자 이름으로 게시물을 정렬합니다:

```
    const posts = await prisma.post.findMany({
      orderBy: {
        author: {
          name: "asc",
        },
      },
    });
```

#

- 관련 `User` 레코드의 `name`으로 `Post` 정렬, `null` 레코드를 먼저 배치

다음 쿼리는 사용자 이름으로 게시물을 정렬하며, `null` 레코드를 먼저 배치합니다:

```
    const posts = await prisma.post.findMany({
      orderBy: {
        author: {
          name: { sort: "asc", nulls: "first" },
        },
      },
    });
```

#

- title의 관련도로 `Post` 정렬

PostgreSQL의 경우 이 기능은 아직 Preview 상태입니다. 사용하려면 [`fullTextSearchPostgres` feature flag를 활성화](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/full-text-search#enabling-full-text-search-for-postgresql)하세요.

다음 쿼리는 검색어 `'database'`와 title의 관련도로 게시물을 정렬합니다:

```
    const posts = await prisma.post.findMany({
      orderBy: {
        _relevance: {
          fields: ['title'],
          search: 'database',
          sort: 'asc'
        },
    })
```

#

- `posts` 개수로 `User` 정렬

다음 쿼리는 게시물 수로 사용자를 정렬합니다:

```
    const getActiveusers = await prisma.user.findMany({
      orderBy: {
        posts: {
          count: "desc",
        },
      },
    });
```

#

- 여러 필드 - `email` _and_ `role`로 `User` 정렬

다음 예제는 사용자 레코드를 두 필드로 정렬합니다. 먼저 `email`, 그다음 `role`입니다:

```
    const users = await prisma.user.findMany({
      select: {
        email: true,
        role: true,
      },
      orderBy: [
        {
          email: "desc",
        },
        {
          role: "desc",
        },
      ],
    });
```

```
    [
      {
        "email": "yuki@prisma.io",
        "role": "USER"
      },
      {
        "email": "nora@prisma.io",
        "role": "USER"
      },
      {
        "email": "mary@prisma.io",
        "role": "MODERATOR"
      },
      {
        "email": "elsa@prisma.io",
        "role": "MODERATOR"
      },
      {
        "email": "eloise@prisma.io",
        "role": "USER"
      },
      {
        "email": "coco@prisma.io",
        "role": "ADMIN"
      },
      {
        "email": "anna@prisma.io",
        "role": "USER"
      },
      {
        "email": "alice@prisma.io",
        "role": "USER"
      }
    ]
```

정렬 파라미터의 순서는 중요합니다. 다음 쿼리는 `role`, 그다음 `email` 순으로 정렬합니다. 결과 차이를 확인하세요:

```
    const users = await prisma.user.findMany({
      select: {
        email: true,
        role: true,
      },
      orderBy: [
        {
          role: "desc",
        },
        {
          email: "desc",
        },
      ],
    });
```

```
    [
      {
        "email": "mary@prisma.io",
        "role": "MODERATOR"
      },
      {
        "email": "elsa@prisma.io",
        "role": "MODERATOR"
      },
      {
        "email": "yuki@prisma.io",
        "role": "USER"
      },
      {
        "email": "nora@prisma.io",
        "role": "USER"
      },
      {
        "email": "eloise@prisma.io",
        "role": "USER"
      },
      {
        "email": "anna@prisma.io",
        "role": "USER"
      },
      {
        "email": "alice@prisma.io",
        "role": "USER"
      },
      {
        "email": "coco@prisma.io",
        "role": "ADMIN"
      }
    ]
```

#

- `email`로 `User` 정렬, `name`과 `email` 선택

다음 예제는 모든 `User` 레코드의 `name`과 `email` 필드를 `email` 기준으로 정렬해 반환합니다:

```
    const users3 = await prisma.user.findMany({
      orderBy: {
        email: "asc",
      },
      select: {
        name: true,
        email: true,
      },
    });
```

```
    [
      {
        name: "Alice",
        email: "alice@prisma.io",
      },
      {
        name: "Ariadne",
        email: "ariadne@prisma.io",
      },
      {
        name: "Bob",
        email: "bob@prisma.io",
      },
    ];
```

#

- `email`로 `User` 레코드 정렬하고 중첩 `Post` 레코드는 `title`로 정렬

다음 예제는:

- 모든 `User` 레코드를 `email` 기준으로 정렬해 반환합니다.
- 각 `User` 레코드에 대해, 중첩된 모든 `Post` 레코드의 `title` 필드를 `title` 기준으로 정렬해 반환합니다.

```
    const usersWithPosts = await prisma.user.findMany({
      orderBy: {
        email: "asc",
      },
      include: {
        posts: {
          select: {
            title: true,
          },
          orderBy: {
            title: "asc",
          },
        },
      },
    });
```

```
    [
      {
        "id": 2,
        "email": "alice@prisma.io",
        "name": "Alice",
        "posts": [
          {
            "title": "Watch the talks from Prisma Day 2019"
          }
        ]
      },
      {
        "id": 3,
        "email": "ariadne@prisma.io",
        "name": "Ariadne",
        "posts": [
          {
            "title": "How to connect to a SQLite database"
          },
          {
            "title": "My first day at Prisma"
          }
        ]
      },
      {
        "id": 1,
        "email": "bob@prisma.io",
        "name": "Bob",
        "posts": [
          {
            "title": "Follow Prisma on Twitter"
          },
          {
            "title": "Subscribe to GraphQL Weekly for community news "
          }
        ]
      }
    ]
```

#

- 한 사용자의 중첩 `Post` 레코드 목록 정렬

다음 예제는 ID로 단일 `User` 레코드를 조회하고, `title` 기준으로 정렬된 중첩 `Post` 레코드 목록도 함께 가져옵니다:

```
    const userWithPosts = await prisma.user.findUnique({
      where: {
        id: 1,
      },
      include: {
        posts: {
          orderBy: {
            title: "desc",
          },
          select: {
            title: true,
            published: true,
          },
        },
      },
    });
```

```
    {
      "email": "sarah@prisma.io",
      "id": 1,
      "name": "Sarah",
      "extendedProfile": null,
      "role": "USER",
      "posts": [
        {
          "title": "Prisma Day 2020",
          "published": false
        },
        {
          "title": "My first post",
          "published": false
        },
        {
          "title": "All about databases",
          "published": true
        }
      ]
    }
```

#

- `enum` 기준 정렬

다음은 모든 `User` 레코드를 `role`(`enum`) 기준으로 정렬합니다:

```
    const sort = await prisma.user.findMany({
      orderBy: {
        role: "desc",
      },
      select: {
        email: true,
        role: true,
      },
    });
```

```
    [
      {
        "email": "emma@prisma.io",

        "role": "USER"
      },
      {
        "email": "suma@prisma.io",
        "role": "ADMIN"
      },
      {
        "email": "kwame@prisma.io",
        "role": "ADMIN"
      },
      {
        "email": "pearl@prisma.io",
        "role": "ADMIN"
      }
    ]
```

#

- `orderBy`에 대한 생성된 타입

다음 예제는 TypeScript의 `satisfies` 연산자를 `orderBy`와 함께 사용하는 방법을 보여줍니다.

- `UserOrderByInput`

```
const orderEmailsByDescending = { email: "desc" } satisfies Prisma.UserOrderByInput;
```

- `distinct`

[`findMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findmany) 또는 [`findFirst`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findfirst) 결과 목록에서 중복 레코드를 제거합니다. 참고: [Aggregation, grouping, and summarizing](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#select-distinct)

#

- 예제

#

- 단일 필드에서 distinct 선택

다음 예제는 중복 없는 모든 `city` 필드를 반환하고, `city`와 `country` 필드만 선택합니다:

```
    const distinctCities = await prisma.user.findMany({
      select: {
        city: true,
        country: true,
      },
      distinct: ["city"],
    });
```

```
    [
      { city: "Paris", country: "France" },
      { city: "Lyon", country: "France" },
    ];
```

#

- 여러 필드에서 distinct 선택

다음 예제는 중복 없는 모든 `city` _and_ `country` 필드 조합을 반환하고, `city`와 `country` 필드만 선택합니다:

```
    const distinctCitiesAndCountries = await prisma.user.findMany({
      select: {
        city: true,
        country: true,
      },
      distinct: ["city", "country"],
    });
```

```
    [
      { city: "Paris", country: "France" },
      { city: "Paris", country: "Denmark" },
      { city: "Lyon", country: "France" },
    ];
```

이제 `"Paris, France"` 외에 `"Paris, Denmark"`도 존재한다는 점에 유의하세요:

#

- 필터와 결합한 distinct 선택

다음 예제는 사용자의 이메일에 `"prisma.io"`가 포함된 경우에 대해, 중복 없는 모든 `city` _and_ `country` 필드 조합을 반환하고 `city`와 `country` 필드만 선택합니다:

```
    const distinctCitiesAndCountries = await prisma.user.findMany({
      where: {
        email: {
          contains: "prisma.io",
        },
      },
      select: {
        city: true,
        country: true,
      },
      distinct: ["city", "country"],
    });
```

```
    [
      { city: "Paris", country: "Denmark" },
      { city: "Lyon", country: "France" },
    ];
```

## `nativeDistinct`

Prisma 스키마에서 `nativeDistinct`를 활성화하면 `distinct` 작업이 데이터베이스 계층으로 푸시됩니다(지원되는 경우). 이는 성능을 크게 향상시킬 수 있습니다. 다만 다음 사항에 유의하세요.

- 일부 데이터베이스는 특정 필드 조합에서 DISTINCT를 완전히 지원하지 않을 수 있습니다.

- 동작은 provider마다 다를 수 있습니다.

`nativeDistinct`를 활성화하려면:

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["nativeDistinct"]
    }
```

자세한 내용은 [Preview Features](https://docs.prisma.io/docs/orm/reference/preview-features/client-preview-features#preview-features-promoted-to-general-availability)를 참고하세요.

## 중첩 쿼리

- `create`

중첩 `create` 쿼리는 부모 레코드에 새로운 연관 레코드(또는 레코드 집합)를 추가합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- 비고
  - `create`는 새 부모 레코드를 `create()` (`prisma.user.create(...)`) 하거나 기존 부모 레코드를 `update()` (`prisma.user.update(...)`) 할 때 중첩 쿼리로 사용할 수 있습니다.
  - 여러 연관 레코드를 생성할 때는 중첩 `create` 또는 중첩 [`createMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmany-1)를 사용할 수 있습니다. [`skipDuplicates` 쿼리 옵션](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#nested-createmany-options)이 필요하다면 `createMany`를 사용해야 합니다.

#

- 예시

#

- 새 `Profile` 레코드와 함께 새 `User` 레코드 생성

```
    const user = await prisma.user.create({
      data: {
        email: 'alice@prisma.io',
        profile: {
          create: { bio: 'Hello World' },
        },
      },
    });
```

#

- 새 `User` 레코드와 함께 새 `Profile` 레코드 생성

```
    const user = await prisma.profile.create({
      data: {
        bio: "Hello World",
        user: {
          create: { email: "alice@prisma.io" },
        },
      },
    });
```

#

- 새 `Post` 레코드와 함께 새 `User` 레코드 생성

```
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        posts: {
          create: { title: "Hello World" },
        },
      },
    });
```

#

- 새 `Post` 레코드 2개와 함께 새 `User` 레코드 생성

일대다 관계이므로 `create`에 배열을 전달해 여러 `Post` 레코드를 한 번에 생성할 수도 있습니다:

```
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        posts: {
          create: [
            {
              title: "This is my first post",
            },
            {
              title: "Here comes a second post",
            },
          ],
        },
      },
    });
```

참고: 동일한 결과를 위해 중첩 [`createMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmany-1)도 사용할 수 있습니다.

#

- 새 `Profile` 레코드를 생성하여 기존 `User` 레코드 업데이트

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          create: { bio: "Hello World" },
        },
      },
    });
```

#

- 새 `Post` 레코드를 생성하여 기존 `User` 레코드 업데이트

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          create: { title: "Hello World" },
        },
      },
    });
```

- `createMany`

중첩 `createMany` 쿼리는 부모 레코드에 새로운 레코드 집합을 추가합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- 비고
  - `createMany`는 새 부모 레코드를 `create()` (`prisma.user.create(...)`) 하거나 기존 부모 레코드를 `update()` (`prisma.user.update(...)`) 할 때 중첩 쿼리로 사용할 수 있습니다.
    - 일대다 관계 컨텍스트에서 사용 가능합니다. 예를 들어 `prisma.user.create(...)`로 사용자를 생성하고 중첩 `createMany`로 여러 게시물을 생성할 수 있습니다(게시물은 한 사용자에 속함).
    - 다대다 관계 컨텍스트에서는 사용할 수 없습니다. 예를 들어 `prisma.post.create(...)`로 게시물을 생성하면서 중첩 `createMany`로 카테고리를 생성할 수는 **없습니다**(여러 게시물이 여러 카테고리를 가짐).
  - 추가 `create` 또는 `createMany`를 중첩할 수 없습니다.
  - 외래 키를 직접 설정할 수 있습니다. 예를 들어 게시물의 `categoryId`를 설정할 수 있습니다.
  - 중첩 `createMany`는 SQLite에서 지원됩니다.
  - 여러 연관 레코드를 생성할 때는 중첩 `create` 또는 중첩 `createMany`를 사용할 수 있습니다 - [`skipDuplicates` 쿼리 옵션이 필요 없다면 `create`를 사용하는 편이 좋습니다](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#create-a-single-record-and-multiple-related-records).

#

- 옵션

| Name              | Type                              | Required | Description                                                                                                                                                                                                                                    |
| ----------------- | --------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`            | `Enumerable<UserCreateManyInput>` | **Yes**  | 새 레코드 생성 시 제공할 수 있도록 모든 모델 필드를 타입으로 래핑합니다. 데이터모델에서 선택 사항으로 표시되었거나 기본값이 있는 필드는 선택 사항입니다.                                                                                       |
| `skipDuplicates?` | `boolean`                         | No       | 고유 필드 또는 ID 필드가 이미 존재하는 레코드는 삽입하지 않습니다. [`ON CONFLICT DO NOTHING`](https://www.postgresql.org/docs/9.5/sql-insert.html#SQL-ON-CONFLICT)을 지원하는 데이터베이스에서만 지원됩니다. MongoDB와 SQLServer는 제외됩니다. |

#

- 예시

#

- `User`와 여러 개의 새 연관 `Post` 레코드 업데이트

```
    const user = await prisma.user.update({
      where: {
        id: 9,
      },
      data: {
        name: "Elliott",
        posts: {
          createMany: {
            data: [{ title: "My first post" }, { title: "My second post" }],
          },
        },
      },
    });
```

- `set`

`set`은 관계 값을 덮어씁니다. 예를 들어 `Post` 레코드 목록을 다른 목록으로 교체합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- 예시

#

- 기존 `User` 레코드를 업데이트하면서 이전 `Post` 레코드를 모두 연결 해제하고 다른 기존 레코드 2개를 연결

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          set: [{ id: 32 }, { id: 42 }],
        },
      },
    });
```

- `connect`

중첩 `connect` 쿼리는 ID 또는 고유 식별자를 지정해 레코드를 기존 연관 레코드에 연결합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- 비고
  - `connect`는 새 부모 레코드를 생성하거나 기존 부모 레코드를 업데이트할 때 중첩 쿼리로 사용할 수 있습니다.

  - 연관 레코드가 존재하지 않으면 Prisma Client가 예외를 발생시킵니다:

```
The required connected records were not found. Expected 1 records to be connected, found 0.
```

- `set`과 `connect`를 함께 사용할 때는 적용 순서가 결과에 큰 영향을 줍니다. `set`을 `connect`보다 먼저 사용하면 `set`이 기존 연결을 모두 지운 뒤 `connect`가 새 연결을 설정하므로, 연결된 레코드는 `connect` 연산으로 확정된 최종 상태만 반영합니다. 반대로 `connect`를 `set`보다 먼저 적용하면 `set` 연산이 모든 연결 레코드를 지우고 자신이 지정한 상태로 대체하므로 `connect` 동작을 덮어씁니다.

#

- 예시

#

- 새 `Profile` 레코드를 생성하고 고유 필드를 통해 기존 `User` 레코드에 연결

```
    const user = await prisma.profile.create({
      data: {
        bio: "Hello World",
        user: {
          connect: { email: "alice@prisma.io" },
        },
      },
    });
```

#

- 새 `Profile` 레코드를 생성하고 ID 필드를 통해 기존 `User` 레코드에 연결

```
    const user = await prisma.profile.create({
      data: {
        bio: "Hello World",
        user: {
          connect: { id: 42 }, // sets userId of Profile record
        },
      },
    });
```

외래 키를 직접 설정할 수도 있습니다:

```
    const user = await prisma.profile.create({
      data: {
        bio: "Hello World",
        userId: 42,
      },
    });
```

하지만 동일한 쿼리에서 직접 설정 방식과 `connect` 방식을 함께 사용할 수는 없습니다. 자세한 내용은 [this issue comment](https://github.com/prisma/prisma/issues/4322#issuecomment-737976117)를 참고하세요.

#

- 새 `Post` 레코드를 생성하고 기존 `User` 레코드에 연결

```
    const user = await prisma.post.create({
      data: {
        title: "Hello World",
        author: {
          connect: { email: "alice@prisma.io" },
        },
      },
    });
```

#

- 기존 `Profile` 레코드에 연결하여 기존 `User` 레코드 업데이트

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          connect: { id: 24 },
        },
      },
    });
```

#

- 기존 `Post` 레코드 2개에 연결하여 기존 `User` 레코드 업데이트

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          connect: [{ id: 24 }, { id: 42 }],
        },
      },
    });
```

- `connectOrCreate`

`connectOrCreate`는 ID 또는 고유 식별자로 레코드를 기존 연관 레코드에 연결하거나, 해당 레코드가 없으면 새 연관 레코드를 생성합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- 비고

동시 트랜잭션으로 실행되는 여러 `connectOrCreate` 쿼리는 **경쟁 상태(race condition)** 를 일으킬 수 있습니다. 다음 예시에서는 두 쿼리가 동시에 `computing`이라는 이름의 블로그 게시물 태그를 `connectOrCreate`하려고 시도합니다(태그 이름은 고유해야 함):

쿼리 A

쿼리 B

```
    const createPost = await prisma.post.create({
      data: {
        title: "How to create a compiler",
        content: "...",
        author: {
          connect: {
            id: 9,
          },
        },
        tags: {
          connectOrCreate: {
            create: {
              name: "computing",
            },
            where: {
              name: "computing",
            },
          },
        },
      },
    });
```

아래와 같이 쿼리 A와 쿼리 B가 겹치면 쿼리 A는 예외가 발생합니다:

| 쿼리 A (실패 ❌)                       | 쿼리 B (성공 ✅)                       |
| -------------------------------------- | -------------------------------------- |
| 쿼리가 서버에 도달하여 트랜잭션 A 시작 | 쿼리가 서버에 도달하여 트랜잭션 B 시작 |

| `tagName`이 `computing`인 레코드 조회, 레코드 없음
`tagName`이 `computing`인 레코드 조회, 레코드 없음|
| `tagName`이 `computing`인 레코드 생성 후 연결
`tagName`이 `computing`인 레코드 생성|
고유성 위반, 트랜잭션 B가 이미 레코드 생성|

이 상황을 우회하려면 고유성 위반 예외(`PrismaClientKnownRequestError`, error `P2002`)를 잡아 실패한 쿼리를 재시도하는 것을 권장합니다.

#

- 예시

#

- 새 `Profile` 레코드를 생성한 다음, 기존 `User` 레코드에 연결하거나 새 `User` 생성

다음 예시는:

1. `Profile`을 생성합니다
2. 이메일 주소가 `alice@prisma.io`인 `User`에 profile을 연결하려고 시도합니다
3. 일치하는 사용자가 없으면 새 사용자를 생성합니다

```
    const user = await prisma.profile.create({
      data: {
        bio: 'The coolest Alice on the planet',
        user: {
          connectOrCreate: {
            where:  { email: 'alice@prisma.io' },
            create: { email: 'alice@prisma.io'}
        },
      },
    })
```

#

- 새 `Post` 레코드를 생성하고 기존 `User` 레코드에 연결하거나, 새 `User` 생성

```
    const user = await prisma.post.create({
      data: {
        title: "Hello World",
        author: {
          connectOrCreate: {
            where: { email: "alice@prisma.io" },
            create: { email: "alice@prisma.io" },
          },
        },
      },
    });
```

#

- 기존 `User` 레코드를 업데이트하면서 기존 `Profile` 레코드에 연결하거나 새 `Profile` 레코드 생성

다음 예시는:

1. `id`가 `20`인 `Profile`에 사용자를 연결하려고 시도합니다
2. 일치하는 profile이 없으면 새 profile을 생성합니다

```
    const updateUser = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          connectOrCreate: {
            where: { id: 20 },
            create: {
              bio: "The coolest Alice in town",
            },
          },
        },
      },
    });
```

#

- 기존 `User` 레코드를 업데이트하면서 기존 `Post` 레코드 2개에 연결하거나 새 `Post` 레코드 2개 생성

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          connectOrCreate: [
            {
              where: { id: 32 },
              create: { title: "This is my first post" },
            },
            {
              where: { id: 19 },
              create: { title: "This is my second post" },
            },
          ],
        },
      },
    });
```

- `disconnect`

중첩 `disconnect` 쿼리는 부모 레코드와 관련 레코드 간의 연결을 끊지만, 두 레코드 모두 삭제하지는 않습니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries)

#

- Remarks
  - `disconnect`는 관계가 optional인 경우에만 사용할 수 있습니다.
  - 연결 해제를 시도하는 관계가 존재하지 않으면 작업은 아무 동작도 하지 않습니다.

#

- Examples

#

- Update an existing `User` record by disconnecting the `Profile` record it's connected to

```
    const user = await prisma.user.update({
      where: { email: "bob@prisma.io" },
      data: {
        profile: {
          disconnect: true,
        },
      },
    });
```

#

- Update an existing `User` record by disconnecting two `Post` records it's connected to

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          disconnect: [{ id: 44 }, { id: 46 }],
        },
      },
    });
```

- `update`

중첩 `update` 쿼리는 부모 레코드의 ID가 `n`인 조건에서 하나 이상의 관련 레코드를 업데이트합니다. 참고: [Working with relations](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#update-a-specific-related-record)

#

- Remarks
  - 중첩 `update` 쿼리는 최상위 `update` 쿼리의 컨텍스트에서만 사용할 수 있습니다(예: `prisma.user.update(...)`).

  - 부모 레코드가 존재하지 않으면 Prisma Client가 예외를 발생시킵니다:

```
AssertionError("Expected a valid parent ID to be present for nested update to-one case.")
```

- 업데이트하려는 관련 레코드가 존재하지 않으면 Prisma Client가 예외를 발생시킵니다:

```
AssertionError("Expected a valid parent ID to be present for nested update to-one case.")
```

#

- Examples

#

- Update an existing `User` record by updating the `Profile` record it's connected to

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          update: { bio: "Hello World" },
        },
      },
    });
```

#

- Update an existing `User` record by updating two `Post` records it's connected to

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          update: [
            {
              data: { published: true },
              where: { id: 32 },
            },
            {
              data: { published: true },
              where: { id: 23 },
            },
          ],
        },
      },
    });
```

- `upsert`

이 섹션은 `update()` 내에서의 중첩 upsert 사용법을 다룹니다. [`upsert()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#upsert) 작업에 대해서는 링크된 문서를 참고하세요.

중첩 `upsert` 쿼리는 관련 레코드가 존재하면 업데이트하고, 존재하지 않으면 새로운 관련 레코드를 생성합니다.

#

- Examples

#

- Update an existing `User` record by updating the `Profile` record it's connected to or creating a new one (_upsert_)

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          upsert: {
            create: { bio: "Hello World" },
            update: { bio: "Hello World" },
          },
        },
      },
    });
```

#

- Update an existing `User` record by updating two `Post` record it's connected to or creating new ones (_upsert_)

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          upsert: [
            {
              create: { title: "This is my first post" },
              update: { title: "This is my first post" },
              where: { id: 32 },
            },
            {
              create: { title: "This is my second post" },
              update: { title: "This is my second post" },
              where: { id: 23 },
            },
          ],
        },
      },
    });
```

- `delete`

중첩 `delete` 쿼리는 관련 레코드를 삭제합니다. 부모 레코드는 삭제되지 않습니다.

#

- Remarks
  - `delete`는 관계가 optional인 경우에만 사용할 수 있습니다.

#

- Examples

#

- Update an existing `User` record by deleting the `Profile` record it's connected to

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        profile: {
          delete: true,
        },
      },
    });
```

#

- Update an existing `User` record by deleting two `Post` records it's connected to

```
    const user = await prisma.user.update({
      where: { email: "alice@prisma.io" },
      data: {
        posts: {
          delete: [{ id: 34 }, { id: 36 }],
        },
      },
    });
```

- `updateMany`

중첩 `updateMany`는 관련 레코드 목록을 업데이트하며 필터링을 지원합니다. 예를 들어 사용자의 게시되지 않은 게시물을 업데이트할 수 있습니다.

#

- Examples

#

- Update all unpublished posts belonging to a specific user

```
    const result = await prisma.user.update({
      where: {
        id: 2,
      },
      data: {
        posts: {
          updateMany: {
            where: {
              published: false,
            },
            data: {
              likes: 0,
            },
          },
        },
      },
    });
```

- `deleteMany`

중첩 `deleteMany`는 관련 레코드를 삭제하며 필터링을 지원합니다. 예를 들어, 해당 사용자의 다른 속성을 업데이트하면서 게시물을 삭제할 수 있습니다.

#

- Examples

#

- Delete all posts belonging to a specific user as part of an update

```
    const result = await prisma.user.update({
      where: {
        id: 2,
      },
      data: {
        name: "Updated name",
        posts: {
          deleteMany: {},
        },
      },
    });
```

## 필터 조건과 연산자

- `equals`

값이 `n`과 같습니다.

#

- Examples

**`name`이 `"Eleanor"`와 같은 모든 사용자를 반환**

```
    const result = await prisma.user.findMany({
      where: {
        name: {
          equals: "Eleanor",
        },
      },
    });
```

`equals`는 생략할 수도 있습니다:

```
    const result = await prisma.user.findMany({
      where: {
        name: "Eleanor",
      },
    });
```

**수량이 "warn quantity" 임계값보다 낮은 모든 제품 반환**

이 예제는 동일한 모델의 필드를 비교합니다.

```
    const productsWithLowQuantity = await prisma.product.findMany({
      where: {
        quantity: {
          lte: prisma.product.fields.warnQuantity,
        },
      },
    });
```

**선호 색상이 파란색과 초록색인 모든 사용자 반환**

이 예제는 `favoriteColors` 필드가 `['blue', 'green']`로 설정된 사용자를 찾습니다.

`equals`를 사용할 때는 요소의 순서가 중요합니다. 즉 `['blue', 'green']`은 `['green', 'blue']`와 **같지 않습니다**

```
    const favoriteColorFriends = await prisma.user.findMany({
      where: {
        favoriteColors: {
          equals: ["blue", "green"],
        },
      },
    });
```

- `not`

값이 `n`과 같지 않습니다.

#

- Examples

#

- Return all users where `name` does **not** equal `"Eleanor"`

```
    const result = await prisma.user.findMany({
      where: {
        name: {
          not: "Eleanor",
        },
      },
    });
```

`not`은 지정된 값과 일치하지 않는 모든 항목을 반환합니다. 하지만 컬럼이 nullable이면 `NULL` 값은 반환되지 않습니다. `null` 값도 반환해야 한다면 [`OR`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#or) 연산자를 사용해 `NULL` 값을 포함하세요.

#

- Return all users where `name` does **not** equal `"Eleanor"` **including** users where `name` is `NULL`

```
    await prisma.user.findMany({
      where: {
        OR: [{ name: { not: "Eleanor" } }, { name: null }],
      },
    });
```

- `in`

값 `n`이 목록에 존재합니다.

`null` 값은 반환되지 않습니다. 예를 들어 `in`과 `NOT`을 결합해 이름이 목록에 _없는_ 사용자를 반환하더라도, 이름 값이 `null`인 사용자는 반환되지 않습니다.

#

- Examples

#

#### Get `User` records where the `id` can be found in the following list: `[22, 91, 14, 2, 5]`

```
    const getUser = await prisma.user.findMany({
      where: {
        id: { in: [22, 91, 14, 2, 5] },
      },
    });
```

#

#### Get `User` records where the `name` can be found in the following list: `['Saqui', 'Clementine', 'Bob']`

```
    const getUser = await prisma.user.findMany({
      where: {
        name: { in: ["Saqui", "Clementine", "Bob"] },
      },
    });
```

#

- Get `User` records where `name` is **not** present in the list

다음 예제는 `in`과 [`NOT`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#not)을 결합합니다. [`notIn`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#notin)도 사용할 수 있습니다.

```
    const getUser = await prisma.user.findMany({
      where: {
        NOT: {
          name: { in: ["Saqui", "Clementine", "Bob"] },
        },
      },
    });
```

#

- Get a `User` record where at least one `Post` has at least one specified `Category`

```
    const getUser = await prisma.user.findMany({
      where: {
        // Find users where..
        posts: {
          some: {
            // ..at least one (some) posts..
            categories: {
              some: {
                // .. have at least one category ..
                name: {
                  in: ["Food", "Introductions"], // .. with a name that matches one of the following.
                },
              },
            },
          },
        },
      },
    });
```

- `notIn`

값 `n`이 목록에 존재하지 않습니다.

#

- Remarks
  - `null` 값은 반환되지 않습니다.

#

- Examples

#

#### Get `User` records where the `id` can **not** be found in the following list: `[22, 91, 14, 2, 5]`

```
    const getUser = await prisma.user.findMany({
      where: {
        id: { notIn: [22, 91, 14, 2, 5] },
      },
    });
```

- `lt`

값 `n`이 `x`보다 작습니다.

#

- Examples

#

- Get all `Post` records where `likes` is less than `9`

```
    const getPosts = await prisma.post.findMany({
      where: {
        likes: {
          lt: 9,
        },
      },
    });
```

- `lte`

값 `n`이 `x`보다 작거나 같습니다.

#

- Examples

#

- Get all `Post` records where `likes` is less or equal to `9`

```
    const getPosts = await prisma.post.findMany({
      where: {
        likes: {
          lte: 9,
        },
      },
    });
```

- `gt`

값 `n`이 `x`보다 큽니다.

#

- Examples

#

- Get all `Post` records where `likes` is greater than `9`

```
    const getPosts = await prisma.post.findMany({
      where: {
        likes: {
          gt: 9,
        },
      },
    });
```

- `gte`

값 `n`이 `x`보다 크거나 같습니다.

#

- Examples

#

- Get all `Post` records where `likes` is greater than or equal to `9`

```
    const getPosts = await prisma.post.findMany({
      where: {
        likes: {
          gte: 9,
        },
      },
    });
```

#

- Examples

#

- Get all `Post` records where `date_created` is greater than March 19th, 2020

```
    const result = await prisma.post.findMany({
      where: {
        date_created: {
          gte: new Date("2020-03-19T14:21:00+0200") /* Includes time offset for UTC */,
        },
      },
    });
```

- `contains`

값 `n`은 `x`를 포함합니다.

#

- 예시

#

- `content`에 `databases`가 포함된 모든 `Post` 레코드 수 계산

```
    const result = await prisma.post.count({
      where: {
        content: {
          contains: "databases",
        },
      },
    });
```

#

- `content`에 `databases`가 **포함되지 않은** 모든 `Post` 레코드 수 계산

```
    const result = await prisma.post.count({
      where: {
        NOT: {
          content: {
            contains: "databases",
          },
        },
      },
    });
```

- `search`

`String` 필드 내에서 검색하려면 [Full-Text Search](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/full-text-search)를 사용하세요.

PostgreSQL의 경우 이 기능은 아직 Preview 상태입니다. 사용하려면 [`fullTextSearchPostgres` feature flag를 활성화](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/full-text-search#enabling-full-text-search-for-postgresql)해야 합니다.

#

- 예시

#

- 제목에 `cat` 또는 `dog`가 포함된 모든 게시물 찾기

```
    const result = await prisma.post.findMany({
      where: {
        title: {
          search: "cat | dog",
        },
      },
    });
```

#

- 제목에 `cat`과 `dog`가 포함된 모든 게시물 찾기

```
    const result = await prisma.post.findMany({
      where: {
        title: {
          search: "cat & dog",
        },
      },
    });
```

#

- 제목에 `cat`이 포함되지 않은 모든 게시물 찾기

```
    const result = await prisma.post.findMany({
      where: {
        title: {
          search: "!cat",
        },
      },
    });
```

- `mode`

#

- 참고
  - PostgreSQL 및 MongoDB 커넥터에서만 지원됩니다.

#

- 예시

#

- 대소문자를 구분하지 않는 방식으로 `title`에 `prisma`가 포함된 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        title: {
          contains: "prisma",
          mode: "insensitive",
        },
      },
    });
```

- `startsWith`

#

- 예시

#

- `title`이 `Pr`(예: `Prisma`)로 시작하는 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        title: {
          startsWith: "Pr",
        },
      },
    });
```

- `endsWith`

#

- `email`이 `prisma.io`로 끝나는 모든 `User` 레코드 가져오기

```
    const result = await prisma.user.findMany({
      where: {
        email: {
          endsWith: "prisma.io",
        },
      },
    });
```

- `AND`

모든 조건이 `true`를 반환해야 합니다. 또는 `where` 절에 객체 목록을 전달할 수 있으며, 이 경우 [`AND` 연산자는 필요하지 않습니다](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-all-post-records-where-the-content-field-contains-prisma-and-published-is-false-no-and).

#

- 예시

#

- `content` 필드에 `Prisma`가 포함되고 `published`가 `false`인 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        AND: [
          {
            content: {
              contains: "Prisma",
            },
          },
          {
            published: {
              equals: false,
            },
          },
        ],
      },
    });
```

#

- `content` 필드에 `Prisma`가 포함되고 `published`가 `false`인 모든 `Post` 레코드 가져오기 (`AND` 없음)

다음 형식은 `AND` 연산자 **없이도** 이전 예시와 동일한 결과를 반환합니다:

```
    const result = await prisma.post.findMany({
      where: {
        content: {
          contains: "Prisma",
        },
        published: {
          equals: false,
        },
      },
    });
```

#

- `title` 필드에 `Prisma` 또는 `databases`가 포함되고, `published`가 `false`인 모든 `Post` 레코드 가져오기

다음 예시는 `OR`과 `AND`를 결합합니다:

```
    const result = await prisma.post.findMany({
      where: {
        OR: [
          {
            title: {
              contains: "Prisma",
            },
          },
          {
            title: {
              contains: "databases",
            },
          },
        ],
        AND: {
          published: false,
        },
      },
    });
```

- `OR`

하나 이상의 조건이 `true`를 반환해야 합니다.

#

- 예시

#

- `title` 필드에 `Prisma` 또는 `databases`가 포함된 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        OR: [
          {
            title: {
              contains: "Prisma",
            },
          },
          {
            title: {
              contains: "databases",
            },
          },
        ],
      },
    });
```

#

- `title` 필드에 `Prisma` 또는 `databases`가 포함되지만 `SQL`은 포함되지 않은 모든 `Post` 레코드 가져오기

다음 예시는 `OR`과 `NOT`을 결합합니다:

```
    const result = await prisma.post.findMany({
      where: {
        OR: [
          {
            title: {
              contains: "Prisma",
            },
          },
          {
            title: {
              contains: "databases",
            },
          },
        ],
        NOT: {
          title: {
            contains: "SQL",
          },
        },
      },
    });
```

#

- `title` 필드에 `Prisma` 또는 `databases`가 포함되고, `published`가 `false`인 모든 `Post` 레코드 가져오기

다음 예시는 `OR`과 `AND`를 결합합니다:

```
    const result = await prisma.post.findMany({
      where: {
        OR: [
          {
            title: {
              contains: "Prisma",
            },
          },
          {
            title: {
              contains: "databases",
            },
          },
        ],
        AND: {
          published: false,
        },
      },
    });
```

- `NOT`

모든 조건이 `false`를 반환해야 합니다.

#

- 예시

#

- `title`에 `SQL`이 포함되지 않은 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        NOT: {
          title: {
            contains: "SQL",
          },
        },
      },
    });
```

#

- `title` 필드에 `Prisma` 또는 `databases`가 포함되지만 `SQL`은 포함되지 않고, 관련 `User` 레코드의 이메일 주소에 `sarah`도 포함되지 않은 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        OR: [
          {
            title: {
              contains: "Prisma",
            },
          },
          {
            title: {
              contains: "databases",
            },
          },
        ],
        NOT: {
          title: {
            contains: "SQL",
          },
        },
        user: {
          NOT: {
            email: {
              contains: "sarah",
            },
          },
        },
      },
      include: {
        user: true,
      },
    });
```

## 관계 필터

- `some`

**하나 이상**("some")의 _관련_ 레코드가 필터링 기준과 일치하는 모든 레코드를 반환합니다.

#

- 참고
  - 매개변수 없이 `some`을 사용해 관계가 하나 이상 있는 모든 레코드를 반환할 수 있습니다.

#

- 예시

#

- _일부_ 게시물에서 `Prisma`를 언급하는 모든 `User` 레코드 가져오기

```
    const result = await prisma.user.findMany({
      where: {
        post: {
          some: {
            content: {
              contains: "Prisma"
            }
          }
        }
      }
    }
```

- `every`

**모든**("every") _관련_ 레코드가 필터링 기준과 일치하는 모든 레코드를 반환합니다.

#

- 예시

#

- _모든_ 게시물이 게시된 모든 `User` 레코드 가져오기

```
    const result = await prisma.user.findMany({
      where: {
        post: {
          every: {
            published: true
          },
        }
      }
    }
```

- `none`

필터링 기준과 일치하는 _관련_ 레코드가 **0개**인 모든 레코드를 반환합니다.

#

- 참고
  - 매개변수 없이 `none`을 사용해 [관계가 없는 모든 레코드](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-all-user-records-with-zero-posts)를 반환할 수 있습니다.

#

- 예시

#

- 게시물이 0개인 모든 `User` 레코드 가져오기](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#get-all-user-records-with-zero-posts)

```
    const result = await prisma.user.findMany({
      where: {
        post: {
            none: {} // User has no posts
        }
      }
    }
```

#

- 게시된 게시물이 0개인 모든 `User` 레코드 가져오기

```
    const result = await prisma.user.findMany({
      where: {
        post: {
            none: {
              published: true
            }
        }
      }
    }
```

- `is`

관련 레코드가 필터링 기준과 일치하는 모든 레코드를 반환합니다(예: 사용자 이름이 `is` Bob).

#

- 예시

#

- 사용자 이름이 `"Bob"`인 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        user: {
            is: {
              name: "Bob"
            },
        }
      }
    }
```

- `isNot`

관련 레코드가 필터링 기준과 일치하지 않는 모든 레코드를 반환합니다(예: 사용자 이름이 `isNot` Bob).

#

- 예시

#

- 사용자 이름이 `"Bob"`이 아닌 모든 `Post` 레코드 가져오기

```
    const result = await prisma.post.findMany({
      where: {
        user: {
            isNot: {
              name: "Bob"
            },
        }
      }
    }
```

## 스칼라 리스트 메서드

- `set`

스칼라 리스트 필드 값을 덮어쓰려면 `set`을 사용하세요.

#

- 참고
  - `set`은 선택 사항이며, 값을 직접 설정할 수도 있습니다:

```
tags: ["computers", "books"];
```

#

- 예시

#

- `tags` 값을 문자열 값 목록으로 설정

```
    const setTags = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: {
          set: ["computing", "books"],
        },
      },
    });
```

#

- `set` 키워드 없이 `tags`를 값 목록으로 설정

```
    const setTags = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: ["computing", "books"],
      },
    });
```

#

- `tags` 값을 단일 문자열 값으로 설정

```
    const setTags = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: {
          set: "computing",
        },
      },
    });
```

- `push`

스칼라 리스트 필드에 _하나_ 또는 *여러 개*의 값을 추가하려면 `push`를 사용하세요.

#

- 참고
  - PostgreSQL과 MongoDB에서만 사용할 수 있습니다.
  - 값 목록 또는 단일 값 하나만 추가할 수 있습니다.

#

- 예시

#

- `tags` 목록에 `computing` 항목 추가

```
    const addTag = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: {
          push: "computing",
        },
      },
    });
```

```
    const addTag = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: {
          push: ["computing", "genetics"],
        },
      },
    });
```

- `unset`

스칼라 리스트 값을 해제하려면 `unset`을 사용하세요(MongoDB 전용). `set: null`과 달리 `unset`은 리스트 자체를 완전히 제거합니다.

#

- 예시

#

- `tags` 값 해제

```
    const setTags = await prisma.post.update({
      where: {
        id: 9,
      },
      data: {
        tags: {
          unset: true,
        },
      },
    });
```

## 스칼라 리스트 필터

스칼라 리스트 필터를 사용하면 리스트 / 배열 필드의 내용으로 필터링할 수 있습니다.

PostgreSQL, CockroachDB, MongoDB에서 사용할 수 있습니다.

- 비고
  - 스칼라 리스트 / 배열 필터는 [`NULL` 값](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays#null-values-in-arrays)을 무시합니다. `isEmpty` 또는 `NOT`을 사용해도 값이 `NULL`인 리스트 / 배열 레코드는 반환되지 않으며, `{ equals: null }`는 오류를 발생시킵니다.

- `has`

지정한 값이 리스트에 존재합니다.

#

- 예시

다음 쿼리는 `tags` 리스트에 `"databases"`가 포함된 모든 `Post` 레코드를 반환합니다:

```
    const posts = await client.post.findMany({
      where: {
        tags: {
          has: "databases",
        },
      },
    });
```

다음 쿼리는 `tags` 리스트에 `"databases"`가 **포함되지 않은** 모든 `Post` 레코드를 반환합니다:

```
    const posts = await client.post.findMany({
      where: {
        NOT: {
          tags: {
            has: "databases",
          },
        },
      },
    });
```

- `hasEvery`

모든 값이 리스트에 존재합니다.

#

- 예시

다음 쿼리는 `tags` 리스트에 _최소한_ `"databases"` _그리고_ `"typescript"`가 포함된 모든 `Post` 레코드를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          hasEvery: ["databases", "typescript"],
        },
      },
    });
```

- `hasSome`

하나 이상의 값이 리스트에 존재합니다.

#

- 예시

다음 쿼리는 `tags` 리스트에 `"databases"` _또는_ `"typescript"`가 포함된 모든 `Post` 레코드를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          hasSome: ["databases", "typescript"],
        },
      },
    });
```

- `isEmpty`

리스트가 비어 있습니다.

#

- 예시

다음 쿼리는 태그가 없는 모든 `Post` 레코드를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          isEmpty: true,
        },
      },
    });
```

- `isSet`

리스트를 필터링하여 설정된 결과만 포함합니다(MongoDB 전용)(값으로 설정되었거나 `null`로 명시적으로 설정된 경우). 이 필터를 `true`로 설정하면 전혀 설정되지 않은 undefined 결과는 제외됩니다.

#

- 예시

다음 쿼리는 `tags`가 `null` 또는 어떤 값으로 설정된 모든 `Post` 레코드를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          isSet: true,
        },
      },
    });
```

- `equals`

리스트가 주어진 값과 정확히 일치합니다.

#

- 예시

다음 쿼리는 `tags` 리스트에 `"databases"`와 `"typescript"`만 포함된 모든 `Post` 레코드를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          equals: ["databases", "typescript"],
        },
      },
    });
```

## 복합 타입 메서드

복합 타입 메서드를 사용하면 [복합 타입](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types)을 생성, 업데이트, 삭제할 수 있습니다(MongoDB 전용).

- `set`

`set`을 사용해 복합 타입의 값을 덮어씁니다.

#

- 비고
  - `set` 키워드는 선택 사항이며, 값을 직접 설정할 수 있습니다:

```
photos: [
          { height: 100, width: 200, url: "1.jpg" },
          { height: 100, width: 200, url: "2.jpg" },
        ];
```

#

- 예시

#

- 새 `order` 내에서 `shippingAddress` 복합 타입 설정

```
    const order = await prisma.order.create({
      data: {
        // Normal relation
        product: { connect: { id: "some-object-id" } },
        color: "Red",
        size: "Large",
        // Composite type
        shippingAddress: {
          set: {
            street: "1084 Candycane Lane",
            city: "Silverlake",
            zip: "84323",
          },
        },
      },
    });
```

#

- 선택적 복합 타입을 `null`로 설정

```
    const order = await prisma.order.create({
      data: {
        // Embedded optional type, set to null
        billingAddress: {
          set: null,
        },
      },
    });
```

- `unset`

`unset`을 사용해 복합 타입의 값을 해제합니다. `set: null`과 달리, 이 방식은 MongoDB 문서에서 해당 필드를 완전히 제거합니다.

#

- 예시

#

- `order`에서 `billingAddress` 제거

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        billingAddress: {
          // Unset the billing address
          // Removes "billingAddress" field from order
          unset: true,
        },
      },
    });
```

- `update`

`update`를 사용해 필수 복합 타입 내부의 필드를 업데이트합니다.

#

- 비고

`update` 메서드는 선택 타입에는 사용할 수 없습니다. 대신 [upsert](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#upsert-2)를 사용하세요.

#

- 예시

#

- `shippingAddress` 복합 타입의 `zip` 필드 업데이트

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        shippingAddress: {
          // Update just the zip field
          update: {
            zip: "41232",
          },
        },
      },
    });
```

- `upsert`

`upsert`를 사용해 기존 선택적 복합 타입이 있으면 업데이트하고, 없으면 복합 타입을 설정합니다.

#

- 비고

`upsert` 메서드는 필수 타입에는 사용할 수 없습니다. 대신 [update](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#update-2)를 사용하세요.

#

- 예시

#

- `billingAddress`가 없으면 새로 만들고, 있으면 업데이트

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        billingAddress: {
          // Create the address if it doesn't exist,
          // otherwise update it
          upsert: {
            set: {
              street: "1084 Candycane Lane",
              city: "Silverlake",
              zip: "84323",
            },
            update: {
              zip: "84323",
            },
          },
        },
      },
    });
```

- `push`

`push`를 사용해 복합 타입 리스트의 끝에 값을 추가합니다.

#

- 예시

#

- `photos` 리스트에 새 사진 추가

```
    const product = prisma.product.update({
      where: {
        id: 10,
      },
      data: {
        photos: {
          // Push a photo to the end of the photos list
          push: [{ height: 100, width: 200, url: "1.jpg" }],
        },
      },
    });
```

## 복합 타입 필터

복합 타입 필터를 사용하면 [복합 타입](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types)의 내용을 필터링할 수 있습니다(MongoDB 전용).

- `equals`

`equals`를 사용해 복합 타입 또는 복합 타입 리스트와 일치하는 결과를 필터링합니다. 복합 타입의 모든 필수 필드가 일치해야 합니다.

#

- 비고

선택 필드를 매칭할 때는 문서에서 undefined(누락) 필드와 명시적으로 `null`로 설정된 필드를 구분해야 합니다.

- 선택 필드를 생략하면 undefined 필드에는 일치하지만 `null`로 설정된 필드에는 일치하지 않습니다.
- `equals: { ... exampleField: null ... }`로 선택 필드의 `null` 값을 필터링하면, 필드가 `null`로 설정된 문서에만 일치하고 undefined 필드에는 일치하지 않습니다.

`equals`를 사용할 때는 필드와 리스트의 순서가 중요합니다.

- 필드의 경우 `{ "a": "1", "b": "2" }`와 `{ "b": "2", "a": "1" }`는 동일하다고 간주되지 않습니다.
- 리스트의 경우 `[ { "a": 1 }, { "a": 2 } ]`와 `[ { "a": 2 }, { "a": 1 } ]`는 동일하다고 간주되지 않습니다.

#

- 예시

#

- 주어진 `shippingAddress`와 정확히 일치하는 주문 찾기

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          equals: {
            street: "555 Candy Cane Lane",
            city: "Wonderland",
            zip: "52337",
          },
        },
      },
    });
```

#

- `url` 목록 전체와 일치하는 사진을 가진 상품 찾기

```
    const product = prisma.product.findMany({
      where: {
        equals: {
          photos: [{ url: "1.jpg" }, { url: "2.jpg" }],
        },
      },
    });
```

- `is`

`is`를 사용해 복합 타입 내 특정 필드와 일치하는 결과를 필터링합니다.

#

- 예시

#

- 주어진 도로명과 일치하는 `shippingAddress`를 가진 주문 찾기

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          is: {
            street: "555 Candy Cane Lane",
          },
        },
      },
    });
```

- `isNot`

`isNot`을 사용해 일치하지 않는 복합 타입 필드 결과를 필터링합니다.

#

- 예시

#

- 주어진 우편번호와 일치하지 않는 `shippingAddress`를 가진 주문 찾기

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          isNot: {
            zip: "52337",
          },
        },
      },
    });
```

- `isEmpty`

`isEmpty`를 사용해 빈 복합 타입 리스트 결과를 필터링합니다.

#

- 예시

#

- 사진이 없는 상품 찾기

```
    const product = prisma.product.findMany({
      where: {
        photos: {
          isEmpty: true,
        },
      },
    });
```

- `every`

`every`를 사용해 리스트의 모든 항목이 조건과 일치하는 복합 타입 리스트를 필터링합니다.

#

- 예시

#

- 모든 사진의 `height`가 `200`인 첫 번째 상품 찾기

```
    const product = await prisma.product.findFirst({
      where: {
        photos: {
          every: {
            height: 200,
          },
        },
      },
    });
```

- `some`

`some`을 사용해 리스트에서 하나 이상의 항목이 조건과 일치하는 복합 타입 리스트를 필터링합니다.

#

- 예시

#

- 하나 이상의 사진 `url`이 `2.jpg`인 첫 번째 상품 찾기

```
    const product = await prisma.product.findFirst({
      where: {
        photos: {
          some: {
            url: "2.jpg",
          },
        },
      },
    });
```

- `none`

`none`을 사용해 리스트의 어떤 항목도 조건과 일치하지 않는 복합 타입 리스트를 필터링합니다.

#

- 예시

#

- 어떤 사진도 `url`이 `2.jpg`가 아닌 첫 번째 상품 찾기

```
    const product = await prisma.product.findFirst({
      where: {
        photos: {
          none: {
            url: "2.jpg",
          },
        },
      },
    });
```

## 원자적 숫자 연산

업데이트 시 원자적 연산은 숫자 필드 타입(`Float`, `Int`)에서 사용할 수 있습니다. 이 기능을 사용하면 레이스 컨디션 위험 없이 (**현재** 값을 기준으로) 필드를 업데이트할 수 있습니다(예: _빼기_, _나누기_).

개요: 레이스 컨디션

레이스 컨디션은 작업을 완료하기 위해 둘 이상의 연산을 순서대로 수행해야 할 때 발생합니다. 다음 예시에서는 두 클라이언트가 같은 필드(`postCount`)를 1씩 증가시키려고 합니다.

| Client   | Operation            | Value |
| -------- | -------------------- | ----- |
| Client 1 | **가져오기** 필드 값 | `21`  |

Client 2| 필드 값 **가져오기**| `21`
Client 2| 필드 값 **설정**| `22`
Client 1| 필드 값 **설정**| `22` ✘

값은 `23`이어야 _하지만_, 두 클라이언트가 `postCount` 필드를 순차적으로 읽고 쓰지 않았습니다. 업데이트 시 원자적 연산은 읽기와 쓰기를 하나의 작업으로 결합하므로 경쟁 상태를 방지합니다.

| Client   | 작업                        | 값            |
| -------- | --------------------------- | ------------- |
| Client 1 | 필드 값을 **가져오고 설정** | `21` → `22`   |
| Client 2 | 필드 값을 **가져오고 설정** | `22` → `23` ✔ |

- 연산자

| 옵션        | 설명                                                       |
| ----------- | ---------------------------------------------------------- |
| `increment` | 현재 값에 `n`을 더합니다.                                  |
| `decrement` | 현재 값에서 `n`을 뺍니다.                                  |
| `multiply`  | 현재 값에 `n`을 곱합니다.                                  |
| `divide`    | 현재 값을 `n`으로 나눕니다.                                |
| `set`       | 현재 필드 값을 설정합니다. `{ myField : n }`와 동일합니다. |

- 참고 사항
  - 필드당, 쿼리당 **하나의** 원자적 업데이트만 수행할 수 있습니다.
  - 필드가 `null`이면 `increment`, `decrement`, `multiply`, `divide`로 업데이트되지 않습니다.

- 예제

#

- 모든 `Post` 레코드의 `view` 및 `likes` 필드를 `1`씩 증가시키기

```
    const updatePosts = await prisma.post.updateMany({
      data: {
        views: {
          increment: 1,
        },
        likes: {
          increment: 1,
        },
      },
    });
```

#

- 모든 `Post` 레코드의 `views` 필드를 `0`으로 설정하기

```
    const updatePosts = await prisma.post.updateMany({
      data: {
        views: {
          set: 0,
        },
      },
    });
```

다음과 같이도 작성할 수 있습니다:

```
    const updatePosts = await prisma.post.updateMany({
      data: {
        views: 0,
      },
    });
```

## `Json` 필터

사용 사례와 고급 예제는 다음을 참고하세요: [Working with `Json` fields](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields).

`path` 옵션의 문법이 서로 다른 [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) 및 [MySQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)에서 지원됩니다. PostgreSQL은 배열 내 객체 키 값에 대한 필터링을 지원하지 않습니다.

이 섹션의 예제는 `pet` 필드 값이 다음과 같다고 가정합니다:

```
    {
      "favorites": {
        "catBreed": "Turkish van",
        "dogBreed": "Rottweiler",
        "sanctuaries": ["RSPCA", "Alley Cat Allies"],
        "treats": [
          { "name": "Dreamies", "manufacturer": "Mars Inc" },
          { "name": "Treatos", "manufacturer": "The Dog People" }
        ]
      },
      "fostered": {
        "cats": ["Bob", "Alice", "Svetlana the Magnificent", "Queenie"]
      },
      "owned": {
        "cats": ["Elliott"]
      }
    }
```

- 참고 사항
  - `Json` 필터링 구현은 [데이터베이스 커넥터마다 다릅니다](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields)
  - PostgreSQL의 필터링은 대소문자를 구분하며 아직 `mode`를 지원하지 않습니다

- `path`

`path`는 특정 키의 위치를 나타냅니다. 다음 쿼리는 중첩된 `favorites` > `dogBreed` 키가 `"Rottweiler"`와 같은 모든 사용자를 반환합니다.

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["favorites", "dogBreed"],
          equals: "Rottweiler",
        },
      },
    });
```

다음 쿼리는 중첩된 `owned` > `cats` 배열에 `"Elliott"`가 포함된 모든 사용자를 반환합니다.

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["owned", "cats"],
          array_contains: ["Elliott"],
        },
      },
    });
```

배열 내부 객체의 키 값으로 필터링하는 기능(아래)은 MySQL 커넥터에서만 지원됩니다.

다음 쿼리는 중첩된 `favorites` > `treats` 배열에 `name` 값이 `"Dreamies"`인 객체가 포함된 모든 사용자를 반환합니다:

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: "$.favorites.treats[*].name",
          array_contains: "Dreamies",
        },
      },
    });
```

- `string_contains`

다음 쿼리는 중첩된 `favorites` > `catBreed` 키 값에 `"Van"`이 포함된 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["favorites", "catBreed"],
          string_contains: "Van",
        },
      },
    });
```

- `string_starts_with`

다음 쿼리는 중첩된 `favorites` > `catBreed` 키 값이 `"Turkish"`로 시작하는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["favorites", "catBreed"],
          string_starts_with: "Turkish",
        },
      },
    });
```

- `string_ends_with`

다음 쿼리는 중첩된 `favorites` > `catBreed` 키 값이 `"Van"`으로 끝나는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["favorites", "catBreed"],
          string_ends_with: "Van",
        },
      },
    });
```

- `mode`

문자열 필터링을 대소문자 구분(기본값)으로 할지, 대소문자 비구분으로 할지 지정합니다.

다음 쿼리는 중첩된 `favorites` > `catBreed` 키 값에 `"Van"` 또는 `"van"`이 포함된 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["favorites", "catBreed"],
          string_contains: "Van",
          mode: "insensitive",
        },
      },
    });
```

- `array_contains`

다음 쿼리는 `sanctuaries` 배열에 `"RSPCA"` 값이 포함된 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["sanctuaries"],
          array_contains: ["RSPCA"],
        },
      },
    });
```

PostgreSQL에서는 `array_contains` 값이 문자열이 아니라 배열이어야 하며, 배열에 값이 하나만 있어도 동일합니다.

다음 쿼리는 `sanctuaries` 배열에 주어진 배열의 값이 _모두_ 포함된 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["sanctuaries"],
          array_contains: ["RSPCA", "Alley Cat Allies"],
        },
      },
    });
```

- `array_starts_with`

다음 쿼리는 `sanctuaries` 배열이 `"RSPCA"` 값으로 시작하는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["sanctuaries"],
          array_starts_with: "RSPCA",
        },
      },
    });
```

- `array_ends_with`

다음 쿼리는 `sanctuaries` 배열이 `"Alley Cat Allies"` 값으로 끝나는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        pets: {
          path: ["sanctuaries"],
          array_ends_with: "Alley Cat Allies",
        },
      },
    });
```

## 클라이언트 메서드

**참고:** Client 레벨 메서드는 `$` 접두사를 사용합니다.

- 참고 사항
  - [`$extends`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#extends)를 사용해 확장한 클라이언트 인스턴스에는 `$on` 및 `$use` 클라이언트 메서드가 존재하지 않습니다

[확장된 클라이언트](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)에서는 Client 메서드가 반드시 존재하지는 않습니다. 클라이언트를 확장하는 경우 `$transaction` 또는 `$connect` 같은 Client 메서드를 사용하기 전에 존재 여부를 확인하세요.

또한 `$on` 또는 `$use`를 사용하는 경우, 이러한 메서드는 확장된 클라이언트에 존재하지 않으므로 클라이언트를 확장하기 전에 사용해야 합니다. 특히 `$use`의 경우 [query extensions 사용으로 전환](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query)할 것을 권장합니다.

- `$disconnect()`

`$disconnect()` 메서드는 `$connect` 호출 시 설정된 데이터베이스 연결을 닫고 Prisma ORM의 쿼리 엔진이 실행하던 프로세스를 중지합니다. `$connect()`와 `$disconnect()` 개요는 [Connection management](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management)를 참고하세요.

#

- 참고 사항
  - `$disconnect()`는 `Promise`를 반환하므로 `await` 키워드와 함께 `async` 함수 내부에서 호출해야 합니다.

- `$connect()`

`$connect()` 메서드는 Prisma ORM의 쿼리 엔진을 통해 데이터베이스에 물리적 연결을 설정합니다. `$connect()`와 `$disconnect()` 개요는 [Connection management](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management)를 참고하세요.

#

- 참고 사항
  - `$connect()`는 `Promise`를 반환하므로 `await` 키워드와 함께 `async` 함수 내부에서 호출해야 합니다.

- `$on()`

`$on`은 [확장된 클라이언트](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)에서 사용할 수 없습니다. 클라이언트 확장으로 마이그레이션하거나, 클라이언트를 확장하기 전에 `$on` 메서드를 사용하세요.

`$on()` 메서드를 사용하면 [logging events](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#log) 또는 [exit hook](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#exit-hooks)을 구독할 수 있습니다.

- `$queryRawTyped`

참고: [Using Raw SQL (`$queryRawTyped`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql).

- `$queryRaw`

참고: [Using Raw SQL (`$queryRaw`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryraw).

- `$queryRawUnsafe()`

참고: [Using Raw SQL (`$queryRawUnsafe()`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryrawunsafe).

- `$executeRaw`

참고: [Using Raw SQL (`$executeRaw`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#executeraw).

- `$executeRawUnsafe()`

참고: [Using Raw SQL (`$executeRawUnsafe()`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#executerawunsafe).

- `$runCommandRaw()`

참고: [Using Raw SQL (`$runCommandRaw()`)](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#runcommandraw).

- `$transaction()`

참고: [Transactions](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions).

- `$extends`

`$extends`를 사용하면 Prisma Client 확장을 생성하고 사용하여 다음 방식으로 Prisma Client에 기능을 추가할 수 있습니다:

- `model`: 모델에 사용자 정의 메서드 추가
- `client`: 클라이언트에 사용자 정의 메서드 추가
- `query`: 사용자 정의 Prisma Client 쿼리 생성
- `result`: 쿼리 결과에 사용자 정의 필드 추가

자세히 보기: [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions).

## 유틸리티 타입

유틸리티 타입은 `Prisma` 네임스페이스에 있는 도우미 함수 및 타입입니다. 애플리케이션의 타입 안정성을 유지하는 데 유용합니다.

- `satisfies`를 사용한 타입 검사

TypeScript의 `satisfies` 연산자를 사용하면 스키마 모델을 기반으로 재사용 가능한 쿼리 파라미터를 만들면서, 생성한 객체가 생성된 Prisma Client 타입과 타입 호환되도록 보장할 수 있습니다. 함께 참고: [Type safety with Prisma Client](https://docs.prisma.io/docs/orm/prisma-client/type-safety).

생성된 Prisma Client 타입을 `satisfies`와 함께 사용해 타입 검사와 추론을 얻을 수 있습니다:

```
    const args = { ... } satisfies Prisma.GeneratedType;
```

#

- 예제

다음 예제는 앱 내에서 재사용할 수 있는 `create` 작업용 타입 검증 입력을 만드는 방법을 보여줍니다:

```
    import { Prisma } from "../prisma/generated/client";

    const createUserAndPostInput = (
      name: string,
      email: string,
      postTitle: string,
    ) =>
      ({
        name,
        email,
        posts: {
          create: {
            title: postTitle,
          },
        },
      }) satisfies Prisma.UserCreateInput;
```

## 같은 테이블의 컬럼 비교

비고유 필터의 경우 같은 테이블의 컬럼을 직접 비교할 수 있습니다.

다음 상황에서는 [raw queries를 사용해 같은 테이블의 컬럼을 비교](https://docs.prisma.io/docs/orm/more/troubleshooting/raw-sql-comparisons)해야 합니다:

- [`findUnique`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findunique) 또는 [`findUniqueOrThrow`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#finduniqueorthrow) 같은 고유 필터를 사용하려는 경우
  - [고유 제약 조건](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-unique-field)이 있는 필드를 비교하려는 경우
  - MySQL 또는 MariaDB에서 [JSON field](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields)를 다른 필드와 비교할 때, 다음 연산자 중 하나를 사용하려는 경우: [`gt`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#gt), [`gte`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#gte), [`lt`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#lt), 또는 [`lte`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#lte). 이 연산자들은 JSON field를 스칼라 값과 비교할 때는 사용할 수 있습니다. 이 제한은 JSON field를 다른 필드와 비교하려고 할 때에만 적용됩니다.

같은 테이블 내에서 컬럼을 비교하려면 `<model>.fields` 속성을 사용하세요. 다음 예제에서 쿼리는 `prisma.product.quantity` 필드 값이 `prisma.product.warnQuantity` 필드 값보다 작거나 같은 모든 레코드를 반환합니다.

```
    prisma.product.findMany({
      where: { quantity: { lte: prisma.product.fields.warnQuantity } },
    });
```

`fields`는 모든 모델의 특수 속성입니다. 해당 모델의 필드 목록을 포함합니다.

- 고려 사항

#

- 필드는 동일한 타입이어야 합니다

비교는 동일한 타입의 필드끼리만 할 수 있습니다. 예를 들어, 다음은 오류를 발생시킵니다:

```
    await prisma.order.findMany({
      where: {
        id: { equals: prisma.order.fields.due },
        // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        // Type error: id is a string, while amountDue is an integer
      },
    });
```

#

- 필드는 동일한 모델에 있어야 합니다

`fields` 속성을 사용한 비교는 같은 모델의 필드에 대해서만 가능합니다. 다음 예제는 동작하지 않습니다:

```
    await prisma.order.findMany({
      where: {
        id: { equals: prisma.user.fields.name },
        // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        // Type error: name is a field on the User model, not Order
      },
    });
```

하지만 [표준 쿼리](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#model-queries)를 사용하면 서로 다른 모델의 필드를 비교할 수 있습니다.

#

- `groupBy` 모델 쿼리에서는 참조하는 필드를 `by` 인자에 넣어야 합니다

`having` 옵션과 함께 [groupBy](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#groupby) 모델 쿼리를 사용하는 경우, 참조하는 필드를 반드시 `by` 인자에 포함해야 합니다.

다음 예제는 동작합니다:

```
    prisma.user.groupBy({
      by: ["id", "name"],
      having: { id: { equals: prisma.user.fields.name } },
    });
```

다음 예제는 `name`이 `by` 인자에 없기 때문에 동작하지 않습니다:

```
    prisma.user.groupBy({
      by: ["id"],
      having: { id: { equals: prisma.user.fields.name } },
      // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      // name is not in the 'by' argument
    });
```

#

- 스칼라 리스트에서 필드 검색

데이터 소스가 스칼라 리스트를 지원한다면(예: PostgreSQL), 특정 필드 값이 필드 리스트 안에 있는 모든 레코드를 검색할 수 있습니다. 이를 위해 스칼라 리스트를 [`in`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#in) 및 [`notIn`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#notin) 필터로 참조하세요. 예:

```
    await prisma.user.findMany({
      where: {
        // find all users where 'name' is in a list of tags
        name: { in: prisma.user.fields.tags },
      },
    });
```

## `UserWhereUniqueInput`으로 비고유 필드 필터링

[`where`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#where)의 생성 타입인 `UserWhereUniqueInput`은 고유 필드뿐 아니라 모델의 모든 필드를 노출합니다.

`where` 문에서는 [불리언 연산자](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#boolean-operators-with-userwhereuniqueinput) 바깥에 최소 하나의 고유 필드를 지정해야 하며, 추가로 원하는 수만큼 고유/비고유 필드를 지정할 수 있습니다. 이를 통해 단일 레코드를 반환하는 모든 연산에 필터를 추가할 수 있습니다. 예를 들어 다음과 같은 용도로 사용할 수 있습니다:

- 업데이트 시 낙관적 동시성 제어
- 권한 확인
- 소프트 삭제
- 선택적 [one-to-one nested reads](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads)에서 필터링

* 업데이트 시 낙관적 동시성 제어

`update` 작업에서 [optimistic concurrency control](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#optimistic-concurrency-control)을 수행하기 위해 비고유 필드로 필터링할 수 있습니다.

낙관적 동시성 제어를 수행하려면 `version` 필드를 사용해 코드 실행 중 레코드(또는 관련 레코드)의 데이터가 변경되었는지 확인합니다.

다음 예제에서 `updateOne`과 `updateTwo`는 먼저 같은 레코드를 읽고 그다음 업데이트를 시도합니다. 데이터베이스는 초기 읽기 시점과 `version` 값이 같을 때만 업데이트를 실행합니다. 이 업데이트들 중 첫 번째(`updateOne` 또는 `updateTwo`, 타이밍에 따라 다름)를 실행하면 데이터베이스가 `version` 값을 증가시킵니다. 따라서 두 번째 업데이트는 `version` 값이 이미 변경되었기 때문에 실행되지 않습니다.

```
    model User {
      id      Int    @id @default(autoincrement())
      email   String @unique
      city    String
      version Int
    }
```

```
    function updateOne() {
      const user = await prisma.user.findUnique({ id: 1 });

      await prisma.user.update({
        where: { id: user.id, version: user.version },
        data: { city: "Berlin", version: { increment: 1 } },
      });
    }

    function updateTwo() {
      const user = await prisma.user.findUnique({ id: 1 });

      await prisma.user.update({
        where: { id: user.id, version: user.version },
        data: { city: "New York", version: { increment: 1 } },
      });
    }

    function main() {
      await Promise.allSettled([updateOne(), updateTwo()]);
    }
```

- 권한 확인

업데이트 중 권한을 확인하기 위해 비고유 필드로 필터링할 수 있습니다.

다음 예제에서 사용자는 게시물 제목을 수정하려고 합니다. `where` 문은 `authorId` 값을 확인해 사용자가 게시물 작성자인지 검증합니다. 애플리케이션은 사용자가 게시물 작성자인 경우에만 제목을 업데이트합니다.

```
    await prisma.post.update({
      where: { id: 1, authorId: 1 },
      data: { title: "Updated post title" },
    });
```

- 소프트 삭제

소프트 삭제를 처리하기 위해 비고유 필드로 필터링할 수 있습니다.

다음 예제에서는 게시물이 소프트 삭제된 경우 반환하지 않으려고 합니다. 이 작업은 `isDeleted` 값이 `false`일 때만 게시물을 반환합니다.

```
    prisma.Post.findUnique({ where: { id: postId, isDeleted: false } });
```

- `UserWhereUniqueInput` 고려 사항

#

- `UserWhereUniqueInput`과 불리언 연산자

`UserWhereUniqueInput`에서는 불리언 연산자 `AND`, `OR`, `NOT` 바깥에 최소 하나의 고유 필드를 지정해야 합니다. 그래도 필터에서 다른 고유 필드 또는 비고유 필드와 함께 이 불리언 연산자들을 사용할 수 있습니다.

다음 예제에서는 고유 필드인 `id`를 `email`과 함께 검사하며, 이는 유효합니다.

```
    await prisma.user.update({
      where: { id: 1, OR: [{ email: "bob@prisma.io" }, { email: "alice@prisma.io" }] },
            // ^^^ Valid: the expression specifies a unique field (`id`) outside of any boolean operators
      data: { ... }
    })

    // SQL equivalent:
    // WHERE id = 1 AND (email = "bob@prisma.io" OR email = "alice@prisma.io")
```

다음 예제는 어떤 불리언 연산자 바깥에도 고유 필드가 없기 때문에 유효하지 않습니다:

```
    await prisma.user.update({
      where: { OR: [{ email: "bob@prisma.io" }, { email: "alice@prisma.io" }] },
            // ^^^ Invalid: the expressions does not contain a unique field outside of boolean operators
      data: { ... }
    })
```

#

- 일대일 관계

다음 [one-to-one relations](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations) 작업에서는 비고유 필드로 필터링할 수 있습니다:

- Nested update
- Nested upsert
- Nested disconnect
- Nested delete

Prisma Client는 적절한 관련 레코드를 선택하기 위해 자동으로 고유 필터를 사용합니다. 따라서 `where` 문에서 `WhereUniqueInput` [generated type](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#generated-types-for-where)으로 고유 필터를 직접 지정할 필요가 없습니다. 대신 `where` 문은 `WhereInput` 생성 타입을 가집니다. 이를 사용하면 `WhereUniqueInput`의 제한 없이 필터링할 수 있습니다.

#

- Nested update 예제

```
    await prisma.user.update({
      where: { id: 1 },
      data: {
        to_one: {
          update: { where: { /* WhereInput */ }, data: { field: "updated" } }
        }
      }
    })
```

#

- Nested upsert 예제

```
    await prisma.user.update({
      where: { id: 1 },
      data: {
        to_one: {
          upsert: {
            where: { /* WhereInput */ },
            create: { /* CreateInput */ },
            update: { /* UpdateInput */ },
          }
        }
      }
    })
```

#

- Nested disconnect 예제

```
    await prisma.user.update({
      where: { id: 1 },
      data: {
        to_one: {
          disconnect: { /* WhereInput */ }
        }
      }
    })
```

#

- Nested delete 예제

```
    await prisma.user.update({
      where: { id: 1 },
      data: {
        to_one: {
          delete: { /* WhereInput */ }
        }
      }
    })
```

## `PrismaPromise` 동작

모든 Prisma Client 쿼리는 `PrismaPromise` 인스턴스를 반환합니다. 이것은 ["thenable"](https://masteringjs.io/tutorials/fundamentals/thenable)이므로, `PrismaPromise`는 `await`, `.then()`, 또는 `.catch()`를 호출할 때에만 실행됩니다. 이 동작은 즉시 실행을 시작하는 일반 JavaScript [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)와 다릅니다.

예:

```
    const findPostOperation = prisma.post.findMany({}); // Query not yet executed

    findPostOperation.then(); // Prisma Client now executes the query
    // or
    await findPostOperation; // Prisma Client now executes the query
```

[`$transaction` API](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#the-transaction-api)를 사용할 때, 이 동작 덕분에 Prisma Client는 모든 쿼리를 단일 트랜잭션으로 쿼리 엔진에 전달할 수 있습니다.
