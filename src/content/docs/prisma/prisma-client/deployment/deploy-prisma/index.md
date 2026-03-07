---
title: "Prisma ORM 배포하기"
description: "Node.js 애플리케이션의 다양한 배포 패러다임과, 이러한 패러다임이 Prisma Client를 사용하는 애플리케이션 배포에 어떤 영향을 미치는지 자세히 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma

# Prisma ORM 배포하기

Node.js 애플리케이션의 다양한 배포 패러다임과, 이러한 패러다임이 Prisma Client를 사용하는 애플리케이션 배포에 어떤 영향을 미치는지 자세히 알아보세요.

Prisma Client를 사용하는 프로젝트는 다양한 클라우드 플랫폼에 배포할 수 있습니다. 클라우드 플랫폼의 종류가 많고 명칭도 제각각이므로, Prisma Client를 사용하는 애플리케이션 배포 방식에 영향을 주는 여러 배포 패러다임을 구분해 이해하는 것이 중요합니다.

## 배포 패러다임

각 패러다임은 애플리케이션의 성능, 확장성, 운영 비용에 영향을 주는 서로 다른 트레이드오프를 가집니다.

또한 애플리케이션의 사용자 트래픽 패턴도 중요한 고려 요소입니다. 예를 들어, 사용자 트래픽이 꾸준한 애플리케이션은 [지속 실행 패러다임](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma#traditional-servers)에 더 적합할 수 있고, 갑작스러운 트래픽 급증이 있는 애플리케이션은 [serverless](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma#serverless-functions)가 더 적합할 수 있습니다.

- 전통적인 서버

Node.js 프로세스가 지속적으로 실행되며 동시에 여러 요청을 처리한다면, 애플리케이션은 [전통적인 방식으로 배포](https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku)된 것입니다. 애플리케이션은 [Heroku](https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku), [Koyeb](https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-koyeb), [Render](https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-render) 같은 Platform-as-a-Service(PaaS)에 배포할 수도 있고, Kubernetes에 Docker 컨테이너로 배포하거나, 가상 머신 또는 베어메탈 서버에서 Node.js 프로세스로 실행할 수도 있습니다.

참고: [장기 실행 프로세스에서의 연결 관리](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#long-running-processes)

- Serverless Functions

요청이 들어올 때마다 애플리케이션의 Node.js 프로세스(또는 함수 단위로 분리된 일부)가 시작되고, 각 함수가 한 번에 하나의 요청만 처리한다면 애플리케이션은 [serverless](https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-vercel)입니다. 이 경우 보통 [AWS Lambda](https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-aws-lambda) 또는 [Azure Functions](https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions) 같은 Function-as-a-Service(FaaS)에 배포됩니다.

Serverless 환경에는 warm start 개념이 있습니다. 즉, 동일한 함수를 이후에 다시 호출할 때, 이미 존재하는 컨테이너를 재사용할 수 있으며 그 안의 할당된 프로세스, 메모리, 파일 시스템(AWS Lambda에서는 `/tmp`에 쓰기 가능), 심지어 DB 연결까지 그대로 사용 가능할 수 있습니다.

일반적으로 [handler 외부](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)에 있는 코드는 초기화된 상태로 유지됩니다.

참고: [Serverless 환경에서의 연결 관리](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)

- Edge Functions

애플리케이션이 [serverless](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma#serverless-functions)이며, 함수가 사용자와 가까운 하나 이상의 리전에 분산되어 있다면 애플리케이션은 [edge 배포](https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/overview)된 것입니다.

일반적으로 edge 환경은 전통적 환경이나 serverless 환경과 런타임이 다르기 때문에, 자주 사용되는 API를 사용할 수 없는 경우가 많습니다.
