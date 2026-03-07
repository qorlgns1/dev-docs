---
title: "scalar list 작업하기"
description: "scalar list / 배열을 읽고, 쓰고, 필터링하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-scalar-lists-arrays

# scalar list 작업하기

scalar list / 배열을 읽고, 쓰고, 필터링하는 방법

[Scalar lists](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#-modifier)는 `[]` 수정자로 표현되며, 기본 데이터베이스가 scalar list를 지원하는 경우에만 사용할 수 있습니다. 다음 예시에는 `pets`라는 이름의 scalar `String` list가 하나 있습니다.

관계형 데이터베이스

MongoDB

```
    model User {
      id   Int      @id @default(autoincrement())
      name String
      pets String[]
    }
```

필드 값 예시:

```
    ["Fido", "Snoopy", "Brian"]
```

## scalar list 값 설정하기

다음 예시는 모델을 생성할 때 scalar list(`coinflips`)의 값을 [`set`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference)하는 방법을 보여줍니다:

```
    const createdUser = await prisma.user.create({
      data: {
        email: "eloise@prisma.io",
        coinflips: [true, true, true, false, true],
      },
    });
```

## scalar list 값 해제하기

이 방법은 MongoDB에서만 사용할 수 있습니다.

다음 예시는 scalar list(`coinflips`)의 값을 [`unset`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#unset)하는 방법을 보여줍니다:

```
    const createdUser = await prisma.user.create({
      data: {
        email: "eloise@prisma.io",
        coinflips: {
          unset: true,
        },
      },
    });
```

`set: null`과 달리 `unset`은 리스트 자체를 완전히 제거합니다.

## scalar list에 항목 추가하기

PostgreSQL, CockroachDB, MongoDB에서 사용할 수 있습니다.

scalar list에 단일 값을 추가하려면 [`push`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#push) 메서드를 사용하세요:

```
    const userUpdate = await prisma.user.update({
      where: {
        id: 9,
      },
      data: {
        coinflips: {
          push: true,
        },
      },
    });
```

이전 버전에서는 전체 값을 덮어써야 합니다. 다음 예시는 user를 조회하고, `push()`를 사용해 새 coin flip 세 개를 추가한 뒤, `update`에서 `coinflips` 필드를 덮어씁니다:

```
    const user = await prisma.user.findUnique({
      where: {
        email: "eloise@prisma.io",
      },
    });

    if (user) {
      console.log(user.coinflips);

      user.coinflips.push(true, true, false);

      const updatedUser = await prisma.user.update({
        where: {
          email: "eloise@prisma.io",
        },
        data: {
          coinflips: user.coinflips,
        },
      });

      console.log(updatedUser.coinflips);
    }
```

## scalar list 필터링

PostgreSQL, CockroachDB, MongoDB에서 사용할 수 있습니다.

특정 조건과 일치하는 scalar list를 가진 레코드를 필터링하려면 [scalar list filters](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#scalar-list-filters)를 사용하세요. 다음 예시는 tags 리스트에 `databases` _및_ `typescript`가 포함된 모든 post를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          hasEvery: ["databases", "typescript"],
        },
      },
    });
```

- 배열의 `NULL` 값

이 섹션은 PostgreSQL과 CockroachDB에 적용됩니다.

관계형 데이터베이스 커넥터에서 scalar list filter를 사용할 때, 값이 `NULL`인 배열 필드는 다음 조건에서 고려되지 않습니다:

- `NOT` (배열에 X가 포함되지 않음)
- `isEmpty` (배열이 비어 있음)

즉, 보일 것으로 예상한 레코드가 반환되지 않을 수 있습니다. 다음 예시를 살펴보세요:

- 다음 쿼리는 `tags`에 `databases`가 **포함되지 않은** 모든 post를 반환합니다:

```
const posts = await prisma.post.findMany({
          where: {
            NOT: {
              tags: {
                has: "databases",
              },
            },
          },
        });
```

    * ✔ `"databases"`를 포함하지 않는 배열(예: `{"typescript", "graphql"}`)
    * ✔ 빈 배열(예: `[]`)

이 쿼리는 다음을 반환하지 않습니다:

    * ✘ `"databases"`를 포함하지 않더라도 `NULL` 배열은 반환되지 않음

다음 쿼리는 `tags`가 비어 있는 모든 post를 반환합니다:

```
    const posts = await prisma.post.findMany({
      where: {
        tags: {
          isEmpty: true,
        },
      },
    });
```

이 쿼리는 다음을 반환합니다:

- ✔ 빈 배열(예: `[]`)

이 쿼리는 다음을 반환하지 않습니다:

- ✘ 비어 있다고 볼 수 있더라도 `NULL` 배열은 반환되지 않음

이 문제를 우회하려면 배열 필드의 기본값을 `[]`로 설정할 수 있습니다.
