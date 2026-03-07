---
title: "제한 사항 및 알려진 문제"
description: "Prisma Migrate는 현재 MongoDB 커넥터를 지원하지 않습니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/limitations-and-known-issues

# 제한 사항 및 알려진 문제

## MongoDB 커넥터는 지원되지 않음

Prisma Migrate는 현재 MongoDB 커넥터를 지원하지 않습니다.

## 데이터베이스 공급자를 자동으로 전환할 수 없음

Prisma Migrate는 공급자별 SQL 파일을 생성합니다. 즉, 마이그레이션의 문법이 호환되지 않기 때문에 프로덕션에서는 PostgreSQL용, 개발에서는 SQLite용으로 동일한 마이그레이션 파일을 사용할 수 없습니다.

[2.15.0](https://github.com/prisma/prisma/releases/2.15.0)부터 Prisma Migrate는 마이그레이션이 설정된 공급자와 일치하지 않을 때 이를 감지하고 도움이 되는 오류 메시지를 출력합니다. 예를 들어, 마이그레이션은 PostgreSQL 데이터베이스용인데 `provider`가 `mysql`로 설정된 경우:

```
    Error: P3014

    The datasource provider `postgresql` specified in your schema does not match the one specified in the migration_lock.toml, mysql. Please remove your current migration directory and start a new migration history with prisma migrate dev.
```

데이터베이스 공급자를 수동으로 전환하려면 다음을 수행해야 합니다.

- 스키마의 `datasource` 블록에서 `provider` 파라미터를 변경합니다.
- config의 `datasource` 객체에서 `url`을 업데이트합니다.
- 기존 마이그레이션 히스토리를 보관하거나 제거합니다. `./prisma/migrations` 폴더가 없어야 합니다.
- `prisma migrate dev`를 실행해 새 마이그레이션 히스토리를 시작합니다.

마지막 단계에서는 빈 데이터베이스에서 현재 `schema.prisma`로 가는 새 초기 마이그레이션이 생성됩니다. 다음 사항에 유의하세요.

- 이 마이그레이션에는 `schema.prisma`에 반영된 내용만 포함됩니다. 이전 마이그레이션 파일을 수동으로 수정해 커스텀 SQL을 추가했다면, 해당 내용도 다시 직접 추가해야 합니다.
- 새 공급자로 새로 생성된 데이터베이스에는 어떤 데이터도 포함되지 않습니다.

## 데이터베이스 리셋 시 데이터 손실

개발 환경에서 Prisma Migrate는 때때로 데이터베이스 리셋을 요청합니다. 리셋은 데이터베이스를 삭제 후 재생성하므로 데이터 손실이 발생합니다. 데이터베이스는 다음 경우에 리셋됩니다.

- `prisma migrate reset`을 명시적으로 호출한 경우
- `prisma migrate dev`를 호출했고 Prisma Migrate가 데이터베이스 드리프트 또는 마이그레이션 히스토리 충돌을 감지한 경우

`prisma migrate dev` 및 `prisma migrate reset` 명령은 **개발 환경에서만** 사용하도록 설계되었으며, 프로덕션 데이터에 영향을 주어서는 안 됩니다.

데이터베이스가 리셋될 때 Prisma Migrate가 `prisma.config.ts`에서 시드 스크립트를 감지하면 시딩을 트리거합니다.

Note

데이터베이스 리셋 시 데이터를 간단하고 통합된 방식으로 다시 생성하려면 [seeding guide](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding)를 확인하세요.

## Prisma Migrate와 PgBouncer

연결 풀링에 PgBouncer를 사용하는 환경에서 Prisma Migrate 명령을 실행하려고 하면 다음 오류가 나타날 수 있습니다.

```
    Error: undefined: Database error
    Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

자세한 정보와 우회 방법은 [Prisma Migrate and PgBouncer workaround](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer)를 참고하세요. 업데이트는 [GitHub issue #6485](https://github.com/prisma/prisma/issues/6485)를 확인하세요.

## 비대화형 환경에서의 Prisma Migrate

Prisma ORM은 Docker, Node 스크립트, bash 셸과 같은 비대화형 환경에서 CLI 명령을 실행하는 경우를 감지합니다. 이 경우 환경이 비대화형이며 `migrate dev` 명령이 지원되지 않는다는 경고가 표시됩니다.

Docker 환경이 명령을 인식하도록 하려면, 이미지가 `migrate dev` 명령에 반응할 수 있도록 `interactive` 모드로 실행하세요.

```
    docker run --interactive --tty <image name>
    # or
    docker -it <image name>

    # Example usage
    docker run -it node
```
