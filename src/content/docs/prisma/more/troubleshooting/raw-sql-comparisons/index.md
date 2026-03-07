---
title: "Raw SQL 비교"
description: "Prisma ORM에서 Raw 쿼리로 동일 테이블의 컬럼 비교하기"
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/raw-sql-comparisons

# Raw SQL 비교

Prisma ORM에서 Raw 쿼리로 동일 테이블의 컬럼 비교하기

같은 테이블의 서로 다른 컬럼을 비교하는 것은 흔한 시나리오입니다. 이 페이지에서는 Prisma ORM 4.3.0 이전 버전에서 Raw 쿼리를 사용해 이를 수행하는 방법을 보여줍니다.

4.3.0 버전부터는 같은 테이블의 컬럼을 비교하기 위해 Raw 쿼리를 사용할 필요가 없습니다. `<model>.fields` 속성을 사용해 [컬럼을 비교](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#compare-columns-in-the-same-table)할 수 있습니다.

## 숫자 값 비교

예시: 좋아요 수보다 댓글 수가 더 많은 게시물 가져오기.

```
    model Post {
      id            Int      @id @default(autoincrement())
      createdAt     DateTime @default(now())
      updatedAt     DateTime @updatedAt
      title         String
      content       String?
      published     Boolean  @default(false)
      author        User     @relation(fields: [authorId], references: [id])
      authorId      Int
      likesCount    Int
      commentsCount Int
    }
```

- PostgreSQL / CockroachDB

```
    const response =
      await prisma.$queryRaw`SELECT * FROM "public"."Post" WHERE "likesCount" < "commentsCount";`;
```

- MySQL

```
    const response =
      await prisma.$queryRaw`SELECT * FROM \`public\`.\`Post\` WHERE \`likesCount\` < \`commentsCount\`;`;
```

- SQLite

```
    const response =
      await prisma.$queryRaw`SELECT * FROM "Post" WHERE "likesCount" < "commentsCount";`;
```

## 날짜 값 비교

예시: 마감일 이후에 완료된 모든 프로젝트 가져오기.

```
    model Project {
      id            Int      @id @default(autoincrement())
      title         String
      author        User     @relation(fields: [authorId], references: [id])
      authorId      Int
      dueDate       DateTime
      completedDate DateTime
      createdAt     DateTime @default(now())
    }
```

- PostgreSQL / CockroachDB

```
    const response =
      await prisma.$queryRaw`SELECT * FROM "public"."Project" WHERE "completedDate" > "dueDate";`;
```

- MySQL

```
    const response =
      await prisma.$queryRaw`SELECT * FROM \`public\`.\`Project\` WHERE \`completedDate\` > \`dueDate\`;`;
```

- SQLite

```
    const response =
      await prisma.$queryRaw`SELECT * FROM "Project" WHERE "completedDate" > "dueDate";`;
```
