---
title: "생성기(Generators)"
description: "Prisma 스키마의 생성기(generator)는  명령이 실행될 때 어떤 자산이 생성되는지 지정합니다. 이 페이지에서는 생성기를 구성하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/overview/generators

# 생성기(Generators)

Prisma 스키마의 생성기(generator)는 `prisma generate` 명령이 실행될 때 어떤 자산이 생성되는지 지정합니다. 이 페이지에서는 생성기를 구성하는 방법을 설명합니다.

Prisma 스키마에는 하나 이상의 generator가 있을 수 있으며, [`generator`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#generator) 블록으로 표현됩니다:

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }
```

generator는 `prisma generate` 명령을 실행할 때 어떤 자산이 생성될지를 결정합니다.

Prisma Client의 기본 generator는 `prisma-client`이며, 일반 TypeScript 코드를 출력하고 사용자 지정 `output` 경로가 _필수_ 입니다([여기](https://www.prisma.io/blog/why-prisma-orm-generates-code-into-node-modules-and-why-it-ll-change)에서 자세히 보기).

또는 generator 사양을 준수하는 임의의 npm 패키지를 구성할 수 있습니다.

## `prisma-client`

새로운 `prisma-client` generator는 다양한 JavaScript 환경(예: ESM, Bun, Deno, ...)에서 Prisma ORM을 사용할 때 더 큰 제어력과 유연성을 제공합니다.

`generator` 블록의 `output` 필드로 지정한 애플리케이션 코드베이스 내 사용자 지정 디렉터리에 Prisma Client를 생성합니다. 이를 통해 생성된 코드를 완전히 확인하고 제어할 수 있습니다. 또한 생성된 Prisma Client 라이브러리를 여러 파일로 [분할](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators#importing-types)합니다.

이 generator를 사용하면 숨겨진 동작이나 자동 동작에 의존하지 않고, 원하는 방식 그대로 애플리케이션 코드를 번들링할 수 있습니다.

`prisma-client-js`와 비교한 주요 차이점은 다음과 같습니다:

- `output` 경로가 필수이며, 더 이상 `node_modules`로의 "매직" 생성이 없음
- 런타임에 `.env`를 로드하지 않음; 대신 `dotenv`를 사용하거나 환경 변수를 수동으로 설정
- `moduleFormat` 필드를 통해 ESM과 CommonJS 지원
- 추가 [fields](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators#field-reference) 덕분에 더 유연함
- 나머지 애플리케이션 코드와 동일하게 번들되는 일반 TypeScript 출력

`prisma-client` generator는 기본 generator입니다.

- 시작하기

프로젝트에서 새로운 `prisma-client` generator를 사용하려면 다음 단계를 따르세요.

#

- 1\. `schema.prisma`에서 `prisma-client` generator 구성

[`generator`](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators) 블록을 업데이트하세요:

prisma/schema.prisma

```
    generator client {
      provider = "prisma-client"            // Required
      output   = "../src/generated/prisma"  // Required
    }
```

**`output` 옵션은 필수**이며, Prisma ORM이 생성된 Prisma Client 코드를 어디에 둘지 지정합니다. 프로젝트 구조에 맞는 어떤 위치든 선택할 수 있습니다. 예를 들어 아래와 같은 레이아웃이 있다면:

```
    .
    ├── package.json
    ├── prisma
    │   └── schema.prisma
    ├── src
    │   └── index.ts
    └── tsconfig.json
```

그러면 `../src/generated/prisma`는 `schema.prisma` 기준으로 `src/generated/prisma`에 생성 코드를 배치합니다.

#

- 2\. Prisma Client 생성

다음을 실행해 Prisma Client를 생성하세요:

npm

pnpm

yarn

bun

```
    npx prisma generate
```

이렇게 하면 Prisma Client 코드(쿼리 엔진 바이너리 포함)가 지정한 `output` 폴더에 생성됩니다.

#

- 3\. 애플리케이션에서 Prisma Client 사용

#

- Prisma Client 가져오기

Prisma Client를 생성한 후, 지정한 경로에서 가져오세요:

src/index.ts

```
    import { PrismaClient } from "./generated/prisma/client";
    import { PrismaPg } from "@prisma/adapter-pg"; // or the adapter for your database
    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });
