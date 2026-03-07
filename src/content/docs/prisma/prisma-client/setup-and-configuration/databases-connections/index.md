---
title: "데이터베이스 연결"
description: "데이터베이스 연결을 관리하고 connection pool을 구성하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections

# 데이터베이스 연결

데이터베이스 연결을 관리하고 connection pool을 구성하는 방법을 알아보세요.

데이터베이스는 동시에 처리할 수 있는 연결 수에 제한이 있습니다. 각 연결은 RAM을 필요로 하므로, 사용 가능한 리소스를 확장하지 않은 채 데이터베이스 연결 한도만 단순히 늘리면 다음과 같은 문제가 생깁니다.

- ✔ 더 많은 프로세스의 연결을 허용할 수는 _있지만_
- ✘ **데이터베이스 성능**에 큰 영향을 주며, **시스템 리소스 고갈**로 인해 데이터베이스가 **중단**될 수 있습니다.

애플리케이션이 **연결을 관리하는 방식**도 성능에 영향을 줍니다. 이 가이드는 [서버리스 환경](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)과 [장기 실행 프로세스](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#long-running-processes)에서 연결 관리를 어떻게 접근해야 하는지 설명합니다.

이 가이드는 **관계형 데이터베이스**와 Prisma ORM connection pool의 구성 및 튜닝 방법에 초점을 둡니다(MongoDB는 MongoDB 드라이버 connection pool 사용).

## 장기 실행 프로세스

장기 실행 프로세스의 예로는 Heroku 같은 서비스나 가상 머신에서 호스팅되는 Node.js 애플리케이션이 있습니다. 장기 실행 환경에서의 연결 관리를 위해 아래 체크리스트를 참고하세요.

- 드라이버 어댑터에 맞게 [pool size and timeouts](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)를 구성하세요(기본값과 옵션은 어댑터별로 다름).
- [전역 `PrismaClient` 인스턴스를 **하나만**](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prismaclient-in-long-running-applications) 사용하도록 하세요.

* 장기 실행 애플리케이션에서의 `PrismaClient`

**장기 실행** 애플리케이션에서는 다음을 권장합니다.

- ✔ `PrismaClient` 인스턴스를 **하나만** 생성하고 애플리케이션 전반에서 재사용
- ✔ _개발 환경에서만_ `PrismaClient`를 전역 변수에 할당하여 [hot reloading으로 새 인스턴스가 생성되는 것을 방지](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#prevent-hot-reloading-from-creating-new-instances-of-prismaclient)

#

- 단일 `PrismaClient` 인스턴스 재사용

단일 인스턴스를 재사용하려면 `PrismaClient` 객체를 export하는 모듈을 만드세요.

client.ts

```
    import { PrismaClient } from "../prisma/generated/client";

    let prisma = new PrismaClient();

    export default prisma;
```

모듈이 처음 import될 때 객체가 [cached](https://nodejs.org/api/modules.html#modules_caching)됩니다. 이후 요청에서는 새 `PrismaClient`를 생성하는 대신 캐시된 객체를 반환합니다.

app.ts

```
    import prisma from "./client";

    async function main() {
      const allUsers = await prisma.user.findMany();
    }

    main();
```

위 예제를 정확히 그대로 복제할 필요는 없습니다. 목표는 `PrismaClient`가 캐시되도록 만드는 것입니다. 예를 들어 Express 앱에 [전달하는](https://github.com/prisma/prisma-examples/blob/9f1a6b9e7c25b9e1851bd59b273046158d748995/typescript/graphql-express/src/server.ts#L12) `context` 객체에서 [`PrismaClient`를 instantiate](https://github.com/prisma/prisma-examples/blob/9f1a6b9e7c25b9e1851bd59b273046158d748995/typescript/graphql-express/src/context.ts#L9)할 수 있습니다.

#

- `$disconnect()`를 명시적으로 호출하지 마세요

요청을 계속 처리하는 장기 실행 애플리케이션 맥락에서는 [`$disconnect()`를 명시적으로 호출할 필요가 없습니다](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#calling-disconnect-explicitly). 새 연결을 여는 데는 시간이 걸리며, 각 쿼리 후 연결을 끊으면 애플리케이션이 느려질 수 있습니다.

#

- hot reloading으로 `PrismaClient`의 새 인스턴스가 생성되지 않게 하기

[Next.js](https://nextjs.org/) 같은 프레임워크는 변경된 파일의 hot reloading을 지원하여 재시작 없이 애플리케이션 변경 사항을 확인할 수 있게 해줍니다. 하지만 `PrismaClient`를 export하는 모듈이 새로고침되면, **개발 환경에서 원치 않는`PrismaClient` 추가 인스턴스**가 생길 수 있습니다.

우회 방법으로, 전역 변수는 다시 로드되지 않으므로 개발 환경에서만 `PrismaClient`를 전역 변수로 저장할 수 있습니다.

client.ts

```
    import { PrismaClient } from "../prisma/generated/client";

    const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };

    export const prisma = globalForPrisma.prisma || new PrismaClient();

    if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

Prisma Client를 import하고 사용하는 방식은 바뀌지 않습니다.

app.ts

```
    import { prisma } from "./client";

    async function main() {
      const allUsers = await prisma.user.findMany();
    }

    main();
```

## CLI 명령당 생성되는 연결 수

Postgres, MySQL, SQLite에 대한 로컬 테스트에서 각 Prisma CLI 명령은 일반적으로 단일 연결을 사용합니다. 아래 표는 해당 테스트에서 관찰된 범위를 보여줍니다. 환경에 따라 결과가 약간 다를 _수 있습니다_.

| Command                                                                                           | Connections | Description                                    |
| ------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------- |
| [`migrate status`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-status) | 1           | 마이그레이션 상태 확인                         |
| [`migrate dev`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-dev)       | 1–4         | 개발 환경에서 대기 중인 마이그레이션 적용      |
| [`migrate diff`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-diff)     | 1–2         | 데이터베이스 스키마와 마이그레이션 이력 비교   |
| [`migrate reset`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-reset)   | 1–2         | 데이터베이스 초기화 후 마이그레이션 재적용     |
| [`migrate deploy`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-deploy) | 1–2         | 프로덕션에서 대기 중인 마이그레이션 적용       |
| [`db pull`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-pull)               | 1           | 데이터베이스 스키마를 Prisma schema로 가져오기 |
| [`db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push)               | 1–2         | Prisma schema를 데이터베이스에 반영            |
| [`db execute`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-execute)         | 1           | raw SQL 명령 실행                              |
| [`db seed`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-seed)               | 1           | 초기 데이터로 데이터베이스 시드                |

## 서버리스 환경 (FaaS)

서버리스 환경의 예로는 AWS Lambda, Vercel, Netlify Functions에 호스팅된 Node.js 함수가 있습니다. 서버리스 환경의 연결 관리를 위해 아래 체크리스트를 참고하세요.

- [서버리스 연결 관리 과제](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#the-serverless-challenge)를 숙지하세요.
- 드라이버 어댑터에 맞게 [pool size and timeouts](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)를 구성하세요(기본값과 옵션은 어댑터별로 다름).
- [`PrismaClient`를 handler 외부에서 instantiate](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#instantiate-prismaclient-outside-the-handler)하고 `$disconnect()`를 명시적으로 호출하지 마세요.
- [함수 동시성](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#concurrency-limits)을 구성하고 [idle connections](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#zombie-connections)을 처리하세요.

* 서버리스 과제

서버리스 환경에서는 각 함수가 `PrismaClient`의 **자체 인스턴스**를 만들고, 각 클라이언트 인스턴스는 자체 connection pool을 가집니다.

다음 예시를 보세요. 하나의 AWS Lambda 함수가 `PrismaClient`를 사용해 데이터베이스에 연결하며 `connection_limit`은 **3** 입니다.

![데이터베이스에 연결하는 AWS Lambda 함수.](https://docs.prisma.io/docs/img/orm/prisma-client/setup-and-configuration/databases-connections/serverless-connections.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

트래픽 급증으로 AWS Lambda가 증가한 부하를 처리하기 위해 Lambda 두 개를 추가로 생성합니다. 각 Lambda는 `PrismaClient` 인스턴스를 생성하고, 각각 `connection_limit` **3** 을 가지므로 데이터베이스에 대한 최대 연결 수는 **9** 가 됩니다.

![데이터베이스에 연결하는 세 개의 AWS Lambda 함수.](https://docs.prisma.io/docs/img/orm/prisma-client/setup-and-configuration/databases-connections/serverless-connections-2.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

트래픽 급증 📈 에 대응하는 _동시 함수_ 수가 많아지면 데이터베이스 연결 한도를 매우 빠르게 소진할 수 있습니다. 또한 **일시 중지된** 함수도 기본적으로 연결을 열린 상태로 유지하여 다른 함수가 해당 연결을 사용하지 못하게 막습니다.

1. [driver adapter](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)에 대해 작은 pool size를 설정하세요(어댑터별로 다름, pooler를 사용하지 않는 경우 작게 시작).
2. 함수당 더 많은 연결이 필요하면 [PgBouncer 같은 외부 connection pooler](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#external-connection-poolers) 사용을 고려하세요.

- 서버리스 환경에서의 `PrismaClient`

#

- handler 외부에서 `PrismaClient` instantiate

재사용 가능성을 높이려면 함수 handler 범위 [외부에서 `PrismaClient`를 instantiate](https://github.com/prisma/e2e-tests/blob/5d1041d3f19245d3d237d959eca94d1d796e3a52/platforms/serverless-lambda/index.ts#L3)하세요. handler가 'warm'(사용 중) 상태를 유지하는 한, 연결은 재사용될 가능성이 있습니다.

```
    import { PrismaClient } from "../prisma/generated/client";

    const client = new PrismaClient();

    export async function handler() {
      /* ... */
    }
```

#

- `$disconnect()`를 명시적으로 호출하지 마세요

함수 끝에서 [`$disconnect()`를 명시적으로 호출할 필요가 없습니다](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#calling-disconnect-explicitly). 컨테이너가 재사용될 가능성이 있기 때문입니다. 새 연결을 여는 데는 시간이 걸리며 함수의 요청 처리 능력을 저하시킵니다. 일부 경우(예: [Cloudflare Workers](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare))에는 임시 클라이언트를 해제할 때 `$disconnect()` 호출이 권장됩니다. 자세한 내용은 [connection management caveat](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management#calling-disconnect-explicitly)를 참고하세요.

- 기타 서버리스 고려 사항

#

- 컨테이너 재사용

함수의 이후 근접 호출이 동일한 컨테이너에 도달한다는 보장은 없습니다. 예를 들어 AWS는 언제든 새 컨테이너를 생성할 수 있습니다.

코드는 컨테이너가 상태 비저장(stateless)임을 전제로 하며, 연결이 존재하지 않을 때만 연결을 생성해야 합니다 - Prisma Client JS는 이미 이 로직을 구현하고 있습니다.

#

- 좀비 연결

"to be removed"로 표시되었고 재사용되지 않는 컨테이너도 여전히 **연결을 열린 상태로 유지**하며, 일정 시간(기간은 AWS에서 알려지지 않았고 문서화되지 않음) 이런 상태로 남아 있을 수 있습니다. 이로 인해 데이터베이스 연결을 비효율적으로 사용할 수 있습니다.

가능한 해결책은 **유휴 연결을 정리**하는 것입니다 ([`serverless-mysql`](https://github.com/jeremydaly/serverless-mysql)이 이 아이디어를 구현하지만, Prisma ORM과 함께 사용할 수는 없습니다).

#

- 동시성 한도

serverless 동시성 한도(병렬로 실행되는 serverless 함수 수)에 따라, 여전히 데이터베이스의 연결 한도를 소진할 수 있습니다. 이는 너무 많은 함수가 동시에 호출되고, 각 함수가 자체 연결 풀을 가지며, 결국 데이터베이스 연결 한도를 고갈시킬 때 발생할 수 있습니다. 이를 방지하려면, [serverless 동시성 한도 설정](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)을 데이터베이스 최대 연결 한도를 각 함수 호출에서 사용하는 연결 수로 나눈 값보다 낮게 설정할 수 있습니다(다른 용도로 다른 클라이언트에서도 연결할 수 있어야 할 수 있기 때문입니다).

## 연결 풀 최적화

Prisma Client가 어댑터의 acquire timeout 전에 풀에서 연결을 얻지 못하면 로그에 connection pool timeout 예외가 표시됩니다. connection pool timeout은 다음과 같은 경우에 발생할 수 있습니다:

- 많은 사용자가 동시에 앱에 접근하는 경우
- 대량의 쿼리를 병렬로 전송하는 경우(예: `await Promise.all()` 사용)

풀 크기, acquire timeout, 기타 풀 동작은 **드라이버 어댑터별로 구성**되며, Prisma ORM v7에서는 이를 위한 connection URL parameter가 없습니다. 각 어댑터의 풀 설정(예: `pg`의 `max`, `connectionTimeoutMillis`)과 기반 드라이버 문서는 [connection pool reference](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)를 확인하세요. 다음을 만족하도록 풀을 튜닝하세요:

- 데이터베이스가 총 동시 연결 수(풀 크기 × 인스턴스 수)를 지원할 수 있어야 함
- timeout 및 queue 동작이 워크로드와 일치해야 함(예: queue가 무한정 증가해 시스템 리소스가 고갈되지 않도록)

## 외부 연결 풀러

PgBouncer 같은 connection pooler는 애플리케이션이 데이터베이스 연결 한도를 소진하지 않도록 도와줍니다.

Prisma Client는 pooled connection을 유지하면서 Prisma CLI 명령(예: migration 또는 introspection)은 직접 연결할 수 있게 하려면, 두 개의 환경 변수를 정의하세요:

.env

```
    # Connection URL to your database using PgBouncer.
    DATABASE_URL="postgres://root:password@127.0.0.1:54321/postgres?pgbouncer=true"

    # Direct connection URL to the database used for Prisma CLI commands.
    DIRECT_URL="postgres://root:password@127.0.0.1:5432/postgres"
```

`prisma.config.ts`가 direct connection string을 가리키도록 구성하세요. Prisma CLI 명령은 항상 이 구성을 읽습니다.

prisma.config.ts

```
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      datasource: {
        url: env("DIRECT_URL"),
      },
    });
```

런타임에서는 pooled connection string을 사용하는 드라이버 어댑터(예: `@prisma/adapter-pg`)로 Prisma Client를 인스턴스화하세요:

src/db/client.ts

```
    import { PrismaClient } from "../prisma/generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });
    export const prisma = new PrismaClient({ adapter });
```

- PgBouncer

PostgreSQL은 동시 연결 수를 일정량만 지원하며, 서비스 사용량이 증가하면 이 한도에 매우 빠르게 도달할 수 있습니다. 특히 [serverless environments](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)에서는 더 그렇습니다.

[PgBouncer](https://www.pgbouncer.org/)는 데이터베이스에 대한 connection pool을 유지하고, Prisma Client와 데이터베이스 사이에서 중간 프록시 역할을 하며 들어오는 클라이언트 연결을 프록시합니다. 이렇게 하면 데이터베이스가 특정 시점에 처리해야 하는 프로세스 수가 줄어듭니다. PgBouncer는 데이터베이스로 전달하는 연결 수를 제한하고, 연결이 사용 가능해지면 전달하기 위해 추가 연결을 큐에 대기시킵니다. PgBouncer 사용 방법은 [Configure Prisma Client with PgBouncer](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/pgbouncer)를 참고하세요.

- AWS RDS Proxy

AWS RDS Proxy가 연결을 고정(pin)하는 방식 때문에, Prisma Client와 함께 사용할 경우 [connection pooling 이점을 제공하지 않습니다](https://docs.prisma.io/docs/orm/prisma-client/deployment/caveats-when-deploying-to-aws-platforms#aws-rds-proxy).
