---
title: "Config API 레퍼런스"
description: "Prisma Config 파일()은 TypeScript를 사용해 Prisma CLI를 구성합니다. 이 파일은 을 실행하면 자동으로 생성됩니다."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/prisma-config-reference

# Config API 레퍼런스

`prisma.config.ts` 구성 옵션에 대한 전체 레퍼런스

Prisma Config 파일(`prisma.config.ts`)은 TypeScript를 사용해 Prisma CLI를 구성합니다. 이 파일은 `prisma init`을 실행하면 자동으로 생성됩니다.

`defineConfig` 헬퍼 또는 TypeScript의 `satisfies` 연산자를 사용해 config를 정의할 수 있습니다.

- `defineConfig` 헬퍼 사용:

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

- `PrismaConfig` 타입과 함께 TypeScript의 `satisfies` 연산자 사용:

```
import "dotenv/config";
        import type { PrismaConfig } from "prisma";
        import { env } from "prisma/config";

        export default {
          schema: "prisma/schema.prisma",
          migrations: {
            path: "prisma/migrations",
            seed: "tsx prisma/seed.ts",
          },
          datasource: {
            url: env("DATABASE_URL"),
          },
        } satisfies PrismaConfig;
```

## 구성 인터페이스

다음은 `PrismaConfig` 타입의 단순화된 버전입니다:

```
    export declare type PrismaConfig = {
      // Whether features with an unstable API are enabled.
      experimental: {
        externalTables: boolean;
      };

      // The path to the schema file, or path to a folder that shall be recursively searched for *.prisma files.
      schema?: string;

      // Configuration for Prisma migrations.
      migrations?: {
        path: string;
        seed: string;
        initShadowDb: string;
      };

      // Configuration for the database view entities.
      views?: {
        path: string;
      };

      // Configuration for the `typedSql` preview feature.
      typedSql?: {
        path: string;
      };

      // Database connection configuration
      datasource?: {
        url: string;
        shadowDatabaseUrl?: string;
      };
    };
```

## 지원되는 파일 확장자

Prisma Config 파일은 `prisma.config.*` 또는 `.config/prisma.*` 형식으로 이름을 지정할 수 있으며, 확장자는 `js`, `ts`, `mjs`, `cjs`, `mts`, `cts`를 사용할 수 있습니다. 그 외 확장자도 다양한 TypeScript 컴파일러 설정과의 호환성을 위해 지원됩니다.

권장 사항

- 작은 TypeScript 프로젝트에는 **`prisma.config.ts`**를 사용하세요.
- 여러 구성 파일을 사용하는 큰 TypeScript 프로젝트에는 **`.config/prisma.ts`**를 사용하세요([`.config` 디렉터리 제안](https://github.com/pi0/config-dir) 준수).

## 옵션 레퍼런스

- `schema`

Prisma ORM이 스키마 파일을 찾고 로드하는 방식을 구성합니다. 파일 또는 폴더 경로를 지정할 수 있습니다. 상대 경로는 `prisma.config.ts` 파일 위치를 기준으로 해석됩니다. 스키마 위치 옵션에 대한 자세한 내용은 [여기](https://docs.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema)를 참고하세요.

| Property | Type     | Required | Default                                        |
| -------- | -------- | -------- | ---------------------------------------------- |
| `schema` | `string` | No       | `./prisma/schema.prisma` and `./schema.prisma` |

- `tables.external` and `enums.external`

이 옵션들은 데이터베이스의 테이블과 enum 중 **외부에서 관리되는** 항목(Prisma Migrate가 관리하지 않음)을 선언합니다. Prisma Client로는 계속 조회할 수 있지만, 마이그레이션에서는 무시됩니다.

| Property          | Type       | Required | Default |
| ----------------- | ---------- | -------- | ------- |
| `tables.external` | `string[]` | No       | `[]`    |
| `enums.external`  | `string[]` | No       | `[]`    |

**예시:**

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      tables: {
        external: ["public.users"],
      },
      enums: {
        external: ["public.role"],
      },
    });
```

[`externalTables` 기능에 대한 자세한 내용은 여기](https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables)를 참고하세요.

- `migrations.path`

Prisma가 마이그레이션 파일을 저장하고 검색할 디렉터리 경로입니다.

| Property          | Type     | Required | Default |
| ----------------- | -------- | -------- | ------- |
| `migrations.path` | `string` | No       | none    |

- `migrations.seed`

`npx prisma db seed` 실행 시 수행할 명령어를 정의합니다. 시딩은 이 명령어로 명시적으로 실행될 때만 트리거됩니다.

| Property          | Type     | Required | Default |
| ----------------- | -------- | -------- | ------- |
| `migrations.seed` | `string` | No       | none    |

**예시:**

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        seed: "tsx db/seed.ts",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

- `migrations.initShadowDb`

이 옵션을 사용하면 Prisma가 마이그레이션 생성 전에 **shadow database**에서 실행할 SQL 구문을 정의할 수 있습니다. Prisma가 올바르게 마이그레이션을 생성하려면 해당 테이블의 구조를 알아야 하므로, [externally managed tables](https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables)와 함께 작업할 때 유용합니다.

| Property                  | Type     | Required | Default |
| ------------------------- | -------- | -------- | ------- |
| `migrations.initShadowDb` | `string` | No       | none    |

**예시:**

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
        initShadowDb: `
          CREATE TABLE public.users (id SERIAL PRIMARY KEY);
        `,
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
      tables: {
        external: ["public.users"],
      },
    });
```

[`externalTables` 기능에 대한 자세한 내용은 여기](https://docs.prisma.io/docs/orm/prisma-schema/data-model/externally-managed-tables)를 참고하세요.

- `views.path`

Prisma가 SQL 뷰 정의를 찾을 디렉터리 경로입니다.

| Property     | Type     | Required | Default |
| ------------ | -------- | -------- | ------- |
| `views.path` | `string` | No       | none    |

- `typedSql.path`

[`typedSql`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql)을 통해 타입을 생성할 때 사용하는 SQL 파일을 Prisma가 찾을 디렉터리 경로입니다.

| Property        | Type     | Required | Default |
| --------------- | -------- | -------- | ------- |
| `typedSql.path` | `string` | No       | none    |

- `experimental`

Prisma CLI에서 특정 실험적 기능을 활성화합니다.

| Property         | Type      | Required | Default |
| ---------------- | --------- | -------- | ------- |
| `externalTables` | `boolean` | No       | `false` |

예시:

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
      experimental: {
        externalTables: true,
      },
    });
