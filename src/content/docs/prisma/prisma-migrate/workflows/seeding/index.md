---
title: "시딩(Seeding)"
description: "Prisma ORM의 통합 시딩 기능과 Prisma Client를 사용해 데이터베이스를 시딩하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding

# 시딩(Seeding)

Prisma ORM의 통합 시딩 기능과 Prisma Client를 사용해 데이터베이스를 시딩하는 방법을 알아보세요.

시딩을 사용하면 데이터베이스에 동일한 데이터를 일관되게 다시 생성할 수 있으며, 다음과 같은 용도로 활용할 수 있습니다:

- 기본 언어 또는 통화처럼, 애플리케이션 시작에 필요한 데이터를 데이터베이스에 채웁니다.
- 개발 환경에서 애플리케이션을 검증하고 사용하는 데 필요한 기본 데이터를 제공합니다. 이는 특히 Prisma Migrate를 사용하는 경우 유용한데, Prisma Migrate는 때때로 개발 데이터베이스 초기화를 요구하기 때문입니다.

### 동영상 보기: 데이터베이스 시딩하기

## Prisma ORM에서 데이터베이스를 시딩하는 방법

Prisma ORM의 통합 시딩 기능은 `prisma.config.ts`의 `migrations` 객체 안 `"seed"` 키에 명령어가 정의되어 있기를 기대합니다. 이 명령어는 어떤 것이든 가능하며, `prisma db seed`는 해당 명령어를 실행하기만 합니다. 이 가이드와 기본 권장 방식에서는 프로젝트의 `prisma/` 폴더 안에 시드 스크립트를 작성하고, 명령어로 이를 시작하는 방식을 권장합니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";
    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx prisma/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

## Prisma Migrate와 통합된 시딩

데이터베이스 시딩은 `prisma db seed`를 실행할 때 수행됩니다. `prisma db seed`를 사용하면 시드 명령을 언제 호출할지 _직접_ 결정할 수 있습니다. 예를 들어 테스트 설정이나 새로운 개발 환경 준비에 유용합니다.

Prisma ORM v7 변경 사항

Prisma ORM v7에서는 `npx prisma db seed`를 실행할 때만 시딩이 **명시적으로 트리거**됩니다. `prisma migrate dev` 또는 `prisma migrate reset` 중 자동 시딩은 제거되었습니다.

## 예제 시드 스크립트

여기서는 다양한 상황에 맞는 구체적인 시드 스크립트를 제안합니다. 필요에 맞게 자유롭게 커스터마이즈할 수 있으며, 여기 제시된 형태 그대로 사용할 수도 있습니다:

- 데이터베이스 시딩하기
  - `seed.ts`라는 새 파일을 생성합니다. 이 파일은 프로젝트 폴더 구조 내 어디에나 둘 수 있습니다. 아래 예제에서는 `/prisma` 폴더에 배치합니다.

  - `seed.ts` 파일에서 Prisma Client를 import하고, 초기화한 뒤, 몇 개의 레코드를 생성합니다. 예시로 `User`와 `Post` 모델이 있는 다음 Prisma 스키마를 사용합니다:

schema.prisma

```
    model User {
     id    Int    @id @default(autoincrement())
     email String @unique
     name  String
     posts Post[]
    }

    model Post {
     id        Int     @id @default(autoincrement())
     title     String
     content   String
     published Boolean
     user      User    @relation(fields: [userId], references: [id])
     userId    Int
    }
```

`prisma/seed.ts` 파일에서 새로운 사용자와 게시물을 생성합니다:

Prisma ORM v7 요구 사항

Prisma ORM v7에서는 `PrismaClient`를 드라이버 어댑터와 함께 초기화해야 합니다. 아래 예제는 PostgreSQL connection pool과 함께 `@prisma/adapter-pg`를 사용합니다.

seed.ts

```
    import "dotenv/config";
    import { Pool } from "pg";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "../prisma/generated/client";

    const connectionString = `${process.env.DATABASE_URL}`;
    const pool = new Pool({ connectionString });
    const adapter = new PrismaPg(pool);
    const prisma = new PrismaClient({ adapter });
    async function main() {
      const alice = await prisma.user.upsert({
        where: { email: "alice@prisma.io" },
        update: {},
        create: {
          email: "alice@prisma.io",
          name: "Alice",
          posts: {
            create: {
              title: "Check out Prisma with Next.js",
              content: "https://www.prisma.io/nextjs",
              published: true,
            },
          },
        },
      });
      const bob = await prisma.user.upsert({
        where: { email: "bob@prisma.io" },
        update: {},
        create: {
          email: "bob@prisma.io",
          name: "Bob",
          posts: {
            create: [
              {
                title: "Follow Prisma on Twitter",
                content: "https://twitter.com/prisma",
                published: true,
              },
              {
                title: "Follow Nexus on Twitter",
                content: "https://twitter.com/nexusgql",
                published: true,
              },
            ],
          },
        },
      });
      console.log({ alice, bob });
    }
    main()
      .then(async () => {
        await prisma.$disconnect();
        await pool.end();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        await pool.end();
        process.exit(1);
      });
```

