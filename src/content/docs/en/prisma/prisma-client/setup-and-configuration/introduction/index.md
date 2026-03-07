---
title: "Introduction to Prisma Client"
description: "Learn how to set up and configure Prisma Client in your project"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction

# Introduction to Prisma Client

Learn how to set up and configure Prisma Client in your project

Prisma Client is an auto-generated and type-safe query builder that's _tailored_ to your data. The easiest way to get started with Prisma Client is by following the **[Quickstart](https://docs.prisma.io/docs/prisma-orm/quickstart/sqlite)**.

[Quickstart (5 min)](https://docs.prisma.io/docs/prisma-orm/quickstart/sqlite)

## Prerequisites

In order to set up Prisma Client, you need a Prisma Config and a [Prisma schema file](https://docs.prisma.io/docs/orm/prisma-schema/overview):

Prisma Config

Prisma Schema

prisma.config.ts

```
    import 'dotenv/config';
    import { defineConfig, env } from 'prisma/config';

    export default defineConfig({
      schema: './prisma/schema.prisma',
      datasource: {
        url: env('DATABASE_URL'),
      },
    });
```

## Installation

[Install the Prisma CLI](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference), the Prisma Client library, and the [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) for your database:

PostgreSQL

MySQL / MariaDB

SQLite

npm

pnpm

yarn

bun

```
    npm install prisma --save-dev
    npm install @prisma/client @prisma/adapter-pg pg
```

Prisma 7 requires a [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) to connect to your database. Make sure your `package.json` includes `"type": "module"` for ESM support. See the [upgrade guide](https://docs.prisma.io/docs/guides/upgrade-prisma-orm/v7) for details.

## Generate the Client API

Prisma Client is based on the models in Prisma Schema. To provide the correct types, you need generate the client code:

npm

pnpm

yarn

bun

```
    npx prisma generate
```

This will create a `generated` directory based on where you set the `output` to in the Prisma Schema. Any time your import Prisma Client, it will need to come from this generated client API.

## Importing Prisma Client

With the client generated, import it along with your [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) and create a new instance:

PostgreSQL

MySQL / MariaDB

SQLite

PostgreSQL (Edge)

```
    import { PrismaClient } from "./path/to/generated/prisma";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL!,
    });

    export const prisma = new PrismaClient({ adapter });
```

`PrismaClient` requires a driver adapter in Prisma 7. Calling `new PrismaClient()` without an `adapter` will result in an error.

Find out what [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers) is needed for your database.

Your application should generally only create **one instance** of `PrismaClient`. How to achieve this depends on whether you are using Prisma ORM in a [long-running application](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-long-running-applications) or in a [serverless environment](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-serverless-environments).

Creating multiple instances of `PrismaClient` will create multiple connection pools and can hit the connection limit for your database. Too many connections may start to **slow down your database** and eventually lead to errors such as:

```
    Error in connector: Error querying the database: db error: FATAL: sorry, too many clients already
       at PrismaClientFetcher.request
```

## Use Prisma Client to send queries to your database

Once you have instantiated `PrismaClient`, you can start sending queries in your code:

```
    // run inside `async` function
    const newUser = await prisma.user.create({
      data: {
        name: "Alice",
        email: "alice@prisma.io",
      },
    });

    const users = await prisma.user.findMany();
```

## Evolving your application

Whenever you make changes to your database that are reflected in the Prisma schema, you need to manually re-generate Prisma Client to update the generated code in your output directory:

npm

pnpm

yarn

bun

```
    npx prisma generate
```
