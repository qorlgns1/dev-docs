---
title: "인덱스 구성"
description: "인덱스 기능을 구성하고 전체 텍스트 인덱스를 추가하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes

# 인덱스

인덱스 기능을 구성하고 전체 텍스트 인덱스를 추가하는 방법

Prisma ORM을 사용하면 데이터베이스 인덱스, 고유 제약 조건, 기본 키 제약 조건을 구성할 수 있습니다. MySQL과 MongoDB의 전체 텍스트 인덱스는 `@@fulltext` 속성과 함께 `fullTextIndex` 프리뷰 기능을 통해 사용할 수 있습니다.

## 인덱스 구성

다음 속성 인수를 사용해 인덱스, 고유 제약 조건, 기본 키 제약 조건을 구성할 수 있습니다:

- [`length` 인수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-the-length-of-indexes-with-length-mysql)를 사용하면 `String` 및 `Bytes` 타입에서 인덱싱할 값의 하위 부분에 대한 최대 길이를 지정할 수 있습니다.
  - `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용 가능
  - MySQL 전용

- [`sort` 인수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-the-index-sort-order-with-sort)를 사용하면 제약 조건 또는 인덱스 항목이 데이터베이스에 저장되는 순서를 지정할 수 있습니다.
  - 모든 데이터베이스에서 `@unique`, `@@unique`, `@@index` 속성에 사용 가능하며, SQL Server에서는 `@id`, `@@id` 속성에도 사용 가능

- [`type` 인수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-the-access-type-of-indexes-with-type-postgresql)를 사용하면 PostgreSQL의 기본 `BTree` 접근 방식 외의 인덱스 접근 방법을 지원할 수 있습니다.
  - `@@index` 속성에서 사용 가능
  - PostgreSQL 전용
  - 지원되는 인덱스 접근 방식: `Hash`, `Gist`, `Gin`, `SpGist`, `Brin`

- [`clustered` 인수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-if-indexes-are-clustered-or-non-clustered-with-clustered-sql-server)를 사용하면 제약 조건 또는 인덱스를 clustered 또는 non-clustered로 구성할 수 있습니다.
  - `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용 가능
  - SQL Server 전용

- [`map` 인수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-the-name-of-indexes-with-map)를 사용하면 기본 데이터베이스에서 인덱스 또는 제약 조건의 사용자 지정 이름을 지정할 수 있습니다.
  - `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용 가능
  - 모든 데이터베이스에서 지원

* `length`로 인덱스 길이 구성하기 (MySQL)

`length` 인수는 MySQL 전용이며, `String` 및 `Byte` 타입 컬럼에 대해 인덱스와 제약 조건을 정의할 수 있게 해줍니다. 이러한 타입의 경우, 전체 값이 MySQL의 인덱스 크기 제한을 초과하면 인덱싱할 값의 하위 부분에 대한 최대 길이를 지정해야 합니다. 자세한 내용은 [MySQL 문서](https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html)를 참조하세요.

`length` 인수는 `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용할 수 있습니다.

예를 들어, 다음 데이터 모델은 최대 길이가 3000자인 `id` 필드를 선언합니다:

schema.prisma

```
    model Id {
      id String @id @db.VarChar(3000)
    }
```

이는 MySQL에서 유효하지 않습니다. MySQL 인덱스 저장 한도를 초과하므로 Prisma ORM이 데이터 모델을 거부합니다. 생성된 SQL도 데이터베이스에서 거부됩니다.

```
    CREATE TABLE `Id` (
      `id` VARCHAR(3000) PRIMARY KEY
    )
```

`length` 인수를 사용하면 `id` 값의 일부만 기본 키를 나타내도록 지정할 수 있습니다. 아래 예제에서는 처음 100자를 사용합니다:

schema.prisma

```
    model Id {
      id String @id(length: 100) @db.VarChar(3000)
    }
```

Prisma Migrate는 데이터 모델에 지정된 경우 `length` 인수를 포함한 제약 조건과 인덱스를 생성할 수 있습니다. 즉, Prisma 스키마 타입 `Byte` 및 `String` 값에 대해 인덱스와 제약 조건을 생성할 수 있습니다. 인수를 지정하지 않으면 기존과 같이 인덱스가 전체 값을 포함하는 것으로 처리됩니다.

Introspection은 기존 데이터베이스에 이러한 제한이 있으면 이를 가져옵니다. 이를 통해 Prisma ORM은 이전에 억제되던 인덱스와 제약 조건을 지원할 수 있으며, 이 기능을 사용하는 MySQL 데이터베이스 지원이 개선됩니다.