```

이제 Prisma Client를 프로젝트에서 사용할 준비가 완료되었습니다.

#

- 생성된 모델 타입 가져오기

모델에 대해 생성된 타입을 가져오려면 다음과 같이 할 수 있습니다:

src/index.ts

```
    import { UserModel, PostModel } from "./generated/prisma/models";
```

#

- 생성된 enum 타입 가져오기

enum에 대해 생성된 타입을 가져오려면 다음과 같이 할 수 있습니다:

src/index.ts

```
    import { Role, User } from "./generated/prisma/enums";
```

#

- 브라우저 환경에서 가져오기

프론트엔드 코드에서 생성된 타입에 접근해야 한다면 다음과 같이 가져올 수 있습니다:

src/index.ts

```
    import { Role } from "./generated/prisma/browser";
```

`./generated/prisma/browser`는 `PrismaClient`를 노출하지 않는다는 점에 유의하세요.

- Field reference

`generator client { ... }` 블록에서 다음 옵션을 사용하세요. 필수는 `output`뿐입니다. 나머지 필드는 기본값이 있거나 환경 및 `tsconfig.json`에서 추론됩니다.

schema.prisma

```
    generator client {
      // Required
      provider = "prisma-client"
      output   = "../src/generated/prisma"

      // Optional
      engineType             = "client"
      runtime                = "nodejs"
      moduleFormat           = "esm"
      generatedFileExtension = "ts"
      importFileExtension    = "ts"
    }
```

아래는 `prisma-client` generator의 옵션입니다:

| **옵션**            | **기본값** | **설명**                                                          |
| ------------------- | ---------- | ----------------------------------------------------------------- |
| `output` (**필수**) |            | Prisma Client가 생성되는 디렉터리(예: `../src/generated/prisma`). |
| `runtime`           | `nodejs`   | 대상 런타임 환경.                                                 |

지원 값:
`nodejs`, `deno`, `bun`, `workerd` (별칭 `cloudflare`), `vercel-edge` (별칭 `edge-light`), `react-native`.
`moduleFormat`| 환경에서 추론| 모듈 형식(`esm` 또는 `cjs`). `import.meta.url` 또는 `__dirname` 사용 여부를 결정합니다.
`generatedFileExtension`| `ts`| 생성되는 TypeScript 파일의 확장자(`ts`, `mts`, `cts`).
`importFileExtension`| 환경에서 추론| **import statements**에서 사용하는 파일 확장자. `ts`, `mts`, `cts`, `js`, `mjs`, `cjs` 또는 빈 값(베어 import용)이 될 수 있습니다.

`nodejs`, `deno`, `bun`은 모두 동일한 내부 코드 경로로 매핑되지만, 명확성을 위해 사용자에게 보이는 값은 분리되어 유지됩니다.

- 타입 가져오기

새로운 `prisma-client` generator는 개별 `.ts` 파일을 생성하여 더 세분화된 타입 import를 가능하게 합니다. 이는 컴파일 및 타입체크 성능을 개선할 수 있고 tree-shaking에도 유용합니다. 여전히 단일 import를 통해 모든 타입을 내보내는 최상위 배럴 파일을 사용할 수 있습니다.

생성된 출력의 전체 구조는 다음과 같습니다:

```
    generated/
    └── prisma
        ├── browser.ts
        ├── client.ts
        ├── commonInputTypes.ts
        ├── enums.ts
        ├── internal
        │   ├── ...
        ├── models
        │   ├── Post.ts
        │   └── User.ts
        └── models.ts
```

#

- `client.ts`

서버 코드에서 사용합니다.

- `PrismaClient` 인스턴스 및 모든 모델/유틸리티 타입에 접근 가능
- `prisma-client-js` 생성 출력과의 호환성이 가장 좋음
- 서버 전용 패키지에 대한 전이 의존성을 포함하므로 브라우저 컨텍스트에서는 사용할 수 없음

예시:

src/index.ts

```
    import { Prisma, type Post, PrismaClient } from "./generated/prisma/client";