```

실험 플래그를 활성화하지 않고 `externalTables` 기능을 사용하면 Prisma가 오류를 발생시킵니다:

```
    Failed to load config file "~" as a TypeScript/JavaScript module. Error: Error: The `externalTables` configuration requires `experimental.externalTables` to be set to `true`.
```

- `datasource.url`

인증 정보를 포함한 연결 URL입니다. [데이터베이스에서 제공하는 구문](https://docs.prisma.io/docs/orm/reference/connection-urls#format)을 사용합니다.

| Property         | Type     | Required | Default |
| ---------------- | -------- | -------- | ------- |
| `datasource.url` | `string` | Yes      | `''`    |

**예시:**

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

- `datasource.shadowDatabaseUrl`

Prisma Migrate가 사용하는 shadow database의 연결 URL입니다. shadow database로 클라우드 호스팅 데이터베이스를 사용할 수 있습니다.

| Property                       | Type     | Required | Default |
| ------------------------------ | -------- | -------- | ------- |
| `datasource.shadowDatabaseUrl` | `string` | No       | `''`    |

- `datasource.directUrl` (Removed)

Prisma ORM v7에서 제거됨

`datasource.directUrl` 속성은 Prisma ORM v7에서 제거되었으며, [`url` 속성](https://docs.prisma.io/docs/orm/reference/prisma-config-reference#datasourceurl)으로 대체되었습니다.

Prisma ORM v6.19 이하

데이터베이스에 직접 연결하기 위한 연결 URL입니다.

`url` 인자에 연결 풀러 URL(예: pgBouncer)을 사용하는 경우, 데이터베이스 직접 연결이 필요한 Prisma CLI 명령은 `directUrl` 인자의 URL을 사용합니다.

`directUrl` 속성은 Prisma Studio 5.1.0 이상에서 지원됩니다. [Prisma Postgres](https://docs.prisma.io/docs/postgres) 데이터베이스를 사용하는 경우에는 `directUrl` 속성이 필요하지 않습니다.

| Property               | Type     | Required | Default |
| ---------------------- | -------- | -------- | ------- |
| `datasource.directUrl` | `string` | No       | `''`    |

- `adapter` (Removed)

Prisma ORM v7에서 제거됨

`adapter` 속성은 Prisma ORM v7에서 제거되었습니다. Prisma ORM v7부터 드라이버 어댑터용 마이그레이션은 `prisma.config.ts`의 추가 구성 없이 자동으로 동작합니다.

Prisma ORM v6.19 이하

Prisma CLI가 마이그레이션을 실행할 때 사용할 Prisma 드라이버 어댑터 인스턴스를 반환하는 함수입니다. 이 함수는 유효한 Prisma 드라이버 어댑터로 resolve되는 `Promise`를 반환해야 합니다.

| Property  | Type                                                   | Required | Default |
| --------- | ------------------------------------------------------ | -------- | ------- |
| `adapter` | `() => Promise<SqlMigrationAwareDriverAdapterFactory>` | No       | none    |

Prisma ORM D1 드라이버 어댑터를 사용하는 예시:

```
    import path from "node:path";
    import type { PrismaConfig } from "prisma";
    import { PrismaD1 } from "@prisma/adapter-d1";

    export default {
      experimental: {
        adapter: true,
      },
      engine: "js",
      schema: path.join("prisma", "schema.prisma"),
      async adapter() {
        return new PrismaD1({
          CLOUDFLARE_D1_TOKEN: process.env.CLOUDFLARE_D1_TOKEN,
          CLOUDFLARE_ACCOUNT_ID: process.env.CLOUDFLARE_ACCOUNT_ID,
          CLOUDFLARE_DATABASE_ID: process.env.CLOUDFLARE_DATABASE_ID,
        });
      },
    } satisfies PrismaConfig;
