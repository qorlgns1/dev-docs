---
title: "연결 URL"
description: "PostgreSQL, MySQL, SQLite용 데이터베이스 연결 URL을 정의할 때 Prisma ORM이 사용하는 형식과 문법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/connection-urls

# 연결 URL

PostgreSQL, MySQL, SQLite용 데이터베이스 연결 URL을 정의할 때 Prisma ORM이 사용하는 형식과 문법을 알아보세요.

Prisma ORM이 데이터베이스에 연결하려면 연결 URL이 필요합니다. 예를 들어 [Prisma Client](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction)로 쿼리를 전송할 때나 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)로 데이터베이스 스키마를 변경할 때 사용됩니다.

연결 URL은 Prisma 설정(또는 버전 6의 경우 Prisma 스키마)에서 `datasource` 블록의 `url` 필드로 제공됩니다. 일반적으로 다음 구성 요소로 이루어집니다(SQLite 및 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 제외):

- **사용자** : 데이터베이스 사용자 이름
- **비밀번호** : 데이터베이스 사용자 비밀번호
- **호스트** : 데이터베이스 서버가 실행 중인 머신의 IP 또는 도메인 이름
- **포트** : 데이터베이스 서버가 실행 중인 포트
- **데이터베이스 이름** : 사용하려는 데이터베이스 이름

Prisma ORM을 시작할 때 이 정보를 미리 준비해 두세요. 아직 데이터베이스 서버를 실행하지 않았다면 로컬 SQLite 데이터베이스 파일을 사용하거나([Quickstart](https://docs.prisma.io/docs/prisma-orm/quickstart/sqlite) 참고), [Prisma Postgres로 무료 PostgreSQL 데이터베이스를 설정](https://docs.prisma.io/docs/postgres)할 수 있습니다.

## 형식

연결 URL 형식은 사용 중인 _데이터베이스 커넥터_ 에 따라 달라집니다. Prisma ORM은 일반적으로 각 데이터베이스의 표준 형식을 지원합니다. 데이터베이스별 연결 URL에 대한 자세한 내용은 전용 문서 페이지에서 확인할 수 있습니다:

- PostgreSQL
- MySQL
- SQLite
- MongoDB
- Microsoft SQL Server
- CockroachDB

* 특수 문자

MySQL, PostgreSQL, CockroachDB의 경우 연결 URL의 어느 부분이든(비밀번호 포함) [특수 문자를 퍼센트 인코딩](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)해야 합니다. 예를 들어 `p@$$w0rd`는 `p%40%24%24w0rd`가 됩니다.

Microsoft SQL Server의 경우 연결 문자열의 어느 부분이든 [특수 문자를 이스케이프](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server#connection-details)해야 합니다.

## 예시

다음은 Prisma ORM이 지원하는 데이터베이스의 연결 URL 예시입니다:

- Prisma Postgres

[Prisma Postgres](https://docs.prisma.io/docs/postgres)는 unikernel에서 실행되는 관리형 PostgreSQL 서비스입니다. Prisma Postgres에 연결하는 방법은 여러 가지가 있습니다:

- direct TCP 연결 사용(모든 ORM 또는 데이터베이스 도구로 연결 가능)
- [Prisma Accelerate](https://docs.prisma.io/docs/accelerate) 사용(Prisma ORM에서만 지원)
- 로컬

이들의 연결 문자열 형식은 아래에서 설명합니다.

#

- Direct TCP

direct TCP로 Prisma Postgres에 연결할 때 연결 문자열은 다음과 같습니다:

```
    DATABASE_URL="postgres://USER:PASSWORD@db.prisma.io:5432/?sslmode=require"
```

`USER` 및 `PASSWORD` 값은 [Prisma Console](https://console.prisma.io)에서 Prisma Postgres 인스턴스 자격 증명을 생성할 때 제공됩니다. 다음은 샘플 값을 사용한 예시입니다:

```
    DATABASE_URL="postgres://2f9881cc7eef46f094ac913df34c1fb441502fe66cbe28cc48998d4e6b20336b:sk_QZ3u8fMPFfBzOID4ol-mV@db.prisma.io:5432/?sslmode=require"
```

#

- Prisma Accelerate(HTTP) 경유

Prisma Accelerate를 통해 연결할 때는 일반적인 연결 문자열과 달리 사용자/비밀번호가 필요하지 않습니다. 대신 API 키로 인증합니다:

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
      },
    });
```

이 스니펫에서 `API_KEY`는 [Prisma Console](https://console.prisma.io)을 통해 새 Prismas Postgres 인스턴스를 설정할 때 받게 되는 API 키를 의미하는 플레이스홀더입니다. 실제 Prisma Postgres 연결 URL은 다음과 같을 수 있습니다:

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "prisma+postgres://accelerate.prisma-data.net/?api_key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5IjoiMGNkZTFlMjQtNzhiYi00NTY4LTkyM2EtNWUwOTEzZWUyNjU1IiwidGVuYW50X2lkIjoiNzEyZWRlZTc1Y2U2MDk2ZjI4NDg3YjE4NWMyYzA2OTNhNGMxNzJkMjhhOWFlNGUwZTYxNWE4NWIxZWY1YjBkMCIsImludGVybmFsX3NlY3JldCI6IjA4MzQ2Y2RlLWI5ZjktNDQ4Yy04NThmLTMxNjg4ODEzNmEzZCJ9.N1Za6q6NfInzHvRkud6Ojt_-RFg18a0601vdYWGKOrk"
      },
    });
```

#

- 로컬 Prisma Postgres

[로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 인스턴스에 연결하는 연결 문자열은 Accelerate를 통한 원격 인스턴스의 구조를 따릅니다:

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "prisma+postgres://accelerate.prisma-data.net/?api_key=API_KEY"
      },
    });
```

하지만 이 경우 `API_KEY`는 인증 정보를 제공하지 않습니다. 대신 로컬 Prisma Postgres 인스턴스에 대한 정보를 인코딩합니다. 로컬 연결 문자열은 [`prisma dev`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#dev) 명령으로 얻을 수 있습니다.

- PostgreSQL

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "postgresql://janedoe:mypassword@localhost:5432/mydb?schema=sample"
      },
    });
```

- MySQL

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "mysql://janedoe:mypassword@localhost:3306/mydb"
      },
    });
