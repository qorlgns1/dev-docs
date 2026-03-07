---
title: "직접 SQL 작성하기"
description: "Prisma Client에서 raw SQL 쿼리를 사용하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql

# 직접 SQL 작성하기

Prisma Client에서 raw SQL 쿼리를 사용하는 방법을 알아보세요.

Prisma Client API는 모든 데이터베이스 쿼리를 직관적이고, 타입 안전하며, 편리하게 만들도록 설계되었지만, 여전히 raw SQL이 최선의 선택인 상황이 있을 수 있습니다.

이런 경우는 다양한 이유로 발생할 수 있습니다. 예를 들어 특정 쿼리의 성능을 최적화해야 하거나, Prisma Client의 쿼리 API로는 데이터 요구사항을 완전히 표현할 수 없는 경우입니다.

대부분의 경우 [TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql#writing-type-safe-queries-with-prisma-client-and-typedsql)을 사용하면 SQL로 쿼리를 작성하면서도 Prisma Client의 뛰어난 사용자 경험을 그대로 누릴 수 있습니다. 하지만 TypedSQL은 정적 타입 기반이므로 동적으로 생성되는 `WHERE` 절과 같은 특정 시나리오를 처리하지 못할 수 있습니다. 이런 경우에는 [`$queryRaw`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryraw) 또는 [`$executeRaw`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#executeraw), 혹은 이들의 unsafe 대응 메서드를 사용해야 합니다.

## Prisma Client와 TypedSQL로 타입 안전한 쿼리 작성하기

- TypedSQL이란?

TypedSQL은 Prisma ORM의 새로운 기능으로, `.sql` 파일에 쿼리를 작성하면서도 Prisma Client의 뛰어난 개발자 경험을 그대로 누릴 수 있게 해줍니다. 익숙한 방식으로 코드를 작성하면서 입력과 출력에 대한 완전한 타입 지원을 받을 수 있습니다.

TypedSQL을 사용하면 다음과 같은 이점이 있습니다:

1. 익숙한 문법으로 복잡한 SQL 쿼리 작성
2. SQL에 대한 완전한 IDE 지원 및 문법 하이라이팅 활용
3. TypeScript 코드에서 SQL 쿼리를 완전한 타입이 적용된 함수로 import
4. Prisma 타입 시스템의 안전성과 raw SQL의 유연성을 동시에 유지

TypedSQL은 특히 다음과 같은 경우에 유용합니다:

- Prisma의 쿼리 API로 표현하기 어려운 복잡한 리포팅 쿼리
- 정교하게 튜닝된 SQL이 필요한 성능 핵심 작업
- Prisma API에서 아직 지원되지 않는 데이터베이스 전용 기능 활용

TypedSQL을 사용하면 raw SQL의 강력함과 유연성을 포기하지 않으면서 효율적이고 type-safe한 데이터베이스 쿼리를 작성할 수 있습니다. 이 기능을 통해 Prisma 기반 애플리케이션에 커스텀 SQL 쿼리를 자연스럽게 통합하고, 타입 안전성을 보장하며 개발 생산성을 높일 수 있습니다.

설정 방법과 사용 예시를 포함해 TypedSQL을 시작하는 자세한 가이드는 [TypedSQL 문서](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/typedsql)를 참고하세요.

## 원시 쿼리(Raw queries)

[TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql#writing-type-safe-queries-with-prisma-client-and-typedsql)만큼 사용성이 좋지는 않지만, raw 쿼리는 여전히 지원되며 TypedSQL에서 아직 지원되지 않는 기능이 필요하거나 쿼리가 동적으로 생성되는 경우에 유용합니다.

- 관계형 데이터베이스에서 raw SQL 쿼리에 대한 대안적 접근

Prisma ORM은 관계형 데이터베이스에서 raw SQL 쿼리를 실행하기 위해 네 가지 메서드를 지원합니다:

- `$queryRaw`
- `$executeRaw`
- `$queryRawUnsafe`
- `$executeRawUnsafe`

이 명령들은 TypedSQL 사용 방식과 유사하지만, type-safe하지 않으며 전용 `.sql` 파일이 아니라 코드 내 문자열로 작성됩니다.

- 문서형 데이터베이스에서 raw 쿼리에 대한 대안적 접근

MongoDB의 경우 Prisma ORM은 raw 쿼리 실행을 위해 세 가지 메서드를 지원합니다:

- `$runCommandRaw`
- `<model>.findRaw`
- `<model>.aggregateRaw`

이 메서드들은 raw MongoDB 명령과 쿼리를 실행할 수 있게 해주며, MongoDB 전용 기능이나 최적화가 필요할 때 유연성을 제공합니다.

`$runCommandRaw`는 데이터베이스 명령 실행에 사용되고, `<model>.findRaw`는 필터와 일치하는 문서를 찾는 데 사용되며, `<model>.aggregateRaw`는 집계 작업에 사용됩니다.

관계형 데이터베이스의 raw 쿼리와 마찬가지로, 이 메서드들도 type-safe하지 않으며 쿼리 결과를 수동으로 처리해야 합니다.