- `typescript`, `tsx`, `@types/node`, `@prisma/adapter-pg`, `pg`, `@types/pg`, `dotenv`를 개발 의존성으로 추가합니다:

npm

pnpm

yarn

bun

```
    npm install -D typescript tsx @types/node @prisma/adapter-pg pg @types/pg dotenv
```

- `prisma.config.ts` 파일에 `seed` 필드를 추가합니다:

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";
    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx prisma/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

- 데이터베이스를 시딩하려면 `db seed` CLI 명령어를 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma db seed
```

여기서는 TypeScript를 사용했지만, 동일한 작업을 순수 JavaScript로도 수행할 수 있습니다. 동일한 단계를 따르되 `prisma/seed.js` 파일(타입 없이)을 사용하고, `tsx` 대신 `node prisma/seed.js`를 호출하면 됩니다.

- raw SQL 쿼리로 데이터베이스 시딩하기

raw SQL 쿼리를 사용해서 데이터로 데이터베이스를 시딩할 수도 있습니다.

이를 위해 일반 텍스트 `.sql` 파일(예: 데이터 덤프)을 사용할 수 있지만, 쿼리 길이가 짧다면 raw 쿼리를 `seed.js` 파일에 넣는 편이 더 쉬운 경우가 많습니다. 이렇게 하면 데이터베이스 connection string을 따로 처리하거나 `psql` 같은 바이너리 의존성을 추가해야 하는 번거로움을 줄일 수 있습니다.

위 `schema.prisma`에 추가 데이터를 시딩하려면, `seed.js`(또는 `seed.ts`) 파일에 다음 내용을 추가합니다:

seed.js

```
    async function rawSql() {
      const result =
        await prisma.$executeRaw`INSERT INTO "User" ("id", "email", "name") VALUES (3, 'foo@example.com', 'Foo') ON CONFLICT DO NOTHING;`;
      console.log({ result });
    }
```

그리고 파일 끝부분에서 아래 변경처럼 이 함수를 promise 호출 체인에 연결합니다:

seed.js

```
    main()
      .then(rawSql)
      .then(async () => {
        await prisma.$disconnect();
        await pool.end();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        await pool.end();
        process.exit(1);
      });
```

- 어떤 언어로든 데이터베이스 시딩하기 (Bash 스크립트 사용)

TypeScript와 JavaScript 외에도 Bash 스크립트(`seed.sh`)를 사용해 Go 같은 다른 언어나 순수 SQL로 데이터베이스를 시딩할 수 있습니다.

다음 예제는 `seed.sh`와 같은 폴더에 있는 Go 스크립트를 실행합니다:

seed.sh

```
    #!/bin/sh
    # -e Exit immediately when a command returns a non-zero status.
    # -x Print commands before they are executed
    set -ex
    # Seeding command go
    run ./seed/
```

다음 예제는 `seed.sh`와 같은 폴더에 있는 SQL 스크립트를 실행하기 위해 [psql](https://www.postgresql.org/docs/13/app-psql.html)을 사용합니다:

seed.sh

```
    #!/bin/sh
    # -e Exit immediately when a command returns a non-zero status.
    # -x Print commands before they are executed
    set -ex
    # Seeding command
    psql file.sql
```

- 사용자 정의 인자

`prisma db seed`를 사용하면 시드 파일에서 사용자 정의 인자를 정의하고 이를 `prisma db seed` 명령어에 전달할 수 있습니다. 예를 들어 환경별로 다른 데이터를 시딩하거나, 일부 테이블에만 부분적으로 데이터를 시딩하도록 자신만의 인자를 정의할 수 있습니다.

다음은 환경별로 다른 데이터를 시딩하기 위해 사용자 정의 인자를 정의한 시드 파일 예제입니다:

seed.js

```
    import { parseArgs } from "node:util";

    const options = {
      environment: { type: "string" },
    };

    async function main() {
      const {
        values: { environment },
      } = parseArgs({ options });

      switch (environment) {
        case "development":
          /** data for your development */
          break;
        case "test":
          /** data for your test environment */
          break;
        default:
          break;
      }
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

그런 다음 `prisma db seed`를 사용할 때 [delimiter](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02)인 `--`를 추가한 뒤, 사용자 정의 인자를 전달해 `environment` 인자를 제공할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma db seed -- --environment development
```

## 더 알아보기

다음은 데이터베이스 시딩을 위해 개발 워크플로에서 Prisma ORM과 함께 통합할 수 있는 다른 도구들의 예시 목록입니다(일부만 포함):

- Supabase community project
- Replibyte
