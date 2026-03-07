---
title: "AWS Lambda에 배포하기"
description: "AWS SAM, Serverless Framework 또는 SST를 사용해 Prisma ORM 기반 애플리케이션을 AWS Lambda에 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-aws-lambda

# AWS Lambda에 배포하기

AWS SAM, Serverless Framework 또는 SST를 사용해 Prisma ORM 기반 애플리케이션을 AWS Lambda에 배포하는 방법을 알아보세요.

빠른 요약

이 가이드는 Prisma ORM을 사용하는 프로젝트를 [AWS Lambda](https://aws.amazon.com/lambda/)에 배포할 때 흔히 발생하는 문제를 피하는 방법을 설명합니다.

이 페이지에서 답하는 질문

- Prisma를 AWS Lambda에 어떻게 배포하나요?
- 어떤 binaryTargets를 구성해야 하나요?
- Lambda에서 connection pooling을 어떻게 처리하나요?

AWS Lambda에 배포할 때 배포 프레임워크가 필수는 아니지만, 이 가이드에서는 다음을 사용한 배포를 다룹니다.

- [AWS Serverless Application Model (SAM)](https://aws.amazon.com/serverless/sam/)은 서버리스 애플리케이션 생성에 사용할 수 있는 AWS의 오픈소스 프레임워크입니다. AWS SAM에는 애플리케이션을 빌드, 테스트, 배포하는 데 사용할 수 있는 [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html#serverless-sam-cli)가 포함되어 있습니다.

- [Serverless Framework](https://www.serverless.com/framework)는 워크플로 자동화와 AWS 리소스 프로비저닝을 돕는 CLI를 제공합니다. Prisma ORM은 Serverless Framework에서 기본 설정만으로도 잘 동작하지만, 원활한 배포와 성능을 위해 프로젝트 내에서 몇 가지 개선을 할 수 있습니다. 또한 [`serverless-webpack`](https://www.npmjs.com/package/serverless-webpack) 또는 [`serverless-bundle`](https://www.npmjs.com/package/serverless-bundle) 라이브러리를 사용하는 경우 추가 설정이 필요합니다.

- [SST](https://sst.dev/)는 개발자가 애플리케이션을 쉽게 정의, 테스트, 디버그, 배포할 수 있도록 도구를 제공합니다. Prisma ORM은 SST와 잘 동작하지만, 스키마가 SST에 의해 올바르게 패키징되도록 구성해야 합니다.

## AWS Lambda에 배포할 때의 일반 고려사항

이 섹션은 프레임워크와 관계없이 애플리케이션에 적용해야 하는 변경 사항을 다룹니다. 이 단계를 완료한 뒤, 사용하는 프레임워크의 단계를 따르세요.

- AWS SAM으로 배포
- Serverless Framework로 배포
- SST로 배포

* Connection pooling

Function as a Service(FaaS) 환경에서는 각 함수 호출이 일반적으로 새로운 데이터베이스 연결을 생성합니다. 지속적으로 실행되는 Node.js 서버와 달리, 이러한 연결은 실행 간에 유지되지 않습니다. 서버리스 환경에서 더 나은 성능을 위해서는 함수 호출마다 새 연결을 만들기보다 기존 데이터베이스 연결을 재사용하도록 connection pooling을 구현하세요.

이 문제를 해결하기 위해 내장 connection pooling을 제공하는 [Prisma Postgres](https://docs.prisma.io/docs/postgres)를 사용할 수 있습니다. 다른 해결 방법은 [서버리스 환경용 connection management 가이드](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)를 참고하세요.

## AWS SAM으로 배포

- 환경 변수 로드

AWS SAM은 `.env` 파일의 값을 직접 로드하는 것을 지원하지 않습니다. 이 파라미터를 저장하고 조회하려면 AWS 서비스 중 하나를 사용해야 합니다. [이 가이드](https://medium.com/bip-xtech/a-practical-guide-to-surviving-aws-sam-d8ab141b3d25)는 Parameters, SSM, Secrets Manager 등에서 값을 저장하고 조회하는 방법과 선택지를 잘 설명합니다.

## Serverless Framework로 배포

- `.env` 파일을 통한 환경 변수 로드

함수가 데이터베이스에 접근하려면 `DATABASE_URL` 환경 변수가 필요합니다. `serverless-dotenv-plugin`을 사용하면 배포 시 `.env` 파일을 사용할 수 있습니다.

먼저 플러그인이 설치되어 있는지 확인하세요.

npm

pnpm

yarn

bun

```
    npm install -D serverless-dotenv-plugin
```

그런 다음 `serverless.yml`의 plugins 목록에 `serverless-dotenv-plugin`을 추가하세요.

serverless.yml

```
    plugins:
      - serverless-dotenv-plugin
```

이제 `.env` 파일의 환경 변수가 패키징 또는 배포 시 자동으로 로드됩니다.

```
    serverless package
```

```
    Running "serverless" from node_modules
    DOTENV: Loading environment variables from .env:
             - DATABASE_URL

    Packaging deployment-example-sls for stage dev (us-east-1)
    .
```

## SST로 배포

- 환경 변수 다루기

SST는 `.env` 파일을 지원하지만, [권장되지는 않습니다](https://v2.sst.dev/config#should-i-use-configsecret-or-env-for-secrets). SST는 이러한 환경 변수에 안전하게 접근하기 위해 `Config` 사용을 권장합니다.

[여기서 제공되는](https://v2.sst.dev/config#overview) SST 가이드는 `Config` 시작을 위한 단계별 안내입니다. `DATABASE_URL`이라는 새 secret을 만들고 [해당 secret을 앱에 바인딩했다면](https://v2.sst.dev/config#bind-the-config), 다음과 같이 `PrismaClient`를 설정할 수 있습니다.

prisma.ts

```
    import { PrismaClient } from "./generated/client";
    import { Config } from "sst/node/config";
    import { PrismaPg } from "@prisma/adapter-pg";
    const globalForPrisma = global as unknown as { prisma: PrismaClient };

    const adapter = new PrismaPg({ connectionString });

    export const prisma =
      globalForPrisma.prisma ||
      new PrismaClient({ adapter });

    if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;

    export default prisma;
```
