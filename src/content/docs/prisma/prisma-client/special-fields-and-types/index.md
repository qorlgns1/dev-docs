---
title: "필드 및 타입"
description: "Prisma Client에서 특수 필드와 타입을 사용하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types

# 필드 및 타입

Prisma Client에서 특수 필드와 타입을 사용하는 방법을 알아보세요.

이 섹션에서는 Prisma Client와 함께 사용할 수 있는 다양한 특수 필드와 타입을 다룹니다.

## `Decimal` 사용하기

`Decimal` 필드는 [`Decimal.js` library](https://mikemcl.github.io/decimal.js/)로 표현됩니다. 다음 예제는 `Prisma.Decimal`을 import하고 사용하는 방법을 보여줍니다:

```
    import { PrismaClient, Prisma } from "@prisma/client";

    const newTypes = await prisma.sample.create({
      data: {
        cost: new Prisma.Decimal(24.454545),
      },
    });
```

산술 연산도 수행할 수 있습니다:

```
    import { PrismaClient, Prisma } from "@prisma/client";

    const newTypes = await prisma.sample.create({
      data: {
        cost: new Prisma.Decimal(24.454545).plus(1),
      },
    });
```

`Prisma.Decimal`은 Decimal.js를 사용합니다. 자세한 내용은 [Decimal.js docs](https://mikemcl.github.io/decimal.js)를 참고하세요.

`Decimal` 필드의 사용은 [현재 MongoDB에서 지원되지 않습니다](https://github.com/prisma/prisma/issues/12637).

## `BigInt` 사용하기

- 개요

`BigInt` 필드는 [`BigInt` type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)으로 표현됩니다(`Node.js 10.4.0+` 필요). 다음 예제는 `BigInt` type 사용 방법을 보여줍니다:

```
    import { PrismaClient, Prisma } from "@prisma/client";

    const newTypes = await prisma.sample.create({
      data: {
        revenue: BigInt(534543543534),
      },
    });
```

- `BigInt` 직렬화하기

Prisma Client는 레코드를 일반 JavaScript 객체로 반환합니다. `BigInt` 필드가 포함된 객체에 `JSON.stringify`를 사용하려고 하면 다음 오류가 발생합니다:

```
    Do not know how to serialize a BigInt
```

이 문제를 우회하려면 `JSON.stringify`를 사용자 지정 구현으로 사용하세요:

```
    JSON.stringify(
      this,
      (key, value) => (typeof value === "bigint" ? value.toString() : value), // return everything else unchanged
    );
```

## `Bytes` 사용하기

`Bytes` 필드는 [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) type으로 표현됩니다. 다음 예제는 `Uint8Array` type 사용 방법을 보여줍니다:

```
    import { PrismaClient, Prisma } from "@prisma/client";

    const newTypes = await prisma.sample.create({
      data: {
        myField: new Uint8Array([1, 2, 3, 4]),
      },
    });
```

## `DateTime` 사용하기

현재 [bug](https://github.com/prisma/prisma/issues/9516)로 인해 `DateTime` 값을 문자열로 전달할 수 없으며, 그렇게 하면 런타임 오류가 발생합니다. `DateTime` 값은 [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) 객체로 전달해야 합니다(즉, `'2024-12-04'` 대신 `new Date('2024-12-04')`).

[`DateTime`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datetime) type 필드가 있는 레코드를 생성할 때, Prisma Client는 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 표준을 따르는 [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) 객체 값을 허용합니다.

다음 schema를 살펴보세요:

```
    model User {
      id        Int       @id @default(autoincrement())
      birthDate DateTime?
    }
```

다음은 새 레코드를 생성하는 몇 가지 예시입니다:

#

- 1998년 1월 1일; 00시 00분 000밀리초

```
    await prisma.user.create({
      data: {
        birthDate: new Date("1998"),
      },
    });
```

#

- 1998년 12월 1일; 00시 00분 000밀리초

```
    await prisma.user.create({
      data: {
        birthDate: new Date("1998-12"),
      },
    });
```

#

- 1998년 12월 24일; 00시 00분 000밀리초

```
    await prisma.user.create({
      data: {
        birthDate: new Date("1998-12-24"),
      },
    });
```

#

- 1998년 12월 24일; 06시 22분 33초 444밀리초

```
    await prisma.user.create({
      data: {
        birthDate: new Date("1998-12-24T06:22:33.444Z"),
      },
    });
```
