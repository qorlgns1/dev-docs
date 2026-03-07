---
title: "패치 및 핫픽스"
description: "프로덕션 환경에 핫픽스 또는 패치를 적용한 뒤 마이그레이션 히스토리를 정합시키는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing

# 패치 및 핫픽스

프로덕션 환경에 핫픽스 또는 패치를 적용한 뒤 마이그레이션 히스토리를 정합시키는 방법입니다.

데이터베이스 패치 또는 핫픽스는 보통 시간적으로 긴급한 변경을 프로덕션에 직접 적용하는 작업입니다. 예를 들어, 느리게 실행되는 쿼리 문제를 해결하기 위해 프로덕션 데이터베이스에 인덱스를 직접 추가할 수 있습니다.

프로덕션 데이터베이스를 직접 패치하면 **schema drift** 가 발생합니다. 즉, 데이터베이스 스키마가 단일 진실 공급원(source of truth)에서 벗어나 마이그레이션 히스토리와 동기화되지 않은 상태가 됩니다. `prisma migrate resolve` 명령을 사용하면 `prisma migrate deploy`로 핫픽스를 제거했다가 다시 적용하지 않고도 마이그레이션 히스토리를 정합시킬 수 있습니다.

이 가이드는 **MongoDB에는 적용되지 않습니다**.
MongoDB에서는 `migrate dev` 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다([MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb) 참고).

## 패치 또는 핫픽스로 마이그레이션 히스토리 정합시키기

다음 시나리오는 프로덕션에서 수동 변경을 수행했고, 그 변경을 마이그레이션 히스토리와 다른 데이터베이스에 반영하려는 경우를 가정합니다.

프로덕션에서 마이그레이션 히스토리와 데이터베이스 스키마를 정합시키려면:

- 프로덕션에서 수행한 변경을 스키마에도 동일하게 반영합니다. 예: 특정 모델에 `@@index` 추가.
- 새 마이그레이션을 생성하고, CLI에 기록되는 타임스탬프를 포함한 전체 마이그레이션 이름(`20210316150542_retroactively_add_index`)을 메모합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name retroactively-add-index
```

```
    migrations/
    └─ 20210316150542_retroactively_add_index/
    └─ migration.sql

    Your database is now in sync with your schema.

    ✔ Generated Prisma Client (2.19.0-dev.29) to .\node_modules\@prisma\client in 190ms
```

- **`migrate deploy`를 실행하지 않고** 마이그레이션을 프로덕션에 반영합니다. 대신 Prisma Migrate가 핫픽스를 두 번째로 적용하려고 시도하지 않도록, 이전 단계에서 생성한 마이그레이션을 'already applied'로 표시합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --applied "20201127134938-retroactively-add-index"
```

이 명령은 실제 SQL을 실행하지 않고 마이그레이션 히스토리 테이블에 해당 마이그레이션을 추가합니다.

- 패치된 다른 데이터베이스에도 이전 단계를 반복합니다. 예: 스테이징 데이터베이스에 패치를 적용한 경우.
- 패치되지 않은 다른 데이터베이스에는 마이그레이션을 전파합니다. 예: 마이그레이션을 소스 컨트롤에 커밋하고 CI/CD 파이프라인이 모든 데이터베이스에 적용하도록 설정. `prisma migrate resolve` 명령으로 이미 적용됨으로 표시된 데이터베이스에는 마이그레이션이 적용되지 않습니다.

## 실패한 마이그레이션

마이그레이션은 다음과 같은 경우 실패할 수 있습니다:

- [실행 전에 마이그레이션을 수정](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)하여 구문 오류를 도입한 경우
- 이미 데이터가 있는 테이블에 필수(`NOT NULL`) 컬럼을 추가한 경우
- 마이그레이션 프로세스가 예기치 않게 중단된 경우
- 마이그레이션 도중 데이터베이스가 종료된 경우

`_prisma_migrations` 테이블의 각 마이그레이션에는 오류를 저장하는 `logs` 컬럼이 있습니다.

프로덕션 환경에서 실패한 마이그레이션을 처리하는 방법은 두 가지입니다:

- 롤백하고, 필요 시 문제를 수정한 뒤 다시 배포
- 마이그레이션 단계를 수동으로 완료하고 마이그레이션 해결 처리

* 옵션 1: 마이그레이션을 rolled back으로 표시하고 다시 배포

다음 예시는 마이그레이션을 롤백하고, 필요 시 문제를 수정한 후 다시 배포하는 방법을 보여줍니다:

- 마이그레이션을 rolled back으로 표시합니다. 이렇게 하면 `_prisma_migrations` 테이블의 마이그레이션 레코드가 롤백 상태로 갱신되어 다시 적용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --rolled-back "20201127134938_added_bio_index"
```

- 마이그레이션이 부분적으로 실행된 경우, 다음 중 하나를 선택할 수 있습니다:
  - 단계가 이미 완료되었는지 확인하도록 마이그레이션을 수정 (`CREATE TABLE ... IF NOT EXISTS` 등) _OR_
  - 완료된 단계를 수동으로 되돌림(예: 생성된 테이블 삭제)

마이그레이션을 수정했다면, 프로덕션 데이터베이스 상태가 개발 환경에 정확히 반영되도록 반드시 소스 컨트롤에 다시 반영해야 합니다.

- 해당되는 경우 실패 원인을 수정합니다. 예: SQL 스크립트 자체 문제로 마이그레이션이 실패한 경우. 변경된 마이그레이션은 반드시 소스 컨트롤에 다시 반영하세요.

- 마이그레이션을 다시 배포합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate deploy
```

