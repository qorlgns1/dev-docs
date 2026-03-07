---
title: "Json 필드 사용하기"
description: "Json 필드를 읽고, 쓰고, 필터링하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields

# Json 필드 사용하기

Json 필드를 읽고, 쓰고, 필터링하는 방법

기본 데이터베이스의 JSON 타입에서 읽기, 쓰기, 기본 필터링을 수행하려면 [`Json`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#json) Prisma ORM 필드 타입을 사용하세요. 다음 예시에서 `User` 모델은 `extendedPetsData`라는 선택적 `Json` 필드를 가집니다:

```
    model User {
      id               Int     @id @default(autoincrement())
      email            String  @unique
      name             String?
      posts            Post[]
      extendedPetsData Json?
    }
```

필드 값 예시:

```
    {
      "pet1": {
        "petName": "Claudine",
        "petType": "House cat"
      },
      "pet2": {
        "petName": "Sunny",
        "petType": "Gerbil"
      }
    }
```

`Json` 필드는 `string`, `boolean` 같은 몇 가지 추가 타입도 지원합니다. 이러한 추가 타입은 [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)에서 지원하는 타입과 맞추기 위해 존재합니다:

```
    export type JsonValue = string | number | boolean | null | JsonObject | JsonArray;
```

## JSON 필드의 사용 사례

데이터를 관련 모델로 표현하는 대신 JSON으로 저장하는 이유는 다음과 같습니다:

- 일관된 구조가 없는 데이터를 저장해야 하는 경우
- 다른 시스템에서 데이터를 가져오며, 해당 데이터를 Prisma 모델에 매핑하고 싶지 않은 경우

## `Json` 필드 읽기

`Prisma.JsonArray` 및 `Prisma.JsonObject` 유틸리티 클래스를 사용해 `Json` 필드의 내용을 다룰 수 있습니다:

```
    const { PrismaClient, Prisma } = require("@prisma/client");

    const user = await prisma.user.findFirst({
      where: {
        id: 9,
      },
    });

    // Example extendedPetsData data:
    // [{ name: 'Bob the dog' }, { name: 'Claudine the cat' }]

    if (
      user?.extendedPetsData &&
      typeof user?.extendedPetsData === "object" &&
      Array.isArray(user?.extendedPetsData)
    ) {
      const petsObject = user?.extendedPetsData as Prisma.JsonArray;

      const firstPet = petsObject[0];
    }
```

참고: [고급 예시: 중첩 JSON 키 값 업데이트](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#advanced-example-update-a-nested-json-key-value)

## `Json` 필드에 쓰기

다음 예시는 JSON 객체를 `extendedPetsData` 필드에 기록합니다:

```
    var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }] as Prisma.JsonArray;

    const createUser = await prisma.user.create({
      data: {
        email: "birgitte@prisma.io",
        extendedPetsData: json,
      },
    });
```

> **참고** : JavaScript 객체(예: `{ extendedPetsData: "none"}`)는 자동으로 JSON으로 변환됩니다.

참고: [고급 예시: 중첩 JSON 키 값 업데이트](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#advanced-example-update-a-nested-json-key-value)

## `Json` 필드 필터링(기본)

`Json` 타입 행을 필터링할 수 있습니다.

- 정확한 필드 값으로 필터링

다음 쿼리는 `extendedPetsData` 값이 `json` 변수와 정확히 일치하는 모든 사용자를 반환합니다:

```
    var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }];

    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          equals: json,
        },
      },
    });
```

다음 쿼리는 `extendedPetsData` 값이 `json` 변수와 정확히 일치하지 **않는** 모든 사용자를 반환합니다:

```
    var json = [{ name: "Bob the dog" }, { name: "Claudine the cat" }];

    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          not: json,
        },
      },
    });
```

## `Json` 필드 필터링(고급)

`Json` 필드 내부 데이터로도 행을 필터링할 수 있습니다. 이를 **고급 `Json` 필터링**이라고 부릅니다. 이 기능은 [PostgreSQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)과 [MySQL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)에서만 지원되며, [`path` 옵션 문법은 데이터베이스마다 다릅니다](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#path-syntax-depending-on-database).

PostgreSQL은 [배열 내부 객체 키 값 필터링](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#filtering-on-object-key-value-inside-array)을 지원하지 않습니다.

- 데이터베이스별 `path` 문법

아래 필터는 `path` 옵션을 사용해 `Json` 값의 특정 부분을 선택해 필터링합니다. 이 필터링의 구현은 커넥터마다 다릅니다:

- [MySQL connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)는 [MySQL의 JSON path 구현](https://dev.mysql.com/doc/refman/8.0/en/json.html#json-path-syntax)을 사용합니다.
- [PostgreSQL connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql)는 [12 버전 _이전 및 포함_ 에서 지원되는](https://www.postgresql.org/docs/11/functions-json.html) 사용자 정의 JSON 함수와 연산자를 사용합니다.

예를 들어, 다음은 유효한 MySQL `path` 값입니다:

```
    $petFeatures.petName
```

다음은 유효한 PostgreSQL `path` 값입니다:

```
    ["petFeatures", "petName"]
```

- 객체 속성으로 필터링

JSON 블록 내부의 특정 속성으로 필터링할 수 있습니다. 다음 예시에서 `extendedPetsData` 값은 1차원 비중첩 JSON 객체입니다:

```
    {
      "petName": "Claudine",
      "petType": "House cat"
    }
```

다음 쿼리는 `petName` 값이 `"Claudine"`인 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["petName"],
          equals: "Claudine",
        },
      },
    });
```

다음 쿼리는 `petType` 값에 `"cat"`이 _포함된_ 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["petType"],
          string_contains: "cat",
        },
      },
    });
```

사용 가능한 문자열 필터는 다음과 같습니다:

- `string_contains`
- `string_starts_with`
- [`string_ends_with`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#string_ends_with) .

여기에 대소문자 구분 없는 필터를 사용하려면 [`mode`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#mode) 옵션을 사용할 수 있습니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["petType"],
          string_contains: "cat",
          mode: "insensitive",
        },
      },
    });
```

- 중첩 객체 속성으로 필터링

중첩된 JSON 속성으로 필터링할 수 있습니다. 다음 예시에서 `extendedPetsData` 값은 여러 단계로 중첩된 JSON 객체입니다.

```
    {
      "pet1": {
        "petName": "Claudine",
        "petType": "House cat"
      },
      "pet2": {
        "petName": "Sunny",
        "petType": "Gerbil",
        "features": {
          "eyeColor": "Brown",
          "furColor": "White and black"
        }
      }
    }
```

다음 쿼리는 `"pet2"` → `"petName"`이 `"Sunny"`인 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["pet2", "petName"],
          equals: "Sunny",
        },
      },
    });
```

다음 쿼리는 아래 조건을 모두 만족하는 모든 사용자를 반환합니다:

- `"pet2"` → `"petName"`이 `"Sunny"`
- `"pet2"` → `"features"` → `"furColor"`에 `"black"`이 포함됨

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        AND: [
          {
            extendedPetsData: {
              path: ["pet2", "petName"],
              equals: "Sunny",
            },
          },
          {
            extendedPetsData: {
              path: ["pet2", "features", "furColor"],
              string_contains: "black",
            },
          },
        ],
      },
    });
