---
title: "스키마 프로토타이핑"
description: "마이그레이션 없이 를 사용해 Prisma 스키마를 빠르게 프로토타이핑하세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema

# 스키마 프로토타이핑

마이그레이션 없이 `db push`를 사용해 Prisma 스키마를 빠르게 프로토타이핑하세요.

Prisma CLI에는 스키마 프로토타이핑을 위한 전용 명령어가 있습니다: [`db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push)

`db push`는 Prisma Migrate와 동일한 엔진을 사용해 Prisma 스키마와 데이터베이스 스키마를 동기화합니다. `db push` 명령어는 다음을 수행합니다.

- 데이터베이스를 인트로스펙션하여 데이터베이스 스키마가 Prisma 스키마의 상태를 반영하도록 필요한 변경 사항을 추론하고 실행합니다.
- 기본적으로 데이터베이스 스키마에 변경이 적용된 후 제너레이터(예: Prisma Client)가 트리거됩니다. `prisma generate`를 수동으로 호출할 필요가 없습니다.
- `db push`가 변경으로 인해 데이터 손실이 발생할 수 있다고 예상하면 다음과 같이 동작합니다.
  - 오류를 발생시킵니다.
  - 그래도 변경을 적용하려면 `--accept-data-loss` 옵션을 요구합니다.

참고

- `db push`는 마이그레이션과 상호작용하지 않으며 마이그레이션에 의존하지도 않습니다. 마이그레이션 테이블 `_prisma_migrations`는 생성되거나 업데이트되지 않으며, 마이그레이션 파일도 생성되지 않습니다.
- PlanetScale을 사용하는 경우 `migrate` 대신 `db push` 사용을 권장합니다. 자세한 내용은 상황에 따라 Getting started 문서의 [Start from scratch guide](https://docs.prisma.io/docs/prisma-orm/quickstart/planetscale) 또는 [Add to existing project guide](https://docs.prisma.io/docs/prisma-orm/add-to-existing-project/planetscale)를 참고하세요.

## `db push`와 Prisma Migrate 선택하기

다음 경우 `db push`가 잘 맞습니다.

- 다른 개발자 환경이나 스테이징/프로덕션 환경처럼 다른 환경에 배포할 필요 없이, 로컬에서 스키마 설계를 **빠르게 프로토타이핑하고 반복**하고 싶을 때
- **원하는 최종 상태**에 도달하는 것을 우선시하고, 그 최종 상태에 도달하기 위해 실행된 변경이나 단계는 중요하지 않을 때 (`db push`로 적용될 변경 사항을 미리 확인하는 방법은 없습니다)
- 스키마 변경이 데이터에 미치는 영향을 제어할 필요가 없을 때. 스키마 마이그레이션과 데이터 마이그레이션을 오케스트레이션할 방법이 없습니다. `db push`가 변경으로 인해 데이터 손실이 발생할 것으로 예상하면 `--accept-data-loss` 옵션으로 데이터 손실을 수용하거나 프로세스를 중단해야 합니다. 변경 사항을 커스터마이징할 방법은 없습니다.

이 방식으로 `db push`를 사용하는 예시는 [Schema prototyping with `db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 참고하세요.

다음 경우 `db push`는 **권장되지 않습니다**.

- 데이터 손실 없이 다른 환경에 스키마 변경을 복제하고 싶을 때. 프로토타이핑에는 `db push`를 사용할 수 있지만, 스키마 변경을 커밋하고 다른 환경에 적용하려면 마이그레이션을 사용해야 합니다.
- 스키마 변경 실행 방식을 세밀하게 제어하고 싶을 때. 예: [열을 삭제하고 새로 만드는 대신 이름 변경](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations#example-rename-a-field).
- 시간에 따른 데이터베이스 스키마 변경 이력을 추적하고 싶을 때. `db push`는 이러한 변경을 추적할 수 있는 어떤 산출물도 만들지 않습니다.
- 스키마 변경을 되돌릴 수 있어야 할 때. 원래 상태로 되돌리기 위해 `db push`를 다시 사용할 수는 있지만, 데이터 손실이 발생할 수 있습니다.

## Prisma Migrate와 `db push`를 함께 사용할 수 있나요?

예, [개발 워크플로에서 `db push`와 Prisma Migrate를 함께 사용할 수 있습니다](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema). 예를 들면 다음과 같습니다.

- 프로젝트 초기에 `db push`로 스키마를 프로토타이핑하고, 첫 번째 초안이 만족스러울 때 마이그레이션 이력을 초기화합니다.
- 기존 스키마 변경을 `db push`로 프로토타이핑한 뒤, `prisma migrate dev`를 실행해 해당 변경으로부터 마이그레이션을 생성합니다(리셋하라는 안내가 표시됩니다).

## 새 스키마 프로토타이핑

다음 시나리오는 빈 데이터베이스와 새 스키마를 `db push`로 동기화하고, 그 스키마를 발전시키는 방법을 보여줍니다. 또한 `db push`가 변경으로 인한 데이터 손실을 감지했을 때 어떤 일이 일어나는지도 포함합니다.

- 스키마의 첫 번째 초안을 작성합니다.

schema.prisma

```
generator client {
          provider = "prisma-client"
          output   = "./generated"
        }

        datasource db {
          provider = "postgresql"
        }

        model User {
          id       Int      @id @default(autoincrement())
          name     String
          jobTitle String
          posts    Post[]
          profile  Profile?
        }

        model Profile {
          id       Int    @id @default(autoincrement())
          biograpy String // Intentional typo!
          userId   Int    @unique
          user     User   @relation(fields: [userId], references: [id])
        }

        model Post {
          id         Int        @id @default(autoincrement())
          title      String
          published  Boolean    @default(true)
          content    String     @db.VarChar(500)
          authorId   Int
          author     User       @relation(fields: [authorId], references: [id])
          categories Category[]
        }

        model Category {
          id    Int    @id @default(autoincrement())
          name  String @db.VarChar(50)
          posts Post[]

          @@unique([name])
        }
```

- `db push`를 사용해 초기 스키마를 데이터베이스에 푸시합니다.

npm

pnpm

yarn

bun

```
npx prisma db push
```

- 예시 데이터를 생성합니다.

main.ts

```
const add = await prisma.user.create({
          data: {
            name: "Eloise",
            jobTitle: "Programmer",
            posts: {
              create: {
                title: "How to create a MySQL database",
                content: "Some content",
              },
            },
          },
        });
```

- 추가적인 변경을 수행합니다. 예를 들어, 새로운 필수 필드를 만듭니다.

schema.prisma

```
model Post {
          id          Int        @id @default(autoincrement())
          title       String
          description String
          published   Boolean    @default(true)
          content     String     @db.VarChar(500)
          authorId    Int
          author      User       @relation(fields: [authorId], references: [id])
          categories  Category[]
        }
```

- 변경 사항을 푸시합니다.

npm

pnpm

yarn

bun

```
npx prisma db push
```

기본값을 제공하지 않으면 기존 데이터가 있는 테이블에 필수 필드를 추가할 수 없기 때문에 `db push`가 실패합니다.

- 데이터베이스의 **모든 데이터**를 리셋하고 마이그레이션을 다시 적용합니다.

npm

pnpm

yarn

bun

```
npx prisma migrate reset
```

참고

Prisma Migrate와 달리 `db push`는 데이터를 보존하도록 수정할 수 있는 마이그레이션을 생성하지 않으므로, 개발 환경에서의 프로토타이핑에 가장 적합합니다.

- 비교적 안정적인 상태에 도달할 때까지 스키마를 계속 발전시킵니다.

- 마이그레이션 이력을 초기화합니다.

npm

pnpm

yarn

bun

```
npx prisma migrate dev --name initial-state
```

초기 프로토타입에 도달하기까지의 단계는 보존되지 않습니다. `db push`는 이력을 생성하지 않습니다.

- 마이그레이션 이력과 Prisma 스키마를 소스 제어(예: Git)에 푸시합니다.

이 시점에서 프로토타이핑의 최종 초안은 마이그레이션으로 보존되며, 다른 환경(테스트, 프로덕션 또는 팀의 다른 구성원)으로 푸시할 수 있습니다.

## 기존 마이그레이션 이력으로 프로토타이핑

다음 시나리오는 이미 마이그레이션 이력이 있는 Prisma 스키마의 변경을 `db push`로 프로토타이핑하는 방법을 보여줍니다.

- 최신 Prisma 스키마와 마이그레이션 이력을 체크아웃합니다.

schema.prisma

```
generator client {
          provider = "prisma-client"
          output   = "./generated"
        }

        datasource db {
          provider = "postgresql"
        }

        model User {
          id       Int      @id @default(autoincrement())
          name     String
          jobTitle String
          posts    Post[]
          profile  Profile?
        }

        model Profile {
          id       Int    @id @default(autoincrement())
          biograpy String // Intentional typo!
          userId   Int    @unique
          user     User   @relation(fields: [userId], references: [id])
        }

        model Post {
          id         Int        @id @default(autoincrement())
          title      String
          published  Boolean    @default(true)
          content    String     @db.VarChar(500)
          authorId   Int
          author     User       @relation(fields: [authorId], references: [id])
          categories Category[]
        }

        model Category {
          id    Int    @id @default(autoincrement())
          name  String @db.VarChar(50)
          posts Post[]

          @@unique([name])
        }
```

- 새 기능을 프로토타이핑합니다. 여기에는 원하는 만큼의 단계가 포함될 수 있습니다. 예를 들면 다음과 같습니다.
  - `tags String[]` 필드를 만든 다음 `db push`를 실행합니다.
  - 필드 타입을 `tags Tag[]`로 변경하고 `Tag`라는 새 모델을 추가한 다음 `db push`를 실행합니다.
  - 생각을 바꿔 원래의 `tags String[]` 필드로 되돌린 다음 `db push`를 호출합니다.
  - 데이터베이스에서 `tags` 필드에 수동 변경을 가합니다. 예: 제약 조건 추가

여러 해결책을 실험한 후 최종 스키마 변경은 다음과 같습니다.

schema.prisma

```
model Post {
      id          Int        @id @default(autoincrement())
      title       String
      description String
      published   Boolean    @default(true)
      content     String     @db.VarChar(500)
      authorId    Int
      author      User       @relation(fields: [authorId], references: [id])
      categories  Category[]
      tags        String[]
    }
```

- 새 `tags` 필드를 추가하는 마이그레이션을 만들려면 `migrate dev` 명령어를 실행합니다.

npm

pnpm

yarn

bun

```
npx prisma migrate dev --name added-tags
```

Prisma Migrate는 프로토타이핑 중 수동 변경 및 `db push`로 적용한 변경이 마이그레이션 이력에 포함되어 있지 않기 때문에 리셋하라는 안내를 표시합니다.

```
√ Drift detected: Your database schema is not in sync with your migration history.

        We need to reset the PostgreSQL database "prototyping" at "localhost:5432".
```

이로 인해 전체 데이터 손실이 발생합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate reset
```

- Prisma Migrate는 기존 마이그레이션 이력을 재생하고, 스키마 변경을 기반으로 새 마이그레이션을 생성한 뒤, 해당 변경을 데이터베이스에 적용합니다.

`migrate dev`를 사용할 때 스키마 변경으로 인해 시드 스크립트가 더 이상 동작하지 않는다면, `--skip-seed` 플래그를 사용해 시드 스크립트를 무시할 수 있습니다.

이 시점에서 프로토타이핑의 최종 결과는 마이그레이션으로 보존되며, 다른 환경(테스트, 프로덕션 또는 팀의 다른 구성원)으로 푸시할 수 있습니다.
