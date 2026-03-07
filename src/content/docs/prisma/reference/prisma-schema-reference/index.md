---
title: "Schema API 레퍼런스"
description: "Prisma 스키마 언어(PSL) 참조"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/prisma-schema-reference

# Schema API 레퍼런스

Prisma 스키마 언어(PSL) 참조

## `datasource`

Prisma 스키마에서 [data source](https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources)를 정의합니다.

- 필드

`datasource` 블록은 다음 필드를 허용합니다:

| Name           | Required | Type                                                                            | Description                                                                                                                                                  |
| -------------- | -------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `provider`     | **Yes**  | String (`postgresql`, `mysql`, `sqlite`, `sqlserver`, `mongodb`, `cockroachdb`) | 사용할 데이터베이스 커넥터를 지정합니다.                                                                                                                     |
| `relationMode` | No       | String (`foreignKeys`, `prisma`)                                                | [참조 무결성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode)을 외래 키로 강제할지, Prisma로 강제할지 설정합니다.          |
| `schemas`      | No       | Array of strings                                                                | 포함할 데이터베이스 스키마 목록입니다([multi-schema](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema) 지원, PostgreSQL 및 SQL Server). |
| `extensions`   | No       | Array of extension names                                                        | 활성화할 [PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions)입니다.                                                 |