```

- 배열 값 필터링

스칼라 배열(문자열, 정수)에 특정 값이 존재하는지 필터링할 수 있습니다. 다음 예시에서 `extendedPetsData` 값은 문자열 배열입니다:

```
    ["Claudine", "Sunny"]
```

다음 쿼리는 `"Claudine"`이라는 이름의 반려동물이 있는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          array_contains: ["Claudine"],
        },
      },
    });
```

PostgreSQL에서는 배열에 단일 값만 포함되어 있어도 `array_contains` 값은 문자열이 아니라 배열이어야 합니다.

사용 가능한 배열 필터는 다음과 같습니다:

- `array_contains`
- `array_starts_with`
- `array_ends_with`

* 중첩 배열 값 필터링

스칼라 배열(문자열, 정수)에 특정 값이 존재하는지 필터링할 수 있습니다. 다음 예시에서 `extendedPetsData` 값에는 이름의 중첩 스칼라 배열이 포함됩니다:

```
    {
      "cats": { "owned": ["Bob", "Sunny"], "fostering": ["Fido"] },
      "dogs": { "owned": ["Ella"], "fostering": ["Prince", "Empress"] }
    }
```

#

- 스칼라 값 배열

다음 쿼리는 `"Fido"`라는 이름의 고양이를 임시 보호하는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["cats", "fostering"],
          array_contains: ["Fido"],
        },
      },
    });
