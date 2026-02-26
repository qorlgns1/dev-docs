---
title: "Databases"
description: "NextAuth.js comes with multiple ways of connecting to a database:"
---

Source URL: https://next-auth.js.org/v3/configuration/databases

# Databases | NextAuth.js

Version: v3

NextAuth.js comes with multiple ways of connecting to a database:

- **TypeORM** (default)
  _The TypeORM adapter supports MySQL, PostgreSQL, MSSQL, SQLite and MongoDB databases._
- **Prisma**
  _The Prisma 2 adapter supports MySQL, PostgreSQL and SQLite databases._
- **Fauna**
  _The FaunaDB adapter only supports FaunaDB._
- **Custom Adapter**
  _A custom Adapter can be used to connect to any database._

> There are currently efforts in the [`nextauthjs/adapters`](https://github.com/nextauthjs/adapters) repository to get community-based DynamoDB, Sanity, PouchDB and Sequelize Adapters merged. If you are interested in any of the above, feel free to check out the PRs in the `nextauthjs/adapters` repository!

**This document covers the default adapter (TypeORM).**

See the [documentation for adapters](https://authjs.dev/reference/adapters) to learn more about using Prisma adapter or using a custom adapter.

To learn more about databases in NextAuth.js and how they are used, check out [databases in the FAQ](https://next-auth.js.org/faq#databases).

---

## How to use a database[​](https://next-auth.js.org/v3/configuration/databases#how-to-use-a-database "Direct link to heading")

You can specify database credentials as as a connection string or a [TypeORM configuration](https://github.com/typeorm/typeorm/blob/master/docs/using-ormconfig.md) object.

The following approaches are exactly equivalent:

```
    database: "mysql://nextauth:password@127.0.0.1:3306/database_name"

```

```
    database: {
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'nextauth',
      password: 'password',
      database: 'database_name'
    }

```

tip

You can pass in any valid [TypeORM configuration option](https://github.com/typeorm/typeorm/blob/master/docs/using-ormconfig.md).

_e.g. To set a prefix for all table names you can use the**entityPrefix** option as connection string parameter:_

```
    "mysql://nextauth:password@127.0.0.1:3306/database_name?entityPrefix=nextauth_"

```

_…or as a database configuration object:_

```
     database: {
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'nextauth',
      password: 'password',
      database: 'database_name',
      entityPrefix: 'nextauth_'
    }

```

---

## Setting up a database[​](https://next-auth.js.org/v3/configuration/databases#setting-up-a-database "Direct link to heading")

Using SQL to create tables and columns is the recommended way to set up an SQL database for NextAuth.js.

Check out the links below for SQL you can run to set up a database for NextAuth.js.

- [MySQL Schema](https://next-auth.js.org/v3/adapters/typeorm/mysql)
- [Postgres Schema](https://next-auth.js.org/v3/adapters/typeorm/postgres)

_If you are running SQLite, MongoDB or a Document database you can skip this step._

Alternatively, you can also have your database configured automatically using the `synchronize: true` option:

```
    database: "mysql://nextauth:password@127.0.0.1:3306/database_name?synchronize=true"

```

```
    database: {
      type: 'mysql',
      host: '127.0.0.1',
      port: 3306,
      username: 'nextauth',
      password: 'password',
      database: 'database_name',
      synchronize: true
    }

```

danger

**The`synchronize` option should not be used against production databases.**

It is useful to create the tables you need when setting up a database for the first time, but it should not be enabled against production databases as it may result in data loss if there is a difference between the schema that found in the database and the schema that the version of NextAuth.js being used is expecting.

---

## Supported databases[​](https://next-auth.js.org/v3/configuration/databases#supported-databases "Direct link to heading")

The default database adapter is TypeORM, but only some databases supported by TypeORM are supported by NextAuth.js as custom logic needs to be handled by NextAuth.js.

Databases compatible with MySQL, Postgres and MongoDB should work out of the box with NextAuth.js. When used with any other database, NextAuth.js will assume an ANSI SQL compatible database.

tip

When configuring your database you also need to install an appropriate **node module** for your database.

### MySQL[​](https://next-auth.js.org/v3/configuration/databases#mysql "Direct link to heading")

Install module: `npm i mysql`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example "Direct link to heading")

```
    database: "mysql://username:password@127.0.0.1:3306/database_name"

```

### MariaDB[​](https://next-auth.js.org/v3/configuration/databases#mariadb "Direct link to heading")

Install module: `npm i mariadb`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example-1 "Direct link to heading")

```
    database: "mariadb://username:password@127.0.0.1:3306/database_name"

```

### Postgres / CockroachDB[​](https://next-auth.js.org/v3/configuration/databases#postgres--cockroachdb "Direct link to heading")

Install module: `npm i pg`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example-2 "Direct link to heading")

PostgresDB

```
    database: "postgres://username:password@127.0.0.1:5432/database_name"

```

CockroachDB

```
    database: "postgres://username:password@127.0.0.1:26257/database_name"

```

If the node is using Self-signed cert

```
    database: {
        type: "cockroachdb",
        host: process.env.DATABASE_HOST,
        port: 26257,
        username: process.env.DATABASE_USER,
        password: process.env.DATABASE_PASSWORD,
        database: process.env.DATABASE_NAME,
        ssl: {
          rejectUnauthorized: false,
          ca: fs.readFileSync('/path/to/server-certificates/root.crt').toString()
        },
      },

```

Read more: <https://node-postgres.com/features/ssl>

---

### Microsoft SQL Server[​](https://next-auth.js.org/v3/configuration/databases#microsoft-sql-server "Direct link to heading")

Install module: `npm i mssql`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example-3 "Direct link to heading")

```
    database: "mssql://sa:password@localhost:1433/database_name"

```

### MongoDB[​](https://next-auth.js.org/v3/configuration/databases#mongodb "Direct link to heading")

Install module: `npm i mongodb`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example-4 "Direct link to heading")

```
    database: "mongodb://username:password@127.0.0.1:3306/database_name"

```

### SQLite[​](https://next-auth.js.org/v3/configuration/databases#sqlite "Direct link to heading")

_SQLite is intended only for development / testing and not for production use._

Install module: `npm i sqlite3`

#### Example[​](https://next-auth.js.org/v3/configuration/databases#example-5 "Direct link to heading")

```
    database: "sqlite://localhost/:memory:"

```

## Other databases[​](https://next-auth.js.org/v3/configuration/databases#other-databases "Direct link to heading")

See the [documentation for adapters](https://authjs.dev/reference/adapters) for more information on advanced configuration, including how to use NextAuth.js with other databases using a [custom adapter](https://next-auth.js.org/tutorials/creating-a-database-adapter).
