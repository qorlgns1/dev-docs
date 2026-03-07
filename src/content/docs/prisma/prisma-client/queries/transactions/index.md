---
title: "트랜잭션 및 배치 쿼리"
description: "이 페이지에서는 Prisma Client의 트랜잭션 API를 설명합니다."
---

# 트랜잭션 및 배치 쿼리

이 페이지에서는 Prisma Client의 트랜잭션 API를 설명합니다.

데이터베이스 트랜잭션은 읽기/쓰기 작업의 연속으로, 전체가 하나로 성공하거나 실패하도록 보장됩니다(ACID 속성: Atomic, Consistent, Isolated, Durable).

Prisma Client는 여러 방식으로 트랜잭션을 지원합니다:

| 시나리오         | 기법                              |
| ---------------- | --------------------------------- |
| 종속 쓰기        | 중첩 쓰기                         |
| 독립 쓰기        | `$transaction([])` API, 배치 작업 |
| 읽기, 수정, 쓰기 | 인터랙티브 트랜잭션               |

## 중첩 쓰기

[중첩 쓰기](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes)는 관련 레코드에 대한 여러 작업을 단일 트랜잭션에서 수행합니다:

```
    // Create user with posts in a single transaction
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        posts: {
          create: [{ title: "Post 1" }, { title: "Post 2" }],
        },
      },
    });
```

## 배치 작업

다음 대량 작업은 트랜잭션으로 실행됩니다:

- `createMany()` / `createManyAndReturn()`
- `updateMany()` / `updateManyAndReturn()`
- `deleteMany()`

## `$transaction` API

- 순차 작업

트랜잭션에서 순차적으로 실행할 쿼리 배열을 전달합니다:

```
    const [posts, totalPosts] = await prisma.$transaction([
      prisma.post.findMany({ where: { title: { contains: "prisma" } } }),
      prisma.post.count(),
    ]);
```

옵션 포함:

```
    await prisma.$transaction(
      [prisma.resource.deleteMany({ where: { name: "name" } }), prisma.resource.createMany({ data })],
      { isolationLevel: Prisma.TransactionIsolationLevel.Serializable },
    );
```

- 인터랙티브 트랜잭션

쿼리 사이에 복잡한 로직이 필요한 경우 인터랙티브 트랜잭션을 사용합니다:

```
    const result = await prisma.$transaction(async (tx) => {
      const sender = await tx.account.update({
        data: { balance: { decrement: 100 } },
        where: { email: "alice@prisma.io" },
      });

      if (sender.balance < 0) {
        throw new Error("Insufficient funds");
      }

      return await tx.account.update({
        data: { balance: { increment: 100 } },
        where: { email: "bob@prisma.io" },
      });
    });
```

트랜잭션은 짧게 유지하세요. 오래 실행되는 트랜잭션은 성능을 저하시킬 수 있고 데드락을 유발할 수 있습니다.

**옵션:**

```
    await prisma.$transaction(
      async (tx) => {
        /* ... */
      },
      {
        maxWait: 5000, // Max wait to acquire transaction (default: 2000ms)
        timeout: 10000, // Max transaction run time (default: 5000ms)
        isolationLevel: Prisma.TransactionIsolationLevel.Serializable,
      },
    );
```

- 트랜잭션 격리 수준

이 기능은 MongoDB에서는 사용할 수 없습니다. MongoDB는 격리 수준을 지원하지 않기 때문입니다.