```

[Prisma ORM v6.11.0](https://github.com/prisma/prisma/releases/tag/6.11.0)부터 D1 어댑터 이름이 `PrismaD1HTTP`에서 `PrismaD1`으로 변경되었습니다.

- `engine` (Removed)

Prisma ORM v7에서 제거됨

`engine` 속성은 Prisma ORM v7에서 제거되었습니다.

Prisma ORM v6.19 이하

프로젝트에서 사용할 스키마 엔진을 구성합니다.

| Property | Type              | Required | Default   |
| -------- | ----------------- | -------- | --------- |
| `engine` | `classic` or `js` | No       | `classic` |

기본값은 classic 엔진이며, 이 경우 `prisma.config.ts`에 `datasource`가 설정되어 있어야 합니다.

```
    import "dotenv/config";
    import path from "node:path";
    import { defineConfig, env } from "prisma/config";
    export default defineConfig({
      engine: "classic",
      datasource: {
        url: env("DATABASE_URL"),
      },
      schema: path.join("prisma", "schema.prisma"),
    });
```

- `studio` (Removed)

Prisma ORM v7에서 제거됨

`studio` 속성은 Prisma ORM v7에서 제거되었습니다. Prisma Studio를 실행하려면 다음을 사용하세요:

npm

pnpm

yarn

bun

```
    npx prisma studio --config ./prisma.config.ts
```

Prisma Studio는 이제 `datasource` 속성의 연결 구성을 자동으로 사용합니다. 자세한 내용은 [Prisma Studio 문서](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#studio)를 참고하세요.

Prisma ORM v6.19 이하

Prisma Studio가 데이터베이스에 연결하는 방식을 구성합니다. 자세한 내용은 아래 하위 옵션을 참고하세요.

| Property | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `studio` | `object` | No       | none    |

#

- `studio.adapter` (Removed)

Prisma 드라이버 어댑터 인스턴스를 반환하는 함수입니다. 이 함수는 환경 변수를 포함하는 `env` 파라미터를 받고, 유효한 Prisma 드라이버 어댑터로 resolve되는 `Promise`를 반환해야 합니다.

| Property          | Type                                                           | Required | Default |
| ----------------- | -------------------------------------------------------------- | -------- | ------- |
| `studio.adapter ` | `(env: Env) => Promise<SqlMigrationAwareDriverAdapterFactory>` | No       | none    |

Prisma ORM LibSQL 드라이버 어댑터를 사용하는 예시:

```
    import type { PrismaConfig } from "prisma";

    export default {
      experimental: {
        studio: true,
      },
      engine: "js",
      studio: {
        adapter: async (env: Env) => {
          const { PrismaLibSQL } = await import("@prisma/adapter-libsql");
          const { createClient } = await import("@libsql/client");

          const libsql = createClient({
            url: env.DOTENV_PRISMA_STUDIO_LIBSQL_DATABASE_URL,
          });
          return new PrismaLibSQL(libsql);
        },
      },
    } satisfies PrismaConfig;
