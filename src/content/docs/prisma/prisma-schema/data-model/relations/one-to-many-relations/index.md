---
title: "일대다 관계"
description: "Prisma에서 일대다 관계를 정의하고 사용하는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-many-relations

# 일대다 관계

Prisma에서 일대다 관계를 정의하고 사용하는 방법입니다.

일대다(1-n) 관계는 한쪽의 하나의 레코드를 다른 쪽의 0개 이상의 레코드와 연결합니다:

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }

    model Post {
      id       Int  @id @default(autoincrement())
      author   User @relation(fields: [authorId], references: [id])
      authorId Int
    }
```

이는 다음을 의미합니다:

- 사용자는 게시물을 0개 이상 가질 수 있습니다
- 게시물은 항상 작성자를 가져야 합니다

`@unique`를 사용해 ID가 아닌 필드도 참조할 수 있습니다:

```
    model Post {
      id          Int    @id @default(autoincrement())
      authorEmail String
      author      User   @relation(fields: [authorEmail], references: [email])
    }
```

## 다중 필드 관계(관계형 데이터베이스 전용)

```
    model User {
      firstName String
      lastName  String
      post      Post[]
      @@id([firstName, lastName])
    }

    model Post {
      id              Int    @id @default(autoincrement())
      author          User   @relation(fields: [authorFirstName, authorLastName], references: [firstName, lastName])
      authorFirstName String
      authorLastName  String
    }
```

## 데이터베이스에서의 1-n

1-1과 1-n의 차이는, 1-1 관계에서는 외래 키에 `UNIQUE` 제약이 반드시 있어야 한다는 점입니다. `UNIQUE`가 없으면 여러 레코드가 동일한 부모를 가리킬 수 있으므로 1-n이 됩니다.

## 필수 관계 필드와 선택 관계 필드

주석 처리된 관계 필드와 관계 스칼라는 선택 사항일 수도 있고 필수일 수도 있습니다. 리스트 측은 항상 필수입니다.

**선택적 1-n** (`User` 없이 `Post` 생성 가능):

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }

    model Post {
      id       Int   @id @default(autoincrement())
      author   User? @relation(fields: [authorId], references: [id])
      authorId Int?
    }
```

**필수 1-n** (`Post` 생성 시 `User`를 반드시 지정):

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }

    model Post {
      id       Int  @id @default(autoincrement())
      author   User @relation(fields: [authorId], references: [id])
      authorId Int
    }
```
