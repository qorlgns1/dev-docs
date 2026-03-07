---
title: "다대다 관계"
description: "Prisma에서 다대다 관계를 정의하고 사용하는 방법."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations

# 다대다 관계

Prisma에서 다대다 관계를 정의하고 사용하는 방법.

다대다(m-n) 관계는 한쪽의 0개 이상의 레코드와 다른 쪽의 0개 이상의 레코드를 연결합니다. 이는 [암시적](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations)(Prisma가 관계 테이블을 관리)일 수도 있고 [명시적](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#explicit-many-to-many-relations)(사용자가 관계 테이블을 정의)일 수도 있습니다.

## 관계형 데이터베이스

관계 테이블에 추가 메타데이터를 저장해야 하는 경우가 아니라면 [암시적](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations) m-n을 사용하세요.

- 명시적 다대다 관계

관계 테이블은 스키마에서 모델로 표현됩니다:

```
    model Post {
      id         Int                 @id @default(autoincrement())
      title      String
      categories CategoriesOnPosts[]
    }

    model Category {
      id    Int                 @id @default(autoincrement())
      name  String
      posts CategoriesOnPosts[]
    }

    model CategoriesOnPosts {
      post       Post     @relation(fields: [postId], references: [id])
      postId     Int
      category   Category @relation(fields: [categoryId], references: [id])
      categoryId Int
      assignedAt DateTime @default(now())
      assignedBy String
      @@id([postId, categoryId])
    }
```

관계 테이블에는 `assignedAt`, `assignedBy` 같은 추가 필드를 저장할 수 있습니다.

#

- 명시적 다대다 쿼리하기

```
    // Create post with new category
    const post = await prisma.post.create({
      data: {
        title: "How to be Bob",
        categories: {
          create: [
            {
              assignedBy: "Bob",
              category: { create: { name: "New category" } },
            },
          ],
        },
      },
    });

    // Connect to existing categories
    await prisma.post.create({
      data: {
        title: "My Post",
        categories: {
          create: [
            { assignedBy: "Bob", category: { connect: { id: 9 } } },
            { assignedBy: "Bob", category: { connect: { id: 22 } } },
          ],
        },
      },
    });

    // Query posts by category
    const posts = await prisma.post.findMany({
      where: { categories: { some: { category: { name: "New Category" } } } },
    });
```

- 암시적 다대다 관계

Prisma가 관계 테이블을 자동으로 관리합니다:

```
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      categories Category[]
    }

    model Category {
      id    Int    @id @default(autoincrement())
      name  String
      posts Post[]
    }
```

#

- 암시적 다대다 쿼리하기

```
    // Create post with categories
    const post = await prisma.post.create({
      data: {
        title: "How to become a butterfly",
        categories: {
          create: [{ name: "Magic" }, { name: "Butterflies" }],
        },
      },
    });

    // Get posts with categories
    const posts = await prisma.post.findMany({
      include: { categories: true },
    });
```

#

- 암시적 m-n 규칙
  - 두 모델 모두 단일 `@id`를 가져야 함(복합 ID 또는 `@unique` 불가)
  - `@relation` 속성은 필요하지 않음(모호성 해소 시 제외)
  - `@relation`에서 `fields`, `references`, `onUpdate`, `onDelete` 사용 불가

#

- 관계 테이블 규칙

`prisma db pull`이 암시적 m-n 테이블을 인식하려면:

- 테이블 이름: `_CategoryToPost`(언더스코어 + 모델 이름을 알파벳순으로 정렬 + `To`)
- 컬럼: `A`(알파벳순 첫 번째 모델의 FK), `B`(두 번째 모델의 FK)
- 두 컬럼에 대한 고유 인덱스, `B`에 대한 비고유 인덱스

* 관계 테이블 이름 구성

테이블 이름을 사용자 지정하려면 양쪽에 `@relation("MyRelationTable")`을 사용하세요.

## MongoDB

MongoDB에서는 양쪽 모두에 명시적 ID 배열이 필요합니다:

```
    model Post {
      id          String     @id @default(auto()) @map("_id") @db.ObjectId
      categoryIDs String[]   @db.ObjectId
      categories  Category[] @relation(fields: [categoryIDs], references: [id])
    }

    model Category {
      id      String   @id @default(auto()) @map("_id") @db.ObjectId
      name    String
      postIDs String[] @db.ObjectId
      posts   Post[]   @relation(fields: [postIDs], references: [id])
    }
```

- MongoDB m-n 쿼리하기

```
    // Find posts by category IDs
    const posts = await prisma.post.findMany({
      where: { categoryIDs: { hasSome: [id1, id2] } },
    });

    // Find posts by category name
    const posts = await prisma.post.findMany({
      where: { categories: { some: { name: { contains: "Servers" } } } },
    });
```