트랜잭션의 [격리 수준](https://www.prisma.io/dataguide/intro/database-glossary#isolation-levels)을 설정할 수 있습니다.

#

- 격리 수준 설정

트랜잭션 격리 수준을 설정하려면 API의 두 번째 매개변수에서 `isolationLevel` 옵션을 사용하세요.

순차 작업의 경우:

```
    await prisma.$transaction(
      [
        // Prisma Client operations running in a transaction...
      ],
      {
        isolationLevel: Prisma.TransactionIsolationLevel.Serializable, // optional, default defined by database configuration
      },
    );
```

인터랙티브 트랜잭션의 경우:

```
    await prisma.$transaction(
      async (prisma) => {
        // Code running in a transaction...
      },
      {
        isolationLevel: Prisma.TransactionIsolationLevel.Serializable, // optional, default defined by database configuration
        maxWait: 5000, // default: 2000
        timeout: 10000, // default: 5000
      },
    );
```

#

- 지원되는 격리 수준

Prisma Client는 기본 데이터베이스에서 사용 가능한 경우 다음 격리 수준을 지원합니다:

- `ReadUncommitted`
- `ReadCommitted`
- `RepeatableRead`
- `Snapshot`
- `Serializable`

각 데이터베이스 커넥터에서 사용 가능한 격리 수준은 다음과 같습니다:

| 데이터베이스 | `ReadUncommitted` | `ReadCommitted` | `RepeatableRead` | `Snapshot` | `Serializable` |
| ------------ | ----------------- | --------------- | ---------------- | ---------- | -------------- |
| PostgreSQL   | ✔️                | ✔️              | ✔️               | No         | ✔️             |
| MySQL        | ✔️                | ✔️              | ✔️               | No         | ✔️             |
| SQL Server   | ✔️                | ✔️              | ✔️               | ✔️         | ✔️             |
| CockroachDB  | No                | No              | No               | No         | ✔️             |
| SQLite       | No                | No              | No               | No         | ✔️             |

기본적으로 Prisma Client는 데이터베이스에 현재 구성된 값을 격리 수준으로 설정합니다.

각 데이터베이스에 기본으로 구성된 격리 수준은 다음과 같습니다:

| 데이터베이스 | 기본값           |
| ------------ | ---------------- |
| PostgreSQL   | `ReadCommitted`  |
| MySQL        | `RepeatableRead` |
| SQL Server   | `ReadCommitted`  |
| CockroachDB  | `Serializable`   |
| SQLite       | `Serializable`   |

#

- 격리 수준에 대한 데이터베이스별 정보

다음 리소스를 참고하세요:

- PostgreSQL의 트랜잭션 격리 수준
- Microsoft SQL Server의 트랜잭션 격리 수준
- MySQL의 트랜잭션 격리 수준

CockroachDB와 SQLite는 `Serializable` 격리 수준만 지원합니다.

- 트랜잭션 타이밍 이슈
  - 이 섹션의 해결 방법은 MongoDB에는 적용되지 않습니다. MongoDB는 [격리 수준](https://www.prisma.io/dataguide/intro/database-glossary#isolation-levels)을 지원하지 않기 때문입니다.
  - 이 섹션에서 다루는 타이밍 이슈는 CockroachDB와 SQLite에는 적용되지 않습니다. 이 데이터베이스들은 가장 높은 `Serializable` 격리 수준만 지원하기 때문입니다.

둘 이상의 트랜잭션이 특정 [격리 수준](https://www.prisma.io/dataguide/intro/database-glossary#isolation-levels)에서 동시에 실행되면, 타이밍 이슈로 인해 고유 제약 조건 위반과 같은 쓰기 충돌 또는 데드락이 발생할 수 있습니다. 예를 들어 트랜잭션 A와 트랜잭션 B가 모두 `deleteMany`와 `createMany` 작업을 실행하려고 하는 다음 이벤트 순서를 생각해 보겠습니다:

1. 트랜잭션 B: `createMany` 작업이 새 행 집합을 생성합니다.
2. 트랜잭션 B: 애플리케이션이 트랜잭션 B를 커밋합니다.
3. 트랜잭션 A: `createMany` 작업.
4. 트랜잭션 A: 애플리케이션이 트랜잭션 A를 커밋합니다. 새 행이 2단계에서 트랜잭션 B가 추가한 행과 충돌합니다.

이 충돌은 PostgreSQL과 Microsoft SQL Server의 기본 격리 수준인 `ReadCommitted`에서 발생할 수 있습니다. 이 문제를 피하려면 더 높은 격리 수준(`RepeatableRead` 또는 `Serializable`)을 설정할 수 있습니다. 트랜잭션 단위로 격리 수준을 설정할 수 있으며, 이 경우 해당 트랜잭션에서는 데이터베이스 기본 격리 수준을 덮어씁니다.

트랜잭션에서 쓰기 충돌과 데드락을 방지하려면:

1. 트랜잭션에서 `isolationLevel` 매개변수를 `Prisma.TransactionIsolationLevel.Serializable`로 사용합니다.

이렇게 하면 애플리케이션이 여러 동시 또는 병렬 트랜잭션을 직렬로 실행된 것처럼 커밋하도록 보장됩니다. 쓰기 충돌 또는 데드락으로 트랜잭션이 실패하면 Prisma Client는 [P2034 오류](https://docs.prisma.io/docs/orm/reference/error-reference#p2034)를 반환합니다.

2. 애플리케이션 코드에서 아래 예시처럼 트랜잭션 주위에 재시도 로직을 추가해 P2034 오류를 처리합니다:

```
import { Prisma, PrismaClient } from "../prisma/generated/client";

         const prisma = new PrismaClient();
         async function main() {
           const MAX_RETRIES = 5;
           let retries = 0;

           let result;
           while (retries < MAX_RETRIES) {
             try {
               result = await prisma.$transaction(
                 [
                   prisma.user.deleteMany({
                     where: {
                       /** args */
                     },
                   }),
                   prisma.post.createMany({
                     data: {
                       /** args */
                     },
                   }),
                 ],
                 {
                   isolationLevel: Prisma.TransactionIsolationLevel.Serializable,
                 },
               );
               break;
             } catch (error) {
               if (error.code === "P2034") {
                 retries++;
                 continue;
               }
               throw error;
             }
           }
         }
```

- `Promise.all()` 내에서 `$transaction` 사용

`Promise.all()` 호출 안에 `$transaction`을 감싸면, 트랜잭션 내부 쿼리는 _직렬로_ 실행됩니다(즉, 하나씩 순서대로):

```
    await prisma.$transaction(async (prisma) => {
      await Promise.all([
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
        prisma.user.findMany(),
      ]);
    });
```

이는 `Promise.all()`이 보통 전달된 호출을 *병렬화*한다는 점에서 직관에 반할 수 있습니다.

이 동작의 이유는 다음과 같습니다:

- 하나의 트랜잭션은 내부의 모든 쿼리가 동일한 연결에서 실행되어야 함을 의미합니다.
- 데이터베이스 연결은 한 번에 하나의 쿼리만 실행할 수 있습니다.
- 하나의 쿼리가 작업 중일 때 연결을 점유하므로, `Promise.all`에 트랜잭션을 넣으면 사실상 쿼리를 순차적으로 실행하게 됩니다.

## 종속 쓰기

작업이 이전 작업의 결과(예: 데이터베이스가 생성한 ID 사용)에 의존할 때 쓰기는 **종속적**입니다.

- 종속 작업을 위한 중첩 쓰기

관련 레코드를 원자적으로 생성해야 할 때 중첩 쓰기를 사용합니다:

```
    const team = await prisma.team.create({
      data: {
        name: "Aurora Adventures",
        members: {
          create: { email: "alice@prisma.io" },
        },
      },
    });
```

어떤 작업이든 실패하면 Prisma Client는 전체 트랜잭션을 롤백합니다.

`$transaction([])` API는 작업 간에 ID를 전달할 수 없습니다. 한 레코드에서 생성된 ID로 다른 레코드를 생성해야 하면 중첩 쓰기를 사용하세요.

## 독립 쓰기

쓰기 작업이 이전 작업 결과에 의존하지 않으면 **독립적**입니다. 다음과 같은 경우에 사용하세요:

- 여러 주문의 상태를 "Dispatched"로 업데이트
- 이메일 목록을 "Read"로 표시

* 대량 작업

```
    const updateUsers = await prisma.user.updateMany({
      where: { email: { contains: "prisma.io" } },
      data: { role: "ADMIN" },
    });
```

### 독립 쓰기에 `$transaction([])` 사용

```
    const [deleteResult, createResult] = await prisma.$transaction([
      prisma.post.deleteMany({ where: { authorId: 7 } }),
      prisma.user.delete({ where: { id: 7 } }),
    ]);
```

### 시나리오: 사전 계산된 ID와 `$transaction([])` API

ID를 미리 계산하는 경우(예: UUID 사용), 두 작업 모두 ID를 사전에 알고 있으므로 중첩 쓰기나 `$transaction([])`를 모두 사용할 수 있습니다.

#

- 대량 작업을 사용해야 하는 경우

다음과 같은 경우 대량 작업을 해결책으로 고려하세요:

- ✔ 이메일 배치처럼 *같은 유형*의 레코드 배치를 업데이트하려는 경우

#

- 시나리오: 이메일을 읽음으로 표시

gmail.com과 같은 서비스를 구축 중이고, 고객이 사용자가 모든 이메일을 읽음으로 표시할 수 있는 **"Mark as read"** 기능을 원한다고 가정해 보겠습니다. 각 이메일 상태 업데이트는 이메일끼리 서로 의존하지 않으므로 독립 쓰기입니다. 예를 들어 이모가 보낸 "Happy Birthday! 🍰" 이메일은 IKEA 프로모션 이메일과 관련이 없습니다.

다음 스키마에서 `User`는 수신한 이메일을 여러 개 가질 수 있습니다(일대다 관계):

```
    model User {
      id    Int       @id @default(autoincrement())
      email           String @unique
      receivedEmails  Email[] // Many emails
    }

    model Email {
      id      Int     @id @default(autoincrement())
      user    User    @relation(fields: [userId], references: [id])
      userId  Int
      subject String
      body    String
      unread  Boolean
    }
```

이 스키마를 기반으로 `updateMany`를 사용해 읽지 않은 모든 이메일을 읽음으로 표시할 수 있습니다:

```
    await prisma.email.updateMany({
      where: {
        user: {
          id: 10,
        },
        unread: true,
      },
      data: {
        unread: false,
      },
    });
```

#

- 대량 작업에서 중첩 쓰기를 사용할 수 있나요?

아니요. 현재 `updateMany`와 `deleteMany` 모두 중첩 쓰기를 지원하지 않습니다. 예를 들어 여러 팀과 해당 팀의 모든 멤버를 함께 삭제하는 것(연쇄 삭제)은 할 수 없습니다:

```
    await prisma.team.deleteMany({
      where: {
        id: {
          in: [2, 99, 2, 11],
        },
      },
      data: {
        members: {}, // Cannot access members here
      },
    });
```

#

### 대량 작업을 `$transaction([])` API와 함께 사용할 수 있나요?

예. 예를 들어 여러 `deleteMany` 작업을 `$transaction([])` 안에 포함할 수 있습니다.

### `$transaction([])` API

`$transaction([])` API는 독립 쓰기에 대한 범용 솔루션으로, 여러 작업을 단일 원자 작업으로 실행할 수 있게 해줍니다. 어떤 작업이든 실패하면 Prisma Client가 전체 트랜잭션을 롤백합니다.

또한 작업은 트랜잭션에 배치된 순서대로 실행된다는 점도 중요합니다.

```
    await prisma.$transaction([iRunFirst, iRunSecond, iRunThird]);
```

> **참고** : 트랜잭션에서 쿼리를 사용하더라도 쿼리 자체 내부의 작업 순서에는 영향을 주지 않습니다.

Prisma Client가 발전함에 따라 `$transaction([])` API의 사용 사례는 점점 더 특화된 대량 작업(`createMany` 등)과 중첩 쓰기로 대체될 것입니다.

#

### `$transaction([])` API를 사용해야 하는 경우

다음과 같은 경우 `$transaction([])` API를 고려하세요:

- ✔ 이메일과 사용자처럼 서로 다른 유형의 레코드가 포함된 배치를 업데이트하려는 경우. 레코드 간에 관계가 있을 필요는 없습니다.
- ✔ 원시 SQL 쿼리(`$executeRaw`)를 배치로 실행하려는 경우. 예를 들어 Prisma Client가 아직 지원하지 않는 기능을 구현할 때 유용합니다.

#

- 시나리오: 개인정보 보호 법규

GDPR 및 기타 개인정보 보호 법률은 사용자가 조직에 자신의 모든 개인 데이터를 삭제해 달라고 요청할 권리를 부여합니다. 다음 예시 스키마에서 `User`는 여러 게시물과 개인 메시지를 가질 수 있습니다:

```
    model User {
      id              Int              @id @default(autoincrement())
      posts           Post[]
      privateMessages PrivateMessage[]
    }

    model Post {
      id      Int    @id @default(autoincrement())
      user    User   @relation(fields: [userId], references: [id])
      userId  Int
      title   String
      content String
    }

    model PrivateMessage {
      id      Int    @id @default(autoincrement())
      user    User   @relation(fields: [userId], references: [id])
      userId  Int
      message String
    }
```

사용자가 잊힐 권리를 행사하면 세 가지 레코드를 삭제해야 합니다: 사용자 레코드, 개인 메시지, 게시물. _모든_ 삭제 작업이 함께 성공하거나 전혀 수행되지 않아야 하므로, 이는 트랜잭션의 대표적인 사용 사례입니다. 하지만 이 시나리오에서는 세 개의 모델에 걸쳐 삭제해야 하므로 `deleteMany` 같은 단일 대량 작업을 사용할 수 없습니다. 대신 `$transaction([])` API를 사용해 세 작업을 함께 실행할 수 있습니다. 즉, `deleteMany` 두 번과 `delete` 한 번입니다:

```
    const id = 9; // User to be deleted

    const deletePosts = prisma.post.deleteMany({
      where: {
        userId: id,
      },
    });

    const deleteMessages = prisma.privateMessage.deleteMany({
      where: {
        userId: id,
      },
    });

    const deleteUser = prisma.user.delete({
      where: {
        id: id,
      },
    });

    await prisma.$transaction([deletePosts, deleteMessages, deleteUser]); // Operations succeed or fail together
```

#

### 시나리오: 사전 계산된 ID와 `$transaction([])` API

`$transaction([])` API는 종속 쓰기(dependent writes)를 지원하지 않습니다. 작업 A가 작업 B에서 생성된 ID에 의존한다면 [nested writes](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#nested-writes)를 사용하세요. 그러나 ID를 *사전 계산*했다면(예: GUID 생성), 쓰기 작업은 독립적이 됩니다. nested writes 예제의 회원가입 흐름을 살펴보겠습니다:

```
    await prisma.team.create({
      data: {
        name: "Aurora Adventures",
        members: {
          create: {
            email: "alice@prisma.io",
          },
        },
      },
    });
```

ID를 자동 생성하는 대신 `Team`과 `User`의 `id` 필드를 `String`으로 변경합니다(값을 제공하지 않으면 UUID가 자동 생성됨). 이 예제는 UUID를 사용합니다:

```
    model Team {
      id      Int    @id @default(autoincrement())
      id      String @id @default(uuid())
      name    String
      members User[]
    }

    model User {
      id    Int    @id @default(autoincrement())
      id    String @id @default(uuid())
      email String @unique
      teams Team[]
    }
```

nested writes 대신 `$transaction([])` API를 사용하도록 회원가입 흐름 예제를 리팩터링합니다:

```
    import { v4 } from "uuid";

    const teamID = v4();
    const userID = v4();

    await prisma.$transaction([
      prisma.user.create({
        data: {
          id: userID,
          email: "alice@prisma.io",
          team: {
            id: teamID,
          },
        },
      }),
      prisma.team.create({
        data: {
          id: teamID,
          name: "Aurora Adventures",
        },
      }),
    ]);
```

원한다면 사전 계산된 API와 함께 nested writes 문법을 계속 사용할 수도 있습니다:

```
    import { v4 } from "uuid";

    const teamID = v4();
    const userID = v4();

    await prisma.team.create({
      data: {
        id: teamID,
        name: "Aurora Adventures",
        members: {
          create: {
            id: userID,
            email: "alice@prisma.io",
            team: {
              id: teamID,
            },
          },
        },
      },
    });
```

이미 자동 생성 ID와 nested writes를 사용 중이라면, 수동 생성 ID와 `$transaction([])` API로 전환해야 할 강력한 이유는 없습니다.

## 읽기, 수정, 쓰기

경우에 따라 원자적 작업의 일부로 사용자 정의 로직을 수행해야 할 수 있으며, 이를 [read-modify-write pattern](https://en.wikipedia.org/wiki/Read%E2%80%93modify%E2%80%93write)이라고도 합니다. 다음은 read-modify-write pattern의 예입니다:

- 데이터베이스에서 값을 읽기
- 해당 값을 조작하는 로직 실행(예: 외부 API 호출)
- 값을 다시 데이터베이스에 쓰기

모든 작업은 데이터베이스에 원치 않는 변경을 남기지 않고 **함께 성공하거나 함께 실패**해야 하지만, 반드시 실제 데이터베이스 트랜잭션을 사용해야 하는 것은 아닙니다. 이 가이드 섹션에서는 Prisma Client와 read-modify-write pattern을 함께 사용하는 두 가지 방법을 설명합니다:

- 멱등 API 설계
- 낙관적 동시성 제어

* 멱등 API

멱등성(idempotency)은 동일한 파라미터로 같은 로직을 여러 번 실행해도 결과가 동일한 성질입니다. 즉, 로직을 한 번 실행하든 천 번 실행하든 **데이터베이스에 미치는 효과**가 같습니다. 예:

- **멱등하지 않음 (NOT IDEMPOTENT)** : 이메일 주소 `"letoya@prisma.io"`로 데이터베이스에서 사용자를 업서트(update-or-insert)합니다. `User` 테이블이 이메일 고유성을 **강제하지 않습니다**. 로직을 한 번 실행하면(사용자 1명 생성)와 열 번 실행하면(사용자 10명 생성) 데이터베이스 효과가 달라집니다.
- **멱등함 (IDEMPOTENT)** : 이메일 주소 `"letoya@prisma.io"`로 데이터베이스에서 사용자를 업서트(update-or-insert)합니다. `User` 테이블이 이메일 고유성을 **강제합니다**. 로직을 한 번 실행하든(사용자 1명 생성) 열 번 실행하든(기존 사용자가 같은 입력으로 업데이트됨) 데이터베이스 효과는 같습니다.

멱등성은 가능하다면 애플리케이션에 적극적으로 설계에 반영할 수 있고, 또 그렇게 해야 하는 특성입니다.

#

- 멱등 API를 설계해야 하는 경우
  - ✔ 데이터베이스에서 원치 않는 부작용 없이 동일한 로직을 재시도할 수 있어야 할 때

#

- 시나리오: Slack 팀 업그레이드

팀이 유료 기능을 잠금 해제할 수 있도록 Slack용 업그레이드 흐름을 만들고 있다고 가정해 보겠습니다. 팀은 여러 요금제 중에서 선택할 수 있으며 사용자당 월 과금됩니다. 결제 게이트웨이로 Stripe를 사용하고, `Team` 모델을 확장해 `stripeCustomerId`를 저장합니다. 구독 관리는 Stripe에서 이루어집니다.

```
    model Team {
      id               Int     @id @default(autoincrement())
      name             String
      User             User[]
      stripeCustomerId String?
    }
```

업그레이드 흐름은 다음과 같습니다:

1. 사용자 수를 계산
2. 사용자 수를 포함한 구독을 Stripe에서 생성
3. 유료 기능을 잠금 해제하기 위해 팀을 Stripe customer ID와 연결

```
    const teamId = 9;
    const planId = "plan_id";

    // Count team members
    const numTeammates = await prisma.user.count({
      where: {
        teams: {
          some: {
            id: teamId,
          },
        },
      },
    });

    // Create a customer in Stripe for plan-9454549
    const customer = await stripe.customers.create({
      externalId: teamId,
      plan: planId,
      quantity: numTeammates,
    });

    // Update the team with the customer id to indicate that they are a customer
    // and support querying this customer in Stripe from our application code.
    await prisma.team.update({
      data: {
        customerId: customer.id,
      },
      where: {
        id: teamId,
      },
    });
```

이 예제에는 문제가 있습니다. 로직을 _한 번만_ 실행할 수 있다는 점입니다. 다음 시나리오를 보겠습니다:

1. Stripe가 새 customer와 구독을 생성하고 customer ID를 반환
2. 팀 업데이트가 **실패** \- Slack 데이터베이스에서 해당 팀이 customer로 표시되지 않음
3. Stripe에서는 고객에게 과금되지만, 팀에 유효한 `customerId`가 없어 Slack에서 유료 기능이 잠금 해제되지 않음
4. 같은 코드를 다시 실행하면 다음 중 하나가 발생:
   - `externalId`로 정의된 팀이 이미 존재해 오류 발생 - Stripe는 customer ID를 반환하지 않음
   - `externalId`에 고유 제약이 없다면 Stripe가 또 다른 구독을 생성함(**멱등하지 않음**)

오류 발생 시 이 코드를 다시 실행할 수 없고, 이중 과금 없이 다른 요금제로 변경할 수도 없습니다.

다음 리팩터링(강조 표시됨)은 구독이 이미 존재하는지 확인하는 메커니즘을 도입하고, 설명(description)을 생성하거나 기존 구독을 업데이트합니다(입력이 동일하면 변경 없음):

```
    // Calculate the number of users times the cost per user
    const numTeammates = await prisma.user.count({
      where: {
        teams: {
          some: {
            id: teamId,
          },
        },
      },
    });

    // Find customer in Stripe
    let customer = await stripe.customers.get({ externalId: teamID });

    if (customer) {
      // If team already exists, update
      customer = await stripe.customers.update({
        externalId: teamId,
        plan: "plan_id",
        quantity: numTeammates,
      });
    } else {
      customer = await stripe.customers.create({
        // If team does not exist, create customer
        externalId: teamId,
        plan: "plan_id",
        quantity: numTeammates,
      });
    }

    // Update the team with the customer id to indicate that they are a customer
    // and support querying this customer in Stripe from our application code.
    await prisma.team.update({
      data: {
        customerId: customer.id,
      },
      where: {
        id: teamId,
      },
    });
```

이제 동일한 입력으로 같은 로직을 여러 번 재시도해도 부작용이 없습니다. 이 예제를 더 개선하려면, 정해진 횟수만큼 시도해도 업데이트가 성공하지 않을 경우 구독을 취소하거나 일시 비활성화하는 메커니즘을 도입할 수 있습니다.

- 낙관적 동시성 제어

낙관적 동시성 제어(OCC)는 단일 엔터티에 대한 동시 작업을 처리하는 모델로, 🔒 잠금에 의존하지 않습니다. 대신 읽기와 쓰기 사이에 레코드가 변경되지 않을 것이라고 **낙관적으로** 가정하고, 동시성 토큰(타임스탬프 또는 버전 필드)을 사용해 레코드 변경을 감지합니다.

❌ 충돌이 발생하면(내가 읽은 뒤 다른 누군가가 레코드를 변경한 경우) 트랜잭션을 취소합니다. 시나리오에 따라 이후 다음을 수행할 수 있습니다:

- 트랜잭션 재시도(다른 영화 좌석 예약)
- 오류 발생(다른 사람이 만든 변경을 덮어쓰려 한다고 사용자에게 알림)

이 섹션에서는 직접 낙관적 동시성 제어를 구현하는 방법을 설명합니다. 참고: GitHub의 [애플리케이션 수준 낙관적 동시성 제어 계획](https://github.com/prisma/prisma/issues/4988)

#

- 낙관적 동시성 제어를 사용할 때
  - ✔ 동시 요청이 많을 것으로 예상될 때(여러 사람이 영화 좌석 예약)
  - ✔ 동시 요청 간 충돌은 드물 것으로 예상될 때

동시 요청이 많은 애플리케이션에서 잠금을 피하면 부하에 대한 복원력이 높아지고 전체 확장성도 향상됩니다. 잠금 자체가 본질적으로 나쁜 것은 아니지만, 고동시성 환경에서의 잠금은 의도치 않은 결과를 초래할 수 있습니다. 개별 행만 짧게 잠근다고 해도 마찬가지입니다. 자세한 내용은 다음을 참고하세요:

- Why ROWLOCK Hints Can Make Queries Slower and Blocking Worse in SQL Server

#

- 시나리오: 영화관 좌석 예약

영화관 예매 시스템을 만들고 있다고 가정해 보겠습니다. 각 영화에는 정해진 좌석 수가 있습니다. 다음 스키마는 영화와 좌석을 모델링합니다:

```
    model Seat {
      id        Int   @id @default(autoincrement())
      userId    Int?
      claimedBy User? @relation(fields: [userId], references: [id])
      movieId   Int
      movie     Movie @relation(fields: [movieId], references: [id])
    }

    model Movie {
      id    Int    @id     @default(autoincrement())
      name  String @unique
      seats Seat[]
    }
```

다음 샘플 코드는 첫 번째 빈 좌석을 찾아 해당 좌석을 사용자에게 할당합니다:

```
    const movieName = "Hidden Figures";

    // Find first available seat
    const availableSeat = await prisma.seat.findFirst({
      where: {
        movie: {
          name: movieName,
        },
        claimedBy: null,
      },
    });

    // Throw an error if no seats are available
    if (!availableSeat) {
      throw new Error(`Oh no! ${movieName} is all booked.`);
    }

    // Claim the seat
    await prisma.seat.update({
      data: {
        claimedBy: userId,
      },
      where: {
        id: availableSeat.id,
      },
    });
```

하지만 이 코드는 "중복 예약 문제(double-booking problem)"를 겪습니다. 두 사람이 같은 좌석을 예약할 수 있습니다:

1. Sorcha에게 좌석 3A 반환(`findFirst`)
2. Ellen에게 좌석 3A 반환(`findFirst`)
3. Sorcha가 좌석 3A 선점(`update`)
4. Ellen이 좌석 3A 선점(`update` \- Sorcha의 선점을 덮어씀)

Sorcha가 좌석 예약에 성공했더라도, 시스템에는 결국 Ellen의 선점이 저장됩니다. 이 문제를 낙관적 동시성 제어로 해결하려면 좌석에 `version` 필드를 추가합니다:

```
    model Seat {
      id        Int   @id @default(autoincrement())
      userId    Int?
      claimedBy User? @relation(fields: [userId], references: [id])
      movieId   Int
      movie     Movie @relation(fields: [movieId], references: [id])
      version   Int
    }
```

다음으로 업데이트 전에 `version` 필드를 확인하도록 코드를 조정합니다:

```
    const userEmail = "alice@prisma.io";
    const movieName = "Hidden Figures";

    // Find the first available seat
    // availableSeat.version might be 0
    const availableSeat = await client.seat.findFirst({
      where: {
        Movie: {
          name: movieName,
        },
        claimedBy: null,
      },
    });

    if (!availableSeat) {
      throw new Error(`Oh no! ${movieName} is all booked.`);
    }

    // Only mark the seat as claimed if the availableSeat.version
    // matches the version we're updating. Additionally, increment the
    // version when we perform this update so all other clients trying
    // to book this same seat will have an outdated version.
    const seats = await client.seat.updateMany({
      data: {
        claimedBy: userEmail,
        version: {
          increment: 1,
        },
      },
      where: {
        id: availableSeat.id,
        version: availableSeat.version, // This version field is the key; only claim seat if in-memory version matches database version, indicating that the field has not been updated
      },
    });

    if (seats.count === 0) {
      throw new Error(`That seat is already booked! Please try again.`);
    }
```

이제 두 사람이 같은 좌석을 예약하는 것은 불가능합니다:

1. Sorcha에게 좌석 3A 반환(`version`은 0)
2. Ellen에게 좌석 3A 반환(`version`은 0)
3. Sorcha가 좌석 3A 선점(`version`이 1로 증가, 예약 성공)
4. Ellen이 좌석 3A 선점 시도(메모리상의 `version`(0)이 데이터베이스 `version`(1)과 일치하지 않아 예약 실패)

- 대화형 트랜잭션

기존 애플리케이션이 있다면 낙관적 동시성 제어를 사용하도록 리팩터링하는 일은 상당히 큰 작업일 수 있습니다. 이런 경우 대화형 트랜잭션(Interactive Transactions)은 유용한 우회 수단이 됩니다.

대화형 트랜잭션을 만들려면 async 함수를 [$transaction](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#transaction-api)에 전달하세요.

이 async 함수에 전달되는 첫 번째 인자는 Prisma Client 인스턴스입니다. 아래에서는 이 인스턴스를 `tx`라고 부르겠습니다. 이 `tx` 인스턴스에서 호출되는 모든 Prisma Client 호출은 트랜잭션에 캡슐화됩니다.

아래 예제에서 Alice와 Bob은 각자 계좌에 $100이 있습니다. 보유 금액보다 더 많은 돈을 보내려고 하면 이체가 거절됩니다.

기대되는 결과는 Alice가 $100 이체를 1회 수행하고, 다른 이체는 거절되는 것입니다. 그 결과 Alice는 $0, Bob은 $200이 됩니다.

```
    import { PrismaClient } from "../prisma/generated/client";
    const prisma = new PrismaClient();

    async function transfer(from: string, to: string, amount: number) {
      return await prisma.$transaction(async (tx) => {
        // 1. Decrement amount from the sender.
        const sender = await tx.account.update({
          data: {
            balance: {
              decrement: amount,
            },
          },
          where: {
            email: from,
          },
        });

        // 2. Verify that the sender's balance didn't go below zero.
        if (sender.balance < 0) {
          throw new Error(`${from} doesn't have enough to send ${amount}`);
        }

        // 3. Increment the recipient's balance by amount
        const recipient = tx.account.update({
          data: {
            balance: {
              increment: amount,
            },
          },
          where: {
            email: to,
          },
        });

        return recipient;
      });
    }

    async function main() {
      // This transfer is successful
      await transfer("alice@prisma.io", "bob@prisma.io", 100);
      // This transfer fails because Alice doesn't have enough funds in her account
      await transfer("alice@prisma.io", "bob@prisma.io", 100);
    }

    main();
```

위 예제에서는 두 `update` 쿼리가 모두 데이터베이스 트랜잭션 안에서 실행됩니다. 애플리케이션이 함수 끝에 도달하면 트랜잭션은 데이터베이스에 **커밋**됩니다.

진행 중에 오류가 발생하면 async 함수가 예외를 던지고 트랜잭션은 자동으로 **롤백**됩니다.

대화형 트랜잭션에 대한 자세한 내용은 이 [섹션](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#interactive-transactions)에서 확인할 수 있습니다.

**대화형 트랜잭션은 주의해서 사용하세요**. 트랜잭션을 오래 열어 두면 데이터베이스 성능이 저하되고 데드락까지 유발할 수 있습니다. 트랜잭션 함수 내부에서 네트워크 요청 수행이나 느린 쿼리 실행은 피하세요. 가능한 한 빠르게 들어가서 빠르게 나오기를 권장합니다.

## 결론

Prisma Client는 API를 직접 사용하거나, 애플리케이션에 낙관적 동시성 제어와 멱등성을 도입할 수 있도록 지원함으로써 트랜잭션을 처리하는 여러 방법을 제공합니다. 제안된 어떤 옵션으로도 다루기 어려운 사용 사례가 애플리케이션에 있다면, 논의를 시작할 수 있도록 [GitHub issue](https://github.com/prisma/prisma/issues/new/choose)를 열어 주세요.