`length` 인수는 아래 예시처럼 `@@id` 속성을 사용해 복합 기본 키에도 사용할 수 있습니다:

schema.prisma

```
    model CompoundId {
      id_1 String @db.VarChar(3000)
      id_2 String @db.VarChar(3000)

      @@id([id_1(length: 100), id_2(length: 10)])
    }
```

유사한 문법을 `@@unique` 및 `@@index` 속성에도 사용할 수 있습니다.

- `sort`로 인덱스 정렬 순서 구성하기

`sort` 인수를 사용하면 인덱스 또는 제약 조건의 항목이 데이터베이스에 저장되는 순서를 지정할 수 있습니다. 이는 특정 쿼리에서 데이터베이스가 인덱스를 사용할 수 있는지에 영향을 줄 수 있습니다. 동작과 지원 범위는 데이터베이스별로 다릅니다:

- MySQL/MariaDB에서는 고유 제약 조건과 인덱스에 정렬 순서(`ASC`/`DESC`)를 직접 지정할 수 있습니다.
- PostgreSQL에서는 정렬 순서를 인덱스에만 지정할 수 있고, 고유 제약 조건에는 지정할 수 없습니다.
- SQL Server에서는 `@id`, `@@id`를 포함한 모든 제약 조건과 인덱스에서 정렬 순서를 지원합니다.

예를 들어 MySQL/MariaDB에서 다음 테이블은 내림차순 고유 제약 조건을 사용합니다:

```
    CREATE TABLE `Unique` (
      `unique` INT,
      CONSTRAINT `Unique_unique_key` UNIQUE (`unique` DESC)
    )
```

이는 다음과 같이 introspection됩니다.

schema.prisma

```
    model Unique {
      unique Int @unique(sort: Desc)
    }
```

PostgreSQL에서는 고유 제약 조건에 정렬 순서를 직접 지정할 수는 없지만, 고유성을 강제하는 정렬 순서가 있는 고유 인덱스를 만들 수 있다는 점에 유의하세요:

```
    -- PostgreSQL approach
    CREATE UNIQUE INDEX "unique_index_desc" ON "Unique" ("unique" DESC);
```

`sort` 인수는 복합 인덱스에서도 사용할 수 있습니다:

schema.prisma

```
    model CompoundUnique {
      unique_1 Int
      unique_2 Int

      @@unique([unique_1(sort: Desc), unique_2])
    }
```

- 예제: `sort`와 `length` 함께 사용하기

다음 예제는 `Post` 모델의 인덱스와 제약 조건을 구성하기 위해 `sort` 및 `length` 인수를 사용하는 방법을 보여줍니다:

schema.prisma

```
    model Post {
      title      String   @db.VarChar(300)
      abstract   String   @db.VarChar(3000)
      slug       String   @unique(sort: Desc, length: 42) @db.VarChar(3000)
      author     String
      created_at DateTime

      @@id([title(length: 100, sort: Desc), abstract(length: 10)])
      @@index([author, created_at(sort: Desc)])
    }
```

- `type`으로 인덱스 접근 타입 구성하기 (PostgreSQL)

`type` 인수는 PostgreSQL에서 `@@index` 속성을 사용해 인덱스 타입을 구성할 때 사용할 수 있습니다. 사용 가능한 인덱스 접근 방식은 `Hash`, `Gist`, `Gin`, `SpGist`, `Brin`이며, 기본 `BTree` 인덱스 접근 방식도 포함됩니다.

#

- Hash

`Hash` 타입은 인덱스 데이터를 훨씬 더 빠르게 검색하고 삽입할 수 있는 형식으로 저장하며, 디스크 공간도 더 적게 사용합니다. 하지만 `=` 및 `<>` 비교만 인덱스를 사용할 수 있으므로 `<`, `>` 같은 다른 비교 연산자는 기본 `BTree` 타입보다 `Hash`에서 훨씬 느립니다.

예를 들어, 다음 모델은 `value` 필드에 `type`이 `Hash`인 인덱스를 추가합니다:

schema.prisma

```
    model Example {
      id    Int @id
      value Int

      @@index([value], type: Hash)
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE "Example" (
      id INT PRIMARY KEY,
      value INT NOT NULL
    );

    CREATE INDEX "Example_value_idx" ON "Example" USING HASH (value);
```

#

- Generalized Inverted Index (GIN)

GIN 인덱스는 배열이나 `JsonB` 데이터 같은 복합 값을 저장합니다. 이는 한 객체가 다른 객체의 일부인지 조회하는 쿼리를 가속하는 데 유용합니다. 전체 텍스트 검색에 일반적으로 사용됩니다.

