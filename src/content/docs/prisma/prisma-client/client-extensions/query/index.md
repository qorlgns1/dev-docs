---
title: "사용자 정의 Prisma Client 쿼리 만들기"
description: "Prisma Client의 기능 확장, query 컴포넌트"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query

# 사용자 정의 Prisma Client 쿼리 만들기

Prisma Client의 기능 확장, query 컴포넌트

`query` [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) 컴포넌트 타입을 사용해 쿼리 라이프사이클에 훅을 걸고, 들어오는 쿼리 또는 그 결과를 수정할 수 있습니다.

Prisma Client extensions의 `query` 컴포넌트를 사용하면 동작이 커스터마이즈된 독립적인 클라이언트를 만들 수 있습니다. 한 클라이언트는 특정 필터나 사용자에 바인딩하고, 다른 클라이언트는 다른 필터나 사용자에 바인딩할 수 있습니다. 예를 들어 행 수준 보안(RLS) 확장에서 [사용자 격리](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#extended-clients)를 구현할 때 이렇게 할 수 있습니다. `query` 확장 컴포넌트는 모든 사용자 정의 쿼리에 대해 엔드 투 엔드 타입 안전성을 제공합니다.

## Prisma Client 쿼리 작업 확장

`$extends` [client-level method](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)를 사용해 [extended client](https://docs.prisma.io/docs/orm/prisma-client/client-extensions#about-prisma-client-extensions)를 생성합니다. extended client는 하나 이상의 확장으로 래핑된 표준 Prisma Client의 변형입니다.

`query` 확장 컴포넌트를 사용해 쿼리를 수정합니다. 사용자 정의 쿼리는 다음 범위에서 수정할 수 있습니다:

- 특정 모델의 특정 작업
- 스키마의 모든 모델에서 특정 작업
- 모든 Prisma Client 작업
- 특정 모델의 모든 작업
- 스키마의 모든 모델에서 모든 작업
- 특정 최상위 raw 쿼리 작업

사용자 정의 쿼리를 만들려면 다음 구조를 사용하세요:

```
    const prisma = new PrismaClient().$extends({
      name?: 'name',
      query?: {
        user: { ... } // in this case, we add a query to the `user` model
      },
    });
```

속성은 다음과 같습니다:

- `name`: (선택 사항) 오류 로그에 표시될 확장 이름을 지정합니다.
- `query`: 사용자 정의 쿼리를 정의합니다.

* 특정 모델의 특정 작업 수정

`query` 객체에는 `findUnique()`, `findFirst`, `findMany`, `count`, `create` 같은 [Prisma Client operations](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#model-queries) 이름에 매핑되는 함수를 포함할 수 있습니다. 다음 예시는 `user.findMany`를 수정해 18세 초과 사용자만 찾는 사용자 정의 쿼리를 사용합니다:

```
    const prisma = new PrismaClient().$extends({
      query: {
        user: {
          async findMany({ model, operation, args, query }) {
            // take incoming `where` and set `age`
            args.where = { ...args.where, age: { gt: 18 } };

            return query(args);
          },
        },
      },
    });

    await prisma.user.findMany(); // returns users whose age is greater than 18
```

위 예시에서 `prisma.user.findMany` 호출은 `query.user.findMany`를 트리거합니다. 각 콜백은 쿼리를 설명하는 타입 안전한 `{ model, operation, args, query }` 객체를 받습니다. 이 객체에는 다음 속성이 있습니다:

- `model`: 확장하려는 쿼리를 포함하는 모델의 이름입니다.

위 예시에서 `model`은 `"User"` 타입의 문자열입니다.

- `operation`: 확장 및 실행되는 작업의 이름입니다.

위 예시에서 `operation`은 `"findMany"` 타입의 문자열입니다.

- `args`: 확장할 특정 쿼리 입력 정보입니다.

이 객체는 타입 안전하며, 쿼리 실행 전에 변경할 수 있습니다. `args`의 어떤 속성이든 변경할 수 있습니다. 예외: `include` 또는 `select`는 변경할 수 없습니다. 예상 출력 타입이 바뀌어 타입 안전성이 깨지기 때문입니다.

- `query`: 쿼리 결과에 대한 promise입니다.
  - `await`를 사용한 뒤 이 promise의 결과를 변경할 수 있습니다. 값이 타입 안전하기 때문입니다. TypeScript는 객체에 대한 안전하지 않은 변경을 감지합니다.

* 스키마의 모든 모델에서 특정 작업 수정

스키마의 모든 모델 쿼리를 확장하려면 특정 모델 이름 대신 `$allModels`를 사용하세요. 예:

```
    const prisma = new PrismaClient().$extends({
      query: {
        $allModels: {
          async findMany({ model, operation, args, query }) {
            // set `take` and fill with the rest of `args`
            args = { ...args, take: 100 };

            return query(args);
          },
        },
      },
    });
```

- 특정 모델의 모든 작업 수정

특정 모델의 모든 작업을 확장하려면 `$allOperations`를 사용하세요.

예를 들어, 다음 코드는 `user` 모델의 모든 작업에 사용자 정의 쿼리를 적용합니다:

```
    const prisma = new PrismaClient().$extends({
      query: {
        user: {
          $allOperations({ model, operation, args, query }) {
            /* your custom logic here */
            return query(args);
          },
        },
      },
    });
```

- 모든 Prisma Client 작업 수정

Prisma Client에 있는 모든 쿼리 메서드를 수정하려면 `$allOperations` 메서드를 사용하세요. `$allOperations`는 모델 작업과 raw 쿼리 모두에 사용할 수 있습니다.

다음과 같이 모든 메서드를 수정할 수 있습니다:

```
    const prisma = new PrismaClient().$extends({
      query: {
        $allOperations({ model, operation, args, query }) {
          /* your custom logic for modifying all Prisma Client operations here */
          return query(args);
        },
      },
    });
```

[raw query](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries)가 호출되면, 콜백에 전달되는 `model` 인수는 `undefined`입니다.

예를 들어, `$allOperations` 메서드를 사용해 다음과 같이 쿼리를 로깅할 수 있습니다:

```
    const prisma = new PrismaClient().$extends({
      query: {
        async $allOperations({ operation, model, args, query }) {
          const start = performance.now();
          const result = await query(args);
          const end = performance.now();
          const time = end - start;
          console.log(
            util.inspect(
              { model, operation, args, time },
              { showHidden: false, depth: null, colors: true },
            ),
          );
          return result;
        },
      },
    });
```

- 스키마의 모든 모델에서 모든 작업 수정

스키마의 모든 모델의 모든 작업을 확장하려면 `$allModels`와 `$allOperations`를 사용하세요.

스키마의 모든 모델의 모든 작업에 사용자 정의 쿼리를 적용하려면:

```
    const prisma = new PrismaClient().$extends({
      query: {
        $allModels: {
          $allOperations({ model, operation, args, query }) {
            /* your custom logic for modifying all operations on all models here */
            return query(args);
          },
        },
      },
    });
```

- 최상위 raw 쿼리 작업 수정

특정 최상위 raw 쿼리 작업에 사용자 정의 동작을 적용하려면 모델 이름 대신 최상위 raw 쿼리 함수 이름을 사용하세요:

관계형 데이터베이스

MongoDB

```
    const prisma = new PrismaClient().$extends({
      query: {
        $queryRaw({ args, query, operation }) {
          // handle $queryRaw operation
          return query(args);
        },
        $executeRaw({ args, query, operation }) {
          // handle $executeRaw operation
          return query(args);
        },
        $queryRawUnsafe({ args, query, operation }) {
          // handle $queryRawUnsafe operation
          return query(args);
        },
        $executeRawUnsafe({ args, query, operation }) {
          // handle $executeRawUnsafe operation
          return query(args);
        },
      },
    });
```

- 쿼리 결과 변경

`await`를 사용한 뒤 `query` promise의 결과를 변경할 수 있습니다.

```
    const prisma = new PrismaClient().$extends({
      query: {
        user: {
          async findFirst({ model, operation, args, query }) {
            const user = await query(args);

            if (user.password !== undefined) {
              user.password = "******";
            }

            return user;
          },
        },
      },
    });
```

위 예시는 이것이 가능함을 보여주기 위해 포함했습니다. 하지만 성능상의 이유로, 기존 필드를 재정의할 때는 [`result` component type](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result)을 사용할 것을 권장합니다. 이 상황에서는 보통 `result` component type이 더 나은 성능을 제공합니다. 접근 시점에만 계산하기 때문입니다. `query` component type은 쿼리 실행 후에 계산합니다.

## 쿼리를 배치 트랜잭션으로 래핑

확장된 쿼리를 [batch transaction](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions)으로 래핑할 수 있습니다. 예를 들어 행 수준 보안(RLS)을 적용할 때 사용할 수 있습니다.

다음 예시는 `findFirst`를 확장해 배치 트랜잭션에서 실행되도록 합니다.

```
    const transactionExtension = Prisma.defineExtension((prisma) =>
      prisma.$extends({
        query: {
          user: {
            // Get the input `args` and a callback to `query`
            async findFirst({ args, query, operation }) {
              const [result] = await prisma.$transaction([query(args)]); // wrap the query in a batch transaction, and destructure the result to return an array
              return result; // return the first result found in the array
            },
          },
        },
      }),
    );
    const prisma = new PrismaClient().$extends(transactionExtension);
```
