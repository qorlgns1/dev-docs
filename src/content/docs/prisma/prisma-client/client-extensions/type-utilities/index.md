---
title: "타입 유틸리티"
description: "고급 타입 안정성: 커스텀 모델 메서드의 타입 안정성을 개선합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/type-utilities

# 타입 유틸리티

고급 타입 안정성: 커스텀 모델 메서드의 타입 안정성을 개선합니다.

Prisma Client에는 고도의 타입 안정성을 갖춘 확장을 만드는 데 도움이 되는 여러 타입 유틸리티가 있습니다.

## 타입 유틸리티

[Prisma Client 타입 유틸리티](https://docs.prisma.io/docs/orm/prisma-client/type-safety)는 애플리케이션과 Prisma Client 확장 내에서 사용할 수 있는 유틸리티로, 확장을 위한 안전하고 확장 가능한 타입을 구성하는 유용한 방법을 제공합니다.

사용 가능한 타입 유틸리티는 다음과 같습니다.

- `Exact<Input, Shape>`: `Input`에 엄격한 타입 안정성을 강제합니다. `Exact`는 제네릭 타입 `Input`이 `Shape`에 지정한 타입을 엄격하게 준수하도록 보장합니다. 또한 `Input`을 가장 정밀한 타입으로 [좁혀줍니다](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).
- `Args<Type, Operation>`: 주어진 모델과 연산의 입력 인수를 가져옵니다. 이는 특히 다음을 원하는 확장 작성자에게 유용합니다.
  - 기존 타입을 재사용해 확장하거나 수정하기.
  - 기존 연산과 동일한 자동 완성 경험 활용하기.
- `Result<Type, Arguments, Operation>`: 입력 인수를 받아 주어진 모델과 연산의 결과를 제공합니다. 일반적으로 `Args`와 함께 사용합니다. `Args`와 마찬가지로 `Result`도 기존 타입을 재사용해 확장하거나 수정하는 데 도움을 줍니다.
- `Payload<Type, Operation>`: 주어진 모델과 연산에 대해 스칼라 및 관계 객체를 포함한 전체 결과 구조를 가져옵니다. 예를 들어 타입 수준에서 어떤 키가 스칼라인지, 어떤 키가 객체인지 판단하는 데 사용할 수 있습니다.

다음 예시는 `findFirst`를 기반으로 새 연산 `exists`를 생성합니다. 이 연산은 `findFirst`의 모든 인수를 가집니다.

```
    const prisma = new PrismaClient().$extends({
      model: {
        $allModels: {
          // Define a new `exists` operation on all models
          // T is a generic type that corresponds to the current model
          async exists<T>(
            // `this` refers to the current type, e.g. `prisma.user` at runtime
            this: T,

            // The `exists` function will use the `where` arguments from the current model, `T`, and the `findFirst` operation
            where: Prisma.Args<T, "findFirst">["where"],
          ): Promise<boolean> {
            // Retrieve the current model at runtime
            const context = Prisma.getExtensionContext(this);

            // Prisma Client query that retrieves data based
            const result = await (context as any).findFirst({ where });
            return result !== null;
          },
        },
      },
    });

    async function main() {
      const user = await prisma.user.exists({ name: "Alice" });
      const post = await prisma.post.exists({
        OR: [{ title: { contains: "Prisma" } }, { content: { contains: "Prisma" } }],
      });
    }
```

## 메서드에 커스텀 속성 추가하기

다음 예시는 확장 내 메서드에 커스텀 인수를 추가하는 방법을 보여줍니다.

```
    type CacheStrategy = {
      swr: number;
      ttl: number;
    };

    const prisma = new PrismaClient().$extends({
      model: {
        $allModels: {
          findMany<T, A>(
            this: T,
            args: Prisma.Exact<
              A,
              // For the `findMany` method, use the arguments from model `T` and the `findMany` method
              // and intersect it with `CacheStrategy` as part of `findMany` arguments
              Prisma.Args<T, "findMany"> & CacheStrategy
            >,
          ): Prisma.Result<T, A, "findMany"> {
            // method implementation with the cache strategy
          },
        },
      },
    });

    async function main() {
      await prisma.post.findMany({
        cacheStrategy: {
          ttl: 360,
          swr: 60,
        },
      });
    }
```

여기의 예시는 개념 설명용입니다. 실제로 캐싱이 동작하려면 로직을 직접 구현해야 합니다. 캐싱 확장/서비스에 관심이 있다면 [Prisma Accelerate](https://www.prisma.io/accelerate)를 살펴보는 것을 권장합니다.
