---
title: "Fly.io에 배포하기"
description: "Prisma ORM을 사용하는 Node.js 서버를 Fly.io에 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-flyio

# Fly.io에 배포하기

Prisma ORM을 사용하는 Node.js 서버를 Fly.io에 배포하는 방법을 알아보세요.

이 가이드는 Prisma ORM과 PostgreSQL을 사용하는 Node.js 서버를 Fly.io에 배포하는 방법을 설명합니다.

[Prisma Render deployment example](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render)에는 REST 엔드포인트와 간단한 프런트엔드가 포함된 Express.js 애플리케이션이 들어 있습니다. 이 앱은 Prisma Client를 사용해 데이터베이스에서 레코드를 조회, 생성, 삭제합니다. 이 가이드에서는 수정 없이 동일한 애플리케이션을 Fly.io에 배포하는 방법을 보여줍니다.

## Fly.io 소개

[fly.io](https://fly.io/)는 개발자가 사용자와 가까운 머신에서 요청 시 시작되는 풀스택 애플리케이션을 쉽게 배포하고 확장할 수 있게 해주는 클라우드 애플리케이션 플랫폼입니다. 이 예제를 위해 알아두면 좋은 내용은 다음과 같습니다.

- Fly.io를 사용하면 [전 세계 35개 리전](https://fly.io/docs/reference/regions/)에 장시간 실행되는 "serverful" 풀스택 애플리케이션을 배포할 수 있습니다. 기본적으로 애플리케이션은 사용되지 않을 때 [자동 중지](https://fly.io/docs/launch/autostop-autostart/)되도록 구성되며, 요청이 들어오면 필요에 따라 자동 시작됩니다.
- Fly.io는 Node.js와 Bun을 포함해 다양한 [언어와 프레임워크](https://fly.io/docs/languages-and-frameworks/)를 네이티브로 지원합니다. 이 가이드에서는 Node.js 런타임을 사용합니다.
- Fly.io는 [GitHub에서 앱을 직접 시작](https://fly.io/speedrun)할 수 있습니다. CLI에서 `fly launch`를 실행하면 GitHub에 호스팅된 애플리케이션이 push 시 배포되도록 자동 구성됩니다.

## 사전 준비

- [Fly.io](https://fly.io/docs/getting-started/launch/) 계정 가입

## 예제 코드 가져오기

[example code](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render)를 로컬 머신에 다운로드하세요.

```
    curl https://codeload.github.com/prisma/prisma-examples/tar.gz/latest | tar -xz --strip=2 prisma-examples-latest/deployment-platforms/render
    cd render
```

## 예제 이해하기

앱을 배포하기 전에 예제 코드를 살펴보겠습니다.

- 웹 애플리케이션

Express 앱의 로직은 두 파일에 있습니다.

- `src/index.js`: API입니다. 엔드포인트는 Prisma Client를 사용해 데이터베이스에서 데이터를 조회, 생성, 삭제합니다.
- `public/index.html`: 웹 프런트엔드입니다. 프런트엔드는 API 엔드포인트 일부를 호출합니다.

* Prisma 스키마 및 마이그레이션

이 앱의 Prisma 구성 요소는 세 파일에 있습니다.

- `prisma/schema.prisma`: 이 앱의 데이터 모델입니다. 이 예제는 `User`와 `Post` 두 모델을 정의합니다. 이 파일 형식은 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 따릅니다.
- `prisma/migrations/<migration name>/migration.sql`: PostgreSQL 데이터베이스에서 이 스키마를 구성하는 SQL 명령입니다. [`prisma migrate dev`](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#what-is-prisma-migrate)를 실행해 이와 같은 마이그레이션 파일을 자동 생성할 수 있습니다.
- `prisma/seed.js`: 일부 테스트 사용자와 게시물을 정의하며, 시작 데이터를 [데이터베이스 시드](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding)하는 데 사용됩니다.

## 예제 배포하기

- 1\. `fly launch` 실행 후 기본값 수락

이것으로 끝입니다. 배포가 완료되는 즉시 웹 서비스가 `fly.dev` URL에서 실행됩니다. 선택적으로 원하는 대로 머신의 크기, 수, 배치를 [scale](https://fly.io/docs/launch/scale-count/)할 수 있습니다. [`fly console`](https://fly.io/docs/flyctl/console/)을 사용하면 새 머신 또는 기존 머신에 ssh로 접속할 수 있습니다.

자세한 내용은 [fly.io documentation](https://fly.io/docs/js/prisma/)에서 확인할 수 있습니다.