```

PostgreSQL에서는 배열에 단일 값만 포함되어 있어도 `array_contains` 값은 문자열이 아니라 배열이어야 합니다.

다음 쿼리는 `"Fido"` _그리고_ `"Bob"`이라는 이름의 고양이를 임시 보호하는 모든 사용자를 반환합니다:

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["cats", "fostering"],
          array_contains: ["Fido", "Bob"],
        },
      },
    });
```

#

- JSON 객체 배열

PostgreSQL

MySQL

```
    const json = [{ status: "expired", insuranceID: 92 }];

    const checkJson = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["insurances"],
          array_contains: json,
        },
      },
    });
```

- PostgreSQL을 사용하는 경우, 배열에 객체가 하나만 있어도 매칭할 객체 배열을 전달해야 합니다:

```
[{ status: "expired", insuranceID: 92 }]
        // PostgreSQL
```

MySQL을 사용하는 경우, 매칭할 단일 객체를 전달해야 합니다:

```
{ status: "expired", insuranceID: 92 }
        // MySQL
```

- 필터 배열에 여러 객체가 포함된 경우 PostgreSQL은 _하나 이상_ 이 아니라 _모든_ 객체가 존재할 때만 결과를 반환합니다.

- `array_contains`는 문자열이 아니라 JSON 객체로 설정해야 합니다. 문자열을 사용하면 Prisma Client가 따옴표를 이스케이프하여 쿼리가 결과를 반환하지 않습니다. 예:

```
array_contains: '[{"status": "expired", "insuranceID": 92}]';
```

는 데이터베이스에 다음과 같이 전송됩니다:

```
[{\"status\": \"expired\", \"insuranceID\": 92}]
```

- 인덱스로 배열 요소 지정

특정 위치에 있는 요소의 값으로 필터링할 수 있습니다.

```
    { "owned": ["Bob", "Sunny"], "fostering": ["Fido"] }
```

PostgreSQL

MySQL

```
    const getUsers = await prisma.user.findMany({
      where: {
        comments: {
          path: ["owned", "1"],
          string_contains: "Bob",
        },
      },
    });
```

- 배열 내부 객체 키 값 필터링

provider에 따라 배열 내부 객체의 키 값으로 필터링할 수 있습니다.

배열 내 객체 키 값 필터링은 [MySQL database connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql)에서만 지원됩니다. 다만 여전히 [전체 JSON 객체의 존재 여부로 필터링](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#json-object-arrays)은 가능합니다.

다음 예시에서 `extendedPetsData` 값은 중첩된 `insurances` 배열을 가진 객체 배열이며, 해당 배열에는 두 개의 객체가 포함되어 있습니다:

```
    [
      {
        "petName": "Claudine",
        "petType": "House cat",
        "insurances": [
          { "insuranceID": 92, "status": "expired" },
          { "insuranceID": 12, "status": "active" }
        ]
      },
      {
        "petName": "Sunny",
        "petType": "Gerbil"
      },
      {
        "petName": "Gerald",
        "petType": "Corn snake"
      },
      {
        "petName": "Nanna",
        "petType": "Moose"
      }
    ]
```

다음 쿼리는 최소 한 마리의 반려동물이 무스인 모든 사용자를 반환합니다:

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: "$[*].petType",
          array_contains: "Moose",
        },
      },
    });
```

- `$[*]`는 반려동물 객체의 루트 배열입니다.
- `petType`은 모든 반려동물 객체의 `petType` 키와 매칭됩니다.

다음 쿼리는 최소 한 마리의 반려동물이 만료된 보험을 가진 모든 사용자를 반환합니다:

```
    const getUsers = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: "$[*].insurances[*].status",
          array_contains: "expired",
        },
      },
    });
```

- `$[*]`는 반려동물 객체의 루트 배열입니다.
- `insurances[*]`는 모든 반려동물 객체 내부의 모든 `insurances` 배열과 매칭됩니다.
- `status`는 모든 보험 객체의 모든 `status` 키와 매칭됩니다.

## 고급 예시: 중첩 JSON 키 값 업데이트

다음 예시는 `extendedPetsData` 값이 아래와 같은 형태라고 가정합니다:

```
    {
      "petName": "Claudine",
      "petType": "House cat",
      "insurances": [
        { "insuranceID": 92, "status": "expired" },
        { "insuranceID": 12, "status": "active" }
      ]
    }
