---
title: "Data sources"
description: "Data sources enable Prisma to connect to your database. This page explains how to configure data sources in your Prisma schema"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources

# Data sources

Data sources enable Prisma to connect to your database. This page explains how to configure data sources in your Prisma schema

A data source determines how Prisma ORM connects to your database, and is represented by the [`datasource`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datasource) block in the Prisma schema. Connection details (such as the database URL) are configured in [Prisma Config](https://docs.prisma.io/docs/orm/reference/prisma-config-reference). The following data source uses the `postgresql` provider:

```
    datasource db {
      provider = "postgresql"
    }
```

A Prisma schema can only have _one_ data source. However, you can:

- Override the database connection when creating your `PrismaClient`
- Specify a different **database** for Prisma Migrate's shadow database if you are working with cloud-hosted development databases

## Securing database connections

Some data source `provider`s allow you to configure your connection with SSL/TLS **by specifying certificate locations in your connection configuration**.

- Configuring an SSL connection with PostgreSQL
- Configuring an SSL connection with MySQL
- Configure a TLS connection with Microsoft SQL Server

See the database-specific documentation above for examples of SSL/TLS connection configuration in Prisma Config.
