---
title: "Prisma Migrate 개요"
description: "Prisma Migrate에 대해 알아야 할 모든 것을 학습하세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate

# Prisma Migrate 개요

Prisma Migrate에 대해 알아야 할 모든 것을 학습하세요.

Prisma Migrate를 사용하면 다음이 가능합니다.

- [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)가 발전함에 따라 데이터베이스 스키마를 이에 맞춰 동기화된 상태로 유지
- 데이터베이스의 기존 데이터 유지

Prisma Migrate는 [`.sql` 마이그레이션 파일의 이력](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/migration-histories)을 생성하며, [개발 및 프로덕션](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production) 모두에서 역할을 수행합니다.

Prisma Migrate는 _하이브리드_ 데이터베이스 스키마 마이그레이션 도구로 볼 수 있으며, _선언형_ 요소와 _명령형_ 요소를 모두 갖습니다.

- 선언형: 데이터 모델은 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에서 선언적으로 설명됩니다. Prisma Migrate는 해당 데이터 모델로부터 SQL 마이그레이션 파일을 생성합니다.
- 명령형: 생성된 모든 SQL 마이그레이션 파일은 완전히 사용자 지정할 수 있습니다. 따라서 Prisma Migrate는 마이그레이션의 실행 대상과 실행 방식을 수정할 수 있게 하여 명령형 마이그레이션 도구의 유연성을 제공하며(예: 네이티브 데이터베이스 기능 활용, 데이터 마이그레이션 수행 등을 위한 커스텀 SQL 실행 허용), ...

프로토타이핑 중이라면 [`db push`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#db-push) 명령 사용을 고려하세요. 예시는 [`db push`를 사용한 스키마 프로토타이핑](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)을 참고하세요.

Prisma Migrate CLI 명령에 대한 자세한 정보는 [Prisma Migrate reference](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#prisma-migrate)를 확인하세요.

MongoDB에는 적용되지 않음

`migrate dev` 및 관련 명령 대신, [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서는 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용하세요.