```

다음 예시는:

1. 모든 사용자를 가져오고
2. 각 보험 객체의 `"status"`를 `"expired"`로 변경한 뒤
3. ID가 `92`인 만료 보험이 있는 모든 사용자를 가져옵니다.

PostgreSQL

MySQL

```
    const userQueries: string | any[] = [];

    getUsers.forEach((user) => {
      if (
        user.extendedPetsData &&
        typeof user.extendedPetsData === "object" &&
        !Array.isArray(user.extendedPetsData)
      ) {
        const petsObject = user.extendedPetsData as Prisma.JsonObject;

        const i = petsObject["insurances"];

        if (i && typeof i === "object" && Array.isArray(i)) {
          const insurancesArray = i as Prisma.JsonArray;

          insurancesArray.forEach((i) => {
            if (i && typeof i === "object" && !Array.isArray(i)) {
              const insuranceObject = i as Prisma.JsonObject;

              insuranceObject["status"] = "expired";
            }
          });

          const whereClause = Prisma.validator<Prisma.UserWhereInput>()({
            id: user.id,
          });

          const dataClause = Prisma.validator<Prisma.UserUpdateInput>()({
            extendedPetsData: petsObject,
          });

          userQueries.push(
            prisma.user.update({
              where: whereClause,
              data: dataClause,
            }),
          );
        }
      }
    });

    if (userQueries.length > 0) {
      console.log(userQueries.length + " queries to run!");
      await prisma.$transaction(userQueries);
    }

    const json = [{ status: "expired", insuranceID: 92 }];

    const checkJson = await prisma.user.findMany({
      where: {
        extendedPetsData: {
          path: ["insurances"],
          array_contains: json,
        },
      },
    });

    console.log(checkJson.length);
```

## `null` 값 사용하기

SQL 데이터베이스의 `JSON` 필드에는 두 종류의 `null` 값이 있을 수 있습니다.

- 데이터베이스 `NULL`: 데이터베이스의 값이 `NULL`입니다.
- JSON `null`: 데이터베이스 값에 `null`인 JSON 값이 포함되어 있습니다.

이 두 경우를 구분하기 위해 사용할 수 있는 세 가지 _null enum_ 을 도입했습니다:

- `JsonNull`: JSON의 `null` 값을 나타냅니다.
- `DbNull`: 데이터베이스의 `NULL` 값을 나타냅니다.

- `AnyNull`: JSON `null` 값과 데이터베이스 `NULL` 값을 모두 나타냅니다. (필터링 시에만)
  - _null enums_ 중 하나로 필터링할 때는 축약형을 사용해 `equals` 연산자를 생략할 수 없습니다.
  - MongoDB에서는 JSON `null`과 데이터베이스 `NULL`의 차이가 없으므로 이러한 _null enums_ 가 적용되지 않습니다.
  - 모든 데이터베이스에서 `array_contains` 연산자에는 _null enums_ 가 적용되지 않습니다. JSON 배열 안에는 JSON `null`만 존재할 수 있기 때문입니다. JSON 배열 안에는 데이터베이스 `NULL`이 있을 수 없으므로 `{ array_contains: null }`은 모호하지 않습니다.

예시:

```
    model Log {
      id   Int  @id
      meta Json
    }
```

다음은 `AnyNull` 사용 예시입니다:

```
    import { Prisma } from "@prisma/client";

    prisma.log.findMany({
      where: {
        data: {
          meta: {
            equals: Prisma.AnyNull,
          },
        },
      },
    });
```

- `null` 값 삽입하기

이는 `create`, `update`, `upsert`에도 동일하게 적용됩니다. `Json` 필드에 `null` 값을 삽입하려면 다음과 같이 작성합니다:

```
    import { Prisma } from "@prisma/client";

    prisma.log.create({
      data: {
        meta: Prisma.JsonNull,
      },
    });
```

그리고 `Json` 필드에 데이터베이스 `NULL`을 삽입하려면 다음과 같이 작성합니다:

```
    import { Prisma } from "@prisma/client";

    prisma.log.create({
      data: {
        meta: Prisma.DbNull,
      },
    });
```

- `null` 값으로 필터링하기

`JsonNull` 또는 `DbNull`로 필터링하려면 다음과 같이 작성합니다:

```
    import { Prisma } from "@prisma/client";

    prisma.log.findMany({
      where: {
        meta: {
          equals: Prisma.AnyNull,
        },
      },
    });