- 옵션 2: 마이그레이션을 수동으로 완료하고 applied로 해결 처리

다음 예시는 마이그레이션 단계를 수동으로 완료하고 해당 마이그레이션을 applied로 표시하는 방법을 보여줍니다.

- 프로덕션 데이터베이스에서 마이그레이션 단계를 수동으로 완료합니다. 수동 단계가 마이그레이션 파일의 단계와 정확히 일치하는지 확인하고, 모든 변경 사항을 소스 컨트롤에 다시 반영합니다.

- 마이그레이션을 applied로 해결 처리합니다. 이렇게 하면 Prisma Migrate가 해당 마이그레이션을 성공적으로 적용된 것으로 간주합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --applied "20201127134938_my_migration"
```

## `migrate diff`와 `db execute`로 실패한 마이그레이션 수정하기

**Prisma v7 참고** : `prisma db execute`에서 `--url` 플래그가 제거되었습니다. 프로덕션 데이터베이스를 대상으로 이 명령을 실행하려면, `db execute` 실행 전에 `prisma.config.ts` 파일에 프로덕션 데이터베이스 URL을 설정해야 합니다. 프로덕션용 별도 설정 파일(예: `prisma.config.prod.ts`)을 만들고 `--config prisma.config.prod.ts`로 지정할 수 있습니다.

실패한 마이그레이션 복구를 돕기 위해 Prisma ORM은 마이그레이션 파일 생성 및 실행을 위한 다음 명령을 제공합니다:

- [`prisma migrate diff`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff): 두 데이터베이스 스키마 소스를 비교해, 첫 번째를 두 번째 상태로 만드는 마이그레이션을 생성합니다. 차이 요약 또는 sql script로 출력할 수 있습니다. 스크립트는 `> file_name.sql`로 파일에 출력하거나 `db execute --stdin` 명령으로 파이프할 수 있습니다.
- [`prisma db execute`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-execute): Prisma migrations 테이블과 상호작용하지 않고 SQL 스크립트를 데이터베이스에 적용합니다.

이 섹션에서는 실패한 마이그레이션 시나리오 예시를 보여주고, 이를 수정하기 위해 `migrate diff`와 `db execute`를 사용하는 방법을 설명합니다.

- 실패한 마이그레이션 예시

로컬 개발 환경과 프로덕션 환경 모두에서 스키마에 다음 `User` 모델이 있다고 가정합니다:

schema.prisma

```
    model User {
      id   Int    @id
      name String
    }
```

이 시점에서 스키마는 동기화되어 있지만, 두 환경의 데이터는 서로 다릅니다.

그다음 데이터 모델을 변경해 `Post` 모델을 추가하고 `User`의 `name` 필드를 unique로 만들기로 결정합니다:

schema.prisma

```
    model User {
      id    Int     @id
      name  String  @unique
      email String?
    }

    model Post {
      id    Int    @id
      title String
    }
```

`npx prisma migrate dev -n Unique` 명령으로 'Unique'라는 마이그레이션을 생성하면 로컬 마이그레이션 히스토리에 저장됩니다. 개발 환경에서는 적용에 성공했고, 이제 프로덕션에 배포할 차례입니다.

하지만 이 마이그레이션은 부분적으로만 실행될 수 있습니다. `Post` 모델 생성과 `email` 컬럼 추가는 성공하지만, `name` 필드를 unique로 만드는 단계에서 다음 오류와 함께 실패합니다:

```
    ERROR 1062 (23000): Duplicate entry 'paul' for key 'User_name_key'