인덱싱된 필드는 연산자 클래스를 정의할 수 있으며, 이 클래스는 인덱스가 처리할 연산자를 정의합니다.

인덱싱할 값을 결정하기 위해 함수(예: `to_tsvector`)를 사용하는 인덱스는 아직 Prisma ORM에서 지원되지 않습니다. 이 방식으로 정의된 인덱스는 `prisma db pull`에서 보이지 않습니다.

예를 들어, 다음 모델은 `value` 필드에 `Gin` 인덱스를 추가하고, 인덱스를 사용할 수 있는 연산자 클래스로 `JsonbPathOps`를 지정합니다:

schema.prisma

```
    model Example {
      id    Int  @id
      value Json
      //    ^ field type matching the operator class

      @@index([value(ops: JsonbPathOps)], type: Gin)
      //                  ^ operator class      ^ index type
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE "Example" (
      id INT PRIMARY KEY,
      value JSONB NOT NULL
    );

    CREATE INDEX "Example_value_idx" ON "Example" USING GIN (value jsonb_path_ops);
```

`JsonbPathOps`의 일부로 `@>` 연산자가 인덱스에서 처리되므로 `value @> '{"foo": 2}'` 같은 쿼리가 빨라집니다.

#

- GIN에서 지원되는 연산자 클래스

Prisma ORM은 일반적으로 PostgreSQL 10 이상 버전에서 제공하는 연산자 클래스를 지원합니다. 연산자 클래스가 Prisma ORM이 아직 지원하지 않는 필드 타입을 요구하는 경우, 문자열 입력과 함께 `raw` 함수를 사용하면 검증 없이 해당 연산자 클래스를 사용할 수 있습니다.

기본 연산자 클래스(✅로 표시)는 인덱스 정의에서 생략할 수 있습니다.

| 연산자 클래스  | 허용 필드 타입(네이티브 타입) | 기본값 | 기타                        |
| -------------- | ----------------------------- | ------ | --------------------------- |
| `ArrayOps`     | 모든 배열                     | ✅     | CockroachDB에서도 사용 가능 |
| `JsonbOps`     | `Json` (`@db.JsonB`)          | ✅     | CockroachDB에서도 사용 가능 |
| `JsonbPathOps` | `Json` (`@db.JsonB`)          |        |
| `raw("other")` |                               |        |

기본 제공 연산자 클래스에 대한 자세한 내용은 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/14/gin-builtin-opclasses.html)를 참고하세요.

#

- CockroachDB

CockroachDB에서 지원되는 인덱스 타입은 GIN과 BTree뿐입니다. CockroachDB에서 동작하도록 표시된 연산자 클래스만 해당 데이터베이스에서 허용되며 Prisma ORM에서 지원됩니다. Prisma Schema Language에서는 연산자 클래스를 정의할 수 없습니다. CockroachDB에서는 `ops` 인수가 필요하지도 않고 허용되지도 않습니다.

#

- Generalized Search Tree (GiST)

GiST 인덱스 타입은 사용자 정의 타입용 인덱싱 스킴을 구현할 때 사용됩니다. 기본적으로 GiST 인덱스의 직접적인 용도는 많지 않지만, 예를 들어 B-Tree 인덱스 타입은 GiST 인덱스를 사용해 구축됩니다.

예를 들어, 다음 모델은 `value` 필드에 `Gist` 인덱스를 추가하고, 인덱스를 사용할 연산자로 `InetOps`를 지정합니다:

schema.prisma

```
    model Example {
      id    Int    @id
      value String @db.Inet
      //           ^ native type matching the operator class
      //                                   ^ index type
      //                  ^ operator class

      @@index([value(ops: InetOps)], type: Gist)
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE "Example" (
      id INT PRIMARY KEY,
      value INET NOT NULL
    );

    CREATE INDEX "Example_value_idx" ON "Example" USING GIST (value inet_ops);
```

`value > '10.0.0.2'` 같은 IP 주소 비교 쿼리는 이 인덱스를 사용합니다.

#

- GiST에서 지원되는 연산자 클래스

Prisma ORM은 일반적으로 PostgreSQL 10 이상 버전에서 제공하는 연산자 클래스를 지원합니다. 연산자 클래스가 Prisma ORM이 아직 지원하지 않는 필드 타입을 요구하는 경우, 문자열 입력과 함께 `raw` 함수를 사용하면 검증 없이 해당 연산자 클래스를 사용할 수 있습니다.