```

#

- `browser.ts`

프론트엔드(즉, 브라우저에서 실행되는 코드)에서 타입을 사용할 때 사용합니다.

- Node.js 또는 기타 서버 전용 패키지에 대한 전이 의존성이 없음
- 실제 `PrismaClient` 생성자를 포함하지 않음
- 모든 모델/enum 타입과 값을 포함
- `Prisma.JsonNull`, `Prisma.Decimal` 같은 다양한 유틸리티에 접근 가능

예시:

src/index.ts

```
    import { Prisma, type Post } from "./generated/prisma/browser";
```

#

- `enums.ts`

사용자 정의 enum 타입과 값에 대한 분리된 접근을 제공합니다.

- 전이 의존성이 없고 매우 경량
- 백엔드와 프론트엔드 모두에서 사용 가능
- enum 접근 시 최적의 tree-shaking 및 타입체크 성능을 위해 이것을 권장

예시:

src/index.ts

```
    import { MyEnum } from "./generated/prisma/enums";
```

#

- `models.ts`

모든 모델 타입에 대한 분리된 접근을 제공합니다.

- 백엔드와 프론트엔드 모두에서 사용 가능
- `<ModelName>WhereInput` 또는 `<ModelName>UpdateInput>` 같은 파생 유틸리티 타입을 포함한 모든 모델을 포함

기본 모델 타입은 여기서 `<ModelName>Model`(예: `PostModel`)로 노출됩니다. 이는 `client.ts`와 `browser.ts`에서 단순히 `<ModelName>`(예: `Post`)로 노출되는 이름과 대조됩니다.

이는 내부 타입과의 잠재적 이름 충돌을 피하기 위한 내부 제약 때문에 필요합니다.

예시:

src/index.ts

```
    import type {
      UserModel,
      PostModel,
      PostWhereInput,
      UserUpdateInput,
    } from "./generated/prisma/models";
```

#

- `models/<ModelName>.ts`

개별 모델의 타입에 대한 분리된 접근을 제공합니다.

- 백엔드와 프론트엔드 모두에서 사용 가능
- `<ModelName>WhereInput` 또는 `<ModelName>UpdateInput>` 같은 파생 유틸리티 타입을 포함한 해당 모델 타입을 포함

기본 모델 타입은 여기서 `<ModelName>Model`(예: `PostModel`)로 노출됩니다.

예시:

src/index.ts

```
    import type { UserModel, UserWhereInput, UserUpdateInput } from "./generated/prisma/models/User";
```

#

- `commonInputTypes.ts`

직접 필요할 일은 거의 없는 공통 유틸리티 타입을 제공합니다.

예시:

```
    import type { IntFilter } from "./generated/prisma/commonInputTypes";
