---
title: "체크 제약 조건"
description: "Prisma ORM과 PostgreSQL에서 데이터 유효성 검증을 위해 CHECK 제약 조건을 구성하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/check-constraints

# 체크 제약 조건

Prisma ORM과 PostgreSQL에서 데이터 유효성 검증을 위해 CHECK 제약 조건을 구성하는 방법을 알아보세요.

이 페이지에서는 PostgreSQL 데이터베이스에서 [check constraints](https://www.postgresql.org/docs/9.4/ddl-constraints.html#DDL-CONSTRAINTS-CHECK-CONSTRAINTS)를 구성하는 방법을 설명합니다. 체크 제약 조건은 값이 테이블에 저장되기 전에 반드시 충족되어야 하는 조건입니다. 예를 들어, 제품의 할인 가격은 항상 원래 가격보다 낮아야 합니다.

체크 제약 조건은 테이블을 생성할 때(`CREATE TABLE` 사용) 추가하거나, 이미 존재하는 테이블에(`ALTER TABLE` 사용) 추가할 수 있습니다.

## 사전 요구 사항

- 실행 중인 [PostgreSQL](https://www.postgresql.org/) 데이터베이스 서버
- [`psql`](https://www.postgresql.org/docs/13/app-psql.html) 명령줄 클라이언트
- 설치된 [Node.js](https://nodejs.org/)

## 단일 컬럼 체크 제약 조건

단일 컬럼에 체크 제약 조건이 있는 테이블을 생성합니다:

```
    CREATE TABLE "public"."product" (
      price NUMERIC CONSTRAINT price_value_check CHECK (price > 0.01 AND price <> 1240.00)
    );
    ALTER TABLE "public"."product"
      ADD COLUMN "productid" serial,
      ADD PRIMARY KEY ("productid");
```

이렇게 하면 price가 0.01보다 작아지지 않고, 1240.00과 같아지지도 않도록 보장됩니다.

## 다중 컬럼 체크 제약 조건

두 컬럼의 값을 비교하는 체크 제약 조건이 있는 테이블을 생성합니다:

```
    CREATE TABLE "public"."anotherproduct" (
      reducedprice NUMERIC CONSTRAINT reduced_price_check CHECK (price > reducedprice),
      price NUMERIC
    );
    ALTER TABLE "public"."anotherproduct"
      ADD COLUMN "productid" serial,
      ADD PRIMARY KEY ("productid");
```

이렇게 하면 `reducedprice`가 항상 `price`보다 작도록 보장됩니다.

## 여러 체크 제약 조건

```
    CREATE TABLE "public"."secondtolastproduct" (
      reducedprice NUMERIC CONSTRAINT reduced_price_check CHECK (price > reducedprice),
      price NUMERIC,
      tags TEXT[] CONSTRAINT tags_contains_product CHECK ('product' = ANY(tags))
    );
    ALTER TABLE "public"."secondtolastproduct"
      ADD COLUMN "productid" serial,
      ADD PRIMARY KEY ("productid");
```

## 기존 테이블에 체크 제약 조건 추가

```
    CREATE TABLE "public"."lastproduct" (
      category TEXT
    );

    ALTER TABLE "public"."lastproduct"
      ADD CONSTRAINT "category_not_clothing" CHECK (category <> 'clothing');
```

## Prisma ORM과 함께 사용

인트로스펙션 후 Prisma 스키마에는 모델이 포함되지만, 체크 제약 조건은 데이터베이스 수준에서 적용됩니다:

```
    model product {
      price     Float?
      productid Int    @id
    }

    model anotherproduct {
      price        Float?
      productid    Int    @id
      reducedprice Float?
    }
```

Prisma Client를 생성하고 테스트합니다:

```
    const { PrismaClient } = require("../prisma/generated/client");

    const prisma = new PrismaClient();

    async function main() {
      // This will fail due to the check constraint
      const newProduct = await prisma.product.create({
        data: {
          price: 0.0, // violates price > 0.01
        },
      });
    }

    main();
```

스크립트는 `price_check_value` 체크 제약 조건이 충족되지 않았음을 나타내는 오류를 발생시킵니다:

```
    Error: new row for relation "product" violates check constraint "price_value_check"
```

체크 제약 조건은 알파벳 순서로 확인되며, 오류 메시지에는 가장 먼저 실패한 제약 조건만 표시됩니다.
