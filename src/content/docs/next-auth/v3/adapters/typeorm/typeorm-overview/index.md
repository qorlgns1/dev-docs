---
title: 'TypeORM 어댑터[​](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview#typeorm-adapter "Direct link to heading")'
description: "원본 URL: https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview"
---

원본 URL: https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview

# 개요 | NextAuth.js

버전: v3

## TypeORM 어댑터[​](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview#typeorm-adapter "Direct link to heading")

NextAuth.js에는 [TypeORM](https://typeorm.io/)을 사용하는 기본 어댑터가 포함되어 있어, 추가 설정 없이도 다양한 데이터베이스와 함께 사용할 수 있습니다. 프로젝트에서 사용하려는 데이터베이스 드라이버의 node 모듈을 추가하고 NextAuth.js에 데이터베이스 연결 문자열을 전달하기만 하면 됩니다.

### 데이터베이스 스키마[​](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview#database-schemas "Direct link to heading")

NextAuth.js가 기대하는 스키마에 맞게 테이블과 컬럼을 생성하여 데이터베이스를 구성하세요.

- [MySQL 스키마](https://next-auth.js.org/v3/adapters/typeorm/mysql)
- [Postgres 스키마](https://next-auth.js.org/v3/adapters/typeorm/postgres)
- [Microsoft SQL Server 스키마](https://next-auth.js.org/v3/adapters/typeorm/mssql)
- [MongoDB](https://next-auth.js.org/v3/adapters/typeorm/mongodb)

기본 어댑터는 TypeORM 어댑터이며, TypeORM의 기본 데이터베이스 타입은 SQLite입니다. 다음 구성 옵션들은 정확히 동일합니다.

```
    database: {
      type: 'sqlite',
      database: ':memory:',
      synchronize: true
    }

```

```
    adapter: Adapters.Default({
      type: "sqlite",
      database: ":memory:",
      synchronize: true,
    })

```

```
    adapter: Adapters.TypeORM.Adapter({
      type: "sqlite",
      database: ":memory:",
      synchronize: true,
    })

```

튜토리얼 [Custom models with TypeORM](https://next-auth.js.org/v3/tutorials/typeorm-custom-models)에서는 TypeORM 어댑터에서 사용하는 내장 모델과 스키마를 확장하는 방법을 설명합니다. 이 모델들은 여러분의 코드에서도 사용할 수 있습니다.

tip

TypeORM의 `synchronize` 옵션은 MySQL 및 Postgres에 대해 문서화된 스키마와 정확히 일치하는 SQL을 생성합니다. 이 옵션은 엔티티 모델에서 발견한 변경 사항을 자동으로 적용하므로, 구성된 스키마가 예상 스키마와 일치하지 않을 경우 데이터 손실을 초래할 수 있어 **프로덕션 데이터베이스에서는 활성화하면 안 됩니다**!
