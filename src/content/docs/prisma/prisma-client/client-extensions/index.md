---
title: "Client Extensions란?"
description: "Prisma Client 확장을 사용하면 모델, 결과 객체, 쿼리에 기능을 추가하거나 클라이언트 수준 메서드를 추가할 수 있습니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions

# Client Extensions란?

Prisma Client의 기능 확장

Prisma Client 확장을 사용하면 모델, 결과 객체, 쿼리에 기능을 추가하거나 클라이언트 수준 메서드를 추가할 수 있습니다.

다음 컴포넌트 유형 중 하나 이상으로 확장을 만들 수 있습니다:

- `model`: [모델에 사용자 정의 메서드 또는 필드 추가](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model)
- `client`: [Prisma Client에 클라이언트 수준 메서드 추가](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/client)
- `query`: [사용자 정의 Prisma Client 쿼리 생성](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query)
- `result`: [쿼리 결과에 사용자 정의 필드 추가](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result)

예를 들어 `model` 및 `client` 컴포넌트 유형을 사용하는 확장을 만들 수 있습니다.

## Prisma Client 확장 소개

Prisma Client 확장을 사용하면 _확장된 클라이언트(extended client)_ 를 생성하게 됩니다. 확장된 클라이언트는 하나 이상의 확장으로 래핑된 표준 Prisma Client의 경량 변형입니다. 표준 클라이언트 자체는 변경되지 않습니다. 프로젝트에 원하는 만큼 확장된 클라이언트를 추가할 수 있습니다. [확장된 클라이언트 자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#extended-clients).

단일 확장 또는 여러 확장을 하나의 확장된 클라이언트에 연결할 수 있습니다. [여러 확장 자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#multiple-extensions).

다른 Prisma ORM 사용자와 [Prisma Client 확장을 공유](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions)할 수 있으며, 다른 사용자가 개발한 [Prisma Client 확장을 Prisma ORM 프로젝트로 가져올](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions#install-a-shared-packaged-extension) 수도 있습니다.

- 확장된 클라이언트

확장된 클라이언트는 서로 및 표준 클라이언트와 다음과 같이 상호작용합니다:

- 각 확장된 클라이언트는 격리된 인스턴스에서 독립적으로 동작합니다.
- 확장된 클라이언트끼리, 또는 표준 클라이언트와 충돌할 수 없습니다.
- 모든 확장된 클라이언트와 표준 클라이언트는 동일한 커넥션 풀을 공유합니다.

> **참고** : 확장 작성자는 확장의 일부로 임의 코드를 실행할 수 있으므로 이 동작을 수정할 수 있습니다. 예를 들어, 어떤 확장은 완전히 새로운 `PrismaClient` 인스턴스(자체 쿼리 엔진 및 커넥션 풀 포함)를 실제로 생성할 수 있습니다. 사용하는 확장의 문서를 확인하여 구현된 특정 동작이 있는지 반드시 확인하세요.

- 확장된 클라이언트의 예시 사용 사례

확장된 클라이언트는 격리된 인스턴스에서 동작하므로, 예를 들어 다음과 같은 작업에 적합합니다:

- 행 수준 보안(RLS) 구현: 각 HTTP 요청이 세션 데이터에 맞춰 커스터마이즈된 자체 RLS 확장을 가진 자체 클라이언트를 갖도록 할 수 있습니다. 이렇게 하면 각 사용자를 별도 클라이언트에서 완전히 분리할 수 있습니다.
- 현재 로그인한 사용자를 가져오기 위해 `User` 모델에 `user.current()` 메서드 추가.
- 디버그 쿠키가 설정된 경우 요청에 대해 더 상세한 로깅 활성화.
- 모든 로그에 고유한 요청 ID를 연결해 나중에 상관관계를 추적할 수 있도록 하여, 예를 들어 Prisma Client가 수행한 작업 분석에 도움을 줄 수 있습니다.
- 애플리케이션이 관리자 엔드포인트를 호출하고 사용자가 필요한 권한을 가진 경우를 제외하고 모델에서 `delete` 메서드 제거.

## Prisma Client에 확장 추가

확장은 주로 두 가지 방법으로 만들 수 있습니다:

- 클라이언트 수준 [`$extends`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods) 메서드 사용

```
const prisma = new PrismaClient().$extends({
          name: 'signUp', // Optional: name appears in error logs
          model: {        // This is a `model` component
            user: { ... } // The extension logic for the `user` model goes inside the curly braces
          },
        })
```

- `Prisma.defineExtension` 메서드로 확장을 정의해 변수에 할당한 뒤, 해당 확장을 클라이언트 수준 `$extends` 메서드에 전달

```
import { Prisma } from '@prisma/client'

        // Define the extension
        const myExtension = Prisma.defineExtension({
          name: 'signUp', // Optional: name appears in error logs
          model: {        // This is a `model` component
            user: { ... } // The extension logic for the `user` model goes inside the curly braces
          },
        })

        // Pass the extension to a Prisma Client instance
        const prisma = new PrismaClient().$extends(myExtension)
```

이 패턴은 프로젝트 내 여러 파일 또는 디렉터리로 확장을 분리하고 싶을 때 유용합니다.

위 예시는 [`model` 확장 컴포넌트](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model)를 사용해 `User` 모델을 확장합니다.

`$extends` 메서드에서는 적절한 확장 컴포넌트([`model`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model), [`client`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/client), [`result`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result), [`query`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query))를 사용하세요.

## 에러 로그용 확장 이름 지정

에러 로그에서 확장을 식별하기 쉽도록 확장에 이름을 지정할 수 있습니다. 이를 위해 선택 필드 `name`을 사용합니다. 예:

```
    const prisma = new PrismaClient().$extends({
      name: `signUp`,  // (Optional) Extension name
      model: {
        user: { ... }
     },
    })
```

## 여러 확장

다음 두 가지 방법 중 하나로 확장을 [확장된 클라이언트](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#about-prisma-client-extensions)에 연결할 수 있습니다:

- 확장을 단독으로 확장된 클라이언트에 연결하거나,
- 해당 확장을 다른 확장들과 결합해 이 모든 확장을 하나의 확장된 클라이언트에 연결할 수 있습니다. 결합된 확장들의 기능은 동일한 확장된 클라이언트에 적용됩니다. 참고: [결합된 확장은 충돌할 수 있습니다](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#conflicts-in-combined-extensions).

위 두 접근법은 함께 사용할 수 있습니다. 예를 들어, 하나의 확장은 자체 확장된 클라이언트에 연결하고 다른 두 확장은 또 다른 확장된 클라이언트에 연결할 수 있습니다. [클라이언트 인스턴스 상호작용 자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#extended-clients).

- 확장된 클라이언트에 여러 확장 적용

다음 예시에서 `extensionA`와 `extensionB`라는 두 확장이 있다고 가정해 봅시다. 이를 결합하는 방법은 두 가지입니다.

#

- 옵션 1: 한 줄로 새 클라이언트 선언

이 옵션에서는 한 줄의 코드로 두 확장을 모두 새 클라이언트에 적용합니다.

```
    // First of all, store your original Prisma Client in a variable as usual
    const prisma = new PrismaClient();

    // Declare an extended client that has an extensionA and extensionB
    const prismaAB = prisma.$extends(extensionA).$extends(extensionB);
```

그다음 코드에서 `prismaAB`를 참조할 수 있습니다. 예: `prismaAB.myExtensionMethod()`.

#

- 옵션 2: 여러 확장된 클라이언트 선언

이 옵션의 장점은 각 확장된 클라이언트를 개별적으로 호출할 수 있다는 점입니다.

```
    // First of all, store your original Prisma Client in a variable as usual
    const prisma = new PrismaClient();

    // Declare an extended client that has extensionA applied
    const prismaA = prisma.$extends(extensionA);

    // Declare an extended client that has extensionB applied
    const prismaB = prisma.$extends(extensionB);

    // Declare an extended client that is a combination of clientA and clientB
    const prismaAB = prismaA.$extends(extensionB);
```

코드에서 이러한 클라이언트를 각각 호출할 수 있습니다. 예: `prismaA.myExtensionMethod()`, `prismaB.myExtensionMethod()`, `prismaAB.myExtensionMethod()`.

- 결합된 확장의 충돌

두 개 이상의 확장을 하나의 확장된 클라이언트로 결합하면, 충돌 시 선언한 _마지막_ 확장이 우선합니다. 위 옵션 1의 예시에서 `extensionA`에 `myExtensionMethod()` 메서드가 있고 `extensionB`에도 `myExtensionMethod()`가 있다고 가정해봅시다. `prismaAB.myExtensionMethod()`를 호출하면 Prisma Client는 `extensionB`에 정의된 `myExtensionMethod()`를 사용합니다.

- query 확장을 통한 미들웨어 체이닝

미들웨어를 조합하려면 [`query`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query) 확장을 체이닝하세요. 확장은 선언 순서대로 실행됩니다(FIFO):

```
    import { PrismaClient } from "./generated/prisma";

    const prisma = new PrismaClient()
      // Extension 1: Logging - measures query execution time
      .$extends({
        query: {
          $allModels: {
            async $allOperations({ model, operation, args, query }) {
              const start = Date.now();
              const result = await query(args);
              console.log(`[LOGGING] ${model}.${operation}: ${Date.now() - start}ms`);
              return result;
            },
          },
        },
      })
      // Extension 2: Audit - logs write operations
      .$extends({
        query: {
          $allModels: {
            async $allOperations({ model, operation, args, query }) {
              if (["create", "update", "delete"].includes(operation)) {
                console.log(`[AUDIT] ${operation} on ${model}:`, JSON.stringify(args));
              }
              return query(args);
            },
          },
        },
      });
```

## 확장된 클라이언트의 타입

[`typeof`](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html) 유틸리티를 사용하면 확장된 Prisma Client 인스턴스의 타입을 다음과 같이 추론할 수 있습니다:

```
    const extendedPrismaClient = new PrismaClient().$extends({
      /** extension */
    });

    type ExtendedPrismaClient = typeof extendedPrismaClient;
```

Prisma Client를 싱글턴으로 사용 중이라면 `typeof`와 [`ReturnType`](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype) 유틸리티를 사용해 확장된 Prisma Client 인스턴스 타입을 다음과 같이 얻을 수 있습니다:

```
    function getExtendedClient() {
      return new PrismaClient().$extends({
        /* extension */
      });
    }

    type ExtendedPrismaClient = ReturnType<typeof getExtendedClient>;
```

## `Prisma.Result`로 모델 타입 확장

`Prisma.Result` 타입 유틸리티를 사용하면 클라이언트 확장을 통해 추가된 속성을 포함하도록 모델 타입을 확장할 수 있습니다. 이를 통해 확장된 속성을 포함한 확장 모델의 타입을 추론할 수 있습니다.

- 예시

다음 예시는 `Prisma.Result`를 사용해 클라이언트 확장으로 추가된 `__typename` 속성을 포함하도록 `User` 모델 타입을 확장하는 방법을 보여줍니다.

```
    import { PrismaClient, Prisma } from "@prisma/client";

    const prisma = new PrismaClient().$extends({
      result: {
        user: {
          __typename: {
            needs: {},
            compute() {
              return "User";
            },
          },
        },
      },
    });

    type ExtendedUser = Prisma.Result<typeof prisma.user, { select: { id: true } }, "findFirstOrThrow">;

    async function main() {
      const user: ExtendedUser = await prisma.user.findFirstOrThrow({
        select: {
          id: true,
          __typename: true,
        },
      });

      console.log(user.__typename); // Output: 'User'
    }

    main();
```

`Prisma.Result` 타입 유틸리티는 클라이언트 확장으로 추가된 `__typename` 속성을 포함한 확장 `User` 모델의 타입을 추론하는 데 사용됩니다.

## 제한 사항

- 확장된 클라이언트에서 클라이언트 수준 메서드 사용

[클라이언트 수준 메서드](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)는 확장된 클라이언트에 반드시 존재하는 것은 아닙니다. 이러한 클라이언트에서는 사용 전에 먼저 존재 여부를 확인해야 합니다.

```
    const xPrisma = new PrismaClient().$extends(...);

    if (xPrisma.$connect) {
      xPrisma.$connect()
    }
```

- 중첩 연산과 함께 사용

`query` 확장 유형은 중첩된 읽기 및 쓰기 연산을 지원하지 않습니다.
