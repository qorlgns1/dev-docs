---
title: "Unsupported database features (Prisma Migrate)"
description: "How to include unsupported database features for projects that use Prisma Migrate"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features

# Unsupported database features (Prisma Migrate)

How to include unsupported database features for projects that use Prisma Migrate

Prisma Migrate uses the Prisma schema to determine what features to create in the database. However, some database features [cannot be represented in the Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features) , including but not limited to:

- Stored procedures
- Triggers
- Views

To add an unsupported feature to your database, you must [customize a migration](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations) to include that feature before you apply it.

Partial indexes are now supported in Prisma Schema Language via the `where` argument on `@@index`, `@@unique`, and `@unique`. See [Configuring partial indexes](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where) for details. You no longer need to customize migrations for partial indexes.

The Prisma schema is also able to represent [unsupported field types](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#unsupported-field-types) and [native database functions](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions).

This guide **does not apply for MongoDB**.
Instead of `migrate dev`, [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema) is used for [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb).

## Customize a migration to include an unsupported feature

To customize a migration to include an unsupported feature:

- Use the `--create-only` flag to generate a new migration without applying it:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- Open the generated `migration.sql` file and add the unsupported feature - for example, a trigger function:

migration.sql

```
    CREATE OR REPLACE FUNCTION notify_on_insert()
    RETURNS TRIGGER AS $$
    BEGIN
      PERFORM pg_notify('new_record', NEW.id::text);
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
```

- Apply the migration:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

- Commit the modified migration to source control.
