---
title: "문제 해결"
description: "개발 환경에서 Prisma Migrate 관련 문제를 해결합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting

# 문제 해결

개발 환경에서 Prisma Migrate 관련 문제를 해결합니다.

이 가이드는 개발 환경에서 Prisma Migrate 문제를 해결하는 방법을 설명하며, 이 과정에는 데이터베이스 재설정이 자주 포함됩니다. 프로덕션 중심 문제 해결은 다음을 참고하세요.

- 프로덕션 문제 해결
- 프로덕션 데이터베이스 패치 / 핫픽스

이 가이드는 **MongoDB에는 적용되지 않습니다**.
MongoDB에서는 `migrate dev` 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다([MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb) 참고).

## 마이그레이션 히스토리 충돌 처리

마이그레이션 히스토리 충돌은 **파일 시스템의 migrations 폴더**와 **데이터베이스의 `_prisma_migrations` 테이블** 사이에 불일치가 있을 때 발생합니다.

#

- 개발 환경에서 마이그레이션 히스토리 충돌이 발생하는 원인
  - 이미 적용된 마이그레이션이 나중에 수정된 경우
  - 이미 적용된 마이그레이션이 파일 시스템에서 누락된 경우

개발 환경에서는 기능 브랜치를 전환할 때 히스토리 충돌이 발생할 수 있습니다. 예를 들어 `_prisma_migrations` 테이블에는 `branch-1`의 마이그레이션이 들어 있는데 `branch-2`로 전환하면 그중 일부 마이그레이션이 사라질 수 있습니다.

참고

[이미 적용된 마이그레이션은 의도적으로 삭제하거나 수정하면 안 됩니다](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories#do-not-edit-or-delete-migrations-that-have-been-applied). 그렇게 하면 개발 환경과 프로덕션 환경 간 불일치가 생길 수 있습니다.

#

- 개발 환경에서 마이그레이션 히스토리 충돌 수정

`prisma migrate dev` 실행 시 Prisma Migrate가 마이그레이션 히스토리 충돌을 감지하면, CLI가 데이터베이스를 재설정하고 마이그레이션 히스토리를 다시 적용할지 묻습니다.

## 스키마 드리프트

데이터베이스 스키마 드리프트는 데이터베이스 스키마가 마이그레이션 히스토리와 동기화되지 않은 상태를 의미합니다. 즉, 데이터베이스 스키마가 단일 진실 공급원(source of truth)에서 벗어난 상태입니다.

#

- 개발 환경에서 스키마 드리프트가 발생하는 원인

다음과 같은 경우 스키마 드리프트가 발생할 수 있습니다.

- 마이그레이션을 사용하지 않고 데이터베이스 스키마를 변경한 경우(예: [`prisma db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push) 사용 또는 수동 변경)

참고

스키마 드리프트를 감지하려면 [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)가 필요하므로, 이 작업은 개발 환경에서만 수행할 수 있습니다.

#

- 개발 환경에서 스키마 드리프트 수정

유지하고 싶지 않거나 Prisma schema에서 쉽게 재현할 수 있는 수동 변경을 데이터베이스에 적용했다면:

- 데이터베이스를 재설정하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate reset
```

- Prisma schema에 변경 사항을 재현하고 새 마이그레이션을 생성하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

유지하고 싶은 수동 변경을 데이터베이스에 적용했다면, 다음을 수행할 수 있습니다.

- 데이터베이스를 introspect 하세요.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

Prisma는 데이터베이스에 직접 적용된 변경 사항으로 schema를 업데이트합니다.

- introspect한 변경 사항을 마이그레이션 히스토리에 포함하도록 새 마이그레이션을 생성하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name introspected_change
```

Prisma Migrate는 재설정을 요청한 뒤, 기존 마이그레이션 전체와 introspect된 변경 사항 기반의 새 마이그레이션을 적용합니다. 이제 수동 변경 사항을 포함해 데이터베이스와 마이그레이션 히스토리가 동기화됩니다.

## 실패한 마이그레이션

#

- 개발 환경에서 마이그레이션이 실패하는 원인

다음과 같은 경우 마이그레이션이 실패할 수 있습니다.

- [실행 전에 마이그레이션을 수정](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)하면서 구문 오류를 만든 경우
- 이미 데이터가 있는 테이블에 필수(`NOT NULL`) 컬럼을 추가한 경우
- 마이그레이션 프로세스가 예기치 않게 중단된 경우
- 마이그레이션 도중 데이터베이스가 종료된 경우

`_prisma_migrations` 테이블의 각 마이그레이션에는 오류를 저장하는 `logs` 컬럼이 있습니다.

#

- 개발 환경에서 실패한 마이그레이션 수정

개발자 환경에서 실패한 마이그레이션을 처리하는 가장 쉬운 방법은 근본 원인을 해결하고 데이터베이스를 재설정하는 것입니다. 예를 들어:

- 데이터베이스를 수동 편집하다 SQL 구문 오류를 만들었다면, 실패한 `migration.sql` 파일을 수정하고 데이터베이스를 재설정하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate reset
```

- 데이터가 있는 데이터베이스에 적용할 수 없는 변경을 Prisma schema에 추가했다면(예: 데이터가 있는 테이블에 필수 컬럼 추가):
  - `migration.sql` 파일을 삭제합니다.
  - schema를 수정합니다(예: 필수 필드에 기본값 추가).
  - 마이그레이션합니다.

npm

pnpm

yarn

bun

```
npx prisma migrate dev
```

Prisma Migrate는 데이터베이스 재설정과 모든 마이그레이션 재적용을 요청합니다.

- 무언가가 마이그레이션 프로세스를 중단했다면 데이터베이스를 재설정하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate reset
```

## Prisma Migrate와 PgBouncer

연결 풀링에 PgBouncer를 사용하는 환경에서 Prisma Migrate 명령을 실행하려고 하면 다음 오류가 나타날 수 있습니다.

```
    Error: undefined: Database error
    Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

자세한 정보와 우회 방법은 [Prisma Migrate와 PgBouncer 우회 방법](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer)을 참고하세요.
