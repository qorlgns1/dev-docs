---
title: "집계, 그룹화 및 요약"
description: "Prisma Client를 사용해 집계하고, 그룹화하고, 개수를 세고, 고유 값을 선택할 수 있습니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing

# 집계, 그룹화 및 요약

Prisma Client를 사용해 집계하고, 그룹화하고, 개수를 세고, 고유 값을 선택할 수 있습니다.

Prisma Client를 사용하면 레코드 수를 계산하고, 숫자 필드를 집계하며, 필드의 고유 값을 선택할 수 있습니다.

## Aggregate

Prisma Client에서는 모델의 **숫자** 필드(`Int`, `Float` 등)에 대해 [`aggregate`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#aggregate)를 수행할 수 있습니다. 다음 쿼리는 모든 사용자의 평균 나이를 반환합니다:

```
    const aggregations = await prisma.user.aggregate({
      _avg: { age: true },
    });

    console.log('Average age:' + aggregations._avg.age);
```

집계는 필터링 및 정렬과 함께 사용할 수 있습니다. 예를 들어, 다음 쿼리는 다음 조건으로 사용자 평균 나이를 반환합니다:

- `age` 오름차순 정렬
- `email`에 `prisma.io` 포함
- 사용자 10명으로 제한

```
    const aggregations = await prisma.user.aggregate({
      _avg: { age: true },
      where: {
        email: {
          contains: 'prisma.io',
        },
      },
      orderBy: { age: 'asc' },
      take: 10,
    });

    console.log('Average age:' + aggregations._avg.age);
```

- 집계 값은 nullable입니다

**nullable 필드**에 대한 집계는 `number` 또는 `null`을 반환할 수 있습니다. 단, `count`는 예외이며 레코드를 찾지 못하면 항상 0을 반환합니다.

다음 쿼리를 보세요. 여기서 스키마의 `age`는 nullable입니다:

```
    const aggregations = await prisma.user.aggregate({
      _avg: { age: true },
      _count: { age: true },
    });
```

```
    {
      "_avg": { "age": null },
      "_count": { "age": 9 }
    }
```

다음 두 경우 모두 쿼리는 `{ _avg: { age: null } }`을 반환합니다:

- 사용자가 없는 경우
- 모든 사용자의 `age` 필드 값이 `null`인 경우

이를 통해 실제 집계 값(0일 수도 있음)과 데이터 없음 상태를 구분할 수 있습니다.

## Group by

Prisma Client의 [`groupBy()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#groupby)를 사용하면 `country` 또는 `country`와 `city` 같은 하나 이상의 필드 값으로 **레코드를 그룹화**하고, 각 그룹에 대해 **집계 수행**(예: 특정 도시에 사는 사람들의 평균 나이 계산)할 수 있습니다.

다음 예시는 모든 사용자를 `country` 필드로 그룹화하고, 각 국가의 프로필 조회수 총합을 반환합니다:

```
    const groupUsers = await prisma.user.groupBy({
      by: ['country'],
      _sum: { profileViews: true },
    });
```

```
    [
      { country: 'Germany', _sum: { profileViews: 126 } },
      { country: 'Sweden', _sum: { profileViews: 0 } },
    ];
```

`by` 옵션에 요소가 하나만 있으면, 다음과 같은 축약 문법으로 쿼리를 표현할 수 있습니다:

```
    const groupUsers = await prisma.user.groupBy({
      by: 'country',
    });
```

- `groupBy()`와 필터링

`groupBy()`는 `where`와 `having`이라는 두 단계의 필터링을 지원합니다.

#

- `where`로 레코드 필터링

`where`를 사용해 **그룹화 전에** 모든 레코드를 필터링합니다. 다음 예시는 사용자를 국가별로 그룹화해 프로필 조회수를 합산하되, 이메일 주소에 `prisma.io`가 포함된 사용자만 포함합니다:

```
    const groupUsers = await prisma.user.groupBy({
      by: ['country'],
      where: {
        email: {
          contains: 'prisma.io',
        },
      },
      _sum: {
        profileViews: true,
      },
    });
```

#

- `having`으로 그룹 필터링

`having`을 사용하면 개별 레코드가 아니라, 필드 합계나 평균 같은 집계 값을 기준으로 **그룹 전체**를 필터링할 수 있습니다. 예: _평균_ `profileViews`가 100보다 큰 그룹만 반환:

```
    const groupUsers = await prisma.user.groupBy({
      by: ['country'],
      where: {
        email: {
          contains: 'prisma.io',
        },
      },
      _sum: { profileViews: true, },
      having: {
        profileViews: {
          _avg: {
            gt: 100,
          },
        },
      },
    });
```

#

- `having`의 사용 사례

`having`의 주요 사용 사례는 집계 결과에 대한 필터링입니다. 그룹화 _전_ 에 데이터셋 크기를 최대한 줄이기 위해 `where`를 사용하는 것을 권장합니다. 이렇게 하면 ✔ 데이터베이스가 반환해야 하는 레코드 수가 줄고 ✔ 인덱스를 활용할 수 있습니다.

예를 들어, 다음 쿼리는 스웨덴 또는 가나 출신이 _아닌_ 모든 사용자를 그룹화합니다:

```
    const fd = await prisma.user.groupBy({
      by: ['country'],
      where: {
        country: {
          notIn: ['Sweden', 'Ghana'],
        },
      },
      _sum: {
        profileViews: true,
      },
      having: {
        profileViews: {
          _min: {
            gte: 10,
          },
        },
      },
    });
```

다음 쿼리도 기술적으로 같은 결과를 내지만, 그룹화 _후_ 가나 사용자를 제외합니다. 이는 이점이 없으며 권장되지 않습니다.

```
    const groupUsers = await prisma.user.groupBy({
      by: ['country'],
      where: {
        country: {
          not: 'Sweden',
        },
      },
      _sum: {
        profileViews: true,
      },
      having: {
        country: {
          not: 'Ghana',
        },
        profileViews: {
          _min: {
            gte: 10,
          },
        },
      },
    });
```

> **참고** : `having` 내부에서는 집계 값 _또는_ `by`에서 사용 가능한 필드만 기준으로 필터링할 수 있습니다.

- `groupBy()`와 정렬

`groupBy()`와 `orderBy`를 함께 사용할 때는 다음 제약이 적용됩니다:

- `by`에 포함된 필드를 `orderBy`할 수 있습니다
- 집계 값으로 `orderBy`할 수 있습니다(2.21.0 이상에서 Preview)
- `groupBy()`와 함께 `skip` 및/또는 `take`를 사용한다면, 쿼리에 `orderBy`도 반드시 포함해야 합니다

#

- 집계 그룹 기준 정렬

**집계 그룹 기준으로 정렬**할 수 있습니다. 다음 예시는 각 `city` 그룹을 해당 그룹의 사용자 수로 정렬합니다(가장 큰 그룹이 먼저):

```
    const groupBy = await prisma.user.groupBy({
      by: ['city'],
      _count: {
        city: true,
      },
      orderBy: {
        _count: {
          city: 'desc',
        },
      },
    });
```

```
    [
      { city: 'Berlin', count: { city: 3 } },
      { city: 'Paris', count: { city: 2 } },
      { city: 'Amsterdam', count: { city: 1 } },
    ];
```

#

- 필드 기준 정렬

다음 쿼리는 그룹을 국가 기준으로 정렬하고, 처음 두 그룹을 건너뛴 뒤 3번째와 4번째 그룹을 반환합니다:

```
    const groupBy = await prisma.user.groupBy({
      by: ['country'],
      _sum: {
        profileViews: true,
      },
      orderBy: {
        country: 'desc',
      },
      skip: 2,
      take: 2,
    });
```

- `groupBy()` FAQ

#

- `groupBy()`와 함께 `select`를 사용할 수 있나요?

`groupBy()`와 함께 `select`는 사용할 수 없습니다. 하지만 `by`에 포함된 모든 필드는 자동으로 반환됩니다.

#

- `groupBy()`에서 `where`와 `having`의 차이는 무엇인가요?

`where`는 그룹화 전에 모든 레코드를 필터링하고, `having`은 그룹 전체를 필터링하며 해당 그룹의 특정 필드 평균 또는 합계 같은 집계 필드 값을 기준으로 필터링할 수 있습니다.

#

- `groupBy()`와 `distinct`의 차이는 무엇인가요?

`distinct`와 `groupBy()` 모두 하나 이상의 고유 필드 값으로 레코드를 그룹화합니다. `groupBy()`는 각 그룹 내 데이터 집계(예: 덴마크 게시물의 평균 조회수 반환)가 가능하지만, `distinct`는 그렇지 않습니다.

## Count

- 레코드 수 세기

[`count()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#count)를 사용해 레코드 수 또는 `null`이 아닌 필드 값의 개수를 셀 수 있습니다. 다음 예시 쿼리는 모든 사용자의 수를 계산합니다:

```
    const userCount = await prisma.user.count();
```

- 관계 수 세기

관계의 개수(예: 사용자 게시물 수)를 반환하려면, 다음과 같이 중첩된 `select`와 함께 `_count` 파라미터를 사용합니다:

```
    const usersWithCount = await prisma.user.findMany({
      include: {
        _count: {
          select: { posts: true },
        },
      },
    });
```

```
    { id: 1, _count: { posts: 3 } },
    { id: 2, _count: { posts: 2 } },
    { id: 3, _count: { posts: 2 } },
    { id: 4, _count: { posts: 0 } },
    { id: 5, _count: { posts: 0 } }
```

`_count` 파라미터는 다음과 같습니다:

- 최상위 `include` 또는 `select` 내부에서 사용 가능
- 레코드를 반환하는 모든 쿼리(`delete`, `update`, `findFirst` 포함)에서 사용 가능
- [여러 관계 수](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#return-multiple-relation-counts)를 반환 가능
- [관계 수 필터링](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#filter-the-relation-count) 가능(버전 4.3.0부터)

#

- `include`로 관계 수 반환

다음 쿼리는 결과에 각 사용자의 게시물 수를 포함합니다:

```
    const usersWithCount = await prisma.user.findMany({
      include: {
        _count: {
          select: { posts: true },
        },
      },
    });
```

```
    { id: 1, _count: { posts: 3 } },
    { id: 2, _count: { posts: 2 } },
    { id: 3, _count: { posts: 2 } },
    { id: 4, _count: { posts: 0 } },
    { id: 5, _count: { posts: 0 } }
```

#

- `select`로 관계 수 반환

다음 쿼리는 `select`를 사용해 각 사용자의 게시물 수만 반환하며, _다른 필드는 반환하지 않습니다_ :

```
    const usersWithCount = await prisma.user.findMany({
      select: {
        _count: {
          select: { posts: true },
        },
      },
    });
```

```
    {
      _count: {
        posts: 3;
      }
    }
```

#

- 여러 관계 수 반환

다음 쿼리는 각 사용자의 `posts`와 `recipes` 수를 반환하며 다른 필드는 반환하지 않습니다:

```
    const usersWithCount = await prisma.user.findMany({
      select: {
        _count: {
          select: {
            posts: true,
            recipes: true,
          },
        },
      },
    });
```

```
    {
      "_count": {
        "posts": 3,
        "recipes": 9
      }
    }
```

#

- 관계 수 필터링

`where`를 사용해 `_count` 출력 타입이 반환하는 필드를 필터링할 수 있습니다. 이는 [scalar fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields)와 [relation fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#relation-fields) 모두에 적용할 수 있습니다.

예를 들어, 다음 쿼리는 제목이 "Hello!"인 모든 사용자 게시물을 반환합니다:

```
    // Count all user posts with the title "Hello!"
    await prisma.user.findMany({
      select: {
        _count: {
          select: {
            posts: { where: { title: 'Hello!' } },
          },
        },
      },
    });
```

다음 쿼리는 작성자 이름이 "Alice"인 댓글이 있는 모든 사용자 게시물을 찾습니다:

```
    // Count all user posts that have comments
    // whose author is named "Alice"
    await prisma.user.findMany({
      select: {
        _count: {
          select: {
            posts: {
              where: { comments: { some: { author: { is: { name: 'Alice' } } } } },
            },
          },
        },
      },
    });
```

- `null`이 아닌 필드 값 세기

[2.15.0](https://github.com/prisma/prisma/releases/2.15.0) 이상에서는 모든 레코드 수뿐 아니라 `null`이 아닌 필드 값의 모든 인스턴스도 셀 수 있습니다. 다음 쿼리는 다음 개수를 반환합니다:

- 모든 `User` 레코드(`_all`)
- `null`이 아닌 모든 `name` 값(고유 값이 아니라, 단순히 `null`이 아닌 값)

```
    const userCount = await prisma.user.count({
      select: {
        _all: true, // Count all records
        name: true, // Count all non-null field values
      },
    });
```

```
    { "_all": 30, "name": 10 }
```

- 필터링된 count

`count`는 필터링을 지원합니다. 다음 예시 쿼리는 프로필 조회수가 100보다 큰 모든 사용자의 수를 계산합니다:

```
    const userCount = await prisma.user.count({
      where: {
        profileViews: {
          gte: 100,
        },
      },
    });
```

다음 예시 쿼리는 특정 사용자의 게시물 수를 계산합니다:

```
    const postCount = await prisma.post.count({
      where: {
        authorId: 29,
      },
    });
```

## 고유 값 선택

Prisma Client에서는 [`findMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#findmany) 쿼리 응답에서 중복 행을 걸러내기 위해 [`distinct`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#distinct)를 사용할 수 있습니다. `distinct`는 보통 [`select`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#select)와 함께 사용되어 테이블 행에서 특정 고유 값 조합을 식별합니다.

다음 예시는 `name` 필드 값이 고유한 모든 `User` 레코드의 모든 필드를 반환합니다:

```
    const result = await prisma.user.findMany({
      where: {},
      distinct: ['name'],
    });
```

다음 예시는 고유한 `role` 필드 값(예: `ADMIN`, `USER`)을 반환합니다:

```
    const distinctRoles = await prisma.user.findMany({
      distinct: ['role'],
      select: {
        role: true,
      },
    });
```

```
    [
      { role: 'USER', },
      { role: 'ADMIN', },
    ];
```

- `distinct` 내부 동작

Prisma Client의 `distinct` 옵션은 SQL `SELECT DISTINCT`를 사용하지 않습니다. 대신 `distinct`는 다음을 사용합니다:

- `SELECT` 쿼리
- 고유 값 선택을 위한 메모리 내 후처리

이렇게 설계된 이유는 `distinct` 쿼리에서 **`select`와 `include`를 지원**하기 위해서입니다.

다음 예시는 `gameId`와 `playerId`에 대해 distinct를 적용하고 `score`로 정렬하여, **게임별 각 플레이어의 최고 점수**를 반환합니다. 이 쿼리는 추가 데이터를 포함하기 위해 `include`와 `select`를 사용합니다:

- `score` 선택(`Play`의 필드)
- 관련 플레이어 이름 선택(`Play`와 `User` 간 관계)
- 관련 게임 이름 선택(`Play`와 `Game` 간 관계)

샘플 스키마 펼치기

schema.prisma

```
    model User {
      id   Int     @id @default(autoincrement())
      name String?
      play Play[]
    }

    model Game {
      id   Int     @id @default(autoincrement())
      name String?
      play Play[]
    }

    model Play {
      id       Int   @id @default(autoincrement())
      score    Int?  @default(0)
      playerId Int?
      player   User? @relation(fields: [playerId], references: [id])
      gameId   Int?
      game     Game? @relation(fields: [gameId], references: [id])
    }
```

```
    const distinctScores = await prisma.play.findMany({
      distinct: ['playerId', 'gameId'],
      orderBy: {
        score: 'desc',
      },
      select: {
        score: true,
        game: {
          select: {
            name: true,
          },
        },
        player: {
          select: {
            name: true,
          },
        },
      },
    });
```

```
    [
      {
        "score": 900,
        "game": { "name": "Pacman" },
        "player": { "name": "Bert Bobberton" }
      },
      {
        "score": 400,
        "game": { "name": "Pacman" },
        "player": { "name": "Nellie Bobberton" }
      }
    ]
```

`select`와 `distinct`가 없으면, 쿼리는 다음을 반환합니다:

```
    [
      {
        "gameId": 2,
        "playerId": 5
      },
      {
        "gameId": 2,
        "playerId": 10
      }
    ]
```
