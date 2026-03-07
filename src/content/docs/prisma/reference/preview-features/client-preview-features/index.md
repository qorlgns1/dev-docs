---
title: "Prisma Client & Prisma schema"
description: "현재 Preview 상태인 Prisma Client 및 Prisma schema 기능"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/preview-features/client-preview-features

# Prisma Client & Prisma schema

현재 Preview 상태인 Prisma Client 및 Prisma schema 기능

새로운 Prisma Client 또는 Prisma schema 기능을 릴리스할 때, 사용자가 기능을 테스트하고 피드백을 제출할 수 있도록 보통 Preview로 먼저 제공됩니다. 피드백을 반영해 기능을 개선하고 내부 테스트 결과가 충분히 만족스러우면, 해당 기능을 정식 출시(General Availability)로 승격합니다.

자세한 내용은 [ORM releases and maturity levels](https://docs.prisma.io/docs/orm/more/releases)를 참고하세요.

## 현재 활성화된 Preview 기능

다음 [Preview](https://docs.prisma.io/docs/orm/more/releases#preview) 기능 플래그를 Prisma Client 및 Prisma schema에서 사용할 수 있습니다:

| Feature                                                                                               | Preview로 릴리스됨                                             | 피드백 이슈                                                       |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`views`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/views)                             | [4.9.0](https://github.com/prisma/prisma/releases/tag/4.9.0)   | [피드백 제출](https://github.com/prisma/prisma/issues/17335)      |
| `relationJoins`                                                                                       | [5.7.0](https://github.com/prisma/prisma/releases/tag/5.7.0)   | [피드백 제출](https://github.com/prisma/prisma/discussions/22288) |
| `nativeDistinct`                                                                                      | [5.7.0](https://github.com/prisma/prisma/releases/tag/5.7.0)   | [피드백 제출](https://github.com/prisma/prisma/discussions/22287) |
| `typedSql`                                                                                            | [5.19.0](https://github.com/prisma/prisma/releases/tag/5.19.0) | [피드백 제출](https://github.com/prisma/prisma/discussions/25106) |
| `strictUndefinedChecks`                                                                               | [5.20.0](https://github.com/prisma/prisma/releases/tag/5.20.0) | [피드백 제출](https://github.com/prisma/prisma/discussions/25271) |
| [`fullTextSearchPostgres`](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/full-text-search) | [6.0.0](https://github.com/prisma/prisma/releases/tag/6.0.0)   | [피드백 제출](https://github.com/prisma/prisma/issues/25773)      |
| `shardKeys`                                                                                           | [6.10.0](https://pris.ly/release/6.10.0)                       | [피드백 제출](https://github.com/prisma/prisma/issues/)           |
| [`partialIndexes`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes)                  | [7.4.0](https://pris.ly/release/7.4.0)                         | [피드백 제출](https://github.com/prisma/prisma/issues/6974)       |

Preview 기능을 활성화하려면 `schema.prisma` 파일에서 [feature flag를 `generator` 블록에 추가](https://docs.prisma.io/docs/orm/reference/preview-features/client-preview-features#enabling-a-prisma-client-preview-feature)하세요. [GitHub에서 모든 Preview 기능에 대한 피드백을 공유](https://github.com/prisma/prisma/issues/3108)해 주세요.

## Prisma Client Preview 기능 활성화

Prisma Client Preview 기능을 활성화하려면:

1. `generator` 블록에 Preview 기능 플래그를 추가합니다:

```
generator client {
           provider        = "prisma-client"
           output          = "./generated"
           previewFeatures = ["relationJoins"]
         }
```

2. Prisma Client를 다시 생성합니다:

npm

pnpm

yarn

bun

```
npx prisma generate
```

3. Visual Studio Code를 사용 중인데 Prisma Client 생성 후에도 `.ts` 파일에서 Preview 기능을 사용할 수 없다면, **TypeScript: Restart TS server** 명령을 실행하세요.

## 정식 출시(General Availability)로 승격된 Preview 기능

아래 목록에서 Preview 상태였다가 현재는 정식 출시된 Prisma Client 및 Prisma schema 기능의 이력을 확인할 수 있습니다. 기능은 정식 출시로 승격된 최신 버전 순으로 정렬되어 있습니다.

| Feature                                                                                                                                          | Preview로 릴리스됨                                             | 정식 출시로 릴리스됨                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------- |
| [`driverAdapters`](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters)                           | [5.4.0](https://github.com/prisma/prisma/releases/tag/5.4.0)   | [6.16.0](https://github.com/prisma/prisma/releases/tag/6.16.0) |
| [`multiSchema`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/multi-schema)                                                           | [4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)   | [6.13.0](https://github.com/prisma/prisma/releases/tag/6.13.0) |
| [`prismaSchemaFolder`](https://docs.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema)                                 | [5.15.0](https://github.com/prisma/prisma/releases/tag/5.15.0) | [6.7.0](https://pris.ly/release/6.7.0)                         |
| `omitApi`                                                                                                                                        | [5.13.0](https://github.com/prisma/prisma/releases/tag/5.13.0) | [6.2.0](https://github.com/prisma/prisma/releases/tag/6.2.0)   |
| `jsonProtocol`                                                                                                                                   | [4.11.0](https://github.com/prisma/prisma/releases/tag/4.11.0) | [5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)   |
| [`extendedWhereUnique`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#filter-on-non-unique-fields-with-userwhereuniqueinput) | [4.5.0](https://github.com/prisma/prisma/releases/tag/4.5.0)   | [5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)   |
| [`fieldReference`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#compare-columns-in-the-same-table)                          | [4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)   | [5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0)   |
| [`clientExtensions`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)                                                            | [4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)   | [4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0) |
| [`filteredRelationCount`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#filter-the-relation-count)      | [4.3.0](https://github.com/prisma/prisma/releases/tag/4.3.0)   | [4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0) |
| [`tracing`](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing)                                       | [4.2.0](https://github.com/prisma/prisma/releases/tag/4.2.0)   | [6.1.0](https://github.com/prisma/prisma/releases/tag/6.1.0)   |
| [`orderByNulls`](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-with-null-records-first-or-last)            | [4.1.0](https://github.com/prisma/prisma/releases/tag/4.1.0)   | [4.16.0](https://github.com/prisma/prisma/releases/tag/4.16.0) |
| [`referentialIntegrity`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode)                                       | [3.1.1](https://github.com/prisma/prisma/releases/tag/3.1.1)   | [4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)   |
| [`interactiveTransactions`](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#interactive-transactions)                         | [2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0) | [4.7.0](https://github.com/prisma/prisma/releases/tag/4.7.0)   |

with Prisma Accelerate [5.1.1](https://github.com/prisma/prisma/releases/tag/5.1.1)
[`extendedIndexes`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes)| [3.5.0](https://github.com/prisma/prisma/releases/tag/3.5.0)| [4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)
[`filterJson`](https://docs.prisma.io/docs/orm/prisma-client/special-fields-and-types/working-with-json-fields#filter-on-a-json-field-simple)| [2.23.0](https://github.com/prisma/prisma/releases/tag/2.23.0)| [4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)
[`improvedQueryRaw`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#raw-query-type-mapping)| [3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)| [4.0.0](https://github.com/prisma/prisma/releases/tag/4.0.0)
[`cockroachdb`](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#cockroachdb)| [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)
migrations in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)| [3.14.0](https://github.com/prisma/prisma/releases/tag/3.14.0)
[`mongodb`](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)| [2.27.0](https://github.com/prisma/prisma/releases/tag/2.27.0)
introspection in [3.2.0](https://github.com/prisma/prisma/releases/tag/3.2.0)
embedded docs in [3.4.0](https://github.com/prisma/prisma/releases/tag/3.4.0)
raw queries in [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)
filters/ordering in embedded docs in [3.11.0](https://github.com/prisma/prisma/releases/tag/3.11.0)| [3.12.0](https://github.com/prisma/prisma/releases/tag/3.12.0)
[`microsoftSqlServer`](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/sql-server)| [2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`namedConstraints`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/database-mapping#constraint-and-index-names)| [2.29.0](https://github.com/prisma/prisma/releases/tag/2.29.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`referentialActions`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)| [2.26.0](https://github.com/prisma/prisma/releases/tag/2.26.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`orderByAggregateGroup`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#order-by-aggregate-group)| [2.21.0](https://github.com/prisma/prisma/releases/tag/2.21.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`orderByRelation`](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#sort-by-relation)| [2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)
aggregates in [2.19.0](https://github.com/prisma/prisma/releases/tag/2.19.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`selectRelationCount`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#count-relations)| [2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
`napi`| [2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)| [3.0.1](https://github.com/prisma/prisma/releases/tag/3.0.1)
[`groupBy`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#groupby)| [2.14.0](https://github.com/prisma/prisma/releases/tag/2.14.0)| [2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)
[`createMany`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#createmany)| [2.16.0](https://github.com/prisma/prisma/releases/tag/2.16.0)| [2.20.0](https://github.com/prisma/prisma/releases/tag/2.20.0)
[`nativeTypes`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#native-types-mapping)| [2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)| [2.17.0](https://github.com/prisma/prisma/releases/tag/2.17.0)
[`uncheckedScalarInputs`](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#create-a-single-record-and-multiple-related-records)| [2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)| [2.15.0](https://github.com/prisma/prisma/releases/tag/2.15.0)
[`transactionApi`](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#the-transaction-api)| [2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)| [2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)
[`connectOrCreate`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#connectorcreate)| [2.1.0](https://github.com/prisma/prisma/releases/tag/2.1.0)| [2.11.0](https://github.com/prisma/prisma/releases/tag/2.11.0)
[`atomicNumberOperations`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#atomic-number-operations)| [2.6.0](https://github.com/prisma/prisma/releases/tag/2.6.0)| [2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0)
[`insensitiveFilters` (PostgreSQL)](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#case-insensitive-filtering)| [2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)| [2.8.0](https://github.com/prisma/prisma/releases/tag/2.8.0)

[`aggregateApi`](https://docs.prisma.io/docs/orm/prisma-client/queries/aggregation-grouping-summarizing#aggregate)| [2.2.0](https://github.com/prisma/prisma/releases/tag/2.2.0)| [2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)
[`distinct`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#distinct)| [2.3.0](https://github.com/prisma/prisma/releases/tag/2.3.0)| [2.5.0](https://github.com/prisma/prisma/releases/tag/2.5.0)
