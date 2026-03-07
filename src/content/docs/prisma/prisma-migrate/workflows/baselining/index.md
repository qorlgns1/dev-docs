---
title: "데이터베이스 베이스라인 설정"
description: "중요한 데이터를 포함한 기존 데이터베이스에 대해 마이그레이션 히스토리를 초기화하는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/baselining

# 데이터베이스 베이스라인 설정

중요한 데이터를 포함한 기존 데이터베이스에 대해 마이그레이션 히스토리를 초기화하는 방법입니다.

베이스라인 설정은 다음과 같은 데이터베이스에 대해 마이그레이션 히스토리를 초기화하는 과정입니다.

- ✔ Prisma Migrate를 사용하기 전에 이미 존재했던 데이터베이스
- ✔ 유지해야 하는 데이터(예: 프로덕션)를 포함하여 데이터베이스를 재설정할 수 없는 경우

베이스라인 설정은 하나 이상의 마이그레이션이 **이미 적용되었다고** Prisma Migrate에 알려줍니다. 이렇게 하면 이미 존재하는 테이블과 필드를 다시 생성하려 할 때 생성된 마이그레이션이 실패하는 것을 방지할 수 있습니다.

이는 개발 데이터베이스를 대상으로 하는 작업이므로, 데이터베이스를 재설정하고 다시 시드할 수 있다고 가정합니다.

베이스라인 설정은 [기존 데이터베이스가 있는 프로젝트에 Prisma Migrate 추가](https://docs.prisma.io/docs/orm/prisma-migrate/getting-started#adding-to-an-existing-project)의 일부입니다.

이 가이드는 **MongoDB에는 적용되지 않습니다**.
MongoDB에서는 `migrate deploy` 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다([MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb) 참고).

## 베이스라인 설정이 필요한 이유

기존 프로젝트에 Prisma Migrate를 추가하면, 초기 마이그레이션에는 **Prisma Migrate를 사용하기 전** 데이터베이스 상태를 다시 생성하는 데 필요한 모든 SQL이 포함됩니다:

![이미지에는 'Existing database'라는 라벨이 붙은 데이터베이스와 그 옆에 기존 데이터베이스 기능 목록(24 tables, 13 relationships, 92 fields, 3 indexes)이 표시됩니다. 'represented by'라는 라벨의 화살표가 기능 목록과 마이그레이션을 나타내는 박스를 연결합니다. 기존 데이터베이스의 기능은 단일 마이그레이션으로 표현됩니다.](https://docs.prisma.io/docs/img/orm/prisma-migrate/workflows/existing-database.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

초기 마이그레이션을 편집하여 Prisma 스키마로 표현할 수 없는 스키마 요소(예: 저장 프로시저, 트리거)를 포함할 수 있습니다.

이 초기 마이그레이션은 **개발 환경**을 생성하고 재설정하는 데 필요합니다:

![이미지에는 세 개의 마이그레이션이 있는 마이그레이션 히스토리가 표시됩니다. 각 마이그레이션은 파일 아이콘과 이름으로 표현되며, 모두 'migration history'라는 박스로 둘러싸여 있습니다. 첫 번째 마이그레이션에는 "State of database before Prisma Migrate"라는 추가 라벨이 있고, 나머지 두 마이그레이션에는 "Generated as part of the Prisma Migrate workflow" 라벨이 있습니다. 'prisma migrate dev'라는 라벨의 화살표가 마이그레이션 히스토리 박스와 "new development database"를 연결하며, 세 개의 마이그레이션이 모두 개발 데이터베이스에 적용되고 어느 것도 건너뛰지 않음을 나타냅니다.](https://docs.prisma.io/docs/img/orm/prisma-migrate/workflows/new-dev-db.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

하지만 이미 존재하고 재설정 _할 수 없는_ 데이터베이스(예: 프로덕션)에 `prisma migrate deploy`로 마이그레이션을 배포할 때는 **초기 마이그레이션을 포함하고 싶지 않습니다**.

대상 데이터베이스에는 이미 초기 마이그레이션이 생성한 테이블과 컬럼이 존재하므로, 이 요소들을 다시 생성하려 하면 대부분 오류가 발생합니다.

![세 개의 마이그레이션 파일(파일 아이콘과 이름)로 표현된 마이그레이션 히스토리가 'migration history' 박스로 둘러싸여 있습니다. 첫 번째 마이그레이션은 'do not apply', 두 번째와 세 번째 마이그레이션은 'apply'로 표시됩니다. 'prisma migrate deploy' 명령 라벨이 붙은 화살표가 마이그레이션 히스토리에서 'production' 데이터베이스로 향합니다.](https://docs.prisma.io/docs/img/orm/prisma-migrate/workflows/deploy-db.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

베이스라인 설정은 초기 마이그레이션이 **이미 적용되었다고** Prisma Migrate에 가정하게 하여 이 문제를 해결합니다.

## 데이터베이스 베이스라인 설정

베이스라인 마이그레이션을 생성하려면:

- 이미 `prisma/migrations` 폴더가 있다면 이 폴더를 삭제, 이동, 이름 변경 또는 보관합니다.
- 새 `prisma/migrations` 디렉터리를 만듭니다.
- 그런 다음 원하는 이름으로 또 다른 새 디렉터리를 만듭니다. 중요한 점은 Prisma migrate가 [사전식 순서](https://en.wikipedia.org/wiki/Lexicographic_order)로 마이그레이션을 적용할 수 있도록 `0_` 접두사를 사용하는 것입니다. 현재 타임스탬프 같은 다른 값을 사용할 수도 있습니다.
- `prisma migrate diff`를 사용해 마이그레이션을 생성하고 파일로 저장합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate diff \
      --from-empty \
      --to-schema prisma/schema.prisma \
      --script > prisma/migrations/0_init/migration.sql
```

- 무시해야 하는 각 마이그레이션에 대해 `prisma migrate resolve` 명령을 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --applied 0_init
```

이 명령은 대상 마이그레이션을 `_prisma_migrations` 테이블에 추가하고 적용된 것으로 표시합니다. 새 마이그레이션을 적용하기 위해 `prisma migrate deploy`를 실행하면 Prisma Migrate는:

1. 베이스라인 마이그레이션을 포함해 'applied'로 표시된 모든 마이그레이션을 건너뜁니다.
2. 베이스라인 마이그레이션 _이후_ 에 오는 새 마이그레이션을 적용합니다.
