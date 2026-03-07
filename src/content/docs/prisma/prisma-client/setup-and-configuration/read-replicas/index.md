---
title: "읽기 복제본"
description: "Prisma Client에서 읽기 복제본을 설정하고 사용하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/read-replicas

# 읽기 복제본

Prisma Client에서 읽기 복제본을 설정하고 사용하는 방법을 알아보세요.

읽기 복제본을 사용하면 트래픽이 많은 워크로드에서 데이터베이스 복제본으로 작업 부하를 분산할 수 있습니다. [read replicas extension](https://github.com/prisma/extension-read-replicas)인 `@prisma/extension-read-replicas`는 Prisma Client에 읽기 전용 데이터베이스 복제본 지원을 추가합니다.

버그를 발견했거나 피드백이 있다면 [여기](https://github.com/prisma/extension-read-replicas/issues/new)에서 GitHub 이슈를 생성해 주세요.

## 읽기 복제본 확장 설정

확장을 설치하세요:

npm

pnpm

yarn

bun

```
    npm install @prisma/extension-read-replicas@latest
```

Prisma Client 인스턴스를 확장해 확장을 초기화하고, 읽기 복제본용 전체 `PrismaClient` 인스턴스를 확장에 제공하세요. 기본 접근 방식은 드라이버 어댑터를 사용하는 것입니다:

```
    import { readReplicas } from "@prisma/extension-read-replicas";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/prisma/client";

    // Create main client with adapter
    const mainAdapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL!,
    });

    const mainClient = new PrismaClient({ adapter: mainAdapter });

    // Create replica client with adapter
    const replicaAdapter = new PrismaPg({
      connectionString: process.env.REPLICA_URL!,
    });

    const replicaClient = new PrismaClient({ adapter: replicaAdapter });

    // Extend main client with read replicas
    const prisma = mainClient.$extends(readReplicas({ replicas: [replicaClient] }));

    // Query is run against the database replica
    await prisma.post.findMany();

    // Query is run against the primary database
    await prisma.post.create({
      data: {
        /** */
      },
    });
```

모든 읽기 작업(예: `findMany`)은 데이터베이스 복제본에서 실행됩니다. 모든 쓰기 작업(예: `create`, `update`)과 `$transaction` 쿼리는 기본 데이터베이스에서 실행됩니다.

## 여러 데이터베이스 복제본 구성

`replicas` 속성은 모든 데이터베이스 복제본에 대한 `PrismaClient` 인스턴스 배열을 받습니다:

```
    import { readReplicas } from "@prisma/extension-read-replicas";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/prisma/client";

    // Create main client
    const mainAdapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL!,
    });
    const mainClient = new PrismaClient({ adapter: mainAdapter });

    // Create multiple replica clients
    const replicaAdapter1 = new PrismaPg({
      connectionString: process.env.DATABASE_URL_REPLICA_1!,
    });
    const replicaClient1 = new PrismaClient({ adapter: replicaAdapter1 });

    const replicaAdapter2 = new PrismaPg({
      connectionString: process.env.DATABASE_URL_REPLICA_2!,
    });
    const replicaClient2 = new PrismaClient({ adapter: replicaAdapter2 });

    // Configure multiple replicas
    const prisma = mainClient.$extends(
      readReplicas({
        replicas: [replicaClient1, replicaClient2],
      }),
    );
```

둘 이상의 읽기 복제본이 구성되어 있으면, 쿼리 실행을 위해 데이터베이스 복제본이 무작위로 선택됩니다.

## 기본 데이터베이스에서 읽기 작업 실행

`$primary()` 메서드를 사용해 읽기 작업을 기본 데이터베이스에서 명시적으로 실행할 수 있습니다:

```
    const posts = await prisma.$primary().post.findMany();
```

## 데이터베이스 복제본에서 작업 실행

`$replica()` 메서드를 사용해 기본 데이터베이스 대신 복제본에서 쿼리를 명시적으로 실행할 수 있습니다:

```
    const result = await prisma.$replica().user.findFirst(...)
```
