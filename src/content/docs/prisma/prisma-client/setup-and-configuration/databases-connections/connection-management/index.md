---
title: "연결 관리"
description: "이 페이지에서는 Prisma Client에서 데이터베이스 연결을 처리하는 방식과 데이터베이스를 수동으로 연결 및 연결 해제하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management

# 연결 관리

이 페이지에서는 Prisma Client에서 데이터베이스 연결을 처리하는 방식과 데이터베이스를 수동으로 연결 및 연결 해제하는 방법을 설명합니다.

빠른 요약

이 페이지에서는 Prisma Client가 데이터베이스 연결을 관리하는 방법(예: `$connect()` 및 `$disconnect()` 메서드를 언제, 어떻게 사용할지, connection pooling 동작, 장기 실행 환경과 서버리스 환경 각각의 모범 사례)을 설명합니다.

`PrismaClient`는 다음 두 가지 메서드를 사용해 데이터 소스에 연결하고 연결을 해제합니다.

- `$connect()`
- `$disconnect()`

대부분의 경우 **이 메서드들을 명시적으로 호출할 필요가 없습니다**. `PrismaClient`는 첫 쿼리를 실행할 때 자동으로 연결하고, [connection pool](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)을 생성하며, Node.js 프로세스가 종료될 때 연결을 해제합니다.

다양한 배포 패러다임(장기 실행 프로세스 및 서버리스 함수)에서 연결을 관리하는 방법은 [connection management guide](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections)를 참고하세요.

이 페이지에서 답하는 질문

- 언제 $connect와 $disconnect를 호출해야 하나요?
- Prisma는 connection pool을 어떻게 관리하나요?
- 서버리스에서 연결을 어떻게 처리하나요?

## `$connect()`

_lazy connect_ 동작 덕분에 [`$connect()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference)를 호출할 필요는 없습니다. `PrismaClient` 인스턴스는 API에 첫 요청이 들어올 때 지연 연결되며(내부적으로 `$connect()`가 호출됨), 필요 시점에 연결이 이루어집니다.

- `$connect()` 명시적으로 호출하기

첫 요청이 즉시 응답해야 하고 지연 연결이 설정될 때까지 기다릴 수 없다면, `prisma.$connect()`를 명시적으로 호출해 데이터 소스 연결을 미리 설정할 수 있습니다.

```
    const prisma = new PrismaClient();

    // run inside `async` function
    await prisma.$connect();
```

## `$disconnect()`

[`$disconnect()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference)를 호출하면 Prisma Client는 다음을 수행합니다.

1. [`beforeExit` hook](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#exit-hooks)을 실행합니다.
2. pool 내 모든 연결을 닫습니다.

요청을 지속적으로 처리하는 GraphQL API 같은 장기 실행 애플리케이션에서는 요청마다 `$disconnect()`를 호출하는 것이 적절하지 않습니다. 연결을 설정하는 데 시간이 걸리며, 이를 요청 처리의 일부로 매번 수행하면 애플리케이션이 느려집니다.

장기 실행 애플리케이션에서 연결이 _너무_ 많아지는 것을 방지하려면, [애플리케이션 전역에서 단일 `PrismaClient` 인스턴스를 사용](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction#use-prisma-client-to-send-queries-to-your-database)하는 것을 권장합니다.

- `$disconnect()` 명시적으로 호출하기

대부분의 장기 실행 또는 서버리스 앱에서는 연결 재사용을 위해 요청마다 `$disconnect()`를 호출하면 **안 됩니다**. 하지만 일부 상황에서는 명시적으로 호출하는 것이 **타당합니다**. 예를 들어, 임시 `PrismaClient`를 생성한 뒤 즉시 리소스를 해제해야 하는 경우입니다(예: [Cloudflare Workers](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare)에서 `ctx.waitUntil(prisma.$disconnect())` 권장).

또 다른 시나리오는 다음과 같은 스크립트입니다.

1. **드물게** 실행됩니다(예: 매일 밤 이메일을 보내는 예약 작업). 즉, 데이터베이스에 대한 장기 연결의 이점을 얻기 어렵습니다. _그리고_
2. **장기 실행 애플리케이션** 컨텍스트(예: 백그라운드 서비스)에서 존재합니다. 애플리케이션이 종료되지 않으면 Prisma Client도 연결을 해제하지 않습니다.

다음 스크립트는 `PrismaClient`의 새 인스턴스를 생성하고 작업을 수행한 뒤 연결을 해제하며, 이때 connection pool이 닫힙니다.

```
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient();
    const emailService = new EmailService();

    async function main() {
      const allUsers = await prisma.user.findMany();
      const emails = allUsers.map((x) => x.email);

      await emailService.send(emails, "Hello!");
    }

    main()
      .then(async () => {
        await prisma.$disconnect();
      })
      .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
      });
```

위 스크립트가 장기 실행 애플리케이션 컨텍스트에서 `$disconnect()` 호출 _없이_ 여러 번 실행되면, `PrismaClient`의 새 인스턴스가 생성될 때마다 새로운 connection pool이 만들어집니다.

## 종료 hook

`beforeExit` hook은 Prisma ORM이 외부에서(예: `SIGINT` signal을 통해) 종료 트리거될 때 실행되며, Prisma Client가 연결을 해제하기 _전에_ 코드를 실행할 수 있게 해줍니다. 예를 들어 서비스의 graceful shutdown 과정에서 쿼리를 실행할 수 있습니다.

```
    const prisma = new PrismaClient();

    prisma.$on("beforeExit", async () => {
      console.log("beforeExit hook");
      // PrismaClient still available
      await prisma.message.create({
        data: {
          message: "Shutting down server",
        },
      });
    });
```
