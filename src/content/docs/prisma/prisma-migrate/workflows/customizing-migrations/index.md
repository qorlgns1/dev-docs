---
title: "마이그레이션 사용자 지정하기"
description: "프로덕션에서 데이터 손실을 방지하기 위해 적용 전에 마이그레이션 파일을 편집하는 방법입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations

# 마이그레이션 사용자 지정하기

프로덕션에서 데이터 손실을 방지하기 위해 적용 전에 마이그레이션 파일을 편집하는 방법입니다.

일부 시나리오에서는 마이그레이션 파일을 적용하기 전에 편집해야 합니다. 예를 들어 [1-1 관계의 방향을 변경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-change-the-direction-of-a-1-1-relation)할 때(외래 키를 한쪽에서 다른 쪽으로 이동) 데이터 손실 없이 진행하려면, 마이그레이션의 일부로 데이터를 이동해야 합니다. 이 SQL은 기본 마이그레이션에 포함되지 않으므로 수동으로 작성해야 합니다.

이 가이드는 마이그레이션 파일을 편집하는 방법을 설명하고, 그렇게 해야 할 수 있는 몇 가지 사용 사례 예시를 제공합니다.

## 마이그레이션 파일 편집 방법

적용 전에 마이그레이션 파일을 편집하는 일반적인 절차는 다음과 같습니다.

- 사용자 지정 SQL이 필요한 스키마 변경을 수행합니다(예: 기존 데이터 보존).
- 다음을 사용해 초안 마이그레이션을 생성합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- 생성된 SQL 파일을 수정합니다.
- 다음을 실행해 수정된 SQL을 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

- 예시: 필드 이름 바꾸기

기본적으로 스키마에서 필드 이름을 바꾸면 생성되는 마이그레이션은 다음을 수행합니다.

- 새 컬럼을 `CREATE` 합니다(예: `fullname`).
- 기존 컬럼(예: `name`)을 `DROP` 하고 해당 컬럼의 데이터도 함께 제거합니다.

프로덕션에서 마이그레이션 실행 시 실제로 필드를 **이름 변경**하고 데이터 손실을 피하려면, 데이터베이스에 적용하기 전에 생성된 마이그레이션 SQL을 수정해야 합니다. 다음 스키마 조각을 살펴보면 `biograpy` 필드의 철자가 잘못되어 있습니다.

schema.prisma

```
    model Profile {
      id       Int    @id @default(autoincrement())
      biograpy String
      userId   Int    @unique
      user     User   @relation(fields: [userId], references: [id])
    }
```

`biograpy` 필드를 `biography`로 이름 변경하려면:

스키마에서 필드 이름을 변경합니다:

```
    model Profile {
      id        Int    @id @default(autoincrement())
      biograpy  String
      biography String
      userId    Int    @unique
      user      User   @relation(fields: [userId], references: [id])
    }
```

- 데이터베이스에 적용하기 전에 편집할 수 있는 **초안 마이그레이션**을 만들기 위해 다음 명령어를 실행합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name rename-migration --create-only
```

- 표시된 것처럼 초안 마이그레이션을 편집하여 `DROP` / `DELETE`를 단일 `RENAME COLUMN`으로 변경합니다.

이전

이후

migration.sql

```
    ALTER TABLE "Profile" DROP COLUMN "biograpy",
    ADD COLUMN  "biography" TEXT NOT NULL;
```

- 저장한 뒤 마이그레이션을 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

같은 기법으로 `model`의 이름도 바꿀 수 있습니다. 생성된 SQL을 편집해 테이블을 삭제 후 재생성하지 말고 _이름 변경_ 하세요.

- 예시: 다운타임 없이 스키마를 발전시키기 위한 expand and contract 패턴 사용

기존 필드에 대한 스키마 변경(예: 필드 이름 변경)은 다운타임을 유발할 수 있습니다. 이는 기존 필드를 수정하는 마이그레이션을 적용한 시점과, 수정된 필드를 사용하는 새 애플리케이션 코드를 배포하는 시점 사이의 시간 구간에서 발생합니다.

필드 변경에 필요한 단계를, 변경을 점진적으로 도입하도록 설계된 일련의 개별 단계로 나누면 다운타임을 방지할 수 있습니다. 이 패턴을 _expand and contract pattern_ 이라고 합니다.

이 패턴은 두 가지 구성 요소를 포함합니다: 데이터베이스에 접근하는 애플리케이션 코드와, 변경하려는 데이터베이스 스키마입니다.

Prisma에서 _expand and contract_ 패턴으로 `bio` 필드를 `biography`로 이름 변경하는 과정은 다음과 같습니다.

- Prisma 스키마에 새 `biography` 필드를 추가하고 마이그레이션을 생성합니다.

schema.prisma

```
    model Profile {
     id        Int    @id @default(autoincrement())
     bio       String
     biography String
     userId    Int    @unique
     user      User   @relation(fields: [userId], references: [id])
    }
