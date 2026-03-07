---
title: "Vercel에 배포하기"
description: "Prisma Client 기반 Next.js 애플리케이션을 Vercel에 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-vercel

# Vercel에 배포하기

Prisma Client 기반 Next.js 애플리케이션을 Vercel에 배포하는 방법을 알아보세요.

이 가이드는 Prisma를 사용하는 서버리스 애플리케이션을 [Vercel](https://vercel.com/)에 설정하고 배포하는 단계를 안내합니다.

Vercel은 정적 사이트, 서버리스 함수, 엣지 함수를 호스팅하는 클라우드 플랫폼입니다. Vercel 프로젝트를 GitHub 저장소와 연동하면 새 커밋을 푸시할 때 자동으로 배포할 수 있습니다.

Prisma를 사용하는 애플리케이션을 Vercel에 배포할 때 참고할 수 있도록 Next.js 기반 [예제 애플리케이션](https://github.com/prisma/deployment-example-vercel)을 만들었습니다.

예제는 Next.js를 사용하지만, 다른 애플리케이션도 Vercel에 배포할 수 있습니다. 다른 옵션의 예시는 [Using Express with Vercel](https://vercel.com/guides/using-express-with-vercel) 및 [Nuxt on Vercel](https://vercel.com/docs/frameworks/nuxt)을 참고하세요.

## 빌드 구성

- Vercel 빌드 중 Prisma Client 업데이트

Vercel은 배포 시 의존성을 자동으로 캐시합니다. 대부분의 애플리케이션에서는 문제가 되지 않지만, Prisma ORM의 경우 Prisma 스키마가 변경되었을 때 Prisma Client가 오래된 버전으로 남을 수 있습니다. 이 문제를 피하려면 애플리케이션의 `postinstall` 스크립트에 `prisma generate`를 추가하세요.

package.json

```
    {
      ...
      "scripts": {
        "postinstall": "prisma generate"
      }
      ...
    }
```

이렇게 하면 빌드 시점에 Prisma Client를 다시 생성하므로, 배포 환경에서 항상 최신 클라이언트를 사용할 수 있습니다. Prisma Client가 오래되는 문제를 피하는 또 다른 방법은 클라이언트를 버전 관리에 포함하는 것입니다. 이렇게 하면 각 배포에 올바른 Prisma Client가 반드시 포함됩니다.

Vercel 배포 중 `prisma: command not found` 오류가 발생한다면 dependencies에 `prisma`가 빠져 있는 것입니다. 기본적으로 `prisma`는 dev dependency이므로 일반 dependency로 옮겨야 할 수 있습니다.

- CI/CD 워크플로

더 고도화된 CI/CD 환경에서는 로컬 개발 중 수행한 마이그레이션을 데이터베이스 스키마에 반영하고 싶을 수 있습니다. 이때 [`prisma migrate deploy`](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#migrate-deploy) 명령을 사용할 수 있습니다.

이 경우 `package.json`에 사용자 지정 빌드 명령(예: `vercel-build`)을 다음과 같이 만들 수 있습니다.

package.json

```
    {
      ...
      "scripts" {
        "vercel-build": "prisma generate && prisma migrate deploy && next build",
      }
      ...
    }
```

다음 명령으로 CI/CD 파이프라인 안에서 이 스크립트를 호출할 수 있습니다.

npm

pnpm

yarn

bun

```
    npm run vercel-build
```

## 프리뷰 배포용 별도 데이터베이스 추가

기본적으로 애플리케이션에는 저장소의 `main` git 브랜치와 연결된 단일 _production_ 환경이 있습니다. 애플리케이션 변경을 위한 pull request를 열면 Vercel이 새 _preview_ 환경을 생성합니다.

Vercel은 프로젝트를 가져올 때 정의한 `DATABASE_URL` 환경 변수를 production과 preview 환경 모두에서 사용합니다. 이는 데이터베이스 스키마 마이그레이션이 포함된 pull request를 만들 경우, 해당 pull request가 production 데이터베이스 스키마를 변경하게 되어 문제가 됩니다.

이를 방지하려면 프리뷰 배포를 처리할 _두 번째_ 호스팅 데이터베이스를 사용하세요. 해당 연결 문자열을 얻은 뒤 Vercel 대시보드에서 preview 환경용 `DATABASE_URL`을 추가할 수 있습니다.

1. Vercel 프로젝트의 **Settings** 탭을 클릭합니다.

2. **Environment variables**를 클릭합니다.

3. 키를 `DATABASE_URL`로 하는 환경 변수를 추가하고, **Preview** 환경 옵션만 선택합니다.

![프리뷰 환경용 환경 변수 추가](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/serverless/images/300-60-deploy-to-vercel-preview-environment-variable.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

4. 값을 두 번째 데이터베이스의 연결 문자열로 설정합니다.

```
postgresql://dbUsername:dbPassword@myhost:5432/mydb
```

5. **Save**를 클릭합니다.

## 연결 풀링

Vercel Serverless functions 같은 Function-as-a-Service 제공자를 사용하면, 함수 호출마다 데이터베이스에 새 연결이 생길 수 있습니다. 이로 인해 데이터베이스의 열린 연결 수가 빠르게 한도에 도달하고 애플리케이션이 멈출 수 있습니다. 따라서 데이터베이스 연결 풀링은 필수입니다.

내장 연결 풀링이 제공되는 [Prisma Postgres](https://docs.prisma.io/docs/postgres)를 사용하면 Prisma Client 번들 크기를 줄이고 콜드 스타트를 피할 수 있습니다.

서버리스 환경의 연결 관리에 대한 자세한 내용은 [connection management guide](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)를 참고하세요.

## Vercel Fluid와 함께 Prisma ORM 사용하기

[Fluid compute](https://vercel.com/fluid)는 서버리스의 유연성과 서버의 안정성을 결합한 Vercel의 컴퓨팅 모델로, 스트리밍 데이터와 AI API 같은 동적 워크로드에 적합합니다. Vercel의 Fluid compute는 [엣지 및 Node.js 런타임을 모두 지원](https://vercel.com/docs/fluid-compute#available-runtime-support)합니다. 기존 서버리스 플랫폼의 일반적인 과제는 함수가 일시 중단될 때 풀에서 유휴 연결을 닫지 못해 데이터베이스 연결이 누수되는 문제입니다. Fluid는 함수가 일시 중단되기 전에 유휴 연결이 해제되도록 [`attachDatabasePool`](https://vercel.com/blog/the-real-serverless-compute-to-database-connection-problem-solved)을 제공합니다.

Fluid에서 연결을 안전하게 관리하려면 `attachDatabasePool`을 [Prisma의 driver adapters](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers)와 함께 사용하세요.

```
    import { Pool } from "pg";
    import { attachDatabasePool } from "@vercel/functions";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/client";

    const pool = new Pool({ connectionString: process.env.POSTGRES_URL });

    attachDatabasePool(pool);

    export const prisma = new PrismaClient({
      adapter: new PrismaPg(pool),
    });
```
