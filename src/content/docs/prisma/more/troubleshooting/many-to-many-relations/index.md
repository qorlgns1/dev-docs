---
title: "다대다 관계"
description: "Prisma ORM으로 다대다 관계를 모델링, 쿼리, 변환하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/many-to-many-relations

# 다대다 관계

Prisma ORM으로 다대다 관계를 모델링, 쿼리, 변환하는 방법을 알아보세요.

관계형 데이터베이스에서 다대다 관계를 모델링하고 쿼리하는 일은 까다로울 수 있습니다. 이 가이드에서는 [암시적](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations) 및 [명시적](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#explicit-many-to-many-relations) 다대다 관계를 다루는 방법과, 이들 사이를 변환하는 방법을 설명합니다.

## 암시적 관계

암시적 다대다 관계에서는 Prisma ORM이 [관계 테이블](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#relation-table-conventions)을 내부적으로 처리합니다:

```
    model Post {
      id    Int    @id @default(autoincrement())
      title String
      tags  Tag[]
    }

    model Tag {
      id    Int    @id @default(autoincrement())
      name  String @unique
      posts Post[]
    }
```

- 레코드 생성

```
    await prisma.post.create({
      data: {
        title: "Types of relations",
        tags: { create: [{ name: "dev" }, { name: "prisma" }] },
      },
    });
```

- 관계를 포함한 쿼리

```
    await prisma.post.findMany({
      include: { tags: true },
    });
```

결과:

```
    [
      {
        "id": 1,
        "title": "Types of relations",
        "tags": [
          { "id": 1, "name": "dev" },
          { "id": 2, "name": "prisma" }
        ]
      }
    ]
```

- 태그 연결과 생성을 동시에 수행

```
    await prisma.post.update({
      where: { id: 1 },
      data: {
        title: "Prisma is awesome!",
        tags: { set: [{ id: 1 }, { id: 2 }], create: { name: "typescript" } },
      },
    });
```

## 명시적 관계

관계 테이블에 추가 필드를 저장해야 하거나, 기존 데이터베이스를 [introspecting](https://docs.prisma.io/docs/orm/prisma-schema/introspection)할 때는 명시적 관계가 필요합니다:

```
    model Post {
      id    Int        @id @default(autoincrement())
      title String
      tags  PostTags[]
    }

    model PostTags {
      id     Int   @id @default(autoincrement())
      post   Post? @relation(fields: [postId], references: [id])
      tag    Tag?  @relation(fields: [tagId], references: [id])
      postId Int?
      tagId  Int?

      @@index([postId, tagId])
    }

    model Tag {
      id    Int        @id @default(autoincrement())
      name  String     @unique
      posts PostTags[]
    }
```

- 명시적 관계로 레코드 생성

```
    await prisma.post.create({
      data: {
        title: "Types of relations",
        tags: {
          create: [{ tag: { create: { name: "dev" } } }, { tag: { create: { name: "prisma" } } }],
        },
      },
    });
```

- 명시적 관계로 쿼리

```
    await prisma.post.findMany({
      include: { tags: { include: { tag: true } } },
    });
```

- 응답 매핑

암시적 관계와 유사하게 더 깔끔한 응답을 얻으려면:

```
    const result = posts.map((post) => {
      return { ...post, tags: post.tags.map((tag) => tag.tag) };
    });
```

## 암시적 관계를 명시적 관계로 변환

때로는 암시적 관계에서 명시적 관계로 전환해야 할 수 있습니다. 예를 들어 관계에 타임스탬프 같은 메타데이터를 추가하려는 경우입니다.

- 1단계: 명시적 관계 모델 추가

새 모델을 추가하면서 기존 암시적 관계는 유지합니다:

```
    model User {
      id        Int        @id @default(autoincrement())
      name      String
      posts     Post[]
      userPosts UserPost[]
    }

    model Post {
      id        Int        @id @default(autoincrement())
      title     String
      authors   User[]
      userPosts UserPost[]
    }

    model UserPost {
      id        Int       @id @default(autoincrement())
      userId    Int
      postId    Int
      user      User      @relation(fields: [userId], references: [id])
      post      Post      @relation(fields: [postId], references: [id])
      createdAt DateTime  @default(now())

      @@unique([userId, postId])
    }
```

마이그레이션 실행:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name "added explicit relation"
```

- 2단계: 기존 데이터 마이그레이션

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient();

    async function main() {
      const users = await prisma.user.findMany({
        include: { posts: true },
      });

      for (const user of users) {
        for (const post of user.posts) {
          await prisma.userPost.create({
            data: {
              userId: user.id,
              postId: post.id,
            },
          });
        }
      }

      console.log("Data migration completed.");
    }

    main()
      .catch((e) => {
        throw e;
      })
      .finally(async () => {
        await prisma.$disconnect();
      });
```

- 3단계: 암시적 관계 컬럼 제거

데이터 마이그레이션 후 암시적 관계 컬럼을 제거합니다:

```
    model User {
      id        Int        @id @default(autoincrement())
      name      String
      userPosts UserPost[]
    }

    model Post {
      id        Int        @id @default(autoincrement())
      title     String
      userPosts UserPost[]
    }
```

마이그레이션 실행:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name "removed implicit relation"
```

이렇게 하면 암시적 테이블 `_PostToUser`가 삭제됩니다.
