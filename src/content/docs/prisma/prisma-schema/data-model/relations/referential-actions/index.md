---
title: "참조 동작"
description: "참조 동작을 사용하면 데이터베이스 수준에서 관련 모델의 업데이트 및 삭제 동작을 정의할 수 있습니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions

# 참조 동작

참조 동작을 사용하면 데이터베이스 수준에서 관련 모델의 업데이트 및 삭제 동작을 정의할 수 있습니다.

참조 동작은 애플리케이션이 관련 레코드를 삭제하거나 업데이트할 때 어떤 일이 발생하는지를 결정합니다. 이는 [`@relation`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#relation) 속성에서 정의되며, 데이터베이스의 외래 키 제약 조건에 매핑됩니다.

다음 예시에서 `onDelete: Cascade`는 `User` 레코드를 삭제하면 관련된 모든 `Post` 레코드도 함께 삭제된다는 의미입니다.

schema.prisma

```
    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      author   User   @relation(fields: [authorId], references: [id], onDelete: Cascade)
      authorId Int
    }

    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

참조 동작을 지정하지 않으면 Prisma ORM은 [기본값을 사용합니다](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#referential-action-defaults).

이 페이지에서 답하는 질문

- 참조 동작은 무엇을 하나요?
- 아무것도 설정하지 않으면 어떤 기본값이 적용되나요?
- 동작은 내 데이터베이스에 어떻게 매핑되나요?
- SQL Server에서 cascade cycle은 어떻게 해결하나요?
- MongoDB 자기 참조 관계에는 NoAction이 필요한가요?
- 여러 cascade 경로는 어떻게 처리하나요?

## 사용 가능한 참조 동작

Prisma ORM은 5가지 참조 동작을 지원합니다.

- **[`Cascade`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#cascade)** - 삭제/업데이트가 관련 레코드로 연쇄 적용됨
- **[`Restrict`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#restrict)** - 관련 레코드가 있으면 삭제/업데이트를 방지함
- **[`NoAction`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#noaction)** - Restrict와 유사하지만 동작은 데이터베이스마다 다름
- **[`SetNull`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#setnull)** - 외래 키를 NULL로 설정함(선택적 관계 필요)
- **[`SetDefault`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#setdefault)** - 외래 키를 기본값으로 설정함

* 참조 동작 기본값

참조 동작을 지정하지 않으면 Prisma ORM은 다음 기본값을 사용합니다.

| 절         | 선택적 관계 | 필수 관계  |
| ---------- | ----------- | ---------- |
| `onDelete` | `SetNull`   | `Restrict` |
| `onUpdate` | `Cascade`   | `Cascade`  |

## 주의 사항

다음 주의 사항이 적용됩니다.

- [암시적 다대다 관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations)에서는 참조 동작이 **지원되지 않습니다**. 참조 동작을 사용하려면 명시적 다대다 관계를 정의하고 [조인 테이블](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/troubleshooting-relations#how-to-use-a-relation-table-with-a-many-to-many-relationship)에서 참조 동작을 정의해야 합니다.
- 일부 참조 동작과 필수/선택 관계의 조합은 호환되지 않습니다. 예를 들어 필수 관계에 `SetNull`을 사용하면, null 불가 제약을 위반하게 되므로 참조된 레코드를 삭제할 때 데이터베이스 오류가 발생합니다. 자세한 내용은 [이 GitHub 이슈](https://github.com/prisma/prisma/issues/7909)를 참고하세요.

## 참조 동작 유형

다음 표는 각 데이터베이스가 어떤 참조 동작을 지원하는지 보여줍니다.

| 데이터베이스  | Cascade | Restrict | NoAction | SetNull | SetDefault |
| ------------- | ------- | -------- | -------- | ------- | ---------- |
| PostgreSQL    | ✔️      | ✔️       | ✔️       | ✔️⌘     | ✔️         |
| MySQL/MariaDB | ✔️      | ✔️       | ✔️       | ✔️      | ❌ (✔️†)   |
| SQLite        | ✔️      | ✔️       | ✔️       | ✔️      | ✔️         |
| SQL Server    | ✔️      | ❌‡      | ✔️       | ✔️      | ✔️         |
| CockroachDB   | ✔️      | ✔️       | ✔️       | ✔️      | ✔️         |
| MongoDB       | ✔️      | ✔️       | ✔️       | ✔️      | ❌         |

- † [MySQL의 특수 사례](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#mysqlmariadb)를 참고하세요.
- ⌘ [PostgreSQL의 특수 사례](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#postgresql)를 참고하세요.
- ‡ [SQL Server의 특수 사례](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#sql-server)를 참고하세요.

* 참조 동작의 특수 사례

참조 동작은 ANSI SQL 표준의 일부입니다. 하지만 일부 관계형 데이터베이스는 표준과 다르게 동작하는 특수 사례가 있습니다.

#

- MySQL/MariaDB

MySQL/MariaDB와 그 기반인 InnoDB 스토리지 엔진은 `SetDefault`를 지원하지 않습니다. 정확한 동작은 데이터베이스 버전에 따라 다릅니다.

- MySQL 8 이상 및 MariaDB 10.5 이상에서는 `SetDefault`가 사실상 `NoAction`의 별칭처럼 동작합니다. `SET DEFAULT` 참조 동작으로 테이블을 정의할 수는 있지만, 런타임에 외래 키 제약 오류가 발생합니다.
- MySQL 5.6 이상 및 MariaDB 10.5 미만에서는 `SET DEFAULT` 참조 동작이 포함된 테이블 정의를 생성하려고 하면 구문 오류로 실패합니다.

이 때문에 데이터베이스 provider를 `mysql`로 설정하면 Prisma ORM은 Prisma 스키마의 `SetDefault` 참조 동작을 다른 동작으로 교체하라고 경고합니다.

#

- PostgreSQL

PostgreSQL은 Prisma ORM이 지원하는 데이터베이스 중, null 불가 필드를 참조하는 `SetNull` 참조 동작을 정의할 수 있는 유일한 데이터베이스입니다. 그러나 이 동작이 런타임에 트리거되면 외래 키 제약 오류가 발생합니다.

이 때문에 (기본값인) `foreignKeys` relation mode에서 데이터베이스 provider를 `postgres`로 설정하면 Prisma ORM은 `SetNull` 참조 동작이 있는 `@relation` 속성에 포함된 필드를 선택적(optional)으로 표시하라고 경고합니다. 다른 모든 데이터베이스 provider에서는 Prisma ORM이 유효성 검사 오류와 함께 스키마를 거부합니다.

#

- SQL Server

SQL Server 데이터베이스에서는 [`Restrict`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#restrict)를 사용할 수 없지만, 대신 [`NoAction`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#noaction)을 사용할 수 있습니다.

- `Cascade`
  - `onDelete: Cascade` 참조된 레코드를 삭제하면 이를 참조하는 레코드 삭제가 트리거됩니다.
  - `onUpdate: Cascade` 종속 레코드의 참조 대상 scalar 필드가 업데이트되면 relation scalar 필드도 업데이트됩니다.

#

- 예시 사용법

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

**결과:** `User` 레코드가 삭제되면 해당 사용자의 게시물도 함께 삭제됩니다. 사용자의 `id`가 업데이트되면 해당 `authorId`도 함께 업데이트됩니다.

- `Restrict`
  - `onDelete: Restrict` 참조하는 레코드가 하나라도 있으면 삭제를 방지합니다.
  - `onUpdate: Restrict` 참조된 레코드의 식별자가 변경되는 것을 방지합니다.

#

- 예시 사용법

schema.prisma

```
    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      author   User   @relation(fields: [authorId], references: [id], onDelete: Restrict, onUpdate: Restrict)
      authorId Int
    }

    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

