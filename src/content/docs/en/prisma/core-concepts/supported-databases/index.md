---
title: "Overview"
description: "Prisma ORM supports PostgreSQL, MySQL, SQLite, MongoDB, SQL Server, CockroachDB, and serverless databases"
---

Source URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases

# Overview

Prisma ORM supports PostgreSQL, MySQL, SQLite, MongoDB, SQL Server, CockroachDB, and serverless databases

## Database versions

- Self-hosted

| Database                                                                                    | Version |
| ------------------------------------------------------------------------------------------- | ------- |
| [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)  | 9.6+    |
| [MySQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)            | 5.6+    |
| [MariaDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)          | 10.0+   |
| [SQL Server](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)  | 2017+   |
| [SQLite](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite)          | All     |
| [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)        | 4.2+    |
| [CockroachDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) | 21.2.4+ |

- Managed/Serverless

| Database                | Notes               |
| ----------------------- | ------------------- |
| Neon                    | Serverless Postgres |
| Supabase                | Postgres            |
| PlanetScale             | MySQL               |
| Turso                   | libSQL (SQLite)     |
| Cloudflare D1 (Preview) | SQLite              |
| AWS Aurora              | MySQL/Postgres      |
| MongoDB Atlas           | MongoDB             |

## Feature matrix

- Constraints

| Feature     | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| ----------- | ---------- | ----- | ------ | ---------- | ------- |
| PRIMARY KEY | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| FOREIGN KEY | ✔️         | ✔️    | ✔️     | ✔️         | —       |
| UNIQUE      | ✔️         | ✔️    | ✔️     | ✔️\*       | ✔️      |
| NOT NULL    | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| DEFAULT     | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |

\*SQL Server has [limitations with UNIQUE constraints](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#common-considerations)

- Data types

| Feature | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| ------- | ---------- | ----- | ------ | ---------- | ------- |
| Arrays  | ✔️         | —     | —      | —          | ✔️      |
| JSON    | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| Enums   | ✔️         | ✔️    | ✔️     | —          | ✔️      |

## Database guides

- [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) — Self-hosted, Neon, Supabase, and CockroachDB
- [MySQL/MariaDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql) — Self-hosted and PlanetScale
- [SQLite](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite) — Local, Turso, and Cloudflare D1
- SQL Server
- MongoDB

* Driver adapters

For custom database drivers, see [Driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers).