```

- Microsoft SQL Server

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "sqlserver://localhost:1433;initial catalog=sample;user=sa;password=mypassword;"
      },
    });
```

- SQLite

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "file:./dev.db"
      },
    });
```

- CockroachDB

prisma.config.ts

```
    export default defineConfig({
      datasource: {
        url: "postgresql://janedoe:mypassword@localhost:26257/mydb?schema=public"
      },
    });
```

- MongoDB

_현재 MongoDB 지원은 [Prisma 6](https://docs.prisma.io/docs/v6/orm/reference/connection-urls#mongodb)으로 제한되어 있습니다. Prisma v7에서 MongoDB 지원을 작업 중입니다._

## .env

연결 URL을 환경 변수로 제공할 수도 있습니다:

schema.prisma

```
    datasource db {
      provider = "postgresql"
    }
```

그다음 터미널에서 환경 변수를 설정하거나 `.env`라는 이름의 [dotenv](https://github.com/motdotla/dotenv) 파일을 제공할 수 있습니다. Prisma CLI가 이를 자동으로 인식합니다.

Prisma ORM은 다음 상황에서 dotenv 파일에서 연결 URL을 읽습니다:

- 빌드 타임에 스키마를 업데이트할 때
- 런타임에 데이터베이스에 연결할 때

```
    DATABASE_URL=postgresql://janedoe:mypassword@localhost:5432/mydb
```