```

이는 프로덕션 데이터베이스에 중복되지 않아야 하는 데이터가 있기 때문입니다(예: 같은 이름을 가진 사용자 2명).

이제 부분 실행된 마이그레이션 상태에서 수동으로 복구해야 합니다. 실패 상태에서 복구하기 전까지는 `prisma migrate deploy`를 사용한 후속 마이그레이션이 불가능합니다.

이 시점에서는 중복 데이터 처리 방식에 따라 두 가지 선택지가 있습니다:

- 중복 데이터가 유효하다는 것을 알게 되어 현재 개발 작업 방향으로는 진행할 수 없습니다. 전체 마이그레이션을 롤백하려면 [뒤로 이동하여 모든 변경 되돌리기](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing#moving-backwards-and-reverting-all-changes)를 참조하세요.
- 데이터베이스의 중복 데이터 존재가 의도치 않은 것이며 이를 수정하고 싶습니다. 수정 후 나머지 마이그레이션을 계속 진행하려면 [앞으로 이동하여 누락된 변경 적용하기](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing#moving-forwards-and-applying-missing-changes)를 참조하세요.

#

- 뒤로 이동하여 모든 변경 되돌리기

이 경우, 프로덕션 데이터베이스를 마지막 마이그레이션 이전 데이터 모델 상태로 되돌리는 마이그레이션을 생성해야 합니다.

- 먼저 실패한 마이그레이션 이전 시점의 마이그레이션 히스토리가 필요합니다. git 히스토리에서 가져오거나, 로컬 마이그레이션 히스토리에서 마지막 실패 마이그레이션 폴더를 삭제해도 됩니다.
- 이제 프로덕션 환경의 현재 실패 상태를 로컬 마이그레이션 히스토리에 지정된 상태로 되돌려야 합니다:
  - 다음 `prisma migrate diff` 명령을 실행합니다:

```
# Prisma 6
          npx prisma migrate diff \
            --from-url "$DATABASE_URL_PROD" \
            --to-migrations ./prisma/migrations \
            --shadow-database-url $SHADOW_DATABASE_URL \
            --script > backward.sql

          # Prisma v7 (with production config)
          npx prisma migrate diff \
            --from-config-datasource \
            --to-migrations ./prisma/migrations \
            --config prisma.config.prod.ts \
            --script > backward.sql
```

이렇게 하면 프로덕션 환경의 현재 실패 상태를 마이그레이션 히스토리로 정의된 목표 상태로 옮기는 데 필요한 모든 변경이 포함된 SQL 스크립트 파일이 생성됩니다.

    * 다음 `prisma db execute` 명령을 실행합니다:

```
# Prisma 6
          npx prisma db execute --url "$DATABASE_URL_PROD" --file backward.sql

          # Prisma v7 (with production config)
          npx prisma db execute --config prisma.config.prod.ts --file backward.sql
```

이 명령은 migrations 테이블과 상호작용하지 않고 대상 데이터베이스에 SQL 스크립트 변경 사항을 적용합니다.

    * 다음 `prisma migrate resolve` 명령을 실행합니다:

npm

pnpm

yarn

bun

```
npx prisma migrate resolve --rolled-back Unique
```

이렇게 하면 프로덕션 환경의 migrations 테이블에서 'Unique'라는 실패한 마이그레이션이 rolled back으로 표시됩니다.

이제 로컬 마이그레이션 히스토리는 프로덕션 데이터베이스의 현재 상태와 동일한 결과를 생성합니다. 이후 데이터모델을 다시 수정해, 현재 기능 요구(이름의 중복 허용)에 맞는 마이그레이션을 생성할 수 있습니다.

#

- 앞으로 이동하여 누락된 변경 적용하기

이 경우, 중복 데이터를 수정한 다음 계획대로 나머지 마이그레이션을 진행해야 합니다:

- 프로덕션에 마이그레이션 배포를 시도했을 때의 오류 메시지에서 `name` 컬럼에 중복 데이터가 있음을 이미 알려줬습니다. 문제를 일으키는 행을 수정하거나 삭제해야 합니다.
- 실패한 마이그레이션의 나머지 부분 적용을 이어서 진행해 `schema.prisma` 파일에 정의된 데이터 모델 상태로 맞춥니다.
- 다음 `prisma migrate diff` 명령을 실행합니다

npm

pnpm

yarn

bun

```
    npx prisma migrate diff --from-config-datasource --to-schema schema.prisma --config prisma.config.prod.ts --script > forward.sql
```

이렇게 하면 프로덕션 환경의 현재 실패 상태를 `schema.prisma` 파일에 정의된 목표 상태로 옮기는 데 필요한 모든 변경이 포함된 SQL 스크립트 파일이 생성됩니다.

- 다음 `prisma db execute` 명령을 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma db execute --config prisma.config.prod.ts --file forward.sql
```

이 명령은 migrations 테이블과 상호작용하지 않고 대상 데이터베이스에 SQL 스크립트 변경 사항을 적용합니다.

- 다음 `prisma migrate resolve` 명령을 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --applied Unique
```

이렇게 하면 프로덕션 환경의 migrations 테이블에서 'Unique'라는 실패한 마이그레이션이 applied로 표시됩니다.

이제 로컬 마이그레이션 히스토리는 프로덕션 환경의 상태와 동일한 결과를 생성합니다. 이제 기존에 알려진 `migrate dev` /`migrate deploy` 워크플로를 계속 사용할 수 있습니다.

## Prisma Migrate와 PgBouncer

연결 풀링을 위해 PgBouncer를 사용하는 환경에서 Prisma Migrate 명령을 실행하려고 하면 다음 오류가 표시될 수 있습니다:

```
    Error: undefined: Database error
    Error querying the database: db error: ERROR: prepared statement "s0" already exists
```

자세한 정보와 우회 방법은 [Prisma Migrate and PgBouncer workaround](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer)를 참고하세요. 업데이트는 [GitHub issue #6485](https://github.com/prisma/prisma/issues/6485)에서 확인하세요.