| 연산자 클래스  | 허용 필드 타입(허용 네이티브 타입) |
| -------------- | ---------------------------------- |
| `InetOps`      | `String` (`@db.Inet`)              |
| `raw("other")` |

기본 제공 연산자 클래스에 대한 자세한 내용은 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/14/gist-builtin-opclasses.html)를 참고하세요.

#

- Space-Partitioned GiST (SP-GiST)

SP-GiST 인덱스는 다양한 비균형 데이터 구조에 적합한 선택입니다. 쿼리가 파티셔닝 규칙과 일치하면 매우 빠를 수 있습니다.

GiST와 마찬가지로 SP-GiST는 사용자 정의 타입을 위한 핵심 구성 요소로 중요하며, 데이터베이스와 함께 사용자 정의 검색 연산자를 직접 구현할 수 있게 합니다.

예를 들어, 다음 모델은 `value` 필드에 `SpGist` 인덱스를 추가하고, 인덱스를 사용할 연산자로 `TextOps`를 지정합니다:

schema.prisma

```
    model Example {
      id    Int    @id
      value String
      //    ^ field type matching the operator class

      @@index([value], type: SpGist)
      //                     ^ index type
      //       ^ using the default ops: TextOps
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE "Example" (
      id INT PRIMARY KEY,
      value TEXT NOT NULL
    );

    CREATE INDEX "Example_value_idx" ON "Example" USING SPGIST (value);
```

`value LIKE 'something%'` 같은 쿼리는 이 인덱스로 인해 더 빨라집니다.

#

- SP-GiST에서 지원되는 연산자 클래스

Prisma ORM은 일반적으로 PostgreSQL 10 이상 버전에서 제공되는 연산자 클래스를 지원합니다. 연산자 클래스에 Prisma ORM이 아직 지원하지 않는 필드 타입이 필요한 경우, 문자열 입력과 함께 `raw` 함수를 사용하면 검증 없이 이러한 연산자 클래스를 사용할 수 있습니다.

기본 연산자 클래스(✅로 표시)는 인덱스 정의에서 생략할 수 있습니다.

| 연산자 클래스  | 허용되는 필드 타입(네이티브 타입)    | 기본값 | 지원되는 PostgreSQL 버전 |
| -------------- | ------------------------------------ | ------ | ------------------------ |
| `InetOps`      | `String` (`@db.Inet`)                | ✅     | 10+                      |
| `TextOps`      | `String` (`@db.Text`, `@db.VarChar`) | ✅     |
| `raw("other")` |                                      |        |

기본 제공 연산자 클래스에 대한 자세한 내용은 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/14/spgist-builtin-opclasses.html)를 참고하세요.

#

- 블록 범위 인덱스(BRIN)

BRIN 인덱스 유형은 삽입 후 변경되지 않는 대량의 데이터(예: 날짜 및 시간 값)가 있을 때 유용합니다. 데이터가 인덱스에 잘 맞으면, 매우 적은 공간으로 대규모 데이터셋을 저장할 수 있습니다.

예를 들어, 다음 모델은 `value` 필드에 `Int4BloomOps`를 인덱스를 사용할 연산자로 지정한 `Brin` 인덱스를 추가합니다.

schema.prisma

```
    model Example {
      id    Int @id
      value Int
      //    ^ field type matching the operator class

      @@index([value(ops: Int4BloomOps)], type: Brin)
      //                  ^ operator class      ^ index type
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE "Example" (
      id INT PRIMARY KEY,
      value INT4 NOT NULL
    );

    CREATE INDEX "Example_value_idx" ON "Example" USING BRIN (value int4_bloom_ops);
```

이제 `value = 2` 같은 쿼리는 인덱스를 사용하며, `BTree` 또는 `Hash` 인덱스 대비 일부 공간만 사용합니다.

#

- BRIN에서 지원되는 연산자 클래스

Prisma ORM은 일반적으로 PostgreSQL 10 이상 버전에서 제공되는 연산자 클래스를 지원하며, 일부 지원 연산자는 PostgreSQL 14 이상에서만 사용할 수 있습니다. 연산자 클래스에 Prisma ORM이 아직 지원하지 않는 필드 타입이 필요한 경우, 문자열 입력과 함께 `raw` 함수를 사용하면 검증 없이 이러한 연산자 클래스를 사용할 수 있습니다.

기본 연산자 클래스(✅로 표시)는 인덱스 정의에서 생략할 수 있습니다.

