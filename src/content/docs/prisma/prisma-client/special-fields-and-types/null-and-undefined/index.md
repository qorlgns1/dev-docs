---
title: "Null 및 undefined"
description: "Prisma Client가 null과 undefined를 처리하는 방식"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/null-and-undefined

# Null 및 undefined

Prisma Client가 null과 undefined를 처리하는 방식

Prisma ORM에서 `undefined`가 값으로 전달되면 생성된 쿼리에 포함되지 않습니다. 이 동작은 예상치 못한 결과와 데이터 손실로 이어질 수 있습니다. 아래에 설명된 `strictUndefinedChecks` 프리뷰 기능을 활성화할 것을 강력히 권장합니다.

현재 동작(`strictUndefinedChecks` 프리뷰 기능 없음)에 대한 문서는 [current behavior](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/null-and-undefined#current-behavior)를 참고하세요.

## 엄격한 undefined 검사 (프리뷰 기능)

`strictUndefinedChecks` 프리뷰 기능은 Prisma Client가 `undefined` 값을 처리하는 방식을 변경하여, 우발적인 데이터 손실이나 의도하지 않은 쿼리 동작으로부터 더 나은 보호를 제공합니다.

- 엄격한 undefined 검사 활성화

이 기능을 활성화하려면 Prisma 스키마에 다음을 추가하세요:

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["strictUndefinedChecks"]
    }
```

- 엄격한 undefined 검사 사용

이 기능이 활성화되면:

1. 쿼리에서 필드를 `undefined`로 명시적으로 설정하면 런타임 오류가 발생합니다.
2. 쿼리에서 필드를 건너뛰려면 `undefined` 대신 새로운 `Prisma.skip` 심볼을 사용하세요.

사용 예시:

```
    // This will throw an error
    prisma.user.create({
      data: {
        name: "Alice",
        email: undefined, // Error: Cannot explicitly use undefined here
      },
    });

    // Use `Prisma.skip` (a symbol provided by Prisma) to omit a field
    prisma.user.create({
      data: {
        name: "Alice",
        email: Prisma.skip, // This field will be omitted from the query
      },
    });
```

이 변경은 다음과 같은 우발적인 삭제 또는 업데이트를 방지하는 데 도움이 됩니다:

```
    // Before: This would delete all users
    prisma.user.deleteMany({
      where: {
        id: undefined
      }
    })

    // After: This will throw an error
    Invalid \`prisma.user.deleteMany()\` invocation in
    /client/tests/functional/strictUndefinedChecks/test.ts:0:0
      XX })
      XX
      XX test('throws on undefined input field', async () => {
    → XX   const result = prisma.user.deleteMany({
             where: {
               id: undefined
                   ~~~~~~~~~
             }
           })
    Invalid value for argument \`where\`: explicitly \`undefined\` values are not allowed."
```

- 마이그레이션 경로

기존 코드를 마이그레이션하려면:

```
    // Before
    let optionalEmail: string | undefined;

    prisma.user.create({
      data: {
        name: "Alice",
        email: optionalEmail,
      },
    });

    // After
    prisma.user.create({
      data: {
        name: "Alice",
        email: optionalEmail ?? Prisma.skip,
      },
    });
```

- `exactOptionalPropertyTypes`

`strictUndefinedChecks` 외에도 TypeScript 컴파일러 옵션 `exactOptionalPropertyTypes` 활성화를 권장합니다. 이 옵션은 선택적 속성이 정확히 일치하도록 강제하므로, 코드에서 `undefined` 값과 관련된 잠재적 문제를 포착하는 데 도움이 됩니다. `strictUndefinedChecks`가 잘못된 `undefined` 사용에 대해 런타임 오류를 발생시키는 반면, `exactOptionalPropertyTypes`는 빌드 과정에서 이러한 문제를 잡아냅니다.

