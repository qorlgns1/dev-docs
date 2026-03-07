---
title: "다운 마이그레이션 생성하기"
description: "지정한 마이그레이션 파일을 되돌리는 다운 마이그레이션 SQL 파일을 생성하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/generating-down-migrations

# 다운 마이그레이션 생성하기

지정한 마이그레이션 파일을 되돌리는 다운 마이그레이션 SQL 파일을 생성하는 방법

마이그레이션 SQL 파일을 생성할 때, 해당 "업 마이그레이션(up migration)" 파일의 스키마 변경을 되돌리는 "다운 마이그레이션(down migration)" SQL 파일도 함께 만들고 싶을 수 있습니다. 참고로 "다운 마이그레이션"은 "마이그레이션 롤백(migration rollback)"이라고도 부릅니다.

이 가이드에서는 Prisma Migrate의 [`migrate diff` command](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff)를 사용해 다운 마이그레이션을 생성하는 방법과, 업 마이그레이션이 실패한 경우 [`db execute`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-execute) 명령으로 이를 프로덕션 데이터베이스에 적용하는 방법을 설명합니다.

이 가이드는 관계형 데이터베이스용 SQL 다운 마이그레이션 생성에만 적용됩니다. MongoDB에는 적용되지 않습니다.

## 다운 마이그레이션 생성 시 고려사항

다운 마이그레이션 파일을 생성할 때는 다음 사항을 유의해야 합니다.

- 다운 마이그레이션은 [실패한 마이그레이션에 다운 마이그레이션 적용하기](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/generating-down-migrations#how-to-apply-your-down-migration-to-a-failed-migration)의 단계에 따라, 실패한 마이그레이션 이후 데이터베이스 스키마를 되돌리는 데 사용할 수 있습니다. 이 경우 `migrate resolve` 명령을 사용해야 하며, 이 명령은 실패한 마이그레이션에만 사용할 수 있습니다. 업 마이그레이션이 성공했는데 이를 되돌리고 싶다면, 대신 `schema.prisma` 파일을 업 마이그레이션 이전 상태로 되돌린 뒤 `migrate dev` 명령으로 새 마이그레이션을 생성해야 합니다.
- 다운 마이그레이션은 데이터베이스 스키마는 되돌리지만, 업 마이그레이션의 일부로 수행된 데이터 변경이나 애플리케이션 코드 변경은 되돌리지 않습니다. 예를 들어 마이그레이션 중 데이터를 변경하는 스크립트가 있다면, 다운 마이그레이션 실행 시 해당 데이터는 원래대로 복구되지 않습니다.
- 마이그레이션 파일에 수동으로 변경하거나 추가한 SQL을 되돌리는 데는 `migrate diff`를 사용할 수 없습니다. 뷰(view)나 트리거(trigger) 같은 커스텀 추가 사항이 있다면 다음이 필요합니다.
  - [아래 안내](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/generating-down-migrations#how-to-generate-and-run-down-migrations)에 따라 다운 마이그레이션 생성
  - 데이터베이스에 적용하기 전에 편집할 수 있도록 [`migrate dev --create-only`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference)로 업 마이그레이션 생성
  - 업 마이그레이션에 커스텀 SQL 수동 추가(예: 뷰 추가)
  - 다운 마이그레이션에 반대로 동작하는 커스텀 SQL 수동 추가(예: 뷰 삭제)

## 다운 마이그레이션 생성 및 실행 방법

이 섹션에서는 해당 업 마이그레이션과 함께 다운 마이그레이션 SQL 파일을 생성하고, 이후 프로덕션에서 업 마이그레이션이 실패했을 때 이를 실행해 데이터베이스 스키마를 되돌리는 방법을 설명합니다.

예시로, `User`와 `Post` 모델이 있는 다음 Prisma 스키마를 시작점으로 사용합니다.

schema.prisma

```
    model Post {
      id       Int     @id @default(autoincrement())
      title    String  @db.VarChar(255)
      content  String?
      author   User    @relation(fields: [authorId], references: [id])
      authorId Int
    }

    model User {
      id    Int     @id @default(autoincrement())
      name  String?
      posts Post[]
    }
```

해당 업 마이그레이션을 생성하기 전에, 먼저 다운 마이그레이션을 생성해야 합니다.

- 마이그레이션 생성하기
  - 업 마이그레이션에 필요한 변경사항이 반영되도록 Prisma 스키마를 수정합니다. 이 예시에서는 새 `Profile` 모델을 추가합니다.

schema.prisma

```
model Post {
          id       Int     @id @default(autoincrement())
          title    String  @db.VarChar(255)
          content  String?
          author   User    @relation(fields: [authorId], references: [id])
          authorId Int
        }

        model Profile {
          id     Int     @id @default(autoincrement())
          bio    String?
          user   User    @relation(fields: [userId], references: [id])
          userId Int     @unique
        }

        model User {
          id      Int      @id @default(autoincrement())
          name    String?
          posts   Post[]
          profile Profile?
        }
```

- 다운 마이그레이션용 SQL 파일을 생성합니다. 이를 위해 `migrate diff`로 다음을 비교합니다.
  - 새로 수정한 스키마
  - 마지막 마이그레이션 이후의 스키마 상태

그리고 결과를 SQL 스크립트 `down.sql`로 출력합니다.

'target(to) 상태'를 지정하는 방법은 두 가지가 있습니다.

    * `--to-migrations` 사용: migrations 디렉터리에 있는 마이그레이션 상태와 비교합니다. 더 견고하므로 권장되는 옵션입니다. 이 옵션을 사용하려면 다음을 실행합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate diff \
      --from-schema prisma/schema.prisma \
      --to-migrations prisma/migrations \
      --script > down.sql
```

- `--to-config-datasource` (Prisma v7) 또는 `--to-schema-datasource` (Prisma 6) 사용: 데이터베이스 상태와 비교합니다. 이 방법은 섀도 데이터베이스가 필요 없지만, 데이터베이스 스키마가 최신 상태라는 전제에 의존합니다. 이 옵션을 사용하려면 다음을 실행합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate diff \
      --from-schema prisma/schema.prisma \
      --to-config-datasource \
      --script > down.sql
```

- `add_profile`이라는 이름으로 업 마이그레이션을 생성하고 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name add_profile
```

이렇게 하면 `prisma/migrations` 디렉터리 안에 `<timestamp>_add_profile` 새 디렉터리가 생성되고, 그 안에 새로운 `migration.sql` 업 마이그레이션 파일이 만들어집니다.

- `down.sql` 파일을 업 마이그레이션 파일과 함께 새 디렉터리에 복사합니다.

* 실패한 마이그레이션에 다운 마이그레이션 적용하기

이전 업 마이그레이션이 실패했다면, 다음 단계로 프로덕션 데이터베이스에 다운 마이그레이션을 적용할 수 있습니다.

실패한 업 마이그레이션 이후 프로덕션 데이터베이스에 다운 마이그레이션을 적용하려면 다음을 수행하세요.

- `db execute`를 사용해 데이터베이스 서버에서 `down.sql` 파일을 실행합니다(`prisma.config.ts`에 설정된 데이터베이스 URL 사용).

npm

pnpm

yarn

bun

```
    npx prisma db execute --file ./down.sql
```

- `migrate resolve`를 사용해 `add_profile`이라는 이름의 업 마이그레이션을 롤백했음을 기록합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate resolve --rolled-back add_profile
```
