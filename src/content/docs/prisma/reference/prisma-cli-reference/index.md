---
title: "Prisma CLI 참조"
description: "이 페이지는 사용 가능한 모든 Prisma CLI 명령의 개요를 제공하고, 각 옵션을 설명하며, 다양한 사용 예시를 보여줍니다."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/prisma-cli-reference

# Prisma CLI 참조

이 페이지는 사용 가능한 모든 Prisma CLI 명령의 개요를 제공하고, 각 옵션을 설명하며, 다양한 사용 예시를 보여줍니다.

이 문서는 Prisma CLI 명령, 인수, 옵션을 설명합니다.

## 명령

- `version` (`-v`)

`version` 명령은 현재 `prisma` 버전, 플랫폼, 엔진 바이너리에 대한 정보를 출력합니다.

#

- 옵션

`version` 명령은 동작을 변경하기 위해 다음 옵션을 인식합니다.

| Option   | Required | Description                           |
| -------- | -------- | ------------------------------------- |
| `--json` | No       | 버전 정보를 JSON 형식으로 출력합니다. |

#

- 예시

#

- 버전 정보 출력

```
    prisma version
```

```
    Environment variables loaded from .env
    prisma               : 2.21.0-dev.4
    @prisma/client       : 2.21.0-dev.4
    Current platform     : windows
    Query Engine         : query-engine 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\query-engine-windows.exe)
    Migration Engine     : migration-engine-cli 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\migration-engine-windows.exe)
    Format Binary        : prisma-fmt 60ba6551f29b17d7d6ce479e5733c70d9c00860e (at node_modules\@prisma\engines\prisma-fmt-windows.exe)
    Default Engines Hash : 60ba6551f29b17d7d6ce479e5733c70d9c00860e
    Studio               : 0.365.0
```

#

- 버전 정보 출력 (`-v`)

```
    prisma -v
```

```
    Environment variables loaded from .env
    prisma               : 2.21.0-dev.4
    @prisma/client       : 2.21.0-dev.4
    Current platform     : windows
    Query Engine         : query-engine 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\query-engine-windows.exe)
    Migration Engine     : migration-engine-cli 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6 (at C:\Users\veroh\AppData\Roaming\npm\node_modules\@prisma\cli\migration-engine-windows.exe)
    Format Binary        : prisma-fmt 60ba6551f29b17d7d6ce479e5733c70d9c00860e (at node_modules\@prisma\engines\prisma-fmt-windows.exe)
    Default Engines Hash : 60ba6551f29b17d7d6ce479e5733c70d9c00860e
    Studio               : 0.365.0
```

#

- 버전 정보를 JSON으로 출력

```
    prisma version --json
```

```
    Environment variables loaded from .env
    {
      "prisma": "2.21.0-dev.4",
      "@prisma/client": "2.21.0-dev.4",
      "current-platform": "windows",
      "query-engine": "query-engine 60ba6551f29b17d7d6ce479e5733c70d9c00860e (at node_modules\\@prisma\\engines\\query-engine-windows.exe)",
      "migration-engine": "migration-engine-cli 60ba6551f29b17d7d6ce479e5733c70d9c00860e (at node_modules\\@prisma\\engines\\migration-engine-windows.exe)",
      "format-binary": "prisma-fmt 60ba6551f29b17d7d6ce479e5733c70d9c00860e (at node_modules\\@prisma\\engines\\prisma-fmt-windows.exe)",
      "default-engines-hash": "60ba6551f29b17d7d6ce479e5733c70d9c00860e",
      "studio": "0.365.0"
    }
```

- `init`

현재 디렉터리 내에서 새 Prisma ORM 프로젝트를 부트스트랩합니다.

`init` 명령은 기존 파일을 해석하지 않습니다. 대신 현재 디렉터리에 최소 구성의 `schema.prisma` 파일이 포함된 `prisma` 디렉터리를 생성합니다.

