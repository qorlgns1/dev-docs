---
title: "데이터베이스 매핑"
description: "모델 및 필드 이름을 데이터베이스 테이블 및 컬럼에 매핑하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping

# 데이터베이스 매핑

모델 및 필드 이름을 데이터베이스 테이블 및 컬럼에 매핑하는 방법을 알아보세요

[Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에는 특정 데이터베이스 객체의 이름을 정의할 수 있게 해주는 메커니즘이 포함되어 있습니다. 다음을 할 수 있습니다.

- 모델 및 필드 이름을 다른 컬렉션/테이블 및 필드/컬럼 이름에 매핑
- 제약 조건 및 인덱스 이름 정의

## 컬렉션/테이블 및 필드/컬럼 이름 매핑

때때로 데이터베이스에서 엔티티를 설명하는 데 사용되는 이름이, 생성된 API에서 선호하는 이름과 일치하지 않을 수 있습니다. Prisma schema에서 이름 매핑을 사용하면, 기본 데이터베이스 이름을 변경하지 않고도 Client API의 네이밍에 영향을 줄 수 있습니다.

예를 들어 데이터베이스에서 테이블/컬렉션 이름을 짓는 일반적인 방식은 복수형과 [snake_case](https://en.wikipedia.org/wiki/Snake_case) 표기법을 사용하는 것입니다. 그러나 Prisma는 다른 [네이밍 규칙(단수형, PascalCase)](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#naming-conventions)을 권장합니다.

`@map` 및 `@@map`을 사용하면, 기본 데이터베이스의 테이블/컬럼 이름과 모델/필드 이름을 분리하여 [Prisma Client API의 형태를 조정](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)할 수 있습니다.

- 컬렉션 / 테이블 이름 매핑

예를 들어 `comments`라는 테이블이 있는 데이터베이스를 [introspect](https://docs.prisma.io/docs/orm/prisma-schema/introspection)하면, 결과 Prisma 모델은 다음과 같이 보입니다:

```
    model comments {
      // Fields
    }
```

하지만 [`@@map`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성을 사용하면 데이터베이스의 기본 `comments` 테이블 이름은 바꾸지 않고도 모델 이름을 `Comment`(예: 네이밍 규칙 준수)로 선택할 수 있습니다:

```
    model Comment {
      // Fields

      @@map("comments")
    }
```

이렇게 수정된 모델 정의를 사용하면 Prisma Client가 자동으로 `Comment` 모델을 기본 데이터베이스의 `comments` 테이블에 매핑합니다.

- 필드 / 컬럼 이름 매핑

컬럼/필드 이름도 [`@map`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#map)할 수 있습니다:

```
    model Comment {
      content String @map("comment_text")
      email   String @map("commenter_email")
      type    Enum   @map("comment_type")

      @@map("comments")
    }
```

이렇게 하면 Prisma Client API에서 `comment_text` 컬럼은 `prisma.comment.comment_text`로는 사용할 수 없고, `prisma.comment.content`를 통해 접근할 수 있습니다.

- enum 이름 및 값 매핑

enum 값에는 `@map`을, enum 자체에는 `@@map`을 사용할 수도 있습니다:

```
    enum Type {
      Blog,
      Twitter @map("comment_twitter")

      @@map("comment_source_enum")
    }
```

이 예시에서:

- `@@map("comment_source_enum")`은 enum 이름 `Type`을 데이터베이스의 `comment_source_enum`에 매핑합니다
- `@map("comment_twitter")`는 enum 값 `Twitter`를 데이터베이스의 `comment_twitter`에 매핑합니다

#

- 생성된 TypeScript에 미치는 영향

enum 값에 `@map`을 사용하면, 생성된 TypeScript enum은 매핑된 값이 아니라 **schema 이름**을 사용합니다:

```
    enum Status {
      PENDING  @map("pending")
      APPROVED @map("approved")
    }
```

그러면 다음과 같은 TypeScript가 생성됩니다:

```
    export const Status = {
      PENDING: "PENDING",
      APPROVED: "APPROVED",
    } as const;
```

즉, `Status.PENDING`은 `"pending"`이 아니라 `"PENDING"`으로 평가됩니다. 매핑은 데이터베이스 레벨에서만 처리됩니다.

## 제약 조건 및 인덱스 이름

선택적으로 `map` 인수를 사용해 Prisma schema에서 [`@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#id), [`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference), [`@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unique), [`@@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference), [`@@index`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#index), [`@relation`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#relation) 속성의 **기본 제약 조건 및 인덱스 이름**을 명시적으로 정의할 수 있습니다.

데이터베이스를 introspection할 때, `map` 인수는 이름이 Prisma ORM의 [인덱스 및 제약 조건 기본 네이밍 규칙](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#prisma-orms-default-naming-conventions-for-indexes-and-constraints)과 _다를 때만_ schema에 렌더링됩니다.

- 이름 있는 제약 조건의 사용 사례

제약 조건 이름을 명시적으로 지정하는 사용 사례는 다음과 같습니다.

- 회사 정책
- 다른 도구의 규칙

* Prisma ORM의 인덱스 및 제약 조건 기본 네이밍 규칙

Prisma ORM 네이밍 규칙은 결정론적이기 때문에 PostgreSQL과 맞추도록 선택되었습니다. 또한 많은 데이터베이스가 이미 이 규칙과 일치하므로 이름을 렌더링할 필요가 없는 경우를 최대화하는 데 도움이 됩니다.

Prisma ORM은 기본 인덱스 및 제약 조건 이름을 생성할 때 항상 엔티티의 데이터베이스 이름을 사용합니다. 모델이 데이터 모델에서 `@@map` 또는 `@map`으로 다른 이름에 리매핑되더라도, 기본 이름 생성은 여전히 데이터베이스의 _테이블_ 이름을 입력으로 사용합니다. 필드와 *컬럼*도 동일합니다.

| 엔티티         | 규칙                              | 예시                           |
| -------------- | --------------------------------- | ------------------------------ |
| 기본 키        | {tablename}\_pkey                 | `User_pkey`                    |
| 고유 제약 조건 | {tablename}\_{column_names}\_key  | `User_firstName_last_Name_key` |
| 비고유 인덱스  | {tablename}\_{column_names}\_idx  | `User_age_idx`                 |
| 외래 키        | {tablename}\_{column_names}\_fkey | `User_childName_fkey`          |

대부분의 데이터베이스에는 엔티티 이름 길이 제한이 있으므로, 데이터베이스 제한을 넘지 않도록 필요 시 이름이 잘립니다. 전체 이름이 허용 최대 길이를 넘지 않도록 `_suffix` 앞부분을 필요에 따라 줄입니다.

- 기본 제약 조건 이름 사용

`map` 인수로 명시적 이름을 제공하지 않으면 Prisma ORM은 [기본 네이밍 규칙](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#prisma-orms-default-naming-conventions-for-indexes-and-constraints)을 따라 인덱스와 제약 조건 이름을 생성합니다.

데이터베이스를 introspection하면 인덱스 및 제약 조건 이름이 Prisma ORM의 네이밍 규칙을 따르지 않는 한 schema에 추가됩니다. 규칙을 따르면 schema 가독성을 높이기 위해 이름이 렌더링되지 않습니다. 이런 schema를 migrate할 때 Prisma는 기본 이름을 추론해 데이터베이스에 유지합니다.

#

- 예시

다음 schema는 세 가지 제약 조건(`@id`, `@unique`, `@relation`)과 하나의 인덱스(`@@index`)를 정의합니다:

```
    model User {
      id    Int    @id @default(autoincrement())
      name  String @unique
      posts Post[]
    }

    model Post {
      id         Int    @id @default(autoincrement())
      title      String
      authorName String @default("Anonymous")
      author     User?  @relation(fields: [authorName], references: [name])

      @@index([title, authorName])
    }
```

`map` 인수로 명시적 이름이 제공되지 않았으므로 Prisma는 이것들이 기본 네이밍 규칙을 따른다고 가정합니다.

다음 표는 기본 데이터베이스에서 각 제약 조건과 인덱스의 이름을 보여줍니다:

| 제약 조건 또는 인덱스           | 규칙 준수 여부 | 기본 제약 조건 또는 인덱스 이름 |
| ------------------------------- | -------------- | ------------------------------- |
| `@id` (`User` > `id` 필드)      | 예             | `User_pk`                       |
| `@@index` (`Post`에서)          | 예             | `Post_title_authorName_idx`     |
| `@id` (`Post` > `id` 필드)      | 예             | `Post_pk`                       |
| `@relation` (`Post` > `author`) | 예             | `Post_authorName_fkey`          |

- 사용자 지정 제약 조건 / 인덱스 이름 사용

`map` 인수를 사용해 기본 데이터베이스에서 **사용자 지정 제약 조건 및 인덱스 이름**을 정의할 수 있습니다.

#

- 예시

다음 예시는 하나의 `@id`와 `@@index`에 사용자 지정 이름을 추가합니다:

```
    model User {
      id    Int    @id(map: "Custom_Primary_Key_Constraint_Name") @default(autoincrement())
      name  String @unique
      posts Post[]
    }

    model Post {
      id         Int    @id @default(autoincrement())
      title      String
      authorName String @default("Anonymous")
      author     User?  @relation(fields: [authorName], references: [name])

      @@index([title, authorName], map: "My_Custom_Index_Name")
    }
```

다음 표는 기본 데이터베이스에서 각 제약 조건과 인덱스의 이름을 보여줍니다:

| 제약 조건 또는 인덱스           | 규칙 준수 여부 | 기본 제약 조건 또는 인덱스 이름      |
| ------------------------------- | -------------- | ------------------------------------ |
| `@id` (`User` > `id` 필드)      | 아니요         | `Custom_Primary_Key_Constraint_Name` |
| `@@index` (`Post`에서)          | 아니요         | `My_Custom_Index_Name`               |
| `@id` (`Post` > `id` 필드)      | 예             | `Post_pk`                            |
| `@relation` (`Post` > `author`) | 예             | `Post_authorName_fkey`               |

- 관련: Prisma Client용 인덱스 및 기본 키 이름 지정

`map` 외에도 `@@id` 및 `@@unique` 속성은 선택적 `name` 인수를 받아 Prisma Client API를 사용자 지정할 수 있습니다.

다음과 같은 모델에서:

```
    model User {
      firstName String
      lastName  String

      @@id([firstName, lastName])
    }
```

해당 기본 키를 선택하는 기본 API는 필드 조합으로 생성된 값을 사용합니다:

```
    const user = await prisma.user.findUnique({
      where: {
        firstName_lastName: {
          firstName: "Paul",
          lastName: "Panther",
        },
      },
    });
```

`@@id([firstName, lastName], name: "fullName")`를 지정하면 Prisma Client API는 다음과 같이 변경됩니다:

```
    const user = await prisma.user.findUnique({
      where: {
        fullName: {
          firstName: "Paul",
          lastName: "Panther",
        },
      },
    });
```
