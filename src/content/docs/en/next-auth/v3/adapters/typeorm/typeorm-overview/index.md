---
title: "Overview"
description: "NextAuth.js comes with a default Adapter that uses TypeORM so that it can be used with many different databases without any further configuration, you..."
---

Source URL: https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview

# Overview | NextAuth.js

Version: v3

## TypeORM Adapter[​](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview#typeorm-adapter "Direct link to heading")

NextAuth.js comes with a default Adapter that uses [TypeORM](https://typeorm.io/) so that it can be used with many different databases without any further configuration, you simply add the node module for the database driver you want to use in your project and pass a database connection string to NextAuth.js.

### Database Schemas[​](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview#database-schemas "Direct link to heading")

Configure your database by creating the tables and columns to match the schema expected by NextAuth.js.

- [MySQL Schema](https://next-auth.js.org/v3/adapters/typeorm/mysql)
- [Postgres Schema](https://next-auth.js.org/v3/adapters/typeorm/postgres)
- [Microsoft SQL Server Schema](https://next-auth.js.org/v3/adapters/typeorm/mssql)
- [MongoDB](https://next-auth.js.org/v3/adapters/typeorm/mongodb)

The default Adapter is the TypeORM Adapter and the default database type for TypeORM is SQLite, the following configuration options are exactly equivalent.

```
    database: {
      type: 'sqlite',
      database: ':memory:',
      synchronize: true
    }

```

```
    adapter: Adapters.Default({
      type: "sqlite",
      database: ":memory:",
      synchronize: true,
    })

```

```
    adapter: Adapters.TypeORM.Adapter({
      type: "sqlite",
      database: ":memory:",
      synchronize: true,
    })

```

The tutorial [Custom models with TypeORM](https://next-auth.js.org/v3/tutorials/typeorm-custom-models) explains how to extend the built in models and schemas used by the TypeORM Adapter. You can use these models in your own code.

tip

The `synchronize` option in TypeORM will generate SQL that exactly matches the documented schemas for MySQL and Postgres. This will automatically apply any changes it finds in the entity model, therefore it **should not be enabled against production databases** as it may cause data loss if the configured schema does not match the expected schema!
