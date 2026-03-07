---
title: "Drizzle"
description: "Prisma ORM이 Drizzle과 어떻게 다른지 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-drizzle

# Drizzle

Prisma ORM이 Drizzle과 어떻게 다른지 알아보세요

Prisma와 Drizzle은 데이터베이스를 다루는 방식에서 서로 다른 접근법을 취합니다. Drizzle은 SQL에 가깝게 쿼리를 작성하길 선호하는 개발자에게 매력적이며, Prisma는 명확성, 협업, 장기 유지보수성이 중요한 프로덕션 애플리케이션을 구축하고 운영하는 팀을 지원하도록 설계되었습니다.

두 라이브러리 모두 유사한 문제를 해결하지만, 작동 방식은 매우 다르며 각각 장단점이 있습니다. 어떤 것을 선택할지는 프로젝트의 요구사항과 중요하게 여기는 구체적인 트레이드오프에 따라 달라집니다.

## Drizzle vs Prisma ORM

**Drizzle**은 JavaScript/TypeScript 함수로 SQL 쿼리를 조합할 수 있게 해주는 전통적인 SQL 쿼리 빌더입니다. 데이터베이스 조회나 마이그레이션 실행에 사용할 수 있습니다. Drizzle은 SQL보다 한 단계 높은 추상화를 제공하는 Queries API도 제공하며, 중첩된 relation 조회에 사용할 수 있습니다. Drizzle 스키마는 TypeScript 파일에 정의되며, 이 정의를 기반으로 SQL 마이그레이션을 생성한 뒤 데이터베이스에 실행합니다.

