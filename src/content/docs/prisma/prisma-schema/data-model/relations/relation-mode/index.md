---
title: "관계 모드(Relation mode)"
description: "Prisma에서 관계 모드(relation mode)를 사용해 레코드 간 관계를 관리합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode

# 관계 모드(Relation mode)

Prisma에서 관계 모드(relation mode)를 사용해 레코드 간 관계를 관리합니다.

이 페이지에서 답하는 질문

- Prisma에서 `relationMode`란 무엇인가요?
- `prisma`와 `foreignKeys`는 언제 사용해야 하나요?
- relation 에뮬레이션은 제약 조건에 어떤 영향을 주나요?

Prisma schema에서 레코드 간 관계는 [`@relation`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#relation) 속성(attribute)으로 정의됩니다. 예를 들어, 다음 schema에는 `User`와 `Post` 모델 간 일대다 관계가 있습니다.

schema.prisma

```
    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      author   User   @relation(fields: [authorId], references: [id], onDelete: Cascade, onUpdate: Cascade)
      authorId Int
    }

    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

Prisma ORM에는 _relation mode_ 가 두 가지 있으며, `foreignKeys`와 `prisma`가 레코드 간 관계를 어떻게 강제할지 지정합니다.

Prisma ORM을 관계형 데이터베이스와 함께 사용하는 경우, 기본적으로 Prisma ORM은 [`foreignKeys` relation mode](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode#handle-relations-in-your-relational-database-with-the-foreignkeys-relation-mode)를 사용하며, 외래 키를 통해 데이터베이스 수준에서 레코드 간 관계를 강제합니다. 외래 키는 한 테이블의 열(또는 열 집합)로, 다른 테이블의 기본 키를 기반으로 값을 가집니다. 외래 키를 사용하면 다음이 가능합니다.

- 참조를 깨뜨리는 변경을 방지하는 제약 조건 설정
- 레코드 변경 처리 방식을 정의하는 [referential actions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions) 설정

이 제약 조건과 referential actions를 함께 사용하면 데이터의 _referential integrity_ 가 보장됩니다.

위 예시 schema에서 PostgreSQL 커넥터를 사용하는 경우, Prisma Migrate는 기본적으로 다음 SQL을 생성합니다:

```
    -- CreateTable
    CREATE TABLE "Post" (
        "id" SERIAL NOT NULL,
        "title" TEXT NOT NULL,
        "authorId" INTEGER NOT NULL,

        CONSTRAINT "Post_pkey" PRIMARY KEY ("id")
    );

    -- CreateTable
    CREATE TABLE "User" (
        "id" SERIAL NOT NULL,

        CONSTRAINT "User_pkey" PRIMARY KEY ("id")
    );

    -- AddForeignKey
    ALTER TABLE "Post"
      ADD CONSTRAINT "Post_authorId_fkey"
      FOREIGN KEY ("authorId")
      REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

이 경우 `Post` 테이블의 `authorId` 열에 있는 외래 키 제약은 `User` 테이블의 `id` 열을 참조하며, 게시물에 반드시 존재하는 작성자가 있어야 함을 보장합니다. 사용자를 업데이트하거나 삭제하면 `ON DELETE` 및 `ON UPDATE` referential actions에서 `CASCADE` 옵션이 지정되어, 해당 사용자에 속한 모든 게시물도 함께 삭제되거나 업데이트됩니다.

MongoDB 또는 [PlanetScale](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale) 같은 일부 데이터베이스는 외래 키를 지원하지 않습니다. 또한 일반적으로 외래 키를 지원하는 관계형 데이터베이스에서도, 경우에 따라 개발자가 외래 키를 사용하지 않기를 원할 수 있습니다. 이런 상황을 위해 Prisma ORM은 [the `prisma` relation mode](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode#emulate-relations-in-prisma-orm-with-the-prisma-relation-mode)를 제공하며, 관계형 데이터베이스의 일부 관계 속성을 에뮬레이션합니다. `prisma` relation mode를 활성화한 상태로 Prisma Client를 사용하면 쿼리 동작은 동일하거나 유사하지만, referential actions 및 일부 제약은 데이터베이스가 아니라 Prisma engine에서 처리됩니다.

Prisma Client에서 referential integrity 및 referential actions를 에뮬레이션하면 성능에 영향을 줄 수 있습니다. 기반 데이터베이스가 외래 키를 지원하는 경우에는 일반적으로 외래 키를 사용하는 편이 더 적합합니다.

## How to set the relation mode in your Prisma schema

relation mode를 설정하려면 `datasource` 블록에 `relationMode` 필드를 추가하세요:

schema.prisma

```
    datasource db {
      provider     = "mysql"
      relationMode = "prisma"
    }
```

관계형 데이터베이스에서 사용 가능한 옵션은 다음과 같습니다.

- `foreignKeys`: 외래 키를 사용해 데이터베이스에서 관계를 처리합니다. 모든 관계형 데이터베이스 커넥터의 기본 옵션이며, `datasource` 블록에 `relationMode`를 명시적으로 설정하지 않으면 활성화됩니다.
- `prisma`: Prisma Client에서 관계를 에뮬레이션합니다. PlanetScale 데이터베이스 설정에서 네이티브 외래 키 제약을 활성화하지 않은 상태로 MySQL 커넥터와 PlanetScale 데이터베이스를 사용하는 경우에도 [이 옵션을 활성화](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)해야 합니다.

MongoDB에서는 `prisma` relation mode만 사용할 수 있습니다. 이 모드 역시 `datasource` 블록에 `relationMode`를 명시적으로 설정하지 않으면 활성화됩니다.

relation mode를 전환하면 Prisma ORM은 다음에 Prisma Migrate 또는 `db push`로 schema 변경 사항을 적용할 때 데이터베이스의 외래 키를 추가하거나 제거합니다. 자세한 내용은 [Switch between relation modes](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode#switch-between-relation-modes)를 참고하세요.

## Handle relations in your relational database with the `foreignKeys` relation mode

`foreignKeys` relation mode는 외래 키를 사용해 관계형 데이터베이스에서 관계를 처리합니다. 관계형 데이터베이스 커넥터(PostgreSQL, MySQL, SQLite, SQL Server, CockroachDB)를 사용할 때 기본 옵션입니다.

MongoDB 커넥터를 사용할 때는 `foreignKeys` relation mode를 사용할 수 없습니다. [PlanetScale](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale) 같은 일부 관계형 데이터베이스도 외래 키 사용을 금지합니다. 이런 경우에는 대신 [Prisma ORM에서 `prisma` relation mode로 관계를 에뮬레이션](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode#emulate-relations-in-prisma-orm-with-the-prisma-relation-mode)해야 합니다.

- Referential integrity

`foreignKeys` relation mode는 외래 키 제약과 referential actions를 통해 데이터베이스 수준에서 referential integrity를 유지합니다.

#

- Foreign key constraints

다른 레코드와 관계가 있는 레코드를 _create_ 또는 _update_ 할 때, 관련 레코드는 반드시 존재해야 합니다. 외래 키 제약은 데이터베이스에서 이 동작을 강제합니다. 레코드가 존재하지 않으면 데이터베이스가 오류 메시지를 반환합니다.

#

- Referential actions

관련 레코드가 있는 레코드를 _update_ 또는 _delete_ 하면 데이터베이스에서 referential actions가 트리거됩니다. 관련 레코드의 referential integrity를 유지하기 위해, referential actions는 referential integrity를 깨뜨릴 수 있는 변경을 방지하거나, 변경을 관련 레코드로 전파(cascade)하거나, 업데이트/삭제된 레코드를 참조하는 필드 값을 `null` 또는 기본값으로 설정합니다.

자세한 내용은 [referential actions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions) 페이지를 참고하세요.

- Introspection

`foreignKeys` relation mode를 활성화한 상태에서 `db pull` 명령으로 관계형 데이터베이스를 introspect하면, 외래 키가 존재하는 관계에 대해 Prisma schema에 `@relation` attribute가 추가됩니다.

- Prisma Migrate and `db push`

`foreignKeys` relation mode를 활성화한 상태에서 Prisma Migrate 또는 `db push`로 Prisma schema 변경 사항을 적용하면, schema의 모든 `@relation` attribute에 대해 데이터베이스에 외래 키가 생성됩니다.

## Emulate relations in Prisma ORM with the `prisma` relation mode

`prisma` relation mode는 referential integrity를 유지하기 위해, 각 Prisma Client 쿼리에 대해 추가 데이터베이스 쿼리와 로직을 사용해 일부 외래 키 제약과 referential actions를 에뮬레이션합니다.

`prisma` relation mode는 MongoDB 커넥터의 기본 옵션입니다. 외래 키를 지원하지 않는 관계형 데이터베이스를 사용하는 경우에도 설정해야 합니다. 예를 들어 [외래 키 제약 없이 PlanetScale을 사용하는 경우](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale), `prisma` relation mode를 사용해야 합니다.

Prisma Client에서 referential integrity를 에뮬레이션할 때 referential integrity 유지를 위해 추가 데이터베이스 쿼리를 사용하므로 성능에 영향을 줄 수 있습니다. 기반 데이터베이스가 외래 키로 referential integrity를 처리할 수 있다면, 일반적으로 외래 키 방식이 더 적합합니다.

관계 에뮬레이션은 Prisma Client 쿼리에서만 사용할 수 있으며 raw query에는 적용되지 않습니다.

- Which foreign key constraints are emulated?

레코드를 _update_ 할 때 Prisma ORM은 외래 키 제약을 에뮬레이션합니다. 즉, 다른 레코드와 관계가 있는 레코드를 업데이트할 때 관련 레코드는 반드시 존재해야 합니다. 레코드가 존재하지 않으면 Prisma Client가 오류 메시지를 반환합니다.

하지만 레코드를 _create_ 할 때는 Prisma ORM이 외래 키 제약을 에뮬레이션하지 않습니다. 따라서 유효하지 않은 데이터를 생성할 수 있습니다.

- Which referential actions are emulated?

관련 레코드가 있는 레코드를 _update_ 또는 _delete_ 할 때 Prisma ORM은 referential actions를 에뮬레이션합니다.

다음 표는 각 데이터베이스 커넥터에서 사용할 수 있는 에뮬레이션 referential actions를 보여줍니다.

| Database    | Cascade | Restrict | NoAction | SetNull | SetDefault |
| ----------- | ------- | -------- | -------- | ------- | ---------- |
| PostgreSQL  | **✔️**  | **✔️**   | **❌** ‡ | **✔️**  | **❌** †   |
| MySQL       | **✔️**  | **✔️**   | **✔️**   | **✔️**  | **❌** †   |
| SQLite      | **✔️**  | **✔️**   | **❌** ‡ | **✔️**  | **❌** †   |
| SQL Server  | **✔️**  | **✔️**   | **✔️**   | **✔️**  | **❌** †   |
| CockroachDB | **✔️**  | **✔️**   | **✔️**   | **✔️**  | **❌** †   |
| MongoDB     | **✔️**  | **✔️**   | **✔️**   | **✔️**  | **❌** †   |

- † `SetDefault` referential action은 `prisma` relation mode에서 지원되지 않습니다.
- ‡ `NoAction` referential action은 PostgreSQL 및 SQLite의 `prisma` relation mode에서 지원되지 않습니다. 대신 `Restrict` action을 사용하세요.

* Error messages

`prisma` relation mode에서 에뮬레이션된 제약 및 referential actions가 반환하는 오류 메시지는 Prisma Client가 생성하며, `foreignKeys` relation mode의 오류 메시지와 약간 다릅니다:

```
    Example:
    // foreignKeys:
    ... Foreign key constraint failed on the field: `ProfileOneToOne_userId_fkey (index)`
    // prisma:
    ... The change you are trying to make would violate the required relation 'ProfileOneToOneToUserOneToOne' between the `ProfileOneToOne` and `UserOneToOne` models.
```

- Introspection

`prisma` relation mode를 활성화한 상태에서 `db pull` 명령으로 데이터베이스를 introspect하면, 관계가 schema에 자동으로 추가되지 않습니다. 대신 `@relation` attribute를 사용해 관계를 수동으로 추가해야 합니다. 이 작업은 한 번만 하면 되며, 다음에 데이터베이스를 introspect할 때 Prisma ORM이 추가한 `@relation` attribute를 유지합니다.

- Prisma Migrate and `db push`

`prisma` relation mode를 활성화한 상태에서 Prisma Migrate 또는 `db push`로 Prisma schema 변경 사항을 적용하면, Prisma ORM은 데이터베이스에서 외래 키를 사용하지 않습니다.

- Indexes

외래 키 제약 조건을 사용하는 관계형 데이터베이스에서는, 일반적으로 데이터베이스가 외래 키 컬럼에 대한 인덱스도 암묵적으로 생성합니다. 예를 들어, [MySQL will create an index on all foreign key columns](https://dev.mysql.com/doc/refman/8.0/en/constraint-foreign-key.html#:~:text=MySQL%20requires%20that%20foreign%20key%20columns%20be%20indexed%3B%20if%20you%20create%20a%20table%20with%20a%20foreign%20key%20constraint%20but%20no%20index%20on%20a%20given%20column%2C%20an%20index%20is%20created.). 이는 외래 키 검사가 빠르게 수행되고 테이블 스캔이 필요하지 않도록 하기 위함입니다.

`prisma` relation mode는 외래 키를 사용하지 않으므로, Prisma Migrate 또는 `db push`로 데이터베이스에 변경 사항을 적용할 때 인덱스가 생성되지 않습니다. 대신 관계 스칼라 필드에 [`@@index`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#index) 속성(또는 해당되는 경우 [`@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unique), [`@@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 또는 [`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성)을 사용해 인덱스를 수동으로 추가해야 합니다.

#

- Index validation

인덱스를 수동으로 추가하지 않으면 쿼리에 전체 테이블 스캔이 필요할 수 있습니다. 이는 느릴 수 있으며, 접근한 행 수에 따라 과금하는 데이터베이스 제공자에서는 비용도 증가할 수 있습니다. 이를 방지할 수 있도록, Prisma ORM은 스키마에 `@relation`에서 사용되지만 인덱스가 정의되지 않은 필드가 포함되어 있으면 경고를 표시합니다. 예를 들어 `User` 모델과 `Post` 모델 사이에 관계가 있는 다음 스키마를 보겠습니다.

schema.prisma

```
    datasource db {
      provider     = "mysql"
      relationMode = "prisma"
    }

    model User {
      id    Int    @id
      posts Post[]
    }

    model Post {
      id     Int  @id
      userId Int
      user   User @relation(fields: [userId], references: [id])
    }
```

`prisma format` 또는 `prisma validate`를 실행하면 Prisma ORM은 다음과 같은 경고를 표시합니다:

```
    With `relationMode = "prisma"`, no foreign keys are used, so relation fields will not benefit from the index usually created by the relational database under the hood. This can lead to poor performance when querying these fields. We recommend adding an index manually.
```

이를 수정하려면 `Post` 모델에 인덱스를 추가하세요:

schema.prisma

```
    model Post {
      id     Int  @id
      userId Int
      user   User @relation(fields: [userId], references: [id])

      @@index([userId])
    }
```

[Prisma VS Code extension](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)(또는 [language server in another editor](https://docs.prisma.io/docs/orm/more/dev-environment/editor-setup))를 사용하면, 이 경고에 필요한 인덱스를 자동으로 추가해 주는 Quick Fix가 함께 제공됩니다:

![The Quick Fix pop-up for adding an index on a relation scalar field in VS Code](https://docs.prisma.io/docs/img/orm/prisma-schema/data-model/relations/quick-fix-index.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

## Switch between relation modes

relation mode 간 전환은 관계형 데이터베이스 커넥터(PostgreSQL, MySQL, SQLite, SQL Server, CockroachDB)를 사용하는 경우에만 가능합니다.

- Switch from `foreignKeys` to `prisma`

관계형 데이터베이스를 사용하고 `datasource` 블록에 `relationMode` 필드를 포함하지 않으면 기본 relation mode는 `foreignKeys`입니다. `prisma` relation mode로 전환하려면 `relationMode` 필드에 `prisma` 값을 추가하거나, 이미 존재하는 경우 `relationMode` 필드 값을 `prisma`로 업데이트하세요.

relation mode를 `foreignKeys`에서 `prisma`로 전환한 뒤, Prisma Migrate 또는 `db push`로 스키마 변경 사항을 처음 적용하면 Prisma ORM은 다음 마이그레이션에서 이전에 생성된 모든 외래 키를 제거합니다.

같은 데이터베이스를 유지한다면 이후에는 평소처럼 계속 작업할 수 있습니다. 외래 키를 전혀 지원하지 않는 데이터베이스로 전환하는 경우에는, 기존 마이그레이션 기록에 외래 키를 생성하는 SQL DDL이 포함되어 있어 이 마이그레이션을 다시 실행해야 할 때 오류가 발생할 수 있습니다. 이 경우 `migrations` 디렉터리를 삭제하는 것을 권장합니다. (외래 키를 지원하지 않는 PlanetScale을 사용하는 경우에는 일반적으로 [use `db push` rather than Prisma Migrate](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)를 권장합니다.)

- Switch from `prisma` to `foreignKeys`

`prisma` relation mode에서 `foreignKeys` relation mode로 전환하려면 `relationMode` 필드 값을 `prisma`에서 `foreignKeys`로 업데이트하세요. 이를 위해서는 데이터베이스가 외래 키를 지원해야 합니다. relation mode를 전환한 뒤 Prisma Migrate 또는 `db push`로 스키마 변경 사항을 처음 적용하면, Prisma ORM은 다음 마이그레이션에서 모든 관계에 대한 외래 키를 생성합니다.