기본적으로 프로젝트는 [local Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 인스턴스를 설정하지만, `--datasource-provider` 옵션으로 다른 데이터베이스를 선택할 수 있습니다.

#

- 인수

| Argument                 | Required | Description                                                                                                                                                                                                                            | Default               |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `--datasource-provider`  | No       | `datasource` 블록의 `provider` 필드 값을 지정합니다. 옵션은 `prisma+postgres`, `sqlite`, `postgresql`, `mysql`, `sqlserver`, `mongodb`, `cockroachdb`입니다.                                                                           | `postgresql`          |
| `--db`                   | No       | `--datasource-provider prisma+postgres`의 축약 문법입니다. 새 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 인스턴스를 생성합니다. [PDP Console](https://console.prisma.io) 인증이 필요합니다.                               |
| `--prompt` (or `--vibe`) | No       | 프롬프트를 기반으로 Prisma 스키마를 스캐폴딩하고 새 Prisma Postgres 인스턴스에 배포합니다. [PDP Console](https://console.prisma.io) 인증이 필요합니다.                                                                                 |
| `--url`                  | No       | 사용자 지정 `datasource` url을 정의합니다.                                                                                                                                                                                             |
| `--generator-provider`   | No       | 사용할 generator provider를 정의합니다.                                                                                                                                                                                                | `prisma-client`       |
| `--preview-feature`      | No       | 사용할 [Preview features](https://docs.prisma.io/docs/orm/reference/preview-features/cli-preview-features)를 정의합니다. 여러 Preview feature를 정의하려면 각 Preview feature마다 플래그를 여러 번 제공해야 합니다. 예시를 참고하세요. |
| `--output`               | No       | [생성된 클라이언트의 출력 위치](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider)를 지정합니다.                                                                                     | `../generated/prisma` |
| `--with-model`           | No       | 초기 Prisma 스키마에 간단한 `User` 모델을 추가합니다. `5.14.0` 버전부터 사용 가능합니다.                                                                                                                                               |

#

- 예시

**`prisma init` 실행**

```
    prisma init
```

```
    npx prisma init

    Initialized Prisma in your project

      prisma/
        schema.prisma
      prisma.config.ts

    Next, choose how you want to set up your database:

    CONNECT EXISTING DATABASE:
      1. Configure your DATABASE_URL in `prisma.config.ts`
      2. Run `npx prisma db pull` to introspect your database.

    CREATE NEW DATABASE:
      Local: npx prisma dev (runs Postgres locally in your terminal)
      Cloud: npx create-db (creates a free Prisma Postgres database)

      Then, define your models in `prisma/schema.prisma` and run `npx prisma migrate dev` to apply your schema.

    Learn more: https://pris.ly/getting-started
```

다음으로, 로컬 Prisma Postgres 인스턴스와 상호작용하려면(예: 마이그레이션 실행 또는 쿼리 실행) `prisma dev` 명령을 실행하세요.

**`prisma init --datasource-provider sqlite` 실행**

```
    prisma init --datasource-provider sqlite
```

명령 출력에는 생성된 파일 사용법과 프로젝트에서 Prisma ORM 사용을 시작하는 방법에 대한 유용한 정보가 포함됩니다.

**`prisma init --db` 실행**

```
    prisma init --db
```

```
    ✓ Select an authentication method Google
    Authenticating to Prisma Platform via browser.

    Visit the following URL in your browser to authenticate:
    https://console.prisma.io/auth/cli?state=eyJjb6ll...

    Successfully authenticated as amanyoyoyo@gmail.com.
    Let's set up your Prisma Postgres database!
    ✓ Select your region: ap-southeast-1 - Asia Pacific (Singapore)
    ✓ Enter a project name: My Prisma Project
    ✓ Success! Your Prisma Postgres database is ready ✅

    We found an existing schema.prisma file in your current project directory.

    --- Database URL ---

    Connect Prisma ORM to your Prisma Postgres database with this URL:

    --- Next steps ---

    Go to https://pris.ly/ppg-init for detailed instructions.

    1. Install the Postgres adapter
    npm install @prisma/adapter-pg

    ...and add it to your Prisma Client instance:

    import { PrismaClient } from "./generated/prisma/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    const connectionString = `${process.env.DATABASE_URL}`;

    const adapter = new PrismaPg({ connectionString });
    const prisma = new PrismaClient({ adapter });

    2. Apply migrations
    Run the following command to create and apply a migration:
    npx prisma migrate dev

    3. Manage your data
    View and edit your data locally by running this command:
    npx prisma studio

    ...or online in Console:
    https://console.prisma.io/cmhyn0uwl0q6903foel16ff31/cmhyn143t074tyLfoezs684ag/cmhyn143t074uylfon8hfre5z/studio

    4. Send queries from your app
    If you already have an existing app with Prisma ORM, you can now run it and it will send queries against your newly created Prisma Postgres instance.

    5. Learn more
    For more info, visit the Prisma Postgres docs: https://pris.ly/ppg-docs
```

이 명령은 새 [Prisma Postgres](https://www.prisma.io/postgres) 인스턴스를 생성합니다. [PDP Console](https://console.prisma.io)에 인증되어 있어야 한다는 점에 유의하세요. 인증되지 않은 상태에서 처음 실행하면 Console에 로그인할 수 있도록 브라우저가 열립니다.

**`prisma init --prompt "Simple habit tracker application"` 실행**

```
    prisma init --prompt "Simple habit tracker application"
```

이 명령은 Prisma 스키마를 스캐폴딩하고 새 [Prisma Postgres](https://www.prisma.io/postgres) 인스턴스에 배포합니다. [PDP Console](https://console.prisma.io)에 인증되어 있어야 한다는 점에 유의하세요. 인증되지 않은 상태에서 처음 실행하면 Console에 로그인할 수 있도록 브라우저가 열립니다.

**`prisma init --preview-feature` 실행**

```
    prisma init --preview-feature metrics
```

```
    datasource db {
      provider = "postgresql"
    }

    generator client {
      provider        = "prisma-client"
      previewFeatures = ["metrics"]
    }
```

```
    prisma init --preview-feature view --preview-feature metrics
```

```
    datasource db {
      provider = "postgresql"
    }

    generator client {
      provider        = "prisma-client"
      previewFeatures = ["views", "metrics"]
    }
```

#

- 생성된 자산

**`prisma/schema.prisma`**

스키마를 정의하기 위한 초기 `schema.prisma` 파일:

```
    // This is your Prisma schema file,
    // learn more about it in the docs: https://pris.ly/d/prisma-schema

    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "postgresql"
    }
```

**`prisma.config.ts`**

datasource URL 및 기타 설정을 정의하는 Prisma용 TypeScript 구성 파일:

```
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

자세한 내용은 [Prisma Config reference](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)를 참고하세요.

**`.env`**

프로젝트의 환경 변수를 정의하는 파일:

```
    # Environment variables declared in this file are automatically made available to Prisma.
    # See the documentation for more detail: https://pris.ly/d/prisma-schema#using-environment-variables

    # Prisma supports the native connection string format for PostgreSQL, MySQL, SQLite, SQL Server, MongoDB and CockroachDB.
    # See the documentation for all the connection string options: https://pris.ly/d/connection-strings

    DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
```

**`.gitignore`**

프로젝트에서 git이 무시할 폴더/파일을 지정하는 파일입니다.

```
    node_modules
    # Keep environment variables out of version control
    .env

    /generated/prisma
```

**`prisma init --url mysql://user:password@localhost:3306/mydb` 실행**

`--url` 인수를 사용한 `init` 명령을 통해 Prisma 초기화 중 자리표시자 데이터베이스 URL에 의존하지 않고 사용자 지정 datasource URL을 지정할 수 있습니다.

```
    prisma init --url mysql://user:password@localhost:3306/mydb
```

#

- 생성된 자산

**`prisma/schema.prisma`**

스키마를 정의하기 위한 최소 구성의 `schema.prisma` 파일:

```
    // This is your Prisma schema file,
    // learn more about it in the docs: https://pris.ly/d/prisma-schema

    datasource db {
      provider = "mysql"
    }

    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }
```

**`prisma.config.ts`**

사용자 지정 URL이 포함된 Prisma용 TypeScript 구성 파일:

```
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

**`.env`**

프로젝트의 환경 변수를 정의하는 파일:

```
    # Environment variables declared in this file are automatically made available to Prisma.
    # See the documentation for more detail: https://pris.ly/d/prisma-schema#using-environment-variables

    # Prisma supports the native connection string format for PostgreSQL, MySQL, SQLite, SQL Server, MongoDB and CockroachDB.
    # See the documentation for all the connection string options: https://pris.ly/d/connection-strings

    DATABASE_URL="mysql://user:password@localhost:3306/mydb"
```

- `generate`

`generate` 명령은 `prisma/schema.prisma` 파일에 정의된 [`generator`](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators) 및 [`data model`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models) 블록을 기반으로 Prisma Client 같은 자산을 생성합니다.

`generate` 명령은 가장 자주 `prisma-client` generator와 함께 사용되어 Prisma Client를 생성합니다. 이때 다음이 수행됩니다.

1. 처리할 Prisma Schema를 찾기 위해 현재 디렉터리를 검사합니다.
2. generator 블록에 지정된 출력 디렉터리에 스키마 기반의 맞춤형 Prisma Client를 생성합니다.

#

- 사전 요구사항

`generate` 명령을 사용하려면 `schema.prisma` 파일에 generator 정의를 추가해야 합니다. Prisma Client를 생성하는 데 사용되는 `prisma-client` generator는 `schema.prisma` 파일에 다음을 포함하여 추가할 수 있습니다.

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }
```

#

- 옵션

| Option              | Required | Description                                                                                                                                                                                                                                          | Default |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `--data-proxy`      | No       | `generate` 명령은 Prisma 5.0.0 이전 버전에서 [Prisma Accelerate](https://docs.prisma.io/docs/accelerate)와 함께 사용할 Prisma Client를 생성합니다. `--accelerate` 및 `--no-engine`과 상호 배타적입니다.                                              |
| `--accelerate`      | No       | `generate` 명령은 [Prisma Accelerate](https://docs.prisma.io/docs/accelerate)와 함께 사용할 Prisma Client를 생성합니다. `--data-proxy` 및 `--no-engine`과 상호 배타적입니다. Prisma 5.1.0 이상에서 사용 가능합니다.                                  |
| `--no-engine`       | No       | `generate` 명령은 [Prisma Accelerate](https://docs.prisma.io/docs/accelerate)와 함께 사용하기 위해 엔진을 동반하지 않는 Prisma Client를 생성합니다. `--data-proxy` 및 `--accelerate`와 상호 배타적입니다. Prisma ORM 5.2.0 이상에서 사용 가능합니다. |
| `--no-hints`        | No       | `generate` 명령은 사용 힌트, 설문, 정보 배너를 터미널에 출력하지 않는 Prisma Client를 생성합니다. Prisma ORM 5.16.0 이상에서 사용 가능합니다.                                                                                                        |
| `--allow-no-models` | No       | `generate` 명령은 어떤 모델도 생성하지 않고 Prisma Client를 생성합니다.                                                                                                                                                                              |
| `--watch`           | No       | `generate` 명령은 `schema.prisma` 파일을 계속 감시하고 파일 변경 시 Prisma Client를 다시 생성합니다.                                                                                                                                                 |

**사용 중단 경고**

Prisma 5.2.0부터 `--data-proxy`와 `--accelerate`는 `--no-engine`으로 대체되어 사용 중단(deprecated)되었습니다. Prisma Client는 더 이상 Prisma Accelerate와 함께 동작하기 위해 별도 옵션이 필요하지 않습니다. 모든 옵션은 계속 사용 가능하고 유사하게 동작하지만, 엔진 다운로드를 방지하여 serverless 및 edge functions에 배포되는 앱 크기에 큰 영향을 주므로 `--no-engine` 사용을 권장합니다.

#

- 인수

| Argument      | Required | Description                                                                                                                                                           | Default                                     |
| ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `--schema`    | No       | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다.                                                                | `./schema.prisma`, `./prisma/schema.prisma` |
| `--generator` | No       | 자산 생성에 사용할 generator를 지정합니다. 이 옵션은 여러 generator를 포함하기 위해 여러 번 제공할 수 있습니다. 기본적으로 대상 스키마의 모든 generator가 실행됩니다. |                                             |

#

- 예시

#

- 기본 `schema.prisma` 경로를 사용하여 Prisma Client 생성

```
    prisma generate
```

```
    ✔ Generated Prisma Client to ./node_modules/.prisma/client in 61ms

    You can now start using Prisma Client in your code:

    import { PrismaClient } from '../prisma/generated/client'
    // or const { PrismaClient } = require('@prisma/client')

    const prisma = new PrismaClient()

    Explore the full API: https://pris.ly/d/client
```

#

- 기본이 아닌 `schema.prisma` 경로를 사용하여 Prisma Client 생성

```
    prisma generate --schema=./alternative/schema.prisma
```

#

- `schema.prisma` 파일 변경을 계속 감시하여 Prisma Client를 자동으로 다시 생성

```
    prisma generate --watch
```

```
    Watching... /home/prismauser/prisma/prisma-play/prisma/schema.prisma

    ✔ Generated Prisma Client to ./node_modules/.prisma/client in 45ms
```

#

- 특정 generator만 사용하여 `generate` 명령 실행

```
    prisma generate --generator client
```

#

- 여러 특정 generator를 사용하여 `generate` 명령 실행

```
    prisma generate --generator client --generator zod_schemas
```

#

- 생성된 자산

`prisma-client` generator는 `output` 필드로 지정한 사용자 지정 출력 디렉터리에서 데이터베이스 작업을 위한 맞춤형 클라이언트를 생성합니다. [출력 폴더를 사용자 지정](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider)할 수 있습니다.

- `validate`

Prisma 스키마 파일의 [Prisma Schema Language](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 검증합니다.

#

- 인수

| Argument   | Required | Description                                                                                            | Default                                     |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| `--schema` | No       | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma`, `./prisma/schema.prisma` |

#

- 예시

#

- 오류 없이 스키마 검증하기

```
    prisma validate
```

```
    Environment variables loaded from .env
    Prisma schema loaded from prisma/schema.prisma
    The schema at /absolute/path/prisma/schema.prisma is valid 🚀
```

#

- 검증 오류가 있는 스키마 검증하기

```
    prisma validate
```

```
    Environment variables loaded from .env
    Prisma schema loaded from prisma/schema.prisma
    Error: Schema validation error - Error (query-engine-node-api library)
    Error code: P1012
    error: The preview feature "unknownFeatureFlag" is not known. Expected one of: [...]
      */}  schema.prisma:3
       |
     2 |     provider        = "prisma-client"
     3 |     previewFeatures = ["unknownFeatureFlag"]
       |

    Validation Error Count: 1
    [Context: getDmmf]

    Prisma CLI Version : 4.5.0
```

- `format`

Prisma 스키마 파일의 형식을 지정합니다. 여기에는 스키마 검증, 포맷팅, 저장이 포함됩니다.

#

- 인수

| Argument   | Required | Description                                                                                                            | Default                                     |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `--schema` | 아니요   | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다.                 | `./schema.prisma`, `./prisma/schema.prisma` |
| `--check`  | 아니요   | 포맷되지 않은 파일이 하나라도 있으면 실패합니다. CI에서 스키마가 올바르게 포맷되었는지 감지하는 데 사용할 수 있습니다. |

#

- 예제

#

- 오류 없이 스키마 검증하기

```
    prisma format
```

```
    Environment variables loaded from .env
    Prisma schema loaded from prisma/schema.prisma
    Formatted prisma/schema.prisma in 116ms �
```

#

- 검증 오류가 있는 스키마 포맷팅

```
    prisma format
```

```
    Environment variables loaded from .env
    Prisma schema loaded from prisma/schema.prisma
    Error: Schema validation error - Error (query-engine-node-api library)
    Error code: P1012
    error: The preview feature "unknownFeatureFlag" is not known. Expected one of: [...]
      */}  schema.prisma:3
       |
     2 |     provider        = "prisma-client"
     3 |     previewFeatures = ["unknownFeatureFlag"]
       |

    Validation Error Count: 1
    [Context: getDmmf]

    Prisma CLI Version : 4.5.0
```

- `debug`

디버깅 및 버그 리포트를 위한 정보를 출력합니다.

이 기능은 버전 5.6.0 이상에서 사용할 수 있습니다.

#

- 인수

| Argument         | Required | Description                                                                                            | Default                                     |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| `--schema`       | 아니요   | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma`, `./prisma/schema.prisma` |
| `--help` / `--h` | 아니요   | 도움말 메시지를 표시합니다.                                                                            |

#

- 예제

```
    prisma debug
```

```
    -- Prisma schema --
    Path: /prisma/schema.prisma

    -- Local cache directory for engines files --
    Path: /.cache/prisma

    -- Environment variables --
    When not set, the line is dimmed and no value is displayed.
    When set, the line is bold and the value is inside the `` backticks.

    For general debugging
     - CI:
     - DEBUG:
     - NODE_ENV:
     - RUST_LOG:
     - RUST_BACKTRACE:
     - NO_COLOR:
     - TERM: `xterm-256color`
     - NODE_TLS_REJECT_UNAUTHORIZED:
     - NO_PROXY:
     - http_proxy:
     - HTTP_PROXY:
     - https_proxy:
     - HTTPS_PROXY:

    For more information see our [environment variable documentation](/orm/reference/environment-variables-reference)

    For hiding messages
     - PRISMA_DISABLE_WARNINGS:
     - PRISMA_HIDE_PREVIEW_FLAG_WARNINGS:
     - PRISMA_HIDE_UPDATE_MESSAGE:

    For downloading engines
     - PRISMA_ENGINES_MIRROR:
     - PRISMA_BINARIES_MIRROR (deprecated):
     - PRISMA_ENGINES_CHECKSUM_IGNORE_MISSING:
     - BINARY_DOWNLOAD_VERSION:

    For configuring the Query Engine Type
     - PRISMA_CLI_QUERY_ENGINE_TYPE: (Not supported in Prisma ORM v7)
     - PRISMA_CLIENT_ENGINE_TYPE: (Not supported in Prisma ORM v7)

    For custom engines
     - PRISMA_QUERY_ENGINE_BINARY: (Not supported in Prisma ORM v7)
     - PRISMA_QUERY_ENGINE_LIBRARY: (Not supported in Prisma ORM v7)
     - PRISMA_SCHEMA_ENGINE_BINARY:
     - PRISMA_MIGRATION_ENGINE_BINARY:

    For the "postinstall" npm hook
     - PRISMA_GENERATE_SKIP_AUTOINSTALL: (Not supported in Prisma ORM v7)
     - PRISMA_SKIP_POSTINSTALL_GENERATE: (Not supported in Prisma ORM v7)
     - PRISMA_GENERATE_IN_POSTINSTALL: (Not supported in Prisma ORM v7)

    For "prisma generate"
     - PRISMA_GENERATE_DATAPROXY: (Not supported in Prisma ORM v7)
     - PRISMA_GENERATE_NO_ENGINE: (Not supported in Prisma ORM v7)

    For Prisma Client
     - PRISMA_SHOW_ALL_TRACES:
     - PRISMA_CLIENT_NO_RETRY (Binary engine only): (Not supported in Prisma ORM v7)

    For Prisma Migrate
     - PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK:
     - PRISMA_MIGRATE_SKIP_GENERATE: (Not supported in Prisma ORM v7)
     - PRISMA_MIGRATE_SKIP_SEED: (Not supported in Prisma ORM v7)

    For Prisma Studio
     - BROWSER:

    -- Terminal is interactive? --
    true

    -- CI detected? --
    false
```

이전 버전의 Prisma를 사용 중이라면, 다음을 실행하여 이 명령을 사용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma@latest debug
```

## `dev`

`dev` 명령은 Prisma ORM 명령을 실행할 수 있는 [로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 데이터베이스를 시작합니다. 개발 및 테스트 목적에 유용하며, 프로덕션에서 [Prisma Postgres](https://docs.prisma.io/docs/postgres)로 쉽게 전환할 수도 있습니다.

- 인수

| Argument              | Required | Description                                                                                                                                                                               | Default   |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `--name` (or `-n`)    | 아니요   | 특정 데이터베이스 인스턴스를 대상으로 지정할 수 있습니다. [자세히 보기](https://docs.prisma.io/docs/postgres/database/local-development#using-different-local-prisma-postgres-instances). | `default` |
| `--port` (or `-p`)    | 아니요   | 로컬 Prisma Postgres HTTP 서버가 수신할 메인 포트 번호입니다.                                                                                                                             | `51213`   |
| `--db-port` (or `-P`) | 아니요   | 로컬 Prisma Postgres 데이터베이스 서버가 수신할 포트 번호입니다.                                                                                                                          | `51214`   |
| `--shadow-db-port`    | 아니요   | 섀도 데이터베이스 서버가 수신할 포트 번호입니다.                                                                                                                                          | `51215`   |
| `--detach` (or `-d`)  | 아니요   | 서버를 백그라운드에서 실행합니다.                                                                                                                                                         | `false`   |
| `--debug`             | 아니요   | 디버그 로깅을 활성화합니다.                                                                                                                                                               | `false`   |

- 예제

**`prisma dev` 실행**

```
    prisma dev
```

```
    $ npx prisma dev
    Fetching latest updates for this subcommand...
    ✔  Great Success! 😉👍

       Your  prisma dev  server default is ready and listening on ports 63567-63569.

    ╭──────────────────────────────╮
    │[q]uit  [h]ttp url  [t]cp urls│
    ╰──────────────────────────────╯
```

**특정 이름으로 `prisma dev` 실행**

npm

pnpm

yarn

bun

```
    npx prisma dev --name="mydbname"
```

이렇게 하면 나중에 인스턴스 관리 명령으로 시작, 중지, 관리할 수 있는 `mydbname`이라는 이름의 인스턴스가 생성됩니다.

**분리 모드로 `prisma dev` 실행**

npm

pnpm

yarn

bun

```
    npx prisma dev --detach
```

서버를 백그라운드에서 실행하므로 터미널을 다른 명령에 사용할 수 있습니다. 실행 중인 서버를 보려면 `prisma dev ls`를, 중지하려면 `prisma dev stop`을 사용하세요.

- `dev start`

기존 [로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 인스턴스를 백그라운드에서 시작합니다.

이 명령은 이미 존재하는 인스턴스에서만 동작합니다.

npm

pnpm

yarn

bun

```
    npx prisma dev start <glob>
```

`<glob>`는 시작할 로컬 Prisma Postgres 인스턴스를 지정하는 glob 패턴 자리표시자입니다. 예:

npm

pnpm

yarn

bun

```
    npx prisma dev start mydb # starts a DB called `mydb` in the background (only if it already exists)
```

`mydb`로 시작하는 모든 데이터베이스(예: `mydb-dev`, `mydb-prod`)를 시작하려면 glob를 사용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma dev start mydb* # starts all existing DBs starting with `mydb`
```

이를 통해 VS Code 확장 외부에서도 백그라운드 인스턴스 관리를 할 수 있습니다.

- `dev ls`

사용 가능한 모든 [로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 인스턴스를 나열합니다:

npm

pnpm

yarn

bun

```
    npx prisma dev ls
```

이 명령은 시스템의 모든 인스턴스와 현재 상태 및 구성을 보여줍니다.

- `dev stop`

하나 이상의 [로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 데이터베이스를 중지합니다:

npm

pnpm

yarn

bun

```
    npx prisma dev stop <glob>
```

`<glob>`는 중지할 로컬 Prisma Postgres 인스턴스를 지정하는 glob 패턴 자리표시자입니다. 예:

npm

pnpm

yarn

bun

```
    npx prisma dev stop mydb # stops a DB called `mydb`
```

`mydb`로 시작하는 모든 데이터베이스(예: `mydb-dev`, `mydb-prod`)를 중지하려면 glob를 사용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma dev stop mydb* # stops all DBs starting with `mydb`
```

`stop` 명령은 대화형이며, 실수로 작업하는 것을 방지하기 위한 안전 확인 프롬프트를 포함합니다.

- `dev rm`

파일 시스템에서 하나 이상의 [로컬 Prisma Postgres](https://docs.prisma.io/docs/postgres/database/local-development) 데이터베이스 데이터를 제거합니다:

npm

pnpm

yarn

bun

```
    npx prisma dev rm <glob>
```

`<glob>`는 제거할 로컬 Prisma Postgres 인스턴스를 지정하는 glob 패턴 자리표시자입니다. 예:

npm

pnpm

yarn

bun

```
    npx prisma dev rm mydb # removes a DB called `mydb`
```

`mydb`로 시작하는 모든 데이터베이스(예: `mydb-dev`, `mydb-prod`)를 제거하려면 glob를 사용할 수 있습니다:

npm

pnpm

yarn

bun

```
    npx prisma dev rm mydb* # removes all DBs starting with `mydb`
```

#

- 인수

| Argument  | Required | Description                                                                                                    | Default |
| --------- | -------- | -------------------------------------------------------------------------------------------------------------- | ------- |
| `--force` | 아니요   | 제거 전에 실행 중인 서버를 모두 중지합니다. 이 플래그가 없으면 서버가 하나라도 실행 중일 때 명령이 실패합니다. | `false` |

`rm` 명령은 대화형이며, 실수로 데이터를 잃는 것을 방지하기 위한 안전 확인 프롬프트를 포함합니다.

## `db`

- `db pull`

`db pull` 명령은 데이터베이스에 연결하여 현재 데이터베이스 스키마를 반영하는 Prisma 모델을 Prisma 스키마에 추가합니다.

**경고** : 이 명령은 현재 `schema.prisma` 파일을 새 스키마로 덮어씁니다. 일부 수동 변경이나 커스터마이징이 손실될 수 있습니다. `schema.prisma`에 중요한 수정 사항이 포함되어 있다면 `db pull` 실행 전에 현재 `schema.prisma` 파일을 반드시 백업하세요(또는 변경 사항을 되돌릴 수 있도록 현재 상태를 버전 관리에 커밋하세요).

[MongoDB connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 `db pull` 명령으로 수행하는 인트로스펙션은 스키마를 읽는 대신 데이터를 샘플링합니다.

#

- 사전 요구 사항

`db pull` 명령을 사용하기 전에 `prisma.config.ts` 파일에서 데이터베이스 연결을 구성해야 합니다.

예를 들어:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "sqlite"
    }
```

prisma.config.ts

```
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

#

- 옵션

| Option    | Required | Description                                                                                                        | Default |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------ | ------- |
| `--force` | 아니요   | 스키마에 수동으로 적용된 변경 사항을 강제로 덮어씁니다. 생성되는 스키마는 인트로스펙션된 스키마만 기반으로 합니다. |
| `--print` | 아니요   | 생성된 `schema.prisma`를 파일 시스템에 쓰는 대신 화면에 출력합니다.                                                |

#

- 인수

| Argument   | Required | Description                                                                                            | Default                                     |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| `--schema` | 아니요   | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma`, `./prisma/schema.prisma` |

#

- 예제

#

- 데이터베이스를 분석하고 해당 스키마를 `schema.prisma` 파일에 작성

```
    prisma db pull
```

```
    Introspecting based on datasource defined in schema.prisma …

    ✔ Introspected 2 models and wrote them into schema.prisma in 38ms

    Run prisma generate to generate Prisma Client.
```

#

- 읽고 쓸 대체 `schema.prisma` 파일 지정

```
    prisma db pull --schema=./alternative/schema.prisma
```

```
    Introspecting based on datasource defined in alternative/schema.prisma …

    ✔ Introspected 2 models and wrote them into alternative/schema.prisma in 60ms

    Run prisma generate to generate Prisma Client.
```

#

- 파일 시스템에 쓰는 대신 생성된 `schema.prisma` 파일 표시

```
    prisma db pull --print
```

```
    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    datasource db {
      provider = "sqlite"
      url      = "file:./hello-prisma.db"
    }

    model User {
      email   String    @unique
      name    String?
      user_id Int       @id @default(autoincrement())
      post    Post[]
      profile Profile[]
    }

    model Post {
      content   String?
      post_id   Int     @id @default(autoincrement())
      title     String
      author    User?   @relation(fields: [author_id], references: [user_id])
      author_id Int?
    }

    model Profile {
      bio        String?
      profile_id Int     @id @default(autoincrement())
      user       User    @relation(fields: [user_id], references: [user_id])
      user_id    Int     @unique
    }
```

- `db push`

`db push` 명령은 마이그레이션을 사용하지 않고 Prisma 스키마의 상태를 데이터베이스에 반영합니다. 데이터베이스가 존재하지 않으면 생성합니다.

이 명령은 프로토타이핑 및 로컬 개발처럼 스키마 변경을 버전 관리할 필요가 없을 때 좋은 선택입니다.

참고:

- `db push`의 개념적 개요와 Prisma Migrate 대신 사용해야 하는 경우
- `db push`를 사용한 스키마 프로토타이핑

#

- 사전 요구 사항

`db push` 명령을 사용하기 전에 `prisma.config.ts` 파일에서 데이터베이스 연결을 구성해야 합니다.

예를 들어:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "sqlite"
    }
```

prisma.config.ts

```
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

#

- 옵션

| Options              | Required | Description                                                                                                                       |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `--force-reset`      | 아니요   | 데이터베이스를 재설정한 다음 스키마를 업데이트합니다. 실행할 수 없는 마이그레이션 때문에 처음부터 다시 시작해야 할 때 유용합니다. |
| `--accept-data-loss` | 아니요   | 데이터 손실 경고를 무시합니다. 스키마 변경 결과로 데이터가 손실될 수 있는 경우 이 옵션이 필요합니다.                              |
| `--help` / `--h`     | 아니요   | 도움말 메시지를 표시합니다.                                                                                                       |

`--skip-generate` 플래그는 Prisma v7에서 제거되었습니다. `db push`는 더 이상 자동으로 `prisma generate`를 실행하지 않습니다. 필요하면 명시적으로 실행하세요.

#

- 인수

| Argument   | Required | Description                                                                                          | Default           |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------- | ----------------- |
| `--schema` | 아니요   | 기본 경로 대신 처리할 schema.prisma 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- 예제

스키마 푸시:

```
    prisma db push
```

데이터 손실을 허용하며 스키마 푸시:

```
    prisma db push --accept-data-loss
```

커스텀 스키마 위치로 스키마 푸시:

```
    prisma db push --schema=/tmp/schema.prisma
```

- `db seed`

`db seed`는 3.0.1에서 Preview에서 Generally Available (GA)로 변경되었습니다.

[데이터베이스 시드](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding)도 참고하세요.

#

- 옵션

| 옵션             | 필수   | 설명                                                        |
| ---------------- | ------ | ----------------------------------------------------------- |
| `--help` / `--h` | 아니요 | 도움말 메시지를 표시합니다                                  |
| `--`             | 아니요 | 시드 파일에 정의된 사용자 지정 인자를 사용할 수 있게 합니다 |

`--` 인자/ [구분자](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02)/ 더블 대시는 버전 4.15.0 이상에서 사용할 수 있습니다.

#

- 예제

```
    prisma db seed
```

- `db execute`

`db execute` 명령은 버전 3.13.0 이상에서 Generally Available입니다. 3.9.0~3.13.0 버전을 사용하는 경우 `--preview-feature` CLI 플래그 뒤에서 사용할 수 있습니다.

이 명령은 현재 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다.

이 명령은 Prisma 마이그레이션 테이블과 상호작용하지 않고 SQL 스크립트를 데이터베이스에 적용합니다. datasource URL 구성은 Prisma 설정 파일(예: `prisma.config.ts`)에서 읽습니다.

명령 출력은 커넥터별로 다르며, 데이터 반환용이 아니라 성공 또는 실패를 보고하기 위한 용도입니다.

추가 참고:

- 프로덕션에서의 마이그레이션 문제 해결

#

- 사전 준비

`db execute` 명령을 사용하기 전에 `prisma.config.ts` 파일에 데이터베이스 연결을 구성해야 합니다.

예를 들면:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "sqlite"
    }
```

`prisma.config.ts` 파일은 다음과 같이 보여야 합니다:

prisma.config.ts

```
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

#

- 옵션

| 옵션       | 필수   | 설명                                                      |
| ---------- | ------ | --------------------------------------------------------- |
| `--file`   | 예\*   | 파일 경로입니다. 해당 내용이 실행할 스크립트로 전송됩니다 |
| `--stdin`  | 아니요 | 터미널 표준 입력을 실행할 스크립트로 사용합니다           |
| `--config` | 아니요 | Prisma 설정 파일의 사용자 지정 경로                       |
| `--help`   | 아니요 | 도움말 메시지를 표시합니다                                |

- 스크립트 입력을 제공하려면 `--file` 또는 `--stdin` 중 하나가 필요합니다.

**Prisma v7 주요 변경 사항** : `--schema` 및 `--url` 옵션이 제거되었습니다. 대신 `prisma.config.ts`에서 데이터베이스 연결을 구성하세요.

#

- 예제
  - `prisma.config.ts`에 구성된 datasource를 사용해 SQL 스크립트 파일 내용을 실행:

```
prisma db execute --file ./script.sql
```

- 구성된 datasource를 사용해 stdin에서 SQL 스크립트 실행:

```
echo 'TRUNCATE TABLE dev;' | prisma db execute --stdin
```

## Prisma Migrate

Prisma Migrate는 2.19.0에서 Preview에서 Generally Available(GA)로 변경되었습니다.

**MongoDB에는 적용되지 않음**
`migrate dev` 및 관련 명령 대신 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에는 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다.

- `migrate dev`

**개발 환경에서만 사용, shadow database 필요**

`migrate dev` 명령은 다음을 수행합니다:

1. 스키마 드리프트(수정되거나 삭제된 마이그레이션 파일, 또는 데이터베이스 스키마에 대한 수동 변경)를 감지하기 위해 [shadow database](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)에서 기존 마이그레이션 이력을 다시 실행합니다
2. 대기 중인 마이그레이션을 shadow database에 적용합니다(예: 동료가 새로 만든 마이그레이션)
3. `migrate dev` 실행 전에 Prisma 스키마에 적용한 변경 사항으로부터 새 마이그레이션을 생성합니다
4. 적용되지 않은 모든 마이그레이션을 개발 데이터베이스에 적용하고 `_prisma_migrations` 테이블을 업데이트합니다

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다. 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.

**Prisma v7** : `migrate dev`는 더 이상 `prisma generate` 또는 시드 스크립트를 자동으로 실행하지 않습니다. 필요하면 `prisma generate`를 명시적으로 실행하세요.

추가 참고:

- Prisma Migrate 개념 개요
- Prisma Migrate로 개발하기

#

- 옵션

| 옵션            | 필수   | 설명                                                                                                                                                                         | 기본값 |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| `--create-only` | 아니요 | 새 마이그레이션을 생성하지만 적용하지는 않습니다. 스키마를 변경하지 않았더라도 동작하며(이 경우 빈 마이그레이션 생성), 마이그레이션을 적용하려면 `migrate dev`를 실행하세요. |
| `--name` / `-n` | 아니요 | 마이그레이션 이름을 지정합니다(예: `prisma migrate dev --name added_job_title`)                                                                                              |
| `--help` / `-h` | 아니요 | 도움말 메시지를 표시합니다                                                                                                                                                   |

`--skip-generate` 및 `--skip-seed` 플래그는 Prisma v7에서 제거되었습니다. `migrate dev`는 더 이상 `prisma generate` 또는 시드를 자동 실행하지 않습니다. 필요 시 명시적으로 실행하세요.

`--create-only`와 함께 `prisma migrate dev`를 실행하는 동안 [schema drift](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#detecting-schema-drift)가 감지되면 데이터베이스 재설정을 요청받습니다.

#

- 인자

| 인자       | 필수   | 설명                                                                                            | 기본값            |
| ---------- | ------ | ----------------------------------------------------------------------------------------------- | ----------------- |
| `--name`   | 아니요 | 마이그레이션 이름입니다. 이름을 제공하지 않으면 CLI가 입력을 요청합니다.                        |
| `--schema` | 아니요 | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대/상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- 예제

모든 마이그레이션을 적용한 다음, 새 마이그레이션이 있으면 생성하고 적용합니다:

```
    prisma migrate dev
```

모든 마이그레이션을 적용하고 스키마 변경이 있으면 새 마이그레이션을 생성하되 적용하지는 않습니다:

```
    prisma migrate dev --create-only
```

- `migrate reset`

**개발 환경에서만 사용**

이 명령은 다음을 수행합니다:

1. 가능하면 데이터베이스/스키마를 삭제하고, 환경상 데이터베이스/스키마 삭제가 허용되지 않으면 소프트 리셋을 수행합니다
2. 데이터베이스/스키마가 삭제된 경우 동일한 이름으로 새 데이터베이스/스키마를 생성합니다
3. 모든 마이그레이션을 적용합니다
4. 시드 스크립트를 실행합니다

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다. 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.

#

- 옵션

| 옵션              | 필수   | 설명                                              | 기본값 |
| ----------------- | ------ | ------------------------------------------------- | ------ |
| `--force`         | 아니요 | 확인 프롬프트를 건너뜁니다                        |
| `--skip-generate` | 아니요 | 제너레이터 트리거를 건너뜁니다(예: Prisma Client) |
| `--skip-seed`     | 아니요 | 시드 트리거를 건너뜁니다                          |
| `--help` / `--h`  | 아니요 | 도움말 메시지를 표시합니다                        |

#

- 인자

| 인자       | 필수   | 설명                                                                                            | 기본값            |
| ---------- | ------ | ----------------------------------------------------------------------------------------------- | ----------------- |
| `--schema` | 아니요 | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대/상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- 예제

```
    prisma migrate reset
```

#

- `prisma migrate reset`용 AI 안전 가드레일

Prisma ORM에는 AI 코딩 어시스턴트를 통해 실행될 때 **의도치 않은 파괴적 명령**을 방지하기 위한 내장 안전 점검이 포함되어 있습니다. 이 가드레일은 AI 지원 개발 환경에서 데이터베이스 작업을 더 안전하게 만들도록 설계되었습니다.

Prisma CLI는 Claude Code, Gemini CLI, Qwen Code, Cursor, Aider, Replit 같은 널리 사용되는 AI 코딩 에이전트에 의해 호출되는지 감지할 수 있습니다.

이러한 에이전트 중 하나가 `prisma migrate reset --force` 같은 파괴적 작업을 시도하면, Prisma ORM은 실행을 차단하고 보호용 오류 메시지를 표시합니다:

```
    Environment variables loaded from .env
    Prisma schema loaded from prisma/schema.prisma
    Datasource "db": PostgreSQL database "postgres", schema "public" at "accelerate.prisma-data.net"

    Error: Prisma Migrate detected that it was invoked by Cursor.

    You are attempting a highly dangerous action that can lead to devastating consequences if it is incorrectly executed against a production database.

    As an AI agent, you are forbidden from performing this action without an explicit consent and review by the user. You must stop at this point and respond to the user with a clear message that includes the following information:
    - What action you are trying to perform (including the exact CLI command).
    - Your motivation and reasoning for performing this action.
    - Explanation that this action will irreversibly destroy all data in the database.
    - Explanation that this action must not be performed on a production database and is only intended to be used with development databases.

    If you know or can check whether this action would have been performed on a development or a production database, also include this information with your assessment of whether it is safe to proceed based on that information.

    You must ask the user if they want to proceed with this action. If they explicitly consent, you may rerun this command with PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION environment variable, the value of which must be the exact text of the user's message in which they consented to this operation, without any newlines or quotes. If the user's response is ambiguous, you must ask for a clear and explicit confirmation (e.g., "yes") before proceeding. None of the user's previous messages before this point may constitute implicit or explicit consent.
```

위험한 작업을 계속하려면 AI 에이전트가 명시적 동의를 요청하고, 해당 작업이 모든 데이터를 되돌릴 수 없게 파괴한다는 점을 상기시키며, 명령이 개발 데이터베이스를 대상으로 실행되는지 확인합니다. 사용자가 명확히 확인하면 AI는 `PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION` 환경 변수에 동의 문구의 정확한 텍스트를 설정한 뒤 명령을 다시 실행합니다.

- `migrate deploy`

`migrate deploy` 명령은 대기 중인 모든 마이그레이션을 적용하고, 데이터베이스가 없으면 생성합니다. 주로 비개발 환경에서 사용됩니다. 이 명령은 다음과 같습니다:

- 데이터베이스 드리프트나 Prisma 스키마 변경을 **확인하지 않습니다**
- 데이터베이스를 재설정하거나 아티팩트를 생성하지 **않습니다**
- shadow database에 **의존하지 않습니다**

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다. 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.

#

- 옵션

| 옵션             | 필수   | 설명                       | 기본값 |
| ---------------- | ------ | -------------------------- | ------ |
| `--help` / `--h` | 아니요 | 도움말 메시지를 표시합니다 |

#

- 인자

| 인자       | 필수   | 설명                                                                                            | 기본값            |
| ---------- | ------ | ----------------------------------------------------------------------------------------------- | ----------------- |
| `--schema` | 아니요 | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대/상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- 예제

```
    prisma migrate deploy
```

- `migrate resolve`

`migrate resolve` 명령은 실패한 마이그레이션을 이미 적용됨(베이스라이닝 지원) 또는 롤백됨으로 표시하여 프로덕션에서 마이그레이션 이력 문제를 해결할 수 있게 합니다.

이 명령은 실패한 마이그레이션에만 사용할 수 있습니다. 성공한 마이그레이션에 사용하려 하면 오류가 발생합니다.

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다. 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.

#

- 옵션

| 옵션             | 필수   | 설명                       | 기본값 |
| ---------------- | ------ | -------------------------- | ------ |
| `--help` / `--h` | 아니요 | 도움말 메시지를 표시합니다 |

#

- 인자

| 인자            | 필수     | 설명                                                                                             | 기본값            |
| --------------- | -------- | ------------------------------------------------------------------------------------------------ | ----------------- |
| `--applied`     | 아니요\* | 특정 마이그레이션을 적용됨으로 기록합니다 - 예: `--applied "20201231000000_add_users_table"`     |
| `--rolled-back` | 아니요\* | 특정 마이그레이션을 롤백됨으로 기록합니다 - 예: `--rolled-back "20201231000000_add_users_table"` | `./schema.prisma` |

`./prisma/schema.prisma`
`--schema`| 아니요| 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대/상대 경로를 모두 지원합니다.| `./schema.prisma`
`./prisma/schema.prisma`

`--rolled-back` 또는 `--applied` 중 하나를 반드시 지정해야 합니다.

#

- 예제

```
    prisma migrate resolve --applied 20201231000000_add_users_table
```

```
    prisma migrate resolve --rolled-back 20201231000000_add_users_table
```

- `migrate status`

`prisma migrate status` 명령은 `./prisma/migrations/*` 폴더의 마이그레이션과 `_prisma_migrations` 테이블의 항목을 조회하여, 데이터베이스 내 마이그레이션 상태 정보를 종합합니다.

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 지원되지 않습니다. 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.

예시:

```
    Status
    3 migrations found in prisma/migrations

    Your local migration history and the migrations table from your database are different:

    The last common migration is: 20201127134938_new_migration

    The migration have not yet been applied:
    20201208100950_test_migration

    The migrations from the database are not found locally in prisma/migrations:
    20201208100950_new_migration
```

버전 4.3.0 이상에서는, 다음 경우 `prisma migrate status`가 exit code 1로 종료됩니다.

- 데이터베이스 연결 오류가 발생한 경우
- `migrations` 디렉터리에 데이터베이스에 아직 적용되지 않은 마이그레이션 파일이 있는 경우
- `migrations` 디렉터리의 마이그레이션 이력이 데이터베이스 상태와 불일치하게 분기된 경우
- 마이그레이션 테이블을 찾을 수 없는 경우
- 실패한 마이그레이션이 발견된 경우

#

- Options

| Option           | Required | Description                 | Default |
| ---------------- | -------- | --------------------------- | ------- |
| `--help` / `--h` | No       | 도움말 메시지를 표시합니다. |

#

- Arguments

| Argument   | Required | Description                                                                                            | Default           |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------ | ----------------- |
| `--schema` | No       | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- Examples

```
    prisma migrate status
```

- `migrate diff`

이 명령은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 부분적으로만 지원됩니다. 자세한 내용은 아래 명령 옵션을 참조하세요.

이 명령은 두 데이터베이스 스키마 소스를 비교하고, 첫 번째를 두 번째 상태로 바꾸기 위한 마이그레이션 설명을 출력합니다.

출력은 사람이 읽기 쉬운 요약(기본값) 또는 실행 가능한 스크립트로 제공할 수 있습니다.

`migrate diff` 명령은 [Prisma에서 지원되는](https://docs.prisma.io/docs/orm/reference/database-features) 데이터베이스 기능만 비교할 수 있습니다. 두 데이터베이스가 뷰나 트리거처럼 지원되지 않는 기능에서만 다르다면, `migrate diff`는 차이를 표시하지 않습니다.

명령 형식은 다음과 같습니다.

```
    prisma migrate diff --from-... <source1> --to-... <source2>
```

여기서 `--from-...` 및 `--to-...` 옵션은 데이터베이스 스키마 소스 유형에 따라 선택됩니다. 지원되는 소스 유형은 다음과 같습니다.

- 라이브 데이터베이스
- 마이그레이션 이력
- Prisma 스키마 데이터 모델
- 빈 스키마

두 스키마 소스는 동일한 데이터베이스 제공자를 사용해야 합니다. 예를 들어 PostgreSQL 데이터 소스와 SQLite 데이터 소스를 비교하는 diff는 지원되지 않습니다.

참고:

- Migration troubleshooting in production

#

- Prerequisites

`migrate diff` 명령을 사용하기 전에, `--from-config-datasource` 또는 `--to-config-datasource`를 사용하는 경우 `prisma.config.ts` 파일에서 데이터베이스 연결을 구성해야 합니다.

예시:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "sqlite"
    }
```

prisma.config.ts

```
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

#

- Options

**Prisma v7 breaking change** : `--from-url`, `--to-url`, `--from-schema-datasource`, `--to-schema-datasource`, `--shadow-database-url` 옵션이 제거되었습니다. 대신 `prisma.config.ts`에서 데이터베이스 URL을 읽는 `--from-config-datasource`와 `--to-config-datasource`를 사용하세요.

다음 `--from-...` 옵션 중 하나는 필수입니다.

| Options                    | Description                                                 | Notes                       |
| -------------------------- | ----------------------------------------------------------- | --------------------------- |
| `--from-empty`             | 마이그레이션 시작 데이터 모델이 비어 있다고 가정합니다.     |
| `--from-schema`            | Prisma 스키마 파일 경로로, diff에 데이터 모델을 사용합니다. |
| `--from-migrations`        | Prisma Migrate 마이그레이션 디렉터리 경로                   | MongoDB에서는 지원되지 않음 |
| `--from-config-datasource` | Prisma config 파일의 datasource를 사용합니다.               | Prisma v7+                  |

다음 `--to-...` 옵션 중 하나는 필수입니다.

| Options                  | Description                                                 | Notes                       |
| ------------------------ | ----------------------------------------------------------- | --------------------------- |
| `--to-empty`             | 마이그레이션 대상 데이터 모델이 비어 있다고 가정합니다.     |
| `--to-schema`            | Prisma 스키마 파일 경로로, diff에 데이터 모델을 사용합니다. |
| `--to-migrations`        | Prisma Migrate 마이그레이션 디렉터리 경로                   | MongoDB에서는 지원되지 않음 |
| `--to-config-datasource` | Prisma config 파일의 datasource를 사용합니다.               | Prisma v7+                  |

기타 옵션:

| Options          | Required | Description                                                                                                                                | Notes                                                                        |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `--script`       | No       | 기본 사람이 읽기 쉬운 요약 대신 SQL 스크립트를 출력합니다.                                                                                 | MongoDB에서는 지원되지 않음                                                  |
| `-o`, `--output` | No       | stdout 대신 파일에 기록합니다.                                                                                                             | [5.12.1](https://github.com/prisma/prisma/releases/tag/5.12.1)부터 사용 가능 |
| `--exit-code`    | No       | diff가 비어 있는지 여부를 알리도록 exit code 동작을 변경합니다 (Empty: 0, Error: 1, Not empty: 2). 기본 동작은 Success: 0, Error: 1입니다. |
| `--config`       | No       | Prisma config 파일의 사용자 지정 경로                                                                                                      |
| `--help`         | No       | 도움말 메시지를 표시합니다.                                                                                                                |

#

- Examples
  - 구성된 데이터베이스와 Prisma 스키마를 비교합니다(예: 마이그레이션 실패 후 롤포워드):

```
prisma migrate diff \
          --from-config-datasource \
          --to-schema=next_datamodel.prisma \
          --script
```

- Prisma 스키마와 구성된 데이터베이스를 비교합니다:

```
prisma migrate diff \
          --from-schema=schema.prisma \
          --to-config-datasource \
          --script
```

- 마이그레이션 디렉터리와 구성된 데이터베이스를 비교합니다(예: 운영 환경에 이미 적용된 핫픽스용 마이그레이션 생성):

```
prisma migrate diff \
          --from-migrations ./migrations \
          --to-config-datasource \
          --script
```

- 출력을 `prisma db execute`로 파이프합니다:

```
prisma migrate diff \
          --from-config-datasource \
          --to-schema=schema.prisma \
          --script | prisma db execute --stdin
```

- 두 소스가 동기화되어 있는지 감지합니다(변경이 감지되면 code 2로 종료):

```
prisma migrate diff \
          --exit-code \
          --from-config-datasource \
          --to-schema=schema.prisma
```

## Prisma Data Platform

### `platform` ([Early Access](https://docs.prisma.io/docs/console/more/feature-maturity#early-access))

`platform` 명령은 `5.10.0` 이상 버전부터 Prisma CLI를 통해 Prisma Data Platform에 접근할 수 있게 합니다.

- **Authentication** :
  - `platform auth login`: 로그인 또는 계정 생성을 위해 브라우저 창을 엽니다.
  - `platform auth logout`: 플랫폼에서 로그아웃합니다.
  - `platform auth show`: 현재 인증된 사용자 정보를 표시합니다.
- **Workspace Management** :
  - `platform workspace show`: 계정에서 사용 가능한 모든 워크스페이스를 나열합니다.
- **Project Management** :
  - `platform project show`: 지정된 워크스페이스 내 모든 프로젝트를 나열합니다.
  - `platform project create`: 지정된 워크스페이스 내에 새 프로젝트를 생성합니다.
  - `platform project delete`: 지정된 프로젝트를 삭제합니다.
- **Environment Management** :
  - `platform environment show`: 지정된 프로젝트의 모든 환경을 나열합니다.
  - `platform environment create`: 지정된 프로젝트 내에 새 환경을 생성합니다.
  - `platform environment delete`: 지정된 환경을 삭제합니다.
- **API Key Management** :
  - `platform apikey show`: 지정된 환경의 모든 API 키를 나열합니다.
  - `platform apikey create`: 지정된 환경에 새 API 키를 생성합니다.
  - `platform apikey delete`: 지정된 API 키를 삭제합니다.
- **Prisma Accelerate** :
  - `platform accelerate enable`: 지정된 환경에서 Prisma Accelerate를 활성화합니다.
  - `platform accelerate disable`: 지정된 환경에서 Prisma Accelerate를 비활성화합니다.

사용 가능한 명령과 인자의 전체 목록은 [여기](https://docs.prisma.io/docs/cli/console)에서 확인할 수 있습니다.

- `mcp`

[Prisma MCP server](https://docs.prisma.io/docs/ai/tools/mcp-server)를 시작합니다.

## Studio

- `studio`

`studio` 명령은 데이터를 대화형으로 상호작용하고 관리할 수 있게 해줍니다. 프로젝트의 데이터 스키마와 레코드로 구성된 웹 앱이 포함된 로컬 웹 서버를 시작하여 이를 수행합니다.

Prisma ORM v7은 성능 향상과 현대화된 아키텍처를 갖춘 더 안정적인 Prisma Studio 버전을 도입합니다.

지원되는 데이터베이스

현재 Prisma Studio는 PostgreSQL, MySQL, SQLite를 지원합니다. CockroachDB와 MongoDB 지원은 아직 제공되지 않지만 향후 릴리스에서 추가될 수 있습니다.

SQLite 요구 사항을 포함한 자세한 데이터베이스 지원 정보는 [Databases supported by Prisma Studio](https://docs.prisma.io/docs/studio#getting-started)를 참조하세요.

#

- Prerequisites

`studio` 명령을 사용하기 전에 `prisma.config.ts` 파일에서 데이터베이스 연결을 구성해야 합니다.

예시:

schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "sqlite"
    }
```

prisma.config.ts

```
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

#

- Options

`studio` 명령은 다음 옵션을 인식합니다.

| Option            | Required | Description                                           | Default                  |
| ----------------- | -------- | ----------------------------------------------------- | ------------------------ |
| `-b`, `--browser` | No       | Studio를 자동으로 열 브라우저입니다.                  | `<your-default-browser>` |
| `-h`, `--help`    | No       | 사용 가능한 모든 옵션을 표시하고 종료합니다.          |
| `-p`, `--port`    | No       | Studio를 시작할 포트 번호입니다.                      | 5555                     |
| `--config`        | No       | Prisma config 파일의 사용자 지정 경로                 |
| `--url`           | No       | 데이터베이스 연결 문자열(Prisma config의 값을 덮어씀) |

#

- Arguments

| Argument   | Required | Description                                                                                            | Default           |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------ | ----------------- |
| `--schema` | No       | 기본 경로 대신 처리할 `schema.prisma` 파일 경로를 지정합니다. 절대 경로와 상대 경로를 모두 지원합니다. | `./schema.prisma` |

`./prisma/schema.prisma`

#

- Examples

#

- Start Studio on the default port and open a new browser tab to it

```
    prisma studio
```

#

- Start Studio on a different port and open a new browser tab to it

```
    prisma studio --port 7777
```

#

- Start Studio and open a Firefox tab to it

```
    prisma studio --browser firefox
```

#

- Start Studio without opening a new browser tab to it

```
    prisma studio --browser none
```

#

- Start Studio with a custom Prisma config file

```
    prisma studio --config=./prisma.config.ts
```

#

- Start Studio with a direct database connection string

```
    prisma studio --url="postgresql://user:password@localhost:5432/dbname"
```

## Using a HTTP proxy for the CLI

Prisma CLI는 [사용자 지정 HTTP 프록시](https://github.com/prisma/prisma/issues/506)를 지원합니다. 이는 특히 기업 방화벽 뒤에 있는 경우에 중요합니다.

프록시 사용을 활성화하려면 다음 환경 변수 중 하나를 제공하세요.

- [`HTTP_PROXY`](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#http_proxy) 또는 `http_proxy`: http 트래픽용 프록시 URL, 예: `http://localhost:8080`

- [`HTTPS_PROXY`](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#https_proxy) 또는 `https_proxy`: https 트래픽용 프록시 URL(예: `https://localhost:8080`)

## `npx create-db`

[`create-db`](https://create-db.prisma.io/) 명령어는 단일 명령으로 임시 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 데이터베이스를 프로비저닝합니다. 이는 `npx`로 호출할 수 있는 독립 실행형 유틸리티입니다. 빠른 테스트, 프로토타이핑, 또는 Prisma Postgres 통합에 이상적입니다.

다음 변형 명령을 실행할 수 있습니다:

| Command                      | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| `npx create-db@latest`       | 임시 Prisma Postgres 데이터베이스를 생성합니다. |
| `npx create-pg@latest`       | `npx create-db`의 별칭입니다.                   |
| `npx create-postgres@latest` | `npx create-db`의 별칭입니다.                   |

이 명령들로 생성된 각 데이터베이스는 다음과 같습니다:

- 기본적으로 **24시간** 동안 사용할 수 있습니다.
- CLI 출력에 표시되는 URL을 사용해 무료로 **소유(영구화)** 할 수 있습니다.

전체 사용법, 옵션(예: `--region`, `--interactive`), 예시는 [documentation](https://docs.prisma.io/docs/postgres/npx-create-db)을 참고하세요.
