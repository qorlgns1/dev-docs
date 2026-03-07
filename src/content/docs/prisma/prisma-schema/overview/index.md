---
title: "Prisma Schema 개요"
description: "Prisma schema는 Prisma를 사용할 때 구성의 핵심 방법입니다. 일반적으로 라고 하며, 데이터베이스 연결과 데이터 모델을 포함합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/overview

# Prisma Schema 개요

Prisma schema는 Prisma를 사용할 때 구성의 핵심 방법입니다. 일반적으로 `schema.prisma`라고 하며, 데이터베이스 연결과 데이터 모델을 포함합니다.

Prisma Schema(줄여서 _schema_)는 Prisma ORM 설정을 위한 주요 구성 방법입니다. 다음 부분으로 구성됩니다:

- [**데이터 소스**](https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources): Prisma ORM이 연결해야 할 데이터 소스의 세부 정보를 지정합니다(예: PostgreSQL 데이터베이스).
- [**제너레이터**](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators): 데이터 모델을 기반으로 어떤 클라이언트를 생성할지 지정합니다(예: Prisma Client).
- [**데이터 모델 정의**](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models): 애플리케이션의 [모델](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-models)(데이터 소스별 데이터의 형태)과 그 [관계](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)를 지정합니다.

일반적으로 이는 `schema.prisma`라는 단일 파일(또는 `.prisma` 파일 확장자를 가진 여러 파일)이며, 지정되어 있지만 사용자 지정 가능한 [위치](https://docs.prisma.io/docs/orm/prisma-schema/overview/location)에 저장됩니다. 원한다면 [Prisma schema를 여러 파일로 구성](https://docs.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema)할 수도 있습니다.

schema의 각 섹션에 대한 자세한 내용은 [Prisma schema API reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference)를 참고하세요.

`prisma` 명령이 실행될 때마다 CLI는 일반적으로 schema에서 일부 정보를 읽습니다. 예:

- `prisma generate`: 올바른 데이터 소스 클라이언트 코드(예: Prisma Client)를 생성하기 위해 위에서 언급한 Prisma schema 정보를 _모두_ 읽습니다.
- `prisma migrate dev`: 새 마이그레이션을 만들기 위해 데이터 소스와 데이터 모델 정의를 읽습니다.

CLI 명령이 실행될 때 구성 옵션을 제공하기 위해 schema 내부에서 [환경 변수 사용](https://docs.prisma.io/docs/orm/prisma-schema/overview#accessing-environment-variables-from-the-schema)도 가능합니다.

## 예시

다음은 아래를 지정하는 Prisma Schema 예시입니다:

- 데이터 소스(PostgreSQL 또는 MongoDB)
- 제너레이터(Prisma Client)
- 두 개의 모델(하나의 relation 포함)과 하나의 `enum`이 있는 데이터 모델 정의
- 여러 [네이티브 데이터 타입 속성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)(`@db.VarChar(255)`, `@db.ObjectId`)

관계형 데이터베이스

MongoDB

```
    datasource db {
      provider = "postgresql"
    }

    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    model User {
      id        Int      @id @default(autoincrement())
      createdAt DateTime @default(now())
      email     String   @unique
      name      String?
      role      Role     @default(USER)
      posts     Post[]
    }

    model Post {
      id        Int      @id @default(autoincrement())
      createdAt DateTime @default(now())
      updatedAt DateTime @updatedAt
      published Boolean  @default(false)
      title     String   @db.VarChar(255)
      author    User     @relation(fields: [authorId], references: [id])
      authorId  Int
    }

    enum Role {
      USER
      ADMIN
    }
```

## 문법

Prisma Schema 파일은 Prisma Schema Language(PSL)로 작성됩니다. 자세한 내용과 예시는 [데이터 소스](https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources), [제너레이터](https://docs.prisma.io/docs/orm/prisma-schema/overview/generators), [데이터 모델 정의](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models), 그리고 물론 [Prisma Schema API reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 페이지를 참고하세요.

- VS Code

PSL 구문 강조는 [VS Code 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)을 통해 사용할 수 있습니다(Prisma schema 내용을 자동 포맷하고, 빨간 물결선으로 구문 오류를 표시하는 기능도 포함). [에디터에서 Prisma ORM 설정하기](https://docs.prisma.io/docs/orm/more/dev-environment/editor-setup)에서 자세한 내용을 확인하세요.

- GitHub

GitHub의 PSL 코드 스니펫도 `.prisma` 파일 확장자를 사용하거나 Markdown의 fenced code block에 `prisma`를 지정하면 구문 강조로 렌더링할 수 있습니다:

````
    ```prisma
    model User {
      id        Int      @id @default(autoincrement())
      createdAt DateTime @default(now())
      email     String   @unique
      name      String?
    }
    ```
````

## schema에서 환경 변수 접근

CLI 명령이 실행될 때 또는 Prisma Client 쿼리가 실행될 때 구성 옵션을 제공하기 위해 환경 변수를 사용할 수 있습니다.

URL을 schema에 직접 하드코딩할 수도 있지만 보안 위험이 있으므로 권장되지 않습니다. schema에서 환경 변수를 사용하면 **schema에 비밀 정보를 두지 않을 수 있고**, 그 결과 서로 다른 환경에서 사용할 수 있어 **schema의 이식성이 향상됩니다**.

환경 변수는 `env()` 함수를 사용해 접근할 수 있습니다:

```
    datasource db {
      provider = "postgresql"
    }
```

다음 위치에서 `env()` 함수를 사용할 수 있습니다:

- 데이터 소스 URL
- Generator binary targets

개발 중 `.env` 파일을 사용하는 방법에 대한 자세한 내용은 [Environment variables](https://docs.prisma.io/docs/orm/more/dev-environment/environment-variables)를 참고하세요.

## 주석

Prisma Schema Language에서 지원되는 주석 유형은 세 가지입니다:

- `// comment`: 이 주석은 가독성을 위한 것이며 schema의 abstract syntax tree(AST)에는 포함되지 않습니다.
- `/// comment`: 이 주석은 schema의 abstract syntax tree(AST)에서 AST 노드의 설명으로 나타납니다. 이후 도구가 이 주석을 사용해 추가 정보를 제공할 수 있습니다. 모든 주석은 다음에 오는 사용 가능한 노드에 연결됩니다. [자유 부동 주석](https://github.com/prisma/prisma/issues/3544)은 지원되지 않으며 AST에 포함되지 않습니다.
- `/* block comment */`: 이 주석은 `///` 주석과 유사하게 abstract syntax tree에 나타납니다.

다음은 몇 가지 예시입니다:

```
    /// This comment will get attached to the `User` node in the AST
    model User {
      /// This comment will get attached to the `id` node in the AST
      id     Int   @default(autoincrement())
      // This comment is just for you
      weight Float /// This comment gets attached to the `weight` node
    }

    // This comment is just for you. It will not
    // show up in the AST.

    /// This comment will get attached to the
    /// Customer node.
    model Customer {
      /**
       * ...and so will this comment
       */
    }
```

## 자동 포맷팅

Prisma ORM은 `.prisma` 파일의 자동 포맷팅을 지원합니다. `.prisma` 파일을 포맷하는 방법은 두 가지입니다:

- [`prisma format`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#format) 명령을 실행합니다.
- [Prisma VS Code 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)을 설치하고 [VS Code format action](https://code.visualstudio.com/docs/editor/codebasics#_formatting)을 실행합니다. \- 수동 또는 저장 시 실행할 수 있습니다.

구성 옵션은 없습니다. [포맷팅 규칙](https://docs.prisma.io/docs/orm/prisma-schema/overview#formatting-rules)은 고정되어 있습니다(Golang의 `gofmt`와 유사하지만 Javascript의 `prettier`와는 다름):

- 포맷팅 규칙

#

- 구성 블록은 = 기호를 기준으로 정렬됩니다

```
    block _ {
      key      = "value"
      key2     = 1
      long_key = true
    }
```

#

- 필드 정의는 2개 이상의 공백으로 구분된 열 형태로 정렬됩니다

```
    block _ {
      id          String       @id
      first_name  LongNumeric  @default
    }
```

#

- 빈 줄은 블록 정렬과 포맷팅 규칙을 초기화합니다

```
    block _ {
      key   = "value"
      key2  = 1
      key10 = true

      long_key   = true
      long_key_2 = true
    }
```

```
    block _ {
      id  String  @id
                  @default

      first_name  LongNumeric  @default
    }
```

#

- 여러 줄 필드 속성은 나머지 필드 속성과 올바르게 정렬됩니다

```
    block _ {
      id          String       @id
                               @default
      first_name  LongNumeric  @default
    }
```

#

- 블록 속성은 블록의 끝으로 정렬됩니다

```
    block _ {
      key   = "value"

      @@attribute
    }
```
