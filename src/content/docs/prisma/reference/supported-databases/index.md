---
title: "지원되는 데이터베이스"
description: "이 페이지에는 Prisma ORM에서 지원하는 모든 데이터베이스와 해당 버전이 나열되어 있습니다."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/supported-databases

# 지원되는 데이터베이스

이 페이지에는 Prisma ORM에서 지원하는 모든 데이터베이스와 해당 버전이 나열되어 있습니다.

Prisma ORM은 현재 다음 데이터베이스를 지원합니다.

> 참고: [시스템 요구사항](https://docs.prisma.io/docs/orm/reference/system-requirements)도 확인하세요.

별표(\*)는 버전 번호가 중요하지 않음을 의미합니다. 예를 들어 모든 버전이 지원되거나, 공개된 버전 번호가 없는 경우 등이 해당됩니다.

## 셀프 호스팅 데이터베이스

| Database             | Version |
| -------------------- | ------- |
| CockroachDB          | 21.2.4+ |
| MariaDB              | 10.0+   |
| MariaDB              | 11.0+   |
| Microsoft SQL Server | 2017    |
| Microsoft SQL Server | 2019    |
| Microsoft SQL Server | 2022    |
| MongoDB              | 4.2+    |
| MySQL                | 5.6     |
| MySQL                | 5.7     |
| MySQL                | 8.0     |
| MySQL                | 8.4     |
| PostgreSQL           | 9.6     |
| PostgreSQL           | 10      |
| PostgreSQL           | 11      |
| PostgreSQL           | 12      |
| PostgreSQL           | 13      |
| PostgreSQL           | 14      |
| PostgreSQL           | 15      |
| PostgreSQL           | 16      |
| PostgreSQL           | 17      |
| PostgreSQL           | 18      |
| SQLite               | \*      |

모든 Prisma ORM 릴리스에는 고정된 버전의 SQLite가 함께 제공된다는 점에 유의하세요.

## 관리형 데이터베이스

| Database                 | Version |
| ------------------------ | ------- |
| AWS Aurora               | \*      |
| AWS Aurora Serverless ¹  | \*      |
| Azure SQL                | \*      |
| CockroachDB-as-a-Service | \*      |
| MongoDB Atlas            | \*      |
| Neon Serverless Postgres | \*      |
| PlanetScale              | \*      |
| Cloudflare D1 (Preview)  | \*      |
| Aiven (MySQL & Postgres) | \*      |

¹ 여기에는 [Data API for Aurora Serverless](https://github.com/prisma/prisma/issues/1964)에 대한 지원이 포함되지 않습니다.
