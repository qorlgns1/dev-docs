---
title: "쿼리 결과에 커스텀 필드와 메서드 추가하기"
description: "Prisma Client의 기능 확장, result 컴포넌트"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result

# 쿼리 결과에 커스텀 필드와 메서드 추가하기

Prisma Client의 기능 확장, result 컴포넌트

`result` [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) 컴포넌트 타입을 사용해 쿼리 결과에 커스텀 필드와 메서드를 추가할 수 있습니다.

`$extends` [client-level method](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)를 사용해 _확장 클라이언트(extended client)_ 를 생성합니다. 확장 클라이언트는 하나 이상의 확장으로 래핑된 표준 Prisma Client의 변형입니다.

쿼리 결과에 커스텀 [field](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result#add-a-custom-field-to-query-results) 또는 [method](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result#add-a-custom-method-to-the-result-object)를 추가하려면 다음 구조를 사용하세요. 이 예시에서는 `user` 모델 쿼리 결과에 커스텀 필드 `myComputedField`를 추가합니다.

```
    const prisma = new PrismaClient().$extends({
      name?: 'name',
      result?: {
        user: {                   // in this case, we extend the `user` model
          myComputedField: {      // the name of the new computed field
            needs: { ... },
            compute() { ... }
          },
        },
      },
    });
```

매개변수는 다음과 같습니다:

- `name`: (선택 사항) 오류 로그에 표시될 확장 이름을 지정합니다.
- `result`: 쿼리 결과에 새로운 필드와 메서드를 정의합니다.
- `needs`: 결과 필드의 의존성을 설명하는 객체입니다.
- `compute`: 가상 필드에 접근할 때 해당 필드가 어떻게 계산되는지 정의하는 메서드입니다.

## 쿼리 결과에 커스텀 필드 추가하기

`result` 확장 컴포넌트를 사용해 쿼리 결과에 필드를 추가할 수 있습니다. 이 필드들은 런타임에 계산되며 타입 안전성을 보장합니다.

다음 예시에서는 `user` 모델에 `fullName`이라는 새로운 가상 필드를 추가합니다.

```
    const prisma = new PrismaClient().$extends({
      result: {
        user: {
          fullName: {
            // the dependencies
            needs: { firstName: true, lastName: true },
            compute(user) {
              // the computation logic
              return `${user.firstName} ${user.lastName}`;
            },
          },
        },
      },
    });

    const user = await prisma.user.findFirst();

    // return the user's full name, such as "John Doe"
    console.log(user.fullName);
```

위 예시에서 `compute`의 입력인 `user`는 `needs`에 정의된 객체에 따라 자동으로 타입이 지정됩니다. `firstName`과 `lastName`은 `needs`에 지정되어 있으므로 `string` 타입입니다. `needs`에 지정되지 않으면 접근할 수 없습니다.

## 다른 계산 필드에서 계산 필드 재사용하기

다음 예시는 사용자의 호칭과 전체 이름을 타입 안전하게 계산합니다. `titleFullName`은 `fullName` 계산 필드를 재사용하는 계산 필드입니다.

```
    const prisma = new PrismaClient()
      .$extends({
        result: {
          user: {
            fullName: {
              needs: { firstName: true, lastName: true },
              compute(user) {
                return `${user.firstName} ${user.lastName}`;
              },
            },
          },
        },
      })
      .$extends({
        result: {
          user: {
            titleFullName: {
              needs: { title: true, fullName: true },
              compute(user) {
                return `${user.title} (${user.fullName})`;
              },
            },
          },
        },
      });
```

- 필드 관련 고려사항
  - 성능상의 이유로, Prisma Client는 조회 시점이 아니라 접근 시점에 결과를 계산합니다.

  - 스칼라 필드를 기반으로 한 계산 필드만 생성할 수 있습니다.

  - 계산 필드는 `select`와만 함께 사용할 수 있으며 집계할 수 없습니다. 예:

```
const user = await prisma.user.findFirst({
          select: { email: true },
        });
        console.log(user.fullName); // undefined
```

## 결과 객체에 커스텀 메서드 추가하기

`result` 컴포넌트를 사용해 쿼리 결과에 메서드를 추가할 수 있습니다. 다음 예시는 결과 객체에 새 메서드 `save`를 추가합니다.

```
    const prisma = new PrismaClient().$extends({
      result: {
        user: {
          save: {
            needs: { id: true },
            compute(user) {
              return () => prisma.user.update({ where: { id: user.id }, data: user });
            },
          },
        },
      },
    });

    const user = await prisma.user.findUniqueOrThrow({ where: { id: someId } });
    user.email = "mynewmail@mailservice.com";
    await user.save();
```

## `result` 확장 컴포넌트와 함께 `omit` 쿼리 옵션 사용하기

[`omit` (Preview) 옵션](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#omit)을 [커스텀 필드](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/result#add-a-custom-field-to-query-results) 및 커스텀 필드에 필요한 필드와 함께 사용할 수 있습니다.

- 쿼리 결과에서 커스텀 필드에 필요한 `omit` 필드

커스텀 필드의 의존성인 필드를 `omit`하면, 쿼리 결과에는 포함되지 않더라도 해당 필드는 여전히 데이터베이스에서 읽어옵니다.

다음 예시는 커스텀 필드 `sanitizedPassword`의 의존성인 `password` 필드를 `omit`합니다:

```
    const xprisma = prisma.$extends({
      result: {
        user: {
          sanitizedPassword: {
            needs: { password: true },
            compute(user) {
              return sanitize(user.password);
            },
          },
        },
      },
    });

    const user = await xprisma.user.findFirstOrThrow({
      omit: {
        password: true,
      },
    });
```

이 경우 `password`가 결과에서 제외되더라도, `sanitizedPassword` 커스텀 필드의 의존성이므로 데이터베이스에서는 여전히 조회됩니다.

- 쿼리 결과에서 `omit` 커스텀 필드 및 의존성

제외된 필드가 데이터베이스에서 전혀 조회되지 않도록 하려면 커스텀 필드와 해당 의존성을 모두 `omit`해야 합니다.

다음 예시는 커스텀 필드 `sanitizedPassword`와 의존 필드 `password`를 모두 `omit`합니다:

```
    const xprisma = prisma.$extends({
      result: {
        user: {
          sanitizedPassword: {
            needs: { password: true },
            compute(user) {
              return sanitize(user.password);
            },
          },
        },
      },
    });

    const user = await xprisma.user.findFirstOrThrow({
      omit: {
        sanitizedPassword: true,
        password: true,
      },
    });
```

이 경우 `password`와 `sanitizedPassword`를 모두 `omit`하면, 결과에서 둘 다 제외될 뿐 아니라 `password` 필드가 데이터베이스에서 읽히는 것도 방지됩니다.

## 제한사항

현재 Prisma Client의 result 확장 컴포넌트는 relation 필드를 지원하지 않습니다. 즉, 관계형 연관(relational relationship)에 있는 관련 모델 또는 필드(예: user.posts, post.author)를 기반으로 커스텀 필드나 메서드를 만들 수 없습니다. needs 매개변수는 동일한 모델 내의 스칼라 필드만 참조할 수 있습니다. [GitHub의 issue #20091](https://github.com/prisma/prisma/issues/20091)을 확인하세요.

```
    const prisma = new PrismaClient().$extends({
      result: {
        user: {
          postsCount: {
            needs: { posts: true }, // This will not work because posts is a relation field
            compute(user) {
              return user.posts.length; // Accessing a relation is not allowed
            },
          },
        },
      },
    });
```
