---
title: "섀도우 데이터베이스 소개"
description: "Prisma Migrate가 스키마 드리프트를 감지하기 위해 섀도우 데이터베이스를 사용하는 방식을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database

# 섀도우 데이터베이스 소개

Prisma Migrate가 스키마 드리프트를 감지하기 위해 섀도우 데이터베이스를 사용하는 방식을 알아보세요.

섀도우 데이터베이스는 두 번째 _임시_ 데이터베이스로, `prisma migrate dev`를 실행할 때마다 **자동으로 생성 및 삭제**되며, 주로 생성된 마이그레이션의 스키마 드리프트나 잠재적 데이터 손실과 같은 **문제를 감지**하는 데 사용됩니다.

[`migrate diff` command](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff) 역시 `--from-migrations` 또는 `--to-migrations`로 로컬 `migrations` 디렉터리와 diff를 수행할 때 섀도우 데이터베이스가 필요합니다.

- 데이터베이스에서 데이터베이스 생성/삭제를 허용하지 않는 경우(예: 클라우드 호스팅 환경), [섀도우 데이터베이스를 수동으로 생성 및 구성](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#cloud-hosted-shadow-databases-must-be-created-manually)해야 합니다.

섀도우 데이터베이스는 프로덕션 환경에서 **필수 아님**이며, `prisma migrate resolve` 및 `prisma migrate deploy` 같은 프로덕션 중심 명령에서는 사용되지 않습니다.

## 섀도우 데이터베이스 동작 방식

새 마이그레이션을 만들기 위해 `prisma migrate dev`를 실행하면 Prisma Migrate는 섀도우 데이터베이스를 사용해 다음을 수행합니다.

- [스키마 드리프트 감지](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#detecting-schema-drift): 개발 데이터베이스에 **예상치 못한 변경**이 없는지 확인
- [새 마이그레이션 생성](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#generating-new-migrations) 및 적용 시 **데이터 손실**을 유발할 가능성이 있는지 평가

* 스키마 드리프트 감지

개발 환경에서 드리프트를 감지하기 위해 Prisma Migrate는 다음을 수행합니다.

- 섀도우 데이터베이스의 새 복사본을 생성합니다(또는 [`shadowDatabaseUrl`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datasource)로 섀도우 데이터베이스가 구성된 경우 소프트 리셋 수행).
- 섀도우 데이터베이스에서 **현재**의 기존 마이그레이션 이력을 다시 실행합니다.
- 섀도우 데이터베이스를 **introspect**하여 Prisma 스키마의 'current state'를 생성합니다.
- 현재 마이그레이션 이력의 최종 상태를 개발 데이터베이스와 비교합니다.
- 현재 마이그레이션 이력의 최종 상태(섀도우 데이터베이스 기준)가 개발 데이터베이스와 일치하지 않으면(예: 수동 변경으로 인해) **스키마 드리프트**를 보고합니다.

Prisma Migrate가 스키마 드리프트를 감지하지 않으면, [새 마이그레이션 생성](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#generating-new-migrations)으로 진행합니다.

Note

섀도우 데이터베이스는 마이그레이션 파일이 **수정되었거나 삭제되었는지** 확인하는 역할을 하지 않습니다. 이는 `_prisma_migrations` 테이블의 `checksum` 필드를 사용해 수행됩니다.

Prisma Migrate가 스키마 드리프트를 감지하면, 데이터베이스의 어떤 부분에서 드리프트가 발생했는지에 대한 상세 정보를 출력합니다. 다음 예시 출력은 개발 데이터베이스가 수동으로 수정된 경우 표시될 수 있습니다. `Color` enum에 기대한 variant `RED`가 없고, 예상하지 못한 variant `TRANSPARENT`가 포함된 상태입니다.

```
    [*] Changed the `Color` enum
      [+] Added variant `TRANSPARENT`
      [-] Removed variant `RED`
```

- 새 마이그레이션 생성

Prisma Migrate가 [스키마 드리프트를 감지하지 않았다면](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#detecting-schema-drift), Prisma 스키마 변경 사항을 기반으로 새 마이그레이션 생성을 진행합니다. 새 마이그레이션을 생성하기 위해 Prisma Migrate는 다음을 수행합니다.

1. 현재 Prisma 스키마를 기준으로 대상 데이터베이스 스키마를 계산합니다.
2. 기존 마이그레이션 이력의 최종 상태와 대상 스키마를 비교하고, 한쪽에서 다른 쪽으로 이동하기 위한 단계를 생성합니다.
3. 이 단계를 SQL 문자열로 렌더링하여 새 마이그레이션 파일에 저장합니다.
4. SQL로 인해 발생할 수 있는 데이터 손실을 평가하고 경고합니다.
5. 생성된 마이그레이션을 개발 데이터베이스에 적용합니다(`--create-only` 플래그를 지정하지 않은 경우).
6. 섀도우 데이터베이스를 삭제합니다([`shadowDatabaseUrl`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datasource)로 구성된 섀도우 데이터베이스는 삭제되지 않고 `migrate dev` 명령 시작 시 리셋됨).

## 섀도우 데이터베이스 수동 구성

일부 경우(예: [클라우드 호스팅 데이터베이스에서 데이터베이스 생성 및 삭제가 허용되지 않는 경우](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#cloud-hosted-shadow-databases-must-be-created-manually))에는 `migrate dev`에서 섀도우 데이터베이스로 사용할 데이터베이스의 연결 문자열과 이름을 수동으로 정의하는 것이 합리적일 수 있습니다. 이 경우 다음과 같이 할 수 있습니다.

1. 섀도우 데이터베이스로 사용할 전용 데이터베이스를 생성합니다.
2. 해당 데이터베이스의 연결 문자열을 환경 변수 `SHADOW_DATABASE_URL`(또는 `.env` 파일)에 추가합니다.
3. `prisma.config.ts`의 `datasource` 객체 아래 `shadowDatabaseUrl` 필드를 구성합니다. Prisma 6 이하에서는 `schema.prisma` 파일의 `datasource` 블록에 `shadowDatabaseUrl` 필드를 추가합니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
        shadowDatabaseUrl: env("SHADOW_DATABASE_URL"),
      },
    });
```

Important

`url`과 `shadowDatabaseUrl`에 정확히 같은 값을 사용하지 마세요. 데이터베이스의 모든 데이터가 삭제될 수 있습니다.

## 클라우드 호스팅 섀도우 데이터베이스는 수동 생성이 필수

일부 클라우드 제공업체는 SQL로 데이터베이스를 삭제/생성하는 것을 허용하지 않습니다. 어떤 곳은 온라인 인터페이스를 통해서만 데이터베이스 생성/삭제를 요구하고, 어떤 곳은 실제로 데이터베이스를 1개로 제한합니다. 이런 클라우드 호스팅 환경에서 **개발**한다면 다음이 필수입니다.

1. 전용 클라우드 호스팅 섀도우 데이터베이스를 생성합니다.
2. 해당 URL을 환경 변수 `SHADOW_DATABASE_URL`에 추가합니다.
3. `prisma.config.ts`의 `datasource` 객체 아래 `shadowDatabaseUrl` 필드를 구성합니다. Prisma 6 이하에서는 `schema.prisma` 파일의 `datasource` 블록에 `shadowDatabaseUrl` 필드를 추가합니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
        shadowDatabaseUrl: env("SHADOW_DATABASE_URL"),
      },
    });
```

Important

`url`과 `shadowDatabaseUrl`에 정확히 같은 값을 사용하지 마세요. 데이터베이스의 모든 데이터가 삭제될 수 있습니다.

## 섀도우 데이터베이스 사용자 권한

`migrate dev` 사용 시 섀도우 데이터베이스를 생성하고 삭제하려면, Prisma Migrate는 현재 `datasource`에 정의된 데이터베이스 사용자에게 **데이터베이스 생성** 권한이 있어야 합니다.

| Database             | Database user requirements                                                                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQLite               | 특별한 요구 사항이 없습니다.                                                                                                                                                                                                |
| MySQL/MariaDB        | 데이터베이스 사용자에게 `CREATE, ALTER, DROP, REFERENCES ON *.*` 권한이 있어야 합니다.                                                                                                                                      |
| PostgreSQL           | 사용자는 슈퍼유저이거나 `CREATEDB` 권한이 있어야 합니다. `CREATE ROLE` ([PostgreSQL official documentation](https://www.postgresql.org/docs/12/sql-createrole.html)) 참고                                                   |
| Microsoft SQL Server | 사용자는 사이트 관리자이거나 `SERVER` securable 권한이 있어야 합니다. [official documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/permissions-database-engine?view=sql-server-ver15) 참고. |

Prisma Migrate는 연결 URL이 제공한 자격 증명으로 섀도우 데이터베이스를 생성할 수 없으면 다음 오류를 발생시킵니다.

```
    Error: A migration failed when applied to the shadow database
    Database error: Error querying the database: db error: ERROR: permission denied to create database
```

이 오류를 해결하려면:

- 로컬에서 작업 중이라면 데이터베이스 사용자 권한을 업데이트하는 것을 권장합니다.
- 데이터베이스 생성/삭제를 허용하지 않는 데이터베이스를 대상으로 개발 중이라면(이유 불문) [섀도우 데이터베이스 수동 구성](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#manually-configuring-the-shadow-database)을 참조하세요.
- 클라우드 기반 데이터베이스(예: Heroku, Digital Ocean, 또는 Vercel Postgres)를 대상으로 개발 중이라면 다음을 참조하세요: [Cloud-hosted shadow databases](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#cloud-hosted-shadow-databases-must-be-created-manually).
- 클라우드 기반 데이터베이스(예: Heroku, Digital Ocean, 또는 Vercel Postgres)를 대상으로 개발 중이며 현재 **프로토타이핑** 단계라서 생성된 마이그레이션 파일이 중요하지 않고 Prisma 스키마를 데이터베이스 스키마에 적용하기만 하면 된다면, `prisma migrate dev` 명령 대신 [`prisma db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db)를 실행할 수 있습니다.

Important

섀도우 데이터베이스는 개발 환경(정확히는 `prisma migrate dev` 명령)에서만 필요합니다. 프로덕션 환경에는 **어떤 변경도** 할 필요가 없습니다.
