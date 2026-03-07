---
title: "로컬 환경에서 마이그레이션 배포하기"
description: "Prisma Client를 로컬에서 사용하는 Node.js 및 TypeScript 애플리케이션을 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment

# 로컬 환경에서 마이그레이션 배포하기

Prisma Client를 로컬에서 사용하는 Node.js 및 TypeScript 애플리케이션을 배포하는 방법을 알아보세요.

로컬 환경에서 프로덕션 환경으로 마이그레이션을 직접 배포하는 것을 고려할 수 있는 시나리오는 두 가지입니다.

- 로컬 CI/CD 파이프라인을 사용하는 경우
- 프로덕션 환경을 [베이스라이닝](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/baselining)하는 경우

이 페이지에서는 그렇게 할 수 있는 몇 가지 예시와 **일반적으로 이를 권장하지 않는 이유**를 설명합니다.

## 로컬 CI/CD 파이프라인

자동화된 CI/CD 프로세스가 없다면, 기술적으로는 다음과 같은 방법으로 로컬 환경에서 프로덕션에 새 마이그레이션을 배포할 수 있습니다.

1. 마이그레이션 히스토리가 최신 상태인지 확인하세요. `prisma migrate dev`를 실행하면 최신 변경 사항으로부터 마이그레이션 히스토리가 생성됩니다.
2. 로컬 connection URL을 프로덕션 connection URL로 교체합니다.

.env

```
    DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/my_local_database"

    DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/my_production_database"
```

3. `prisma migrate deploy`를 실행합니다.

**⛔ 다음 이유로 이 방법은 강력히 권장하지 않습니다**

- 프로덕션 데이터베이스 connection URL이 버전 관리에 노출될 위험이 있습니다.
- 실수로 프로덕션 connection URL을 사용해 **프로덕션 데이터베이스를 덮어쓰거나 삭제**할 수 있습니다.

**✅ 자동화된 CI/CD 파이프라인 구성을 권장합니다**

파이프라인은 스테이징 및 프로덕션 환경 배포를 처리하고, 파이프라인 단계에서 `migrate deploy`를 사용해야 합니다. 예시는 [배포 가이드](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate)를 참고하세요.

## 프로덕션 데이터베이스 베이스라이닝

Prisma Migrate를 **기존 데이터베이스**에 추가할 때는 프로덕션 데이터베이스를 [베이스라인](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/baselining)해야 합니다. 베이스라이닝은 **한 번만** 수행되며, 로컬 인스턴스에서 실행할 수 있습니다.

![로컬에서 Prisma ORM으로 프로덕션 베이스라이닝](https://docs.prisma.io/docs/img/orm/baseline-production-from-local.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)
