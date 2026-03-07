---
title: "일대일 관계"
description: "Prisma에서 일대일 관계를 정의하고 사용하는 방법."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/one-to-one-relations

# 일대일 관계

Prisma에서 일대일 관계를 정의하고 사용하는 방법.

일대일(1-1) 관계는 양쪽에서 각각 최대 **하나의** 레코드만 연결합니다. 이 예시에서 `User`와 `Profile`은 1-1 관계를 가집니다:

```
    model User {
      id      Int      @id @default(autoincrement())
      profile Profile?
    }

    model Profile {
      id     Int  @id @default(autoincrement())
      user   User @relation(fields: [userId], references: [id])
      userId Int  @unique // Foreign key with unique constraint
    }
```

이는 다음을 의미합니다:

- 사용자는 프로필을 0개 또는 1개 가질 수 있습니다
- 프로필은 반드시 정확히 한 명의 사용자와 연결되어야 합니다

`@unique`를 사용해 ID가 아닌 필드를 참조할 수도 있습니다:

```
    model Profile {
      id        Int    @id @default(autoincrement())
      user      User   @relation(fields: [userEmail], references: [email])
      userEmail String @unique
    }
```

## 다중 필드 관계(관계형 데이터베이스 전용)

```
    model User {
      firstName String
      lastName  String
      profile   Profile?
      @@id([firstName, lastName])
    }

    model Profile {
      id            Int    @id @default(autoincrement())
      user          User   @relation(fields: [userFirstName, userLastName], references: [firstName, lastName])
      userFirstName String
      userLastName  String
      @@unique([userFirstName, userLastName])
    }
```

## 데이터베이스에서의 1-1

SQL에서 1-1 관계를 만들려면 외래 키에 `UNIQUE` 제약 조건이 필요합니다. 이것이 없으면 1-n 관계가 됩니다.

MongoDB에서는 문서가 ID로 서로를 참조합니다:

```
    // User
    { "_id": { "$oid": "60d58e130011041800d209e1" }, "name": "Bob" }
    // Profile
    { "_id": "...", "bio": "I like drawing.", "userId": { "$oid": "60d58e130011041800d209e1" } }
```

## 필수 및 선택적 1-1 관계 필드

관계 스칼라가 _없는_ 쪽은 선택적이어야 합니다:

```
    model User {
      id      Int      @id @default(autoincrement())
      profile Profile? // No relation scalar - must be optional
    }
```

관계 스칼라가 _있는_ 쪽은 필수 또는 선택적으로 설정할 수 있습니다:

**필수 1-1** (`Profile` 없이 `User`를 생성할 수 없음):

```
    model User {
      id        Int     @id @default(autoincrement())
      profile   Profile @relation(fields: [profileId], references: [id])
      profileId Int     @unique
    }
```

**선택적 1-1** (`Profile` 없이 `User`를 생성할 수 있음):

```
    model User {
      id        Int      @id @default(autoincrement())
      profile   Profile? @relation(fields: [profileId], references: [id])
      profileId Int?     @unique
    }
```

## 외래 키를 저장할 쪽 선택하기

1-1 관계에서는 어느 쪽이 `@relation` 속성과 외래 키를 가질지 선택할 수 있습니다. 두 방식 모두 유효합니다:

**옵션 1:** 외래 키를 `Profile`에 둠

```
    model User {
      id      Int      @id @default(autoincrement())
      profile Profile?
    }

    model Profile {
      id     Int  @id @default(autoincrement())
      user   User @relation(fields: [userId], references: [id])
      userId Int  @unique
    }
```

**옵션 2:** 외래 키를 `User`에 둠

```
    model User {
      id        Int      @id @default(autoincrement())
      profile   Profile? @relation(fields: [profileId], references: [id])
      profileId Int?     @unique
    }

    model Profile {
      id   Int   @id @default(autoincrement())
      user User?
    }
```
