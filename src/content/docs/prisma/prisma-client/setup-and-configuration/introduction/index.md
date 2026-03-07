---
title: "Prisma Client 소개"
description: "프로젝트에서 Prisma Client를 설정하고 구성하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction

# Prisma Client 소개

프로젝트에서 Prisma Client를 설정하고 구성하는 방법을 알아보세요

Prisma Client는 데이터에 _맞춰진_ 자동 생성형 타입 안전 쿼리 빌더입니다. Prisma Client를 시작하는 가장 쉬운 방법은 **[Quickstart](https://docs.prisma.io/docs/prisma-orm/quickstart/sqlite)**를 따르는 것입니다.

[Quickstart (5분)](https://docs.prisma.io/docs/prisma-orm/quickstart/sqlite)

## 사전 요구 사항

Prisma Client를 설정하려면 Prisma Config와 [Prisma schema file](https://docs.prisma.io/docs/orm/prisma-schema/overview)이 필요합니다:

Prisma Config

Prisma Schema

prisma.config.ts

```
    import 'dotenv/config';
    import { defineConfig, env } from 'prisma/config';

    export default defineConfig({
      schema: './prisma/schema.prisma',
      datasource: {
        url: env('DATABASE_URL'),
      },
    });
```

## 설치

데이터베이스에 맞는 [Install the Prisma CLI](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference), Prisma Client 라이브러리, 그리고 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)를 설치하세요:

PostgreSQL

MySQL / MariaDB

SQLite

npm

pnpm

yarn

bun

```
    npm install prisma --save-dev
    npm install @prisma/client @prisma/adapter-pg pg
```

Prisma 7은 데이터베이스에 연결하기 위해 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)가 필요합니다. ESM 지원을 위해 `package.json`에 `"type": "module"`이 포함되어 있는지 확인하세요. 자세한 내용은 [upgrade guide](https://docs.prisma.io/docs/guides/upgrade-prisma-orm/v7)를 참고하세요.

## Client API 생성

Prisma Client는 Prisma Schema의 모델을 기반으로 합니다. 올바른 타입을 제공하려면 클라이언트 코드를 생성해야 합니다:

npm

pnpm

yarn

bun

```
    npx prisma generate
```

이렇게 하면 Prisma Schema에서 `output`으로 설정한 위치를 기준으로 `generated` 디렉터리가 생성됩니다. Prisma Client를 import할 때마다 이 생성된 클라이언트 API에서 가져와야 합니다.

## Prisma Client 가져오기

클라이언트가 생성되면 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)와 함께 import하고 새 인스턴스를 생성하세요:

PostgreSQL

MySQL / MariaDB

SQLite

PostgreSQL (Edge)

```
    import { PrismaClient } from "./path/to/generated/prisma";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL!,
    });

    export const prisma = new PrismaClient({ adapter });
```

Prisma 7에서 `PrismaClient`에는 driver adapter가 필요합니다. `adapter` 없이 `new PrismaClient()`를 호출하면 오류가 발생합니다.

사용 중인 데이터베이스에 어떤 [driver adapter](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)가 필요한지 확인하세요.

일반적으로 애플리케이션에서는 `PrismaClient` **인스턴스를 하나만** 생성해야 합니다. 이를 구현하는 방법은 Prisma ORM을 [long-running application](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-long-running-applications)에서 사용하는지, 혹은 [serverless environment](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-serverless-environments)에서 사용하는지에 따라 달라집니다.

`PrismaClient` 인스턴스를 여러 개 생성하면 연결 풀이 여러 개 만들어지고 데이터베이스의 연결 제한에 도달할 수 있습니다. 연결이 너무 많아지면 데이터베이스가 **느려지기 시작**하고, 결국 다음과 같은 오류로 이어질 수 있습니다:

```
    Error in connector: Error querying the database: db error: FATAL: sorry, too many clients already
       at PrismaClientFetcher.request
```

## Prisma Client를 사용해 데이터베이스로 쿼리 보내기

`PrismaClient` 인스턴스를 생성한 후에는 코드에서 쿼리를 보내기 시작할 수 있습니다:

```
    // run inside `async` function
    const newUser = await prisma.user.create({
      data: {
        name: "Alice",
        email: "alice@prisma.io",
      },
    });

    const users = await prisma.user.findMany();
```

## 애플리케이션 발전시키기

Prisma schema에 반영되는 데이터베이스 변경이 있을 때마다, 출력 디렉터리의 생성 코드가 업데이트되도록 Prisma Client를 수동으로 다시 생성해야 합니다:

npm

pnpm

yarn

bun

```
    npx prisma generate
```
