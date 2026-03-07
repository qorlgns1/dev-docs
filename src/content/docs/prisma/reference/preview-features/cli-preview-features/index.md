---
title: "Prisma CLI 프리뷰 기능"
description: "현재 프리뷰 상태인 Prisma CLI 기능입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/preview-features/cli-preview-features

# Prisma CLI 프리뷰 기능

현재 프리뷰 상태인 Prisma CLI 기능입니다.

Prisma CLI의 새 기능을 출시할 때, 사용자가 테스트하고 피드백을 제출할 수 있도록 먼저 프리뷰로 시작하는 경우가 많습니다. 피드백을 반영해 기능을 개선하고 내부 테스트 결과가 충분하다고 판단되면, 해당 기능을 정식 출시(General Availability)로 승격합니다.

자세한 내용은 [ORM 릴리스 및 성숙도 수준](https://docs.prisma.io/docs/orm/more/releases)을 참고하세요.

## 현재 활성화된 프리뷰 기능

현재 Prisma CLI에는 [프리뷰](https://docs.prisma.io/docs/orm/more/releases#preview) 기능이 없습니다.

## 정식 출시로 승격된 프리뷰 기능

아래 목록에서는 프리뷰 상태였다가 현재 정식 출시된 Prisma CLI 기능의 이력을 확인할 수 있습니다. 기능은 정식 출시로 승격된 가장 최신 버전 순으로 정렬되어 있습니다.

| 기능                                                                                                                                                               | 프리뷰에서 출시                                                | 정식 출시                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------- |
| [`prisma migrate diff`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing#fixing-failed-migrations-with-migrate-diff-and-db-execute) | [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)   | [3.13.0](https://github.com/prisma/prisma/releases/tag/3.13.0) |
| [`prisma db execute`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/patching-and-hotfixing#fixing-failed-migrations-with-migrate-diff-and-db-execute)   | [3.9.0](https://github.com/prisma/prisma/releases/tag/3.9.0)   | [3.13.0](https://github.com/prisma/prisma/releases/tag/3.13.0) |
| [`prisma db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)                                                               | [2.10.0](https://github.com/prisma/prisma/releases/tag/2.10.0) | [2.22.0](https://github.com/prisma/prisma/releases/tag/2.22.0) |
| [`prisma migrate`](https://docs.prisma.io/docs/orm/prisma-migrate)                                                                                                 | [2.13.0](https://github.com/prisma/prisma/releases/tag/2.13.0) | [2.19.0](https://github.com/prisma/prisma/releases/tag/2.19.0) |