```

MongoDB는 JSON `null`과 데이터베이스 `NULL`을 구분하지 않으므로 이러한 _null enums_ 는 MongoDB에 적용되지 않습니다. 또한 모든 데이터베이스에서 `array_contains` 연산자에도 적용되지 않습니다. JSON 배열 안에는 JSON `null`만 존재할 수 있기 때문입니다. JSON 배열 안에는 데이터베이스 `NULL`이 있을 수 없으므로 `{ array_contains: null }`은 모호하지 않습니다.

## 타입이 지정된 `Json` 필드

Prisma의 `Json` 필드는 기본적으로 타입이 지정되어 있지 않습니다. 강한 타입 지정을 추가하려면 외부 패키지 [prisma-json-types-generator](https://www.npmjs.com/package/prisma-json-types-generator)를 사용할 수 있습니다.

1. 먼저 패키지를 설치하고 `schema.prisma`에 generator를 추가합니다:

npm

pnpm

yarn

bun

```
npm install -D prisma-json-types-generator
```

schema.prisma

```
generator client {
           provider = "prisma-client"
           output   = "./generated"
         }

         generator json {
           provider = "prisma-json-types-generator"
         }
```

2. 다음으로 [AST comment](https://docs.prisma.io/docs/orm/prisma-schema/overview#comments)를 사용해 필드를 TypeScript 타입에 연결합니다.

schema.prisma

```
model Log {
           id   Int @id

           /// [LogMetaType]
           meta Json
         }
```

3. 그런 다음 `tsconfig.json`에 포함되는 타입 선언 파일(예: `types.ts`)에서 `LogMetaType`을 정의합니다.

types.ts

```
declare global {
           namespace PrismaJson {
             type LogMetaType = { timestamp: number; host: string };
           }
         }

         // This file must be a module.
         export {};
```

이제 `Log.meta`는 `{ timestamp: number; host: string }`으로 강하게 타입 지정됩니다.

- `String` 필드 타입 지정 및 고급 기능

이 기법은 `String` 필드에도 적용할 수 있습니다. 데이터베이스가 enum 타입을 지원하지 않을 때 스키마에서 문자열 기반 enum을 직접 만들 때 특히 유용합니다.

```
    model Post {
      id     Int    @id

      /// !['draft' | 'published']
      status String

      /// [LogMetaType]
      meta   Json[]
    }
```

그 결과 `post.status`는 `'draft' | 'published'`로, `post.meta`는 `LogMetaType[]`로 강하게 타입 지정됩니다.

구성, 모노레포 설정 및 기타 고급 기능에 대한 전체 가이드는 [공식 `prisma-json-types-generator` 문서](https://github.com/arthurfiorette/prisma-json-types-generator#readme)를 참고하세요.

## `Json` FAQ

- 반환할 JSON key/value의 일부만 선택할 수 있나요?

아니요. 아직 [반환할 JSON 요소를 선택](https://github.com/prisma/prisma/issues/2431)할 수 없습니다. Prisma Client는 전체 JSON 객체를 반환합니다.

- 특정 키의 존재 여부로 필터링할 수 있나요?

아니요. 아직 특정 키의 존재 여부로 필터링할 수 없습니다.

- 대소문자 구분 없는 필터링을 지원하나요?

네. `string_contains`, `string_starts_with`, `string_ends_with` 같은 문자열 필터에서 `mode: 'insensitive'` 옵션을 사용할 수 있습니다. 예시는 [객체 속성으로 필터링](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#filter-on-object-property)을 참고하세요.

- JSON 값 내부의 객체 속성을 기준으로 정렬할 수 있나요?

아니요. [JSON 값 내부 객체 속성 정렬](https://github.com/prisma/prisma/issues/10346)(order-by-prop)은 현재 지원되지 않습니다.

- JSON 필드의 기본값은 어떻게 설정하나요?

`Json` 타입에 `@default` 값을 설정하려면 `@default` 속성 내부에서 이중 따옴표로 감싸야 합니다(필요한 경우 백슬래시를 사용해 내부 이중 따옴표를 이스케이프). 예:

```
    model User {
      id    Int  @id @default(autoincrement())
      json1 Json @default("[]")
      json2 Json @default("{ \"hello\": \"world\" }")
    }
```
