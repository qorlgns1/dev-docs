---
title: "SQL Server"
description: "Microsoft SQL Server 데이터베이스와 함께 Prisma ORM 사용하기"
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server

# SQL Server

Microsoft SQL Server 데이터베이스와 함께 Prisma ORM 사용하기

Prisma ORM은 Microsoft SQL Server(2017+) 데이터베이스를 지원합니다.

## 설정

Prisma 스키마에서 SQL Server provider를 구성하세요:

schema.prisma

```
    datasource db {
      provider = "sqlserver"
    }
```

`prisma.config.ts`에서 연결 URL을 설정하세요:

prisma.config.ts

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"), // sqlserver://host:1433;database=db;...
      },
    });
```

## 드라이버 어댑터 사용

[driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 통해 `node-mssql` JavaScript 데이터베이스 드라이버를 사용하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-mssql
```

```
    import { PrismaMssql } from "@prisma/adapter-mssql";
    import { PrismaClient } from "./generated/prisma";

    const config = {
      server: "localhost",
      port: 1433,
      database: "mydb",
      user: "sa",
      password: "mypassword",
      options: {
        encrypt: true,
        trustServerCertificate: true, // For self-signed certificates
      },
    };

    const adapter = new PrismaMssql(config);
    const prisma = new PrismaClient({ adapter });
```

## 연결 세부 정보

SQL Server는 JDBC 스타일 연결 문자열을 사용합니다:

```
    sqlserver://HOST[:PORT];database=DATABASE;user=USER;password=PASSWORD;encrypt=true
```

**특수 문자 이스케이프:**

자격 증명에 `: \ = ; / [ ] { }`가 포함되어 있다면 값을 중괄호로 감싸세요:

```
    sqlserver://host:1433;user={MyServer/User};password={Pass:Word;};database=db
```

- 연결 문자열 인자

| 인자                           | 기본값   | 설명                                                                     |
| ------------------------------ | -------- | ------------------------------------------------------------------------ |
| `database` / `initial catalog` | `master` | 데이터베이스 이름                                                        |
| `user` / `username` / `uid`    |          | SQL Server 로그인 또는 Windows 사용자 이름(`integratedSecurity` 사용 시) |
| `password` / `pwd`             |          | 사용자 비밀번호                                                          |
| `encrypt`                      | `true`   | TLS 사용: `true` (항상), `false` (로그인만)                              |
| `integratedSecurity`           |          | Windows 인증: `true`, `false`, `yes`, `no`                               |
| `schema`                       | `dbo`    | 모든 쿼리에 대한 스키마 접두사                                           |
| `connectTimeout`               | `5`      | 연결 대기 시간(초)                                                       |
| `socketTimeout`                |          | 각 쿼리 대기 시간(초)                                                    |
| `poolTimeout`                  | `10`     | 풀에서 연결을 기다리는 시간(초)                                          |
| `trustServerCertificate`       | `false`  | 검증 없이 서버 인증서 신뢰                                               |
| `trustServerCertificateCA`     |          | CA 인증서 파일 경로 (`.pem`, `.crt`, `.der`)                             |
| `ApplicationName`              |          | 연결에 사용할 애플리케이션 이름                                          |

Prisma ORM v7: 연결 풀 기본값 변경

드라이버 어댑터는 v6와 다른 `mssql` 드라이버 기본값을 사용합니다:

- **연결 타임아웃:** `15s` (v6의 `5s` 대비)
- **유휴 타임아웃:** `30s` (v6의 `300s` 대비)

구성 방법은 [connection pool guide](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool#sql-server-using-the-mssql-driver)를 참고하세요.

## Windows 인증

**현재 Windows 사용자 사용:**

```
    sqlserver://localhost:1433;database=sample;integratedSecurity=true;trustServerCertificate=true;
```

**특정 Active Directory 사용자 사용:**

```
    sqlserver://localhost:1433;database=sample;integratedSecurity=true;username=prisma;password=aBcD1234;trustServerCertificate=true;
```

**명명된 인스턴스:**

```
    sqlserver://mycomputer\sql2019;database=sample;integratedSecurity=true;trustServerCertificate=true;
```

## 타입 매핑

| Prisma     | SQL Server       |
| ---------- | ---------------- |
| `String`   | `NVARCHAR(1000)` |
| `Boolean`  | `BIT`            |
| `Int`      | `INT`            |
| `BigInt`   | `BIGINT`         |
| `Float`    | `FLOAT(53)`      |
| `Decimal`  | `DECIMAL(32,16)` |
| `DateTime` | `DATETIME2`      |
| `Json`     | 지원되지 않음    |
| `Bytes`    | `VARBINARY(MAX)` |

전체 세부 사항은 [full type mapping reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)를 참고하세요.

## 일반 고려 사항

**UNIQUE 제약 조건:**

SQL Server는 [각 `UNIQUE` 제약 조건당 `NULL` 값을 하나만 허용](https://learn.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints)합니다. 이를 우회하려면 filtered index를 사용할 수 있지만, foreign key로는 사용할 수 없습니다.

**순환 참조:**

모델 참조가 순환 구조인 경우, 검증 오류를 피하려면 [`NoAction` referential actions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#special-rules-for-sql-server-and-mongodb)을 사용해야 합니다.

**`VARCHAR` 컬럼에 대한 Raw query:**

raw query의 `String` 파라미터는 `NVARCHAR(4000)` 또는 `NVARCHAR(MAX)`로 인코딩됩니다. `VARCHAR(N)` 컬럼을 조회할 때는 인덱스 성능 문제를 피하기 위해 수동으로 캐스팅하세요:

```
    // ❌ Causes implicit conversion
    await prisma.$queryRaw`SELECT * FROM user WHERE name = ${"John"}`;

    // ✅ Enables index seek
    await prisma.$queryRaw`SELECT * FROM user WHERE name = CAST(${"John"} AS VARCHAR(40))`;
```

## Prisma Migrate 주의사항

**스키마 이름:**

SQL Server에는 `SET search_path`가 없습니다. 연결 URL의 schema 파라미터가 프로덕션(일반적으로 `dbo`)과 일치하는지 확인하세요:

```
    sqlserver://host:1433;database=db;schema=dbo;...
```

**파괴적 변경:**

일부 작업은 테이블 재생성이 필요합니다:

- `autoincrement()` 추가/제거
- 테이블에서 모든 컬럼 삭제

**공유 기본값:**

Prisma는 SQL Server의 `sp_bindefault`를 지원하지 않습니다. 대신 컬럼별 기본값을 사용하세요.

## 로컬 설정

**Windows:**

1. [SQL Server 2019 Developer](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) 설치
2. [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) 설치
3. SQL Server Configuration Manager에서 TCP/IP 활성화 → **Protocols for MSSQLSERVER**
4. (선택 사항) SQL 인증 활성화: **Properties** → **Security** → **SQL Server and Windows Authentication Mode**

**Docker:**

```
    docker pull mcr.microsoft.com/mssql/server:2019-latest

    docker run --name sql_container \
      -e 'ACCEPT_EULA=Y' \
      -e 'SA_PASSWORD=myPassword' \
      -p 1433:1433 \
      -d mcr.microsoft.com/mssql/server:2019-latest
```

다음으로 연결: 사용자 이름 `sa`, 비밀번호 `myPassword`, 포트 `1433`
