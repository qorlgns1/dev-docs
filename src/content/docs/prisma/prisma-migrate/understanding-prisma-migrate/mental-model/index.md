---
title: "마이그레이션 이해하기"
description: "프로젝트에서 Prisma Migrate를 사용할 때를 위한 멘탈 모델 가이드"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model

# 마이그레이션 이해하기

프로젝트에서 Prisma Migrate를 사용할 때를 위한 멘탈 모델 가이드

## 데이터베이스 마이그레이션이란 무엇인가요?

데이터베이스 마이그레이션은 데이터베이스 스키마의 구조를 수정하고 발전시키는, 통제된 변경 집합입니다. 마이그레이션은 데이터베이스 스키마를 한 상태에서 다른 상태로 전환하는 데 도움을 줍니다. 예를 들어, 마이그레이션 내에서 테이블과 컬럼을 생성하거나 제거하고, 테이블의 필드를 분할하거나, 데이터베이스에 타입과 제약 조건을 추가할 수 있습니다.

- 데이터베이스 스키마를 발전시키는 패턴

마이그레이션에는 크게 두 가지 유형이 있습니다:

- **모델/엔티티 우선 마이그레이션(Model/Entity-first migration):** 이 패턴에서는 코드로 데이터베이스 스키마의 구조를 정의한 다음, 마이그레이션 도구를 사용해 SQL을 생성합니다. 예를 들어 애플리케이션과 데이터베이스 스키마를 동기화할 때 사용합니다.