| 연산자 클래스               | 허용되는 필드 타입(네이티브 타입)    | 기본값 | 지원되는 PostgreSQL 버전 |
| --------------------------- | ------------------------------------ | ------ | ------------------------ |
| `BitMinMaxOps`              | `String` (`@db.Bit`)                 | ✅     |
| `VarBitMinMaxOps`           | `String` (`@db.VarBit`)              | ✅     |
| `BpcharBloomOps`            | `String` (`@db.Char`)                |        | 14+                      |
| `BpcharMinMaxOps`           | `String` (`@db.Char`)                | ✅     |
| `ByteaBloomOps`             | `Bytes` (`@db.Bytea`)                |        | 14+                      |
| `ByteaMinMaxOps`            | `Bytes` (`@db.Bytea`)                | ✅     |
| `DateBloomOps`              | `DateTime` (`@db.Date`)              |        | 14+                      |
| `DateMinMaxOps`             | `DateTime` (`@db.Date`)              | ✅     |
| `DateMinMaxMultiOps`        | `DateTime` (`@db.Date`)              |        | 14+                      |
| `Float4BloomOps`            | `Float` (`@db.Real`)                 |        | 14+                      |
| `Float4MinMaxOps`           | `Float` (`@db.Real`)                 | ✅     |
| `Float4MinMaxMultiOps`      | `Float` (`@db.Real`)                 |        | 14+                      |
| `Float8BloomOps`            | `Float` (`@db.DoublePrecision`)      |        | 14+                      |
| `Float8MinMaxOps`           | `Float` (`@db.DoublePrecision`)      | ✅     |
| `Float8MinMaxMultiOps`      | `Float` (`@db.DoublePrecision`)      |        | 14+                      |
| `InetInclusionOps`          | `String` (`@db.Inet`)                | ✅     | 14+                      |
| `InetBloomOps`              | `String` (`@db.Inet`)                |        | 14+                      |
| `InetMinMaxOps`             | `String` (`@db.Inet`)                |        |
| `InetMinMaxMultiOps`        | `String` (`@db.Inet`)                |        | 14+                      |
| `Int2BloomOps`              | `Int` (`@db.SmallInt`)               |        | 14+                      |
| `Int2MinMaxOps`             | `Int` (`@db.SmallInt`)               | ✅     |
| `Int2MinMaxMultiOps`        | `Int` (`@db.SmallInt`)               |        | 14+                      |
| `Int4BloomOps`              | `Int` (`@db.Integer`)                |        | 14+                      |
| `Int4MinMaxOps`             | `Int` (`@db.Integer`)                | ✅     |
| `Int4MinMaxMultiOps`        | `Int` (`@db.Integer`)                |        | 14+                      |
| `Int8BloomOps`              | `BigInt` (`@db.BigInt`)              |        | 14+                      |
| `Int8MinMaxOps`             | `BigInt` (`@db.BigInt`)              | ✅     |
| `Int8MinMaxMultiOps`        | `BigInt` (`@db.BigInt`)              |        | 14+                      |
| `NumericBloomOps`           | `Decimal` (`@db.Decimal`)            |        | 14+                      |
| `NumericMinMaxOps`          | `Decimal` (`@db.Decimal`)            | ✅     |
| `NumericMinMaxMultiOps`     | `Decimal` (`@db.Decimal`)            |        | 14+                      |
| `OidBloomOps`               | `Int` (`@db.Oid`)                    |        | 14+                      |
| `OidMinMaxOps`              | `Int` (`@db.Oid`)                    | ✅     |
| `OidMinMaxMultiOps`         | `Int` (`@db.Oid`)                    |        | 14+                      |
| `TextBloomOps`              | `String` (`@db.Text`, `@db.VarChar`) |        | 14+                      |
| `TextMinMaxOps`             | `String` (`@db.Text`, `@db.VarChar`) | ✅     |
| `TextMinMaxMultiOps`        | `String` (`@db.Text`, `@db.VarChar`) |        | 14+                      |
| `TimestampBloomOps`         | `DateTime` (`@db.Timestamp`)         |        | 14+                      |
| `TimestampMinMaxOps`        | `DateTime` (`@db.Timestamp`)         | ✅     |
| `TimestampMinMaxMultiOps`   | `DateTime` (`@db.Timestamp`)         |        | 14+                      |
| `TimestampTzBloomOps`       | `DateTime` (`@db.Timestamptz`)       |        | 14+                      |
| `TimestampTzMinMaxOps`      | `DateTime` (`@db.Timestamptz`)       | ✅     |
| `TimestampTzMinMaxMultiOps` | `DateTime` (`@db.Timestamptz`)       |        | 14+                      |
| `TimeBloomOps`              | `DateTime` (`@db.Time`)              |        | 14+                      |
| `TimeMinMaxOps`             | `DateTime` (`@db.Time`)              | ✅     |
| `TimeMinMaxMultiOps`        | `DateTime` (`@db.Time`)              |        | 14+                      |
| `TimeTzBloomOps`            | `DateTime` (`@db.Timetz`)            |        | 14+                      |
| `TimeTzMinMaxOps`           | `DateTime` (`@db.Timetz`)            | ✅     |
| `TimeTzMinMaxMultiOps`      | `DateTime` (`@db.Timetz`)            |        | 14+                      |
| `UuidBloomOps`              | `String` (`@db.Uuid`)                |        | 14+                      |
| `UuidMinMaxOps`             | `String` (`@db.Uuid`)                | ✅     |
| `UuidMinMaxMultiOps`        | `String` (`@db.Uuid`)                |        | 14+                      |
| `raw("other")`              |                                      |        |

