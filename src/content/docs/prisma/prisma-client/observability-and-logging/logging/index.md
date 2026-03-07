---
title: "stdout으로 로깅"
description: "Prisma Client가 데이터베이스로 전송하는 원시 SQL 쿼리와 기타 정보를 로깅하도록 구성하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/logging

# 로깅

Prisma Client가 데이터베이스로 전송하는 원시 SQL 쿼리와 기타 정보를 로깅하도록 구성하는 방법을 알아보세요.

`PrismaClient` [`log`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#log) 매개변수를 사용해 경고, 오류, 데이터베이스로 전송된 쿼리 정보 등을 포함한 [로그 레벨](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#log-levels)을 구성할 수 있습니다.

Prisma Client는 두 가지 유형의 로깅을 지원합니다.

- [stdout](https://en.wikipedia.org/wiki/Standard_streams)으로 로깅(기본값)
- 이벤트 기반 로깅([`$on()`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#on) 메서드를 사용해 [이벤트 구독](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/logging#event-based-logging))

또한 `DEBUG` 환경 변수를 사용해 Prisma Client에서 디버깅 출력을 활성화할 수 있습니다. 자세한 내용은 [Debugging](https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging)을 참고하세요.

개별 작업 수준에서 Prisma Client 성능을 더 자세히 파악하려면 [Tracing](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing)을 참고하세요.

## stdout으로 로깅

모든 로그 레벨을 stdout에 출력하는 가장 간단한 방법은 `LogLevel` 객체 배열을 전달하는 것입니다.

```
    const prisma = new PrismaClient({
      log: ["query", "info", "warn", "error"],
    });
```

이는 `emit` 값이 항상 `stdout`인 `LogDefinition` 객체 배열을 전달하는 방식의 축약형입니다.

```
    const prisma = new PrismaClient({
      log: [
        {
          emit: "stdout",
          level: "query",
        },
        {
          emit: "stdout",
          level: "error",
        },
        {
          emit: "stdout",
          level: "info",
        },
        {
          emit: "stdout",
          level: "warn",
        },
      ],
    });
```

## 이벤트 기반 로깅

이벤트 기반 로깅을 사용하려면 다음을 수행하세요.

1. query 같은 특정 로그 레벨에 대해 `emit`을 `event`로 설정합니다.
2. `$on()` 메서드를 사용해 이벤트를 구독합니다.

다음 예시는 모든 `query` 이벤트를 구독하고 `duration` 및 `query`를 콘솔에 출력합니다.

관계형 데이터베이스

```
    const prisma = new PrismaClient({
      log: [
        {
          emit: "event",
          level: "query",
        },
        {
          emit: "stdout",
          level: "error",
        },
        {
          emit: "stdout",
          level: "info",
        },
        {
          emit: "stdout",
          level: "warn",
        },
      ],
    });

    prisma.$on("query", (e) => {
      console.log("Query: " + e.query);
      console.log("Params: " + e.params);
      console.log("Duration: " + e.duration + "ms");
    });
```

```
    Query: SELECT "public"."User"."id", "public"."User"."email", "public"."User"."name" FROM "public"."User" WHERE 1=1 OFFSET $1
    Params: [0]
    Duration: 3ms
    Query: SELECT "public"."Post"."id", "public"."Post"."title", "public"."Post"."authorId" FROM "public"."Post" WHERE "public"."Post"."authorId" IN ($1,$2,$3,$4) OFFSET $5
    Params: [2, 7, 18, 29]
    Duration: 2ms
```

MongoDB

```
    const prisma = new PrismaClient({
      log: [
        {
          emit: "event",
          level: "query",
        },
        {
          emit: "stdout",
          level: "error",
        },
        {
          emit: "stdout",
          level: "info",
        },
        {
          emit: "stdout",
          level: "warn",
        },
      ],
    });

    prisma.$on("query", (e) => {
      console.log("Query: " + e.query);
    });
```

```
    Query: db.User.aggregate([ { $project: { _id: 1, email: 1, name: 1, }, }, ])
    Query: db.Post.aggregate([ { $match: { userId: { $in: [ "622f0bbbdf635a42016ee325", ], }, }, }, { $project: { _id: 1, slug: 1, title: 1, body: 1, userId: 1, }, }, ])
```

정확한 [이벤트(`e`) 타입과 사용 가능한 속성](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#event-types)은 로그 레벨에 따라 달라집니다.
