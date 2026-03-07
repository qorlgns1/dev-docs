---
title: "Prisma Client에 메서드 추가하기"
description: "Prisma Client의 기능을  컴포넌트로 확장하세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/client

# Prisma Client에 메서드 추가하기

Prisma Client의 기능을 `client` 컴포넌트로 확장하세요

`client` [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) 컴포넌트를 사용하면 Prisma Client에 최상위 메서드를 추가할 수 있습니다.

## Prisma Client 확장하기

`$extends` [client-level method](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)를 사용해 _확장된 클라이언트_ 를 생성합니다. 확장된 클라이언트는 하나 이상의 확장으로 래핑된 표준 Prisma Client의 변형입니다. `client` 확장 컴포넌트를 사용해 Prisma Client에 최상위 메서드를 추가하세요.

Prisma Client에 최상위 메서드를 추가하려면 다음 구조를 사용하세요:

```
    const prisma = new PrismaClient().$extends({
      client?: { ... }
    })
```

- 예제

다음 예제는 `client` 컴포넌트를 사용해 Prisma Client에 두 가지 메서드를 추가합니다:

- `$log`는 메시지를 출력합니다.
- `$totalQueries`는 현재 클라이언트 인스턴스가 실행한 쿼리 수를 반환합니다.

```
    let total = 0;
    const prisma = new PrismaClient().$extends({
      client: {
        $log: (s: string) => console.log(s),
        async $totalQueries() {
          return total;
        },
      },
      query: {
        $allModels: {
          async $allOperations({ query, args }) {
            total += 1;
            return query(args);
          },
        },
      },
    });

    async function main() {
      prisma.$log("Hello world");
      const totalQueries = await prisma.$totalQueries();
      console.log(totalQueries);
    }
```