```

- _Expand_ : 애플리케이션 코드를 업데이트해 `bio`와 `biography` 필드 모두에 쓰되, 읽기는 계속 `bio` 필드에서 수행하고 코드를 배포합니다.
- 빈 마이그레이션을 생성하고 기존 데이터를 `bio`에서 `biography` 필드로 복사합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name copy_biography --create-only
```

migration.sql

```
    UPDATE "Profile" SET biography = bio;
```

4. 데이터베이스에서 `biography` 필드의 무결성을 검증합니다.
5. 애플리케이션 코드를 업데이트해 새 `biography` 필드에서 **읽도록** 합니다.
6. 애플리케이션 코드를 업데이트해 `bio` 필드에 **더 이상 쓰지 않도록** 합니다.
7. _Contract_ : Prisma 스키마에서 `bio`를 제거하고, `bio` 필드를 제거하는 마이그레이션을 생성합니다.

schema.prisma

```
    model Profile {
     id        Int    @id @default(autoincrement())
     bio       String
     biography String
     userId    Int    @unique
     user      User   @relation(fields: [userId], references: [id])
    }
```

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name remove_bio
```

이 접근 방식을 사용하면 애플리케이션 코드에서 사용 중인 기존 필드를 변경할 때 발생하기 쉬운 잠재적 다운타임을 피할 수 있고, 마이그레이션 적용과 업데이트된 애플리케이션 코드 배포 사이에 필요한 조율도 줄일 수 있습니다.

이 패턴은 데이터가 존재하고 애플리케이션 코드에서 사용 중인 컬럼 변경이 수반되는 모든 상황에 적용할 수 있습니다. 예를 들어 두 필드를 하나로 결합하거나, `1:n` 관계를 `m:n` 관계로 변환하는 경우가 있습니다.

자세히 알아보려면 Data Guide의 [the expand and contract pattern](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern) 문서를 확인하세요.

- 예시: 1-1 관계의 방향 변경

1-1 관계의 방향을 변경하려면:

- 스키마에서 변경을 수행합니다.

schema.prisma

```
    model User {
     id        Int      @id @default(autoincrement())
     name      String
     posts     Post[]
     profile   Profile? @relation(fields: [profileId], references: [id])
     profileId Int      @unique
    }

    model Profile {
     id        Int    @id @default(autoincrement())
     biography String
     user      User
    }
```

- 데이터베이스에 적용하기 전에 편집할 수 있는 **초안 마이그레이션**을 만들기 위해 다음 명령어를 실행합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name rename-migration --create-only
```

```
    ⚠️  There will be data loss when applying the migration:

    • The migration will add a unique constraint covering the columns `[profileId]` on the table `User`. If there are existing duplicate values, the migration will fail.
```

- 표시된 것처럼 초안 마이그레이션을 편집합니다.

이전

이후

migration

```
    -- DropForeignKey
    ALTER TABLE "Profile" DROP CONSTRAINT "Profile_userId_fkey";

    -- DropIndex
    DROP INDEX "Profile_userId_unique";

    -- AlterTable
    ALTER TABLE "Profile" DROP COLUMN "userId";

    -- AlterTable
    ALTER TABLE "User" ADD COLUMN     "profileId" INTEGER NOT NULL;

    -- CreateIndex
    CREATE UNIQUE INDEX "User_profileId_unique" ON "User"("profileId");

    -- AddForeignKey
    ALTER TABLE "User" ADD FOREIGN KEY ("profileId") REFERENCES "Profile"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

- 저장한 뒤 마이그레이션을 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```
