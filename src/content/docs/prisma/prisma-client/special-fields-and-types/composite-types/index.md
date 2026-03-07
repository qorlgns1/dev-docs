---
title: "복합 타입"
description: "MongoDB에서 복합 타입과 임베디드 문서 작업하기"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types

# 복합 타입

MongoDB에서 복합 타입과 임베디드 문서 작업하기

복합 타입은 MongoDB에서만 사용할 수 있습니다.

MongoDB에서 [embedded documents](https://www.mongodb.com/docs/manual/data-modeling/#embedded-data)로 알려진 [복합 타입](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models)을 사용하면 다른 레코드 안에 레코드를 임베드할 수 있습니다.

이 페이지에서는 다음을 설명합니다:

- `findFirst` 및 `findMany`를 사용해 복합 타입을 포함한 레코드를 [조회](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#finding-records-that-contain-composite-types-with-find-and-findmany)하는 방법
- `create` 및 `createMany`를 사용해 복합 타입이 포함된 새 레코드를 [생성](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#creating-records-with-composite-types-using-create-and-createmany)하는 방법
- `update` 및 `updateMany`를 사용해 기존 레코드 내부의 복합 타입을 [업데이트](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#changing-composite-types-within-update-and-updatemany)하는 방법
- `delete` 및 `deleteMany`를 사용해 복합 타입이 포함된 레코드를 [삭제](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#deleting-records-that-contain-composite-types-with-delete-and-deletemany)하는 방법

## 예제 스키마

아래 이어지는 예제에서는 이 스키마를 사용합니다:

schema.prisma

```
    generator client {
      provider = "prisma-client-js"
    }

    datasource db {
      provider = "mongodb"
      url      = env("DATABASE_URL")
    }

    model Product {
      id     String  @id @default(auto()) @map("_id") @db.ObjectId
      name   String  @unique
      price  Float
      colors Color[]
      sizes  Size[]
      photos Photo[]
      orders Order[]
    }

    model Order {
      id              String   @id @default(auto()) @map("_id") @db.ObjectId
      product         Product  @relation(fields: [productId], references: [id])
      color           Color
      size            Size
      shippingAddress Address
      billingAddress  Address?
      productId       String   @db.ObjectId
    }

    enum Color {
      Red
      Green
      Blue
    }

    enum Size {
      Small
      Medium
      Large
      XLarge
    }

    type Photo {
      height Int    @default(200)
      width  Int    @default(100)
      url    String
    }

    type Address {
      street String
      city   String
      zip    String
    }
```

이 스키마에서 `Product` 모델은 `Photo[]` 복합 타입을 가지며, `Order` 모델은 두 개의 `Address` 복합 타입을 가집니다. `shippingAddress`는 필수이고 `billingAddress`는 선택 사항입니다.

## 복합 타입 사용 시 고려사항

현재 Prisma Client에서 복합 타입을 사용할 때 몇 가지 제한사항이 있습니다:

- [`findUnique()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findunique)는 복합 타입으로 필터링할 수 없습니다.
- [`aggregate`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#aggregate), [`groupBy()`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#group-by), [`count`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#count)는 복합 타입 연산을 지원하지 않습니다.

## 복합 타입의 필수 필드 기본값

복합 타입에 대해 데이터베이스 읽기를 수행할 때 아래 조건이 모두 참이면 Prisma Client는 결과에 기본값을 삽입합니다:

- 복합 타입의 필드가 [필수](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#optional-and-mandatory-fields)이고
- 해당 필드에 [기본값](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-a-default-value)이 있으며
- 반환된 문서에 해당 필드가 존재하지 않는 경우

참고:

- 이는 [모델 필드](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)와 동일한 동작입니다.
- 읽기 작업에서 Prisma Client는 결과에 기본값을 삽입하지만, 데이터베이스에는 기본값을 삽입하지 않습니다.

예제 스키마에서 `photo`에 필수 필드를 추가했다고 가정해 봅시다. 이 필드 `bitDepth`는 기본값을 가집니다:

schema.prisma

```
    ...
    type Photo {
      ...
      bitDepth Int @default(8)
    }

    ...
```

그다음 `npx prisma db push`를 실행해 [데이터베이스를 업데이트](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push)하고, `npx prisma generate`로 Prisma Client를 다시 생성한다고 가정해 봅시다. 이후 아래 애플리케이션 코드를 실행합니다:

```
    console.dir(await prisma.product.findMany({}), { depth: Infinity });
```

`bitDepth` 필드는 방금 추가된 필드이므로 아직 값이 없어서, 쿼리는 기본값 `8`을 반환합니다.

## `find` 및 `findMany`로 복합 타입을 포함한 레코드 조회하기

레코드는 `where` 연산 내에서 복합 타입으로 필터링할 수 있습니다.

다음 섹션에서는 단일 타입 또는 다중 타입 필터링에 사용할 수 있는 연산과 각각의 예제를 설명합니다.

- 단일 복합 타입 필터링

단일 복합 타입을 변경하려면 `is`, `equals`, `isNot`, `isSet` 연산을 사용합니다:

- `is`: 일치하는 복합 타입으로 결과를 필터링합니다. 하나 이상의 필드가 있어야 합니다 _(예: 배송지 주소의 거리명으로 주문 필터링)_
- `equals`: 일치하는 복합 타입으로 결과를 필터링합니다. 모든 필드가 있어야 합니다. _(예: 전체 배송지 주소로 주문 필터링)_
- `isNot`: 일치하지 않는 복합 타입으로 결과를 필터링합니다.
- `isSet`: 선택 필드가 설정된 결과만 포함하도록 필터링합니다(값으로 설정되었거나 명시적으로 `null`로 설정된 경우). 이 필터를 `true`로 설정하면 전혀 설정되지 않은 `undefined` 결과는 제외됩니다.

예를 들어, 거리명이 `'555 Candy Cane Lane'`인 주문을 필터링하려면 `is`를 사용합니다:

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          is: {
            street: "555 Candy Cane Lane",
          },
        },
      },
    });
```

배송지 주소의 모든 필드가 일치하는 주문을 필터링하려면 `equals`를 사용합니다:

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          equals: {
            street: "555 Candy Cane Lane",
            city: "Wonderland",
            zip: "52337",
          },
        },
      },
    });
```

`equals`를 생략하는 축약 표기법도 사용할 수 있습니다:

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          street: "555 Candy Cane Lane",
          city: "Wonderland",
          zip: "52337",
        },
      },
    });
```

`zip` 코드가 `'52337'`이 아닌 주문을 필터링하려면 `isNot`을 사용합니다:

```
    const orders = await prisma.order.findMany({
      where: {
        shippingAddress: {
          isNot: {
            zip: "52337",
          },
        },
      },
    });
```

선택 필드인 `billingAddress`가 설정된(값 또는 `null`) 주문을 필터링하려면 `isSet`을 사용합니다:

```
    const orders = await prisma.order.findMany({
      where: {
        billingAddress: {
          isSet: true,
        },
      },
    });
```

- 다중 복합 타입 필터링

다중 복합 타입을 필터링하려면 `equals`, `isEmpty`, `every`, `some`, `none` 연산을 사용합니다:

- `equals`: 목록이 정확히 동일한지 확인합니다.
- `isEmpty`: 목록이 비어 있는지 확인합니다.
- `every`: 목록의 모든 항목이 조건과 일치해야 합니다.
- `some`: 목록의 하나 이상 항목이 조건과 일치해야 합니다.
- `none`: 목록의 어떤 항목도 조건과 일치하면 안 됩니다.
- `isSet`: 선택 필드가 설정된 결과만 포함하도록 필터링합니다(값으로 설정되었거나 명시적으로 `null`로 설정된 경우). 이 필터를 `true`로 설정하면 전혀 설정되지 않은 `undefined` 결과는 제외됩니다.

예를 들어 `equals`를 사용해 특정 사진 목록을 가진 제품을 찾을 수 있습니다(모든 `url`, `height`, `width` 필드가 일치해야 함):

```
    const product = prisma.product.findMany({
      where: {
        photos: {
          equals: [
            {
              url: "1.jpg",
              height: 200,
              width: 100,
            },
            {
              url: "2.jpg",
              height: 200,
              width: 100,
            },
          ],
        },
      },
    });
```

`equals`를 생략하고 필터링하려는 필드만 지정하는 축약 표기법도 사용할 수 있습니다:

```
    const product = prisma.product.findMany({
      where: {
        photos: [
          {
            url: "1.jpg",
            height: 200,
            width: 100,
          },
          {
            url: "2.jpg",
            height: 200,
            width: 100,
          },
        ],
      },
    });
```

사진이 없는 제품을 필터링하려면 `isEmpty`를 사용합니다:

```
    const product = prisma.product.findMany({
      where: {
        photos: {
          isEmpty: true,
        },
      },
    });
```

하나 이상의 사진에서 `url`이 `"2.jpg"`인 제품을 필터링하려면 `some`을 사용합니다:

```
    const product = prisma.product.findFirst({
      where: {
        photos: {
          some: {
            url: "2.jpg",
          },
        },
      },
    });
```

어떤 사진도 `url`이 `"2.jpg"`가 아닌 제품을 필터링하려면 `none`을 사용합니다:

```
    const product = prisma.product.findFirst({
      where: {
        photos: {
          none: {
            url: "2.jpg",
          },
        },
      },
    });
```

## `create` 및 `createMany`로 복합 타입이 포함된 레코드 생성하기

고유 제약 조건이 있는 복합 타입으로 레코드를 생성할 때는 MongoDB가 레코드 내부의 고유 값을 강제하지 않는다는 점에 유의하세요. [자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#duplicate-values-in-unique-fields-of-composite-types).

복합 타입은 `create` 또는 `createMany` 메서드 내에서 `set` 연산을 사용해 생성할 수 있습니다. 예를 들어 `create` 내에서 `set`을 사용해 `Order` 안에 `Address` 복합 타입을 생성할 수 있습니다:

```
    const order = await prisma.order.create({
      data: {
        // Normal relation
        product: { connect: { id: "some-object-id" } },
        color: "Red",
        size: "Large",
        // Composite type
        shippingAddress: {
          set: {
            street: "1084 Candycane Lane",
            city: "Silverlake",
            zip: "84323",
          },
        },
      },
    });
```

`set`을 생략하고 생성하려는 필드만 지정하는 축약 표기법도 사용할 수 있습니다:

```
    const order = await prisma.order.create({
      data: {
        // Normal relation
        product: { connect: { id: "some-object-id" } },
        color: "Red",
        size: "Large",
        // Composite type
        shippingAddress: {
          street: "1084 Candycane Lane",
          city: "Silverlake",
          zip: "84323",
        },
      },
    });
```

`billingAddress` 같은 선택 타입의 경우 값으로 `null`을 설정할 수도 있습니다:

```
    const order = await prisma.order.create({
      data: {
        // Normal relation
        product: { connect: { id: "some-object-id" } },
        color: "Red",
        size: "Large",
        // Composite type
        shippingAddress: {
          street: "1084 Candycane Lane",
          city: "Silverlake",
          zip: "84323",
        },
        // Embedded optional type, set to null
        billingAddress: {
          set: null,
        },
      },
    });
```

`product`가 여러 `photos` 목록을 포함하는 경우를 모델링하려면, 여러 복합 타입을 한 번에 `set`할 수 있습니다:

```
    const product = await prisma.product.create({
      data: {
        name: "Forest Runners",
        price: 59.99,
        colors: ["Red", "Green"],
        sizes: ["Small", "Medium", "Large"],
        // New composite type
        photos: {
          set: [
            { height: 100, width: 200, url: "1.jpg" },
            { height: 100, width: 200, url: "2.jpg" },
          ],
        },
      },
    });
```

`set`을 생략하고 생성하려는 필드만 지정하는 축약 표기법도 사용할 수 있습니다:

```
    const product = await prisma.product.create({
      data: {
        name: "Forest Runners",
        price: 59.99,
        // Scalar lists that we already support
        colors: ["Red", "Green"],
        sizes: ["Small", "Medium", "Large"],
        // New composite type
        photos: [
          { height: 100, width: 200, url: "1.jpg" },
          { height: 100, width: 200, url: "2.jpg" },
        ],
      },
    });
```

이 연산들은 `createMany` 메서드에서도 동작합니다. 예를 들어 각각 `photos` 목록을 포함한 여러 `product`를 생성할 수 있습니다:

```
    const product = await prisma.product.createMany({
      data: [
        {
          name: "Forest Runners",
          price: 59.99,
          colors: ["Red", "Green"],
          sizes: ["Small", "Medium", "Large"],
          photos: [
            { height: 100, width: 200, url: "1.jpg" },
            { height: 100, width: 200, url: "2.jpg" },
          ],
        },
        {
          name: "Alpine Blazers",
          price: 85.99,
          colors: ["Blue", "Red"],
          sizes: ["Large", "XLarge"],
          photos: [
            { height: 100, width: 200, url: "1.jpg" },
            { height: 150, width: 200, url: "4.jpg" },
            { height: 200, width: 200, url: "5.jpg" },
          ],
        },
      ],
    });
```

## `update` 및 `updateMany` 내에서 복합 타입 변경하기

고유 제약 조건이 있는 복합 타입으로 레코드를 업데이트할 때는 MongoDB가 레코드 내부의 고유 값을 강제하지 않는다는 점에 유의하세요. [자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#duplicate-values-in-unique-fields-of-composite-types).

복합 타입은 `update` 또는 `updateMany` 메서드 내에서 설정, 업데이트, 제거할 수 있습니다. 다음 섹션에서는 단일 타입 또는 다중 타입을 한 번에 업데이트할 때 사용할 수 있는 연산과 각각의 예제를 설명합니다.

- 단일 복합 타입 변경

단일 복합 타입을 변경하려면 `set`, `unset`, `update`, `upsert` 연산을 사용합니다:

- `set`을 사용하면 기존 값을 덮어쓰며 복합 타입을 설정합니다.
- `unset`을 사용하면 복합 타입 설정을 해제합니다. `set: null`과 달리 `unset`은 필드 자체를 완전히 제거합니다.
- `update`를 사용하면 복합 타입을 업데이트합니다.
- `upsert`를 사용하면 복합 타입이 존재할 경우 `update`하고, 존재하지 않으면 복합 타입을 `set`합니다.

예를 들어, `update`를 사용해 `Order` 안의 필수 `shippingAddress`를 `Address` 복합 타입으로 업데이트할 수 있습니다:

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        shippingAddress: {
          // Update just the zip field
          update: {
            zip: "41232",
          },
        },
      },
    });
```

`billingAddress` 같은 선택 임베디드 타입의 경우, 존재하지 않으면 새 레코드를 만들고 존재하면 업데이트하도록 `upsert`를 사용합니다:

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        billingAddress: {
          // Create the address if it doesn't exist,
          // otherwise update it
          upsert: {
            set: {
              street: "1084 Candycane Lane",
              city: "Silverlake",
              zip: "84323",
            },
            update: {
              zip: "84323",
            },
          },
        },
      },
    });
```

`unset` 연산을 사용해 선택 임베디드 타입을 제거할 수도 있습니다. 다음 예제는 `unset`으로 `Order`에서 `billingAddress`를 제거합니다:

```
    const order = await prisma.order.update({
      where: {
        id: "some-object-id",
      },
      data: {
        billingAddress: {
          // Unset the billing address
          // Removes "billingAddress" field from order
          unset: true,
        },
      },
    });
```

복합 타입과 일치하는 모든 레코드를 업데이트하려면 `updateMany` 내에서 [필터](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#finding-records-that-contain-composite-types-with-find-and-findmany)를 사용할 수 있습니다. 다음 예제는 주문 목록의 배송지 주소 거리명을 일치시키기 위해 `is` 필터를 사용합니다:

```
    const orders = await prisma.order.updateMany({
      where: {
        shippingAddress: {
          is: {
            street: "555 Candy Cane Lane",
          },
        },
      },
      data: {
        shippingAddress: {
          update: {
            street: "111 Candy Cane Drive",
          },
        },
      },
    });
```

- 다중 복합 타입 변경

복합 타입 목록을 변경하려면 `set`, `push`, `updateMany`, `deleteMany` 연산을 사용합니다:

- `set`: 복합 타입의 임베디드 목록을 설정하며 기존 목록을 덮어씁니다.
- `push`: 복합 타입의 임베디드 목록 끝에 값을 추가합니다.
- `updateMany`: 여러 복합 타입을 한 번에 업데이트합니다.
- `deleteMany`: 여러 복합 타입을 한 번에 삭제합니다.

예를 들어 `push`를 사용해 `photos` 목록에 새 사진을 추가할 수 있습니다:

```
    const product = prisma.product.update({
      where: {
        id: "62de6d328a65d8fffdae2c18",
      },
      data: {
        photos: {
          // Push a photo to the end of the photos list
          push: [{ height: 100, width: 200, url: "1.jpg" }],
        },
      },
    });
```

`url`이 `1.jpg` 또는 `2.png`인 사진을 업데이트하려면 `updateMany`를 사용합니다:

```
    const product = prisma.product.update({
      where: {
        id: "62de6d328a65d8fffdae2c18",
      },
      data: {
        photos: {
          updateMany: {
            where: {
              url: "1.jpg",
            },
            data: {
              url: "2.png",
            },
          },
        },
      },
    });
```

다음 예제는 `deleteMany`를 사용해 `height`가 100인 사진을 모두 삭제합니다:

```
    const product = prisma.product.update({
      where: {
        id: "62de6d328a65d8fffdae2c18",
      },
      data: {
        photos: {
          deleteMany: {
            where: {
              height: 100,
            },
          },
        },
      },
    });
```

## `upsert`로 복합 타입 업서트하기

고유 제약 조건이 있는 복합 타입의 값을 생성하거나 업데이트할 때는 MongoDB가 레코드 내부의 고유 값을 강제하지 않는다는 점에 유의하세요. [자세히 알아보기](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#duplicate-values-in-unique-fields-of-composite-types).

복합 타입을 생성하거나 업데이트하려면 `upsert` 메서드를 사용하세요. 위의 `create` 및 `update` 메서드와 동일한 복합 연산을 사용할 수 있습니다.

예를 들어 `upsert`를 사용해 새 제품을 생성하거나 기존 제품에 사진을 추가할 수 있습니다:

```
    const product = await prisma.product.upsert({
      where: {
        name: "Forest Runners",
      },
      create: {
        name: "Forest Runners",
        price: 59.99,
        colors: ["Red", "Green"],
        sizes: ["Small", "Medium", "Large"],
        photos: [
          { height: 100, width: 200, url: "1.jpg" },
          { height: 100, width: 200, url: "2.jpg" },
        ],
      },
      update: {
        photos: {
          push: { height: 300, width: 400, url: "3.jpg" },
        },
      },
    });
```

## `delete` 및 `deleteMany`로 복합 타입을 포함한 레코드 삭제하기

복합 타입을 내장한 레코드를 제거하려면 `delete` 또는 `deleteMany` 메서드를 사용하세요. 이렇게 하면 내장된 복합 타입도 함께 제거됩니다.

예를 들어 `deleteMany`를 사용해 `size`가 `"Small"`인 모든 제품을 삭제할 수 있습니다. 이 경우 내장된 `photos`도 함께 삭제됩니다.

```
    const deleteProduct = await prisma.product.deleteMany({
      where: {
        sizes: {
          equals: "Small",
        },
      },
    });
```

또한 [필터](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#finding-records-that-contain-composite-types-with-find-and-findmany)를 사용해 복합 타입과 일치하는 레코드를 삭제할 수 있습니다. 아래 예시는 `some` 필터를 사용해 특정 사진을 포함한 제품을 삭제합니다:

```
    const product = await prisma.product.deleteMany({
      where: {
        photos: {
          some: {
            url: "2.jpg",
          },
        },
      },
    });
```

## 복합 타입 정렬하기

`orderBy` 연산을 사용해 결과를 오름차순 또는 내림차순으로 정렬할 수 있습니다.

예를 들어 다음 명령은 모든 주문을 조회하고, 배송 주소의 도시 이름 기준으로 오름차순 정렬합니다:

```
    const orders = await prisma.order.findMany({
      orderBy: {
        shippingAddress: {
          city: "asc",
        },
      },
    });
```

## 복합 타입의 고유 필드에서 중복 값

고유 제약 조건이 있는 복합 타입을 포함한 레코드에서 다음 작업을 수행할 때 주의하세요. 이 경우 MongoDB는 레코드 내부의 고유 값을 강제하지 않습니다.

- 레코드를 생성할 때
- 레코드에 데이터를 추가할 때
- 레코드의 데이터를 업데이트할 때

스키마에 `@@unique` 제약 조건이 있는 복합 타입이 있으면, MongoDB는 이 복합 타입을 포함한 두 개 이상의 레코드에 대해 제약 대상 값이 동일하게 저장되는 것을 방지합니다. 하지만 MongoDB는 단일 레코드 안에 동일한 필드 값을 여러 개 저장하는 것은 막지 않습니다.

이 문제는 [Prisma ORM relation을 사용해 우회할 수 있습니다](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/composite-types#use-prisma-orm-relations-to-enforce-unique-values-in-a-record).

예를 들어 다음 스키마에서 `MailBox`는 `addresses`라는 복합 타입을 가지며, 이 타입은 `email` 필드에 `@@unique` 제약 조건이 있습니다.

```
    type Address {
      email String
    }

    model MailBox {
      name      String
      addresses Address[]

      @@unique([addresses.email])
    }
```

다음 코드는 `address`에 동일한 값 두 개를 가진 레코드를 생성합니다. 이 상황에서 MongoDB는 오류를 발생시키지 않으며, `alice@prisma.io`를 `addresses`에 두 번 저장합니다.

```
    await prisma.MailBox.createMany({
      data: [
        {
          name: "Alice",
          addresses: {
            set: [
              {
                address: "alice@prisma.io", // Not unique
              },
              {
                address: "alice@prisma.io", // Not unique
              },
            ],
          },
        },
      ],
    });
```

참고: 동일한 값을 서로 다른 두 레코드에 저장하려고 하면 MongoDB는 오류를 발생시킵니다. 위 예시에서 사용자 Alice와 사용자 Bob 모두에게 이메일 주소 `alice@prisma.io`를 저장하려고 하면, MongoDB는 데이터를 저장하지 않고 오류를 발생시킵니다.

- 레코드에서 고유 값을 강제하기 위해 Prisma ORM relation 사용하기

위 예시에서는 MongoDB가 중첩된 주소 이름의 고유 제약 조건을 강제하지 않았습니다. 하지만 데이터를 다르게 모델링하면 레코드 내 고유 값을 강제할 수 있습니다. 이를 위해 Prisma ORM의 [relations](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)을 사용해 복합 타입을 컬렉션으로 전환하세요. 이 컬렉션과의 관계를 설정하고, 고유해야 하는 필드에 고유 제약 조건을 배치합니다.

다음 예시에서는 MongoDB가 레코드 내 고유 값을 강제합니다. `Mailbox`와 `Address` 모델 사이에 relation이 있으며, `Address` 모델의 `name` 필드에도 고유 제약 조건이 있습니다.

```
    model Address {
      id        String   @id @default(auto()) @map("_id") @db.ObjectId
      name      String
      mailbox   Mailbox? @relation(fields: [mailboxId], references: [id])
      mailboxId String?  @db.ObjectId

      @@unique([name])
    }

    model Mailbox {
      id        String    @id @default(auto()) @map("_id") @db.ObjectId
      name      String
      addresses Address[] @relation
    }
```

```
    await prisma.MailBox.create({
      data: {
        name: "Alice",
        addresses: {
          create: [
            { name: "alice@prisma.io" }, // Not unique
            { name: "alice@prisma.io" }, // Not unique
          ],
        },
      },
    });
```

위 코드를 실행하면 MongoDB가 고유 제약 조건을 강제합니다. 애플리케이션에서 이름이 `alice@prisma.io`인 주소 두 개를 추가하는 것을 허용하지 않습니다.
