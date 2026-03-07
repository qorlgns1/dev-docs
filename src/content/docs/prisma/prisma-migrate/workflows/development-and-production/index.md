---
title: "개발 및 프로덕션"
description: "개발 및 프로덕션 환경에서 Prisma Migrate 명령을 사용하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production

# 개발 및 프로덕션

마크다운 복사열기

개발 및 프로덕션 환경에서 Prisma Migrate 명령을 사용하는 방법

개발 환경에서는 `migrate dev` 명령을 사용해 마이그레이션을 생성하고 적용합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

- 마이그레이션 생성 및 적용

`migrate dev`는 개발용 명령이며, 프로덕션 환경에서는 절대 사용하면 안 됩니다.

이 명령은 다음을 수행합니다:

- 스키마 드리프트(편집되거나 삭제된 마이그레이션 파일, 또는 데이터베이스 스키마에 대한 수동 변경)를 감지하기 위해 [섀도 데이터베이스](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)에서 기존 마이그레이션 히스토리를 다시 실행합니다
- 보류 중인 마이그레이션을 섀도 데이터베이스에 적용합니다(예: 동료가 생성한 새 마이그레이션)
- Prisma 스키마 변경이 감지되면 해당 변경으로부터 새 마이그레이션을 생성합니다
- 개발 데이터베이스에 아직 적용되지 않은 모든 마이그레이션을 적용하고 `_prisma_migrations` 테이블을 업데이트합니다
- 아티팩트(예: Prisma Client) 생성을 트리거합니다

`migrate dev` 명령은 다음 상황에서 데이터베이스 재설정을 요청합니다:

- [수정되거나 누락된 마이그레이션](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories#do-not-edit-or-delete-migrations-that-have-been-applied)으로 인해 발생한 마이그레이션 히스토리 충돌
- 데이터베이스 스키마가 마이그레이션 히스토리의 최종 상태에서 벗어난 경우

* 개발 데이터베이스 재설정

수동 변경이나 `db push` 실험을 되돌리기 위해 직접 데이터베이스를 `reset`할 수도 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate reset
```

`migrate reset`은 개발용 명령이며, 프로덕션 환경에서는 절대 사용하면 안 됩니다.

이 명령은 다음을 수행합니다:

- 가능하면 데이터베이스/스키마¹를 삭제하거나, 환경에서 데이터베이스/스키마 삭제를 허용하지 않는 경우 소프트 리셋을 수행합니다\*
- 데이터베이스/스키마¹가 삭제된 경우 동일한 이름으로 새 데이터베이스/스키마¹를 생성합니다
- 모든 마이그레이션을 적용합니다
- 시드 스크립트를 실행합니다

MySQL 및 MongoDB에서는 데이터베이스를, PostgreSQL 및 SQL Server에서는 스키마를, SQLite에서는 데이터베이스 파일을 의미합니다.

개발 데이터베이스의 데이터를 필요할 때마다 간단하고 통합된 방식으로 다시 생성하려면 [시딩 가이드](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding)를 확인하세요.

- 마이그레이션 사용자 지정

때로는 마이그레이션을 **적용하기 전에** 수정해야 합니다. 예를 들어:

- 블로그 게시물 태그를 `String[]`에서 `Tag[]`로 변경하는 것처럼 큰 리팩터링을 도입하려는 경우
- [필드 이름을 변경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-rename-a-field)하려는 경우(기본적으로 Prisma Migrate는 기존 필드를 삭제합니다)
- [1-1 관계의 방향을 변경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-change-the-direction-of-a-1-1-relation)하려는 경우
- 저장 프로시저나 트리거처럼 Prisma Schema Language로 표현할 수 없는 기능을 추가하려는 경우

`--create-only` 명령을 사용하면 마이그레이션을 적용하지 않고 생성할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

수정한 마이그레이션을 적용하려면 `prisma migrate dev`를 다시 실행하세요.

예시는 [마이그레이션 사용자 지정](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)을 참고하세요.

- 팀 개발

참고: [Prisma Migrate를 사용한 팀 개발](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production) .

## 프로덕션 및 테스트 환경

프로덕션 및 테스트 환경에서는 `migrate deploy` 명령을 사용해 마이그레이션을 적용합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate deploy
```

`migrate deploy`는 일반적으로 자동화된 CI/CD 파이프라인의 일부여야 하며, 프로덕션 데이터베이스에 변경 사항을 배포하기 위해 이 명령을 로컬에서 실행하는 것은 권장하지 않습니다.

이 명령은 다음을 수행합니다:

- 적용된 마이그레이션을 마이그레이션 히스토리와 비교하고, 마이그레이션이 수정된 경우 **경고**합니다:

```
WARNING The following migrations have been modified since they were applied:
        20210313140442_favorite_colors
```

- 보류 중인 마이그레이션을 적용합니다

`migrate deploy` 명령은 다음과 같습니다:

- 이미 적용된 마이그레이션이 마이그레이션 히스토리에서 *누락*되어 있어도 경고하지 **않습니다**
- 드리프트를 감지하지 **않습니다**(프로덕션 데이터베이스 스키마가 마이그레이션 히스토리 최종 상태와 다름 - 예: 핫픽스로 인한 경우)
- 데이터베이스를 재설정하거나 아티팩트(예: Prisma Client)를 생성하지 **않습니다**
- 섀도 데이터베이스에 의존하지 **않습니다**

추가 참고:

- 배포에서의 Prisma Migrate
- 프로덕션 문제 해결

* 권고 잠금(advisory locking)

Prisma Migrate는 다음과 같은 프로덕션 명령을 실행할 때 권고 잠금을 사용합니다:

- `prisma migrate deploy`
- `prisma migrate dev`
- `prisma migrate resolve`

이 보호 장치는 여러 명령이 동시에 실행되지 않도록 보장합니다. 예를 들어, 두 개의 pull request를 짧은 간격으로 연속 병합하는 경우입니다.

권고 잠금은 **10초 타임아웃**(구성 불가)을 가지며, 기본 제공자에서 제공하는 기본 권고 잠금 메커니즘을 사용합니다:

- PostgreSQL
- MySQL
- Microsoft SQL server

Prisma Migrate의 권고 잠금 구현은 치명적인 오류를 방지하기 위한 용도입니다. 명령이 타임아웃되면 다시 실행해야 합니다.

`5.3.0`부터는 [`PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK` environment variable](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#prisma_schema_disable_advisory_lock)을 사용해 권고 잠금을 비활성화할 수 있습니다.
