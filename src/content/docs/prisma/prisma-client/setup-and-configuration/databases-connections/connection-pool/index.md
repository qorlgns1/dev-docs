---
title: "연결 풀"
description: "Prisma Client는 데이터베이스 연결을 저장하고 관리하기 위해 연결 풀(데이터베이스 드라이버 또는 드라이버 어댑터에서 제공)을 사용합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool

# 연결 풀

Prisma Client는 데이터베이스 연결을 저장하고 관리하기 위해 연결 풀(데이터베이스 드라이버 또는 드라이버 어댑터에서 제공)을 사용합니다.

빠른 요약

이 페이지에서는 Prisma ORM이 연결 풀을 사용해 데이터베이스 연결을 관리하는 방법과, 최적의 성능을 위해 제한 및 타임아웃을 구성하는 방법을 설명합니다.

Prisma Client는 데이터베이스 연결의 **connection pool**을 사용합니다([driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)를 사용할 때 데이터베이스 드라이버가 관리). 풀은 Prisma Client가 데이터베이스에 _첫 번째_ 연결을 열 때 생성되며, 이는 다음 두 가지 방식 중 하나로 발생할 수 있습니다.

- [`$connect()`를 명시적으로 호출](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#connect)하거나
- 첫 번째 쿼리를 실행할 때(내부적으로 `$connect()` 호출)

관계형 데이터베이스 커넥터는 Prisma ORM 자체 연결 풀을 사용하고, MongoDB 커넥터는 [MongoDB driver connection pool](https://github.com/mongodb/specifications/blob/master/source/connection-monitoring-and-pooling/connection-monitoring-and-pooling.rst)을 사용합니다.

이 페이지에서 답하는 질문

- Prisma의 연결 풀 크기는 어떻게 정하나요?
- 풀 타임아웃과 제한은 어떻게 설정하나요?
- Prisma와 함께 PgBouncer는 언제 사용해야 하나요?

## 관계형 데이터베이스

Prisma ORM v7부터 관계형 datasource는 기본적으로 [driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)와 함께 Prisma Client를 인스턴스화합니다. 드라이버 어댑터는 사용자가 제공한 Node.js 드라이버에 의존하므로, 연결 풀 기본값(및 설정)은 이제 드라이버 자체에서 가져옵니다.

아래 표를 사용해 Prisma ORM v6 연결 URL 파라미터를 Prisma ORM v7 드라이버 어댑터 필드 및 해당 기본값으로 매핑하세요.

- Prisma ORM v7 driver adapter defaults

다음 표는 각 드라이버 어댑터의 기본 연결 풀 설정을 문서화합니다.

Prisma 타임아웃

Prisma ORM에는 데이터베이스 드라이버 타임아웃과 별개인 자체 구성 가능한 타임아웃도 있습니다. 타임아웃 오류가 발생했을 때 그것이 드라이버에서 온 것인지 Prisma Client에서 온 것인지 확실하지 않다면 [Prisma Client timeouts and transaction options documentation](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#transaction-isolation-level)을 확인하세요.

#

- PostgreSQL (`pg` driver adapter 사용)

다음은 `pg` driver adapter의 기본 연결 풀 설정입니다.

| 동작          | v6 URL 파라미터                | v6 기본값                          | v7 `pg` 구성 필드         | v7 기본값           |
| ------------- | ------------------------------ | ---------------------------------- | ------------------------- | ------------------- |
| 풀 크기       | `connection_limit`             | `num_cpus::get_physical() * 2 + 1` | `max`                     | `10`                |
| 획득 타임아웃 | `pool_timeout`                 | `10s`                              | `connectionTimeoutMillis` | `0` (타임아웃 없음) |
| 연결 타임아웃 | `connect_timeout`              | `5s`                               | `connectionTimeoutMillis` | `0` (타임아웃 없음) |
| 유휴 타임아웃 | `max_idle_connection_lifetime` | `300s`                             | `idleTimeoutMillis`       | `10s`               |
| 연결 수명     | `max_connection_lifetime`      | `0` (타임아웃 없음)                | `maxLifetimeSeconds`      | `0` (타임아웃 없음) |

예시: `pg` driver adapter로 Prisma ORM v6 기본값 맞추기

Prisma ORM v6에서 사용하던 동일한 타임아웃 동작을 유지하려면, 드라이버 어댑터를 인스턴스화할 때 다음 구성을 전달하세요:

```
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL,
      // Match Prisma ORM v6 defaults:
      connectionTimeoutMillis: 5_000, // v6 connect_timeout was 5s
      idleTimeoutMillis: 300_000, // v6 max_idle_connection_lifetime was 300s
    });
```

사용 가능한 모든 옵션에 대한 자세한 내용은 [node-postgres pool documentation](https://node-postgres.com/apis/pool)을 참고하세요.

#

- MySQL 또는 MariaDB (`mariadb` driver 사용)

다음은 `mariadb` driver adapter의 기본 연결 풀 설정입니다.

| 동작          | v6 URL 파라미터                | v6 기본값                          | v7 `mariadb` 구성 필드 | v7 기본값 |
| ------------- | ------------------------------ | ---------------------------------- | ---------------------- | --------- |
| 풀 크기       | `connection_limit`             | `num_cpus::get_physical() * 2 + 1` | `connectionLimit`      | `10`      |
| 획득 타임아웃 | `pool_timeout`                 | `10s`                              | `acquireTimeout`       | `10s`     |
| 연결 타임아웃 | `connect_timeout`              | `5s`                               | `connectTimeout`       | `1s`      |
| 유휴 타임아웃 | `max_idle_connection_lifetime` | `300s`                             | `idleTimeout`          | `1800s`   |

예시: `mariadb` driver adapter로 Prisma ORM v6 기본값 맞추기

Prisma ORM v6에서 사용하던 동일한 타임아웃 동작을 유지하려면, 드라이버 어댑터를 인스턴스화할 때 다음 구성을 전달하세요:

```
    import { PrismaMariaDb } from "@prisma/adapter-mariadb";

    const adapter = new PrismaMariaDb({
      host: "localhost",
      port: 3306,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      // Match Prisma ORM v6 defaults:
      connectTimeout: 5_000, // v6 connect_timeout was 5s
      idleTimeout: 300, // v6 max_idle_connection_lifetime was 300s (note: in seconds, not ms)
    });
```

구성 및 튜닝 가이드는 [MariaDB Connector/Node.js pool options](https://mariadb.com/docs/connectors/mariadb-connector-nodejs/connector-nodejs-promise-api#pool-options)을 참고하세요.

#

- SQL Server (`mssql` driver 사용)

다음은 `mssql` driver adapter의 기본 연결 풀 설정입니다.

| 동작          | v6 URL 파라미터                | v6 기본값                          | v7 `mssql` 구성 필드     | v7 기본값 |
| ------------- | ------------------------------ | ---------------------------------- | ------------------------ | --------- |
| 풀 크기       | `connection_limit`             | `num_cpus::get_physical() * 2 + 1` | `pool.max`               | `10`      |
| 연결 타임아웃 | `connect_timeout`              | `5s`                               | `connectionTimeout`      | `15s`     |
| 유휴 타임아웃 | `max_idle_connection_lifetime` | `300s`                             | `pool.idleTimeoutMillis` | `30s`     |

예시: `mssql` driver adapter로 Prisma ORM v6 기본값 맞추기

Prisma ORM v6에서 사용하던 동일한 타임아웃 동작을 유지하려면, 드라이버 어댑터를 인스턴스화할 때 다음 구성을 전달하세요:

```
    import { PrismaMssql } from "@prisma/adapter-mssql";

    const adapter = new PrismaMssql({
      server: "localhost",
      port: 1433,
      database: "mydb",
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      // Match Prisma ORM v6 defaults:
      connectionTimeout: 5_000, // v6 connect_timeout was 5s
      pool: {
        idleTimeoutMillis: 300_000, // v6 max_idle_connection_lifetime was 300s
      },
    });
```

이 필드들에 대한 자세한 내용은 [`node-mssql` pool docs](https://tediousjs.github.io/node-mssql/#general-same-for-all-drivers)를 참고하세요.

## MongoDB

MongoDB 커넥터는 Prisma ORM 연결 풀을 사용하지 않습니다. 연결 풀은 MongoDB 드라이버 내부에서 관리되며 [connection string parameters](https://www.mongodb.com/docs/manual/reference/connection-string-options/#connection-pool-options)를 통해 구성됩니다.

## 외부 연결 풀러

풀 크기는 기본 데이터베이스가 지원할 수 있는 한도를 초과할 수 없습니다. 풀 크기와 타임아웃은 [driver adapter](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)를 통해 구성하세요(위 표 참고). 이는 각 함수가 `PrismaClient` 인스턴스와 자체 연결 풀을 관리하는 서버리스 환경에서 특히 어려운 과제입니다.

애플리케이션 또는 함수가 데이터베이스 연결 한도를 소진하지 않도록 [PgBouncer 같은 외부 연결 풀러](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#pgbouncer) 도입을 고려하세요.

## 수동 데이터베이스 연결 처리

Prisma Client를 드라이버 어댑터와 함께 사용할 때 데이터베이스 연결은 드라이버와 해당 풀이 관리합니다. 개발자에게 노출되지 않으며 개별 연결에 수동으로 접근할 수 없습니다.
