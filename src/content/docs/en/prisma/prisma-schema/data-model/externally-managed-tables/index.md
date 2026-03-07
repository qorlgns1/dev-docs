---
title: "External tables"
description: "How to declare and use externally managed tables in Prisma ORM"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables

# External tables

How to declare and use externally managed tables in Prisma ORM

## Overview

_Externally managed tables_ (or _external tables_ for short) in Prisma ORM are tables that can be **queried via Prisma Client** but are **ignored by Prisma Migrate**.

Sometimes, you might not want Prisma ORM to manage specific tables—such as ones handled by another team or service.

Some concrete use cases for this are:

- auth services like Clerk or Auth0 that manage specific tables with user and session data
- storage services like Supabase Storage with tables for storing metadata about buckets and objects
- a microservice-based organization where specific teams own specific tables in the database

There may be many other scenarios based on custom organizational constraints or preferences where you may not want Prisma ORM to manage specific tables.

Externally managed tables are currently in [Preview](https://docs.prisma.io/docs/orm/more/releases#preview).

Externally managed tables are frequently used in combination with [multi-schema](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema) database setups. However, this is not a hard requirement. You can have only a single schema in your database and also declare externally managed tables within it.

Prisma ORM will not verify that the structure of the tables in the database and the structures of the Prisma models actually match. On the one hand, it requires the developer to be thorough when updating the Prisma schema (the safest way to do it is by using `prisma db pull`). On the other hand, this flexibility enables you to represent only part of the underlying table in the database (and e.g. not expose _all_ its columns).

## Workflow

If you want to use external tables, here's the main workflow:

1. Declare the name of the external tables in your [Prisma Config file](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)
2. Update your Prisma schema (e.g. via `npx prisma db pull`)
3. Re-generate Prisma Client with `npx prisma generate`
4. You can now query the external table using Prisma Client but it will be ignored by Prisma Migrate
5. When the table gets changed (by whoever owns it):
   1. Re-introspect your database using `npx prisma db pull` or manually update the models in your prisma file
   2. Re-generate Prisma Client with `npx prisma generate`

## Prisma Config syntax

You can specify externally managed tables in your [Prisma Config](https://docs.prisma.io/docs/orm/reference/prisma-config-reference) file via the `tables.external` property:

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      // required when using unstable features
      experimental: {
        externalTables: true,
      },
      // declare the `users` table and `role` enum as external
      tables: {
        external: ["public.users"],
      },
      enums: {
        external: ["public.role"],
      },
    });
```

- Analogous to tables, you can also have externally managed _enums_.
- On PostgreSQL and SQL Server you have to specify the fully qualified table/enum name including the schema name. For example: `public.products` or `auth.users`.
- On MySQL and SQLite, you only have to specify the table name.

## Relationships

Prisma can create and update relationships from tables it manages to externally managed tables.

However, for this Prisma needs to be aware of the structure of those externally managed tables during migration creation. You can provide a SQL script that Prisma will run on its [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database) ahead of all migrations to emulate the external tables and enums during migration creation.

The created placeholder table does not need to have the full structure of the actual table but primary keys need to be present.

If the external table is not referenced by any managed table—that is no managed table contains a foreign key constraint on the external table—you do NOT need to provide any SQL for it in `migrations.initShadowDb`.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
      // required when using unstable features
      experimental: {
        externalTables: true,
      },
      // declare a `users` table
      tables: {
        external: ["public.users"],
      },
      migrations: {
        path: "prisma/migrations",
        // setup the users table for the shadow database
        initShadowDb: ` // [!code ++]
          CREATE TABLE public.users (id SERIAL PRIMARY KEY); // [!code ++]
        `,
      },
    });
```

Relationships from an external table to a managed table, where the external table contains the foreign key constraint on the managed table, are **NOT** managed by Prisma as that would modify the external table.

## Example

Assume you have the following Prisma schema which only contains the `posts` table:

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
      // ...
    }

    datasource db {
      provider = "postgresql"
      // ...
    }

    model posts {
      id          Int       @id @default(autoincrement())
      created_at  DateTime  @default(now())
      title       String
      content     String?
    }
```

You have created that `posts` table already via a prior migration. You now also have a `users` table and `role` enum in your database which you want to treat as externally managed.

So the tables in your PostgreSQL database in the default `public` schema look like this:

```
    -- Enum used by users table
    CREATE TYPE role AS ENUM ('customer', 'support', 'admin');

    -- Users table
    CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) NOT NULL UNIQUE,
      email VARCHAR(100) NOT NULL UNIQUE,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      role role
    );

    -- Posts table
    CREATE TABLE posts (
      id SERIAL PRIMARY KEY,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      title VARCHAR(200) NOT NULL,
      content TEXT
    );
```

- 1\. Declaring externally managed tables in Prisma Config

Enable use of externally managed tables via the `tables.external` property:

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      // declare the `users` table and `role` enum as external
      tables: {
        external: ["public.users"],
      },
      enums: {
        external: ["public.role"],
      },
    });
```

- 2\. Update the Prisma schema

Next, you need to update your Prisma schema. You can do this either:

- by manually creating the models
- or by using [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection):

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

The `users` table is now in your Prisma schema:

```
    model posts {
      id         Int       @id @default(autoincrement())
      created_at DateTime? @default(now()) @db.Timestamp(6)
      title      String    @db.VarChar(200)
      content    String?
    }

    model users {
      id         Int       @id @default(autoincrement())
      username   String    @unique @db.VarChar(50)
      email      String    @unique @db.VarChar(100)
      created_at DateTime? @default(now()) @db.Timestamp(6)
      role       role
    }

    enum role {
      customer
      support
      admin
    }
```

- 3\. Re-generate Prisma Client

In order to be able to query the `users` table, you need to re-generate Prisma Client:

npm

pnpm

yarn

bun

```
    npx prisma generate
```

- 4\. Query the `users` table using Prisma Client

You can now query the external `users` table with Prisma Client:

```
    await prisma.users.findMany();
```

- 5\. Add a relationship

Let's say you now want to add an author relationship from `posts` onto `users`.

First update your Prisma schema.

```
    model posts {
      id         Int       @id @default(autoincrement())
      created_at DateTime? @default(now()) @db.Timestamp(6)
      title      String    @db.VarChar(200)
      content    String?
      author     users @relation(fields: [author_id], references: [id])
      author_id  Int
    }

    model users {
      id         Int       @id @default(autoincrement())
      username   String    @unique @db.VarChar(50)
      email      String    @unique @db.VarChar(100)
      created_at DateTime? @default(now()) @db.Timestamp(6)
      role       role
      posts      posts[]
    }

    enum role {
      customer
      support
      admin
    }
```

Then add a `migrations.initShadowDb` script so Prisma knows about the `users` table during migrations.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      tables: {
        external: ["public.users"],
      },
      migrations: {
        path: "prisma/migrations",
        // setup the users table for the shadow database
        initShadowDb: ` // [!code ++]
          CREATE TABLE public.users (id SERIAL PRIMARY KEY); // [!code ++]
        `,
      },
    });
```

Now you can run `prisma migrate dev` command.
