---
title: "데이터베이스 버전"
description: "Prisma ORM은 PostgreSQL, MySQL, SQLite, MongoDB, SQL Server, CockroachDB 및 서버리스 데이터베이스를 지원합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases

# 개요

Prisma ORM은 PostgreSQL, MySQL, SQLite, MongoDB, SQL Server, CockroachDB 및 서버리스 데이터베이스를 지원합니다.

## 데이터베이스 버전

- 자체 호스팅

| 데이터베이스                                                                                | 버전    |
| ------------------------------------------------------------------------------------------- | ------- |
| [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)  | 9.6+    |
| [MySQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)            | 5.6+    |
| [MariaDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)          | 10.0+   |
| [SQL Server](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)  | 2017+   |
| [SQLite](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite)          | 전체    |
| [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)        | 4.2+    |
| [CockroachDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) | 21.2.4+ |

- 관리형/서버리스

| 데이터베이스            | 참고              |
| ----------------------- | ----------------- |
| Neon                    | 서버리스 Postgres |
| Supabase                | Postgres          |
| PlanetScale             | MySQL             |
| Turso                   | libSQL (SQLite)   |
| Cloudflare D1 (Preview) | SQLite            |
| AWS Aurora              | MySQL/Postgres    |
| MongoDB Atlas           | MongoDB           |

## 기능 매트릭스

- 제약 조건

| 기능        | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| ----------- | ---------- | ----- | ------ | ---------- | ------- |
| PRIMARY KEY | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| FOREIGN KEY | ✔️         | ✔️    | ✔️     | ✔️         | —       |
| UNIQUE      | ✔️         | ✔️    | ✔️     | ✔️\*       | ✔️      |
| NOT NULL    | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| DEFAULT     | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |

\*SQL Server는 [UNIQUE 제약 조건](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#common-considerations)에 제한 사항이 있습니다.

- 데이터 타입

| 기능  | PostgreSQL | MySQL | SQLite | SQL Server | MongoDB |
| ----- | ---------- | ----- | ------ | ---------- | ------- |
| 배열  | ✔️         | —     | —      | —          | ✔️      |
| JSON  | ✔️         | ✔️    | ✔️     | ✔️         | ✔️      |
| Enums | ✔️         | ✔️    | ✔️     | —          | ✔️      |

## 데이터베이스 가이드

- [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql) — 자체 호스팅, Neon, Supabase 및 CockroachDB
- [MySQL/MariaDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql) — 자체 호스팅 및 PlanetScale
- [SQLite](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite) — 로컬, Turso 및 Cloudflare D1
- SQL Server
- MongoDB

* 드라이버 어댑터

커스텀 데이터베이스 드라이버는 [Driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)를 참조하세요.
