---
title: "Native database functions"
description: "How to enable PostgreSQL native database functions for projects that use Prisma Migrate."
---

Source URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions

# Native database functions

How to enable PostgreSQL native database functions for projects that use Prisma Migrate.

In PostgreSQL, some [native database functions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#native-database-functions) are part of optional extensions. For example, in PostgreSQL versions 12.13 and earlier the `gen_random_uuid()` function is part of the [`pgcrypto`](https://www.postgresql.org/docs/10/pgcrypto.html) extension.

To use a PostgreSQL extension, you must install it on the file system of your database server and then activate the extension. If you use Prisma Migrate, this must be done as part of a migration.

Do not activate extensions outside a migration file if you use Prisma Migrate. The [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database) requires the same extensions. Prisma Migrate creates and deletes the shadow database automatically, so the only way to activate an extension is to include it in a migration file.

In Prisma ORM versions 4.5.0 and later, you can activate the extension by declaring it in your Prisma schema with the [`postgresqlExtensions` preview feature](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions):

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["postgresqlExtensions"]
    }

    datasource db {
      provider   = "postgresql"
      extensions = [pgcrypto]
    }
```

You can then apply these changes to your database with Prisma Migrate. See [How to migrate PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions) for details.

In earlier versions of Prisma ORM, you must instead add a SQL command to your migration file to activate the extension. See [How to install a PostgreSQL extension as part of a migration](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions#how-to-install-a-postgresql-extension-as-part-of-a-migration).

## How to install a PostgreSQL extension as part of a migration

This section describes how to add a SQL command to a migration file to activate a PostgreSQL extension. If you manage PostgreSQL extensions in your Prisma Schema with the `postgresqlExtensions` preview feature instead, see [How to migrate PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions).

The following example demonstrates how to install the `pgcrypto` extension as part of a migration:

- Add the field with the native database function to your schema:

schema.prisma

```
    model User {
     id String @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
    }
```

If you include a cast operator (such as `::TEXT`), you must surround the entire function with parentheses:

schema.prisma

```
    @default(dbgenerated("(gen_random_uuid()::TEXT)"))
```

- Use the `--create-only` flag to generate a new migration without applying it:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- Open the generated `migration.sql` file and enable the `pgcrypto` module:

migration.sql

```
    CREATE EXTENSION IF NOT EXISTS pgcrypto;

    ADD COLUMN "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    ADD PRIMARY KEY ("id");
```

- Apply the migration:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

Each time you reset the database or add a new member to your team, all required functions are part of the migration history.
