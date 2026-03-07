---
title: "PostgreSQL 확장"
description: "사용자 지정 마이그레이션을 사용해 Prisma ORM에서 PostgreSQL 확장을 설치하고 관리하는 방법, 그리고 Prisma Client에서 이를 사용하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/postgresql-extensions

# PostgreSQL 확장

사용자 지정 마이그레이션을 사용해 Prisma ORM에서 PostgreSQL 확장을 설치하고 관리하는 방법, 그리고 Prisma Client에서 이를 사용하는 방법

이 페이지는 [PostgreSQL 확장](https://www.postgresql.org/docs/current/external-extensions.html)에 관한 내용이며, Prisma ORM과 함께 사용하는 방법을 설명합니다.

## PostgreSQL 확장이란 무엇인가요?

PostgreSQL에서는 _확장(extension)_ 이라고 하는 패키지를 설치하고 활성화하여 데이터베이스 기능을 확장할 수 있습니다. 예를 들어 `citext` 확장은 대소문자를 구분하지 않는 문자열 데이터 타입을 추가합니다. `citext`와 같은 일부 확장은 PostgreSQL에서 직접 제공되며, 다른 확장들은 외부에서 개발됩니다. 확장에 대한 자세한 내용은 [PostgreSQL 문서](https://www.postgresql.org/docs/current/sql-createextension.html)를 참고하세요.

확장을 사용하려면 먼저 데이터베이스 서버의 로컬 파일 시스템에 해당 확장이 _설치_ 되어 있어야 합니다. 그런 다음 확장을 _활성화_ 해야 하며, 이 과정에서 새 기능을 추가하는 스크립트 파일이 실행됩니다.

## Prisma ORM에서 PostgreSQL 확장 사용하기

`citext` 확장을 설치하는 예제를 단계별로 살펴보겠습니다.

- 1\. 빈 마이그레이션 생성

아래 명령어를 실행해 [사용자 지정](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)할 수 있는 빈 마이그레이션을 생성합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- 2\. 확장을 설치하는 SQL 문 추가

`migrations` 디렉터리에 새로 생성된 마이그레이션 파일에 다음 구문을 추가합니다.

```
    CREATE EXTENSION IF NOT EXISTS citext;
```

- 3\. 마이그레이션 배포

아래 명령어를 실행해 마이그레이션을 배포하고 데이터베이스에 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate deploy
```

- 4\. 확장 사용

이제 Prisma Client로 쿼리할 때 해당 확장을 사용할 수 있습니다. 확장에 Prisma 스키마에서 현재 네이티브로 표현할 수 없는 특수 데이터 타입이 있더라도, 모델에서 해당 타입 필드를 [`Unsupported`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#unsupported-types) 폴백 타입으로 정의해 사용할 수 있습니다.