기본 제공 연산자 클래스에 대한 자세한 내용은 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/14/brin-builtin-opclasses.html)를 참고하세요.

- `clustered`로 인덱스를 clustered/non-clustered로 구성하기(SQL Server)

`clustered` 인수는 SQL Server에서 (non)clustered 인덱스를 구성하기 위해 사용할 수 있습니다. `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용할 수 있습니다.

예를 들어, 다음 모델은 `@id`를 clustered 기본값 대신 non-clustered로 구성합니다.

schema.prisma

```
    model Example {
      id    Int @id(clustered: false)
      value Int
    }
```

이는 다음 SQL 명령으로 변환됩니다:

```
    CREATE TABLE [Example] (
      id INT NOT NULL,
      value INT,
      CONSTRAINT [Example_pkey] PRIMARY KEY NONCLUSTERED (id)
    )
```

각 속성에 대한 `clustered`의 기본값은 다음과 같습니다.

| 속성       | 값      |
| ---------- | ------- |
| `@id`      | `true`  |
| `@@id`     | `true`  |
| `@unique`  | `false` |
| `@@unique` | `false` |
| `@@index`  | `false` |

테이블은 clustered 인덱스를 최대 하나만 가질 수 있습니다.

- `map`으로 인덱스 이름 구성하기

`map` 인수를 사용하면 기본 데이터베이스의 인덱스 또는 제약 조건에 사용자 지정 이름을 지정할 수 있습니다. 특정 네이밍 규칙을 사용하고 싶거나 자동 생성된 이름이 요구 사항에 맞지 않을 때 유용합니다.

`map` 인수는 `@id`, `@@id`, `@unique`, `@@unique`, `@@index` 속성에서 사용할 수 있습니다.

예를 들어, 다음 모델은 `title` 필드의 인덱스에 사용자 지정 이름을 구성합니다.

schema.prisma

```
    model Post {
      id    Int    @id
      title String

      @@index([title], map: "my_custom_index_name")
    }
```

이는 다음 SQL 명령으로 변환됩니다(PostgreSQL 예시):

```
    CREATE INDEX "my_custom_index_name" ON "Post" ("title");
```

`map` 인수가 없으면 Prisma는 `Post_title_idx` 같은 기본 이름을 생성합니다.

`map` 인수는 고유 제약 조건에도 사용할 수 있습니다.

schema.prisma

```
    model User {
      id    Int    @id
      email String @unique(map: "unique_user_email")
    }
```

그리고 복합 인덱스 및 제약 조건에도 사용할 수 있습니다.

schema.prisma

```
    model Post {
      id        Int    @id
      title     String
      author    String
      createdAt DateTime

      @@index([author, createdAt], map: "posts_author_date_idx")
      @@unique([title, author], map: "posts_title_author_unique")
    }
```

- `where`로 부분 인덱스 구성하기

`where` 인수를 사용하면 [부분 인덱스](https://www.postgresql.org/docs/current/indexes-partial.html)(필터링 인덱스라고도 함)를 정의할 수 있습니다. 부분 인덱스는 지정된 조건과 일치하는 행만 포함하므로 인덱스 크기를 줄이고, 인덱싱된 데이터 하위 집합에 대해 쓰기 성능과 쿼리 성능을 모두 향상시킵니다.

`where` 인수는 `@unique`, `@@unique`, `@@index` 속성에서 사용할 수 있습니다. 이 기능을 사용하려면 `partialIndexes` Preview 기능이 필요합니다.

부분 인덱스는 **PostgreSQL**, **SQLite**, **SQL Server**, **CockroachDB**에서 지원됩니다. MySQL에서는 **지원되지 않습니다**.

#

- `partialIndexes` Preview 기능 활성화

부분 인덱스를 사용하려면 `schema.prisma` 파일의 `generator` 블록에 `partialIndexes` 기능 플래그를 추가하세요.

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["partialIndexes"]
    }
```

