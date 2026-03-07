---
title: "마이그레이션 히스토리"
description: "Prisma ORM이 마이그레이션 히스토리를 사용해 스키마 변경 사항을 추적하는 방식"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories

# 마이그레이션 히스토리

Prisma ORM이 마이그레이션 히스토리를 사용해 스키마 변경 사항을 추적하는 방식

마이그레이션 히스토리는 데이터 모델 변경의 이력을 의미하며, 다음으로 구성됩니다.

- 각 마이그레이션마다 하위 폴더와 `migration.sql` 파일이 있는 `prisma/migrations` 폴더:

```
    migrations/
      └─ 20210313140442_init/
        └─ migration.sql
      └─ 20210313140442_added_job_title/
        └─ migration.sql
```

`migrations` 폴더는 데이터 모델 히스토리의 **단일 진실 공급원(source of truth)** 입니다.

- 데이터베이스의 `_prisma_migrations` 테이블(다음 항목을 확인하는 데 사용됨):
  - 마이그레이션이 데이터베이스에 실행되었는지 여부
  - 적용된 마이그레이션이 삭제되었는지 여부
  - 적용된 마이그레이션이 변경되었는지 여부

마이그레이션을 변경하거나 삭제하면(**권장되지 않음**), 다음 단계는 [개발 환경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production#production-and-testing-environments)(따라서 `migrate dev` 사용)인지, [프로덕션/테스트 환경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production#production-and-testing-environments)(따라서 `migrate deploy` 사용)인지에 따라 달라집니다.

## 이미 적용된 마이그레이션은 수정하거나 삭제하지 마세요

일반적으로 이미 적용된 마이그레이션은 **수정하거나 삭제하면 안 됩니다**. 이렇게 하면 개발 환경과 프로덕션 환경의 마이그레이션 히스토리 사이에 불일치가 생길 수 있으며, 처음에는 문제가 없어 _보이더라도_ 예기치 못한 결과를 초래할 수 있습니다.

다음 시나리오는 겉보기에 무해해 보이는 불일치를 만드는 변경을 시뮬레이션합니다.

- 개발 환경에서 **이미 적용된** **기존 마이그레이션**을 수정하여 `VARCHAR(550)` 값을 `VARCHAR(560)`으로 변경합니다.

migrations.sql

```
-- AlterTable
         ALTER TABLE "Post" ALTER COLUMN "content" SET DATA TYPE VARCHAR(560);
```

이 변경 후에는 Prisma 스키마에는 여전히 `@db.VarChar(550)`가 남아 있으므로, 마이그레이션 히스토리의 최종 상태가 더 이상 Prisma 스키마와 일치하지 않습니다.

- `prisma migrate dev`를 실행하면 마이그레이션이 변경되었기 때문에 오류가 발생하고 데이터베이스 재설정을 제안합니다.

- `prisma migrate reset` 실행 \- Prisma Migrate가 데이터베이스를 재설정하고, 수정한 마이그레이션을 포함해 모든 마이그레이션을 다시 적용합니다.

- 기존 마이그레이션을 모두 적용한 뒤, Prisma Migrate는 마이그레이션 히스토리의 최종 상태를 Prisma 스키마와 비교하고 불일치를 감지합니다.
  - Prisma 스키마: `@db.VarChar(550)`
  - 데이터베이스 스키마: `VARCHAR(560)`

- Prisma Migrate는 값을 다시 `550`으로 되돌리는 새 마이그레이션을 생성합니다. 마이그레이션 히스토리의 최종 상태는 Prisma 스키마와 일치해야 하기 때문입니다.

- 이후 `prisma migrate deploy`로 프로덕션 및 테스트 환경에 마이그레이션을 배포할 때마다, 스키마의 최종 상태가 일치하더라도 Prisma Migrate는 마이그레이션 히스토리가 일치하지 않는다고 항상 **경고**합니다(그리고 명령을 실행할 때마다 계속 경고합니다):

```
6 migrations found in prisma/migrations
        WARNING The following migrations have been modified since they were applied:
        20210310143435_change_type
```

`migrate reset` 후 겉으로는 문제가 없어 보이는 변경도 실제 문제를 숨길 수 있습니다. 특히 변경 내용이 고도로 커스터마이즈된 마이그레이션과 관련된 경우, 개발 환경에서는 재현되지 않는 버그가 프로덕션에서 발생하거나 그 반대 상황이 생길 수 있습니다.

Prisma Migrate가 이미 적용된 마이그레이션의 누락 또는 수정을 보고한다면, 재설정보다 **근본 원인**(파일 복원 또는 변경 되돌리기) 해결을 권장합니다.

## 마이그레이션 히스토리를 소스 컨트롤에 커밋하기

`prisma/migrations` 폴더 전체를 소스 컨트롤에 커밋해야 합니다. 여기에는 [프로바이더 변경을 시도했는지](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/limitations-and-known-issues#you-cannot-automatically-switch-database-providers) 감지하는 데 사용되는 `prisma/migrations/migration_lock.toml` 파일도 포함됩니다.

`schema.prisma` 파일만 소스 컨트롤로 관리하는 것으로는 충분하지 않으며, 마이그레이션 히스토리도 반드시 포함해야 합니다. 이유는 다음과 같습니다.

- [마이그레이션 커스터마이징](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production#customizing-migrations)을 시작하면, 마이그레이션 히스토리에는 **Prisma 스키마로 표현할 수 없는 정보**가 포함됩니다. 예를 들어, 브레이킹 체인지로 인해 발생할 수 있는 데이터 손실을 완화하도록 마이그레이션을 커스터마이즈할 수 있습니다.
- 스테이징, 테스트, 프로덕션 환경에 변경을 배포할 때 사용하는 `prisma migrate deploy` 명령은 마이그레이션 파일만 실행합니다. 모델을 가져오기 위해 Prisma 스키마를 사용하지 않습니다.