**결과:** 게시물이 있는 `User`는 삭제할 수 없습니다. `User`의 `id`는 변경할 수 없습니다.

`Restrict` 동작은 [Microsoft SQL Server](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)에서 사용할 수 없으며 스키마 유효성 검사 오류를 발생시킵니다. 대신 같은 결과를 내고 SQL Server와 호환되는 [`NoAction`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#noaction)을 사용할 수 있습니다.

- `NoAction`

`NoAction` 동작은 `Restrict`와 유사하며, 둘의 차이는 사용 중인 데이터베이스에 따라 달라집니다.

- **PostgreSQL** : `NoAction`은 검사를(테이블에 참조된 행이 존재하는지 여부) 트랜잭션의 나중 시점까지 지연할 수 있습니다. 자세한 내용은 [PostgreSQL 문서](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK)를 참고하세요.
- **MySQL** : `NoAction`은 `Restrict`와 정확히 동일하게 동작합니다. 자세한 내용은 [MySQL 문서](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html#foreign-key-referential-actions)를 참고하세요.
- **SQLite** : 관련 기본 키가 수정되거나 삭제되어도 아무 동작도 수행되지 않습니다. 자세한 내용은 [SQLite 문서](https://www.sqlite.org/foreignkeys.html#fk_actions)를 참고하세요.
- **SQL Server** : 참조된 레코드가 삭제되거나 수정되면 오류가 발생합니다. 자세한 내용은 [SQL Server 문서](https://learn.microsoft.com/en-us/sql/relational-databases/tables/graph-edge-constraints?view=sql-server-ver15#on-delete-referential-actions-on-edge-constraints)를 참고하세요.
- **MongoDB** : 레코드가 수정되거나 삭제되어도 관련 레코드에는 아무 작업도 수행되지 않습니다.

데이터베이스 외래 키를 사용하는 대신 [Prisma Client에서 관계를 관리](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode#emulate-relations-in-prisma-orm-with-the-prisma-relation-mode)하는 경우, 현재 Prisma ORM은 참조 동작만 구현한다는 점을 알아야 합니다. 외래 키는 제약 조건도 생성하며, 이 제약을 위반하는 방식으로 데이터를 조작하는 것을 불가능하게 만듭니다. 즉 쿼리를 실행하는 대신 데이터베이스가 오류를 반환합니다. Prisma Client에서 참조 무결성을 에뮬레이션하면 이러한 제약은 생성되지 않으므로, 참조 동작을 `NoAction`으로 설정했을 때 참조 무결성 위반을 막아주는 검사가 존재하지 않습니다.

#

- 예시 사용법

schema.prisma

```
    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      author   User   @relation(fields: [authorId], references: [id], onDelete: NoAction, onUpdate: NoAction)
      authorId Int
    }

    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

**결과:** 게시물이 있는 `User`는 삭제할 수 없습니다. `User`의 `id`는 변경할 수 없습니다.

- `SetNull`
  - `onDelete: SetNull` 참조하는 객체의 scalar 필드가 `NULL`로 설정됩니다.

  - `onUpdate: SetNull` 참조된 객체의 식별자를 업데이트할 때, 참조하는 객체의 scalar 필드가 `NULL`로 설정됩니다.

`SetNull`은 선택적 관계에서만 동작합니다. 필수 관계에서는 scalar 필드가 null이 될 수 없으므로 런타임 오류가 발생합니다.

schema.prisma

```
    model Post {
      id       Int    @id @default(autoincrement())
      title    String
      author   User?  @relation(fields: [authorId], references: [id], onDelete: SetNull, onUpdate: SetNull)
      authorId Int?
    }

    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }
```

**결과:** `User`를 삭제하거나 업데이트하면 해당 사용자의 모든 게시물에서 `authorId`가 `NULL`로 설정됩니다.

- `SetDefault`
  - `onDelete: SetDefault` 참조하는 객체의 scalar 필드가 해당 필드의 기본값으로 설정됩니다.

  - `onUpdate: SetDefault` 참조하는 객체의 scalar 필드가 해당 필드의 기본값으로 설정됩니다.

이를 사용하려면 relation scalar 필드에 [`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default)로 기본값을 설정해야 합니다. 어떤 scalar 필드에도 기본값이 제공되지 않으면 런타임 오류가 발생합니다.

schema.prisma

```
    model Post {
      id             Int     @id @default(autoincrement())
      title          String
      authorUsername String? @default("anonymous")
      author         User?   @relation(fields: [authorUsername], references: [username], onDelete: SetDefault, onUpdate: SetDefault)
    }

    model User {
      username String @id
      posts    Post[]
    }
```

**결과:** `User`를 삭제하거나 업데이트할 때 해당 게시물의 `authorUsername`은 기본값(`'anonymous'`)으로 설정됩니다.

## SQL Server 및 MongoDB를 위한 특별 규칙

빠른 요약

이 섹션에서는 SQL Server 및 MongoDB에서 referential actions를 사용할 때의 특별 규칙과 일반적인 문제를 설명하며, 사이클과 다중 cascade 경로를 피하는 방법을 포함합니다.

**SQL Server**는 관계 체인으로 인해 사이클이나 다중 cascade 경로가 발생하는 경우 cascading referential actions를 허용하지 않습니다. SQL 실행 시 서버가 오류를 반환합니다.

**MongoDB**는 무한 루프를 방지하기 위해 자기 참조 관계 또는 세 모델 간 사이클에 `NoAction`이 필요합니다. MongoDB는 기본적으로 `relationMode = "prisma"`를 사용하며, 이는 Prisma ORM이 [참조 무결성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode)을 관리한다는 의미입니다.

Prisma ORM은 SQL을 생성하기 _전에_ 데이터 모델을 검증하여, 문제가 있는 관계를 강조 표시해 이러한 이슈를 조기에 수정할 수 있도록 돕습니다.

- 자기 참조 관계 (SQL Server 및 MongoDB)

다음 모델은 `Employee`가 관리자와 피관리자를 가질 수 있는 자기 참조 관계를 설명하며, 동일한 모델의 엔트리를 참조합니다.

```
    model Employee {
      id        Int        @id @default(autoincrement())
      manager   Employee?  @relation(name: "management", fields: [managerId], references: [id])
      managees  Employee[] @relation(name: "management")
      managerId Int?
    }
```

이 경우 다음 오류가 발생합니다:

```
    Error parsing attribute "@relation": A self-relation must have `onDelete` and `onUpdate` referential actions set to `NoAction` in one of the @relation attributes. (Implicit default `onDelete`: `SetNull`, and `onUpdate`: `Cascade`)
```

어떤 action도 정의하지 않으면, Prisma ORM은 기반 [scalar fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields)가 optional인지 required인지에 따라 다음 기본값을 사용합니다.

| Clause     | 모든 scalar field가 optional | 최소 하나의 scalar field가 required |
| ---------- | ---------------------------- | ----------------------------------- |
| `onDelete` | `SetNull`                    | `NoAction`                          |
| `onUpdate` | `Cascade`                    | `Cascade`                           |

위 관계에서 `onUpdate`의 기본 referential action은 `Cascade`이고 `onDelete`는 `SetNull`이므로, 사이클이 생성됩니다. 해결 방법은 `onUpdate`와 `onDelete` 값을 명시적으로 `NoAction`으로 설정하는 것입니다.

```
    model Employee {
      id        Int        @id @default(autoincrement())
      manager   Employee   @relation(name: "management", fields: [managerId], references: [id])
      manager   Employee   @relation(name: "management", fields: [managerId], references: [id], onDelete: NoAction, onUpdate: NoAction)
      managees  Employee[] @relation(name: "management")
      managerId Int
    }
```

- 세 테이블 간 순환 관계 (SQL Server 및 MongoDB)

다음 모델은 `Chicken`, `Egg`, `Fox` 간의 순환 관계를 설명하며, 각 모델이 서로를 참조합니다.

```
    model Chicken {
      id        Int   @id @default(autoincrement())
      egg       Egg   @relation(fields: [eggId], references: [id])
      eggId     Int
      predators Fox[]
    }

    model Egg {
      id         Int       @id @default(autoincrement())
      predator   Fox       @relation(fields: [predatorId], references: [id])
      predatorId Int
      parents    Chicken[]
    }

    model Fox {
      id        Int     @id @default(autoincrement())
      meal      Chicken @relation(fields: [mealId], references: [id])
      mealId    Int
      foodStore Egg[]
    }
```

이 경우 사이클이 존재함을 나타내는 검증 오류가 발생합니다:

```
    Error parsing attribute "@relation": Reference causes a cycle. One of the @relation attributes in this cycle must have `onDelete` and `onUpdate` referential actions set to `NoAction`. Cycle path: Chicken.egg → Egg.predator → Fox.meal. (Implicit default `onUpdate`: `Cascade`)
```

기본 `onUpdate` action이 `Cascade`이므로 사이클이 생성됩니다. 사이클을 끊으려면 관계 중 하나에 `onUpdate: NoAction`을 설정하세요:

```
    model Chicken {
      id        Int   @id @default(autoincrement())
      egg       Egg   @relation(fields: [eggId], references: [id])
      egg       Egg   @relation(fields: [eggId], references: [id], onUpdate: NoAction)
      eggId     Int
      predators Fox[]
    }
```

- 두 모델 간 다중 cascade 경로 (SQL Server 전용)

이 데이터 모델은 동일한 모델 사이에 두 개의 서로 다른 경로를 설명하며, 두 관계 모두 cascading referential actions를 트리거합니다.

```
    model User {
      id       Int       @id @default(autoincrement())
      comments Comment[]
      posts    Post[]
    }

    model Post {
      id       Int       @id @default(autoincrement())
      authorId Int
      author   User      @relation(fields: [authorId], references: [id])
      comments Comment[]
    }

    model Comment {
      id          Int  @id @default(autoincrement())
      writtenById Int
      postId      Int
      writtenBy   User @relation(fields: [writtenById], references: [id])
      post        Post @relation(fields: [postId], references: [id])
    }
```

`Comment`에서 `User`로 가는 경로가 두 개 있으며, 기본 `onUpdate: Cascade`가 다중 cascade 경로를 생성합니다:

```
    Error parsing attribute "@relation": When any of the records in model `User` is updated or deleted, the referential actions on the relations cascade to model `Comment` through multiple paths. Please break one of these paths by setting the `onUpdate` and `onDelete` to `NoAction`. (Implicit default `onUpdate`: `Cascade`)
```

다중 cascade 경로를 끊으려면 관계 중 하나에 `onUpdate: NoAction`을 설정하세요:

```
    model Comment {
      id          Int  @id @default(autoincrement())
      writtenById Int
      postId      Int
      writtenBy   User @relation(fields: [writtenById], references: [id])
      writtenBy   User @relation(fields: [writtenById], references: [id], onUpdate: NoAction)
      post        Post @relation(fields: [postId], references: [id])
    }
```