#

- `raw()`를 사용한 Raw SQL 구문

`raw()` 함수를 사용해 raw SQL predicate 문자열로 부분 인덱스를 정의할 수 있습니다. 이 접근 방식은 데이터베이스가 허용하는 모든 유효한 SQL `WHERE` 표현식을 지원합니다.

schema.prisma

```
    model User {
      id        Int       @id
      email     String
      status    String
      deletedAt DateTime?

      @@unique([email], where: raw("status = 'active'"))
      @@index([email], where: raw("\"deletedAt\" IS NULL"))
    }
```

이렇게 하면 다음과 같은 SQL이 생성됩니다.

**PostgreSQL:**

```
    CREATE UNIQUE INDEX "User_email_key" ON "User" ("email") WHERE (status = 'active');
    CREATE INDEX "User_email_idx" ON "User" ("email") WHERE ("deletedAt" IS NULL);
```

**SQLite:**

```
    CREATE UNIQUE INDEX "User_email_key" ON "User" ("email") WHERE status = 'active';
    CREATE INDEX "User_email_idx" ON "User" ("email") WHERE "deletedAt" IS NULL;
```

**SQL Server:**

```
    CREATE UNIQUE NONCLUSTERED INDEX [User_email_key] ON [dbo].[User]([email]) WHERE ([status]='active');
    CREATE NONCLUSTERED INDEX [User_email_idx] ON [dbo].[User]([email]) WHERE ([deletedAt] IS NULL);
```

`raw()` 구문은 데이터베이스가 지원하는 모든 SQL 표현식과 함께 사용할 수 있어 가장 유연한 옵션입니다.

#

- 객체 리터럴 구문(타입 안전 대안)

객체 리터럴 구문으로도 부분 인덱스를 정의할 수 있으며, Prisma 스키마를 기준으로 필드 이름과 값 타입을 검증해 타입 안전성을 제공합니다.

schema.prisma

```
    model Post {
      id        Int      @id
      title     String
      published Boolean

      @@index([title], where: { published: true })
      @@unique([title], where: { published: true })
    }
```

객체 리터럴 구문은 다음 값 타입을 지원합니다.

| 값 타입          | 예시                                     | 참고                                            |
| ---------------- | ---------------------------------------- | ----------------------------------------------- |
| `Boolean`        | `{ active: true }`, `{ deleted: false }` | `Boolean` 필드용                                |
| `String`         | `{ status: "active" }`                   | `String`, `DateTime`, `Enum` 필드용             |
| `Number`         | `{ priority: 1 }`, `{ score: 1.5 }`      | `Int`, `BigInt`, `Float`, `Decimal` 필드용      |
| `null`           | `{ deletedAt: null }`                    | `IS NULL`로 변환됨. 모든 nullable 필드에서 동작 |
| `{ not: value }` | `{ deletedAt: { not: null } }`           | 부정 조건. `IS NOT NULL` 또는 `!= value`로 변환 |

하나의 객체에 여러 조건을 결합할 수 있습니다.

schema.prisma

```
    model User {
      id        Int       @id
      email     String
      active    Boolean
      deletedAt DateTime?

      @@unique([email], where: { active: true, deletedAt: null })
    }
```

객체 리터럴 구문은 필드 타입을 검증합니다. 예를 들어 `String` 필드에 `Boolean` 값을 사용할 수 없습니다. 객체 구문이 지원하지 않는 타입의 필드(예: `Unsupported` 또는 복합 타입)의 경우 `raw()`를 대신 사용하세요.

#

- 다른 인덱스 인수와 함께 `where` 사용

`where` 인수는 `name`, `map` 같은 다른 인덱스 인수와 함께 사용할 수 있습니다.

schema.prisma

```
    model User {
      id     Int    @id
      email  String
      status String

      @@unique([email], name: "email_active_unique", map: "idx_email_active", where: raw("status = 'active'"))
    }
```

#

- 데이터베이스별 동작