```

## 일반적인 패턴

- Setting up your project

Prisma Config를 시작하려면 프로젝트 루트에 `prisma.config.ts` 파일을 생성하세요. 다음 두 가지 접근 방식 중 하나를 사용할 수 있습니다.

`defineConfig` 사용:

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

TypeScript 타입 사용:

```
    import "dotenv/config";
    import type { PrismaConfig } from "prisma";
    import { env } from "prisma/config";

    export default {
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DATABASE_URL"),
      },
    } satisfies PrismaConfig;
```

- Using environment variables

`.env` 파일의 환경 변수는 명시적으로 로드해야 합니다. `prisma init` 명령은 기본적으로 `import 'dotenv/config'`를 포함한 config를 생성합니다.

#

- Using dotenv (Recommended for Prisma ORM v7)
  1. `dotenv` 패키지를 설치합니다:

npm

pnpm

yarn

bun

```
    npm install dotenv
```

2. `prisma.config.ts` 파일 상단에 `dotenv/config`를 import합니다:

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

#

- Using Node.js v20+ or tsx with --env-file flag

Node.js v20+ 또는 `tsx`를 사용하는 경우, 환경 변수를 자동으로 로드하도록 `--env-file` 플래그를 전달할 수 있습니다:

```
    tsx --env-title=".env" src/index.ts
    tsx watch --env-title=".env" --env-title=".local.env" src/index.ts
    tsx --env-title=".env" ./prisma/seed.ts
```

#

- Using Bun

Bun에서는 추가 구성 없이 `.env` 파일이 자동으로 로드됩니다. `prisma init`이 생성하는 `import 'dotenv/config'` 줄은 Bun 사용 시 필요하지 않으며, `prisma.config.ts` 파일에서 안전하게 제거할 수 있습니다.

Bun으로 Prisma CLI 명령을 실행할 때는 Prisma가 Node.js로 폴백하지 않고 Bun 런타임을 사용하도록 `--bun` 플래그(예: `bunx --bun prisma init`)를 사용하세요.

#

- Type-safe environment variables

환경 변수에 타입 안전하게 접근하려면 `env()` 헬퍼 함수를 사용하세요:

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    type Env = {
      DATABASE_URL: string;
    };

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env<Env>("DATABASE_URL"),
      },
    });
```

#

- Handling optional environment variables

`prisma/config`의 `env()` 헬퍼 함수는 지정한 환경 변수가 정의되어 있지 않으면 **오류를 발생시킵니다**. 이는 다음 이유로 중요합니다:

- 모든 Prisma CLI 명령은 `prisma.config.ts` 파일을 로드합니다

- 실제로 `datasource.url` 값이 필요한 명령은 **일부**뿐입니다(예: `prisma db *`, `prisma migrate *`, `prisma generate --sql`)
  - `prisma generate` 같은 명령은 데이터베이스 URL이 필요하지 않지만, config 파일을 로드할 때 `env()`에서 오류가 발생하면 여전히 실패합니다

예를 들어, `DATABASE_URL`이 설정되지 않은 상태에서 `prisma generate`를 실행하고 config에서 `env('DATABASE_URL')`를 사용하면 다음이 표시됩니다:

```
    Error: PrismaConfigEnvError: Missing required environment variable: DATABASE_URL
```

**해결 방법:** 환경 변수가 항상 존재한다고 보장할 수 없다면(예: CI/CD 파이프라인에서 타입 체크용으로만 `prisma generate`를 실행하는 경우), `env()` 헬퍼를 사용하지 마세요. 대신 환경 변수에 직접 접근하세요:

```
    import "dotenv/config";
    import { defineConfig } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: process.env.DATABASE_URL!, // Or use: process.env.DATABASE_URL ?? '' to provide a fallback value
      },
    });
```

환경 변수의 존재를 **강제**하고 싶을 때는 `env()` 헬퍼를 사용하세요. 실행하는 명령에 따라 변수가 선택 사항일 수 있다면 `process.env`를 직접 사용하세요.

- 멀티 파일 스키마 사용하기

Prisma 스키마를 여러 파일로 분리하려면 `schema` 속성을 통해 Prisma 스키마 폴더 경로를 지정해야 합니다:

```
    import path from "node:path";
    import type { PrismaConfig } from "prisma";

    export default {
      schema: path.join("prisma", "schema"),
    } satisfies PrismaConfig;
```

이 경우 `migrations` 디렉터리는 `datasource` 블록을 정의한 `.prisma` 파일 옆에 위치해야 합니다.

예를 들어 `schema.prisma`가 `datasource`를 정의한다고 가정하면, migrations 폴더는 다음과 같이 배치해야 합니다:

```
    # `migrations` and `schema.prisma` are on the same level
    .
    ├── migrations
    ├── models
    │   ├── posts.prisma
    │   └── users.prisma
    └── schema.prisma
```

