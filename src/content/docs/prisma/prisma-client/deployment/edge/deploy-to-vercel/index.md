---
title: "Vercel Edge Functions 및 Middleware에 배포하기"
description: "데이터베이스와 통신하기 위해 Prisma Client를 사용하는 Edge function을 배포할 때 알아야 할 사항을 학습하세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel

# Vercel Edge Functions 및 Middleware에 배포하기

데이터베이스와 통신하기 위해 Prisma Client를 사용하는 Edge function을 배포할 때 알아야 할 사항을 학습하세요.

이 페이지에서는 [Vercel Edge Middleware](https://vercel.com/docs/functions/edge-middleware) 또는 [Vercel Edge Runtime](https://vercel.com/docs/functions/runtimes/edge-runtime)에 배포된 [Vercel Function](https://vercel.com/docs/functions)에서, 데이터베이스와 통신하기 위해 Prisma Client를 사용하는 앱을 배포할 때 알아야 할 모든 내용을 다룹니다.

이 페이지에서 답하는 질문

- Vercel Edge에 Prisma를 어떻게 배포하나요?
- 어떤 데이터베이스 드라이버가 지원되나요?
- env와 postinstall은 어떻게 구성하나요?

Vercel은 Vercel Functions에 대해 Node.js 및 edge runtime을 모두 지원합니다. Node.js runtime은 기본값이며 대부분의 사용 사례에 권장됩니다.

기본적으로 Vercel Functions는 Node.js runtime을 사용합니다. 필요하면 runtime을 명시적으로 설정할 수 있습니다:

```
    export const runtime = "edge"; // 'nodejs' is the default

    export function GET(request: Request) {
      return new Response(`I am a Vercel Function!`, {
        status: 200,
      });
    }
```

## Vercel Edge Functions 및 Edge Middleware에 배포할 때의 일반 고려사항

- Prisma Postgres 사용

Vercel의 edge runtime에서 Prisma Postgres를 사용할 수 있습니다. 전체 과정을 다루는 튜토리얼은 [Prisma Postgres를 사용해 애플리케이션을 Vercel에 배포하기](https://docs.prisma.io/docs/guides/frameworks/nextjs) 가이드를 따르세요.

- edge 호환 드라이버 사용

현재 Vercel의 Edge Runtime은 제한된 데이터베이스 드라이버만 지원합니다:

- [Neon Serverless](https://neon.tech/docs/serverless/serverless-driver)는 HTTP를 사용해 데이터베이스에 접근합니다([Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)와도 호환됨)
- [PlanetScale Serverless](https://planetscale.com/docs/tutorials/planetscale-serverless-driver)는 HTTP를 사용해 데이터베이스에 접근합니다
- [`@libsql/client`](https://github.com/tursodatabase/libsql-client-ts)는 Turso 데이터베이스에 접근할 때 사용됩니다

[`node-postgres`](https://node-postgres.com/) (`pg`)는 현재 Vercel Edge Functions에서 *지원되지 않는다는 점*에 유의하세요.

Prisma ORM을 사용하는 Vercel Edge Function을 배포할 때는, 이러한 [edge 호환 드라이버](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/overview#edge-compatibility-of-database-drivers) 중 하나와 Prisma ORM용 해당 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 사용해야 합니다.

애플리케이션이 PostgreSQL을 사용한다면 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 사용을 권장합니다. 이는 edge runtime에서 완전히 지원되며, 별도의 edge 호환 드라이버가 필요하지 않습니다. 다른 데이터베이스의 경우 [Prisma Accelerate](https://docs.prisma.io/docs/accelerate)를 사용하면 edge 호환성이 확장되어 _어떤_ edge function provider에서든 _모든_ 데이터베이스에 연결할 수 있습니다.

- 데이터베이스 연결 URL을 환경 변수로 설정

먼저 Prisma schema의 `datasource` 블록이 올바르게 구성되어 있는지 확인하세요. 데이터베이스 연결 URL은 `prisma.config.ts`에서 구성합니다:

```
    datasource db {
      provider = "postgresql" // this might also be `mysql` or another value depending on your database
    }
```

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

#

- 개발

**development** 환경에서는 `DATABASE_URL` 환경 변수(예: [`.env` files 사용](https://docs.prisma.io/docs/orm/more/dev-environment/environment-variables))를 통해 데이터베이스 연결을 구성할 수 있습니다.

#

- 프로덕션

Edge Function을 **production** 에 배포할 때는 `vercel` CLI를 사용해 데이터베이스 연결을 설정해야 합니다:

npm

pnpm

yarn

bun

```
    npx vercel env add DATABASE_URL
```

이 명령은 대화형으로 실행되며, 이후 단계에서 환경을 선택하고 `DATABASE_URL` 값을 입력하라는 안내를 받게 됩니다.

또는 Vercel Dashboard의 프로젝트 [UI](https://vercel.com/docs/projects/environment-variables#creating-environment-variables)에서 환경 변수를 설정할 수도 있습니다.

- `postinstall` hook에서 Prisma Client 생성

`package.json`에 다음과 같이 `"postinstall"` 섹션을 추가해야 합니다:

package.json

```
    {
      // ...,
      "postinstall": "prisma generate"
    }
```

- 무료 계정의 크기 제한

Vercel은 [무료 계정에서 1 MB 크기 제한](https://vercel.com/docs/functions/limitations)을 적용합니다. Prisma ORM을 포함한 애플리케이션 번들이 이 크기를 초과하면, 유료 계정으로 업그레이드하거나 Prisma Accelerate를 사용해 애플리케이션을 배포하는 것을 권장합니다.

## 데이터베이스별 고려사항 및 예제

이 섹션에서는 Prisma ORM과 함께 Vercel Edge Functions를 배포하기 위한 데이터베이스별 지침을 제공합니다.

- 사전 준비

다음 섹션의 사전 준비로, 로컬에서 실행되는 Vercel Edge Function(일반적으로 Next.js API route 형태)과 Prisma 및 Vercel CLI가 설치되어 있어야 합니다.

아직 준비되지 않았다면, [Vercel Functions Quickstart](https://vercel.com/docs/functions/quickstart) 지침에 따라 아래 명령으로 Next.js 앱을 처음부터 설정할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm install -g vercel
```

npm

pnpm

yarn

bun

```
    npx create-next-app@latest
```

npm

pnpm

yarn

bun

```
    npm install prisma --save-dev && npm install @prisma/client
```

npm

pnpm

yarn

bun

```
    npx prisma init --output ../app/generated/prisma
```

아래 예제에서는 기본 `User` 모델을 사용하겠습니다:

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
    }
```

- Vercel Postgres

Vercel Postgres를 사용하는 경우 다음이 필요합니다:

- Vercel Postgres는 내부적으로 [Neon](https://neon.tech/)을 사용하므로 `@prisma/adapter-neon` database adapter를 사용
- Vercel은 기본적으로 풀링된 연결 문자열을 `POSTGRES_PRISMA_URL`, 직접(비풀링) 연결 문자열을 `POSTGRES_URL_NON_POOLING`으로 제공합니다. Prisma CLI가 직접 연결 문자열을 사용하도록 `prisma.config.ts`를 구성

prisma.config.ts

```
import { defineConfig, env } from "prisma/config";

        export default defineConfig({
          schema: "prisma/schema.prisma",
          datasource: {
            url: env("POSTGRES_URL_NON_POOLING"), // direct connection for Prisma CLI
          },
        });
```

#

- 1\. Prisma schema 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면, [사전 준비](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#prerequisites) 지침에 따라 Prisma ORM이 포함된 기본 Next.js 앱을 부트스트랩하세요.

먼저 데이터베이스 연결이 올바르게 구성되어 있는지 확인하세요. 데이터베이스 연결 URL은 `prisma.config.ts`에서 구성합니다:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    datasource db {
      provider = "postgresql"
    }
```

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("POSTGRES_URL_NON_POOLING"), // direct connection for Prisma CLI
      },
    });
```

다음으로 데이터베이스 연결 값에 맞게 `POSTGRES_PRISMA_URL` 및 `POSTGRES_URL_NON_POOLING` 환경 변수를 설정해야 합니다.

`npx prisma init`을 실행했다면, 이 명령으로 생성된 `.env` 파일을 사용해 다음을 설정할 수 있습니다:

.env

```
    POSTGRES_PRISMA_URL="postgres://user:password@host-pooler.region.postgres.vercel-storage.com:5432/name?pgbouncer=true&connect_timeout=15"
    POSTGRES_URL_NON_POOLING="postgres://user:password@host.region.postgres.vercel-storage.com:5432/name"
```

#

- 2\. 의존성 설치

다음으로 필요한 패키지를 설치합니다:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-neon
```

#

- 3\. `postinstall` hook 구성

다음으로 `package.json`의 `scripts` 섹션에 새 키를 추가합니다:

package.json

```
    {
      // ...
      "scripts": {
        // ...
        "postinstall": "prisma generate"
      }
    }
```

#

- 4\. 데이터베이스 schema 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면 Prisma schema에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 schema를 마이그레이션해야 합니다(데이터베이스에 필요한 테이블이 이미 모두 있다면 이 단계는 건너뛸 수 있습니다):

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name init
```

#

- 5\. Vercel Edge Function에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

프로젝트를 처음부터 생성했다면 다음과 같이 새 edge function을 만들 수 있습니다.

먼저 다음 명령을 사용해 새 API route를 생성합니다:

```
    mkdir src/app/api
    mkdir src/app/api/edge
    touch src/app/api/edge/route.ts
```

방금 생성한 `app/api/edge/route.ts` 파일에서 `PrismaClient`를 초기화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드는 다음과 같습니다:

app/api/edge/route.ts

```
    import { NextResponse } from "next/server";
    import { PrismaClient } from "./generated/client";
    import { PrismaNeon } from "@prisma/adapter-neon";

    export const runtime = "nodejs"; // can also be set to 'edge'

    export async function GET(request: Request) {
      const adapter = new PrismaNeon({ connectionString: process.env.POSTGRES_PRISMA_URL });
      const prisma = new PrismaClient({ adapter });

      const users = await prisma.user.findMany();

      return NextResponse.json(users, { status: 200 });
    }
```

#

- 6\. 로컬에서 Edge Function 실행

다음 명령으로 앱을 실행합니다:

npm

pnpm

yarn

bun

```
    npm run dev
```

이제 다음 URL로 Edge Function에 접근할 수 있습니다: [`http://localhost:3000/api/edge`](http://localhost:3000/api/edge).

#

- 7\. `POSTGRES_PRISMA_URL` 환경 변수 설정 및 Edge Function 배포

다음 명령으로 Vercel에 프로젝트를 배포합니다:

npm

pnpm

yarn

bun

```
    npx vercel deploy
```

프로젝트가 Vercel에 생성된 뒤에는 `POSTGRES_PRISMA_URL` 환경 변수를 설정해야 합니다(첫 배포였다면 실패했을 가능성이 큽니다). 이는 Vercel UI에서 설정하거나 다음 명령으로 설정할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx vercel env add POSTGRES_PRISMA_URL
```

이 시점에서 Vercel Dashboard에서 배포된 애플리케이션 URL을 확인하고 `/api/edge` route를 통해 edge function에 접근할 수 있습니다.

- PlanetScale

PlanetScale 데이터베이스를 사용하는 경우 다음이 필요합니다:

- `@prisma/adapter-planetscale` database adapter 사용([여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)에서 자세히 보기)

#

- 1\. Prisma schema 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면, [사전 준비](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#prerequisites) 지침에 따라 Prisma ORM이 포함된 기본 Next.js 앱을 부트스트랩하세요.

먼저 데이터베이스 연결이 올바르게 구성되어 있는지 확인하세요. 데이터베이스 연결 URL은 `prisma.config.ts`에서 구성합니다:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    datasource db {
      provider     = "mysql"
      relationMode = "prisma" // required for PlanetScale (as by default foreign keys are disabled)
    }
```

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

다음으로 Prisma와 Next.js가 env vars를 읽을 때 모두 사용하는 `.env` 파일에서 `DATABASE_URL` 환경 변수를 설정해야 합니다:

.env

```
    DATABASE_URL="mysql://32qxa2r7hfl3102wrccj:password@us-east.connect.psdb.cloud/demo-cf-worker-ps?sslaccept=strict"
```

#

- 2\. 의존성 설치

다음으로 필요한 패키지를 설치합니다:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-planetscale
```

#

- 3\. `postinstall` hook 구성

다음으로, `package.json`의 `scripts` 섹션에 새 키를 추가하세요:

package.json

```
    {
      // ...
      "scripts": {
        // ...
        "postinstall": "prisma generate"
      }
    }
```

#

- 4\. 데이터베이스 스키마 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면, Prisma 스키마에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 스키마를 마이그레이션해야 합니다(데이터베이스에 이미 필요한 모든 테이블이 있다면 이 단계는 건너뛰어도 됩니다):

npm

pnpm

yarn

bun

```
    npx prisma db push
```

#

- 5\. Edge Function에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

프로젝트를 처음부터 만들었다면, 다음과 같이 새 edge function을 만들 수 있습니다.

먼저, 다음 명령어 등을 사용해 새 API route를 생성하세요:

```
    mkdir src/app/api
    mkdir src/app/api/edge
    touch src/app/api/edge/route.ts
```

방금 생성한 새 `app/api/edge/route.ts` 파일에서 `PrismaClient`를 인스턴스화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드 스니펫은 다음과 같습니다:

app/api/edge/route.ts

```
    import { NextResponse } from "next/server";
    import { PrismaClient } from "./generated/client";
    import { PrismaPlanetScale } from "@prisma/adapter-planetscale";

    export const runtime = "nodejs"; // can also be set to 'edge'

    export async function GET(request: Request) {
      const adapter = new PrismaPlanetScale({ url: process.env.DATABASE_URL });
      const prisma = new PrismaClient({ adapter });

      const users = await prisma.user.findMany();

      return NextResponse.json(users, { status: 200 });
    }
```

#

- 6\. Edge Function을 로컬에서 실행

다음 명령어로 앱을 실행하세요:

npm

pnpm

yarn

bun

```
    npm run dev
```

이제 다음 URL을 통해 Edge Function에 접근할 수 있습니다: [`http://localhost:3000/api/edge`](http://localhost:3000/api/edge).

#

- 7\. `DATABASE_URL` 환경 변수를 설정하고 Edge Function 배포

다음 명령어를 실행해 Vercel로 프로젝트를 배포하세요:

npm

pnpm

yarn

bun

```
    npx vercel deploy
```

프로젝트가 Vercel에 생성된 후에는 `DATABASE_URL` 환경 변수를 설정해야 합니다(첫 배포였다면 배포가 실패했을 가능성이 큽니다). 이는 Vercel UI에서 하거나 다음 명령어를 실행해 설정할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx vercel env add DATABASE_URL
```

이 시점에서 Vercel Dashboard에서 배포된 애플리케이션의 URL을 확인하고 `/api/edge` route를 통해 edge function에 접근할 수 있습니다.

- Neon

Neon 데이터베이스를 사용하는 경우 다음이 필요합니다:

- `@prisma/adapter-neon` 데이터베이스 어댑터를 사용합니다([여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#using-driver-adapters)에서 자세히 알아보기)

#

- 1\. Prisma 스키마 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면, [Prerequisites](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#prerequisites)의 안내에 따라 Prisma ORM이 포함된 기본 Next.js 앱을 부트스트랩하세요.

먼저 데이터베이스 연결이 올바르게 구성되어 있는지 확인하세요. 데이터베이스 연결 URL은 `prisma.config.ts`에서 구성합니다:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    datasource db {
      provider = "postgresql"
    }
```

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

다음으로, Prisma와 Next.js가 환경 변수를 읽을 때 모두 사용하는 `.env` 파일에 `DATABASE_URL` 환경 변수를 설정해야 합니다:

.env

```
    DATABASE_URL="postgresql://janedoe:password@ep-nameless-pond-a23b1mdz.eu-central-1.aws.neon.tech/neondb?sslmode=require"
```

#

- 2\. 의존성 설치

다음으로, 필요한 패키지를 설치하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-neon
```

#

- 3\. `postinstall` hook 구성

다음으로, `package.json`의 `scripts` 섹션에 새 키를 추가하세요:

package.json

```
    {
      // ...
      "scripts": {
        // ...
        "postinstall": "prisma generate"
      }
    }
```

#

- 4\. 데이터베이스 스키마 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면, Prisma 스키마에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 스키마를 마이그레이션해야 합니다(데이터베이스에 이미 필요한 모든 테이블이 있다면 이 단계는 건너뛰어도 됩니다):

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name init
```

#

- 5\. Edge Function에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

프로젝트를 처음부터 만들었다면, 다음과 같이 새 edge function을 만들 수 있습니다.

먼저, 다음 명령어 등을 사용해 새 API route를 생성하세요:

```
    mkdir src/app/api
    mkdir src/app/api/edge
    touch src/app/api/edge/route.ts
```

방금 생성한 새 `app/api/edge/route.ts` 파일에서 `PrismaClient`를 인스턴스화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드 스니펫은 다음과 같습니다:

app/api/edge/route.ts

```
    import { NextResponse } from "next/server";
    import { PrismaClient } from "./generated/client";
    import { PrismaNeon } from "@prisma/adapter-neon";

    export const runtime = "nodejs"; // can also be set to 'edge'

    export async function GET(request: Request) {
      const adapter = new PrismaNeon({ connectionString: process.env.DATABASE_URL });
      const prisma = new PrismaClient({ adapter });

      const users = await prisma.user.findMany();

      return NextResponse.json(users, { status: 200 });
    }
```

#

- 6\. Edge Function을 로컬에서 실행

다음 명령어로 앱을 실행하세요:

npm

pnpm

yarn

bun

```
    npm run dev
```

이제 다음 URL을 통해 Edge Function에 접근할 수 있습니다: [`http://localhost:3000/api/edge`](http://localhost:3000/api/edge).

#

- 7\. `DATABASE_URL` 환경 변수를 설정하고 Edge Function 배포

다음 명령어를 실행해 Vercel로 프로젝트를 배포하세요:

npm

pnpm

yarn

bun

```
    npx vercel deploy
```

프로젝트가 Vercel에 생성된 후에는 `DATABASE_URL` 환경 변수를 설정해야 합니다(첫 배포였다면 배포가 실패했을 가능성이 큽니다). 이는 Vercel UI에서 하거나 다음 명령어를 실행해 설정할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx vercel env add DATABASE_URL
```

이 시점에서 Vercel Dashboard에서 배포된 애플리케이션의 URL을 확인하고 `/api/edge` route를 통해 edge function에 접근할 수 있습니다.

## Vercel Fluid와 함께 Prisma ORM 사용하기

[Fluid compute](https://vercel.com/fluid)는 Vercel의 컴퓨팅 모델로, 서버리스의 유연성과 서버의 안정성을 결합하여 스트리밍 데이터 및 AI API 같은 동적 워크로드에 이상적입니다. Vercel의 Fluid compute는 [edge 및 Node.js runtime을 모두 지원](https://vercel.com/docs/fluid-compute#available-runtime-support)합니다. 기존 서버리스 플랫폼의 일반적인 과제는 함수가 일시 중단되고 풀이 유휴 연결을 닫을 수 없을 때 데이터베이스 연결이 누수되는 문제입니다. Fluid는 함수가 일시 중단되기 전에 유휴 연결이 해제되도록 [`attachDatabasePool`](https://vercel.com/blog/the-real-serverless-compute-to-database-connection-problem-solved)을 제공합니다.

Fluid에서 연결을 안전하게 관리하려면 `attachDatabasePool`을 [Prisma의 driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)와 함께 사용하세요:

```
    import { Pool } from "pg";
    import { attachDatabasePool } from "@vercel/functions";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/client";

    const pool = new Pool({ connectionString: process.env.POSTGRES_URL });

    attachDatabasePool(pool);

    const prisma = new PrismaClient({
      adapter: new PrismaPg(pool),
    });
```
