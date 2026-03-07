---
title: "모델에 커스텀 메서드 추가하기"
description: "Prisma Client의 기능 확장, model 컴포넌트"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model

# 모델에 커스텀 메서드 추가하기

Prisma Client의 기능 확장, model 컴포넌트

`model` [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) 컴포넌트 타입을 사용해 모델에 커스텀 메서드를 추가할 수 있습니다.

`model` 컴포넌트의 가능한 활용 사례는 다음과 같습니다:

- `findMany` 같은 기존 Prisma Client 작업과 함께 동작하는 새 작업
- 캡슐화된 비즈니스 로직
- 반복적인 작업
- 모델별 유틸리티

## 커스텀 메서드 추가하기

`$extends` [client-level method](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)를 사용해 _확장된 클라이언트_ 를 생성합니다. 확장된 클라이언트는 하나 이상의 확장으로 감싼 표준 Prisma Client의 변형입니다. `model` 확장 컴포넌트를 사용해 스키마의 모델에 메서드를 추가할 수 있습니다.

- 특정 모델에 커스텀 메서드 추가하기

스키마의 특정 모델을 확장하려면 다음 구조를 사용하세요. 이 예시는 `user` 모델에 메서드를 추가합니다.

```
    const prisma = new PrismaClient().$extends({
      name?: '<name>',  // (optional) names the extension for error logs
      model?: {
        user: { ... }   // in this case, we extend the `user` model
      },
    });
```

#

- 예시

다음 예시는 `user` 모델에 `signUp`이라는 메서드를 추가합니다. 이 메서드는 지정된 이메일 주소로 새 사용자를 생성합니다:

```
    const prisma = new PrismaClient().$extends({
      model: {
        user: {
          async signUp(email: string) {
            await prisma.user.create({ data: { email } });
          },
        },
      },
    });
```

애플리케이션에서는 다음과 같이 `signUp`을 호출합니다:

```
    const user = await prisma.user.signUp("john@prisma.io");
```

- 스키마의 모든 모델에 커스텀 메서드 추가하기

스키마의 _모든_ 모델을 확장하려면 다음 구조를 사용하세요:

```
    const prisma = new PrismaClient().$extends({
      name?: '<name>', // `name` is an optional field that you can use to name the extension for error logs
      model?: {
        $allModels: { ... }
      },
    })
```

#

- 예시

다음 예시는 모든 모델에 `exists` 메서드를 추가합니다.

```
    const prisma = new PrismaClient().$extends({
      model: {
        $allModels: {
          async exists<T>(this: T, where: Prisma.Args<T, "findFirst">["where"]): Promise<boolean> {
            // Get the current model at runtime
            const context = Prisma.getExtensionContext(this);

            const result = await (context as any).findFirst({ where });
            return result !== null;
          },
        },
      },
    });
```

애플리케이션에서는 다음과 같이 `exists`를 호출합니다:

```
    // `exists` method available on all models
    await prisma.user.exists({ name: "Alice" });
    await prisma.post.exists({
      OR: [{ title: { contains: "Prisma" } }, { content: { contains: "Prisma" } }],
    });
```

## 다른 커스텀 메서드에서 커스텀 메서드 호출하기

두 메서드가 같은 모델에 선언되어 있다면, 한 커스텀 메서드에서 다른 커스텀 메서드를 호출할 수 있습니다. 예를 들어 `user` 모델의 한 커스텀 메서드에서 같은 `user` 모델의 다른 커스텀 메서드를 호출할 수 있습니다. 두 메서드가 같은 확장에 선언되었는지, 서로 다른 확장에 선언되었는지는 중요하지 않습니다.

이렇게 하려면 `Prisma.getExtensionContext(this).methodName`을 사용하세요. `prisma.user.methodName`은 사용할 수 없습니다. `prisma`는 아직 확장되지 않았기 때문에 새 메서드를 포함하고 있지 않기 때문입니다.

예시:

```
    const prisma = new PrismaClient().$extends({
      model: {
        user: {
          firstMethod() {
            ...
          },
          secondMethod() {
              Prisma.getExtensionContext(this).firstMethod()
          }
        }
      }
    })
```

## 런타임에 현재 모델 이름 가져오기

`Prisma.getExtensionContext(this).$name`으로 런타임에 현재 모델의 이름을 가져올 수 있습니다. 이를 사용해 모델 이름을 로그에 기록하거나, 다른 서비스로 이름을 전송하거나, 모델에 따라 코드를 분기할 수 있습니다.

예시:

```
    // `context` refers to the current model
    const context = Prisma.getExtensionContext(this);

    // `context.$name` returns the name of the current model
    console.log(context.$name);

    // Usage
    await (context as any).findFirst({ args });
```

런타임에 현재 모델 이름을 가져오는 구체적인 예시는 [스키마의 모든 모델에 커스텀 메서드 추가하기](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model#example-1)를 참고하세요.

## 고급 타입 안정성: 제네릭 확장 정의를 위한 타입 유틸리티

공유 확장의 `model` 컴포넌트에서 [type utilities](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/type-utilities)를 사용해 타입 안정성을 높일 수 있습니다.
