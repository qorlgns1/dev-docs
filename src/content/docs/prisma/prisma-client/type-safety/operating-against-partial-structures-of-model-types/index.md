---
title: "모델 타입의 부분 구조를 대상으로 작업하기"
description: "이 페이지에서는 Prisma 네임스페이스에서 생성된 타입을 사용하는 다양한 시나리오를 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types

# 모델 타입의 부분 구조를 대상으로 작업하기

이 페이지에서는 Prisma 네임스페이스에서 생성된 타입을 사용하는 다양한 시나리오를 설명합니다.

Prisma Client를 사용할 때, [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)의 각 모델은 전용 TypeScript 타입으로 변환됩니다. 예를 들어, 다음과 같은 `User` 및 `Post` 모델이 있다고 가정해 보겠습니다.

```
    model User {
      id    Int     @id
      email String  @unique
      name  String?
      posts Post[]
    }

    model Post {
      id        Int     @id
      author    User    @relation(fields: [userId], references: [id])
      title     String
      published Boolean @default(false)
      userId    Int
    }
```

이 스키마에서 생성된 Prisma Client 코드에는 `User` 타입이 다음과 같이 표현됩니다.

```
    export type User = {
      id: string;
      email: string;
      name: string | null;
    };
```

## 문제: 생성된 모델 타입의 변형 사용

- 설명

일부 시나리오에서는 생성된 `User` 타입의 _변형_ 이 필요할 수 있습니다. 예를 들어, `posts` 관계를 포함한 `User` 모델 인스턴스를 기대하는 함수가 있을 때입니다. 또는 애플리케이션 코드에서 `User` 모델의 `email`과 `name` 필드만 전달하기 위한 타입이 필요할 수도 있습니다.

- 해결책

해결책으로, Prisma Client의 헬퍼 타입을 사용해 생성된 모델 타입을 커스터마이징할 수 있습니다.

`User` 타입은 모델의 [스칼라](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields) 필드만 포함하며, 관계는 반영하지 않습니다. 이는 Prisma Client 쿼리에서 기본적으로 [관계가 포함되지 않기 때문](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#return-the-default-fields)입니다.

하지만 때로는 **관계를 포함하는** 타입(즉, [`include`](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#return-nested-objects-by-selecting-relation-fields)를 사용하는 API 호출에서 얻는 타입)이 있으면 유용합니다. 마찬가지로, **모델의 스칼라 필드 일부만 포함하는** 타입(즉, [`select`](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/select-fields#select-specific-fields)를 사용하는 API 호출에서 얻는 타입)이 유용한 경우도 있습니다.

이를 달성하는 한 가지 방법은 애플리케이션 코드에서 이러한 타입을 수동으로 정의하는 것입니다.

```
    // 1: Define a type that includes the relation to `Post`
    type UserWithPosts = {
      id: string;
      email: string;
      name: string | null;
      posts: Post[];
    };

    // 2: Define a type that only contains a subset of the scalar fields
    type UserPersonalData = {
      email: string;
      name: string | null;
    };
```

물론 이는 충분히 가능한 접근 방식이지만, Prisma 스키마가 변경될 때 타입도 수동으로 유지보수해야 하므로 유지보수 부담이 커집니다. 이를 더 깔끔하게 해결하는 방법은 TypeScript의 `satisfies` 연산자와 함께 Prisma Client가 `Prisma` 네임스페이스 아래에 생성해 노출하는 `UserGetPayload` 타입을 사용하는 것입니다.

다음 예제에서는 `satisfies` 연산자를 사용해 타입 안전한 객체 두 개를 만들고, 이어서 `Prisma.UserGetPayload` 유틸리티 함수를 사용해 모든 사용자와 그들의 게시글을 반환하는 데 사용할 수 있는 타입을 생성합니다.

```
    import { Prisma } from "@prisma/client";

    // 1: Define a type that includes the relation to `Post`
    const userWithPosts = { include: { posts: true } } satisfies Prisma.UserDefaultArgs;

    // 2: Define a type that only contains a subset of the scalar fields
    const userPersonalData = { select: { email: true, name: true } } satisfies Prisma.UserDefaultArgs;

    // 3: This type will include a user and all their posts
    type UserWithPosts = Prisma.UserGetPayload<typeof userWithPosts>;
```

후자의 접근 방식이 제공하는 주요 이점은 다음과 같습니다.

- Prisma Client가 생성한 타입을 활용하므로 더 깔끔한 접근 방식
- 스키마 변경 시 유지보수 부담 감소 및 타입 안전성 향상

## 문제: 함수의 반환 타입에 접근하기

- 설명

모델에 대해 [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select) 또는 [`include`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#include) 작업을 수행하고 이러한 변형을 함수에서 반환할 때, 반환 타입에 접근하기가 어려울 수 있습니다. 예:

```
    // Function definition that returns a partial structure
    async function getUsersWithPosts() {
      const users = await prisma.user.findMany({ include: { posts: true } });
      return users;
    }
```

위 코드 스니펫에서 "게시글이 포함된 사용자"를 나타내는 타입을 추출하려면 다소 고급 TypeScript 사용법이 필요합니다.

```
    // Function definition that returns a partial structure
    async function getUsersWithPosts() {
      const users = await prisma.user.findMany({ include: { posts: true } });
      return users;
    }

    // Extract `UsersWithPosts` type with
    type ThenArg<T> = T extends PromiseLike<infer U> ? U : T;
    type UsersWithPosts = ThenArg<ReturnType<typeof getUsersWithPosts>>;

    // run inside `async` function
    const usersWithPosts: UsersWithPosts = await getUsersWithPosts();
```

- 해결책

이 문제는 TypeScript의 기본 유틸리티 타입인 [`Awaited`](https://www.typescriptlang.org/docs/handbook/utility-types.html#awaitedtype)와 [`ReturnType`](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype)을 사용해 우아하게 해결할 수 있습니다.

```
    type UsersWithPosts = Awaited<ReturnType<typeof getUsersWithPosts>>;
```
