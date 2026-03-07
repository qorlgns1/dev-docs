---
title: "views 프리뷰 기능 활성화"
description: "Prisma 스키마에 뷰를 포함하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/views

# 뷰

Prisma 스키마에 뷰를 포함하는 방법

데이터베이스 뷰를 사용하면 쿼리에 이름을 지정하고 저장할 수 있습니다. 관계형 데이터베이스에서 뷰는 여러 테이블의 컬럼이나 집계 같은 계산된 값을 포함할 수 있는 [저장된 SQL 쿼리](https://www.postgresql.org/docs/current/sql-createview.html)입니다. MongoDB에서 뷰는 다른 컬렉션에 대한 [aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline)으로 내용이 정의되는 쿼리 가능한 객체입니다.

`views` 프리뷰 기능을 사용하면 Prisma 스키마에서 `view` 키워드로 뷰를 표현할 수 있습니다. Prisma ORM에서 뷰를 사용하려면 다음 단계를 따르세요.

1. `views` 프리뷰 기능 활성화
2. 기본 데이터베이스에 뷰 생성(직접 생성하거나 [Prisma Migrate 마이그레이션 파일에 수동으로 추가](https://docs.prisma.io/docs/orm/prisma-schema/data-model/views#use-views-with-prisma-migrate-and-db-push), 또는 기존 뷰 사용) [(기본 데이터베이스에 뷰 생성)](https://docs.prisma.io/docs/orm/prisma-schema/data-model/views#create-a-view-in-the-underlying-database)
3. Prisma 스키마에 뷰 표현
4. Prisma Client에서 뷰 쿼리

뷰 지원은 현재 [Preview](https://docs.prisma.io/docs/orm/more/releases#preview) 기능입니다. `view` 키워드로 Prisma 스키마에 뷰를 추가하거나 `db pull`로 데이터베이스 스키마의 뷰를 introspect할 수 있습니다. 아직은 `--create-only` 플래그를 사용해 마이그레이션 파일에 변경 사항을 수동으로 추가하지 않는 한, Prisma Migrate 및 `db push`로 스키마의 뷰를 데이터베이스에 적용할 수 없습니다.

이 기능의 진행 상황 업데이트는 [GitHub 이슈](https://github.com/prisma/prisma/issues/17335)에서 확인하세요.

## `views` 프리뷰 기능 활성화

뷰 지원은 현재 초기 프리뷰 단계입니다. `views` 프리뷰 기능을 활성화하려면 Prisma Schema의 `generator` 블록에 있는 `previewFeatures` 필드에 `views` 기능 플래그를 추가하세요.

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["views"]
    }
```

`views`용 전용 프리뷰 기능 [피드백 이슈](https://github.com/prisma/prisma/issues/17335)에 이 프리뷰 기능에 대한 의견을 남겨주세요.

## 기본 데이터베이스에 뷰 생성

현재 Prisma Migrate나 `db push`로 Prisma 스키마에 정의한 뷰를 데이터베이스에 적용할 수 없습니다. 대신 먼저 기본 데이터베이스에 뷰를 생성해야 하며, 수동으로 생성하거나 [마이그레이션의 일부로](https://docs.prisma.io/docs/orm/prisma-schema/data-model/views#use-views-with-prisma-migrate-and-db-push) 생성할 수 있습니다.

예를 들어, `User` 모델과 연관된 `Profile` 모델이 있는 다음 Prisma 스키마를 보겠습니다.

Relational databases

MongoDB

```
    model User {
      id      Int      @id @default(autoincrement())
      email   String   @unique
      name    String?
      profile Profile?
    }

    model Profile {
      id     Int    @id @default(autoincrement())
      bio    String
      user   User   @relation(fields: [userId], references: [id])
      userId Int    @unique
    }
```

다음으로, 기본 데이터베이스에 `User` 모델의 `email`, `name` 필드와 `Profile` 모델의 `bio` 필드를 결합한 `UserInfo` 뷰가 있다고 가정합니다.

관계형 데이터베이스에서 이 뷰를 생성하는 SQL 문은 다음과 같습니다.

```
    CREATE VIEW "UserInfo" AS
        SELECT u.id, email, name, bio
        FROM "User" u
        LEFT JOIN "Profile" p ON u.id = p."userId";
```

MongoDB에서는 다음 명령으로 [뷰를 생성](https://www.mongodb.com/docs/manual/core/views/join-collections-with-view/)할 수 있습니다.

```
    db.createView("UserInfo", "User", [
      {
        $lookup: {
          from: "Profile",
          localField: "_id",
          foreignField: "userId",
          as: "ProfileData",
        },
      },
      {
        $project: {
          _id: 1,
          email: 1,
          name: 1,
          bio: "$ProfileData.bio",
        },
      },
      { $unwind: "$bio" },
    ]);
```

## Prisma Migrate 및 `db push`와 함께 뷰 사용

Prisma Migrate 또는 `db push`로 Prisma 스키마 변경 사항을 적용하면 Prisma ORM은 뷰와 관련된 SQL을 생성하거나 실행하지 않습니다.

마이그레이션에 뷰를 포함하려면 `migrate dev --create-only`를 실행한 뒤 마이그레이션 파일에 뷰용 SQL을 수동으로 추가하세요. 또는 데이터베이스에서 뷰를 수동으로 생성할 수 있습니다.

## Prisma 스키마에 뷰 추가

Prisma 스키마에 뷰를 추가하려면 `view` 키워드를 사용하세요.

위 예시의 `UserInfo` 뷰는 Prisma 스키마에서 다음과 같이 표현할 수 있습니다.

Relational databases

MongoDB

```
    view UserInfo {
      id    Int
      email String
      name  String
      bio   String
    }
```

- 수동 작성

`view` 블록은 두 가지 주요 요소로 구성됩니다.

- `view` 블록 정의
- 뷰의 필드 정의

이 두 요소를 통해 생성된 Prisma Client에서 뷰의 이름과, 뷰 쿼리 결과에 포함되는 컬럼을 정의할 수 있습니다.

#

- `view` 블록 정의

위 예시의 `UserInfo` 뷰를 정의하려면 먼저 `view` 키워드를 사용해 스키마에 `UserInfo`라는 이름의 `view` 블록을 정의하세요.

```
    view UserInfo {
      // Fields
    }
```

#

- 필드 정의

뷰의 속성은 _fields_ 라고 하며, 다음으로 구성됩니다.

- 필드 이름
- 필드 타입

`UserInfo` 예시 뷰의 필드는 다음과 같이 정의할 수 있습니다.

Relational databases

MongoDB

```
    view UserInfo {
      id    Int
      email String
      name  String
      bio   String
    }
```

`view` 블록의 각 _field_ 는 기본 데이터베이스에서 해당 뷰의 쿼리 결과에 있는 하나의 컬럼을 나타냅니다.

- introspection 사용

현재 뷰 introspection은 PostgreSQL, MySQL, SQL Server, CockroachDB 데이터베이스에서만 가능합니다. 다른 데이터베이스 프로바이더를 사용하는 경우 뷰를 수동으로 추가해야 합니다.

데이터베이스에 기존 뷰가 하나 이상 정의되어 있으면 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection)을 통해 Prisma 스키마에 해당 뷰를 나타내는 `view` 블록이 자동 생성됩니다.

예시의 `UserInfo` 뷰가 기본 데이터베이스에 존재한다고 가정하면, 다음 명령을 실행했을 때 Prisma 스키마에 해당 뷰를 나타내는 `view` 블록이 생성됩니다.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

생성된 `view` 블록은 다음과 같이 정의됩니다.

```
    view UserInfo {
      id    Int?
      email String?
      name  String?
      bio   String?
    }
```

현재 `db pull`이 스키마의 뷰를 introspect하는 기능은 PostgreSQL, MySQL, SQL Server, CockroachDB 사용 시에만 동작합니다. 이 워크플로 지원은 다른 데이터베이스 프로바이더로 확장될 예정입니다.

#

- `views` 디렉터리

기존 뷰가 하나 이상 있는 데이터베이스를 introspection하면 `prisma` 디렉터리 안에 새로운 `views` 디렉터리도 생성됩니다. 이 디렉터리에는 데이터베이스 스키마 이름을 딴 하위 디렉터리가 포함되며, 그 안에는 해당 스키마에서 introspect된 각 뷰마다 하나의 `.sql` 파일이 생성됩니다. 각 파일 이름은 개별 뷰 이름과 같고, 관련 뷰가 정의하는 쿼리를 담고 있습니다.

예를 들어, 위 모델을 사용해 기본 `public` 스키마가 있는 데이터베이스를 introspection한 후에는 다음 내용으로 `prisma/views/public/UserInfo.sql` 파일이 생성됩니다.

```
    SELECT
      u.id,
      u.email,
      u.name,
      p.bio
    FROM
      (
        "User" u
        LEFT JOIN "Profile" p ON ((u.id = p."userId"))
      );
```

## Prisma Client에서 뷰 쿼리

Prisma 스키마를 업데이트한 후에는 `view` 정의가 Prisma Client API에 포함되도록 반드시 `prisma generate`를 실행하세요.

Prisma Client에서 뷰는 모델을 쿼리하는 방식과 동일하게 쿼리할 수 있습니다. 예를 들어, 다음 쿼리는 위에서 정의한 `UserInfo` 뷰에서 `name`이 `'Alice'`인 모든 사용자를 찾습니다.

```
    const userinfo = await prisma.userInfo.findMany({
      where: {
        name: "Alice",
      },
    });
```

`views`에서는 쓰기 쿼리(create/update/delete)가 지원되지 않습니다.

## 특수한 유형의 뷰

이 섹션에서는 데이터베이스의 updatable view 및 materialized view와 함께 Prisma ORM을 사용하는 방법을 설명합니다.

- Updatable views

일부 데이터베이스는 _updatable views_ 를 지원합니다(예: [PostgreSQL](https://www.postgresql.org/docs/current/sql-createview.html#SQL-CREATEVIEW-UPDATABLE-VIEWS), [MySQL](https://dev.mysql.com/doc/refman/8.0/en/view-updatability.html), [SQL Server](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver16#updatable-views)). Updatable view를 사용하면 기본 데이터베이스가 해당 연산을 지원하는 경우 항목 생성, 업데이트, 삭제가 가능합니다.

Prisma ORM은 데이터베이스의 기능과 관계없이 뷰에 대한 어떤 mutation(create, update, delete)도 허용하지 않습니다. 이 변경은 Prisma Client 내에서 뷰를 일관되게 읽기 전용 엔터티로 취급하도록 가드레일을 제공합니다. 따라서 Prisma Client API의 `view` 블록에는 `create`, `update`, `delete`, `upsert` 같은 쓰기 메서드가 생성되지 않습니다.

뷰로 표현된 데이터를 수정해야 한다면 기본 테이블에서 직접 쓰기 작업을 수행하거나 raw SQL 쿼리를 사용해야 합니다.

- Materialized views

일부 데이터베이스는 materialized view를 지원합니다. 예: [PostgreSQL](https://www.postgresql.org/docs/current/rules-materializedviews.html), [CockroachDB](https://www.cockroachlabs.com/docs/stable/views.html#materialized-views), [MongoDB](https://www.mongodb.com/docs/manual/core/materialized-views/), [SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-ver16)(여기서는 "indexed views"라고 부름).

Materialized view는 더 빠른 접근을 위해 뷰 쿼리 결과를 저장하며, 필요할 때만 업데이트합니다.

현재 Prisma ORM은 materialized view를 지원하지 않습니다. 하지만 [수동으로 뷰를 생성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/views#create-a-view-in-the-underlying-database)할 때 기본 데이터베이스에서 해당 명령으로 materialized view도 생성할 수 있습니다. 이후 Prisma Client의 [TypedSQL 기능](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql)을 사용해 명령을 실행하고 뷰를 수동으로 새로 고칠 수 있습니다.

향후 Prisma Client는 개별 뷰를 materialized로 표시하는 기능과 materialized view를 새로 고치는 Prisma Client 메서드를 지원할 수 있습니다. 사용 사례가 있다면 [`views` 피드백 이슈](https://github.com/prisma/prisma/issues/17335)에 의견을 남겨주세요.

## 제한 사항

Prisma ORM은 모든 `view` 블록을 실제 테이블이 아니라 데이터베이스 쿼리의 _읽기 전용_ 표현으로 취급합니다. 따라서 Prisma Client 동작을 기본 데이터베이스의 동작과 일관되게 유지하기 위해 몇 가지 제한 사항이 적용됩니다.

- 식별자 없음

뷰는 가상 테이블이므로 고유한 기본 키가 없습니다. 따라서 `view` 블록에 `@id`, `@@id` 속성을 정의할 수 없습니다.

- 인덱스 없음

뷰는 가상 테이블이므로 인덱스를 가질 수 없습니다. 따라서 `view` 블록에 `@index` 및 `@@index`를 정의할 수 없습니다.

- 안전하지 않은 `@unique` 속성

Prisma ORM은 뷰에 `@unique`, `@@unique` 속성을 배치할 수 있게 허용하지만, 기본 데이터베이스와 Prisma는 해당 제약을 강제하지 않습니다. 따라서 고유해야 하는 필드라도 여러 행이 동일한 값을 가질 수 있습니다.

데이터베이스와 Prisma ORM 모두 해당 속성으로 표현된 unique 제약을 강제하지 않습니다.

이 경우 `@unique` 속성의 목적은 Prisma Client에서 뷰 간 관계를 활성화하고, `findUnique` 쿼리 및 커서 기반 페이지네이션을 가능하게 하는 데에만 있습니다.

- 비활성화된 쓰기 쿼리

모든 쓰기 작업(`create`, `update`, `delete`, `upsert`)은 비활성화되며 Prisma Client에서 생성되지 않습니다.
