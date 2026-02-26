---
title: "데이터베이스"
description: "NextAuth.js는 데이터베이스에 연결하는 여러 가지 방법을 제공합니다."
---

Source URL: https://next-auth.js.org/v3/configuration/databases

# 데이터베이스 | NextAuth.js

Version: v3

NextAuth.js는 데이터베이스에 연결하는 여러 가지 방법을 제공합니다.

- **TypeORM** (기본값)
  _TypeORM 어댑터는 MySQL, PostgreSQL, MSSQL, SQLite, MongoDB 데이터베이스를 지원합니다._
- **Prisma**
  _Prisma 2 어댑터는 MySQL, PostgreSQL, SQLite 데이터베이스를 지원합니다._
- **Fauna**
  _FaunaDB 어댑터는 FaunaDB만 지원합니다._
- **Custom Adapter**
  _커스텀 Adapter를 사용하면 어떤 데이터베이스에도 연결할 수 있습니다._

> 현재 [`nextauthjs/adapters`](https://github.com/nextauthjs/adapters) 리포지토리에서는 커뮤니티 기반 DynamoDB, Sanity, PouchDB, Sequelize Adapter를 병합하기 위한 작업이 진행 중입니다. 위 항목에 관심이 있다면 `nextauthjs/adapters` 리포지토리의 PR을 확인해 보세요!

**이 문서는 기본 어댑터(TypeORM)를 다룹니다.**

Prisma 어댑터를 사용하거나 커스텀 어댑터를 사용하는 방법은 [adapters 문서](https://authjs.dev/reference/adapters)를 참고하세요.

NextAuth.js에서 데이터베이스가 어떻게 사용되는지 더 알아보려면 [FAQ의 databases](https://next-auth.js.org/faq#databases)를 확인하세요.

---

## 데이터베이스 사용 방법[​](https://next-auth.js.org/v3/configuration/databases#how-to-use-a-database "Direct link to heading")

데이터베이스 인증 정보는 connection string 또는 [TypeORM configuration](https://github.com/typeorm/typeorm/blob/master/docs/using-ormconfig.md) 객체로 지정할 수 있습니다.

아래 두 방식은 완전히 동일합니다.

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

유효한 [TypeORM configuration option](https://github.com/typeorm/typeorm/blob/master/docs/using-ormconfig.md)은 모두 전달할 수 있습니다.

_예: 모든 테이블 이름에 접두사를 설정하려면 connection string 파라미터로 **entityPrefix** 옵션을 사용할 수 있습니다._

```
    "mysql://nextauth:password@127.0.0.1:3306/database_name?entityPrefix=nextauth_"

```

_…또는 데이터베이스 설정 객체로도 가능합니다:_

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

## 데이터베이스 설정[​](https://next-auth.js.org/v3/configuration/databases#setting-up-a-database "Direct link to heading")

SQL로 테이블과 컬럼을 생성하는 방식이 NextAuth.js용 SQL 데이터베이스를 설정하는 권장 방법입니다.

아래 링크에서 NextAuth.js용 데이터베이스를 설정할 때 실행할 수 있는 SQL을 확인하세요.

- [MySQL Schema](https://next-auth.js.org/v3/adapters/typeorm/mysql)
- [Postgres Schema](https://next-auth.js.org/v3/adapters/typeorm/postgres)

_SQLite, MongoDB 또는 Document 데이터베이스를 사용 중이라면 이 단계를 건너뛰어도 됩니다._

대신 `synchronize: true` 옵션을 사용해 데이터베이스를 자동으로 설정할 수도 있습니다.

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

**`synchronize` 옵션은 프로덕션 데이터베이스에 사용하면 안 됩니다.**

처음 데이터베이스를 설정할 때 필요한 테이블을 생성하는 데는 유용하지만, 프로덕션 데이터베이스에서는 활성화하면 안 됩니다. 데이터베이스에 있는 스키마와 사용 중인 NextAuth.js 버전이 기대하는 스키마가 다를 경우 데이터 손실이 발생할 수 있습니다.

---

## 지원되는 데이터베이스[​](https://next-auth.js.org/v3/configuration/databases#supported-databases "Direct link to heading")

기본 데이터베이스 어댑터는 TypeORM이지만, TypeORM이 지원하는 데이터베이스 중 일부만 NextAuth.js에서 지원됩니다. 이는 NextAuth.js에서 처리해야 하는 커스텀 로직이 있기 때문입니다.

MySQL, Postgres, MongoDB와 호환되는 데이터베이스는 NextAuth.js에서 기본적으로 동작해야 합니다. 그 외 데이터베이스를 사용할 경우 NextAuth.js는 ANSI SQL 호환 데이터베이스로 가정합니다.

tip

데이터베이스를 설정할 때 해당 데이터베이스에 맞는 **node module**도 설치해야 합니다.

### MySQL[​](https://next-auth.js.org/v3/configuration/databases#mysql "Direct link to heading")

설치 모듈: `npm i mysql`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example "Direct link to heading")

```
    database: "mysql://username:password@127.0.0.1:3306/database_name"

```

### MariaDB[​](https://next-auth.js.org/v3/configuration/databases#mariadb "Direct link to heading")

설치 모듈: `npm i mariadb`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example-1 "Direct link to heading")

```
    database: "mariadb://username:password@127.0.0.1:3306/database_name"

```

### Postgres / CockroachDB[​](https://next-auth.js.org/v3/configuration/databases#postgres--cockroachdb "Direct link to heading")

설치 모듈: `npm i pg`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example-2 "Direct link to heading")

PostgresDB

```
    database: "postgres://username:password@127.0.0.1:5432/database_name"

```

CockroachDB

```
    database: "postgres://username:password@127.0.0.1:26257/database_name"

```

node가 Self-signed cert를 사용하는 경우

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

자세히 보기: <https://node-postgres.com/features/ssl>

---

### Microsoft SQL Server[​](https://next-auth.js.org/v3/configuration/databases#microsoft-sql-server "Direct link to heading")

설치 모듈: `npm i mssql`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example-3 "Direct link to heading")

```
    database: "mssql://sa:password@localhost:1433/database_name"

```

### MongoDB[​](https://next-auth.js.org/v3/configuration/databases#mongodb "Direct link to heading")

설치 모듈: `npm i mongodb`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example-4 "Direct link to heading")

```
    database: "mongodb://username:password@127.0.0.1:3306/database_name"

```

### SQLite[​](https://next-auth.js.org/v3/configuration/databases#sqlite "Direct link to heading")

_SQLite는 개발/테스트 용도로만 사용하도록 의도되었으며 프로덕션 용도로는 적합하지 않습니다._

설치 모듈: `npm i sqlite3`

#### 예시[​](https://next-auth.js.org/v3/configuration/databases#example-5 "Direct link to heading")

```
    database: "sqlite://localhost/:memory:"

```

## 기타 데이터베이스[​](https://next-auth.js.org/v3/configuration/databases#other-databases "Direct link to heading")

고급 설정(예: [custom adapter](https://next-auth.js.org/tutorials/creating-a-database-adapter)를 사용해 NextAuth.js를 다른 데이터베이스와 함께 사용하는 방법)에 대한 자세한 내용은 [adapters 문서](https://authjs.dev/reference/adapters)를 참고하세요.
