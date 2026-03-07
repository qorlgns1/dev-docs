---
title: "마이그레이션 스쿼싱"
description: "여러 마이그레이션 파일을 하나의 마이그레이션으로 스쿼싱하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/squashing-migrations

# 마이그레이션 스쿼싱

여러 마이그레이션 파일을 하나의 마이그레이션으로 스쿼싱하는 방법

경우에 따라 일부 또는 전체 마이그레이션 파일을 하나의 마이그레이션으로 스쿼싱하는 것이 유용할 수 있습니다. 이 가이드에서는 이렇게 해야 할 수 있는 두 가지 시나리오를 설명합니다.

- 병합 전에 로컬 마이그레이션을 하나로 스쿼싱하여 [개발 환경에서 깔끔하게 마이그레이션](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/squashing-migrations#migrating-cleanly-from-a-development-environment)하기
- 모든 마이그레이션을 단일 파일로 스쿼싱하여 [프로덕션 환경에서 깔끔한 히스토리 만들기](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/squashing-migrations#creating-a-clean-history-in-a-production-environment)

두 경우 모두 Prisma Migrate는 [`migrate diff`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff) 명령을 사용해 두 데이터베이스 스키마를 비교하고, 한 상태에서 다른 상태로 이동하는 단일 SQL 파일을 출력하는 방식으로 이를 수행할 수 있는 도구를 제공합니다. 이 가이드의 나머지 부분에서는 두 시나리오에서 이를 수행하는 방법을 자세히 안내합니다.

- 개발 환경에서 깔끔하게 마이그레이션

브랜치 기반 워크플로로 개발할 때 마이그레이션 스쿼싱이 유용할 수 있습니다. 기능 브랜치에서 대규모 로컬 개발을 진행하는 동안 `migrate dev`를 사용해 여러 마이그레이션을 생성할 수 있습니다. 기능 개발이 완료되면, 마이그레이션 히스토리에는 `main` 브랜치로 푸시될 최종 마이그레이션 히스토리에서 원치 않는 불필요한 중간 단계가 포함될 수 있습니다.

프로덕션에서 중간 단계를 적용하지 않아야 하는 중요한 이유가 있을 수 있습니다. 예를 들어 데이터 손실을 일으키거나 매우 느리거나 중단을 유발할 수 있습니다. 이런 경우가 아니더라도, 프로덕션 환경의 마이그레이션 히스토리가 복잡해지는 것을 피하고 싶을 수 있습니다.

`migrate dev`를 사용해 이를 달성하는 자세한 단계는 [개발 환경에서 깔끔하게 마이그레이션하는 방법](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/squashing-migrations#how-to-migrate-cleanly-from-a-development-environment) 섹션을 참고하세요.

- 프로덕션 환경에서 깔끔한 히스토리 만들기

마이그레이션 스쿼싱은 프로덕션 환경에서 모든 마이그레이션 파일을 하나로 합치는 데에도 사용할 수 있습니다. 이는 프로덕션 환경에 긴 마이그레이션 히스토리가 누적되어, 중간 단계 때문에 새 환경에서 이를 재실행하는 데 추가 시간이 들고 부담이 커졌을 때 유용합니다. 팀이 마이그레이션 단계 자체에서 큰 가치를 얻지 못하고(필요하면 버전 관리 히스토리에서 되찾을 수 있으므로), 전체 히스토리를 단일 마이그레이션으로 스쿼싱하기로 결정할 수 있습니다.

`migrate diff`와 `migrate resolve`를 사용해 이를 달성하는 자세한 단계는 [프로덕션 환경에서 깔끔한 히스토리를 만드는 방법](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/squashing-migrations#how-to-create-a-clean-history-in-a-production-environment) 섹션을 참고하세요.

## 마이그레이션 스쿼싱 시 고려사항

마이그레이션을 스쿼싱할 때 `migration.sql` 파일에 수동으로 변경하거나 추가한 SQL은 유지되지 않는다는 점에 유의하세요. 뷰(view)나 트리거(trigger) 같은 커스텀 추가 사항이 있는 마이그레이션 파일이 있다면, 스쿼싱 후 다시 추가해야 합니다.

## 마이그레이션 스쿼싱 방법

이 섹션에서는 위에서 다룬 두 시나리오에서 마이그레이션을 스쿼싱하는 단계별 지침을 제공합니다.

- 개발 환경에서 깔끔하게 마이그레이션
- 프로덕션 환경에서 깔끔한 히스토리 만들기

* 개발 환경에서 깔끔하게 마이그레이션하는 방법

마이그레이션을 스쿼싱하기 전에 다음 시작 조건을 충족하는지 확인하세요.

- 스쿼싱 대상 마이그레이션의 내용이 아직 프로덕션 데이터베이스에 적용되지 않았음
- 프로덕션에 적용된 모든 마이그레이션이 이미 로컬 마이그레이션 히스토리에 포함되어 있음
- 브랜치에 추가한 새 마이그레이션 파일 어디에도 커스텀 SQL이 없음

기능 브랜치를 만든 이후 프로덕션 데이터베이스의 마이그레이션 히스토리가 분기되었다면, 먼저 프로덕션의 마이그레이션 히스토리와 데이터 모델 변경 사항을 로컬 히스토리에 병합해야 합니다.

그다음 다음 단계를 따르세요.

- 로컬 `./prisma/migrations` 폴더 내용을 `main` 브랜치의 마이그레이션 히스토리와 일치하도록 재설정합니다.
- 새 마이그레이션을 생성합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name squashed_migrations
```

이렇게 하면 다음을 수행하는 단일 마이그레이션이 생성됩니다.

- 재설정한 마이그레이션 히스토리로 표현된 `main` 브랜치 상태에서
- `./prisma/schema.prisma` 파일로 표현된 로컬 기능 상태까지
- 그리고 이를 `squashed_migrations`로 끝나는 새 디렉터리의 새 `migration.sql` 파일로 출력함(`--name` 플래그로 지정)

이 단일 마이그레이션 파일은 이제 `migrate deploy`를 사용해 프로덕션에 적용할 수 있습니다.

- 프로덕션 환경에서 깔끔한 히스토리를 만드는 방법

마이그레이션을 스쿼싱하기 전에 다음 시작 조건을 충족하는지 확인하세요.

- 마이그레이션 히스토리의 모든 마이그레이션이 프로덕션 데이터베이스에 적용되어 있음
- 데이터 모델이 마이그레이션 히스토리와 일치함
- 데이터 모델과 마이그레이션 히스토리가 동기화되어 있음

그다음, `main` 브랜치에서 진행하거나, 별도로 체크아웃한 새 브랜치에서 진행한 뒤 그곳에 다른 변경이 생기기 전에 `main`에 병합하세요.

- `./prisma/migrations` 디렉터리의 모든 내용을 삭제합니다.

- `./prisma/migrations` 디렉터리 안에 새 빈 디렉터리를 만듭니다. 이 가이드에서는 이를 `000000000000_squashed_migrations`라고 부릅니다. 이 안에 빈 `migration.sql` 파일을 새로 추가합니다.

이 마이그레이션의 이름을 앞에 0을 채운 `000000000000_squashed_migrations`로 지정하는 이유는, 이를 마이그레이션 디렉터리에서 첫 번째 마이그레이션으로 만들기 위해서입니다. Migrate는 디렉터리의 마이그레이션을 사전식(알파벳) 순서로 실행합니다. 그래서 `migrate dev`를 사용할 때 날짜와 시간을 접두사로 붙인 마이그레이션이 생성됩니다. 이후 마이그레이션보다 낮게 정렬되기만 하면 다른 이름을 사용해도 됩니다. 예: `0_squashed` 또는 `202207180000_squashed`.

- 다음을 수행하는 단일 마이그레이션을 생성합니다.
  - 빈 데이터베이스에서
  - `./prisma/schema.prisma` 파일로 표현된 현재 프로덕션 데이터베이스 스키마 상태까지
  - 그리고 이를 위에서 만든 `migration.sql` 파일로 출력함

이는 `migrate diff` 명령으로 수행할 수 있습니다. 프로젝트 루트 디렉터리에서 다음 명령을 실행하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate diff \
      --from-empty \
      --to-schema ./prisma/schema.prisma \
      --script > ./prisma/migrations/000000000000_squashed_migrations/migration.sql
```

- 이 마이그레이션이 프로덕션에 적용된 것으로 표시하여, 그곳에서 실행되지 않도록 합니다.

이는 [`migrate resolve`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-resolve) 명령을 사용해 `000000000000_squashed_migrations` 디렉터리의 마이그레이션을 이미 적용된 것으로 표시하면 됩니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve \
      --applied 000000000000_squashed_migrations
```

이제 프로덕션에 적용된 것으로 표시된 단일 마이그레이션 파일 하나를 갖게 됩니다. 새 체크아웃에서는 프로덕션 데이터베이스 스키마 상태로 이동시키는 마이그레이션 하나만 받게 됩니다.

프로덕션 데이터베이스에는 여전히 마이그레이션 테이블에 적용된 마이그레이션 히스토리가 남아 있습니다. 마이그레이션 폴더와 데이터 모델의 히스토리도 소스 제어에 그대로 남아 있습니다.
