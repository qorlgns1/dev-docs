---
title: "Railway에 배포하기"
description: "Prisma ORM과 Prisma Postgres를 사용하는 앱을 Railway에 배포하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-railway

# Railway에 배포하기

Prisma ORM과 Prisma Postgres를 사용하는 앱을 Railway에 배포하는 방법을 알아보세요

이 가이드는 Prisma ORM과 Prisma Postgres를 사용하는 앱을 [Railway](https://railway.com?utm_medium=integration&utm_source=docs&utm_campaign=prisma)에 배포하는 방법을 설명합니다. 이 앱은 REST API를 노출하며 Prisma Client를 사용해 Prisma Postgres 데이터베이스를 쿼리합니다. 앱은 Railway에서 실행되고 관리형 Prisma Postgres 데이터베이스에 연결됩니다.

Railway는 즉시 배포, 내장형 관측성, 손쉬운 스케일링을 통해 소프트웨어 개발 수명 주기를 단순화하는 배포 플랫폼입니다. 널리 사용되는 레지스트리의 코드 리포지토리와 컨테이너 이미지를 지원합니다. Railway는 구성 관리와 환경 변수를 처리하고, 서비스 간 프라이빗 네트워킹을 제공합니다.

Prisma ORM, Prisma Postgres, Railway가 미리 연결된 Next.js 프로젝트를 사용하려면 [Official Prisma Railway Template](https://railway.com/deploy/prisma-postgres?utm_medium=integration&utm_source=docs&utm_campaign=prisma)을 사용하세요.

이 템플릿은 Prisma Postgres 데이터베이스의 프로비저닝 및 설정을 자동화하고, 배포 시 이를 Next.js 애플리케이션에 직접 연결하여 한 번의 클릭만으로 전체 프로젝트를 준비 상태로 만듭니다.

## 사전 요구사항

시작하려면 다음만 있으면 됩니다:

- Railway account
- 애플리케이션 코드가 포함된 GitHub 리포지토리

아직 준비된 프로젝트가 없다면 [example Prisma project](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/railway)를 사용할 수 있습니다. Prisma ORM을 사용하는 간단한 Hono 애플리케이션으로, REST API, 엔드포인트 테스트용 프론트엔드, 마이그레이션이 포함된 Prisma 스키마가 정의되어 있습니다.

## 애플리케이션 배포하기

- 1\. 새 Railway 프로젝트 만들기
  1. [Railway dashboard](https://railway.com/dashboard?utm_medium=integration&utm_source=docs&utm_campaign=prisma)로 이동합니다.
  2. **Create a New Project**를 클릭합니다.
  3. **GitHub Repo**를 선택합니다.
  4. **Configure GitHub App**을 클릭하고 Railway를 승인합니다.
  5. 리포지토리를 선택합니다.

이제 애플리케이션이 Railway에 배포되기 시작하지만, 데이터베이스 연결이 없으면 정상적으로 실행되지 않습니다.

다음 섹션에서는 데이터베이스를 구성하고 Railway에서 `DATABASE_URL` 환경 변수를 설정합니다.

![Railway deploying application](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/railway-deploying.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

## 데이터베이스 구성하기

- 1\. 데이터베이스 연결 문자열 가져오기

Prisma Postgres 연결 문자열이 필요합니다. 가져오는 방법은 두 가지입니다:

- [Prisma Data Platform](https://console.prisma.io)에서 새 데이터베이스 생성
- 임시 데이터베이스를 위해 `npx create-db` 실행 _(계정 필요 없음)_

* 2\. Railway에 데이터베이스 URL 추가하기
  1. Railway 프로젝트에서 서비스를 엽니다.
  2. **Variables** 탭으로 이동합니다.
  3. **New Variable**을 클릭합니다.
  4. 이름을 `DATABASE_URL`로 설정합니다.
  5. 값으로 데이터베이스 연결 문자열을 붙여넣습니다.
  6. **Deploy**를 클릭해 새 환경 변수로 애플리케이션을 다시 배포합니다.

![Railway environment variables setup](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/railway-env-vars.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

- 3\. 애플리케이션에 접속하기

데이터베이스 URL이 구성된 상태로 배포가 완료되면:

1. **Settings** 탭으로 이동합니다.
2. **Networking** 아래에서 **Generate Domain**을 클릭합니다.
3. 생성된 URL에서 애플리케이션에 접속할 수 있습니다.

![Railway networking settings](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/railway-networking.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

생성된 URL로 이동하면 배포된 앱을 확인할 수 있습니다!

예제 프로젝트를 사용했다면, 다음 세 가지 api 엔드포인트가 이미 설정되어 있을 것입니다:

- API 상태 확인 (`/api`)
- 피드 로드 (`/api/feed`)
- 데이터 시드 (`/api/seed`)

![Railway deployed application](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/railway-final-product.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

오류가 보인다면:

- 잠시 기다린 뒤 새로고침합니다.
- `DATABASE_URL`이 설정되어 있는지 확인합니다.
- 서비스 로그를 확인합니다.
- 다시 배포합니다.

애플리케이션을 위해 Railway가 제공하는 다양한 기능을 더 알아보려면 [Railway documentation](https://docs.railway.app?utm_medium=integration&utm_source=docs&utm_campaign=prisma)을 방문하세요.
