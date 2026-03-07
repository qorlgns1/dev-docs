---
title: "Customizing migrations"
description: "How to edit a migration file before applying it to avoid data loss in production."
---

Source URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations

# Customizing migrations

How to edit a migration file before applying it to avoid data loss in production.

In some scenarios, you need to edit a migration file before you apply it. For example, to [change the direction of a 1-1 relation](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-change-the-direction-of-a-1-1-relation) (moving the foreign key from one side to another) without data loss, you need to move data as part of the migration - this SQL is not part of the default migration, and must be written by hand.

This guide explains how to edit migration files and gives some examples of use cases where you may want to do this.

## How to edit a migration file

To edit a migration file before applying it, the general procedure is the following:

- Make a schema change that requires custom SQL (for example, to preserve existing data)
- Create a draft migration using:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- Modify the generated SQL file.
- Apply the modified SQL by running:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

- Example: Rename a field

By default, renaming a field in the schema results in a migration that will:

- `CREATE` a new column (for example, `fullname`)
- `DROP` the existing column (for example, `name`) and the data in that column

To actually **rename** a field and avoid data loss when you run the migration in production, you need to modify the generated migration SQL before applying it to the database. Consider the following schema fragment - the `biograpy` field is spelled wrong.

schema.prisma

```
    model Profile {
      id       Int    @id @default(autoincrement())
      biograpy String
      userId   Int    @unique
      user     User   @relation(fields: [userId], references: [id])
    }
```

To rename the `biograpy` field to `biography`:

Rename the field in the schema:

```
    model Profile {
      id        Int    @id @default(autoincrement())
      biograpy  String
      biography String
      userId    Int    @unique
      user      User   @relation(fields: [userId], references: [id])
    }
```

- Run the following command to create a **draft migration** that you can edit before applying to the database:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name rename-migration --create-only
```

- Edit the draft migration as shown, changing `DROP` / `DELETE` to a single `RENAME COLUMN`:

Before

After

migration.sql

```
    ALTER TABLE "Profile" DROP COLUMN "biograpy",
    ADD COLUMN  "biography" TEXT NOT NULL;
```

- Save and apply the migration:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

You can use the same technique to rename a `model` \- edit the generated SQL to _rename_ the table rather than drop and re-create it.

- Example: Use the expand and contract pattern to evolve the schema without downtime

Making schema changes to existing fields, e.g., renaming a field can lead to downtime. It happens in the time frame between applying a migration that modifies an existing field, and deploying a new version of the application code which uses the modified field.

You can prevent downtime by breaking down the steps required to alter a field into a series of discrete steps designed to introduce the change gradually. This pattern is known as the _expand and contract pattern_.

The pattern involves two components: your application code accessing the database and the database schema you intend to alter.

With the _expand and contract_ pattern, renaming the field `bio` to `biography` would look as follows with Prisma:

- Add the new `biography` field to your Prisma schema and create a migration

schema.prisma

```
    model Profile {
     id        Int    @id @default(autoincrement())
     bio       String
     biography String
     userId    Int    @unique
     user      User   @relation(fields: [userId], references: [id])
    }
```

- _Expand_ : update the application code and write to both the `bio` and `biography` fields, but continue reading from the `bio` field, and deploy the code
- Create an empty migration and copy existing data from the `bio` to the `biography` field

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name copy_biography --create-only
```

migration.sql

```
    UPDATE "Profile" SET biography = bio;
```

4. Verify the integrity of the `biography` field in the database
5. Update application code to **read** from the new `biography` field
6. Update application code to **stop writing** to the `bio` field
7. _Contract_ : remove the `bio` from the Prisma schema, and create a migration to remove the `bio` field

schema.prisma

```
    model Profile {
     id        Int    @id @default(autoincrement())
     bio       String
     biography String
     userId    Int    @unique
     user      User   @relation(fields: [userId], references: [id])
    }
```

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name remove_bio
```

By using this approach, you avoid potential downtime that altering existing fields that are used in the application code are prone to, and reduce the amount of coordination required between applying the migration and deploying the updated application code.

Note that this pattern is applicable in any situation involving a change to a column that has data and is in use by the application code. Examples include combining two fields into one, or transforming a `1:n` relation to a `m:n` relation.

To learn more, check out the Data Guide article on [the expand and contract pattern](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern)

- Example: Change the direction of a 1-1 relation

To change the direction of a 1-1 relation:

- Make the change in the schema:

schema.prisma

```
    model User {
     id        Int      @id @default(autoincrement())
     name      String
     posts     Post[]
     profile   Profile? @relation(fields: [profileId], references: [id])
     profileId Int      @unique
    }

    model Profile {
     id        Int    @id @default(autoincrement())
     biography String
     user      User
    }
```

- Run the following command to create a **draft migration** that you can edit before applying to the database:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name rename-migration --create-only
```

```
    ⚠️  There will be data loss when applying the migration:

    • The migration will add a unique constraint covering the columns `[profileId]` on the table `User`. If there are existing duplicate values, the migration will fail.
```

- Edit the draft migration as shown:

Before

After

migration

```
    -- DropForeignKey
    ALTER TABLE "Profile" DROP CONSTRAINT "Profile_userId_fkey";

    -- DropIndex
    DROP INDEX "Profile_userId_unique";

    -- AlterTable
    ALTER TABLE "Profile" DROP COLUMN "userId";

    -- AlterTable
    ALTER TABLE "User" ADD COLUMN     "profileId" INTEGER NOT NULL;

    -- CreateIndex
    CREATE UNIQUE INDEX "User_profileId_unique" ON "User"("profileId");

    -- AddForeignKey
    ALTER TABLE "User" ADD FOREIGN KEY ("profileId") REFERENCES "Profile"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

- Save and apply the migration:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```
