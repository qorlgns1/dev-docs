---
title: "Raw SQL comparisons"
description: "Compare columns of the same table with raw queries in Prisma ORM"
---

Source URL: https://docs.prisma.io/docs/orm/more/troubleshooting/raw-sql-comparisons

# Raw SQL comparisons

Compare columns of the same table with raw queries in Prisma ORM

Comparing different columns from the same table is a common scenario. This page shows how to achieve this using raw queries for Prisma ORM versions prior to 4.3.0.

From version 4.3.0, you do not need to use raw queries to compare columns in the same table. You can use the `<model>.fields` property to [compare the columns](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#compare-columns-in-the-same-table).

## Comparing numeric values

Example: retrieving posts that have more comments than likes.

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

## Comparing date values

Example: get all projects completed after the due date.

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