연결 URL(`url`, `directUrl`, `shadowDatabaseUrl`)은 스키마 파일이 아니라 [`prisma.config.ts`](https://docs.prisma.io/docs/orm/reference/prisma-config-reference#datasourceurl)에서 구성합니다.

다음 provider를 사용할 수 있습니다:

- `sqlite`
- `postgresql`
- `mysql`
- `sqlserver`
- `mongodb`
- `cockroachdb`

* 비고
  - 스키마에는 `datasource` 블록을 **하나만** 둘 수 있습니다.
  - `datasource db`는 관례일 뿐이며, 데이터 소스 이름은 자유롭게 지정할 수 있습니다. 예: `datasource mysql`, `datasource data`.

* 예제

#

- PostgreSQL datasource

```
    datasource db {
      provider = "postgresql"
    }
```

`prisma.config.ts`에서 연결 URL을 구성합니다:

```
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      datasource: {
        url: env("DATABASE_URL"),
      },
    });
```

PostgreSQL 연결 문자열에 대한 자세한 내용은 [여기](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)에서 확인하세요.

#

- 환경 변수를 통해 PostgreSQL data source 지정

이 예제에서 대상 데이터베이스는 다음 자격 증명으로 접근할 수 있습니다:

- 사용자: `johndoe`
- 비밀번호: `mypassword`
- 호스트: `localhost`
- 포트: `5432`
- 데이터베이스 이름: `mydb`
- 스키마 이름: `public`

```
    datasource db {
      provider = "postgresql"
    }
```

데이터베이스 연결 URL이 필요한 Prisma CLI 명령(예: `prisma generate`)을 실행할 때는 `DATABASE_URL` 환경 변수가 설정되어 있어야 합니다.

한 가지 방법은 아래 내용으로 [`.env`](https://github.com/motdotla/dotenv) 파일을 만드는 것입니다. Prisma CLI가 자동으로 감지하려면 해당 파일이 `schema.prisma` 파일과 같은 디렉터리에 있어야 합니다.

```
    DATABASE_URL=postgresql://johndoe:mypassword@localhost:5432/mydb?schema=public
```

#

- MySQL datasource

```
    datasource db {
      provider = "mysql"
    }
```

[MySQL connection URLs](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)에 대해 더 알아보세요.

#

- MongoDB datasource

```
    datasource db {
      provider = "mongodb"
    }
```

[MongoDB connection URLs](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에 대해 더 알아보세요.

#

- SQLite datasource

```
    datasource db {
      provider = "sqlite"
    }
```

[SQLite connection URLs](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sqlite)에 대해 더 알아보세요.

#

- CockroachDB datasource

```
    datasource db {
      provider = "cockroachdb"
    }
```

CockroachDB는 PostgreSQL과 동일한 연결 URL 형식을 사용합니다. [PostgreSQL connection URLs](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)에 대해 더 알아보세요.

#

- Multi-schema datasource (PostgreSQL)

```
    datasource db {
      provider = "postgresql"
      schemas  = ["public", "analytics"]
    }
```

## `generator`

Prisma 스키마에서 [generator](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators)를 정의합니다.

- `prisma-client-js` provider용 필드

이는 Prisma ORM 6.x 및 이전 버전의 기본 generator입니다. [generators](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators#prisma-client-js-deprecated)에 대해 더 알아보세요.

`generator` 블록은 다음 필드를 허용합니다:

| Name              | Required | Type                         | Description                                                                                                                                                                                            |
| ----------------- | -------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `provider`        | **Yes**  | `prisma-client-js`           | 사용할 [generator](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators)를 설명합니다. generator를 구현한 파일을 가리키거나 내장 generator를 직접 지정할 수 있습니다.                     |
| `output`          | No       | String (file path)           | 생성된 클라이언트의 위치를 결정합니다. [자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider). **Default** : `node_modules/.prisma/client` |
| `previewFeatures` | No       | List of Enums                | 현재 사용 가능한 Preview 기능 목록은 intellisense로 확인하세요(Visual Studio Code에서 `Ctrl+Space`). **Default** : none                                                                                |
| `engineType`      | No       | Enum (`library` or `binary`) | 다운로드하고 사용할 쿼리 엔진 유형을 정의합니다. **Default** : `library`                                                                                                                               |
| `binaryTargets`   | No       | List of Enums (see below)    | 쿼리 엔진 호환성을 보장하기 위해 Prisma Client가 실행될 OS를 지정합니다. **Default** : `native`                                                                                                        |
| `moduleFormat`    | No       | Enum (`cjs` or `esm`)        | 생성된 Prisma Client의 모듈 형식을 정의합니다. 이 필드는 `prisma-client` generator에서만 사용할 수 있습니다.                                                                                           |

important

커스텀 output 경로를 정의하고, 해당 경로를 `.gitignore`에 추가한 뒤, 사용자 정의 빌드 스크립트 또는 postinstall 훅을 통해 `prisma generate`를 실행하는 것을 권장합니다.

- `prisma-client` provider용 필드

서로 다른 JavaScript 환경에서 더 큰 제어력과 유연성을 제공하는 ESM 우선 클라이언트 generator입니다. 커스텀 디렉터리에 순수 TypeScript 코드를 생성하므로 생성 코드 전체를 직접 확인할 수 있습니다. 새로운 [`prisma-client`](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators#prisma-client) generator에 대해 더 알아보세요.

`prisma-client` generator는 Prisma ORM 7의 기본 generator입니다.

`generator` 블록은 다음 필드를 허용합니다:

| Name                     | Required | Type                                                                                                               | Description                                                                                                                                                                        |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider`               | **Yes**  | `prisma-client`                                                                                                    | 사용할 [generator](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators)를 설명합니다. generator를 구현한 파일을 가리키거나 내장 generator를 직접 지정할 수 있습니다. |
| `output`                 | **Yes**  | String (file path)                                                                                                 | 생성된 클라이언트의 위치를 결정합니다. [자세히 보기](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider).                         |
| `previewFeatures`        | No       | List of Enums                                                                                                      | 현재 사용 가능한 Preview 기능 목록은 intellisense로 확인하세요(Visual Studio Code에서 `Ctrl+Space`). **Default** : none                                                            |
| `runtime`                | No       | Enum (`nodejs`, `deno`, `bun`, `workerd` (alias `cloudflare`), `vercel-edge` (alias `edge-light`), `react-native`) | 대상 런타임 환경입니다. **Default** : `nodejs`                                                                                                                                     |
| `moduleFormat`           | No       | Enum (`esm` or `cjs`)                                                                                              | 생성된 코드가 ESM(`import` 사용) 또는 CommonJS(`require(...)` 사용) 모듈을 지원할지 결정합니다. 특별한 이유가 없다면 항상 `esm`을 권장합니다. **Default** : 환경에서 추론됨.       |
| `generatedFileExtension` | No       | Enum (`ts` or `mts` or `cts`)                                                                                      | 생성된 TypeScript 파일의 확장자입니다. **Default** : `ts`                                                                                                                          |
| `importFileExtension`    | No       | Enum (`ts`,`mts`,`cts`,`js`,`mjs`,`cjs`, empty (for bare imports))                                                 | import 문에서 사용할 파일 확장자입니다. **Default** : 환경에서 추론됨.                                                                                                             |
| `compilerBuild`          | No       | String (`fast`, `small`)                                                                                           | 생성된 클라이언트에 사용할 쿼리 컴파일러 빌드를 정의합니다. 기본값인 `fast`는 쿼리 컴파일이 빠르지만 크기가 증가합니다. `small`은 크기를 최소화하지만 실행 속도가 약간 느립니다.   |

#

- `binaryTargets` 옵션

아래 표에는 `binaryTargets`에서 지정할 수 있는 플랫폼 이름과 함께 지원되는 모든 운영 체제가 나열되어 있습니다.

별도 명시가 없으면 기본 지원 CPU 아키텍처는 x86_64입니다.

#

- macOS

| Build OS           | Prisma engine build name |
| ------------------ | ------------------------ |
| macOS Intel x86_64 | `darwin`                 |
| macOS ARM64        | `darwin-arm64`           |

#

- Windows

| Build OS | Prisma engine build name |
| -------- | ------------------------ |
| Windows  | `windows`                |

#

- Linux (x86_64 아키텍처의 Alpine)

| Build OS           | Prisma engine build name   | OpenSSL |
| ------------------ | -------------------------- | ------- |
| Alpine (3.17 이상) | `linux-musl-openssl-3.0.x` | 3.0.x   |
| Alpine (3.16 이하) | `linux-musl`               | 1.1.x   |

#

- Linux (ARM64 아키텍처의 Alpine)

| Build OS           | Prisma engine build name         | OpenSSL |
| ------------------ | -------------------------------- | ------- |
| Alpine (3.17 이상) | `linux-musl-arm64-openssl-3.0.x` | 3.0.x   |
| Alpine (3.16 이하) | `linux-musl-arm64-openssl-1.1.x` | 1.1.x   |

#

- Linux (Debian), x86_64

| Build OS             | Prisma engine build name | OpenSSL |
| -------------------- | ------------------------ | ------- |
| Debian 8 (Jessie)    | `debian-openssl-1.0.x`   | 1.0.x   |
| Debian 9 (Stretch)   | `debian-openssl-1.1.x`   | 1.1.x   |
| Debian 10 (Buster)   | `debian-openssl-1.1.x`   | 1.1.x   |
| Debian 11 (Bullseye) | `debian-openssl-1.1.x`   | 1.1.x   |
| Debian 12 (Bookworm) | `debian-openssl-3.0.x`   | 3.0.x   |

#

- Linux (Ubuntu), x86_64

| Build OS               | Prisma engine build name | OpenSSL |
| ---------------------- | ------------------------ | ------- |
| Ubuntu 14.04 (trusty)  | `debian-openssl-1.0.x`   | 1.0.x   |
| Ubuntu 16.04 (xenial)  | `debian-openssl-1.0.x`   | 1.0.x   |
| Ubuntu 18.04 (bionic)  | `debian-openssl-1.1.x`   | 1.1.x   |
| Ubuntu 19.04 (disco)   | `debian-openssl-1.1.x`   | 1.1.x   |
| Ubuntu 20.04 (focal)   | `debian-openssl-1.1.x`   | 1.1.x   |
| Ubuntu 21.04 (hirsute) | `debian-openssl-1.1.x`   | 1.1.x   |
| Ubuntu 22.04 (jammy)   | `debian-openssl-3.0.x`   | 3.0.x   |
| Ubuntu 23.04 (lunar)   | `debian-openssl-3.0.x`   | 3.0.x   |

#

- Linux (CentOS), x86_64

| Build OS | Prisma engine build name | OpenSSL |
| -------- | ------------------------ | ------- |
| CentOS 7 | `rhel-openssl-1.0.x`     | 1.0.x   |
| CentOS 8 | `rhel-openssl-1.1.x`     | 1.1.x   |

#

- Linux (Fedora), x86_64

| Build OS  | Prisma engine build name | OpenSSL |
| --------- | ------------------------ | ------- |
| Fedora 28 | `rhel-openssl-1.1.x`     | 1.1.x   |
| Fedora 29 | `rhel-openssl-1.1.x`     | 1.1.x   |

Fedora 30| `rhel-openssl-1.1.x`| 1.1.x
Fedora 36| `rhel-openssl-3.0.x`| 3.0.x
Fedora 37| `rhel-openssl-3.0.x`| 3.0.x
Fedora 38| `rhel-openssl-3.0.x`| 3.0.x

#

- Linux (Linux Mint), x86_64

| 빌드 OS       | Prisma 엔진 빌드 이름  | OpenSSL |
| ------------- | ---------------------- | ------- |
| Linux Mint 18 | `debian-openssl-1.0.x` | 1.0.x   |
| Linux Mint 19 | `debian-openssl-1.1.x` | 1.1.x   |
| Linux Mint 20 | `debian-openssl-1.1.x` | 1.1.x   |
| Linux Mint 21 | `debian-openssl-3.0.x` | 3.0.x   |

#

- Linux (Arch Linux), x86_64

| 빌드 OS               | Prisma 엔진 빌드 이름  | OpenSSL |
| --------------------- | ---------------------- | ------- |
| Arch Linux 2019.09.01 | `debian-openssl-1.1.x` | 1.1.x   |
| Arch Linux 2023.04.23 | `debian-openssl-3.0.x` | 3.0.x   |

#

- Linux ARM64 (all major distros but Alpine)

| 빌드 OS                       | Prisma 엔진 빌드 이름       | OpenSSL |
| ----------------------------- | --------------------------- | ------- |
| Linux ARM64 glibc 기반 배포판 | `linux-arm64-openssl-1.0.x` | 1.0.x   |
| Linux ARM64 glibc 기반 배포판 | `linux-arm64-openssl-1.1.x` | 1.1.x   |
| Linux ARM64 glibc 기반 배포판 | `linux-arm64-openssl-3.0.x` | 3.0.x   |

- 예제

#

- 기본 `output`, `previewFeatures`, `engineType`, `binaryTargets`를 사용해 `prisma-client-js` generator 지정하기

```
    generator client {
      provider = "prisma-client-js"
    }
```

위의 `generator` 정의는 `output`, `engineType`, `binaryTargets`(그리고 암묵적인 `previewFeatures`)의 기본값을 사용하므로 다음과 **동등**합니다:

```
    generator client {
      provider      = "prisma-client-js"
      output        = "node_modules/.prisma/client"
      engineType    = "library"
      binaryTargets = ["native"]
    }
```

#

- Prisma Client에 대한 사용자 지정 `output` 위치 지정하기

이 예제는 생성된 자산의 사용자 지정 `output` 위치를 정의하여 기본 위치를 재정의하는 방법을 보여줍니다.

```
    generator client {
      provider = "prisma-client-js"
      output   = "../src/generated/client"
    }
```

#

- OS 호환성을 보장하기 위해 사용자 지정 `binaryTargets` 지정하기

이 예제는 [위](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#linux-ubuntu-x86_64) 표를 기반으로 Prisma Client가 `Ubuntu 19.04 (disco)`에서 실행되도록 구성하는 방법을 보여줍니다.

```
    generator client {
      provider      = "prisma-client-js"
      binaryTargets = ["debian-openssl-1.1.x"]
    }
```

#

- 사용자 지정 generator 구현을 가리키는 `provider` 지정하기

이 예제는 `my-generator`라는 디렉터리에 위치한 사용자 지정 generator를 사용하는 방법을 보여줍니다.

```
    generator client {
      provider = "./my-generator"
    }
```

## `model`

Prisma [model](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-models)을 정의합니다.

- 비고
  - 모델의 모든 레코드는 _고유하게_ 식별 가능해야 합니다. 모델마다 다음 속성 중 _최소_ 하나를 정의해야 합니다:
    - `@unique`
    - `@@unique`
    - `@id`
    - `@@id`

#

- 이름 지정 규칙
  - 모델 이름은 다음 정규식을 따라야 합니다: `[A-Za-z][A-Za-z0-9_]*`
  - 모델 이름은 문자로 시작해야 하며 일반적으로 [PascalCase](https://wiki.c2.com/?PascalCase)로 작성합니다
  - 모델 이름은 단수형을 사용해야 합니다(예: `user`, `users`, `Users` 대신 `User`)
  - Prisma ORM에는 내부적으로 사용하는 여러 **예약어**가 있으며, 따라서 모델 이름으로 사용할 수 없습니다. 예약어는 [여기](https://github.com/prisma/prisma/blob/6.5.0/packages/client/src/generation/generateClient.ts#L556-L605)와 [여기](https://github.com/prisma/prisma-engines/blob/main/psl/parser-database/src/names/reserved_model_names.rs#L44)에서 확인할 수 있습니다.

> **참고** : [`@@map` attribute](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#map-1)를 사용하면 모델(예: `User`)을 모델 이름 지정 규칙과 일치하지 않는 다른 이름의 테이블(예: `users`)에 매핑할 수 있습니다.

#

- 필드 순서
  - Introspection은 데이터베이스의 해당 열 순서와 동일한 순서로 모델 필드를 나열합니다. 관계 필드는 스칼라 필드 뒤에 나열됩니다.

- 예제

#

- 두 개의 스칼라 필드를 가진 `User`라는 이름의 모델

관계형 데이터베이스

MongoDB

```
    model User {
      email String  @unique // `email` can not be optional because it's the only unique field on the model
      name  String?
    }
```

## `model` 필드

[Fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-fields)는 모델의 속성입니다.

- 비고

#

- 이름 지정 규칙
  - 문자로 시작해야 합니다
  - 일반적으로 camelCase로 작성합니다
  - 다음 정규식을 따라야 합니다: `[A-Za-z][A-Za-z0-9_]*`

> **참고** : [`@map` attribute](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#map)를 사용하면 필드 이름 지정 규칙과 일치하지 않는 다른 이름의 [열에 필드 이름을 매핑](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)할 수 있습니다. 예: `myField @map("my_field")`.

## `model` 필드 스칼라 타입

*데이터 소스 커넥터*는 Prisma ORM 스칼라 타입 각각이 어떤 *네이티브 데이터베이스 타입*에 매핑되는지를 결정합니다. 마찬가지로 *generator*는 이러한 타입 각각이 *대상 프로그래밍 언어의 어떤 타입*에 매핑되는지를 결정합니다.

Prisma 모델에는 모델 간 관계를 정의하는 [model field types](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)도 있습니다.

- `String`

가변 길이 텍스트입니다.

#

- 기본 타입 매핑

| 커넥터      | 기본 매핑        |
| ----------- | ---------------- |
| PostgreSQL  | `text`           |
| SQL Server  | `nvarchar(1000)` |
| MySQL       | `varchar(191)`   |
| MongoDB     | `String`         |
| SQLite      | `TEXT`           |
| CockroachDB | `STRING`         |

#

- PostgreSQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고                                                                                                                                                                                                  |
| -------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`                     | `@db.Text`                           |
| `char(x)`                  | `@db.Char(x)`                        |
| `varchar(x)`               | `@db.VarChar(x)`                     |
| `bit(x)`                   | `@db.Bit(x)`                         |
| `varbit`                   | `@db.VarBit`                         |
| `uuid`                     | `@db.Uuid`                           |
| `xml`                      | `@db.Xml`                            |
| `inet`                     | `@db.Inet`                           |
| `citext`                   | `@db.Citext`                         | [Citext 확장](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#enable-postgresql-extensions-for-native-database-functions)이 활성화된 경우에만 사용 가능합니다. |

#

- MySQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute |
| -------------------------- | ------------------------------------ |
| `VARCHAR(x)`               | `@db.VarChar(x)`                     |
| `TEXT`                     | `@db.Text`                           |
| `CHAR(x)`                  | `@db.Char(x)`                        |
| `TINYTEXT`                 | `@db.TinyText`                       |
| `MEDIUMTEXT`               | `@db.MediumText`                     |
| `LONGTEXT`                 | `@db.LongText`                       |

Prisma Migrate를 사용해 `@db.Bit(1)`을 `String`에 매핑할 수 있습니다:

```
    model Model {
      /* ... */
      myField String @db.Bit(1)
    }
```

#

- MongoDB

`String`

| 네이티브 데이터베이스 타입 attribute | 참고                                                           |
| ------------------------------------ | -------------------------------------------------------------- |
| `@db.String`                         |
| `@db.ObjectId`                       | 기본 BSON 타입이 `OBJECT_ID`인 경우 필수(ID 필드, 관계 스칼라) |

#

- Microsoft SQL Server

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute |
| -------------------------- | ------------------------------------ |
| `char(x)`                  | `@db.Char(x)`                        |
| `nchar(x)`                 | `@db.NChar(x)`                       |
| `varchar(x)`               | `@db.VarChar(x)`                     |
| `nvarchar(x)`              | `@db.NVarChar(x)`                    |
| `text`                     | `@db.Text`                           |
| `ntext`                    | `@db.NText`                          |
| `xml`                      | `@db.Xml`                            |
| `uniqueidentifier`         | `@db.UniqueIdentifier`               |

#

- SQLite

`TEXT`

#

- CockroachDB

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고         |
| -------------------------- | ------------------------------------ | ------------ | --------------- |
| `STRING(x)`                | `TEXT(x)`                            | `VARCHAR(x)` | `@db.String(x)` |
| `CHAR(x)`                  | `@db.Char(x)`                        |
| `"char"`                   | `@db.CatalogSingleChar`              |
| `BIT(x)`                   | `@db.Bit(x)`                         |
| `VARBIT`                   | `@db.VarBit`                         |
| `UUID`                     | `@db.Uuid`                           |
| `INET`                     | `@db.Inet`                           |

PostgreSQL에서 지원되는 `xml` 및 `citext` 타입은 현재 CockroachDB에서는 지원되지 않습니다.

#

- 클라이언트

## Prisma Client JS

`string`

- `Boolean`

참 또는 거짓 값입니다.

#

- 기본 타입 매핑

| 커넥터      | 기본 매핑    |
| ----------- | ------------ |
| PostgreSQL  | `boolean`    |
| SQL Server  | `bit`        |
| MySQL       | `TINYINT(1)` |
| MongoDB     | `Bool`       |
| SQLite      | `INTEGER`    |
| CockroachDB | `BOOL`       |

#

- PostgreSQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고 |
| -------------------------- | ------------------------------------ | ---- |
| `boolean`                  | `@db.Boolean`                        |

#

- MySQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고                                                                                                            |
| -------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `TINYINT(1)`               | `@db.TinyInt(1)`                     | `TINYINT`의 최대 길이가 1보다 크거나(예: `TINYINT(2)`) 기본값이 `1`, `0`, `NULL` 이외인 경우 `Int`에 매핑됩니다 |
| `BIT(1)`                   | `@db.Bit`                            |

#

- MongoDB

`Bool`

#

- Microsoft SQL Server

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고 |
| -------------------------- | ------------------------------------ | ---- |
| `bit`                      | `@db.Bit`                            |

#

- SQLite

`INTEGER`

#

- CockroachDB

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고 |
| -------------------------- | ------------------------------------ | ---- |
| `BOOL`                     | `@db.Bool`                           |

#

- 클라이언트

## Prisma Client JS

`boolean`

- `Int`

#

- 기본 타입 매핑

| 커넥터      | 기본 매핑 |
| ----------- | --------- |
| PostgreSQL  | `integer` |
| SQL Server  | `int`     |
| MySQL       | `INT`     |
| MongoDB     | `Int`     |
| SQLite      | `INTEGER` |
| CockroachDB | `INT`     |

#

- PostgreSQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 attribute | 참고                                     |
| -------------------------- | ------------------------------------ | ---------------------------------------- |
| `integer`                  | `int`, `int4`                        | `@db.Integer`                            |
| `smallint`                 | `int2`                               | `@db.SmallInt`                           |
| `smallserial`              | `serial2`                            | `@db.SmallInt @default(autoincrement())` |
| `serial`                   | `serial4`                            | `@db.Int @default(autoincrement())`      |
| `oid`                      | `@db.Oid`                            |

#

- MySQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                                                                                                                                                             |
| ---------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INT`                  | `@db.Int`                   |
| `INT UNSIGNED`         | `@db.UnsignedInt`           |
| `SMALLINT`             | `@db.SmallInt`              |
| `SMALLINT UNSIGNED`    | `@db.UnsignedSmallInt`      |
| `MEDIUMINT`            | `@db.MediumInt`             |
| `MEDIUMINT UNSIGNED`   | `@db.UnsignedMediumInt`     |
| `TINYINT`              | `@db.TinyInt`               | 최대 길이가 1보다 크면(예: `TINYINT(2)`) _또는_ 기본값이 `1`, `0`, `NULL` 이외의 값이면 `TINYINT`는 `Int`로 매핑됩니다. `TINYINT(1)`은 `Boolean`으로 매핑됩니다. |
| `TINYINT UNSIGNED`     | `@db.UnsignedTinyInt`       | `TINYINT(1) UNSIGNED`는 `Boolean`이 아니라 `Int`로 매핑됩니다                                                                                                    |
| `YEAR`                 | `@db.Year`                  |

#

- MongoDB

`Int`

| 기본 데이터베이스 타입 속성 | 참고 |
| --------------------------- | ---- |
| `@db.Int`                   |
| `@db.Long`                  |

#

- Microsoft SQL Server

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `int`                  | `@db.Int`                   |
| `smallint`             | `@db.SmallInt`              |
| `tinyint`              | `@db.TinyInt`               |
| `bit`                  | `@db.Bit`                   |

#

- SQLite

`INTEGER`

#

- CockroachDB

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                                 |
| ---------------------- | --------------------------- | ------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| `INTEGER`              | `INT`                       | `INT8`                               | `@db.Int8` | PostgreSQL과 다르다는 점에 유의하세요. PostgreSQL에서는 `integer`와 `int`가 `int4`의 별칭이며 `@db.Integer`로 매핑됩니다 |
| `INT4`                 | `@db.Int4`                  |
| `INT2`                 | `SMALLINT`                  | `@db.Int2`                           |
| `SMALLSERIAL`          | `SERIAL2`                   | `@db.Int2 @default(autoincrement())` |
| `SERIAL`               | `SERIAL4`                   | `@db.Int4 @default(autoincrement())` |
| `SERIAL8`              | `BIGSERIAL`                 | `@db.Int8 @default(autoincrement())` |

#

- Clients

## Prisma Client JS

`number`

- `BigInt`

#

- Default type mappings

| 커넥터      | 기본 매핑 |
| ----------- | --------- |
| PostgreSQL  | `bigint`  |
| SQL Server  | `int`     |
| MySQL       | `BIGINT`  |
| MongoDB     | `Long`    |
| SQLite      | `INTEGER` |
| CockroachDB | `INTEGER` |

#

- PostgreSQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                                   |
| ---------------------- | --------------------------- | -------------------------------------- |
| `bigint`               | `int8`                      | `@db.BigInt`                           |
| `bigserial`            | `serial8`                   | `@db.BigInt @default(autoincrement())` |

#

- MySQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성                    | 참고 |
| ---------------------- | ---------------------------------------------- | ---- |
| `BIGINT`               | `@db.BigInt`                                   |
| `SERIAL`               | `@db.UnsignedBigInt @default(autoincrement())` |

#

- MongoDB

`Long`

#

- Microsoft SQL Server

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `bigint`               | `@db.BigInt`                |

#

- SQLite

`INTEGER`

#

- CockroachDB

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                                 |
| ---------------------- | --------------------------- | ------------------------------------ | ---------- | ----------------------------------------------------------------------------------- |
| `BIGINT`               | `INT`                       | `INT8`                               | `@db.Int8` | PostgreSQL과 다르다는 점에 유의하세요. PostgreSQL에서는 `int`가 `int4`의 별칭입니다 |
| `bigserial`            | `serial8`                   | `@db.Int8 @default(autoincrement())` |

#

- Clients

| 클라이언트       | 타입                                                                                                | 설명                                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Prisma Client JS | [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) | [`BigInt` 작업 예시](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types#working-with-bigint) 참조 |

- `Float`

부동소수점 숫자.

#

- Default type mappings

| 커넥터      | 기본 매핑          |
| ----------- | ------------------ |
| PostgreSQL  | `double precision` |
| SQL Server  | `float(53)`        |
| MySQL       | `DOUBLE`           |
| MongoDB     | `Double`           |
| SQLite      | `REAL`             |
| CockroachDB | `DOUBLE PRECISION` |

#

- PostgreSQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `double precision`     | `@db.DoublePrecision`       |
| `real`                 | `@db.Real`                  |

#

- MySQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `FLOAT`                | `@db.Float`                 |
| `DOUBLE`               | `@db.Double`                |

#

- MongoDB

`Double`

#

- Microsoft SQL Server

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 |
| ---------------------- | --------------------------- |
| `float`                | `@db.Float`                 |
| `money`                | `@db.Money`                 |
| `smallmoney`           | `@db.SmallMoney`            |
| `real`                 | `@db.Real`                  |

#

- SQLite connector

`REAL`

#

- CockroachDB

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고         |
| ---------------------- | --------------------------- | ------------ | ------------ |
| `DOUBLE PRECISION`     | `FLOAT8`                    | `@db.Float8` |
| `REAL`                 | `FLOAT4`                    | `FLOAT`      | `@db.Float4` |

#

- Clients

## Prisma Client JS

`number`

- `Decimal`

#

- Default type mappings

| 커넥터      | 기본 매핑                                                      |
| ----------- | -------------------------------------------------------------- |
| PostgreSQL  | `decimal(65,30)`                                               |
| SQL Server  | `decimal(32,16)`                                               |
| MySQL       | `DECIMAL(65,30)`                                               |
| MongoDB     | [지원되지 않음](https://github.com/prisma/prisma/issues/12637) |
| SQLite      | `DECIMAL`                                                      |
| CockroachDB | `DECIMAL`                                                      |

#

- PostgreSQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                 |
| ---------------------- | --------------------------- | -------------------- |
| `decimal`              | `numeric`                   | `@db.Decimal(p, s)`† |
| `money`                | `@db.Money`                 |

- † `p` (precision): 저장할 수 있는 10진수 전체 자릿수의 최대값. `s` (scale): 소수점 오른쪽에 저장되는 10진수 자릿수.

#

- MySQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                 |
| ---------------------- | --------------------------- | -------------------- |
| `DECIMAL`              | `NUMERIC`                   | `@db.Decimal(p, s)`† |

- † `p` (precision): 저장할 수 있는 10진수 전체 자릿수의 최대값. `s` (scale): 소수점 오른쪽에 저장되는 10진수 자릿수.

#

- MongoDB

[지원되지 않음](https://github.com/prisma/prisma/issues/12637).

#

- Microsoft SQL Server

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                 |
| ---------------------- | --------------------------- | -------------------- |
| `decimal`              | `numeric`                   | `@db.Decimal(p, s)`† |

- † `p` (precision): 저장할 수 있는 10진수 전체 자릿수의 최대값. `s` (scale): 소수점 오른쪽에 저장되는 10진수 자릿수.

#

- SQLite

`DECIMAL` (`2.17.0`에서 `REAL`에서 변경)

#

- CockroachDB

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고                                                               |
| ---------------------- | --------------------------- | ------------------------------------------------------------------ | -------------------- |
| `DECIMAL`              | `DEC`                       | `NUMERIC`                                                          | `@db.Decimal(p, s)`† |
| `money`                | 아직 미지원                 | PostgreSQL의 `money` 타입은 CockroachDB에서 아직 지원되지 않습니다 |

- † `p` (precision): 저장할 수 있는 10진수 전체 자릿수의 최대값. `s` (scale): 소수점 오른쪽에 저장되는 10진수 자릿수.

#

- Clients

| 클라이언트       | 타입                                               | 설명                                                                                                                    |
| ---------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Prisma Client JS | [`Decimal`](https://mikemcl.github.io/decimal.js/) | [`Decimal` 작업 예시](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types#working-with-decimal) 참조 |

- `DateTime`

#

- Remarks
  - Prisma Client는 모든 `DateTime`을 기본 [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) 객체로 반환합니다.
  - 현재 Prisma ORM은 MySQL의 [zero dates](https://dev.mysql.com/doc/refman/8.3/en/date-and-time-types.html#:~:text=The%20following%20table%20shows%20the%20format%20of%20the%20%E2%80%9Czero%E2%80%9D%20value%20for%20each%20type) (`0000-00-00 00:00:00`, `0000-00-00`, `00:00:00`)를 [지원하지 않습니다](https://github.com/prisma/prisma/issues/5006).
  - 현재 `DateTime` 값을 문자열로 전달할 수 없고, 그렇게 하면 런타임 오류가 발생하는 [버그](https://github.com/prisma/prisma/issues/9516)가 있습니다. `DateTime` 값은 문자열(`'2024-12-04'`)이 아니라 [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) 객체(예: `new Date('2024-12-04')`)로 전달해야 합니다.

이 섹션에서 더 많은 정보와 예시를 확인할 수 있습니다: [`DateTime` 작업](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types#working-with-datetime).

#

- Default type mappings

| 커넥터      | 기본 매핑      |
| ----------- | -------------- |
| PostgreSQL  | `timestamp(3)` |
| SQL Server  | `datetime2`    |
| MySQL       | `DATETIME(3)`  |
| MongoDB     | `Timestamp`    |
| SQLite      | `NUMERIC`      |
| CockroachDB | `TIMESTAMP`    |

#

- PostgreSQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `timestamp(x)`         | `@db.Timestamp(x)`          |
| `timestamptz(x)`       | `@db.Timestamptz(x)`        |
| `date`                 | `@db.Date`                  |
| `time(x)`              | `@db.Time(x)`               |
| `timetz(x)`            | `@db.Timetz(x)`             |

#

- MySQL

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `DATETIME(x)`          | `@db.DateTime(x)`           |
| `DATE(x)`              | `@db.Date(x)`               |
| `TIME(x)`              | `@db.Time(x)`               |
| `TIMESTAMP(x)`         | `@db.Timestamp(x)`          |

`Int`와 함께 MySQL의 `YEAR` 타입도 사용할 수 있습니다:

```
    yearField     Int    @db.Year
```

#

- MongoDB

`Timestamp`

#

- Microsoft SQL Server

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `date`                 | `@db.Date`                  |
| `time`                 | `@db.Time`                  |
| `datetime`             | `@db.DateTime`              |
| `datetime2`            | `@db.DateTime2`             |
| `smalldatetime`        | `@db.SmallDateTime`         |
| `datetimeoffset`       | `@db.DateTimeOffset`        |

#

- SQLite

`NUMERIC` 또는 `STRING`. 기본 데이터 타입이 `STRING`인 경우, 다음 형식 중 하나를 사용해야 합니다:

- [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) (`1996-12-19T16:39:57-08:00`)
- [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) (`Tue, 1 Jul 2003 10:52:37 +0200`)

#

- CockroachDB

| 기본 데이터베이스 타입 | 기본 데이터베이스 타입 속성 | 참고 |
| ---------------------- | --------------------------- | ---- |
| `TIMESTAMP(x)`         | `@db.Timestamp(x)`          |
| `TIMESTAMPTZ(x)`       | `@db.Timestamptz(x)`        |
| `DATE`                 | `@db.Date`                  |
| `TIME(x)`              | `@db.Time(x)`               |
| `TIMETZ(x)`            | `@db.Timetz(x)`             |

#

- Clients

## Prisma Client JS

`Date`

- `Json`

JSON 객체입니다.

#

- 기본 타입 매핑

| 커넥터      | 기본 매핑                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| PostgreSQL  | `jsonb`                                                                                                  |
| SQL Server  | [지원되지 않음](https://github.com/prisma/prisma/issues/7417)                                            |
| MySQL       | `JSON`                                                                                                   |
| MongoDB     | [유효한 `BSON` 객체(Relaxed mode)](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) |
| SQLite      | `JSONB`                                                                                                  |
| CockroachDB | `JSONB`                                                                                                  |

#

- PostgreSQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 | 참고 |
| -------------------------- | ------------------------------- | ---- |
| `json`                     | `@db.Json`                      |
| `jsonb`                    | `@db.JsonB`                     |

#

- MySQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 | 참고 |
| -------------------------- | ------------------------------- | ---- |
| `JSON`                     | `@db.Json`                      |

#

- MongoDB

[유효한 `BSON` 객체(Relaxed mode)](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/)

#

- Microsoft SQL Server

Microsoft SQL Server에는 JSON 전용 데이터 타입이 없습니다. 하지만 [JSON을 읽고 수정하기 위한 내장 함수](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15#extract-values-from-json-text-and-use-them-in-queries)가 다수 제공됩니다.

#

- SQLite

지원되지 않음

#

- CockroachDB

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 | 참고        |
| -------------------------- | ------------------------------- | ----------- |
| `JSON`                     | `JSONB`                         | `@db.JsonB` |

#

- 클라이언트

## Prisma Client JS

`object`

- `Bytes`

#

- 기본 타입 매핑

| 커넥터      | 기본 매핑   |
| ----------- | ----------- |
| PostgreSQL  | `bytea`     |
| SQL Server  | `varbinary` |
| MySQL       | `LONGBLOB`  |
| MongoDB     | `BinData`   |
| SQLite      | `BLOB`      |
| CockroachDB | `BYTES`     |

#

- PostgreSQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 |
| -------------------------- | ------------------------------- |
| `bytea`                    | `@db.ByteA`                     |

#

- MySQL

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 | 참고 |
| -------------------------- | ------------------------------- | ---- |
| `LONGBLOB`                 | `@db.LongBlob`                  |
| `BINARY`                   | `@db.Binary`                    |
| `VARBINARY`                | `@db.VarBinary`                 |
| `TINYBLOB`                 | `@db.TinyBlob`                  |
| `BLOB`                     | `@db.Blob`                      |
| `MEDIUMBLOB`               | `@db.MediumBlob`                |
| `BIT`                      | `@db.Bit`                       |

#

- MongoDB

`BinData`

| 네이티브 데이터베이스 타입 속성 | 참고                                                               |
| ------------------------------- | ------------------------------------------------------------------ |
| `@db.ObjectId`                  | 기본 BSON 타입이 `OBJECT_ID`인 경우 필수(ID 필드, relation scalar) |
| `@db.BinData`                   |

#

- Microsoft SQL Server

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 | 참고 |
| -------------------------- | ------------------------------- | ---- |
| `binary`                   | `@db.Binary`                    |
| `varbinary`                | `@db.VarBinary`                 |
| `image`                    | `@db.Image`                     |

#

- SQLite

`BLOB`

#

- CockroachDB

| 네이티브 데이터베이스 타입 | 네이티브 데이터베이스 타입 속성 |
| -------------------------- | ------------------------------- | ------ | ----------- |
| `BYTES`                    | `BYTEA`                         | `BLOB` | `@db.Bytes` |

#

- 클라이언트

| 클라이언트                                                                             | 타입                                                                                                        | 설명                                                                                                                |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Prisma Client JS                                                                       | [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | [`Bytes` 작업 예시](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types#working-with-bytes) 참고 |
| Prisma Client JS ([v6 이전](https://docs.prisma.io/docs/guides/upgrade-prisma-orm/v6)) | [`Buffer`](https://nodejs.org/api/buffer.html)                                                              | [`Bytes` 작업 예시](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types#working-with-bytes) 참고 |

- `Unsupported`

**MongoDB에서는 지원되지 않음**
[MongoDB connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)는 `Unsupported` 타입을 지원하지 않습니다.

`Unsupported` 타입은 [2.17.0](https://github.com/prisma/prisma/releases/tag/2.17.0)에서 도입되었으며, Prisma Client가 지원하지 않는 데이터 타입을 Prisma 스키마에서 표현할 수 있게 해줍니다. `Unsupported` 타입 필드는 `prisma db pull`로 Introspection 시 생성되거나 수동으로 작성할 수 있으며, Prisma Migrate 또는 `db push`로 데이터베이스에 생성할 수 있습니다.

#

- 비고
  - `Unsupported` 타입 필드는 생성된 클라이언트에서 사용할 수 없습니다.

  - 모델에 **필수(required)** `Unsupported` 타입이 포함된 경우, Prisma Client에서 `prisma.model.create(..)`, `prisma.model.update(...)`, `prisma.model.upsert(...)`를 사용할 수 없습니다.

  - 지원되지 않는 타입이 포함된 데이터베이스를 introspect하면, Prisma ORM은 다음 경고를 제공합니다:

```
*** WARNING ***

        These fields are not supported by Prisma Client, because Prisma does not currently support their types.
        * Model "Post", field: "circle", original data type: "circle"
```

#

- 예시

```
    model Star {
      id       Int                    @id @default(autoincrement())
      position Unsupported("circle")?
      example1 Unsupported("circle")
      circle   Unsupported("circle")? @default(dbgenerated("'<(10,4),11>'::circle"))
    }
```

## `model` 필드 타입 수정자

### `[]` 수정자

필드를 리스트로 만듭니다.

#

- 비고
  - optional일 수 없습니다(예: `Post[]?`).

#

- 관계형 데이터베이스
  - 스칼라 리스트(배열)는 데이터베이스가 이를 네이티브로 지원하는 경우에만 데이터 모델에서 지원됩니다. 따라서 현재는 PostgreSQL 또는 CockroachDB를 사용할 때만 스칼라 리스트가 지원됩니다(MySQL과 SQLite는 스칼라 리스트를 네이티브로 지원하지 않음).

#

- MongoDB
  - 스칼라 리스트가 지원됩니다.

#

- 예시

#

- 스칼라 리스트 정의

관계형 데이터베이스

MongoDB

```
    model User {
      id             Int      @id @default(autoincrement())
      favoriteColors String[]
    }
```

#

- 기본값이 있는 스칼라 리스트 정의

관계형 데이터베이스

MongoDB

```
    model User {
      id             Int      @id @default(autoincrement())
      favoriteColors String[] @default(["red", "blue", "green"])
    }
```

- `?` 수정자

필드를 optional로 만듭니다.

#

- 비고
  - 리스트 필드와 함께 사용할 수 없습니다(예: `Posts[]`)

#

- 예시

#

- optional `name` 필드

```
    model User {
      id   Int     @id @default(autoincrement())
      name String?
    }
```

## 속성(Attributes)

속성은 [필드](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields) 또는 블록(예: [models](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model))의 동작을 수정합니다. 데이터 모델에 속성을 추가하는 방법은 두 가지입니다.

- _Field_ 속성은 `@`로 시작합니다.
- _Block_ 속성은 `@@`로 시작합니다.

일부 속성은 인자를 받습니다. 속성의 인자는 항상 이름이 지정되지만, 대부분의 경우 인자 _이름_ 은 생략할 수 있습니다.

> **참고** : 시그니처에서 앞에 오는 밑줄은 _인자 이름_ 을 생략할 수 있음을 의미합니다.

- `@id`

모델에서 단일 필드 ID를 정의합니다.

#

- 비고

#

- 일반
  - relation 필드에는 정의할 수 없습니다.
  - optional일 수 없습니다.

#

- 관계형 데이터베이스
  - 해당 데이터베이스 구성 요소: `PRIMARY KEY`

  - ID를 자동 생성하는 [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)를 사용하는 [`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default) 속성으로 주석 처리할 수 있습니다.
    - `autoincrement()`
    - `cuid()`
    - `uuid()`
    - `ulid()`

  - 모든 스칼라 필드(`String`, `Int`, `enum`)에 정의할 수 있습니다.

#

- MongoDB
  - 해당 데이터베이스 구성 요소: [배열을 제외한 모든 유효한 BSON 타입](https://www.mongodb.com/docs/manual/core/document/#the-_id-field)

  - 모든 모델은 `@id` 필드를 정의해야 합니다.

  - [기본 ID 필드 이름은 항상 `_id`](https://www.mongodb.com/docs/manual/core/document/#the-_id-field)이며, `@map("_id")`로 매핑해야 합니다.

  - 데이터베이스에서 `ObjectId`를 사용하려는 경우를 제외하면 모든 스칼라 필드(`String`, `Int`, `enum`)에 정의할 수 있습니다.

  - ID로 [`ObjectId`](https://www.mongodb.com/docs/manual/reference/method/ObjectId/)를 사용하려면 다음이 필요합니다.
    - `String` 또는 `Bytes` 필드 타입 사용

    - 필드에 `@db.ObjectId` 주석 추가:

```
id   String  @db.ObjectId  @map("_id")
```

    * 선택적으로, `ObjectId`를 자동 생성하는 [the `auto()` function](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#auto)을 사용하는 [`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default) 속성을 필드에 추가

```
id   String  @db.ObjectId  @map("_id") @default(auto())
```

- [`cuid()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#cuid), [`uuid()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#uuid), [`ulid()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#ulid)는 지원되지만 유효한 `ObjectId`를 생성하지 않습니다. `@id`에는 대신 `auto()`를 사용하세요.

- `autoincrement()`는 **지원되지 않음**

#

- 인자

| 이름  | 필수       | 타입     | 설명                                              |
| ----- | ---------- | -------- | ------------------------------------------------- |
| `map` | **아니요** | `String` | 데이터베이스의 기본 기본 키 제약 조건 이름입니다. |

MySQL 또는 MongoDB에서는 지원되지 않습니다.
`length`| **아니요**| `number`| 인덱싱할 값의 하위 부분(subpart)에 대한 최대 길이를 지정할 수 있습니다.

MySQL 전용.
`sort`| **아니요**| `String`| 데이터베이스에 ID 항목을 어떤 순서로 저장할지 지정할 수 있습니다. 사용 가능한 옵션은 `Asc` 및 `Desc`입니다.

SQL Server 전용.
`clustered`| **아니요**| `Boolean`| ID를 clustered 또는 non-clustered로 정의합니다. 기본값은 `true`입니다.

SQL Server 전용.

#

- 시그니처

```
    @id(map: String?, length: number?, sort: String?, clustered: Boolean?)
```

#

- 예시

대부분의 경우 데이터베이스가 ID를 생성하도록 하는 것이 좋습니다. 이를 위해 ID 필드에 `@default` 속성을 주석 처리하고 [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)로 필드를 초기화하세요.

#

- ID로 자동 증가 정수 생성하기 (관계형 데이터베이스 전용)

```
    model User {
      id   Int    @id @default(autoincrement())
      name String
    }
```

#

- ID로 `ObjectId` 생성하기 (MongoDB 전용)

```
    model User {
      id   String @id @default(auto()) @map("_id") @db.ObjectId
      name String
    }
```

#

- ID로 `cuid()` 값 생성하기

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(cuid())
      name String
    }
```

`id` 필드 타입이 `ObjectId`인 경우 기본값 생성에 `cuid()`를 사용할 수 없습니다. 유효한 `ObjectId`를 생성하려면 다음 구문을 사용하세요:

```
    id    String  @id @default(auto()) @db.ObjectId @map("_id")
```

#

- ID로 `uuid()` 값 생성하기

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(uuid())
      name String
    }
```

`id` 필드 타입이 `ObjectId`인 경우 기본값 생성에 `uuid()`를 사용할 수 없습니다. 유효한 `ObjectId`를 생성하려면 다음 구문을 사용하세요:

```
    id    String  @id @default(auto()) @db.ObjectId @map("_id")
```

#

- ID로 `ulid()` 값 생성하기

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(ulid())
      name String
    }
```

`id` 필드 타입이 `ObjectId`인 경우 기본값 생성에 `ulid()`를 사용할 수 없습니다. 유효한 `ObjectId`를 생성하려면 다음 구문을 사용하세요:

```
    id    String  @id @default(auto()) @db.ObjectId @map("_id")
```

#

- 기본값이 _없는_ 단일 필드 ID

다음 예시에서 `id`에는 기본값이 없습니다:

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id
      name String
    }
```

```
    model User {
    id    String   @id  @map("_id")
    name  String
    }
```

위 경우에는 Prisma Client를 사용해 `User` 모델의 새 레코드를 생성할 때 _반드시_ 직접 ID 값을 제공해야 합니다. 예:

```
    const newUser = await prisma.user.create({
      data: {
        id: 1,
        name: "Alice",
      },
    });
```

#

- 기본값 없이 relation scalar 필드에 ID 지정하기

다음 예시에서 `authorId`는 relation scalar이면서 동시에 `Profile`의 ID입니다:

관계형 데이터베이스

MongoDB

```
    model Profile {
      authorId Int    @id
      author   User   @relation(fields: [authorId], references: [id])
      bio      String
    }

    model User {
      id      Int      @id
      email   String   @unique
      name    String?
      profile Profile?
    }
```

이 시나리오에서는 `Profile`만 단독으로 생성할 수 없습니다. Prisma Client의 [nested writes](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes)를 사용해 `User`를 생성하거나, 프로필을 기존 사용자에 연결해야 합니다.

다음 예시는 사용자와 프로필을 생성합니다:

```
    const userWithProfile = await prisma.user.create({
      data: {
        id: 3,
        email: "bob@prisma.io",
        name: "Bob Prismo",
        profile: {
          create: {
            bio: "Hello, I'm Bob Prismo and I love apples, blue nail varnish, and the sound of buzzing mosquitoes.",
          },
        },
      },
    });
```

다음 예시는 새 프로필을 사용자에 연결합니다:

```
    const profileWithUser = await prisma.profile.create({
      data: {
        bio: "Hello, I'm Bob and I like nothing at all. Just nothing.",
        author: {
          connect: {
            id: 22,
          },
        },
      },
    });
```

- `@@id`

**MongoDB에서는 지원되지 않음**
[MongoDB connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)는 복합 ID를 지원하지 않습니다.

모델에 다중 필드 ID(복합 ID)를 정의합니다.

#

- 비고
  - 대응되는 데이터베이스 타입: `PRIMARY KEY`
  - [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions)를 사용해 ID를 자동 생성하는 [`@default`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default) 속성으로 주석을 달 수 있습니다.
  - optional일 수 없습니다.
  - 모든 scalar 필드(`String`, `Int`, `enum`)에 정의할 수 있습니다.
  - relation 필드에는 정의할 수 없습니다.
  - Prisma Client에서 복합 ID 필드 이름은 다음 패턴을 따릅니다: `field1_field2_field3`

#

- 인수

| Name     | Required | Type               | Description                                                                                                                                |
| -------- | -------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `fields` | **Yes**  | `FieldReference[]` | 필드 이름 목록 - 예: `["firstname", "lastname"]`                                                                                           |
| `name`   | **No**   | `String`           | 모든 필드를 포괄하는 인수에 대해 Prisma Client가 노출할 이름입니다. 예: `fullName: { firstName: "First", lastName: "Last"}`에서 `fullName` |
| `map`    | **No**   | `String`           | 데이터베이스의 기본 기본 키 제약 조건 이름입니다.                                                                                          |

MySQL에서는 지원되지 않습니다.
`length`| **No**| `number`| 인덱싱할 값의 하위 부분(subpart)에 대한 최대 길이를 지정할 수 있습니다.

MySQL 전용.
`sort`| **No**| `String`| 데이터베이스에 ID 항목을 어떤 순서로 저장할지 지정할 수 있습니다. 사용 가능한 옵션은 `Asc` 및 `Desc`입니다.

SQL Server 전용.
`clustered`| **No**| `Boolean`| ID가 clustered인지 non-clustered인지 정의합니다. 기본값은 `true`입니다.

SQL Server 전용.

`@@id` 속성의 `fields` 인수 이름은 생략할 수 있습니다:

```
    @@id(fields: [title, author])
    @@id([title, author])
```

#

- 시그니처

```
    @@id(_ fields: FieldReference[], name: String?, map: String?)
```

#

- 예시

#

- 두 개의 `String` 필드에 다중 필드 ID 지정하기 (관계형 데이터베이스 전용)

```
    model User {
      firstName String
      lastName  String
      email     String  @unique
      isAdmin   Boolean @default(false)

      @@id([firstName, lastName])
    }
```

사용자를 생성할 때 `firstName`과 `lastName`의 고유한 조합을 제공해야 합니다:

```
    const user = await prisma.user.create({
      data: {
        firstName: "Alice",
        lastName: "Smith",
      },
    });
```

사용자를 조회하려면 생성된 복합 ID 필드(`firstName_lastName`)를 사용하세요:

```
    const user = await prisma.user.findUnique({
      where: {
        firstName_lastName: {
          firstName: "Alice",
          lastName: "Smith",
        },
      },
    });
```

#

- 두 개의 `String` 필드와 하나의 `Boolean` 필드에 다중 필드 ID 지정하기 (관계형 데이터베이스 전용)

```
    model User {
      firstName String
      lastName  String
      email     String  @unique
      isAdmin   Boolean @default(false)

      @@id([firstName, lastName, isAdmin])
    }
```

이제 새 `User` 레코드를 생성할 때 `firstName`, `lastName`, `isAdmin` 값의 고유한 조합을 제공해야 합니다:

```
    const user = await prisma.user.create({
      data: {
        firstName: "Alice",
        lastName: "Smith",
        isAdmin: true,
      },
    });
```

#

- relation 필드를 포함하는 다중 필드 ID 지정하기 (관계형 데이터베이스 전용)

```
    model Post {
      title     String
      published Boolean @default(false)
      author    User    @relation(fields: [authorId], references: [id])
      authorId  Int

      @@id([authorId, title])
    }

    model User {
      id    Int     @default(autoincrement())
      email String  @unique
      name  String?
      posts Post[]
    }
```

이제 새 `Post` 레코드를 생성할 때 `authorId`(외래 키)와 `title` 값의 고유한 조합을 제공해야 합니다:

```
    const post = await prisma.post.create({
      data: {
        title: "Hello World",
        author: {
          connect: {
            email: "alice@prisma.io",
          },
        },
      },
    });
```

- `@default`

[필드의 기본값](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-default-value)을 정의합니다.

#

- 비고
  - Prisma 스키마에서 아직 표현할 수 없는 기본값은 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection)을 사용할 때 [`dbgenerated()` 함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#dbgenerated)로 표현됩니다.
  - Prisma 스키마에서는 relation 필드에 기본값을 허용하지 않습니다. 다만 relation을 뒷받침하는 필드(`@relation` 속성의 `fields` 인수에 나열된 필드)에는 기본값을 정의할 수 있습니다. relation을 뒷받침하는 필드의 기본값은 해당 relation이 자동으로 채워진다는 의미입니다.
  - 기본값은 이를 네이티브로 지원하는 데이터베이스에서 [scalar lists](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays)와 함께 사용할 수 있습니다.

#

- 관계형 데이터베이스
  - 대응되는 데이터베이스 구성 요소: `DEFAULT`
  - 기본값은 정적 값(`4`, `"hello"`)이거나 다음 [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions) 중 하나일 수 있습니다:
    - `autoincrement()`
    - [`sequence()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#sequence) (CockroachDB 전용)
    - `dbgenerated(...)`
    - `cuid()`
    - `cuid(2)`
    - `uuid()`
    - `uuid(4)`
    - `uuid(7)`
    - `ulid()`
    - `nanoid()`
    - `now()`
  - Prisma 스키마에서 아직 표현할 수 없는 기본값은 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection)을 사용할 때 [`dbgenerated(...)` 함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#dbgenerated)로 표현됩니다.
  - Prisma 스키마에서는 relation 필드에 기본값을 허용하지 않습니다. 다만 relation을 뒷받침하는 필드(`@relation` 속성의 `fields` 인수에 나열된 필드)에는 기본값을 정의할 수 있습니다. relation을 뒷받침하는 필드의 기본값은 해당 relation이 자동으로 채워진다는 의미입니다.
  - 기본값은 이를 네이티브로 지원하는 데이터베이스에서 [scalar lists](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays)와 함께 사용할 수 있습니다.
  - JSON 데이터. JSON은 `@default` 속성 안에서 반드시 큰따옴표로 감싸야 합니다. 예: `@default("[]")`. JSON 객체를 제공하려면 큰따옴표로 감싼 다음 내부 큰따옴표를 백슬래시로 이스케이프해야 합니다. 예: `@default("{ \"hello\": \"world\" }")`.

#

- MongoDB
  - 기본값은 정적 값(`4`, `"hello"`)이거나 다음 [함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#attribute-functions) 중 하나일 수 있습니다:
    - [`auto()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#auto) (`@db.ObjectId`와 함께 사용할 때만 MongoDB에서 `ObjectId` 생성 가능)
    - `cuid()`
    - `uuid()`
    - `ulid()`
    - `now()`

#

- 인수

| Name    | Required | Type                              | Description          |
| ------- | -------- | --------------------------------- | -------------------- |
| `value` | **Yes**  | 표현식 (예: `5`, `true`, `now()`) |
| `map`   | **No**   | String                            | **SQL Server 전용.** |

`@default` 속성의 `value` 인수 이름은 생략할 수 있습니다:

```
    id Int @id @default(value: autoincrement())
    id Int @id @default(autoincrement())
```

#

- 시그니처

```
    @default(_ value: Expression, map: String?)
```

#

- 예시

#

- `Int`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email        String @unique
      profileViews Int    @default(0)
    }
```

#

- `Float`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email  String @unique
      number Float  @default(1.1)
    }
```

#

- `Decimal`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email  String  @unique
      number Decimal @default(22.99)
    }
```

#

- `BigInt`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email  String @unique
      number BigInt @default(34534535435353)
    }
```

#

- `String`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email String @unique
      name  String @default("")
    }
```

#

- `Boolean`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email   String  @unique
      isAdmin Boolean @default(false)
    }
```

#

- `DateTime`의 기본값

`DateTime`의 정적 기본값은 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 표준을 기반으로 한다는 점에 유의하세요.

관계형 데이터베이스

MongoDB

```
    model User {
      email String   @unique
      data  DateTime @default("2020-03-19T14:21:00+02:00")
    }
```

#

- `Bytes`의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      email  String @unique
      secret Bytes  @default("SGVsbG8gd29ybGQ=")
    }
```

#

- `enum`의 기본값](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#default-value-for-an-enum)

관계형 데이터베이스

```
    enum Role {
      USER
      ADMIN
    }
```

```
    model User {
      id      Int      @id @default(autoincrement())
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

MongoDB

```
    enum Role {
      USER
      ADMIN
    }
```

```
    model User {
      id      String   @id @default(auto()) @map("_id") @db.ObjectId
      email   String   @unique
      name    String?
      role    Role     @default(USER)
      posts   Post[]
      profile Profile?
    }
```

#

- 스칼라 리스트의 기본값

관계형 데이터베이스

MongoDB

```
    model User {
      id             Int      @id @default(autoincrement())
      posts          Post[]
      favoriteColors String[] @default(["red", "yellow", "purple"])
      roles          Role[]   @default([USER, DEVELOPER])
    }

    enum Role {
      USER
      DEVELOPER
      ADMIN
    }
```

- `@unique`

이 필드에 대한 고유 제약 조건을 정의합니다.

#

- 비고

#

- 일반
  - `@unique`가 주석 처리된 필드는 optional 또는 required일 수 있습니다.
  - `@unique`가 주석 처리된 필드가 `@id` / `@@id`가 없는 모델에서 유일한 고유 제약 조건을 나타내는 경우, 해당 필드는 _반드시_ required여야 합니다.
  - 모델에는 원하는 수만큼 고유 제약 조건을 가질 수 있습니다.
  - 모든 스칼라 필드에 정의할 수 있습니다.
  - 관계 필드에는 정의할 수 **없습니다**.

#

- 관계형 데이터베이스
  - 해당 데이터베이스 구성 요소: `UNIQUE`
  - `NULL` 값은 서로 다른 값으로 간주됩니다(동일한 컬럼에서 `NULL` 값을 가진 여러 행이 허용됨).
  - 고유 제약 조건을 추가하면 지정한 컬럼에 해당하는 *고유 인덱스*가 자동으로 추가됩니다.

#

- MongoDB
  - [MongoDB의 고유 인덱스](https://www.mongodb.com/docs/manual/core/index-unique/)로 강제됩니다.

#

- 인수

| Name     | Required | Type     | Description                                                    |
| -------- | -------- | -------- | -------------------------------------------------------------- |
| `map`    | **No**   | `String` |
| `length` | **No**   | `number` | 인덱싱할 값의 하위 부분에 대한 최대 길이를 지정할 수 있습니다. |

MySQL 전용.
`sort`| **No**| `String`| 제약 조건 항목이 데이터베이스에 어떤 순서로 저장될지 지정할 수 있습니다. 사용 가능한 옵션은 `Asc` 및 `Desc`입니다.
`clustered`| **No**| `Boolean`| 제약 조건이 clustered인지 non-clustered인지 정의합니다. 기본값은 `false`입니다.

SQL Server 전용.
`where`| **No**| `function` or `object`| 지정된 조건과 일치하는 행만 포함하는 [부분 인덱스](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)를 정의합니다. `raw("SQL expression")` 또는 `{ field: value }` 같은 객체 리터럴을 허용합니다.

PostgreSQL, SQLite, SQL Server, CockroachDB에서 지원됩니다. `partialIndexes` Preview 기능이 필요합니다.

- ¹ 일부 인덱스 및 필드 유형에서는 필수일 수 있습니다.

#

- 시그니처

```
    @unique(map: String?, length: number?, sort: String?, clustered: Boolean?, where: raw(String) | { field: value }?)
```

> **참고** : `where` 인수는 raw SQL 조건식을 위한 `raw("SQL expression")` 또는 타입 안전 조건을 위한 `{ field: value }` 객체 리터럴을 허용합니다. 자세한 내용은 [부분 인덱스 구성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)을 참조하세요.

> **참고** : `partialIndexes` Preview 기능 이전에는 시그니처가 다음과 같았습니다:

```
>     @unique(map: String?, length: number?, sort: String?, clustered: Boolean?)
```

#

- 예시

#

- required `String` 필드에 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model User {
      email String @unique
      name  String
    }
```

#

- optional `String` 필드에 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model User {
      id    Int     @id @default(autoincrement())
      email String? @unique
      name  String
    }
```

#

- 관계 스칼라 필드 `authorId`에 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model Post {
      author    User    @relation(fields: [authorId], references: [id])
      authorId  Int     @unique
      title     String
      published Boolean @default(false)
    }

    model User {
      id    Int     @id @default(autoincrement())
      email String? @unique
      name  String
      Post  Post[]
    }
```

#

- `cuid()` 값을 기본값으로 사용하는 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model User {
      token String @unique @default(cuid())
      name  String
    }
```

- `@@unique`

지정된 필드에 대한 복합 [고유 제약 조건](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-unique-field)을 정의합니다.

#

- 비고

#

- 일반
  - 고유 제약 조건을 구성하는 모든 필드는 **반드시** mandatory 필드여야 합니다. 다음 모델은 `id`가 `null`일 수 있으므로 **유효하지 않습니다**:

```
model User {
          firstname Int
          lastname  Int
          id        Int?

          @@unique([firstname, lastname, id])
        }
```

이 동작의 이유는 모든 커넥터가 `null` 값을 서로 다른 값으로 간주하기 때문이며, 그 결과 겉보기에는 동일한 두 행도 고유한 것으로 간주됩니다:

```
firstname  | lastname | id
         -----------+----------+------
         John       | Smith    | null
         John       | Smith    | null
```

- 모델에는 원하는 수만큼 `@@unique` 블록을 가질 수 있습니다.

#

- 관계형 데이터베이스
  - 해당 데이터베이스 구성 요소: `UNIQUE`
  - `@id` / `@@id`가 없는 모델에서 `@@unique` 블록이 유일한 고유 제약 조건을 나타내는 경우 `@@unique` 블록이 필요합니다.
  - 고유 제약 조건을 추가하면 지정한 컬럼에 해당하는 *고유 인덱스*가 자동으로 추가됩니다.

#

- MongoDB
  - [MongoDB의 복합 인덱스](https://www.mongodb.com/docs/manual/core/index-compound/)로 강제됩니다.
  - `@@unique` 블록은 모델의 유일한 고유 식별자로 사용할 수 없습니다. MongoDB는 `@id` 필드를 요구합니다.

#

- 인수

| Name     | Required | Type               | Description                                                                                            |
| -------- | -------- | ------------------ | ------------------------------------------------------------------------------------------------------ |
| `fields` | **Yes**  | `FieldReference[]` | 필드 이름 목록입니다. 예: `["firstname", "lastname"]`. 필드는 mandatory여야 합니다. 비고를 참조하세요. |
| `name`   | **No**   | `String`           | 필드 조합의 고유 이름입니다. 기본값은 `fieldName1_fieldName2_fieldName3`입니다.                        |
| `map`    | **No**   | `String`           |
| `length` | **No**   | `number`           | 인덱싱할 값의 하위 부분에 대한 최대 길이를 지정할 수 있습니다.                                         |

MySQL 전용.
`sort`| **No**| `String`| 제약 조건 항목이 데이터베이스에 어떤 순서로 저장될지 지정할 수 있습니다. 사용 가능한 옵션은 `Asc` 및 `Desc`입니다.
`clustered`| **No**| `Boolean`| 제약 조건이 clustered인지 non-clustered인지 정의합니다. 기본값은 `false`입니다.

SQL Server 전용.
`where`| **No**| `function` or `object`| 지정된 조건과 일치하는 행만 포함하는 [부분 인덱스](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)를 정의합니다. `raw("SQL expression")` 또는 `{ field: value }` 같은 객체 리터럴을 허용합니다.

PostgreSQL, SQLite, SQL Server, CockroachDB에서 지원됩니다. `partialIndexes` Preview 기능이 필요합니다.

`@@unique` 속성의 `fields` 인수 이름은 생략할 수 있습니다:

```
    @@unique(fields: [title, author])
    @@unique([title, author])
    @@unique(fields: [title, author], name: "titleAuthor")
```

`length` 및 `sort` 인수는 해당 필드 이름에 추가됩니다:

```
    @@unique(fields: [title(length:10), author])
    @@unique([title(sort: Desc), author(sort: Asc)])
```

#

- 시그니처

>

```
>     @@unique(_ fields: FieldReference[], name: String?, map: String?, where: raw(String) | { field: value }?)
```

> **참고** : `where` 인수는 raw SQL 조건식을 위한 `raw("SQL expression")` 또는 타입 안전 조건을 위한 `{ field: value }` 객체 리터럴을 허용합니다. 자세한 내용은 [부분 인덱스 구성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)을 참조하세요.

> **참고** : `partialIndexes` Preview 기능 이전(그리고 `extendedIndexes` Preview 기능이 있는 버전 4.0.0 / 3.5.0 이전)에는 시그니처가 다음과 같았습니다:

```
>     @@unique(_ fields: FieldReference[], name: String?, map: String?)
```

#

- 예시

#

- 두 개의 `String` 필드에 다중 필드 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model User {
      id        Int     @default(autoincrement())
      firstName String
      lastName  String
      isAdmin   Boolean @default(false)

      @@unique([firstName, lastName])
    }
```

사용자를 조회하려면 생성된 필드 이름(`firstname_lastname`)을 사용하세요:

```
    const user = await prisma.user.findUnique({
      where: {
        firstName_lastName: {
          firstName: "Alice",
          lastName: "Smith",
          isAdmin: true,
        },
      },
    });
```

#

- 두 개의 `String` 필드와 하나의 `Boolean` 필드에 다중 필드 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model User {
      id        Int     @default(autoincrement())
      firstName String
      lastName  String
      isAdmin   Boolean @default(false)

      @@unique([firstName, lastName, isAdmin])
    }
```

#

- 관계 필드를 포함하는 다중 필드 고유 속성 지정

관계형 데이터베이스

MongoDB

```
    model Post {
      id        Int     @default(autoincrement())
      author    User    @relation(fields: [authorId], references: [id])
      authorId  Int
      title     String
      published Boolean @default(false)

      @@unique([authorId, title])
    }

    model User {
      id    Int    @id @default(autoincrement())
      email String @unique
      posts Post[]
    }
```

#

- 다중 필드 고유 속성에 사용자 지정 `name` 지정

관계형 데이터베이스

MongoDB

```
    model User {
      id        Int     @default(autoincrement())
      firstName String
      lastName  String
      isAdmin   Boolean @default(false)

      @@unique(fields: [firstName, lastName, isAdmin], name: "admin_identifier")
    }
```

사용자를 조회하려면 사용자 지정 필드 이름(`admin_identifier`)을 사용하세요:

```
    const user = await prisma.user.findUnique({
      where: {
        admin_identifier: {
          firstName: "Alice",
          lastName: "Smith",
          isAdmin: true,
        },
      },
    });
```

- `@@index`

데이터베이스의 인덱스를 정의합니다.

#

- 비고

#

- 관계형 데이터베이스
  - 해당 데이터베이스 구성 요소: `INDEX`
  - Prisma 스키마에서 아직 제공되지 않는 추가 인덱스 구성 옵션이 있습니다. 예:
    - PostgreSQL 및 CockroachDB:
      - 인덱스 필드를 식으로 정의(예: `CREATE INDEX title ON public."Post"((lower(title)) text_ops);`)
      - `CONCURRENTLY`를 사용해 인덱스를 동시 생성

Prisma 스키마에서 이러한 옵션을 구성할 수는 없지만, 데이터베이스 레벨에서 직접 구성할 수 있습니다.

#

- MongoDB

#

- 인수

| Name     | Required | Type               | Description                                                                                                                                                                                                      |
| -------- | -------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fields` | **Yes**  | `FieldReference[]` | 필드 이름 목록입니다. 예: `["firstname", "lastname"]`                                                                                                                                                            |
| `name`   | **No**   | `String`           | Prisma Client가 모든 필드를 포함하는 인수에 노출할 이름입니다. 예: `fullName: { firstName: "First", lastName: "Last"}`에서 `fullName`                                                                            |
| `map`    | **No**   | `map`              | 기본 데이터베이스에서의 인덱스 이름입니다(이름을 지정하지 않으면 Prisma가 식별자 길이 제한을 준수하는 인덱스 이름을 생성합니다. Prisma는 다음 네이밍 규칙을 사용합니다: `tablename.field1_field2_field3_unique`) |
| `length` | **No**   | `number`           | 인덱싱할 값의 하위 부분에 대한 최대 길이를 지정할 수 있습니다.                                                                                                                                                   |

MySQL 전용.

`sort`| **아니요**| `String`| 데이터베이스에서 인덱스 또는 제약 조건의 항목이 어떤 순서로 저장될지 지정할 수 있습니다. 사용 가능한 옵션은 `asc` 및 `desc`입니다.
`clustered`| **아니요**| `Boolean`| 인덱스가 클러스터형인지 비클러스터형인지 정의합니다. 기본값은 `false`입니다.

SQL Server 전용.
`type`| **아니요**| `identifier`| 인덱스 액세스 메서드를 지정할 수 있습니다. 기본값은 `BTree`입니다.

PostgreSQL 및 CockroachDB 전용.
`ops`| **아니요**| `identifier` 또는 `function`| 특정 인덱스 유형에 대한 인덱스 연산자를 정의할 수 있습니다.

PostgreSQL 전용.
`where`| **아니요**| `function` 또는 `object`| 지정된 조건과 일치하는 행만 포함하는 [부분 인덱스](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)를 정의합니다. `raw("SQL expression")` 또는 `{ field: value }` 같은 객체 리터럴을 허용합니다.

PostgreSQL, SQLite, SQL Server, CockroachDB에서 사용 가능합니다. `partialIndexes` Preview 기능이 필요합니다.

`@@index` 속성의 `fields` 인수에서 _name_ 은 생략할 수 있습니다:

```
    @@index(fields: [title, author])
    @@index([title, author])
```

`length` 및 `sort` 인수는 관련 필드 이름에 추가됩니다:

```
    @@index(fields: [title(length:10), author])
    @@index([title(sort: Asc), author(sort: Desc)])
```

#

- 시그니처

```
    @@index(_ fields: FieldReference[], map: String?, where: raw(String) | { field: value }?)
```

> **참고** : `where` 인수는 raw SQL 조건식을 위한 `raw("SQL expression")` 또는 타입 안전 조건을 위한 `{ field: value }` 객체 리터럴을 받습니다. 자세한 내용은 [부분 인덱스 구성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)을 참고하세요.

> **참고** : `partialIndexes` Preview 기능에서 `where` 인수를 사용할 수 있습니다. 이 Preview 기능 이전의 시그니처는 다음과 같았습니다:

```
>     @@index(_ fields: FieldReference[], map: String?)
```

#

- 예시

`Post` 모델의 `title` 필드에 인덱스를 추가하려고 한다고 가정해 보겠습니다.

#

- 단일 컬럼 인덱스 정의 (관계형 데이터베이스 전용)

```
    model Post {
      id      Int     @id @default(autoincrement())
      title   String
      content String?

      @@index([title])
    }
```

#

- 다중 컬럼 인덱스 정의 (관계형 데이터베이스 전용)

```
    model Post {
      id      Int     @id @default(autoincrement())
      title   String
      content String?

      @@index([title, content])
    }
```

#

- 이름이 있는 인덱스 정의 (관계형 데이터베이스 전용)

```
    model Post {
      id      Int     @id @default(autoincrement())
      title   String
      content String?

      @@index(fields: [title, content], name: "main_index")
    }
```

#

- 복합 타입 필드에 대한 인덱스 정의 (관계형 데이터베이스 전용)

```
    type Address {
      street String
      number Int
    }

    model User {
      id      Int     @id
      email   String
      address Address

      @@index([address.number])
    }
```

- `@relation`

관계에 대한 메타 정보를 정의합니다. [더 알아보기](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#the-relation-attribute).

#

- 비고

#

- 관계형 데이터베이스
  - 대응되는 데이터베이스 구성 요소: `FOREIGN KEY` / `REFERENCES`

#

- MongoDB
  - 기본 데이터베이스에서 모델의 기본 키가 `ObjectId` 타입인 경우, 기본 키와 외래 키 모두 `@db.ObjectId` 속성을 가져야 합니다.

#

- 인수

| 이름         | 타입                                                                                                                                                           | 필수                                                                                                                    | 설명                                                                                                                                                                 | 예시                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `name`       | `String`                                                                                                                                                       | 경우에 따라 필수 (예: 관계를 구분해야 할 때)                                                                            | 관계의 이름을 정의합니다. m-n 관계에서는 기본 관계 테이블의 이름도 결정합니다.                                                                                       | `"CategoryOnPost"`, `"MyRelation"`                    |
| `fields`     | `FieldReference[]`                                                                                                                                             | [annotated](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields) relation field에서 필수 | _현재_ 모델의 [필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-fields) 목록                                                           | `["authorId"]`, `["authorFirstName, authorLastName"]` |
| `references` | `FieldReference[]`                                                                                                                                             | [annotated](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields) relation field에서 필수 | _관계의 반대편 모델_ 의 [필드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-fields) 목록                                                 | `["id"]`, `["firstName, lastName"]`                   |
| `map`        | `String`                                                                                                                                                       | 아니요                                                                                                                  | 데이터베이스의 외래 키에 대한 [사용자 지정 이름](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names)을 정의합니다. | `["id"]`, `["firstName, lastName"]`                   |
| `onUpdate`   | Enum. 값은 [참조 동작 유형](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#types-of-referential-actions)을 참고하세요. | 아니요                                                                                                                  | 참조된 모델의 항목이 업데이트될 때 수행할 [참조 동작](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)을 정의합니다.          | `Cascade`, `NoAction`                                 |
| `onDelete`   | Enum. 값은 [참조 동작 유형](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#types-of-referential-actions)을 참고하세요. | 아니요                                                                                                                  | 참조된 모델의 항목이 삭제될 때 수행할 [참조 동작](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)을 정의합니다.              | `Cascade`, `NoAction`                                 |

`@relation` 속성의 `name` 인수 이름은 생략할 수 있습니다 (`references`는 필수):

```
    @relation(name: "UserOnPost", references: [id])
    @relation("UserOnPost", references: [id])

    // or

    @relation(name: "UserOnPost")
    @relation("UserOnPost")
```

#

- 시그니처

```
    @relation(_ name: String?, fields: FieldReference[]?, references: FieldReference[]?, onDelete: ReferentialAction?, onUpdate: ReferentialAction?, map: String?)
```

SQLite에서는 시그니처가 다음과 같이 변경됩니다:

```
    @relation(_ name: String?, fields: FieldReference[]?, references: FieldReference[]?, onDelete: ReferentialAction?, onUpdate: ReferentialAction?)
```

#

- 예시

참고: [The `@relation` attribute](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#the-relation-attribute).

- `@map`

Prisma 스키마의 필드 이름 또는 enum 값을 데이터베이스에서 다른 이름의 컬럼 또는 문서 필드에 매핑합니다. `@map`을 사용하지 않으면 Prisma 필드 이름은 컬럼 이름 또는 문서 필드 이름과 정확히 일치합니다.

> `@map` 및 `@@map`이 생성된 Prisma Client를 어떻게 변경하는지 보려면 [사용자 지정 모델 및 필드 이름 사용](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)을 참고하세요.

#

- 비고

#

- 일반
  - `@map`은 데이터베이스의 컬럼/필드 이름을 **변경하지 않습니다**
  - `@map`은 [생성된 클라이언트의 필드 이름을 **변경합니다**](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#map-the-firstname-field-to-a-column-called-first_name)

#

- MongoDB

`@id` 필드에는 반드시 `@map("_id")`가 포함되어야 합니다. 예:

```
    model User {
      id String @default(auto()) @map("_id") @db.ObjectId
    }
```

#

- 인수

| 이름   | 타입     | 필수   | 설명                                                                 | 예시                            |
| ------ | -------- | ------ | -------------------------------------------------------------------- | ------------------------------- |
| `name` | `String` | **예** | 데이터베이스 컬럼(관계형 데이터베이스) 또는 문서 필드(MongoDB) 이름. | `"comments"`, `"someFieldName"` |

`@map` 속성의 `name` 인수 이름은 생략할 수 있습니다:

```
    @map(name: "is_admin")
    @map("users")
```

#

- 시그니처

```
    @map(_ name: String)
```

#

- 예시

#

- `firstName` 필드를 `first_name`이라는 컬럼에 매핑

관계형 데이터베이스

MongoDB

```
    model User {
      id        Int    @id @default(autoincrement())
      firstName String @map("first_name")
    }
```

생성된 클라이언트:

```
    await prisma.user.create({
      data: {
        firstName: "Yewande", // first_name */} firstName
      },
    });
```

#

- `ADMIN`이라는 enum을 데이터베이스 enum `admin`에 매핑

```
    enum Role {
      ADMIN    @map("admin")
      CUSTOMER
    }
```

Prisma ORM v7 이상에서는 생성된 TypeScript enum이 매핑된 값을 사용합니다:

```
    export const Role = {
      ADMIN: "admin",
      CUSTOMER: "CUSTOMER",
    } as const;
```

이는 `Role.ADMIN`이 `"ADMIN"`이 아니라 `"admin"`으로 평가된다는 의미입니다.

- `@@map`

Prisma 스키마 모델 이름을 데이터베이스의 다른 이름의 테이블(관계형 데이터베이스) 또는 컬렉션(MongoDB)에 매핑하거나, enum 이름을 데이터베이스의 다른 기본 enum에 매핑합니다. `@@map`을 사용하지 않으면 모델 이름은 테이블(관계형 데이터베이스) 또는 컬렉션(MongoDB) 이름과 정확히 일치합니다.

> `@map` 및 `@@map`이 생성된 Prisma Client를 어떻게 변경하는지 보려면 [사용자 지정 모델 및 필드 이름 사용](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)을 참고하세요.

#

- 인수

| 이름   | 타입     | 필수   | 설명                                                                | 예시                                        |
| ------ | -------- | ------ | ------------------------------------------------------------------- | ------------------------------------------- |
| `name` | `String` | **예** | 데이터베이스 테이블(관계형 데이터베이스) 또는 컬렉션(MongoDB) 이름. | `"comments"`, `"someTableOrCollectionName"` |

`@@map` 속성의 `name` 인수 이름은 생략할 수 있습니다

```
    @@map(name: "users")
    @@map("users")
```

#

- 시그니처

```
    @@map(_ name: String)
```

#

- 예시

#

- `User` 모델을 `users`라는 데이터베이스 테이블/컬렉션에 매핑

관계형 데이터베이스

MongoDB

```
    model User {
      id   Int    @id @default(autoincrement())
      name String

      @@map("users")
    }
```

생성된 클라이언트:

```
    await prisma.user.create({
      // users */} user
      data: {
        name: "Yewande",
      },
    });
```

#

- `Role` enum을 데이터베이스의 `_Role`이라는 네이티브 enum에 매핑하고 값을 데이터베이스에서 소문자 값으로 매핑

```
    enum Role {
      ADMIN    @map("admin")
      CUSTOMER @map("customer")

      @@map("_Role")
    }
```

- `@updatedAt`

레코드가 마지막으로 업데이트된 시간을 자동으로 저장합니다. 시간을 직접 제공하지 않으면 Prisma Client가 이 속성이 있는 필드의 값을 자동으로 설정합니다.

#

- 비고
  - [`DateTime`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datetime) 필드와 호환됨
  - Prisma ORM 레벨에서 구현됨

[4.4.0](https://github.com/prisma/prisma/releases/tag/4.4.0) 이전 버전에서는 [`now()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#now)도 함께 사용하는 경우, 데이터베이스와 앱의 시간대가 다르면 시간이 `@updatedAt` 값과 다를 수 있습니다. 이는 `@updatedAt`은 Prisma ORM 레벨에서 동작하는 반면 `now()`는 데이터베이스 레벨에서 동작하기 때문입니다.

빈 업데이트 절을 전달하면 @updatedAt 값은 변경되지 않습니다. 예:

```
    await prisma.user.update({
      where: {
        id: 1,
      },
      data: {}, //<- Empty update clause
    });
```

#

- 인수

해당 없음

#

- 시그니처

```
    @updatedAt
```

#

- 예시

관계형 데이터베이스

MongoDB

```
    model Post {
      id        String   @id
      updatedAt DateTime @updatedAt
    }
```

- `@ignore`

Prisma Client에서 제외하려는 필드(예: Prisma Client 사용자가 업데이트하지 못하게 하려는 필드)에 `@ignore`를 추가합니다. 무시된 필드는 생성된 Prisma Client에서 제외됩니다. `@default`가 없는 _필수_ 필드에 이렇게 적용하면 모델의 `create` 메서드는 비활성화됩니다(해당 데이터 없이는 데이터베이스가 항목을 생성할 수 없기 때문).

#

- 비고
  - Prisma ORM은 introspect 시 잘못된 모델을 _참조하는_ 필드에 `@ignore`를 자동으로 추가합니다.

#

- 예시

다음 예시는 `email` 필드를 Prisma Client에서 제외하기 위해 `@ignore`를 수동으로 추가하는 방법을 보여줍니다.

schema.prisma

```
    model User {
      id    Int    @id
      name  String
      email String @ignore // this field will be excluded
    }
```

- `@@ignore`

Prisma Client에서 제외하려는 모델(예: Prisma 사용자가 업데이트하지 못하게 하려는 모델)에 `@@ignore`를 추가합니다. 무시된 모델은 생성된 Prisma Client에서 제외됩니다.

#

- 비고
  - Prisma ORM은 introspection 중 잘못된 모델에 `@@ignore`를 추가합니다. (또한 해당 모델을 가리키는 relation에 [`@ignore`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#ignore)도 추가합니다)

#

- 예시

다음 예시에서 `Post` 모델은 고유 식별자가 없기 때문에 유효하지 않습니다. 생성된 Prisma Client API에서 이를 제외하려면 `@@ignore`를 사용하세요.

schema.prisma

```
    /// The underlying table does not contain a valid unique identifier and can therefore currently not be handled by Prisma Client.
    model Post {
      id       Int  @default(autoincrement()) // no unique identifier
      author   User @relation(fields: [authorId], references: [id])
      authorId Int

      @@ignore
    }
```

다음 예시에서 `Post` 모델은 고유 식별자가 없어서 유효하지 않으며, `User`의 `posts` relation 필드도 유효하지 않은 `Post` 모델을 참조하므로 유효하지 않습니다. 생성된 Prisma Client API에서 모델과 relation 필드를 모두 제외하려면 `Post` 모델에는 `@@ignore`를, `User`의 `posts` relation 필드에는 `@ignore`를 사용하세요.

schema.prisma

```
    /// The underlying table does not contain a valid unique identifier and can therefore currently not be handled by Prisma Client.
    model Post {
      id       Int  @default(autoincrement()) // no unique identifier
      author   User @relation(fields: [authorId], references: [id])
      authorId Int

      @@ignore
    }

    model User {
      id    Int     @id @default(autoincrement())
      name  String?
      posts Post[]  @ignore
    }
```

- `@@schema`

모델에 연결된 테이블이 데이터베이스의 어떤 스키마에 포함될지 지정하려면 모델에 `@@schema`를 추가합니다. [여기에서 여러 스키마 추가](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema)에 대해 더 알아보세요.

[여러 데이터베이스 스키마](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema) 지원은 PostgreSQL, CockroachDB, SQL Server 커넥터에서만 사용할 수 있습니다.

#

- 인수

| Name   | Type     | Required | Description               | Example            |
| ------ | -------- | -------- | ------------------------- | ------------------ |
| `name` | `String` | **Yes**  | 데이터베이스 스키마 이름. | `"base"`, `"auth"` |

`@@schema` 속성의 `name` 인수 이름은 생략할 수 있습니다

```
    @@schema(name: "auth")
    @@schema("auth")
```

#

- 시그니처

```
    @@schema(_ name: String)
```

#

- 예시

#

- `User` 모델을 `auth`라는 데이터베이스 스키마에 매핑

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
    }

    datasource db {
      provider = "postgresql"
      schemas  = ["auth"]
    }

    model User {
      id   Int    @id @default(autoincrement())
      name String

      @@schema("auth")
    }
```

`multiSchema` 기능 사용에 대한 자세한 내용은 [이 가이드](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema)를 참고하세요.

- `@shardKey`

이 기능을 사용하려면 `generator`에 `shardKeys` Preview feature flag가 필요합니다:

```
    generator client {
      provider = "prisma-client"
      output = "../generated/prisma"
      previewFeatures = ["shardKeys"]
    }
```

`@shardKey` 속성은 [PlanetScale](http://planetscale.com/) 데이터베이스에서만 호환됩니다. 이를 통해 모델의 필드에 [shard key](https://planetscale.com/docs/vitess/sharding)를 정의할 수 있습니다:

```
    model User {
      id     String @default(uuid())
      region String @shardKey
    }
```

- `@@shardKey`

이 기능을 사용하려면 `generator`에 `shardKeys` Preview feature flag가 필요합니다:

```
    generator client {
      provider = "prisma-client"
      output = "../generated/prisma"
      previewFeatures = ["shardKeys"]
    }
```

`@@shardKey` 속성은 [PlanetScale](http://planetscale.com/) 데이터베이스에서만 호환됩니다. 이를 통해 모델의 여러 필드에 [shard key](https://planetscale.com/docs/vitess/sharding)를 정의할 수 있습니다:

```
    model User {
      id         String @default(uuid())
      country    String
      customerId String
      @@shardKey([country, customerId])
    }
```

## 속성 함수

- `auto()`

이 함수는 MongoDB에서만 사용할 수 있습니다.

데이터베이스에서 자동으로 생성되는 **기본값**을 나타냅니다.

#

- 비고

#

- MongoDB

`@id` 필드에 대한 `ObjectId`를 생성하는 데 사용됩니다:

```
    id  String  @map("_id") @db.ObjectId @default(auto())
```

#

- 관계형 데이터베이스

`auto()` 함수는 관계형 데이터베이스에서 사용할 수 없습니다.

#

- 예시

#

- `ObjectId` 생성(MongoDB 전용)

```
    model User {
      id   String  @id @default(auto()) @map("_id") @db.ObjectId
      name String?
    }
```

- `autoincrement()`

**MongoDB에서는 지원되지 않음**
[MongoDB connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)는 `autoincrement()` 함수를 지원하지 않습니다.

기반 데이터베이스에 정수 시퀀스를 만들고, 해당 시퀀스를 기준으로 생성된 레코드의 ID 값에 증가된 값을 할당합니다.

#

- 비고
  - 대부분의 데이터베이스에서 `Int`와 호환됨(CockroachDB에서는 `BigInt`)

  - 데이터베이스 레벨에서 구현되므로 데이터베이스 스키마에 반영되며 introspection을 통해 인식할 수 있습니다. 데이터베이스 구현은 다음과 같습니다:

| Database    | Implementation                                                                               |
| ----------- | -------------------------------------------------------------------------------------------- |
| PostgreSQL  | [`SERIAL`](https://www.postgresql.org/docs/9.1/datatype-numeric.html#DATATYPE-SERIAL) 타입   |
| MySQL       | [`AUTO_INCREMENT`](https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html) 속성 |
| SQLite      | [`AUTOINCREMENT`](https://www.sqlite.org/autoinc.html) 키워드                                |
| CockroachDB | [`SERIAL`](https://www.postgresql.org/docs/9.1/datatype-numeric.html#DATATYPE-SERIAL) 타입   |

#

- 예시

#

- 자동 증가 정수를 ID로 생성(관계형 데이터베이스 전용)

```
    model User {
      id   Int    @id @default(autoincrement())
      name String
    }
```

- `sequence()`

**CockroachDB에서만 지원됨**
sequence 함수는 [CockroachDB connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#cockroachdb)에서만 지원됩니다.

기반 데이터베이스에 정수 시퀀스를 만들고, 해당 시퀀스를 기준으로 생성된 레코드의 값에 증가된 값을 할당합니다.

#

- 선택 인수

| Argument  | Example                       |
| --------- | ----------------------------- |
| `virtual` | `@default(sequence(virtual))` |

Virtual sequence는 단조 증가 값을 생성하지 않고, 내장 함수 `unique_rowid()`가 생성하는 값과 유사한 값을 생성하는 시퀀스입니다.
`cache`| `@default(sequence(cache: 20))`
세션에서 재사용하기 위해 메모리에 캐시할 시퀀스 값의 개수입니다. 캐시 크기가 `1`이면 캐시가 없음을 의미하며, `1`보다 작은 캐시 크기는 유효하지 않습니다.
`increment`| `@default(sequence(increment: 4))`
시퀀스가 증가하는 새 값입니다. 음수는 내림차순 시퀀스를 만들고, 양수는 오름차순 시퀀스를 만듭니다.
`minValue`| `@default(sequence(minValue: 10))`
시퀀스의 새 최소값입니다.
`maxValue`| `@default(sequence(maxValue: 3030303))`
시퀀스의 새 최대값입니다.
`start`| `@default(sequence(start: 2))`
시퀀스가 재시작되거나 `maxValue`에 도달했을 때 시작하는 값입니다.

#

- 예시

#

- 순차 정수를 ID로 생성

```
    model User {
      id   Int    @id @default(sequence(maxValue: 4294967295))
      name String
    }
```

- `cuid()`

[`cuid`](https://github.com/ericelliott/cuid) 사양을 기반으로 전역 고유 식별자를 생성합니다.

[`cuid2`](https://github.com/paralleldrive/cuid2) 값을 사용하려면 `cuid` 함수에 인수로 `2`를 전달하면 됩니다: `cuid(2)`.

#

- 비고
  - `String`과 호환됩니다.
  - Prisma ORM에서 구현되므로 기반 데이터베이스 스키마에는 "표시"되지 않습니다. [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 사용 시에도 [Prisma schema를 수동으로 변경](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)하고 Prisma Client를 생성하면 `cuid()`를 사용할 수 있으며, 이 경우 값은 Prisma ORM에서 생성됩니다.
  - `cuid()` 출력 길이는 cuid 제작자에 따라 정의되어 있지 않으므로, 매우 큰 값을 위해 충분한 문자를 허용하려면 안전한 필드 크기는 30자입니다. 필드 크기를 30보다 작게 설정한 뒤 `cuid()`가 더 큰 값을 생성하면 `Error: The provided value for the column is too long for the column's type.` 같은 Prisma Client 오류가 발생할 수 있습니다.
  - **MongoDB**의 경우: `cuid()`는 유효한 `ObjectId`를 생성하지 않습니다. 기반 데이터베이스에서 `ObjectId`를 사용하려면 [`@db.ObjectId` 구문](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#generate-objectid-as-ids-mongodb-only)을 사용할 수 있습니다. 다만 `_id` 필드가 `ObjectId` 타입이 아니라면 `cuid()`를 계속 사용할 수 있습니다.

#

- 예시

#

- `cuid()` 값을 ID로 생성

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(cuid())
      name String
    }
```

#

- `cuid2` 사양 기반의 `cuid(2)` 값을 ID로 생성

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(cuid(2))
      name String
    }
```

- `uuid()`

[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) 사양을 기반으로 전역 고유 식별자를 생성합니다. Prisma ORM은 버전 4(기본값)와 7을 지원합니다.

#

- 비고
  - `String`과 호환됩니다.
  - Prisma ORM에서 구현되므로 기반 데이터베이스 스키마에는 "표시"되지 않습니다. [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 사용 시에도 [Prisma schema를 수동으로 변경](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)하고 Prisma Client를 생성하면 `uuid()`를 사용할 수 있으며, 이 경우 값은 Prisma ORM에서 생성됩니다.
  - **관계형 데이터베이스**의 경우: Prisma ORM의 `uuid()` 함수를 사용하지 않으려면 [`dbgenerated`와 함께 데이터베이스 네이티브 함수](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#override-default-value-behavior-for-supported-types)를 사용할 수 있습니다.

* **MongoDB**의 경우: `uuid()`는 유효한 `ObjectId`를 생성하지 않습니다. 기본 데이터베이스에서 `ObjectId`를 사용하려면 [`@db.ObjectId` syntax](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#generate-objectid-as-ids-mongodb-only)를 사용할 수 있습니다. 다만 `_id` 필드 타입이 `ObjectId`가 아니라면 `uuid()`를 계속 사용할 수 있습니다.

#

- Examples

#

- Generate `uuid()` values as IDs using UUID v4

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(uuid())
      name String
    }
```

#

- Generate `uuid(7)` values as IDs using UUID v7

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(uuid(7))
      name String
    }
```

- `ulid()`

[ULID](https://github.com/ulid/spec) 사양을 기반으로, 사전식 정렬이 가능한 범용 고유 식별자를 생성합니다.

#

- Remarks
  - `ulid()`는 128비트 랜덤 식별자를 생성하며, 26자 길이의 영숫자 문자열로 표현됩니다. 예: `01ARZ3NDEKTSV4RRFFQ69G5FAV`

#

- Examples

#

- Generate `ulid()` values as IDs

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(ulid())
      name String
    }
```

- `nanoid()`

[Nano ID](https://github.com/ai/nanoid) 사양 기반으로 값을 생성합니다. `nanoid()`는 생성할 ID 값의 _길이_ 를 지정하는 2~255 사이의 정수를 받습니다. 예를 들어 `nanoid(16)`은 16자 ID를 생성합니다. `nanoid()` 함수에 값을 주지 않으면 기본값은 21입니다.

Nano ID는 UUID v4(랜덤 기반)와 꽤 유사합니다. ID에 포함되는 랜덤 비트 수가 비슷하기 때문에(Nano ID는 126, UUID는 122), 충돌 확률도 유사합니다.

중복 가능성을 10억 분의 1로 만들려면, version 4 ID를 103조 개 생성해야 합니다.

Nano ID와 UUID v4의 주요 차이점은 두 가지입니다.

- Nano ID는 더 큰 알파벳을 사용하므로, 비슷한 랜덤 비트 수를 36개가 아닌 21개 심볼에 담습니다.
- Nano ID 코드는 uuid/v4 패키지보다 4배 작습니다: 423바이트 대신 130바이트입니다.

#

- Remarks
  - `String`과 호환됩니다.
  - Prisma ORM에 의해 구현되므로 기본 데이터베이스 스키마에는 "보이지" 않습니다. [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 사용 시에도 [Prisma schema를 수동으로 변경](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names)하고 [Prisma Client를 생성](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider)하면 `uuid()`를 계속 사용할 수 있으며, 이 경우 값은 Prisma ORM이 생성합니다.
  - **MongoDB**의 경우: `nanoid()`는 유효한 `ObjectId`를 생성하지 않습니다. 기본 데이터베이스에서 `ObjectId`를 사용하려면 [`@db.ObjectId` syntax](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#generate-objectid-as-ids-mongodb-only)를 사용할 수 있습니다. 다만 `_id` 필드 타입이 `ObjectId`가 아니라면 `nanoid()`를 계속 사용할 수 있습니다.

#

- Examples

#

- Generate `nanoid()` values with 21 characters as IDs

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(nanoid())
      name String
    }
```

#

- Generate `nanoid()` values with 16 characters as IDs

관계형 데이터베이스

MongoDB

```
    model User {
      id   String @id @default(nanoid(16))
      name String
    }
```

- `now()`

레코드가 생성되는 시점의 타임스탬프를 설정합니다.

#

- Remarks

#

- General
  - [`DateTime`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datetime)과 호환됩니다.

[4.4.0](https://github.com/prisma/prisma/releases/tag/4.4.0) 이전 버전에서는 [`@updatedAt`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#updatedat)도 함께 사용하면, 데이터베이스와 앱의 타임존이 다를 때 `now()` 값과 시간이 달라질 수 있습니다. 이는 `@updatedAt`는 Prisma ORM 레벨에서 동작하고, `now()`는 데이터베이스 레벨에서 동작하기 때문입니다.

#

- Relational databases
  - 데이터베이스 레벨에서 구현되므로 데이터베이스 스키마에 반영되며 introspection으로 인식할 수 있습니다. 데이터베이스별 구현:

| Database    | Implementation                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| PostgreSQL  | [`CURRENT_TIMESTAMP`](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT) 및 `now()` 같은 별칭      |
| MySQL       | [`CURRENT_TIMESTAMP`](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 및 `now()` 같은 별칭 |
| SQLite      | `CURRENT_TIMESTAMP` 및 `date('now')` 같은 별칭                                                                                              |
| CockroachDB | [`CURRENT_TIMESTAMP`](https://www.cockroachlabs.com/docs/stable/functions-and-operators#special-syntax-forms) 및 `now()` 같은 별칭          |

#

- MongoDB
  - Prisma ORM 레벨에서 구현됩니다.

#

- Examples

#

- Set current timestamp value when a record is created

관계형 데이터베이스

MongoDB

```
    model User {
      id        String   @id
      createdAt DateTime @default(now())
    }
```

- `dbgenerated(...)`

Prisma schema에서 표현할 수 없는 **기본값**(`random()` 등)을 나타냅니다.

#

- Remarks

#

- Relational databases
  - 모든 스칼라 타입과 호환됩니다.

  - 빈 문자열 `dbgenerated("")`은 사용할 수 없습니다.

  - `String` 값을 받으며, 이를 통해 다음을 수행할 수 있습니다:
    - `Unsupported` 타입의 기본값 설정
    - 지원되는 타입의 기본값 동작 재정의

  - `dbgenerated(...)`의 문자열 값은 DB가 기본값으로 반환하는 값과 일치하지 않을 수 있습니다. 문자열 같은 값이 명시적으로 캐스팅될 수 있기 때문입니다(예: `'hello'::STRING`). 불일치가 있으면 Prisma Migrate는 여전히 마이그레이션이 필요하다고 표시합니다. 차이를 해결하려면 `prisma db pull`을 사용해 올바른 값을 추론할 수 있습니다. ([Related issue](https://github.com/prisma/prisma/issues/14917))

#

- Examples

#

- Set default value for `Unsupported` type

```
    circle     Unsupported("circle")?   @default(dbgenerated("'<(10,4),11>'::circle"))
```

#

- Override default value behavior for supported types

`dbgenerated(...)`를 사용해 지원되는 타입의 기본값을 설정할 수도 있습니다. 예를 들어 PostgreSQL에서는 Prisma ORM의 `uuid()`에 의존하는 대신 데이터베이스 레벨에서 UUID를 생성할 수 있습니다:

```
    model User {
      id   String  @id @default(dbgenerated("gen_random_uuid()")) @db.Uuid
      id   String  @id @default(uuid()) @db.Uuid
      test String?
    }
```

[`gen_random_uuid()` is a PostgreSQL function](https://www.postgresql.org/docs/13/functions-uuid.html). PostgreSQL 12.13 이하 버전에서 이를 사용하려면 `pgcrypto` extension을 활성화해야 합니다. extension 설치 방법은 [PostgreSQL extensions](https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions)를 참고하세요.

## 속성 인수 타입

### `FieldReference[]`

[field](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-fields) 이름의 배열: `[id]`, `[firstName, lastName]`

- `String`

큰따옴표로 감싼 가변 길이 텍스트: `""`, `"Hello World"`, `"Alice"`

- `Expression`

Prisma ORM이 평가할 수 있는 표현식: `42.0`, `""`, `Bob`, `now()`, `cuid()`

## `enum`

**Microsoft SQL Server에서는 지원되지 않음**
[Microsoft SQL Server connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)는 `enum` 타입을 지원하지 않습니다.

[enum](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-enums)을 정의합니다.

- Remarks
  - enum은 [PostgreSQL](https://www.postgresql.org/docs/current/datatype-enum.html)과 [MySQL](https://dev.mysql.com/doc/refman/8.0/en/enum.html)에서 네이티브로 지원됩니다.
  - SQLite와 MongoDB에서는 Prisma ORM 레벨에서 enum이 구현되고 강제됩니다.

- Naming conventions
  - enum 이름은 문자로 시작해야 합니다(보통 [PascalCase](http://wiki.c2.com/?PascalCase)로 표기).
  - enum은 단수형을 사용해야 합니다(예: `role`, `roles`, `Roles` 대신 `Role`).
  - 다음 정규식을 준수해야 합니다: `[A-Za-z][A-Za-z0-9_]*`

- Examples

#

- Specify an `enum` with two possible values

관계형 데이터베이스

MongoDB

```
    enum Role {
      USER
      ADMIN
    }

    model User {
      id   Int  @id @default(autoincrement())
      role Role
    }
```

#

- Specify an `enum` with two possible values and set a default value

관계형 데이터베이스

MongoDB

```
    enum Role {
      USER
      ADMIN
    }

    model User {
      id   Int  @id @default(autoincrement())
      role Role @default(USER)
    }
```

## `type`

복합 타입은 **MongoDB에서만** 사용할 수 있습니다.

[composite type](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-composite-types-mongodb)을 정의합니다.

- Naming conventions

Type 이름은 다음 조건을 충족해야 합니다:

- 문자로 시작해야 합니다(보통 [PascalCase](http://wiki.c2.com/?PascalCase)로 표기).
- 다음 정규식을 준수해야 합니다: `[A-Za-z][A-Za-z0-9_]*`

* Examples

#

- Define a `Product` model with a list of `Photo` composite types

```
    model Product {
      id     String  @id @default(auto()) @map("_id") @db.ObjectId
      name   String
      photos Photo[]
    }

    type Photo {
      height Int
      width  Int
      url    String
    }
```