**Prisma ORM**은 비대해진 모델 인스턴스, 비즈니스 로직과 저장소 로직의 혼합, 타입 안전성 부족, lazy loading 등으로 인한 예측 불가능한 쿼리 같은 전통적 ORM의 여러 문제를 완화합니다. [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 사용해 애플리케이션 모델을 선언적으로 정의합니다. 이후 Prisma Migrate가 Prisma schema로부터 SQL 마이그레이션을 생성해 데이터베이스에 실행합니다. CRUD 쿼리는 Node.js와 TypeScript를 위한 가볍고 완전한 타입 안전성을 갖춘 데이터베이스 클라이언트인 Prisma Client에서 제공합니다.

## Prisma: Built for Teams

Prisma는 팀이 더 빠르게 배포할 수 있도록 설계되었습니다. 특히 팀원 모두가 SQL 전문가가 아닌 경우에 더 효과적입니다.

- **SQL 병목 없음** : Prisma를 사용하면 높은 수준의 SQL 지식이 없어도 생산적으로 작업할 수 있습니다. 원시 쿼리 작성이나 데이터베이스 로직 디버깅을 특정 개인에게 의존하지 않고도 팀 전체가 백엔드 코드에 기여할 수 있습니다.
- **공유된 멘탈 모델** : Prisma의 schema는 사람이 읽기 쉽고 이해하기 쉽습니다. 애플리케이션 데이터 모델에 대해 일관된 단일 관점을 제공합니다.
- **더 쉬운 코드 리뷰** : schema 변경과 데이터 접근 패턴이 투명하고 일관되어, 리뷰어가 백엔드 변경사항을 이해하고 승인하기 쉬워집니다.
- **예측 가능한 워크플로** : Prisma는 마이그레이션 생성, 클라이언트 타이핑, 쿼리 구성을 자동화하므로 팀이 이를 수동으로 처리할 필요가 없습니다.

Drizzle은 SQL을 잘 알거나 배우기를 선호하는 1인 개발자에게는 훌륭할 수 있습니다. 하지만 팀 단위가 되면 Prisma는 속도를 늦추는 마찰과 지식 의존 리스크를 줄여줍니다.

## Type safety

Drizzle은 _완전한_ 타입 안전성을 제공하지는 않습니다. 서드파티가 수행한 이 [비교 연구](https://github.com/thetutlage/meta/discussions/8)의 인용문처럼, "Drizzle gives the impression of type-safety. However, only the query results have type information. You can write invalid queries with Drizzle."

Prisma는 생성된 타입 덕분에 _완전한_ 타입 안전성을 제공합니다. 즉, 코드 작성과 팀 협업 시 오류 가능성을 줄일 수 있습니다.

## Prisma Schema as a Single Source of Truth

Prisma에서는 데이터 모델이 단일 파일 `schema.prisma`에 존재합니다.

- **명시적임** : 타입을 추론하거나 SQL 생성 함수를 해독할 필요 없이 schema가 바로 보입니다.
- **가독성이 높음** : 비기술 직군 팀원도 모델과 관계를 이해할 수 있습니다.
- **모든 것의 기반** : 마이그레이션, TypeScript 타입, 자동완성, ERD 생성 등 모든 것이 schema에서 시작됩니다.

반면 Drizzle의 schema는 TypeScript 코드로 구성되므로 전체 데이터 모델을 한눈에 파악하기 어렵고, 인지 부담을 높이며, 코드베이스 전반에서 모델 정의 방식의 불일치를 초래할 수 있습니다. Prisma가 PSL (Prisma Schema Language)에 확신을 갖는 이유는 [여기](https://www.prisma.io/blog/prisma-schema-language-the-best-way-to-define-your-data)에서 더 읽어보세요.

schema를 ERD로 보고 싶나요? Prisma에서는 한 줄 명령이면 됩니다: `npx prisma generate && npx prisma-erd-generator`

## API design & Level of abstraction

Drizzle과 Prisma ORM은 서로 다른 추상화 수준에서 동작합니다. Drizzle의 철학은 "If you know SQL, you know Drizzle ORM"입니다. API가 SQL을 반영하는 반면, Prisma Client는 애플리케이션 개발자의 일반적인 작업을 염두에 두고 설계된 더 높은 수준의 추상화를 제공합니다. Prisma ORM의 API 설계는 [making the right thing easy](https://jason.energy/right-thing-easy-thing/)라는 아이디어에 크게 기댑니다.

Prisma Client는 더 높은 추상화 수준에서 동작하지만, 언제든 [raw SQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql)로 내려갈 수 있습니다. 다만 Prisma ORM을 온전히 활용해 애플리케이션을 개발하는 데 SQL 지식이 필수는 아닙니다. Prisma ORM의 목표는 개발자 경험과 생산성에 초점을 맞추면서도 개발자에게 익숙하게 느껴지는 쿼리 문법을 구성하는 것입니다. 자세한 내용은 [Why Prisma](https://docs.prisma.io/docs/orm#why-prisma-orm)에서 확인할 수 있습니다.

Prisma Client API로 표현하기 어려운 일부 쿼리를 위해 Prisma ORM은 `.sql` 파일을 직접 활용해 더 익숙하고 타입 안전한 경험을 제공하는 [TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql)도 제공합니다. 기존 SQL 도구와 워크플로를 Prisma Client와 함께 사용해 원하는 어떤 수준의 추상화도 처리할 수 있습니다.

Prisma ORM에서는 TypedSQL로 완전한 타입 지정 SQL 쿼리를 사용할 수 있지만, 아래 섹션에서는 Prisma와 Drizzle API가 어떻게 다른지, 그리고 이 경우 Prisma ORM API 설계의 근거가 무엇인지 몇 가지 예시를 통해 살펴봅니다.

- Data modeling

Prisma 모델은 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에 정의되며, Drizzle은 테이블 정의에 TypeScript 함수를 사용합니다. 이 함수들은 export되어 쿼리에서 사용됩니다.

Prisma는 DataMapper ORM 패턴을 따르며, Prisma schema에 정의된 모델의 데이터를 읽고 쓰기 위한 맞춤형의 완전한 타입 안전 API를 노출하는 경량 데이터베이스 클라이언트를 생성합니다.

Prisma ORM의 데이터 모델링 DSL은 간결하고 단순하며 직관적입니다. VS Code에서 데이터를 모델링할 때 자동완성, quick fix, 정의로 이동 등 개발자 생산성을 높이는 기능을 갖춘 강력한 [VS Code extension](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)도 활용할 수 있습니다. 반면 Drizzle은 TypeScript를 사용하므로 (예: 코드 재사용을 통해) TypeScript의 강력함을 활용해 추가 유연성을 얻을 수 있습니다.

```
    model User {
      id    Int     @id @default(autoincrement())
      name  String?
      email String  @unique
      posts Post[]
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      content   String?
      published Boolean @default(false)
      authorId  Int?
      author    User?   @relation(fields: [authorId], references: [id])
    }
```

```
    import { boolean, integer, pgTable, serial, text, uniqueIndex, varchar } from "drizzle-orm/pg-core";

    export const users = pgTable("users", {
      id: serial("id").primaryKey(),
      name: varchar("name", { length: 256 }),
      email: varchar("email", { length: 256 }).unique(),
    });

    export const posts = pgTable("posts", {
      id: serial("id").primaryKey(),
      title: varchar("title", { length: 256 }).notNull(),
      content: text("content"),
      published: boolean("published"),
      authorId: integer("author_id").references(() => users.id),
    });
```

- Migrations

마이그레이션은 Drizzle과 Prisma ORM에서 유사하게 동작합니다. 두 도구 모두 제공된 모델 정의를 기반으로 SQL 파일을 생성하고, 이를 데이터베이스에 실행하는 CLI를 제공합니다. 마이그레이션 실행 전 SQL 파일을 수정할 수 있으므로 어떤 사용자 지정 데이터베이스 작업이든 두 마이그레이션 시스템에서 수행할 수 있습니다.

- Querying

기본 쿼리는 Drizzle과 Prisma ORM 모두에서 자연스럽게 구성할 수 있습니다. Drizzle의 Queries API를 사용하면 두 접근 방식은 매우 유사합니다.

```
    // find all users
    const allUsers = await prisma.user.findMany();

    // find a single user
    const user = await prisma.user.findFirst({
      where: { id: 27 },
    });

    // find a unique user
    const user = await prisma.user.findUnique({
      where: { email: "nilu@prisma.io" },
    });
```

```
    import { eq } from "drizzle-orm";

    // find all users
    const allUsers = await db.query.users.findMany();

    // find a single user
    const user = await db.query.users.findFirst({
      where: eq(users.id, 1),
    });

    // find a unique post
    const user = await db.query.users.findFirst({
      where: eq(users.email, "nilu@prisma.io"),
    });
```

mutation(`create`, `update`, `delete`)을 수행할 때는 Drizzle Queries API를 사용할 수 없습니다. 이 경우 Drizzle의 SQL 유사 API를 사용해야 합니다.

```
    // create a user
    const user = await prisma.user.create({
      data: {
        name: "Nilu",
        email: "nilu@prisma.io",
      },
    });

    // update a user
    const user = await prisma.user.update({
      where: { email: "nilu@prisma.io" },
      data: { name: "Another Nilu" },
    });

    // delete a user
    const deletedUser = await prisma.user.delete({
      where: { email: "nilu@prisma.io" },
    });
```

```
    // create a user
    const user = await db.insert(users).values({
      name: "Nilu",
      email: "nilu@prisma.io",
    });

    // update a user
    const user = await db
      .update(users)
      .set({ name: "Another Nilu" })
      .where(eq(users.email, "nilu@prisma.io"))
      .returning();

    // delete a user
    const deletedUser = await db.delete(users).where(eq(users.email, "nilu@prisma.io")).returning();
```

- Relations

외래 키로 연결된 레코드를 다루는 일은 SQL에서 매우 복잡해질 수 있습니다. Prisma ORM의 [virtual relation field](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields) 개념은 애플리케이션 개발자가 연관 데이터를 직관적이고 편리하게 다룰 수 있게 해줍니다. Prisma ORM 접근 방식의 몇 가지 장점은 다음과 같습니다.

- fluent API를 통한 관계 탐색 ([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#fluent-api))
- 연결된 레코드의 업데이트/생성을 가능하게 하는 중첩 쓰기 ([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes))
- 연관 레코드에 대한 필터 적용 ([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-filters))
- 내부 SQL을 신경 쓰지 않고 중첩 데이터를 쉽고 타입 안전하게 조회 ([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads))
- 모델과 관계를 기반으로 중첩 TypeScript 타이핑 생성 ([docs](https://docs.prisma.io/docs/orm/prisma-client/type-safety))
- relation field를 통한 데이터 모델 내 직관적인 관계 모델링 ([docs](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations))
- relation table(때로 JOIN, link, pivot, junction table이라고도 함)의 암묵적 처리 ([docs](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations))

```
    const posts = await prisma.post.findMany({
      include: {
        author: true,
      },
    });
```

```
    const posts = await db.query.posts.findMany({
      with: {
        author: true,
      },
    });
```

- Filtering

Drizzle은 특정 SQL dialect의 기본 필터 및 조건 연산자를 노출합니다. 반면 Prisma ORM은 더 직관적으로 사용할 수 있는 [generic set of operators](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#combining-operators)를 제공합니다.

Drizzle과 Prisma ORM의 필터링 API 차이를 보여주는 좋은 예는 `string` 필터입니다. Drizzle은 `like`, `ilike` 필터를 제공하는 반면 Prisma ORM은 개발자가 사용할 수 있는 보다 구체적인 연산자(예: `contains`, `startsWith`, `endsWith`)를 제공합니다.

```
    // case sensitive filter
    const posts = await prisma.post.findMany({
      where: {
        title: "Hello World",
      },
    });

    // case insensitive filter
    const posts = await prisma.post.findMany({
      where: {
        title: "Hello World",
        mode: "insensitive",
      },
    });
```

```
    // case sensitive filter
    const posts = await db.select().from(posts).where(like(posts.title, "Hello World"));

    // case insensitive filter
    const posts = await db.select().from(posts).where(ilike(posts.title, "Hello World"));
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: {
          contains: "Hello World",
        },
      },
    });
```

```
    const posts = await db.select().from(posts).where(ilike(posts.title, "%Hello World%"));
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: {
          startsWith: "Hello World",
        },
      },
    });
```

```
    const posts = await db.select().from(posts).where(ilike(posts.title, "Hello World%"));
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: {
          endsWith: "Hello World",
        },
      },
    });
```

```
    const posts = await db.select().from(posts).where(ilike(posts.title, "%Hello World"));
```

- Observability

Drizzle과 Prisma ORM 모두 쿼리 및 생성된 내부 SQL을 로깅할 수 있습니다.

이 제품들은 [Data DX](https://www.datadx.io/) 원칙을 따라 데이터 기반 애플리케이션을 쉽게 구축할 수 있도록 Prisma ORM과 함께 동작하며, 포괄적인 데이터 툴링을 제공합니다.

## Safer Changes and Fewer Bugs

Prisma는 데이터베이스 작업 시 사람의 실수로 인한 위험을 최소화합니다.

- **필드 이름을 바꾸나요?** Prisma가 schema, 데이터베이스, 생성된 client를 모두 업데이트합니다. 자동으로 동기화 상태를 유지합니다.
- **관계를 변경하나요?** Prisma는 안전한 마이그레이션을 생성하고 완전한 타입 안전성으로 정확성을 강제합니다.

팀이 Prisma를 선택하는 이유는 정확성을 강제하면서도 문제를 일으키지 않고 빠르게 개발할 수 있게 도와주기 때문입니다.

## Batteries-Included Ecosystem

Drizzle과 Prisma ORM 모두, 사용자가 라이브러리에서 직접 지원하지 않는 작업을 하길 원하는 경우가 있습니다. Drizzle은 이러한 경우를 피하기 위해 SQL의 표현력을 활용하는 반면, Prisma ORM은 [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)를 통해 어떤 사용자든 자신의 Prisma Client 인스턴스에 추가 동작을 더할 수 있게 합니다. 이러한 확장은 공유도 가능하므로, 팀이 자체 프로젝트 전반에서 사용하거나 다른 팀이 사용할 수 있도록 개발할 수 있습니다.

Drizzle은 비교적 새로운 제품인 반면, Prisma ORM은 [2021년에 출시](https://www.prisma.io/blog/how-prisma-orm-became-the-most-downloaded-orm-for-node-js)되어 JavaScript/TypeScript 생태계에서 잘 자리 잡았습니다. 이미 그 가치를 입증했으며, 많은 회사가 [Prisma ORM을 프로덕션에서 신뢰](https://www.prisma.io/showcase)하고 있습니다.

Prisma ORM은 또한 [Amplication](https://amplication.com/), [Wasp](https://wasp.sh/), [RedwoodJS](https://rwsdk.com/), [KeystoneJS](https://keystonejs.com/), [Remix](https://remix.run/) 그리고 [t3 stack](https://create.t3.gg/) 같은 많은 메타 프레임워크와 개발 플랫폼에서 선호되는 데이터 계층 도구로 포함되어 있습니다.

Prisma의 성숙도 덕분에, Prisma 커뮤니티는 다양한 Prisma 워크플로를 돕는 [매우 다양한 유용한 도구](https://www.prisma.io/ecosystem)를 개발해 왔습니다. 몇 가지 주요 예시는 다음과 같습니다:

- [`prisma-erd-generator`](https://github.com/keonik/prisma-erd-generator#prisma-entity-relationship-diagram-generator): Prisma schema를 엔터티 관계 다이어그램(ERD)으로 시각화합니다.
- [`prisma-zod-generator`](https://github.com/omar-dulaimi/prisma-zod-generator): Prisma schema로부터 [Zod](https://github.com/colinhacks/zod) schema를 생성합니다.
- [`bridg`](https://github.com/bridg-db/bridg): Prisma Client를 사용해 프런트엔드에서 데이터베이스에 접근할 수 있게 합니다.
- [`jest-prisma`](https://github.com/Quramy/jest-prisma): [Jest](https://jestjs.io/)와 통합된 Prisma 테스트 환경입니다.
- [`prisma-pothos-types`](https://github.com/hayes/pothos/tree/main/packages/plugin-prisma): [GraphQL Pothos](https://github.com/hayes/pothos/tree/main)를 사용할 때 Prisma 모델 기반 GraphQL 타입을 생성합니다.
- [`prisma-trpc-generator`](https://github.com/omar-dulaimi/prisma-trpc-generator): Prisma schema로부터 [tRPC](https://trpc.io/) router를 생성합니다.
- [`@cerbos/orm-prisma`](https://github.com/cerbos/query-plan-adapters/tree/main/prisma): [Cerbos](https://www.cerbos.dev)의 권한 부여 정책을 기반으로 데이터를 필터링합니다.

Prisma는 단순한 ORM이 아니라, 완전한 type-safe 데이터 툴킷입니다:

- Prisma Schema → migrations, types, and documentation
- Prisma Client → auto-completed, fully type-safe queries
- Prisma Studio → 데이터를 조회하고 편집할 수 있는 [GUI](https://prisma.io/studio)
- Native integrations → PlanetScale, Vercel, Cloudflare D1, Neon 등

## 데이터베이스 지원

Drizzle과 Prisma ORM 모두 여러 종류의 데이터베이스를 지원합니다. Drizzle은 Drizzle이 만든 드라이버 구현을 통해 이러한 지원을 제공하며, 이는 기존의 서드파티 데이터베이스 드라이버와 통합됩니다.

Prisma ORM도 [서드파티 데이터베이스 드라이버](https://www.prisma.io/blog/serverless-database-drivers-KML1ehXORxZV) 지원을 추가하기 시작했습니다. 또한 Prisma는 기본적으로 TLS 연결을 사용하므로 보안이 향상됩니다.

추가로 Prisma ORM은 CockroachDB, Microsoft SQL Server, MongoDB를 지원하지만, Drizzle은 현재 이를 지원하지 않습니다. Prisma ORM은 또한 [relation mode](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode)를 제공하여, 이를 지원하지 않는 데이터베이스 엔진에서도 Prisma ORM이 foreign key 제약을 에뮬레이션할 수 있게 합니다. 반면 Drizzle은 현재 Prisma ORM이 지원하지 않는 Cloudflare D1, `bun:sqlite`, HTTP Proxy를 통한 SQLite를 지원합니다.

## 벤치마크

ORM을 선택할 때 성능이 핵심 고려사항이라는 점을 잘 알고 있습니다. 다양한 ORM의 성능을 비교하려면, Vercel에서 호스팅하는 오픈 소스 [database latency benchmark tool](https://pris.ly/benchmark)을 사용할 수 있습니다. 이 도구를 사용하면 서로 다른 워크로드와 구성에서 다양한 ORM의 지연 시간(latency)과 처리량(throughput)을 평가할 수 있습니다. 검토 중인 데이터베이스 또는 데이터베이스 제공자를 대상으로 벤치마크를 실행하면, 상대적인 성능 특성을 명확히 파악해 더 나은 의사결정을 할 수 있습니다.

또는 Drizzle을 포함한 인기 TypeScript ORM을 비교하기 위해 우리가 구축한 [benchmark tool](https://benchmarks.prisma.io)의 결과를 검토할 수도 있습니다. 이 벤치마크는 오픈 소스이며, Node.js 및 TypeScript 생태계에서 데이터베이스 제공자와 ORM 라이브러리 전반의 데이터베이스 쿼리 지연 시간을 공정하게 비교하는 것을 목표로 합니다.

## 결론

네, 우리는 편향되어 있을 수 있습니다. 하지만 이는 사용자와 고객에게서 실제로 들은 이야기이기도 합니다:

- "We switched from Drizzle to Prisma because schema drift was killing us. Prisma just works."
- "I onboarded a junior dev in 2 hours thanks to Prisma’s schema. With Drizzle, it would’ve taken days."
- "I trust Prisma to keep our database sane. No one on our team needs to be a Postgres expert."
- "The pace of updates and new features from the Prisma team has been nothing short of outstanding."

Drizzle ORM과 Prisma ORM은 모두 데이터 접근과 마이그레이션을 위한 도구입니다. Drizzle은 SQL 유사 문법을 감싸는 얇은 래퍼(thin wrapper)에 초점을 두고, Prisma는 편리하고 표현력 있는 API에 초점을 둡니다. 그 외 중요한 차이점으로는 Prisma ORM의 MSSQL 및 MongoDB 지원, [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)를 통한 추가 기능 지원, 추가적인 클라우드 대응 제품, 그리고 견고한 생태계가 있습니다.

반면, 데이터베이스 경험 수준이 다양한 개발자(프런트엔드, 백엔드, 풀스택)로 구성된 팀에게는 Prisma ORM이 데이터 접근과 데이터베이스 스키마 관리를 위한 포괄적이고 학습하기 쉬운 접근 방식을 제공합니다.
