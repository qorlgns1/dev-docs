---
title: "Cloudflare Workers 및 Pages에 배포하기"
description: "데이터베이스와 통신하기 위해 Prisma Client를 사용하는 앱을 Cloudflare Worker 또는 Cloudflare Pages에 배포할 때 알아야 할 사항을 확인하세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare

# Cloudflare Workers 및 Pages에 배포하기

데이터베이스와 통신하기 위해 Prisma Client를 사용하는 앱을 Cloudflare Worker 또는 Cloudflare Pages에 배포할 때 알아야 할 사항을 확인하세요.

요약

이 페이지에서는 Prisma ORM이 포함된 앱을 [Cloudflare Worker](https://developers.cloudflare.com/workers/) 또는 [Cloudflare Pages](https://developers.cloudflare.com/pages)에 배포할 때 필요한 모든 내용을 다룹니다.

이 페이지에서 답하는 질문

- Cloudflare Workers에 Prisma를 어떻게 배포하나요?
- Workers/Pages에서 어떤 드라이버가 동작하나요?
- `DATABASE_URL` 및 env를 어떻게 구성하나요?

## Cloudflare Workers에 배포할 때의 일반 고려사항

이 섹션에서는 사용하는 데이터베이스 제공자와 관계없이, Prisma ORM을 사용하면서 Cloudflare Workers 또는 Pages에 배포할 때 알아야 할 _일반적인_ 사항을 다룹니다.

- Prisma Postgres 사용

Prisma Postgres를 사용하여 Cloudflare Workers에 배포할 수 있습니다.

Worker를 생성한 뒤 다음을 실행하세요:

npm

pnpm

yarn

bun

```
    npx prisma@latest init --db
```

프로젝트 이름을 입력하고 데이터베이스 리전을 선택하세요.

이 명령은 다음을 수행합니다:

- CLI를 [Prisma Data Platform](https://console.prisma.io) 계정에 연결합니다. 로그인하지 않았거나 계정이 없다면, 브라우저가 열려 새 계정을 만들거나 기존 계정에 로그인하도록 안내합니다.
- 데이터베이스 모델을 위한 `schema.prisma` 파일이 포함된 `prisma` 디렉터리를 생성합니다.
- `DATABASE_URL`이 포함된 `.env` 파일을 생성합니다.

* 엣지 호환 드라이버 사용

Prisma ORM을 사용하는 Cloudflare Worker를 배포할 때는 [엣지 호환 드라이버](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/overview#edge-compatibility-of-database-drivers)와 Prisma ORM용 해당 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)를 사용해야 합니다.

Cloudflare Workers 및 Pages에서 사용할 수 있는 엣지 호환 드라이버는 다음과 같습니다:

- [Neon Serverless](https://neon.tech/docs/serverless/serverless-driver): HTTP를 사용해 데이터베이스에 접근
- [PlanetScale Serverless](https://planetscale.com/docs/tutorials/planetscale-serverless-driver): HTTP를 사용해 데이터베이스에 접근
- [`node-postgres`](https://node-postgres.com/) (`pg`): Cloudflare의 `connect()` (TCP)를 사용해 데이터베이스에 접근
- [`@libsql/client`](https://github.com/tursodatabase/libsql-client-ts): HTTP를 통해 Turso 데이터베이스에 접근할 때 사용
- [Cloudflare D1](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare): D1 데이터베이스에 접근할 때 사용

향후 Cloudflare Workers 및 Pages에서 기존 MySQL 데이터베이스에도 접근할 수 있도록 `node-mysql2` 드라이버에 대한 [작업도 진행 중](https://github.com/sidorares/node-mysql2/pull/2289)입니다.

애플리케이션이 PostgreSQL을 사용한다면 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 사용을 권장합니다. 엣지 런타임에서 완전히 지원되며, 별도의 엣지 호환 드라이버가 필요하지 않습니다. 현재 제약 사항은 [Prisma Postgres serverless driver limitations](https://docs.prisma.io/docs/postgres/database/serverless-driver#limitations)를 확인하세요.

- 데이터베이스 연결 URL을 환경 변수로 설정

먼저 Prisma 스키마의 `datasource` 블록이 올바르게 구성되어 있는지 확인하세요. 데이터베이스 연결 URL은 `prisma.config.ts`에서 구성합니다:

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

Worker를 **development** 에서 사용할 때는 로컬에서 [`.dev.vars` file](https://developers.cloudflare.com/workers/configuration/secrets/#local-development-with-secrets)을 통해 데이터베이스 연결을 구성할 수 있습니다.

위에서 언급한 `DATABASE_URL` 환경 변수를 사용한다고 가정하면, 다음과 같이 `.dev.vars` 안에 설정할 수 있습니다:

.dev.vars

```
    DATABASE_URL="your-database-connection-string"
```

위 스니펫에서 `your-database-connection-string`은 자리표시자이며, 예를 들어 아래처럼 본인의 연결 문자열 값으로 바꿔야 합니다:

.dev.vars

```
    DATABASE_URL="postgresql://admin:mypassword42@somehost.aws.com:5432/mydb"
```

`.dev.vars` 파일은 Prisma ORM에서 일반적으로 사용하는 `.env` 파일과 호환되지 않습니다.

즉, 필요할 때 Prisma ORM이 해당 환경 변수에 접근할 수 있도록 해야 합니다. 예를 들어 `prisma migrate dev` 같은 Prisma CLI 명령을 실행할 때입니다.

이를 달성하는 방법은 여러 가지가 있습니다:

- [`dotenv`](https://www.npmjs.com/package/dotenv-cli)를 사용해 Prisma CLI 명령을 실행하고, CLI가 환경 변수를 어디서 읽을지 지정합니다. 예:

```
dotenv -e .dev.vars -- npx prisma migrate dev
```

- [`dotenv`](https://www.npmjs.com/package/dotenv-cli)로 `.dev.vars`를 읽는 스크립트를 `package.json`에 생성합니다. 그런 다음 `npm run env -- npx prisma migrate dev`처럼 `prisma` 명령을 실행할 수 있습니다. 스크립트 예시는 다음과 같습니다:

package.json

```
"scripts":  { "env": "dotenv -e .dev.vars" }
```

- `DATABASE_URL` 및 기타 관련 env vars를 `.env`라는 새 파일에 복제하여 Prisma ORM에서 사용하게 합니다.

`dotenv`가 필요한 접근 방식을 사용한다면 [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli) 패키지가 설치되어 있어야 합니다. 예를 들어 다음 명령으로 프로젝트 로컬에 설치할 수 있습니다: `npm install -D dotenv-cli`.

#

- 프로덕션

Worker를 **production** 에 배포할 때는 `wrangler` CLI를 사용해 데이터베이스 연결을 설정해야 합니다:

npm

pnpm

yarn

bun

```
    npx wrangler secret put DATABASE_URL
```

이 명령은 대화형이며, 터미널의 다음 단계에서 `DATABASE_URL` env var 값을 입력하라고 요청합니다.

이 명령을 실행하려면 인증이 필요하며, 인증되지 않은 경우 Cloudflare 계정 로그인을 요청합니다.

- 무료 계정의 크기 제한

Cloudflare는 [무료 플랜의 Workers에 대해 3 MB 크기 제한](https://developers.cloudflare.com/workers/platform/limits/)이 있습니다. Prisma ORM이 포함된 애플리케이션 번들이 이 크기를 초과하면 유료 Worker 플랜으로 업그레이드하는 것을 권장합니다.

- `@cloudflare/next-on-pages`로 Next.js 앱을 Cloudflare Pages에 배포

Cloudflare는 [`@cloudflare/next-on-pages`](https://github.com/cloudflare/next-on-pages)를 통해 Cloudflare Pages에서 Next.js 앱을 실행하는 옵션을 제공합니다. 안내는 [docs](https://developers.cloudflare.com/pages/framework-guides/nextjs/ssr/get-started/)를 참고하세요.

일부 테스트를 기반으로 다음을 확인했습니다:

- PlanetScale 또는 Neon Serverless Driver를 사용해 배포할 수 있습니다.
- `pg`를 사용하는 기존 PostgreSQL 배포는 동작하지 않습니다. 현재 `pg` 자체가 `@cloudflare/next-on-pages`와 동작하지 않기 때문입니다([여기](https://github.com/cloudflare/next-on-pages/issues/605) 참고).

이 내용에서 변경된 점을 발견하면 [Discord](https://pris.ly/discord?utm_source=docs&utm_medium=inline_text)로 알려주세요.

## 데이터베이스별 고려사항 및 예제

이 섹션에서는 Prisma ORM을 사용해 Cloudflare Worker를 배포하기 위한 데이터베이스별 지침을 제공합니다.

- 사전 준비

다음 섹션의 사전 준비로, 로컬에서 실행 중인 Cloudflare Worker와 설치된 Prisma CLI가 필요합니다.

아직 준비되지 않았다면 다음 명령을 실행할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm create cloudflare@latest prisma-cloudflare-worker-example -- --type hello-world
    cd prisma-cloudflare-worker-example
    npm install prisma --save-dev && npm install @prisma/client
    npx prisma init --output ../generated/prisma
```

또한 선택한 데이터베이스 제공자의 데이터베이스 인스턴스가 준비되어 있어야 합니다. 인스턴스 설정은 해당 제공자의 문서를 참고하세요.

아래 예제에서는 기본 `User` 모델을 사용합니다:

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
    }
```

- PostgreSQL (traditional)

TCP와 `pg` 드라이버를 통해 접근하는 기존 PostgreSQL 데이터베이스를 사용하는 경우 다음이 필요합니다:

- `@prisma/adapter-pg` database adapter를 사용 (자세한 내용은 [여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#using-driver-adapters))
- `wrangler.toml`에 `node_compat = true` 설정 ([Cloudflare docs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) 참고)

#

- 1\. Prisma 스키마 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면 [사전 준비](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#prerequisites)의 안내에 따라 Prisma ORM이 포함된 기본 Cloudflare Worker를 먼저 구성하세요.

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

다음으로 `DATABASE_URL` 환경 변수를 데이터베이스 연결 문자열 값으로 설정해야 합니다. Cloudflare에서 사용하는 `.dev.vars` 파일에서 이를 설정합니다:

.dev.vars

```
    DATABASE_URL="postgresql://admin:mypassword42@somehost.aws.com:5432/mydb"
```

Prisma CLI는 기본적으로 `.env` 파일만 호환되므로, `.dev.vars`에서 env vars를 로드하도록 아래 스크립트를 `package.json`에 추가할 수 있습니다. 이후 `prisma` 명령 실행 전에 이 스크립트로 env vars를 로드하면 됩니다.

`package.json`에 다음 스크립트를 추가하세요:

package.json

```
    {
      // ...
      "scripts": {
        // ....
        "env": "dotenv -e .dev.vars"
      },
      // ...
    }
```

이제 `.dev.vars`의 env vars에 명령이 접근할 수 있도록 하면서, 다음과 같이 Prisma CLI 명령을 실행할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma
```

#

- 2\. 의존성 설치

다음으로 필요한 패키지를 설치하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-pg
```

#

- 3\. `wrangler.toml`에 `node_compat = true` 설정

`wrangler.toml` 파일에 다음 줄을 추가하세요:

wrangler.toml

```
    node_compat = true
```

Cloudflare Pages에서는 `node_compat` 사용이 공식 지원되지 않습니다. Cloudflare Pages에서 `pg`를 사용하고 싶다면 [여기](https://github.com/cloudflare/workers-sdk/pull/2541#issuecomment-1954209855)에서 우회 방법을 확인할 수 있습니다.

#

- 4\. 데이터베이스 스키마 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면 Prisma 스키마에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 스키마를 마이그레이션해야 합니다(데이터베이스에 이미 필요한 테이블이 모두 있다면 이 단계는 건너뛰어도 됩니다):

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma migrate dev --name init
```

#

- 5\. Worker에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

다음은 `PrismaClient`를 인스턴스화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드 스니펫입니다:

```
    import { PrismaClient } from "./generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    export default {
      async fetch(request, env, ctx) {
        const adapter = new PrismaPg({ connectionString: env.DATABASE_URL });
        const prisma = new PrismaClient({ adapter });

        const users = await prisma.user.findMany();
        const result = JSON.stringify(users);
        ctx.waitUntil(prisma.$disconnect());
        return new Response(result);
      },
    };
```

#

- 6\. Worker를 로컬에서 실행하기

Worker를 로컬에서 실행하려면 `wrangler dev` 명령을 실행하면 됩니다:

npm

pnpm

yarn

bun

```
    npx wrangler dev
```

#

- 7\. `DATABASE_URL` 환경 변수를 설정하고 Worker 배포하기

Worker를 배포하려면 먼저 [`wrangler` CLI를 통해](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers) `DATABASE_URL` 환경 변수를 설정해야 합니다:

npm

pnpm

yarn

bun

```
    npx wrangler secret put DATABASE_URL
```

이 명령은 대화형이며, 다음 단계에서 터미널에 `DATABASE_URL` env var 값을 입력하라고 요청합니다.

이 명령을 실행하려면 인증이 필요하며, 인증되지 않은 경우 Cloudflare 계정 로그인을 요청합니다.

그다음 Worker를 계속 배포할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx wrangler deploy
```

명령을 실행하면 배포된 Worker에 접근할 수 있는 URL이 출력됩니다.

- PlanetScale

PlanetScale 데이터베이스를 사용하는 경우 다음이 필요합니다:

- `@prisma/adapter-planetscale` 데이터베이스 어댑터 사용([여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)에서 자세히 보기)

- 충돌하는 `cache` 필드를 수동으로 제거:

```
export default {
          async fetch(request, env, ctx) {
            const adapter = new PrismaPlanetScale({
              url: env.DATABASE_URL,
              // see https://github.com/cloudflare/workerd/issues/698
              fetch(url, init) {
                delete init["cache"];
                return fetch(url, init);
              },
            });
            const prisma = new PrismaClient({ adapter });

            // ...
          },
        };
```

#

- 1\. Prisma 스키마 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면 [Prerequisites](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#prerequisites)의 안내를 따라 Prisma ORM이 포함된 기본 Cloudflare Worker를 부트스트랩하세요.

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

다음으로 `DATABASE_URL` 환경 변수를 데이터베이스 연결 문자열 값으로 설정해야 합니다. 이는 Cloudflare에서 사용하는 `.dev.vars` 파일에서 설정합니다:

.dev.vars

```
    DATABASE_URL="mysql://32qxa2r7hfl3102wrccj:password@us-east.connect.psdb.cloud/demo-cf-worker-ps?sslaccept=strict"
```

Prisma CLI는 기본적으로 `.env` 파일과만 호환되므로, `.dev.vars`에서 env var를 로드하는 다음 스크립트를 `package.json`에 추가해 조정할 수 있습니다. 이후 `prisma` 명령 실행 전에 이 스크립트를 사용해 env var를 로드할 수 있습니다.

다음 스크립트를 `package.json`에 추가하세요:

package.json

```
    {
      // ...
      "scripts": {
        // ....
        "env": "dotenv -e .dev.vars"
      },
      // ...
    }
```

이제 `.dev.vars`의 env var에 명령이 접근할 수 있도록 하면서 아래와 같이 Prisma CLI 명령을 실행할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma
```

#

- 2\. 의존성 설치

다음으로 필요한 패키지를 설치하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-planetscale
```

#

- 3\. 데이터베이스 스키마 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면, Prisma 스키마에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 스키마를 마이그레이션해야 합니다(이미 데이터베이스에 필요한 테이블이 모두 있다면 이 단계는 건너뛸 수 있습니다):

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma db push
```

#

- 4\. Worker에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

다음은 `PrismaClient`를 인스턴스화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드 스니펫입니다:

```
    import { PrismaClient } from "./generated/client";
    import { PrismaPlanetScale } from "@prisma/adapter-planetscale";

    export default {
      async fetch(request, env, ctx) {
        const adapter = new PrismaPlanetScale({
          url: env.DATABASE_URL,
          // see https://github.com/cloudflare/workerd/issues/698
          fetch(url, init) {
            delete init["cache"];
            return fetch(url, init);
          },
        });
        const prisma = new PrismaClient({ adapter });

        const users = await prisma.user.findMany();
        const result = JSON.stringify(users);
        ctx.waitUntil(prisma.$disconnect());
        return new Response(result);
      },
    };
```

#

- 6\. Worker를 로컬에서 실행하기

Worker를 로컬에서 실행하려면 `wrangler dev` 명령을 실행하면 됩니다:

npm

pnpm

yarn

bun

```
    npx wrangler dev
```

#

- 7\. `DATABASE_URL` 환경 변수를 설정하고 Worker 배포하기

Worker를 배포하려면 먼저 [`wrangler` CLI를 통해](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers) `DATABASE_URL` 환경 변수를 설정해야 합니다:

npm

pnpm

yarn

bun

```
    npx wrangler secret put DATABASE_URL
```

이 명령은 대화형이며, 다음 단계에서 터미널에 `DATABASE_URL` env var 값을 입력하라고 요청합니다.

이 명령을 실행하려면 인증이 필요하며, 인증되지 않은 경우 Cloudflare 계정 로그인을 요청합니다.

그다음 Worker를 계속 배포할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx wrangler deploy
```

명령을 실행하면 배포된 Worker에 접근할 수 있는 URL이 출력됩니다.

- Neon

Neon 데이터베이스를 사용하는 경우 다음이 필요합니다:

- `@prisma/adapter-neon` 데이터베이스 어댑터 사용([여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#using-driver-adapters)에서 자세히 보기)

#

- 1\. Prisma 스키마 및 데이터베이스 연결 구성

배포할 프로젝트가 없다면 [Prerequisites](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#prerequisites)의 안내를 따라 Prisma ORM이 포함된 기본 Cloudflare Worker를 부트스트랩하세요.

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

다음으로 `DATABASE_URL` 환경 변수를 데이터베이스 연결 문자열 값으로 설정해야 합니다. 이는 Cloudflare에서 사용하는 `.dev.vars` 파일에서 설정합니다:

.dev.vars

```
    DATABASE_URL="postgresql://janedoe:password@ep-nameless-pond-a23b1mdz.eu-central-1.aws.neon.tech/neondb?sslmode=require"
```

Prisma CLI는 기본적으로 `.env` 파일과만 호환되므로, `.dev.vars`에서 env var를 로드하는 다음 스크립트를 `package.json`에 추가해 조정할 수 있습니다. 이후 `prisma` 명령 실행 전에 이 스크립트를 사용해 env var를 로드할 수 있습니다.

다음 스크립트를 `package.json`에 추가하세요:

package.json

```
    {
      // ...
      "scripts": {
        // ....
        "env": "dotenv -e .dev.vars"
      },
      // ...
    }
```

이제 `.dev.vars`의 env var에 명령이 접근할 수 있도록 하면서 아래와 같이 Prisma CLI 명령을 실행할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma
```

#

- 2\. 의존성 설치

다음으로 필요한 패키지를 설치하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/adapter-neon
```

#

- 3\. 데이터베이스 스키마 마이그레이션(해당하는 경우)

위에서 `npx prisma init`을 실행했다면, Prisma 스키마에 정의된 `User` 테이블을 생성하기 위해 데이터베이스 스키마를 마이그레이션해야 합니다(이미 데이터베이스에 필요한 테이블이 모두 있다면 이 단계는 건너뛸 수 있습니다):

npm

pnpm

yarn

bun

```
    npm run env -- npx prisma migrate dev --name init
```

#

- 5\. Worker에서 Prisma Client를 사용해 데이터베이스에 쿼리 보내기

다음은 `PrismaClient`를 인스턴스화하고 데이터베이스에 쿼리를 보내는 데 사용할 수 있는 샘플 코드 스니펫입니다:

```
    import { PrismaClient } from "./generated/client";
    import { PrismaNeon } from "@prisma/adapter-neon";

    export default {
      async fetch(request, env, ctx) {
        const adapter = new PrismaNeon({ connectionString: env.DATABASE_URL });
        const prisma = new PrismaClient({ adapter });

        const users = await prisma.user.findMany();
        const result = JSON.stringify(users);
        ctx.waitUntil(prisma.$disconnect());
        return new Response(result);
      },
    };
```

#

- 6\. Worker를 로컬에서 실행하기

Worker를 로컬에서 실행하려면 `wrangler dev` 명령을 실행하면 됩니다:

npm

pnpm

yarn

bun

```
    npx wrangler dev
```

#

- 7\. `DATABASE_URL` 환경 변수를 설정하고 Worker 배포하기

Worker를 배포하려면 먼저 [`wrangler` CLI를 통해](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers) `DATABASE_URL` 환경 변수를 설정해야 합니다:

npm

pnpm

yarn

bun

```
    npx wrangler secret put DATABASE_URL
```

이 명령은 대화형이며, 다음 단계에서 터미널에 `DATABASE_URL` env var 값을 입력하라고 요청합니다.

이 명령을 실행하려면 인증이 필요하며, 인증되지 않은 경우 Cloudflare 계정 로그인을 요청합니다.

그다음 Worker를 계속 배포할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx wrangler deploy
```

명령을 실행하면 배포된 Worker에 접근할 수 있는 URL이 출력됩니다.

- Cloudflare D1

Cloudflare D1 사용하기

Prisma ORM과 [Cloudflare D1](https://developers.cloudflare.com/d1/)을 함께 사용하는 단계별 안내(스키마 설정, 마이그레이션, Worker 배포)는 전용 [Cloudflare D1 배포 가이드](https://docs.prisma.io/docs/guides/deployment/cloudflare-d1)를 참고하세요.
