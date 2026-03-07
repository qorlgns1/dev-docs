---
title: "SQL 주석"
description: "관측성, 디버깅, 추적 기능을 향상하기 위해 SQL 쿼리에 주석 형태로 메타데이터를 추가합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/sql-comments

# SQL 주석

관측성, 디버깅, 추적 기능을 향상하기 위해 SQL 쿼리에 주석 형태로 메타데이터를 추가합니다.

SQL 주석을 사용하면 데이터베이스 쿼리에 메타데이터를 덧붙일 수 있어, 쿼리를 애플리케이션 컨텍스트와 더 쉽게 연관 지을 수 있습니다. Prisma ORM은 Google에서 개발한 [sqlcommenter 형식](https://google.github.io/sqlcommenter/)을 지원하며, 이 형식은 다양한 데이터베이스 모니터링 도구에서 널리 지원됩니다.

SQL 주석은 다음과 같은 경우에 유용합니다.

- **Observability** : `traceparent`를 사용해 데이터베이스 쿼리를 애플리케이션 트레이스와 연관
- **Query insights** : 데이터베이스 모니터링 도구에서 분석할 수 있도록 쿼리에 메타데이터 태그 추가
- **Debugging** : 문제 해결을 쉽게 하기 위해 쿼리에 사용자 정의 컨텍스트 추가

## 설치

사용 사례에 따라 하나 이상의 퍼스트 파티 플러그인을 설치하세요.

npm

pnpm

yarn

bun

```
    npm install @prisma/sqlcommenter-query-tags
    npm install @prisma/sqlcommenter-trace-context
```

자체 플러그인을 만들기 위해 코어 SQL commenter types 패키지를 설치하세요.

npm

pnpm

yarn

bun

```
    npm install @prisma/sqlcommenter
```

## 기본 사용법

`PrismaClient` 인스턴스를 생성할 때 `comments` 옵션에 SQL commenter 플러그인 배열을 전달하세요.

```
    import { PrismaClient } from "../prisma/generated/client";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { queryTags } from "@prisma/sqlcommenter-query-tags";
    import { traceContext } from "@prisma/sqlcommenter-trace-context";

    const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL });

    const prisma = new PrismaClient({
      adapter,
      comments: [queryTags(), traceContext()],
    });
```

이 구성을 사용하면 SQL 쿼리에 주석 형태의 메타데이터가 포함됩니다.

```
    SELECT "id", "name" FROM "User" /*application='my-app',traceparent='00-abc123...-01'*/
```

## 공식 플러그인

Prisma는 공식 SQL commenter 플러그인 두 가지를 제공합니다.

- Query tags

`@prisma/sqlcommenter-query-tags` 패키지를 사용하면 `AsyncLocalStorage`를 이용한 비동기 컨텍스트 내에서 쿼리에 임의의 태그를 추가할 수 있습니다.

```
    import { queryTags, withQueryTags } from "@prisma/sqlcommenter-query-tags";
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({
      adapter,
      comments: [queryTags()],
    });

    // Wrap your queries to add tags
    const users = await withQueryTags({ route: "/api/users", requestId: "abc-123" }, () =>
      prisma.user.findMany(),
    );
```

결과 SQL에는 태그가 주석으로 포함됩니다.

```
    SELECT ... FROM "User" /*requestId='abc-123',route='/api/users'*/
```

#

- Multiple queries in one scope

콜백 내부의 모든 쿼리는 동일한 태그를 공유합니다.

```
    const result = await withQueryTags({ traceId: "trace-456" }, async () => {
      const users = await prisma.user.findMany();
      const posts = await prisma.post.findMany();
      return { users, posts };
    });
```

#

- Nested scopes with tag replacement

기본적으로 중첩된 `withQueryTags` 호출은 바깥쪽 태그를 완전히 대체합니다.

```
    await withQueryTags({ requestId: "req-123" }, async () => {
      // Queries here have: requestId='req-123'

      await withQueryTags({ userId: "user-456" }, async () => {
        // Queries here only have: userId='user-456'
        // requestId is NOT included
        await prisma.user.findMany();
      });
    });
```

#

- Nested scopes with tag merging

`withMergedQueryTags`를 사용해 바깥쪽 스코프와 태그를 병합하세요.

```
    import { withQueryTags, withMergedQueryTags } from "@prisma/sqlcommenter-query-tags";

    await withQueryTags({ requestId: "req-123", source: "api" }, async () => {
      await withMergedQueryTags({ userId: "user-456", source: "handler" }, async () => {
        // Queries here have: requestId='req-123', userId='user-456', source='handler'
        await prisma.user.findMany();
      });
    });
```

중첩 스코프에서 태그 값을 `undefined`로 설정해 태그를 제거할 수도 있습니다.

```
    await withQueryTags({ requestId: "req-123", debug: "true" }, async () => {
      await withMergedQueryTags({ userId: "user-456", debug: undefined }, async () => {
        // Queries here have: requestId='req-123', userId='user-456'
        // debug is removed
        await prisma.user.findMany();
      });
    });
```

- Trace context

`@prisma/sqlcommenter-trace-context` 패키지는 쿼리에 W3C Trace Context(`traceparent`) 헤더를 추가하여, 분산 트레이스와 데이터베이스 쿼리를 연관 지을 수 있게 합니다.

```
    import { traceContext } from "@prisma/sqlcommenter-trace-context";
    import { PrismaClient } from "../prisma/generated/client";

    const prisma = new PrismaClient({
      adapter,
      comments: [traceContext()],
    });
```

추적이 활성화되어 있고 현재 span이 샘플링된 경우, 쿼리에 `traceparent`가 포함됩니다.

```
    SELECT * FROM "User" /*traceparent='00-0af7651916cd43dd8448eb211c80319c-b9c7c989f97918e1-01'*/
```

trace context 플러그인을 사용하려면 [`@prisma/instrumentation`](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing) 구성이 필요합니다. `traceparent`는 추적이 활성 상태이고 span이 샘플링된 경우에만 추가됩니다.

`traceparent` 헤더는 [W3C Trace Context](https://www.w3.org/TR/trace-context/) 명세를 따릅니다.

```
    {version}-{trace-id}-{parent-id}-{trace-flags}
```

구성 요소는 다음과 같습니다.

- `version`: 현재 명세에서는 항상 `00`
- `trace-id`: 트레이스 ID를 나타내는 32자리 16진수 문자열
- `parent-id`: 부모 span ID를 나타내는 16자리 16진수 문자열
- `trace-flags`: 2자리 16진수 문자열, `01`은 샘플링됨을 의미

## 사용자 정의 플러그인 만들기

쿼리에 사용자 정의 메타데이터를 추가하기 위해 자체 SQL commenter 플러그인을 만들 수 있습니다.

- Plugin structure

SQL commenter 플러그인은 쿼리 컨텍스트를 받아 key-value 쌍을 반환하는 함수입니다.

```
    import type { SqlCommenterPlugin, SqlCommenterContext } from "@prisma/sqlcommenter";

    const myPlugin: SqlCommenterPlugin = (context: SqlCommenterContext) => {
      return {
        application: "my-app",
        version: "1.0.0",
      };
    };
```

- Using custom plugins

`comments` 옵션에 사용자 정의 플러그인을 전달하세요.

```
    const prisma = new PrismaClient({
      adapter,
      comments: [myPlugin],
    });
```

- Conditional keys

주석에서 제외하고 싶은 키는 `undefined`를 반환하세요. `undefined` 값을 가진 키는 자동으로 필터링됩니다.

```
    const conditionalPlugin: SqlCommenterPlugin = (context) => ({
      model: context.query.modelName, // undefined for raw queries, automatically omitted
      action: context.query.action,
    });
```

- Query context

플러그인은 쿼리 정보가 담긴 `SqlCommenterContext` 객체를 받습니다.

```
    interface SqlCommenterContext {
      query: SqlCommenterQueryInfo;
      sql?: string;
    }
```

`query` 속성은 Prisma operation에 대한 정보를 제공합니다.

| Property    | Type                                                   | Description                                                     |
| ----------- | ------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------- |
| `type`      | `'single'`                                             | `'compacted'`                                                   | 단일 쿼리인지 배치 쿼리인지 여부                         |
| `modelName` | `string`                                               | `undefined`                                                     | 조회 중인 모델(예: `"User"`). raw query에서는 undefined. |
| `action`    | `string`                                               | Prisma operation(예: `"findMany"`, `"createOne"`, `"queryRaw"`) |
| `query`     | `unknown` (single) or `queries: unknown[]` (compacted) | 전체 쿼리 객체. 구조는 공개 API의 일부가 아닙니다.              |

`sql` 속성은 이 Prisma 쿼리에서 생성된 raw SQL 쿼리입니다. `PrismaClient`가 데이터베이스에 연결되어 SQL 쿼리를 직접 렌더링하는 경우 항상 사용할 수 있습니다. Prisma Accelerate를 사용하는 경우 SQL 렌더링은 Accelerate 측에서 수행되므로, `PrismaClient` 측에서 SQL commenter 플러그인이 실행될 때 raw SQL 문자열을 사용할 수 없습니다.

#

- Single vs. compacted queries
  - **Single queries** (`type: 'single'`): 단일 Prisma 쿼리가 실행됨
  - **Compacted queries** (`type: 'compacted'`): 여러 쿼리가 하나의 SQL 문으로 배치됨(예: 자동 `findUnique` 배칭)

- Example: Application metadata

```
    import type { SqlCommenterPlugin } from "@prisma/sqlcommenter";

    const applicationTags: SqlCommenterPlugin = (context) => ({
      application: "my-service",
      environment: process.env.NODE_ENV ?? "development",
      operation: context.query.action,
      model: context.query.modelName,
    });
```

- Example: Async context propagation

애플리케이션 전반에 컨텍스트를 전파하려면 `AsyncLocalStorage`를 사용하세요.

```
    import { AsyncLocalStorage } from "node:async_hooks";
    import type { SqlCommenterPlugin } from "@prisma/sqlcommenter";

    interface RequestContext {
      route: string;
      userId?: string;
    }

    const requestStorage = new AsyncLocalStorage<RequestContext>();

    const requestContextPlugin: SqlCommenterPlugin = () => {
      const context = requestStorage.getStore();
      return {
        route: context?.route,
        userId: context?.userId,
      };
    };

    // Usage in a request handler
    requestStorage.run({ route: "/api/users", userId: "user-123" }, async () => {
      await prisma.user.findMany();
    });
```

- Combining multiple plugins

플러그인은 배열 순서대로 호출되며, 출력은 병합됩니다. 뒤에 오는 플러그인은 앞선 플러그인의 키를 덮어쓸 수 있습니다.

```
    import type { SqlCommenterPlugin } from "@prisma/sqlcommenter";
    import { queryTags } from "@prisma/sqlcommenter-query-tags";
    import { traceContext } from "@prisma/sqlcommenter-trace-context";

    const appPlugin: SqlCommenterPlugin = () => ({
      application: "my-app",
      version: "1.0.0",
    });

    const prisma = new PrismaClient({
      adapter,
      comments: [appPlugin, queryTags(), traceContext()],
    });
```

## 프레임워크 통합

- Hono

Hono의 middleware는 downstream handler를 올바르게 await합니다.

```
    import { createMiddleware } from "hono/factory";
    import { withQueryTags } from "@prisma/sqlcommenter-query-tags";

    app.use(
      createMiddleware(async (c, next) => {
        await withQueryTags(
          {
            route: c.req.path,
            method: c.req.method,
            requestId: c.req.header("x-request-id") ?? crypto.randomUUID(),
          },
          () => next(),
        );
      }),
    );
```

- Koa

Koa의 middleware는 downstream handler를 올바르게 await합니다.

```
    import { withQueryTags } from "@prisma/sqlcommenter-query-tags";

    app.use(async (ctx, next) => {
      await withQueryTags(
        {
          route: ctx.path,
          method: ctx.method,
          requestId: ctx.get("x-request-id") || crypto.randomUUID(),
        },
        () => next(),
      );
    });
```

- Fastify

개별 route handler를 감싸세요.

```
    import { withQueryTags } from "@prisma/sqlcommenter-query-tags";

    fastify.get("/users", (request, reply) => {
      return withQueryTags(
        {
          route: "/users",
          method: "GET",
          requestId: request.id,
        },
        () => prisma.user.findMany(),
      );
    });
```

- Express

Express middleware는 callback을 사용하므로, route handler를 직접 감싸세요.

```
    import { withQueryTags } from "@prisma/sqlcommenter-query-tags";

    app.get("/users", (req, res, next) => {
      withQueryTags(
        {
          route: req.path,
          method: req.method,
          requestId: req.header("x-request-id") ?? crypto.randomUUID(),
        },
        () => prisma.user.findMany(),
      )
        .then((users) => res.json(users))
        .catch(next);
    });
```

- NestJS

handler 실행을 감싸기 위해 interceptor를 사용하세요.

```
    import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from "@nestjs/common";
    import { Observable, from, lastValueFrom } from "rxjs";
    import { withQueryTags } from "@prisma/sqlcommenter-query-tags";

    @Injectable()
    export class QueryTagsInterceptor implements NestInterceptor {
      intercept(context: ExecutionContext, next: CallHandler): Observable<unknown> {
        const request = context.switchToHttp().getRequest<Request>();
        return from(
          withQueryTags(
            {
              route: request.url,
              method: request.method,
              requestId: request.headers.get("x-request-id") ?? crypto.randomUUID(),
            },
            () => lastValueFrom(next.handle()),
          ),
        );
      }
    }

    // Apply globally in main.ts
    app.useGlobalInterceptors(new QueryTagsInterceptor());
```

## 출력 형식

플러그인 출력은 병합되고, 키 기준 알파벳순 정렬되며, URL 인코딩된 뒤 [sqlcommenter specification](https://google.github.io/sqlcommenter/spec/)에 따라 포맷됩니다.

```
    SELECT "id", "name" FROM "User" /*application='my-app',environment='production',model='User'*/
```

주요 동작:

- 플러그인은 배열 순서대로 동기적으로 호출됨
- 동일한 키를 반환하면 뒤에 오는 플러그인이 앞선 플러그인을 덮어씀
- `undefined` 값을 가진 키는 필터링됨(앞선 플러그인이 설정한 키를 제거하지는 않음)
- 키와 값은 sqlcommenter spec에 따라 URL 인코딩됨
- 값 내 작은따옴표는 `\'`로 이스케이프됨
- 주석은 SQL 쿼리 끝에 추가됨

## API 레퍼런스

- `SqlCommenterTags`

```
    type SqlCommenterTags = { readonly [key: string]: string | undefined };
```

SQL 주석으로 추가할 key-value 쌍입니다. `undefined` 값을 가진 키는 자동으로 필터링됩니다.

- `SqlCommenterPlugin`

```
    interface SqlCommenterPlugin {
      (context: SqlCommenterContext): SqlCommenterTags;
    }
```

쿼리 컨텍스트를 받아 key-value 쌍을 반환하는 함수입니다. 특정 쿼리에 주석을 추가하지 않으려면 빈 객체를 반환하세요.

- `SqlCommenterContext`

```
    interface SqlCommenterContext {
      query: SqlCommenterQueryInfo;
      sql?: string;
    }
```

쿼리 정보가 담긴, 플러그인에 제공되는 컨텍스트입니다.

- **`query`** : 실행 중인 Prisma 쿼리에 대한 정보. [`SqlCommenterQueryInfo`](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/sql-comments#sqlcommenterqueryinfo) 참고.
- **`sql`** : 실행 중인 SQL 쿼리. driver adapter 사용 시에만 제공되며 Accelerate 사용 시에는 제공되지 않습니다.

* `SqlCommenterQueryInfo`

```
    type SqlCommenterQueryInfo =
      | ({ type: "single" } & SqlCommenterSingleQueryInfo)
      | ({ type: "compacted" } & SqlCommenterCompactedQueryInfo);
```

실행 중인 쿼리(또는 여러 쿼리)에 대한 정보입니다.

- `SqlCommenterSingleQueryInfo`

```
    interface SqlCommenterSingleQueryInfo {
      modelName?: string;
      action: string;
      query: unknown;
    }
```

단일 Prisma 쿼리에 대한 정보입니다.

- `SqlCommenterCompactedQueryInfo`

```
    interface SqlCommenterCompactedQueryInfo {
      modelName?: string;
      action: string;
      queries: unknown[];
    }
```

컴팩트된 배치 쿼리에 대한 정보입니다.
