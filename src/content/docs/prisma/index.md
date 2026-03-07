---
title: "Prisma ORM"
description: "Prisma ORM은 타입 안전한 데이터베이스 액세스, 마이그레이션, 시각적 데이터 편집기를 제공하는 차세대 Node.js 및 TypeScript ORM입니다."
---

출처 URL: https://docs.prisma.io/docs/orm

# Prisma ORM

Prisma ORM은 타입 안전한 데이터베이스 액세스, 마이그레이션, 시각적 데이터 편집기를 제공하는 차세대 Node.js 및 TypeScript ORM입니다.

Prisma ORM은 [오픈 소스](https://github.com/prisma/prisma)이며 다음으로 구성됩니다.

- [**Prisma Client**](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction): 자동 생성되는 타입 안전한 **ORM 인터페이스**
- [**Prisma Migrate**](https://docs.prisma.io/docs/orm/prisma-migrate): 데이터베이스 마이그레이션 시스템
- [**Prisma Studio**](https://www.prisma.io/studio): 데이터를 조회하고 편집하는 GUI

Prisma Client는 전통적인 서버, serverless 함수, microservices 배포 여부와 관계없이 모든 Node.js 또는 TypeScript 백엔드에서 동작합니다.

## Prisma ORM을 선택하는 이유

기존 데이터베이스 도구는 **생산성**과 **제어력** 사이에서 트레이드오프를 강요합니다. Raw SQL은 완전한 제어를 제공하지만 오류가 발생하기 쉽고 타입 안전성이 없습니다. 기존 ORM은 생산성을 높이지만 지나치게 많은 것을 추상화하여 [object-relational impedance mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)와 n+1 문제 같은 성능 함정을 유발합니다.

Prisma는 다른 접근 방식을 취합니다.

- 전체 자동완성과 함께 컴파일 시점에 검증되는 **타입 안전한 쿼리**
- 관계형 데이터를 매핑하는 복잡성 없이 **객체 중심으로 사고**
- 복잡한 모델 인스턴스가 아닌, 쿼리 결과로 반환되는 **plain JavaScript 객체**
- 데이터베이스와 애플리케이션 모델을 위한 Prisma 스키마의 **단일 진실 공급원(single source of truth)**
- 일반적인 함정과 안티 패턴을 방지하는 **건전한 제약 조건**

## Prisma를 사용하기 좋은 경우

**다음에 해당하면 Prisma가 잘 맞습니다:**

- 서버 사이드 애플리케이션(REST, GraphQL, gRPC, serverless)을 구축한다
- 타입 안전성과 개발자 경험을 중요하게 생각한다
- 팀으로 작업하며 명확하고 선언적인 스키마를 원한다
- 하나의 툴킷에서 마이그레이션, 쿼리, 데이터 모델링이 필요하다

**다음에 해당하면 대안을 고려하세요:**

- 모든 SQL 쿼리를 완전히 제어해야 한다(raw SQL 드라이버 사용)
- no-code 백엔드를 원한다(Supabase 또는 Firebase 같은 BaaS 사용)
- 자동 생성되는 CRUD GraphQL API가 필요하다(Hasura 또는 PostGraphile 사용)

## 동작 방식

- 1\. 스키마 정의

[Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)는 데이터 모델과 데이터베이스 연결을 정의합니다.

```
    datasource db {
      provider = "postgresql"
    }

    generator client {
      provider = "prisma-client"
      output   = "./generated"
    }

    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
      posts Post[]
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      published Boolean @default(false)
      author    User?   @relation(fields: [authorId], references: [id])
      authorId  Int?
    }
```

- 2\. 연결 구성

프로젝트 루트에 `prisma.config.ts` 파일을 생성하세요.

prisma.config.ts

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

- 3\. 마이그레이션 실행

[Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용해 마이그레이션을 생성하고 적용하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

또는 기존 데이터베이스를 [introspect](https://docs.prisma.io/docs/orm/prisma-schema/introspection)하세요.

npm

pnpm

yarn

bun

```
    npx prisma db pull
```

- 4\. Prisma Client로 쿼리

타입 안전한 클라이언트를 생성하고 사용하세요.

npm

pnpm

yarn

bun

```
    npm install @prisma/client
    npx prisma generate
```

```
    import { PrismaClient } from "./generated/client";

    const prisma = new PrismaClient();

    // Find all users with their posts
    const users = await prisma.user.findMany({
      include: { posts: true },
    });

    // Create a user with a post
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        posts: {
          create: { title: "Hello World" },
        },
      },
    });
```

## 다음 단계

- [**Prisma schema**](https://docs.prisma.io/docs/orm/prisma-schema/overview) \- 스키마 언어 알아보기
- [**Prisma Client**](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction) \- 쿼리 API 살펴보기
