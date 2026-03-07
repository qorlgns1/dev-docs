---
title: "복합 ID 및 고유 제약 조건 다루기"
description: "복합 ID와 고유 제약 조건을 기준으로 읽기, 쓰기, 필터링하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints

# 복합 ID 및 고유 제약 조건 다루기

복합 ID와 고유 제약 조건을 기준으로 읽기, 쓰기, 필터링하는 방법

복합 ID와 복합 고유 제약 조건은 Prisma 스키마에서 [`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 및 [`@@unique`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성을 사용해 정의할 수 있습니다.

**MongoDB는 `@@id`를 지원하지 않습니다**
MongoDB는 복합 ID를 지원하지 않으므로, `@@id` 속성으로 모델을 식별할 수 없습니다.

복합 ID 또는 복합 고유 제약 조건은 두 필드의 결합된 값을 데이터베이스 테이블의 기본 키 또는 식별자로 사용합니다. 다음 예시에서는 `postId` 필드와 `userId` 필드를 `Like` 테이블의 복합 ID로 사용합니다:

```
    model User {
      id    Int    @id @default(autoincrement())
      name  String
      post  Post[]
      likes Like[]
    }

    model Post {
      id      Int    @id @default(autoincrement())
      content String
      User    User?  @relation(fields: [userId], references: [id])
      userId  Int?
      likes   Like[]
    }

    model Like {
      postId Int
      userId Int
      User   User @relation(fields: [userId], references: [id])
      Post   Post @relation(fields: [postId], references: [id])

      @@id([postId, userId])
    }
```

`Like` 테이블에서 레코드를 조회(예: `prisma.like.findMany()` 사용)하면 다음과 같은 객체가 반환됩니다:

```
    {
      "postId": 1,
      "userId": 1
    }
```

응답에는 필드가 두 개뿐이지만, 이 두 필드가 `postId_userId`라는 이름의 복합 ID를 구성합니다.

또한 `@@id` 또는 `@@unique` 속성의 `name` 필드를 사용해 이름 있는 복합 ID 또는 복합 고유 제약 조건을 만들 수 있습니다. 예를 들어:

```
    model Like {
      postId Int
      userId Int
      User   User @relation(fields: [userId], references: [id])
      Post   Post @relation(fields: [postId], references: [id])

      @@id(name: "likeId", [postId, userId])
    }
```

## 복합 ID 및 고유 제약 조건을 사용할 수 있는 위치

복합 ID와 복합 고유 제약 조건은 _고유한_ 데이터를 다룰 때 사용할 수 있습니다.

아래는 쿼리의 `where` 필터에서 복합 ID 또는 복합 고유 제약 조건을 허용하는 Prisma Client 함수 목록입니다:

- `findUnique()`
- `findUniqueOrThrow`
- `delete`
- `update`
- `upsert`

복합 ID와 복합 고유 제약 조건은 `connect` 및 `connectOrCreate`를 사용해 관계형 데이터를 생성할 때도 사용할 수 있습니다.

## 복합 ID 또는 고유 제약 조건으로 레코드 필터링

쿼리 결과에는 복합 ID 또는 고유 제약 조건이 필드로 표시되지 않지만, 이러한 복합 값을 사용해 고유 레코드를 대상으로 쿼리를 필터링할 수 있습니다:

```
    const like = await prisma.like.findUnique({
      where: {
        likeId: {
          userId: 1,
          postId: 1,
        },
      },
    });
```

복합 ID 및 복합 고유 제약 조건 키는 `findUnique()` 및 `findUniqueOrThrow` 같은 _고유_ 쿼리에서만 필터 옵션으로 사용할 수 있습니다. 이러한 필드를 사용할 수 있는 위치 목록은 위의 [섹션](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-composite-ids-and-constraints#where-you-can-use-compound-ids-and-unique-constraints)을 참조하세요.

## 복합 ID 또는 고유 제약 조건으로 레코드 삭제

`delete` 쿼리의 `where` 필터에서 복합 ID 또는 복합 고유 제약 조건을 사용할 수 있습니다:

```
    const like = await prisma.like.delete({
      where: {
        likeId: {
          userId: 1,
          postId: 1,
        },
      },
    });
```

## 복합 ID 또는 고유 제약 조건으로 레코드 업데이트 및 upsert

`update` 쿼리의 `where` 필터에서 복합 ID 또는 복합 고유 제약 조건을 사용할 수 있습니다:

```
    const like = await prisma.like.update({
      where: {
        likeId: {
          userId: 1,
          postId: 1,
        },
      },
      data: {
        postId: 2,
      },
    });
```

또한 `upsert` 쿼리의 `where` 필터에서도 사용할 수 있습니다:

```
    await prisma.like.upsert({
      where: {
        likeId: {
          userId: 1,
          postId: 1,
        },
      },
      update: {
        userId: 2,
      },
      create: {
        userId: 2,
        postId: 1,
      },
    });
```

## 복합 ID 또는 고유 제약 조건으로 관계 쿼리 필터링

복합 ID와 복합 고유 제약 조건은 레코드를 연결해 관계를 만들 때 사용하는 `connect` 및 `connectOrCreate` 키에서도 사용할 수 있습니다.

예를 들어, 다음 쿼리를 살펴보겠습니다:

```
    await prisma.user.create({
      data: {
        name: "Alice",
        likes: {
          connect: {
            likeId: {
              postId: 1,
              userId: 2,
            },
          },
        },
      },
    });
```

`likeId` 복합 ID는 `connect` 객체에서 식별자로 사용되며, 이는 새 사용자 `"Alice"`에 연결될 `Like` 테이블의 레코드를 찾는 데 사용됩니다.

마찬가지로 `likeId`는 `connectOrCreate`의 `where` 필터에서도 사용되어 `Like` 테이블의 기존 레코드를 찾으려고 시도할 수 있습니다:

```
    await prisma.user.create({
      data: {
        name: "Alice",
        likes: {
          connectOrCreate: {
            create: {
              postId: 1,
            },
            where: {
              likeId: {
                postId: 1,
                userId: 1,
              },
            },
          },
        },
      },
    });
```
