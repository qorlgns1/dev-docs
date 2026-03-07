---
title: "TypedSQL"
description: "TypedSQL을 사용해 어떤 SQL 콘솔과도 호환되는 완전한 타입 안전 SQL 쿼리를 작성하고 Prisma Client에서 활용하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql

# TypedSQL

TypedSQL을 사용해 어떤 SQL 콘솔과도 호환되는 완전한 타입 안전 SQL 쿼리를 작성하고 Prisma Client에서 활용하는 방법을 알아보세요.

## TypedSQL 시작하기

Prisma 프로젝트에서 TypedSQL을 사용하려면 다음 단계를 따르세요:

1. `@prisma/client`와 `prisma`가 설치되어 있는지 확인합니다:

npm

pnpm

yarn

bun

```
npm install @prisma/client@latest
         npm install -D prisma@latest
```

2. `schema.prisma` 파일에 `typedSql` 프리뷰 기능 플래그를 추가합니다:

```
generator client {
          provider = "prisma-client"
          previewFeatures = ["typedSql"]
          output = "../src/generated/prisma"
         }
```

TypedSQL과 함께 드라이버 어댑터 사용하기

Prisma를 serverless 또는 edge 환경에 배포하는 경우, [driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 사용해 JavaScript 데이터베이스 드라이버를 통해 연결할 수 있습니다. 드라이버 어댑터는 TypedSQL과 호환되지만 `@prisma/adapter-better-sqlite3`는 예외입니다. SQLite를 지원하려면 대신 [`@prisma/adapter-libsql`](https://www.npmjs.com/package/@prisma/adapter-libsql)을 사용하세요. 그 외 모든 드라이버 어댑터는 지원됩니다.

3. `prisma` 디렉터리 안에 `sql` 디렉터리를 생성합니다. 여기에 SQL 쿼리를 작성하게 됩니다.

```
mkdir -p prisma/sql
```

사용자 지정 SQL 폴더 위치

Prisma 6.12.0부터는 Prisma config 파일을 사용해 SQL 파일의 사용자 지정 위치를 설정할 수 있습니다. 프로젝트 루트에 `prisma.config.ts` 파일을 만들고 `typedSql.path` 옵션을 지정하세요:

prisma.config.ts

```
import "dotenv/config";
         import { defineConfig } from "prisma/config";

         export default defineConfig({
           schema: "./prisma/schema.prisma",
           typedSql: {
             path: "./prisma/sql",
           },
         });
```

4. `prisma/sql` 디렉터리에 새 `.sql` 파일을 생성합니다. 예를 들어 `getUsersWithPosts.sql`입니다. 파일 이름은 유효한 JS 식별자여야 하며 `$`로 시작할 수 없습니다.

5. 새 `.sql` 파일에 SQL 쿼리를 작성합니다. 예:

prisma/sql/getUsersWithPosts.sql

```
SELECT u.id, u.name, COUNT(p.id) as "postCount"
         FROM "User" u
         LEFT JOIN "Post" p ON u.id = p."authorId"
         GROUP BY u.id, u.name
```

6. SQL 쿼리에 대한 TypeScript 함수와 타입이 생성되도록 `sql` 플래그를 사용해 Prisma Client를 생성합니다:

`sql` 플래그로 client를 생성하기 전에 대기 중인 migration이 모두 적용되었는지 확인하세요.

```
prisma generate --sql
```

변경할 때마다 client를 다시 생성하고 싶지 않다면, 기존 `--watch` 플래그와 함께 이 명령도 사용할 수 있습니다:

```
prisma generate --sql --watch
```

7. 이제 TypeScript 코드에서 SQL 쿼리를 import하여 사용할 수 있습니다:

/src/index.ts

```
    import { PrismaClient } from "./generated/prisma/client";
    import { getUsersWithPosts } from "./generated/prisma/sql";

    const prisma = new PrismaClient();

    const usersWithPostCounts = await prisma.$queryRawTyped(getUsersWithPosts());
    console.log(usersWithPostCounts);
```

generator `output`을 사용자 지정하지 않았다면, 대신 `@prisma/client`와 `@prisma/client/sql`에서 import할 수 있습니다.

## TypedSQL 쿼리에 인수 전달하기

TypedSQL 쿼리에 인수를 전달하려면 parameterized query를 사용할 수 있습니다. 이렇게 하면 타입 안전성을 유지하면서 유연하고 재사용 가능한 SQL 문을 작성할 수 있습니다. 방법은 다음과 같습니다:

1. SQL 파일에서 전달할 파라미터에 플레이스홀더를 사용합니다. 플레이스홀더 문법은 데이터베이스 엔진에 따라 다릅니다:

PostgreSQL에서는 위치 기반 플레이스홀더 `$1`, `$2` 등을 사용합니다. MySQL에서는 `?`를 사용합니다. SQLite에서는 위치 기반(`$1`, `$2`), 일반(`?`), 또는 이름 기반 플레이스홀더(`:minAge`, `:maxAge`)를 사용할 수 있습니다:

PostgreSQL

MySQL

SQLite

prisma/sql/getUsersByAge.sql

```
    SELECT id, name, age
    FROM users
    WHERE age > $1 AND age < $2
```

SQL 파일에서 [인수 타입을 정의하는 방법](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql#defining-argument-types-in-your-sql-files)은 아래를 참고하세요.

1. TypeScript 코드에서 생성된 함수를 사용할 때는 인수를 `$queryRawTyped`에 추가 파라미터로 전달합니다:

/src/index.ts

```
    import { PrismaClient } from "./generated/prisma/client";
    import { getUsersByAge } from "./generated/prisma/sql";

    const prisma = new PrismaClient();

    const minAge = 18;
    const maxAge = 30;
    const users = await prisma.$queryRawTyped(getUsersByAge(minAge, maxAge));
    console.log(users);
```

parameterized query를 사용하면 타입 안전성을 확보하고 SQL 인젝션 취약점으로부터 보호할 수 있습니다. TypedSQL generator는 SQL 쿼리를 기반으로 파라미터에 맞는 TypeScript 타입을 생성하므로, 쿼리 결과와 입력 파라미터 모두에 대해 완전한 타입 검사를 제공합니다.

- TypedSQL에 배열 인수 전달하기

TypedSQL은 PostgreSQL에서 배열 인수 전달을 지원합니다. 배열 파라미터와 함께 PostgreSQL의 `ANY` 연산자를 사용하세요.

prisma/sql/getUsersByIds.sql

```
    SELECT id, name, email
    FROM users
    WHERE id = ANY($1)
```

/src/index.ts

```
    import { PrismaClient } from "./generated/prisma/client";
    import { getUsersByIds } from "./generated/prisma/sql";

    const prisma = new PrismaClient();

    const userIds = [1, 2, 3];
    const users = await prisma.$queryRawTyped(getUsersByIds(userIds));
    console.log(users);
```

TypedSQL은 배열 파라미터에 대해 적절한 TypeScript 타입을 생성하여, 입력과 쿼리 결과 모두의 타입 안전성을 보장합니다.

배열 인수를 전달할 때는 데이터베이스가 단일 쿼리에서 지원하는 최대 플레이스홀더 수를 유의하세요. 배열이 매우 큰 경우 쿼리를 더 작은 여러 쿼리로 분할해야 할 수 있습니다.

- SQL 파일에서 인수 타입 정의하기

TypedSQL에서 인수 타입 지정은 SQL 파일 내의 특정 주석으로 수행됩니다. 주석 형식은 다음과 같습니다:

```
    -- @param {Type} $N:alias optional description
```

여기서 `Type`은 유효한 데이터베이스 타입이고, `N`은 쿼리에서 인수의 위치이며, `alias`는 TypeScript 타입에서 사용되는 선택적 인수 별칭입니다.

예를 들어, `name`이라는 별칭과 "The name of the user"라는 설명으로 단일 문자열 인수를 타입 지정해야 한다면 SQL 파일에 다음 주석을 추가합니다:

```
    -- @param {String} $1:name The name of the user
```

파라미터가 nullable임을 나타내려면 별칭 뒤에 물음표를 추가하세요:

```
    -- @param {String} $1:name? The name of the user (optional)
```

현재 허용되는 타입은 `Int`, `BigInt`, `Float`, `Boolean`, `String`, `DateTime`, `Json`, `Bytes`, `null`, `Decimal`입니다.

[위의 예시](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql#passing-arguments-to-typedsql-queries)를 적용하면 SQL 파일은 다음과 같습니다:

```
    -- @param {Int} $1:minAge
    -- @param {Int} $2:maxAge
    SELECT id, name, age
    FROM users
    WHERE age > $1 AND age < $2
```

인수 타입 정의 형식은 데이터베이스 엔진과 관계없이 동일합니다.

배열 인수에 대해서는 수동 인수 타입 정의가 지원되지 않습니다. 이러한 인수는 TypedSQL이 제공하는 타입 추론에 의존해야 합니다.

## 예시

TypedSQL 사용에 대한 실용적인 예시는 [Prisma Examples 저장소의 TypedSQL 예시](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/basic-typedsql)를 참고하세요.

## TypedSQL의 제한 사항

- 지원 데이터베이스

TypedSQL은 추가 설정 없이 최신 버전의 MySQL과 PostgreSQL을 지원합니다. MySQL 8.0 미만 버전과 모든 SQLite 버전에서는 SQL 파일에서 [인수 타입을 수동으로 설명](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql#defining-argument-types-in-your-sql-files)해야 합니다. 입력 타입은 지원되는 모든 PostgreSQL 버전과 MySQL 8.0 이상에서 추론됩니다.

TypedSQL은 SQL 데이터베이스용으로 특별히 설계되었기 때문에 MongoDB에서는 동작하지 않습니다.

- 활성 데이터베이스 연결 필요

TypedSQL이 올바르게 동작하려면 활성 데이터베이스 연결이 필요합니다. 즉, `--sql` 플래그로 client를 생성할 때 Prisma가 연결할 수 있는 실행 중인 데이터베이스 인스턴스가 있어야 합니다. TypedSQL은 이 연결을 설정하기 위해 `prisma.config.ts`의 연결 문자열(`datasource.url`)을 사용합니다.

- 동적 컬럼을 사용하는 동적 SQL 쿼리

TypedSQL은 동적으로 컬럼을 추가해 SQL 쿼리를 구성하는 방식을 기본적으로 지원하지 않습니다. 런타임에 컬럼이 결정되는 쿼리를 만들어야 할 때는 `$queryRaw`와 `$executeRaw` 메서드를 사용해야 합니다. 이 메서드들은 동적 컬럼 선택을 포함한 raw SQL 실행을 허용합니다.

**동적 컬럼 선택을 사용하는 쿼리 예시:**

```
    const columns = "name, email, age"; // Columns determined at runtime
    const result = await prisma.$queryRawUnsafe(`SELECT ${columns} FROM Users WHERE active = true`);
```

이 예시에서는 선택할 컬럼이 동적으로 정의되어 SQL 쿼리에 포함됩니다. 이 접근 방식은 유연성을 제공하지만, 특히 [SQL 인젝션 취약점 방지](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention)를 위해 보안에 각별히 주의해야 합니다. 또한 raw SQL 쿼리를 사용하면 TypedSQL의 타입 안전성과 DX를 포기하게 됩니다.

## 감사의 말

이 기능은 [PgTyped](https://github.com/adelsz/pgtyped)와 [SQLx](https://github.com/launchbadge/sqlx)에서 큰 영감을 받았습니다. 또한 SQLite 파싱은 SQLx가 처리합니다.