| 데이터베이스 | 마이그레이션 | 인트로스펙션 | 참고                                                          |
| ------------ | ------------ | ------------ | ------------------------------------------------------------- |
| PostgreSQL   | 완전 지원    | 완전 지원    | predicate 완전 지원                                           |
| SQLite       | 완전 지원    | 완전 지원    | predicate 완전 지원                                           |
| SQL Server   | 완전 지원    | 완전 지원    | `CREATE INDEX`를 통한 필터링 인덱스                           |
| CockroachDB  | 생성만 지원  | 지원 안 함   | predicate 텍스트 인트로스펙션 불가, predicate 수정 감지 안 됨 |
| MySQL        | 지원 안 함   | 지원 안 함   | 데이터베이스에서 부분 인덱스를 지원하지 않음                  |

**CockroachDB 제한 사항**: CockroachDB는 부분 인덱스 생성은 지원하지만, 기존 인덱스에서 predicate 텍스트를 인트로스펙션할 수 없습니다. 즉, 최초 생성 이후 `where` 절 수정(predicate 추가, 변경, 제거)은 Prisma Migrate에서 감지되지 않습니다. differ는 CockroachDB에서 false-positive 마이그레이션을 방지하기 위해 predicate 비교를 건너뜁니다.

#

- 인트로스펙션

부분 인덱스를 포함한 데이터베이스에서 `prisma db pull`을 실행하면 Prisma ORM은 다음을 수행합니다.

1. generator 블록의 `previewFeatures` 목록에 `"partialIndexes"`를 자동으로 추가합니다.
2. 데이터베이스의 정규화된 SQL 표현식 형태를 사용해 부분 인덱스 predicate를 `raw()` 구문으로 표현합니다.

예를 들어 PostgreSQL의 단일 필드 부분 고유 인덱스는 다음과 같이 인트로스펙션됩니다.

schema.prisma

```
    model User {
      id     Int    @id
      email  String @unique(where: raw("(status = 'active'::text)"))
      status String
    }
```

인트로스펙션된 `raw()` 문자열은 SQL 표현식의 데이터베이스 정규화 형태를 반영하므로, 처음 작성한 형태와 다를 수 있습니다. 예를 들어 PostgreSQL은 괄호와 명시적 타입 캐스트(예: `'active'::text`)를 추가하고, SQL Server는 컬럼명을 대괄호로 감싸고 괄호를 추가하며(예: `([status]='active')`), SQLite는 일반적으로 원래 표현식을 그대로 유지합니다.

## 전문 텍스트 인덱스 (MySQL 및 MongoDB)

`fullTextIndex` 프리뷰 기능은 MySQL 및 MongoDB에서 전문 텍스트 인덱스의 인트로스펙션과 마이그레이션을 지원합니다. 이는 `@@fulltext` 속성을 사용해 구성할 수 있습니다. 데이터베이스에 기존에 있던 전문 텍스트 인덱스는 `db pull`로 인트로스펙션한 뒤 Prisma 스키마에 추가되며, Prisma 스키마에 새로 추가한 전문 텍스트 인덱스는 Prisma Migrate를 사용할 때 데이터베이스에 생성됩니다.

현재는 MongoDB용 Prisma Client에서 전문 텍스트 검색 명령을 활성화하지 않았습니다. 진행 상황은 [MongoDB](https://github.com/prisma/prisma/issues/9413) 이슈에서 확인할 수 있습니다.

- `fullTextIndex` 프리뷰 기능 활성화

`fullTextIndex` 프리뷰 기능을 활성화하려면 `schema.prisma` 파일의 `generator` 블록에 `fullTextIndex` 기능 플래그를 추가하세요:

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["fullTextIndex"]
    }
```

- 예제

다음 예제는 `Post` 모델의 `title` 및 `content` 필드에 `@@fulltext` 인덱스를 추가하는 방법을 보여줍니다:

schema.prisma

```
    model Post {
      id      Int    @id
      title   String @db.VarChar(255)
      content String @db.Text

      @@fulltext([title, content])
    }
```

MongoDB에서는 `sort` 인수와 함께 `@@fulltext` 인덱스 속성(`fullTextIndex` 프리뷰 기능을 통해 제공)을 사용하여 전문 텍스트 인덱스에 필드를 오름차순 또는 내림차순으로 추가할 수 있습니다. 다음 예제는 `Post` 모델의 `title` 및 `content` 필드에 `@@fulltext` 인덱스를 추가하고, `title` 필드를 내림차순으로 정렬합니다:

schema.prisma

```
    generator js {
      provider        = "prisma-client-js"
      previewFeatures = ["fullTextIndex"]
    }

    datasource db {
      provider = "mongodb"
      url      = env("DATABASE_URL")
    }

    model Post {
      id      String @id @map("_id") @db.ObjectId
      title   String
      content String

      @@fulltext([title(sort: Desc), content])
    }
```
