---
title: "SafeQL & Prisma Client"
description: "PostGIS처럼 Prisma에서 기본적으로 지원하지 않는 기능을 우회하기 위해 SafeQL과 Prisma Client 확장을 사용하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/safeql

# SafeQL & Prisma Client

PostGIS처럼 Prisma에서 기본적으로 지원하지 않는 기능을 우회하기 위해 SafeQL과 Prisma Client 확장을 사용하는 방법을 알아보세요.

## 개요

이 페이지에서는 Prisma ORM에서 raw SQL 작성 경험을 개선하는 방법을 설명합니다. [Prisma Client 확장](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)과 [SafeQL](https://safeql.dev)을 사용해, 앱에서 필요할 수 있는 커스텀 SQL(`$queryRaw` 사용)을 추상화한 사용자 정의 타입 안전 Prisma Client 쿼리를 만듭니다.

예제에서는 [PostGIS](https://postgis.net/)와 PostgreSQL을 사용하지만, 애플리케이션에서 필요한 모든 raw SQL 쿼리에 동일하게 적용할 수 있습니다.

이 페이지는 Prisma Client에서 제공하는 [기존 raw query 메서드](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries)를 기반으로 합니다. Prisma Client에서 raw SQL의 많은 사용 사례는 [TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql)로 다룰 수 있지만, `Unsupported` 필드 작업에는 이러한 기존 메서드를 사용하는 것이 여전히 권장되는 접근 방식입니다.

## SafeQL이란?

[SafeQL](https://safeql.dev/)은 raw SQL 쿼리에서 고급 linting과 타입 안전성을 제공합니다. 설정을 마치면 SafeQL은 Prisma Client의 `$queryRaw`, `$executeRaw`와 함께 동작하여 raw 쿼리가 필요할 때 타입 안전성을 제공합니다.

SafeQL은 [ESLint](https://eslint.org/) 플러그인으로 실행되며 ESLint 규칙으로 구성됩니다. 이 가이드는 ESLint 설정 자체는 다루지 않으며, 이미 프로젝트에서 ESLint가 실행 중이라고 가정합니다.

## 사전 준비

따라오려면 다음이 필요합니다:

- PostGIS가 설치된 [PostgreSQL](https://www.postgresql.org/) 데이터베이스
- 프로젝트에 설정된 Prisma ORM
- 프로젝트에 설정된 ESLint

## Prisma ORM의 지리 데이터 지원

작성 시점 기준으로 Prisma ORM은 지리 데이터, 특히 [PostGIS](https://github.com/prisma/prisma/issues/2789) 사용을 지원하지 않습니다.

지리 데이터 컬럼이 있는 모델은 [`Unsupported`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported) 데이터 타입으로 저장됩니다. `Unsupported` 타입 필드는 생성된 Prisma Client에 포함되며 `any` 타입으로 지정됩니다. 필수 `Unsupported` 타입이 있는 모델은 `create`, `update` 같은 쓰기 작업을 노출하지 않습니다.

Prisma Client는 필수 `Unsupported` 필드가 있는 모델의 쓰기 작업을 `$queryRaw`, `$executeRaw`로 지원합니다. raw 쿼리에서 지리 데이터를 다룰 때 Prisma Client 확장과 SafeQL을 사용하면 타입 안전성을 개선할 수 있습니다.

## 1\. PostGIS와 함께 사용하도록 Prisma ORM 설정

아직 하지 않았다면 Prisma 스키마에서 `postgresqlExtensions` Preview 기능을 활성화하고 `postgis` PostgreSQL 확장을 추가하세요:

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["postgresqlExtensions"]
    }

    datasource db {
      provider   = "postgresql"
      extensions = [postgis]
    }
```

호스팅된 데이터베이스 제공자를 사용하지 않는 경우, `postgis` 확장을 직접 설치해야 할 가능성이 큽니다. PostGIS 시작 방법은 [PostGIS 문서](http://postgis.net/documentation/getting_started/#installing-postgis)를 참고하세요. Docker Compose를 사용 중이라면 아래 스니펫으로 PostGIS가 설치된 PostgreSQL 데이터베이스를 설정할 수 있습니다:

```
    version: "3.6"
    services:
      pgDB:
        image: postgis/postgis:13-3.1-alpine
        restart: always
        ports:
          - "5432:5432"
        volumes:
          - db_data:/var/lib/postgresql/data
        environment:
          POSTGRES_PASSWORD: password
          POSTGRES_DB: geoexample
    volumes:
      db_data:
```

다음으로 확장을 활성화하기 위해 마이그레이션을 생성하고 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name add-postgis
```

참고로, 마이그레이션 파일의 출력은 다음과 비슷해야 합니다:

migrations/TIMESTAMP_add_postgis/migration.sql

```
    -- CreateExtension
    CREATE EXTENSION IF NOT EXISTS "postgis";
```

`prisma migrate status`를 실행해 마이그레이션이 적용되었는지 다시 확인할 수 있습니다.

## 2\. 지리 데이터 컬럼을 사용하는 새 모델 생성

마이그레이션이 적용되면 `geography` 데이터 타입 컬럼이 있는 새 모델을 추가합니다. 이 가이드에서는 `PointOfInterest`라는 모델을 사용합니다.

```
    model PointOfInterest {
      id       Int                                   @id @default(autoincrement())
      name     String
      location Unsupported("geography(Point, 4326)")
    }
```

`location` 필드가 [`Unsupported`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported) 타입을 사용하는 것을 볼 수 있습니다. 즉, `PointOfInterest` 작업 시 Prisma ORM의 많은 이점을 잃게 됩니다. 이를 해결하기 위해 [SafeQL](https://safeql.dev/)을 사용합니다.

앞서와 같이 `prisma migrate dev` 명령으로 마이그레이션을 생성하고 실행해 데이터베이스에 `PointOfInterest` 테이블을 만듭니다:

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --name add-poi
```

참고로 Prisma Migrate가 생성한 SQL 마이그레이션 파일 출력은 다음과 같습니다:

migrations/TIMESTAMP_add_poi/migration.sql

```
    -- CreateTable
    CREATE TABLE "PointOfInterest" (
        "id" SERIAL NOT NULL,
        "name" TEXT NOT NULL,
        "location" geography(Point, 4326) NOT NULL,

        CONSTRAINT "PointOfInterest_pkey" PRIMARY KEY ("id")
    );
```

## 3\. SafeQL 통합

SafeQL은 Prisma ORM과 쉽게 통합되어 `$queryRaw`, `$executeRaw` Prisma 작업을 lint할 수 있습니다. [SafeQL 통합 가이드](https://safeql.dev/compatibility/prisma.html)를 참고하거나 아래 단계를 따르세요.

- 3.1. `@ts-safeql/eslint-plugin` npm 패키지 설치

npm

pnpm

yarn

bun

```
    npm install -D @ts-safeql/eslint-plugin libpg-query
```

이 ESLint 플러그인이 쿼리 linting을 가능하게 해줍니다.

- 3.2. ESLint 플러그인에 `@ts-safeql/eslint-plugin` 추가

다음으로 ESLint 플러그인 목록에 `@ts-safeql/eslint-plugin`을 추가합니다. 이 예제에서는 `.eslintrc.js` 파일을 사용하지만, [ESLint 구성](https://eslint.org/docs/latest/use/configure/) 방식이라면 무엇이든 동일하게 적용할 수 있습니다.

.eslintrc.js

```
    /** @type {import('eslint').Linter.Config} */
    module.exports = {
      "plugins": [..., "@ts-safeql/eslint-plugin"],
      ...
    }
```

- 3.3 `@ts-safeql/check-sql` 규칙 추가

이제 잘못된 SQL 쿼리를 ESLint 에러로 표시하도록 SafeQL 규칙을 설정합니다.

.eslintrc.js

```
    /** @type {import('eslint').Linter.Config} */
    module.exports = {
      plugins: [..., '@ts-safeql/eslint-plugin'],
      rules: {
        '@ts-safeql/check-sql': [
          'error',
          {
            connections: [
              {
                // The migrations path:
                migrationsDir: './prisma/migrations',
                targets: [
                  // This makes `prisma.$queryRaw` and `prisma.$executeRaw` commands linted
                  { tag: 'prisma.+($queryRaw|$executeRaw)', transform: '{type}[]' },
                ],
              },
            ],
          },
        ],
      },
    }
```

> **참고** : `PrismaClient` 인스턴스 이름이 `prisma`가 아니라면 `tag` 값을 그에 맞게 조정해야 합니다. 예를 들어 `db`라면 `tag` 값은 `'db.+($queryRaw|$executeRaw)'`가 되어야 합니다.

- 3.4. 데이터베이스 연결

마지막으로 SafeQL이 데이터베이스를 introspect하여 스키마에 사용된 테이블/컬럼 이름을 가져올 수 있도록 `connectionUrl`을 설정합니다. 그러면 SafeQL은 이 정보를 사용해 raw SQL 문을 lint하고 문제를 강조 표시합니다.

이 예제는 Prisma ORM과 동일한 연결 문자열을 가져오기 위해 [`dotenv`](https://github.com/motdotla/dotenv) 패키지에 의존합니다. 데이터베이스 URL을 버전 관리에서 제외하기 위해 이 방식을 권장합니다.

아직 `dotenv`를 설치하지 않았다면 다음과 같이 설치할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm install dotenv
```

그다음 ESLint 설정을 아래와 같이 업데이트하세요:

.eslintrc.js

```
    require("dotenv").config();

    /** @type {import('eslint').Linter.Config} */
    module.exports = {
      plugins: ["@ts-safeql/eslint-plugin"],
      // exclude `parserOptions` if you are not using TypeScript
      parserOptions: {
        project: "./tsconfig.json",
      },
      rules: {
        "@ts-safeql/check-sql": [
          "error",
          {
            connections: [
              {
                connectionUrl: process.env.DATABASE_URL,
                // The migrations path:
                migrationsDir: "./prisma/migrations",
                targets: [
                  // what you would like SafeQL to lint. This makes `prisma.$queryRaw` and `prisma.$executeRaw`
                  // commands linted
                  { tag: "prisma.+($queryRaw|$executeRaw)", transform: "{type}[]" },
                ],
              },
            ],
          },
        ],
      },
    };
```

이제 SafeQL이 완전히 설정되어 Prisma Client와 함께 더 나은 raw SQL을 작성할 수 있도록 도와줍니다.

## 4\. raw SQL 쿼리를 타입 안전하게 만드는 확장 만들기

이 섹션에서는 `PointOfInterest` 모델을 편리하게 다루기 위해 커스텀 쿼리를 포함한 두 개의 [`model`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model) 확장을 만듭니다:

1. 데이터베이스에 새 `PointOfInterest` 레코드를 생성할 수 있는 `create` 쿼리
2. 주어진 좌표에 가장 가까운 `PointOfInterest` 레코드를 반환하는 `findClosestPoints` 쿼리

- 4.1. `PointOfInterest` 레코드 생성을 위한 확장 추가

Prisma 스키마의 `PointOfInterest` 모델은 `Unsupported` 타입을 사용합니다. 그 결과 Prisma Client에서 생성되는 `PointOfInterest` 타입으로는 위도/경도 값을 담을 수 없습니다.

이를 해결하기 위해 TypeScript에서 모델을 더 잘 표현하는 두 개의 커스텀 타입을 정의합니다:

```
    type MyPoint = {
      latitude: number;
      longitude: number;
    };

    type MyPointOfInterest = {
      name: string;
      location: MyPoint;
    };
```

다음으로 Prisma Client의 `pointOfInterest` 속성에 `create` 쿼리를 추가할 수 있습니다:

```
    const prisma = new PrismaClient().$extends({
      model: {
        pointOfInterest: {
          async create(data: { name: string; latitude: number; longitude: number }) {
            // Create an object using the custom types from above
            const poi: MyPointOfInterest = {
              name: data.name,
              location: {
                latitude: data.latitude,
                longitude: data.longitude,
              },
            };

            // Insert the object into the database
            const point = `POINT(${poi.location.longitude} ${poi.location.latitude})`;
            await prisma.$queryRaw`
              INSERT INTO "PointOfInterest" (name, location) VALUES (${poi.name}, ST_GeomFromText(${point}, 4326));
            `;

            // Return the object
            return poi;
          },
        },
      },
    });
```

코드 스니펫에서 강조된 줄의 SQL이 SafeQL로 검사된다는 점에 주목하세요. 예를 들어 테이블 이름을 `"PointOfInterest"`에서 `"PointOfInterest2"`로 바꾸면 다음 에러가 나타납니다:

```
    error  Invalid Query: relation "PointOfInterest2" does not exist  @ts-safeql/check-sql
```

이 동작은 `name`, `location` 컬럼 이름에도 동일하게 적용됩니다.

이제 코드에서 다음과 같이 새 `PointOfInterest` 레코드를 생성할 수 있습니다:

```
    const poi = await prisma.pointOfInterest.create({
      name: "Berlin",
      latitude: 52.52,
      longitude: 13.405,
    });
```

- 4.2. `PointOfInterest`에 가장 가까운 레코드를 조회하는 확장 추가

이제 이 모델을 조회하기 위한 Prisma Client 확장을 만들어 보겠습니다. 주어진 경도/위도에 가장 가까운 관심 지점을 찾는 확장을 만들 것입니다.

```
    const prisma = new PrismaClient().$extends({
      model: {
        pointOfInterest: {
          async create(data: { name: string; latitude: number; longitude: number }) {
            // ... same code as before
          },

          async findClosestPoints(latitude: number, longitude: number) {
            // Query for closest points of interest
            const result = await prisma.$queryRaw<
              {
                id: number | null;
                name: string | null;
                st_x: number | null;
                st_y: number | null;
              }[]
            >`SELECT id, name, ST_X(location::geometry), ST_Y(location::geometry)
                FROM "PointOfInterest"
                ORDER BY ST_DistanceSphere(location::geometry, ST_MakePoint(${longitude}, ${latitude})) DESC`;

            // Transform to our custom type
            const pois: MyPointOfInterest[] = result.map((data) => {
              return {
                name: data.name,
                location: {
                  latitude: data.st_x || 0,
                  longitude: data.st_y || 0,
                },
              };
            });

            // Return data
            return pois;
          },
        },
      },
    });
```

이제 `PointOfInterest` 모델에 만든 커스텀 메서드를 사용해, 일반적인 Prisma Client 사용 방식 그대로 주어진 경도/위도에 가까운 관심 지점을 찾을 수 있습니다.

```
    const closestPointOfInterest = await prisma.pointOfInterest.findClosestPoints(53.5488, 9.9872);
```

앞서와 마찬가지로 SafeQL 덕분에 raw 쿼리에 추가 타입 안전성을 얻을 수 있습니다. 예를 들어 `location::geometry`를 `location`으로 바꿔 `location`의 `geometry` 캐스트를 제거하면, 각각 `ST_X`, `ST_Y`, `ST_DistanceSphere` 함수에서 linting 에러가 발생합니다.

```
    error  Invalid Query: function st_distancesphere(geography, geometry) does not exist  @ts-safeql/check-sql
```

## 결론

Prisma ORM을 사용할 때 때로는 raw SQL로 내려가야 할 수 있지만, Prisma ORM에서 raw SQL 쿼리 작성 경험을 개선하는 다양한 기법을 사용할 수 있습니다.

이 글에서는 SafeQL과 Prisma Client 확장을 사용해, 현재 Prisma ORM에서 기본적으로 지원되지 않는 PostGIS 작업을 추상화하는 사용자 정의 타입 안전 Prisma Client 쿼리를 만들었습니다.
