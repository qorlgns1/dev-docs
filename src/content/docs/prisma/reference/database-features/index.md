---
title: "데이터베이스 기능"
description: "Prisma ORM에서 지원하는 데이터베이스 기능"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/database-features

# 데이터베이스 기능

Prisma ORM에서 지원하는 데이터베이스 기능

이 페이지는 Prisma ORM이 지원하는 데이터베이스에서 제공되는 기능을 개괄적으로 설명합니다. 또한 각 기능을 Prisma ORM에서 어떻게 사용할 수 있는지 추가 문서로 연결되는 링크와 함께 설명합니다.

## 관계형 데이터베이스 기능

이 섹션에서는 현재 Prisma ORM이 지원하는 관계형 데이터베이스에 어떤 기능이 있는지 설명합니다. **Prisma schema** 열은 특정 기능을 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에서 어떻게 표현할 수 있는지를 나타내며 관련 문서로 연결됩니다. 데이터베이스 기능이 Prisma schema에서 아직 표현되지 않더라도 **Prisma Client**에서는 사용할 수 있다는 점에 유의하세요.

이 기능들은 관계형 데이터베이스에만 해당합니다. MongoDB 같은 NoSQL 데이터베이스에서 지원되는 기능은 [아래에서 확인할 수 있습니다](https://docs.prisma.io/docs/orm/reference/database-features#nosql-database-features).

- 제약 조건

| Constraint    | Supported | Prisma schema                                                                                                       | Prisma Client | Prisma Migrate |
| ------------- | --------- | ------------------------------------------------------------------------------------------------------------------- | ------------- | -------------- |
| `PRIMARY KEY` | ✔️        | [`@id` and `@@id`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-an-id-field)            | ✔️            | ✔️             |
| `FOREIGN KEY` | ✔️        | [Relation fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)               | ✔️            | ✔️             |
| `UNIQUE`      | ✔️\*      | [`@unique` and `@@unique`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-unique-field) | ✔️            | ✔️             |
| `CHECK`       | ✔️†       | Not yet                                                                                                             | ✔️            | Not yet        |
| `NOT NULL`    | ✔️        | [`?`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#type-modifiers)                               | ✔️            | ✔️             |
| `DEFAULT`     | ✔️        | [`@default`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-default-value)              | ✔️            | ✔️             |
| `EXCLUDE`     | ✔️‡       | Not yet                                                                                                             | ✔️            | Not yet        |

> - Microsoft SQL Server에서 `UNIQUE` 제약 조건을 사용할 때는 [주의사항이 적용됩니다](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#common-considerations). † MySQL에서는 [버전 8 이상](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html)에서만 지원됩니다. ‡ PostgreSQL에서만 지원됩니다.

- 참조 동작(외래 키 참조의 삭제 및 업데이트 동작)

| Deletion behavior | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| ----------------- | --------- | ------------- | ------------- | -------------- |
| `CASCADE`         | ✔️        | ✔️            | ✔️            | ✔️             |
| `RESTRICT`        | ✔️\*      | ✔️            | ✔️            | ✔️             |
| `NO ACTION`       | ✔️        | ✔️            | ✔️            | ✔️             |
| `SET DEFAULT`     | ✔️        | ✔️            | ✔️            | ✔️             |
| `SET NULL`        | ✔️        | ✔️            | ✔️            | ✔️             |

> - `RESTRICT`는 Microsoft SQL Server에서 지원되지 않습니다.

- 인덱스

| Index          | Supported                                | Prisma schema                                                                                                                          | Prisma Client | Prisma Migrate |
| -------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------- |
| `UNIQUE`       | ✔️                                       | [`@unique` and `@@unique`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-unique-field)                    | ✔️            | ✔️             |
| `USING`        | PostgreSQL only                          | [`type`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-the-access-type-of-indexes-with-type-postgresql) | ✔️            | ✔️             |
| `WHERE`        | ✔️                                       | [`where`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where) (Preview)           | ✔️            | ✔️             |
| `(expression)` | ✔️                                       | Not yet                                                                                                                                | ✔️            | Not yet        |
| `INCLUDE`      | PostgreSQL and Microsoft SQL Server only | Not yet                                                                                                                                | ✔️            | Not yet        |

`USING`으로 지정되는 알고리즘:

| Index type (Algorithm) | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| ---------------------- | --------- | ------------- | ------------- | -------------- |
| B-tree                 | ✔️        | ✔️†           | ✔️            | Not yet        |
| Hash                   | ✔️        | ✔️†           | ✔️            | Not yet        |
| GiST                   | ✔️\*      | ✔️†           | ✔️\*          | Not yet        |
| GIN                    | ✔️\*      | ✔️†           | ✔️\*          | Not yet        |
| BRIN                   | ✔️\*      | ✔️†           | ✔️\*          | Not yet        |
| SP-GiST                | ✔️\*      | ✔️†           | ✔️\*          | Not yet        |

- - MySQL 및 SQLite에서는 지원되지 않음
- † PostgreSQL 커넥터에서만 Prisma ORM `4.0.0` 이상 버전에서 사용 가능

* 기타

| Feature                           | Supported                                | Prisma schema                                                                                                 | Prisma Client | Prisma Migrate |
| --------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------- | -------------- |
| Autoincrementing IDs              | ✔️                                       | [`autoincrement()`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-default-value) | ✔️            | ✔️             |
| Arrays                            | PostgreSQL only                          | [`[]`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#type-modifiers)                        | ✔️            | ✔️             |
| Enums                             | ✔️\*†                                    | [`enum`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-enums)                      | ✔️            | ✔️             |
| Native database types             | ✔️                                       | ✔️                                                                                                            | ✔️            | Not yet        |
| SQL Views                         | ✔️                                       | Not yet                                                                                                       | Not yet       | Not yet        |
| JSON support                      | ✔️†                                      | ✔️                                                                                                            | ✔️            | ✔️             |
| Fuzzy/Phrase full text search     | ✔️‡                                      | Not yet                                                                                                       | Not yet       | Not yet        |
| Table inheritance                 | PostgreSQL and Microsoft SQL Server only | Not yet                                                                                                       | ✔️            | Not yet        |
| Authorization and user management | ✔️‡                                      | Not yet                                                                                                       | Not yet       | Not yet        |

- - Microsoft SQL Server에서는 지원되지 않음
- † JSON 및 Enum 타입은 Prisma ORM 6.2.0부터 SQLite에서 지원됩니다.
- ‡ SQLite에서는 지원되지 않음

## NoSQL 데이터베이스 기능

이 섹션에서는 현재 Prisma ORM이 지원하는 NoSQL 데이터베이스에 어떤 기능이 있는지 설명합니다.

- MongoDB

다음 표는 일반적인 MongoDB 기능과 Prisma ORM이 제공하는 지원 수준을 보여줍니다.

| Feature                                   | Supported by Prisma ORM | Notes                                                                                                                       |
| ----------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Embedded documents                        | ✔️                      |
| Transactions                              | ✔️                      |
| Indexes                                   | ✔️ with caveats         | 인덱스는 참조하는 필드에 최소한 일부 데이터가 포함된 경우에만 introspection할 수 있습니다.                                  |
| Autoincrementing IDs                      | No                      |
| Compound IDs                              | No                      | MongoDB는 복합 ID(`@@id`)를 지원하지 않습니다.                                                                              |
| Generated `ObjectId`                      | ✔️                      | 참고: [Defining IDs for MongoDB](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-ids-in-mongodb)   |
| Arrays                                    | ✔️                      |
| Enums                                     | ✔️                      | Prisma ORM 레벨에서 구현됨                                                                                                  |
| Native database types                     | ✔️                      | 참고: [Field mapping reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types) |
| JSON support                              | ✔️                      | 고급 `Json` 필드 필터링은 아직 지원되지 않습니다.                                                                           |
| DBrefs                                    | No                      |
| Change streams                            | No                      |
| Direct access to the aggregation pipeline | No                      |