`exactOptionalPropertyTypes`에 대한 자세한 내용은 [TypeScript documentation](https://www.typescriptlang.org/tsconfig/#exactOptionalPropertyTypes)을 참고하세요.

- 피드백

항상 그렇듯, 이 기능에 대한 여러분의 피드백을 환영합니다. [GitHub discussion for this Preview feature](https://github.com/prisma/prisma/discussions/25271)에 의견과 제안을 공유해 주세요.

## current behavior

Prisma Client는 `null`과 `undefined`를 구분합니다:

- `null`은 **값**입니다
- `undefined`는 **아무 것도 하지 않음**을 의미합니다

이는 특히 [`null`과 `undefined`를 상호 교환해 사용할 수 있는 **GraphQL 컨텍스트의 Prisma ORM**](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/null-and-undefined#null-and-undefined-in-a-graphql-resolver)에서 중요합니다.

아래 데이터는 `User` 테이블을 나타냅니다. 이 데이터 집합은 아래의 모든 예시에서 사용됩니다:

| id  | name        | email                                         |
| --- | ----------- | --------------------------------------------- |
| 1   | Nikolas     | [nikolas@gmail.com](mailto:nikolas@gmail.com) |
| 2   | Martin      | [martin@gmail.com](mailto:martin@gmail.com)   |
| 3   | _비어 있음_ | [sabin@gmail.com](mailto:sabin@gmail.com)     |
| 4   | Tyler       | [tyler@gmail.com](mailto:tyler@gmail.com)     |

- _여러_ 레코드에 영향을 주는 쿼리에서의 `null`과 `undefined`

이 섹션에서는 `undefined`와 `null` 값이 데이터베이스에서 여러 레코드와 상호작용하거나 생성하는 쿼리의 동작에 어떤 영향을 주는지 다룹니다.

#

- Null

제공된 `null` 값과 `name` 값이 일치하는 모든 사용자를 찾는 다음 Prisma Client 쿼리를 살펴보세요:

```
    const users = await prisma.user.findMany({
      where: {
        name: null,
      },
    });
```

```
    [
      {
        "id": 3,
        "name": null,
        "email": "sabin@gmail.com"
      }
    ]
```

`name` 컬럼의 필터로 `null`이 제공되었기 때문에, Prisma Client는 `User` 테이블에서 `name` 컬럼이 _비어 있는_ 모든 레코드를 찾는 쿼리를 생성합니다.

#

- Undefined

이제 같은 쿼리를 `name` 컬럼의 필터 값으로 `undefined`를 사용해 실행하는 시나리오를 살펴봅시다:

```
    const users = await prisma.user.findMany({
      where: {
        name: undefined,
      },
    });
```

```
    [
      {
        "id": 1,
        "name": "Nikolas",
        "email": "nikolas@gmail.com"
      },
      {
        "id": 2,
        "name": "Martin",
        "email": "martin@gmail.com"
      },
      {
        "id": 3,
        "name": null,
        "email": "sabin@gmail.com"
      },
      {
        "id": 4,
        "name": "Tyler",
        "email": "tyler@gmail.com"
      }
    ]
```

필터에서 `undefined`를 값으로 사용하면, 본질적으로 Prisma Client에 해당 컬럼에 대해 *필터를 정의하지 않기로 했다*고 전달하는 것과 같습니다.

위 쿼리를 동일하게 표현하는 방법은 다음과 같습니다:

```
    const users = await prisma.user.findMany();
```

이 쿼리는 `User` 테이블의 모든 행을 선택합니다.

Prisma Client 쿼리의 파라미터 객체에서 어떤 키의 값이 `undefined`이면 Prisma ORM은 해당 키가 전혀 제공되지 않은 것처럼 동작합니다.

이 섹션의 예시는 `findMany` 함수에 초점을 맞췄지만, 동일한 개념은 `updateMany`, `deleteMany`처럼 여러 레코드에 영향을 줄 수 있는 모든 함수에 적용됩니다.

- _하나의_ 레코드에 영향을 주는 쿼리에서의 `null`과 `undefined`

이 섹션에서는 `undefined`와 `null` 값이 데이터베이스에서 단일 레코드와 상호작용하거나 생성하는 쿼리의 동작에 어떤 영향을 주는지 다룹니다.

`findUnique()` 쿼리에서는 `null`이 유효한 필터 값이 아닙니다.

단일 레코드에 영향을 주는 쿼리의 필터 조건에서 `null`과 `undefined`를 사용할 때의 동작은 이전 섹션에서 설명한 동작과 매우 유사합니다.

#

- Null

`name` 컬럼 필터에 `null`을 사용하는 다음 쿼리를 살펴보세요:

```
    const user = await prisma.user.findFirst({
      where: {
        name: null,
      },
    });
```

```
    [
      {
        "id": 3,
        "name": null,
        "email": "sabin@gmail.com"
      }
    ]
```

`name` 컬럼 필터로 `null`이 사용되었기 때문에 Prisma Client는 `User` 테이블에서 `name` 값이 _비어 있는_ 첫 번째 레코드를 찾는 쿼리를 생성합니다.

#

- Undefined

대신 `name` 컬럼의 필터 값으로 `undefined`를 사용하면, _쿼리는 해당 컬럼에 필터 조건이 전혀 전달되지 않은 것처럼 동작합니다_.

아래 쿼리를 살펴보세요:

```
    const user = await prisma.user.findFirst({
      where: {
        name: undefined,
      },
    });
```

```
    [
      {
        "id": 1,
        "name": "Nikolas",
        "email": "nikolas@gmail.com"
      }
    ]
```

이 시나리오에서 쿼리는 데이터베이스의 가장 첫 번째 레코드를 반환합니다.

위 쿼리를 표현하는 또 다른 방법은 다음과 같습니다:

```
    const user = await prisma.user.findFirst();
```

이 섹션의 예시는 `findFirst` 함수에 초점을 맞췄지만, 동일한 개념은 단일 레코드에 영향을 주는 모든 함수에 적용됩니다.

- GraphQL resolver에서의 `null`과 `undefined`

이 예시에서는 다음 Prisma 스키마를 기반으로 한 데이터베이스를 가정합니다:

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
    }
```

사용자를 업데이트하는 다음 GraphQL mutation에서 `authorEmail`과 `name`은 모두 `null`을 허용합니다. GraphQL 관점에서 이는 필드가 **optional**이라는 의미입니다:

```
    type Mutation {
      // Update author's email or name, or both - or neither!
      updateUser(id: Int!, authorEmail: String, authorName: String): User!
    }
```

하지만 `authorEmail` 또는 `authorName`에 `null` 값을 전달해 Prisma Client로 넘기면 다음과 같은 일이 발생합니다:

- `args.authorEmail`이 `null`이면 쿼리가 **실패**합니다. `email`은 `null`을 허용하지 않습니다.
- `args.authorName`이 `null`이면 Prisma Client는 `name` 값을 `null`로 변경합니다. 이는 아마 업데이트 동작으로 의도한 바가 아닐 것입니다.

```
    updateUser: (parent, args, ctx: Context) => {
      return ctx.prisma.user.update({
        where: { id: Number(args.id) },
        data: {
          email: args.authorEmail, // email cannot be null
          name: args.authorName // name set to null - potentially unwanted behavior
        },
      })
    },
```

대신 입력값이 `null`일 때 `email`과 `name` 값을 `undefined`로 설정하세요. 이렇게 하면 해당 필드를 전혀 업데이트하지 않는 것과 같습니다:

```
    updateUser: (parent, args, ctx: Context) => {
      return ctx.prisma.user.update({
        where: { id: Number(args.id) },
        data: {
          email: args.authorEmail != null ? args.authorEmail : undefined, // If null, do nothing
          name: args.authorName != null ? args.authorName : undefined // If null, do nothing
        },
      })
    },
```

- 조건식에서 `null`과 `undefined`의 영향

조건식을 사용한 필터링에는 예상치 못한 결과를 만들 수 있는 몇 가지 주의점이 있습니다. 조건식으로 필터링할 때 Prisma Client가 nullable 값을 처리하는 방식 때문에 예상한 결과와 다른 결과를 받을 수 있습니다.

다음 표는 서로 다른 연산자가 0, 1, `n`개의 필터를 어떻게 처리하는지에 대한 상위 수준 개요를 제공합니다.

| Operator | 0 filters      | 1 filter       | n filters      |
| -------- | -------------- | -------------- | -------------- |
| `OR`     | 빈 목록 반환   | 단일 필터 검증 | 모든 필터 검증 |
| `AND`    | 모든 항목 반환 | 단일 필터 검증 | 모든 필터 검증 |
| `NOT`    | 모든 항목 반환 | 단일 필터 검증 | 모든 필터 검증 |

이 예시는 [`OR`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#or) 연산자를 사용하는 쿼리에서 `undefined` 파라미터가 반환 결과에 어떤 영향을 주는지 보여줍니다.

```
    interface FormData {
      name: string;
      email?: string;
    }

    const formData: FormData = {
      name: "Emelie",
    };

    const users = await prisma.user.findMany({
      where: {
        OR: [
          {
            email: {
              contains: formData.email,
            },
          },
        ],
      },
    });

    // returns: []
```

이 쿼리는 선택적 email 속성을 포함하는 formData 객체에서 필터를 받습니다. 이 경우 email 속성의 값은 `undefined`입니다. 이 쿼리를 실행하면 데이터가 반환되지 않습니다.

이는 [`AND`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#and) 및 [`NOT`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference) 연산자와는 대조적이며, 이 둘은 `undefined` 값을 전달하면 모두 모든 사용자를 반환합니다.

> 이는 `AND` 또는 `NOT` 연산자에 `undefined` 값을 전달하는 것이 아무 값도 전달하지 않는 것과 같기 때문이며, 즉 예시의 `findMany` 쿼리는 필터 없이 실행되어 모든 사용자를 반환합니다.

```
    interface FormData {
      name: string;
      email?: string;
    }

    const formData: FormData = {
      name: "Emelie",
    };

    const users = await prisma.user.findMany({
      where: {
        AND: [
          {
            email: {
              contains: formData.email,
            },
          },
        ],
      },
    });

    // returns: { id: 1, email: 'ems@boop.com', name: 'Emelie' }

    const users = await prisma.user.findMany({
      where: {
        NOT: [
          {
            email: {
              contains: formData.email,
            },
          },
        ],
      },
    });

    // returns: { id: 1, email: 'ems@boop.com', name: 'Emelie' }
```