## 경로 해석

`prisma validate` 또는 `prisma migrate` 같은 Prisma CLI 명령은 `prisma.config.ts`(또는 `.config/prisma.ts`)를 사용해 Prisma 스키마 및 기타 리소스의 위치를 찾습니다.

**핵심 규칙:**

- config 파일에 정의된 경로(예: `schema`, `migrations`)는 CLI 명령을 실행한 위치가 아니라, 항상 **config 파일 위치를 기준으로** 해석됩니다.
- CLI는 먼저 **config 파일 자체를 찾아야** 하며, 이는 Prisma 설치 방식과 사용 중인 패키지 매니저에 따라 달라집니다.

* `pnpm prisma`에서의 동작

Prisma가 로컬에 설치되어 있고 `pnpm prisma`로 실행하는 경우, 프로젝트 루트에서 실행하든 하위 디렉터리에서 실행하든 config 파일이 자동으로 감지됩니다.

예시 프로젝트 트리:

```
    .
    ├── node_modules
    ├── package.json
    ├── prisma-custom
    │   └── schema.prisma
    ├── prisma.config.ts
    └── src
```

프로젝트 루트에서 실행한 예시:

```
    pnpm prisma validate
    # → Loaded Prisma config from ./prisma.config.ts
    # → Prisma schema loaded from prisma-custom/schema.prisma
```

하위 디렉터리에서 실행한 예시:

```
    cd src
    pnpm prisma validate
    # → Still finds prisma.config.ts and resolves schema correctly
```

- `npx prisma` 또는 `bunx --bun prisma`에서의 동작

`npx prisma` 또는 `bunx --bun prisma`로 실행할 때는 명령을 **프로젝트 루트**(Prisma가 `package.json`에 선언된 위치)에서 실행한 경우에만 CLI가 config 파일을 감지합니다.

Bun을 사용할 때 Prisma가 Bun 런타임으로 실행되도록 하려면 `--bun` 플래그가 필요합니다. 이 플래그가 없으면 CLI의 `#!/usr/bin/env node` shebang 때문에 Prisma는 Node.js로 폴백합니다.

프로젝트 루트에서 실행한 예시:

npm

pnpm

yarn

bun

```
    npx prisma validate
    # → Works as expected
```

하위 디렉터리에서 실행(실패):

npm

pnpm

yarn

bun

```
    cd src
    npx prisma validate
    # → Error: Could not find Prisma Schema...
```

이 문제를 해결하려면 `--config` 플래그를 사용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma validate --config ../prisma.config.ts
```

- 전역 Prisma 설치

Prisma를 전역 설치한 경우(`npm i -g prisma`), 기본적으로 `prisma.config.ts` 또는 `prisma/config` 모듈을 찾지 못할 수 있습니다. 문제를 피하려면:

- 프로젝트에서 로컬 Prisma 설치를 권장합니다.
- 또는 `prisma/config`를 로컬에서 사용하고 `--config`를 전달해 config 파일 경로를 지정하세요.

* 모노레포
  - Prisma가 **워크스페이스 루트**에 설치되어 있으면, `pnpm prisma`는 하위 디렉터리에서도 config 파일을 감지합니다.
  - Prisma가 **서브패키지**(예: `./packages/db`)에 설치되어 있으면, 해당 패키지 디렉터리 또는 그 하위에서 명령을 실행하세요.

* 사용자 지정 config 위치

Prisma CLI 명령 실행 시 config 파일의 사용자 지정 위치를 지정할 수 있습니다:

```
    prisma validate --config ./path/to/myconfig.ts
```

## 환경 변수 로딩

환경 변수를 로드하려면 `dotenv` 패키지를 설치하고 `prisma.config.ts` 파일 맨 위에 `import 'dotenv/config'`를 추가하세요.

Prisma 애플리케이션에서 환경 변수를 로드하려면 `prisma.config.ts` 파일과 `prisma/config`의 `env` 헬퍼를 함께 사용할 수 있습니다. 이 접근 방식은 더 나은 타입 안정성과 설정 관리를 제공합니다.

1. `dotenv` 패키지를 설치하세요:

npm

pnpm

yarn

bun

```
npm install dotenv
```

2. 프로젝트 루트에 `.env` 파일이 없으면 생성하고, 데이터베이스 연결 문자열을 추가하세요:

```
DATABASE_URL="your_database_connection_string_here"
```

3. `prisma.config.ts` 파일 상단에서 `dotenv/config`를 import하는지 확인하세요:

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
