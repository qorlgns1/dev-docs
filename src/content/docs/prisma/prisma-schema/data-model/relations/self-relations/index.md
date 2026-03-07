---
title: "자기 관계"
description: "Prisma에서 자기 관계를 정의하고 사용하는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/self-relations

# 자기 관계

Prisma에서 자기 관계를 정의하고 사용하는 방법입니다.

관계 필드는 자기 자신의 모델을 참조할 수 있으며, 이를 *자기 관계*라고 합니다. 자기 관계는 1-1, 1-n, 또는 m-n 형태가 될 수 있습니다.

자기 관계에는 항상 `@relation` 속성이 필요합니다.

## 일대일 자기 관계

```
    model User {
      id          Int     @id @default(autoincrement())
      name        String?
      successorId Int?    @unique
      successor   User?   @relation("BlogOwnerHistory", fields: [successorId], references: [id])
      predecessor User?   @relation("BlogOwnerHistory")
    }
```

이는 다음을 의미합니다:

- 사용자는 predecessor가 없거나 하나만 가질 수 있습니다
- 사용자는 successor가 없거나 하나만 가질 수 있습니다

**핵심 규칙:**

- 양쪽 모두 동일한 `@relation` 이름을 사용해야 합니다
- 한쪽은 `fields`와 `references`로 완전히 주석 처리되어야 합니다
- 1-1 관계에서는 외래 키에 `@unique`가 필요합니다
- 양쪽 모두 필수(required)로 설정할 수 없습니다 (첫 레코드를 생성할 수 없기 때문)

## 일대다 자기 관계

```
    model User {
      id        Int     @id @default(autoincrement())
      name      String?
      teacherId Int?
      teacher   User?   @relation("TeacherStudents", fields: [teacherId], references: [id])
      students  User[]  @relation("TeacherStudents")
    }
```

이는 다음을 의미합니다:

- 사용자는 teacher가 없거나 한 명만 가질 수 있습니다
- 사용자는 student를 0명 이상 가질 수 있습니다

`teacherId`에는 `@unique` 제약이 없습니다 \- 여러 student가 같은 teacher를 공유할 수 있습니다.

## 다대다 자기 관계

```
    model User {
      id         Int     @id @default(autoincrement())
      name       String?
      followedBy User[]  @relation("UserFollows")
      following  User[]  @relation("UserFollows")
    }
```

이는 다음을 의미합니다:

- 사용자는 0명 이상의 사용자에게 팔로우될 수 있습니다
- 사용자는 0명 이상의 사용자를 팔로우할 수 있습니다

관계형 데이터베이스에서는 이는 암시적 m-n 관계입니다 (Prisma가 관계 테이블을 관리함).

**명시적 버전** (추가 필드를 저장하는 경우):

```
    model User {
      id         Int       @id @default(autoincrement())
      name       String?
      followedBy Follows[] @relation("followedBy")
      following  Follows[] @relation("following")
    }

    model Follows {
      followedBy   User @relation("followedBy", fields: [followedById], references: [id])
      followedById Int
      following    User @relation("following", fields: [followingId], references: [id])
      followingId  Int
      @@id([followingId, followedById])
    }
```

## 동일 모델에서 여러 자기 관계

여러 자기 관계를 조합할 수 있습니다:

```
    model User {
      id         Int     @id @default(autoincrement())
      name       String?
      teacherId  Int?
      teacher    User?   @relation("TeacherStudents", fields: [teacherId], references: [id])
      students   User[]  @relation("TeacherStudents")
      followedBy User[]  @relation("UserFollows")
      following  User[]  @relation("UserFollows")
    }
```
