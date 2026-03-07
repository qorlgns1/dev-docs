---
title: "Render에 배포하기"
description: "Prisma ORM을 사용하는 Node.js 서버를 Render에 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-render

# Render에 배포하기

Prisma ORM을 사용하는 Node.js 서버를 Render에 배포하는 방법을 알아보세요.

이 가이드는 Prisma ORM과 PostgreSQL을 사용하는 Node.js 서버를 Render에 배포하는 방법을 설명합니다.

이 페이지에서 답하는 질문

- Render에 Prisma 앱을 배포하는 방법은?
- 시작 전에 마이그레이션을 실행하는 방법은?
- 권장되는 Render 설정은?

[Prisma Render deployment example](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render)에는 REST 엔드포인트와 간단한 프론트엔드를 포함한 Express.js 애플리케이션이 들어 있습니다. 이 앱은 Prisma Client를 사용해 데이터베이스에서 레코드를 조회, 생성, 삭제합니다.

## Render 소개

[Render](https://render.com)는 개발자가 풀스택 애플리케이션을 쉽게 배포하고 확장할 수 있도록 해주는 클라우드 애플리케이션 플랫폼입니다. 이 예제를 위해 알아두면 좋은 점은 다음과 같습니다.

- Render는 장시간 실행되는 "serverful" 풀스택 애플리케이션 배포를 지원합니다. CPU 및/또는 메모리 사용량에 따라 Render 서비스를 [autoscale](https://docs.render.com/scaling)하도록 구성할 수 있습니다. 이는 선택 가능한 여러 [deployment paradigms](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma) 중 하나입니다.
- Render는 Node.js와 Bun을 포함한 [common runtimes](https://docs.render.com/language-support)를 기본 지원합니다. 이 가이드에서는 Node.js 런타임을 사용합니다.
- Render는 커밋 시 자동 배포를 위해 [integrates with Git repos](https://docs.render.com/github)합니다. GitHub, GitLab, Bitbucket에서 Render로 배포할 수 있습니다. 이 가이드에서는 Git 저장소에서 배포합니다.

## 사전 준비

- [Render](https://render.com) 계정 가입

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
- `public/index.html`: 웹 프론트엔드입니다. 프론트엔드는 일부 API 엔드포인트를 호출합니다.

* Prisma 스키마와 마이그레이션

이 앱의 Prisma 구성 요소는 두 파일에 있습니다.

- `prisma/schema.prisma`: 이 앱의 데이터 모델입니다. 이 예제는 `User`와 `Post` 두 모델을 정의합니다. 이 파일 형식은 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 따릅니다.
- `prisma/migrations/<migration name>/migration.sql`: PostgreSQL 데이터베이스에서 이 스키마를 구성하는 SQL 명령입니다. [`prisma migrate dev`](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#what-is-prisma-migrate)를 실행하면 이와 같은 마이그레이션 파일을 자동 생성할 수 있습니다.

* Render Blueprint

`render.yaml` 파일은 [Render blueprint](https://docs.render.com/infrastructure-as-code)입니다. Blueprint는 Render의 Infrastructure as Code 형식입니다. Blueprint를 사용하면 Render의 서비스를 프로그래밍 방식으로 생성하고 수정할 수 있습니다.

`render.yaml`은 Blueprint를 통해 Render에 생성될 서비스를 정의합니다. 이 `render.yaml`에서는 다음을 볼 수 있습니다.

- **Node 런타임을 사용하는 웹 서비스** : Express 앱입니다.
- **PostgreSQL 데이터베이스** : Express 앱이 사용하는 데이터베이스입니다.

이 파일 형식은 [Blueprint specification](https://docs.render.com/blueprint-spec)을 따릅니다.

- Render 배포가 Prisma Migrate와 동작하는 방식

일반적으로 웹 앱이 시작되기 전에 모든 데이터베이스 마이그레이션이 실행되도록 해야 합니다. 그렇지 않으면 앱이 예상한 테이블과 행이 없는 데이터베이스를 조회할 때 오류가 발생할 수 있습니다.

Render 배포의 Pre-Deploy Command 설정을 사용하면 앱 시작 전에 데이터베이스 마이그레이션 같은 명령을 실행할 수 있습니다.

Pre-Deploy Command에 대한 자세한 내용은 [Render's deploy guide](https://docs.render.com/deploys#deploy-steps)를 참고하세요.

예제 코드의 `render.yaml`에는 웹 서비스의 build command, pre-deploy command, start command가 표시됩니다. 특히 `npx prisma migrate deploy`(pre-deploy command)는 `npm run start`(start command)보다 먼저 실행됩니다.

| **Command**        | **Value**                        |
| ------------------ | -------------------------------- |
| Build Command      | `npm install --production=false` |
| Pre-Deploy Command | `npx prisma migrate deploy`      |
| Start Command      | `npm run start`                  |

## 예제 배포하기

- 1\. Git 저장소 초기화
  1. [the example code](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render)를 로컬 머신에 다운로드합니다.
  2. GitHub, GitLab, BitBucket에 새 Git 저장소를 생성합니다.
  3. 예제 코드를 새 저장소에 업로드합니다.

- 2\. 수동 배포
  1. Render Dashboard에서 **New** > **PostgreSQL**을 클릭합니다. 데이터베이스 이름을 입력하고 플랜을 선택합니다. (이 데모에서는 Free 플랜으로도 충분합니다.)
  2. 데이터베이스 준비가 완료되면 해당 데이터베이스의 [internal URL](https://docs.render.com/postgresql-creating-connecting#internal-connections)을 확인합니다.
  3. Render Dashboard에서 **New** > **Web Service**를 클릭하고 예제 코드가 있는 Git 저장소를 연결합니다.
  4. 서비스 생성 중 다음 값을 입력합니다.

| **Setting**                                             | **Value**                                           |
| ------------------------------------------------------- | --------------------------------------------------- |
| Language                                                | `Node`                                              |
| Build Command                                           | `npm install --production=false`                    |
| Pre-Deploy Command (참고: "Advanced" 탭에 있을 수 있음) | `npx prisma migrate deploy`                         |
| Start Command                                           | `npm run start`                                     |
| Environment Variables                                   | `DATABASE_URL`을 데이터베이스의 internal URL로 설정 |

이제 끝입니다. 빌드가 완료되는 즉시 웹 서비스가 `onrender.com` URL에서 실행됩니다.

- 3\. (선택 사항) Infrastructure as Code로 배포

Render Blueprint를 사용해 예제를 배포할 수도 있습니다. Render의 [Blueprint setup guide]를 따라 진행하고, 예제의 `render.yaml`을 사용하세요.

## 보너스: 데이터베이스 시드

Prisma ORM에는 시작 데이터를 데이터베이스에 넣기 위한 [seeding the database](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/seeding) 프레임워크가 포함되어 있습니다. 이 예제에서는 `prisma/seed.js`에서 테스트 사용자와 게시물을 정의합니다.

이 사용자를 데이터베이스에 추가하려면 다음 두 가지 방법 중 하나를 사용할 수 있습니다.

1. 시드 스크립트를 Pre-Deploy Command에 추가하거나
2. SSH 셸을 통해 서버에서 수동으로 명령을 실행

- 방법 1: Pre-Deploy Command

Render 서비스를 수동으로 배포한 경우:

1. Render dashboard에서 웹 서비스로 이동합니다.
2. **Settings**를 선택합니다.
3. Pre-Deploy Command를 다음으로 설정합니다: `npx prisma migrate deploy; npx prisma db seed`

Blueprint를 사용해 Render 서비스를 배포한 경우:

1. `render.yaml` 파일에서 `preDeployCommand`를 다음으로 변경합니다: `npx prisma migrate deploy; npx prisma db seed`
2. 변경 사항을 Git 저장소에 커밋합니다.

- 방법 2: SSH

Render는 웹 서비스에 SSH 접속을 허용합니다.

1. 서버에 연결하려면 [Render's SSH guide](https://docs.render.com/ssh)를 따르세요.
2. 셸에서 다음을 실행합니다: `npx prisma db seed`