![Model-first migration flow](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/entity-first-migration-flow.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

- **데이터베이스 우선 마이그레이션(Database-first migration):** 이 패턴에서는 데이터베이스 구조를 SQL로 정의하고 데이터베이스에 적용합니다. 이후 데이터베이스를 _introspect_ 하여 데이터베이스 구조를 설명하는 코드를 생성해, 애플리케이션과 데이터베이스 스키마를 동기화합니다.

![Database-first migration flow](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/database-first-migration-flow.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

Note

단순화를 위해, 여기서는 데이터베이스 스키마를 발전시키는 다양한 패턴을 설명하기 위해 위 용어를 사용했습니다. 다른 도구나 라이브러리는 동일한 패턴을 설명할 때 다른 용어를 사용할 수 있습니다.

마이그레이션 파일(SQL)은 이상적으로 애플리케이션 코드와 함께 저장되어야 합니다. 또한 버전 관리로 추적하고, 애플리케이션을 함께 작업하는 팀원들과 공유해야 합니다. 마이그레이션은 _상태 관리(state management)_ 를 제공하여 데이터베이스 상태를 추적할 수 있게 해줍니다.

마이그레이션은 특정 시점의 데이터베이스 상태를 재현할 수 있게도 해주며, 이는 팀 협업 시(예: 서로 다른 브랜치 전환) 유용합니다. 데이터베이스 마이그레이션에 대한 자세한 내용은 [Prisma Data Guide](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations)를 참고하세요.

## Prisma Migrate란 무엇인가요?

Prisma Migrate는 _model/entity-first_ 마이그레이션 패턴을 지원하는 데이터베이스 마이그레이션 도구로, 로컬 환경과 프로덕션에서 데이터베이스 스키마를 관리할 수 있게 해줍니다.

프로젝트에서 Prisma Migrate를 사용할 때의 워크플로는 반복적이며 다음과 같습니다:

- 로컬 개발 환경(기능 브랜치)
  - Prisma 스키마를 발전시킵니다
  - [`prisma migrate dev`](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#track-your-migration-history-with-prisma-migrate-dev) 또는 [`prisma db push`](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#prototype-your-schema)를 사용해 Prisma 스키마를 로컬 개발 데이터베이스의 데이터베이스 스키마와 동기화합니다

- 프리뷰/스테이징 환경(기능 pull request)
  1. 변경 사항을 기능 pull request에 푸시합니다
  2. CI 시스템(예: GitHub Actions)을 사용해 `prisma migrate deploy`로 Prisma 스키마와 마이그레이션 이력을 프리뷰 데이터베이스와 동기화합니다

- 프로덕션(main branch)
  - 애플리케이션 코드를 기능 브랜치에서 main branch로 병합합니다.
  - CI 시스템(예: GitHub Actions)을 사용해 `prisma migrate deploy`로 Prisma 스키마와 마이그레이션 이력을 프로덕션 데이터베이스와 동기화합니다

![Prisma Migrate workflow](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-lifecycle.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

## Prisma Migrate가 마이그레이션 상태를 추적하는 방법

Prisma Migrate는 데이터베이스 스키마 상태를 추적하기 위해 다음 상태 조각들을 사용합니다:

- **Prisma 스키마** : 데이터베이스 스키마 구조를 정의하는 단일 진실 공급원(source of truth)
- **마이그레이션 이력** : `prisma/migrations` 폴더의 SQL 파일로, 데이터베이스 스키마에 적용된 변경 이력을 나타냄
- **마이그레이션 테이블** : 데이터베이스의 `prisma_migrations` 테이블로, 데이터베이스에 적용된 마이그레이션 메타데이터를 저장
- **데이터베이스 스키마** : 데이터베이스의 현재 상태

![Prisma Migrate "state management"](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-state-mgt.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

## Prisma Migrate 작업 시 요구사항

- 이상적으로는 환경마다 하나의 데이터베이스를 사용해야 합니다. 예를 들어 development, preview, production 환경에 각각 별도의 데이터베이스를 둘 수 있습니다.
- 개발 환경에서 사용하는 데이터베이스는 일회용이어야 합니다. 필요할 때 쉽게 생성, 사용, 삭제할 수 있어야 합니다.
- 각 환경에서 사용하는 데이터베이스 설정은 일관되어야 합니다. 그래야 워크플로 전반에서 이동하는 특정 마이그레이션이 데이터베이스에 동일한 변경을 적용함을 보장할 수 있습니다.
- Prisma 스키마는 단일 진실 공급원(source of truth) 역할을 하며, [database schema](https://www.prisma.io/dataguide/intro/database-glossary#schema)의 형태를 설명합니다.

## Prisma Migrate로 데이터베이스 스키마 발전시키기

이 섹션에서는 Prisma Migrate를 사용해 development, staging, production 등 다양한 환경에서 데이터베이스 스키마를 발전시키는 방법을 설명합니다.

- 개발 환경(로컬)에서의 Prisma Migrate

#

- `prisma migrate dev`로 마이그레이션 이력 추적하기

[`prisma migrate dev`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-dev) 명령은 데이터베이스에 가한 변경을 추적할 수 있게 해줍니다. `prisma migrate dev` 명령은 SQL 마이그레이션 파일을 자동으로 생성해(`/prisma/migrations`에 저장) 데이터베이스에 적용합니다. 마이그레이션이 데이터베이스에 적용되면 데이터베이스의 마이그레이션 테이블(`_prisma_migrations`)도 함께 업데이트됩니다.

![Prisma Migrate dev flow](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-dev-flow.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

`prisma migrate dev` 명령은 다음 상태 조각을 사용해 데이터베이스 상태를 추적합니다:

- Prisma 스키마
- 마이그레이션 이력
- 마이그레이션 테이블
- 데이터베이스 스키마

Note

마이그레이션 상태를 추적하는 데 사용하는 상태 조각은 [Prisma Migrate가 마이그레이션 상태를 추적하는 방법](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#how-prisma-migrate-tracks-the-migration-state) 섹션에서 설명한 것과 동일합니다.

`--create-only` 플래그를 사용하면 마이그레이션을 데이터베이스에 적용하기 전에 사용자 지정할 수 있습니다. 예를 들어 데이터 손실 없이 컬럼 이름을 변경하고 싶거나, 데이터베이스 확장(PostgreSQL) 및 데이터베이스 뷰(현재 지원되지 않음)를 로드하려는 경우 마이그레이션을 편집할 수 있습니다.

내부적으로 Prisma Migrate는 [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)를 사용해 [schema drift](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#detecting-schema-drift)를 감지하고 새로운 마이그레이션을 생성합니다.

Note

`prisma migrate dev`는 일회용 데이터베이스를 사용하는 개발 환경에서만 사용하도록 설계되었습니다.

`prisma migrate dev`가 schema drift 또는 마이그레이션 이력 충돌을 감지하면, 마이그레이션 이력과 데이터베이스 스키마를 동기화하기 위해 데이터베이스를 reset(삭제 후 재생성)하라는 안내가 표시됩니다.

만화로 shadow database 설명 보기

![A cartoon that shows how the shadow database works.](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/shadow-database.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

#

- 스키마 드리프트 해결하기

스키마 드리프트(schema drift)는 예상한 데이터베이스 스키마와 마이그레이션 이력의 내용이 서로 다를 때 발생합니다. 예를 들어 Prisma 스키마와 `prisma/migrations`를 함께 업데이트하지 않은 채 데이터베이스 스키마를 수동으로 변경하면 이런 상황이 발생할 수 있습니다.

이런 경우 [`prisma migrate diff`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff) 명령을 사용해 마이그레이션 이력을 비교하고 데이터베이스 스키마에 적용된 변경을 되돌릴 수 있습니다.

![Revert database schema with migrate diff](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/prisma-migrate-diff-flow.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

`migrate diff`를 사용하면 다음 중 하나를 수행하는 SQL을 생성할 수 있습니다:

- 데이터베이스 스키마에서 이루어진 변경을 되돌려 현재 Prisma 스키마와 동기화
- Prisma 스키마와 `/migrations`의 누락된 변경을 적용하도록 데이터베이스 스키마를 앞으로 진행

그다음 [`prisma db execute`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-execute) 명령으로 변경 사항을 데이터베이스에 적용할 수 있습니다.

#

- 스키마 프로토타이핑하기

[`prisma db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push) 명령은 마이그레이션(`/prisma/migrations`)을 영속화하지 않고 Prisma 스키마와 데이터베이스 스키마를 동기화할 수 있게 해줍니다. `prisma db push` 명령은 다음 상태 조각을 사용해 데이터베이스 상태를 추적합니다:

- Prisma 스키마
- 데이터베이스 스키마

![prisma db push development flow](https://docs.prisma.io/docs/img/orm/prisma-migrate/understanding-prisma-migrate/mental-model-illustrations/db-push-flow.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

`prisma db push` 명령은 다음과 같은 경우에 유용합니다:

- 다른 개발자 환경이나 staging/production 환경처럼 다른 환경에 이 변경을 배포할 필요 없이, 로컬에서 스키마 설계를 **빠르게 프로토타이핑하고 반복**하고 싶을 때

- `prisma db push`로 수행된 변경 사항이나 단계가 아니라 **원하는 최종 상태(desired end-state)** 에 도달하는 것을 우선합니다 (`prisma db push`로 수행된 변경을 미리 볼 방법은 없습니다)
  - 스키마 변경이 데이터에 어떤 영향을 주는지 제어할 필요가 없습니다. 스키마 및 데이터 마이그레이션을 조율할 방법이 없기 때문입니다. `prisma db push`가 변경으로 인해 데이터 손실이 발생할 것으로 예상하면, `--accept-data-loss` 옵션으로 데이터 손실을 수락하거나 프로세스를 중단할 수 있습니다. 변경 내용을 사용자 지정할 방법은 없습니다.

`prisma db push` 명령이 데이터베이스 스키마에 파괴적 변경(destructive change)을 감지하면, 데이터베이스를 재설정하라는 프롬프트가 표시됩니다. 예를 들어, 기본값을 제공하지 않은 채 기존 데이터가 있는 테이블에 필수 필드를 추가하면 이런 일이 발생합니다.

Schema Drift

[schema drift](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting#schema-drift)는 데이터베이스 스키마가 마이그레이션 이력 및 마이그레이션 테이블과 동기화되지 않았을 때 발생합니다.

- Prisma Migrate in a staging and production environment

#

- Sync your migration histories

[`prisma migrate deploy`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-deploy) 명령은 개발 환경의 마이그레이션 이력을 **staging 또는 production 환경** 의 데이터베이스와 동기화할 수 있게 해줍니다.

내부적으로 `migrate deploy` 명령은 다음을 수행합니다:

1. 이미 적용된 마이그레이션(`_prisma_migrations`에 기록됨)과 마이그레이션 이력(`/prisma/migrations`)을 비교합니다
2. 대기 중인 마이그레이션을 적용합니다
3. 새 마이그레이션으로 `_prisma_migrations` 테이블을 업데이트합니다

![Workflow of Prisma Migrate](https://docs.prisma.io/docs/img/orm/prisma-migrate/workflows/deploy-db.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

이 명령은 GitHub Actions 같은 자동화된 CI/CD 환경에서 실행해야 합니다.

마이그레이션 이력(`/migrations`)이 없다면, 즉 `prisma db push`를 사용 중이라면 staging 및 production 환경에서도 계속 `prisma db push`를 사용해야 합니다. 이 경우 데이터베이스 스키마에 적용되는 변경에 주의해야 합니다. 일부는 파괴적일 수 있습니다. 예를 들어 `prisma db push`는 컬럼 이름 변경을 수행하는 상황을 알 수 없습니다. 따라서 데이터베이스 재설정(drop and re-creation) 프롬프트가 표시됩니다.