```

#

- `internal/*`

이 파일들에서 직접 import하지 마세요! 이들은 생성 코드의 안정적인 API 일부가 아니며, 언제든 호환성이 깨지는 방식으로 변경될 수 있습니다.

일반적으로 այնտեղ서 필요할 수 있는 항목은 `browser.ts` 또는 `client.ts`의 `Prisma` 네임스페이스를 통해 노출됩니다.

- `prisma-client-js`에서의 주요 변경 사항
  - `generator` 블록에 `output` 경로가 필수
  - `Prisma.validator` 함수 없음; 대신 TypeScript 네이티브 [`satisfies`](https://www.prisma.io/blog/satisfies-operator-ur8ys8ccq7zb) 키워드를 사용할 수 있음

- 예제

새로운 `prisma-client` generator가 실제로 어떻게 보이는지 확인하려면 최소 예제와 [즉시 실행 가능한 예제](https://github.com/prisma/prisma-examples)를 확인하세요:

| 예제                                                                                                                                                               | 프레임워크     | 번들러            | 런타임                                           | 모노레포  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ----------------- | ------------------------------------------------ | --------- |
| [`nextjs-starter-webpack`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nextjs-starter-webpack)                                   | Next.js 15     | Webpack           | Node.js                                          | n/a       |
| [`nextjs-starter-turbopack`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nextjs-starter-turbopack)                               | Next.js 15     | Turbopack (alpha) | Node.js                                          | n/a       |
| [`nextjs-starter-webpack-monorepo`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nextjs-starter-webpack-monorepo)                 | Next.js 15     | Webpack           | Node.js                                          | pnpm      |
| [`nextjs-starter-webpack-with-middleware`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nextjs-starter-webpack-with-middleware)   | Next.js 15     | Webpack           | Node.js (main pages), `vercel-edge` (middleware) | n/a       |
| [`nextjs-starter-webpack-turborepo`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nextjs-starter-webpack-turborepo)               | Next.js 15     | Webpack           | Node.js                                          | turborepo |
| [`react-router-starter-nodejs`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/react-router-starter-nodejs)                         | React Router 7 | Vite 6            | Node.js                                          | n/a       |
| [`react-router-starter-cloudflare-workerd`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/react-router-starter-cloudflare-workerd) | React Router 7 |                   |                                                  | n/a       |
| [`nuxt3-starter-nodejs`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nuxt3-starter-nodejs)                                       | Nuxt 3         | Vite 6            | Node.js                                          | n/a       |
| [`nuxt4-starter-nodejs`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/nuxt4-starter-nodejs)                                       | Nuxt 4         | Vite 7            | Node.js                                          | n/a       |
| [`bun`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/deno-deploy)                                                                 | None           | None              | Deno 2                                           | n/a       |

[`deno`](https://github.com/prisma/prisma-examples/tree/latest/generator-prisma-client/deno-deploy)| 없음| 없음| Deno 2| n/a

## `prisma-client-js` (사용 중단 예정)

사용 중단 예정

`prisma-client-js` 제너레이터는 사용 중단 예정입니다. 새 프로젝트에는 [`prisma-client`](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators#prisma-client) 사용을 권장하며, 가능한 경우 기존 프로젝트도 업데이트하는 것을 권장합니다.

`prisma-client-js` 제너레이터는 `@prisma/client` npm 패키지가 필요하며, Prisma Client를 `node_modules`에 생성합니다.

- 필드 참조

Prisma의 JavaScript Client용 제너레이터는 다음과 같은 여러 추가 속성을 허용합니다:

- `previewFeatures`: 포함할 [프리뷰 기능](https://docs.prisma.io/docs/orm/reference/preview-features/client-preview-features)
- `binaryTargets`: `prisma-client-js`용 엔진 바이너리 타깃(예: Ubuntu 18+에 배포하는 경우 `debian-openssl-1.1.x`, 로컬에서 작업하는 경우 `native`)

prisma/schema.prisma

```
    generator client {
      provider        = "prisma-client-js"
      previewFeatures = ["sample-preview-feature"]
      binaryTargets   = ["debian-openssl-1.1.x"] // defaults to `"native"`
    }
```

## 커뮤니티 제너레이터

[멀티 파일 Prisma 스키마](https://docs.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema)를 사용하는 경우, 제너레이터가 스키마를 수동으로 읽지 않는 한 기존 제너레이터나 새 제너레이터는 영향을 받지 않아야 합니다.

다음은 커뮤니티에서 만든 제너레이터 목록입니다.

- [`prisma-dbml-generator`](https://notiz.dev/blog/prisma-dbml-generator/): Prisma 스키마를 [Database Markup Language](https://dbml.dbdiagram.io/home/) (DBML)로 변환하여 쉽게 시각적으로 표현할 수 있게 합니다.
- [`prisma-docs-generator`](https://github.com/pantharshit00/prisma-docs-generator): Prisma Client용 개별 API 레퍼런스를 생성합니다.
- [`prisma-json-schema-generator`](https://github.com/valentinpalkovic/prisma-json-schema-generator): Prisma 스키마를 [JSON schema](https://json-schema.org/)로 변환합니다.
- [`prisma-json-types-generator`](https://github.com/arthurfiorette/prisma-json-types-generator): 스키마를 기반으로 모든 데이터베이스에서 강타입 JSON 필드를 제공하도록 `prisma-client-js`(또는 `prisma-client`)를 강화합니다. 런타임 코드에 영향을 주지 않으면서 코드 생성, Intellisense 등을 개선합니다.
- [`typegraphql-prisma`](https://github.com/MichalLytek/typegraphql-prisma#readme): Prisma 모델용 [TypeGraphQL](https://typegraphql.com/) CRUD 리졸버를 생성합니다.
- [`typegraphql-prisma-nestjs`](https://github.com/EndyKaufman/typegraphql-prisma-nestjs#readme): [`typegraphql-prisma`](https://github.com/MichalLytek/typegraphql-prisma)의 포크로, Prisma 모델용 CRUD 리졸버를 생성하지만 NestJS용입니다.
- [`prisma-typegraphql-types-gen`](https://github.com/YassinEldeeb/prisma-tgql-types-gen): prisma 타입 정의에서 [TypeGraphQL](https://typegraphql.com/) 클래스 타입과 enum을 생성합니다. 생성된 출력은 다음 생성 시 덮어쓰이지 않고 수정할 수 있으며, 수정 과정에서 타입을 잘못 바꾸면 이를 교정할 수 있는 기능도 제공합니다.
- [`nexus-prisma`](https://github.com/prisma/nexus-prisma/): [GraphQL Nexus](https://nexusjs.org/docs/)를 통해 Prisma 모델을 GraphQL로 투영할 수 있게 합니다.
- [`prisma-nestjs-graphql`](https://github.com/unlight/prisma-nestjs-graphql): `@nestjs/graphql` 모듈에서 사용할 수 있도록 Prisma Schema에서 object types, inputs, args 등을 생성합니다.
- [`prisma-appsync`](https://github.com/maoosi/prisma-appsync): [AWS AppSync](https://aws.amazon.com/appsync/)용 완전한 GraphQL API를 생성합니다.
- [`prisma-kysely`](https://github.com/valtyr/prisma-kysely): TypeScript SQL 쿼리 빌더인 Kysely용 타입 정의를 생성합니다. 이를 통해 엣지 런타임에서 데이터베이스 쿼리를 수행하거나, 타입 안정성을 유지하면서 Prisma만으로는 어려운 더 복잡한 SQL 쿼리를 작성할 수 있습니다.
- [`prisma-generator-nestjs-dto`](https://github.com/vegardit/prisma-generator-nestjs-dto): [NestJS Resources](https://docs.nestjs.com/recipes/crud-generator) 및 [@nestjs/swagger](https://www.npmjs.com/package/@nestjs/swagger)와 함께 사용할 수 있도록 relation `connect` 및 `create` 옵션을 포함한 DTO와 Entity 클래스를 생성합니다.
- [`prisma-erd-generator`](https://github.com/keonik/prisma-erd-generator): 엔터티 관계 다이어그램을 생성합니다.
- [`prisma-generator-plantuml-erd`](https://github.com/dbgso/prisma-generator-plantuml-erd/tree/main/packages/generator): PlantUML용 ER 다이어그램을 생성하는 제너레이터입니다. 옵션을 활성화하면 Markdown 및 Asciidoc 문서도 생성할 수 있습니다.
- [`prisma-class-generator`](https://github.com/kimjbstar/prisma-class-generator): Prisma Schema에서 DTO, Swagger Response, TypeGraphQL 등에 사용할 수 있는 클래스를 생성합니다.
- [`zod-prisma`](https://github.com/CarterGrimmeisen/zod-prisma): Prisma 모델에서 Zod 스키마를 생성합니다.
- [`prisma-pothos-types`](https://github.com/hayes/pothos/tree/main/packages/plugin-prisma): Prisma 기반 object type 정의를 더 쉽게 만들고, relation의 n+1 쿼리 문제 해결을 돕습니다. Relay 플러그인과의 통합도 제공하여 node와 connection을 쉽고 효율적으로 정의할 수 있습니다.
- [`prisma-generator-pothos-codegen`](https://github.com/Cauen/prisma-generator-pothos-codegen): Prisma schema에서 [Pothos](https://pothos-graphql.dev/)용 입력 타입(args로 사용)을 자동 생성하고, 분리된 타입 안전 base 파일을 자동 생성하여 커스터마이즈 가능한 object, query, mutation을 쉽게 만들 수 있게 합니다. 선택적으로 base 파일에서 모든 crud를 한 번에 생성할 수 있습니다.
- [`prisma-joi-generator`](https://github.com/omar-dulaimi/prisma-joi-generator): Prisma schema에서 전체 Joi 스키마를 생성합니다.
- [`prisma-yup-generator`](https://github.com/omar-dulaimi/prisma-yup-generator): Prisma schema에서 전체 Yup 스키마를 생성합니다.
- [`prisma-class-validator-generator`](https://github.com/omar-dulaimi/prisma-class-validator-generator): class validator 검증이 준비된 TypeScript 모델을 Prisma schema에서 출력합니다.
- [`prisma-zod-generator`](https://github.com/omar-dulaimi/prisma-zod-generator): Prisma schema에서 Zod 스키마를 출력합니다.
- [`prisma-trpc-generator`](https://github.com/omar-dulaimi/prisma-trpc-generator): 완전히 구현된 tRPC 라우터를 출력합니다.
- [`prisma-json-server-generator`](https://github.com/omar-dulaimi/prisma-json-server-generator): json-server로 실행할 수 있는 JSON 파일을 출력합니다.
- [`prisma-trpc-shield-generator`](https://github.com/omar-dulaimi/prisma-trpc-shield-generator): Prisma schema에서 tRPC shield를 출력합니다.
- [`prisma-custom-models-generator`](https://github.com/omar-dulaimi/prisma-custom-models-generator): Prisma 권장 사항을 기반으로 Prisma schema에서 커스텀 모델을 출력합니다.
- [`nestjs-prisma-graphql-crud-gen`](https://github.com/mk668a/nestjs-prisma-graphql-crud-gen): NestJS와 Prisma로 GraphQL schema에서 CRUD 리졸버를 생성합니다.
- [`prisma-generator-dart`](https://github.com/FredrikBorgstrom/abcx3/tree/master/libs/prisma-generator-dart): to- 및 fromJson 메서드가 포함된 Dart/Flutter 클래스 파일을 생성합니다.
- [`prisma-generator-graphql-typedef`](https://github.com/mavvy22/prisma-generator-graphql-typedef): graphql 스키마를 생성합니다.
- [`prisma-markdown`](https://github.com/samchon/prisma-markdown): ERD 다이어그램과 해당 설명으로 구성된 markdown 문서를 생성합니다. `@namespace` 주석 태그를 통해 ERD 다이어그램의 페이지네이션을 지원합니다.
- [`prisma-models-graph`](https://github.com/dangchinh25/prisma-models-graph): 스키마에 엄격한 관계가 정의되지 않은 경우를 위해 양방향 모델 그래프를 생성하며, 커스텀 스키마 어노테이션으로 동작합니다.
- [`prisma-generator-fake-data`](https://github.com/luisrudge/prisma-generator-fake-data): 단위/통합 테스트, 데모 등에서 사용할 수 있도록 Prisma 모델용으로 현실적인 가짜 데이터를 생성합니다.
- [`prisma-generator-drizzle`](https://github.com/farreldarian/prisma-generator-drizzle): Drizzle 스키마를 쉽게 생성하기 위한 Prisma 제너레이터입니다.
- [`prisma-generator-express`](https://github.com/multipliedtwice/prisma-generator-express): Express CRUD 및 Router generator function을 생성합니다.
- [`prismabox`](https://github.com/m1212e/prismabox): Prisma 모델에서 다목적으로 활용 가능한 [typebox](https://github.com/sinclairzx81/typebox) 스키마를 생성합니다.
- [`prisma-generator-typescript-interfaces`](https://github.com/mogzol/prisma-generator-typescript-interfaces): Prisma schema에서 의존성이 없는 TypeScript 인터페이스를 생성합니다.
- [`prisma-openapi`](https://github.com/nitzano/prisma-openapi): Prisma 모델에서 OpenAPI 스키마를 생성합니다.
