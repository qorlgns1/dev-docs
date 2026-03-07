---
title: "Heroku에 배포하기"
description: "Prisma ORM을 사용하는 Node.js 서버를 Heroku에 배포하는 방법을 알아봅니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku

# Heroku에 배포하기

Prisma ORM을 사용하는 Node.js 서버를 Heroku에 배포하는 방법을 알아봅니다.

이 가이드에서는 PostgreSQL과 함께 Prisma ORM을 사용하는 Node.js 서버를 [Heroku](https://www.heroku.com)에 설정하고 배포합니다. 애플리케이션은 REST API를 노출하며, Prisma Client를 사용해 데이터베이스 레코드를 조회, 생성, 삭제합니다.

Heroku는 서비스형 클라우드 플랫폼(PaaS)입니다. 널리 사용되는 서버리스 배포 모델과 달리, Heroku에서는 요청이 없더라도 애플리케이션이 계속 실행됩니다. 이는 PostgreSQL 데이터베이스의 연결 제한 측면에서 여러 이점이 있습니다. 자세한 내용은 [일반 배포 문서](https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-prisma)를 확인하세요.

일반적으로 Heroku는 커밋 시 자동 배포를 위해 Git 저장소와 통합됩니다. GitHub 저장소에서 Heroku로 배포하거나, [앱마다 Heroku가 생성하는 Git 저장소](https://devcenter.heroku.com/articles/git)에 소스를 푸시할 수 있습니다. 이 가이드는 후자의 방식을 사용하며, Heroku의 앱 저장소로 코드를 푸시하면 빌드가 트리거되고 애플리케이션이 배포됩니다.

이 애플리케이션은 다음 구성 요소로 이루어져 있습니다.

- **Backend** : Express.js로 구축한 Node.js REST API로, 리소스 엔드포인트에서 Prisma Client를 사용해 PostgreSQL 데이터베이스(예: Heroku에서 호스팅) 대상 데이터베이스 작업을 처리합니다.
- **Frontend** : API와 상호작용하기 위한 정적 HTML 페이지.

![Prisma Client, 정적 프런트엔드, PostgreSQL 데이터베이스로 구성된 Node.js 백엔드를 보여주는 Heroku 배포 아키텍처 다이어그램.](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/heroku-architecture.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

이 가이드의 핵심은 Prisma ORM을 사용하는 프로젝트를 Heroku에 배포하는 방법을 보여주는 것입니다. 시작점으로는 [Prisma Heroku 예제](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/heroku)를 사용하며, 여기에는 사전 구성된 몇 가지 REST 엔드포인트와 간단한 프런트엔드가 포함된 Express.js 서버가 들어 있습니다.

> **Note:** 가이드 전반에 있는 여러 **체크포인트**를 통해 단계를 올바르게 수행했는지 확인할 수 있습니다.

## Heroku에 GraphQL 서버를 배포할 때 참고 사항

이 예제는 REST를 사용하지만, 동일한 원칙이 GraphQL 서버에도 적용됩니다. 주요 차이점은 REST처럼 리소스마다 라우트를 두는 대신 일반적으로 단일 GraphQL API 엔드포인트를 사용한다는 점입니다.

## 사전 준비

- [Heroku](https://www.heroku.com) 계정
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) 설치
- Node.js 설치
- PostgreSQL CLI `psql` 설치

> **Note:** Heroku는 무료 요금제를 제공하지 않으므로 결제 정보가 필요합니다.

## Prisma ORM 워크플로

Prisma ORM의 핵심에는 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)가 있습니다. 이는 데이터 모델과 기타 Prisma ORM 관련 구성을 정의하는 선언적 설정입니다. Prisma schema는 Prisma Client와 Prisma Migrate 모두의 단일 진실 공급원(single source of truth)이기도 합니다.

이 가이드에서는 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용해 데이터베이스 스키마를 생성합니다. Prisma Migrate는 Prisma schema를 기반으로 하며, 데이터베이스에 실행할 `.sql` 마이그레이션 파일을 생성하는 방식으로 동작합니다.

Migrate에는 두 가지 주요 워크플로가 있습니다.

- `prisma migrate dev`로 로컬 개발 중 마이그레이션 생성 및 적용
- `prisma migrate deploy`로 프로덕션에 생성된 마이그레이션 적용

간결함을 위해 이 가이드에서는 `prisma migrate dev`로 마이그레이션을 만드는 방법은 다루지 않습니다. 대신 프로덕션 워크플로에 집중하며, 예제 코드에 포함된 Prisma schema와 SQL 마이그레이션을 사용합니다.

Heroku의 [release phase](https://devcenter.heroku.com/articles/release-phase)를 사용해 `prisma migrate deploy` 명령을 실행하여 애플리케이션이 시작되기 전에 마이그레이션이 적용되도록 합니다.

Prisma Migrate로 마이그레이션을 생성하는 방법을 더 알아보려면 [처음부터 시작하기 가이드](https://docs.prisma.io/docs/prisma-orm/quickstart/postgresql)를 확인하세요.

## 1\. 예제 다운로드 및 의존성 설치

터미널을 열고 원하는 위치로 이동하세요. 애플리케이션 코드를 담을 디렉터리를 만들고 예제 코드를 다운로드합니다.

```
    mkdir prisma-heroku
    cd prisma-heroku
    curl https://codeload.github.com/prisma/prisma-examples/tar.gz/latest | tar -xz --strip=3 prisma-examples-latest/deployment-platforms/heroku
```

**Checkpoint:** `ls -1` 출력은 다음과 같아야 합니다.

```
    ls -1
    Procfile
    README.md
    package.json
    prisma
    public
    src
```

의존성을 설치합니다.

npm

pnpm

yarn

bun

```
    npm install
```

> **Note:** `Procfile`은 Heroku에 애플리케이션 시작에 필요한 명령(즉, `npm start`)과 release phase 중 실행할 명령(즉, `npx prisma migrate deploy`)을 알려줍니다.

## 2\. 애플리케이션용 Git 저장소 생성

이전 단계에서 코드를 다운로드했습니다. 이 단계에서는 배포를 위해 Heroku로 푸시할 수 있도록 코드로부터 저장소를 생성합니다.

이를 위해 소스 코드 폴더에서 `git init`을 실행합니다.

```
    git init
    > Initialized empty Git repository in /Users/alice/prisma-heroku/.git/
```

기본 브랜치로 `main` 브랜치를 사용하려면 다음 명령을 실행합니다.

```
    git branch -M main
```

저장소 초기화가 완료되면 파일을 추가하고 커밋합니다.

```
    git add .
    git commit -m 'Initial commit'
```

**Checkpoint:** `git log -1`에서 다음 커밋이 보여야 합니다.

```
    git log -1
    commit 895534590fdd260acee6396e2e1c0438d1be7fed (HEAD -> main)
```

## 3\. Heroku CLI 로그인

CLI로 Heroku에 로그인되어 있는지 확인합니다.

```
    heroku login
```

이렇게 하면 터미널에서 Heroku로 배포할 수 있습니다.

**Checkpoint:** `heroku auth:whoami`에서 사용자 이름이 표시되어야 합니다.

```
    heroku auth:whoami
    > your-email
```

## 4\. Heroku 앱 생성

애플리케이션을 Heroku에 배포하려면 앱을 생성해야 합니다. 다음 명령으로 생성할 수 있습니다.

```
    heroku apps:create your-app-name
```

> **Note:** `your-app-name` 대신 고유한 이름을 사용하세요.

**Checkpoint:** Heroku 앱의 URL과 저장소가 표시되어야 합니다.

```
    heroku apps:create your-app-name
    > Creating ⬢ your-app-name... done
    > https://your-app-name.herokuapp.com/ | https://git.heroku.com/your-app-name.git
```

Heroku 앱을 생성하면 Heroku가 만든 git remote가 로컬 저장소에 추가됩니다. 이 remote로 커밋을 푸시하면 배포가 트리거됩니다.

**Checkpoint:** `git remote -v`에서 애플리케이션의 Heroku git remote가 보여야 합니다.

```
    heroku https://git.heroku.com/your-app-name.git (fetch)
    heroku https://git.heroku.com/your-app-name.git (push)
```

`heroku` remote가 보이지 않으면 다음 명령으로 추가하세요.

```
    heroku git:remote --app your-app-name
```

## 5\. 애플리케이션에 PostgreSQL 데이터베이스 추가

Heroku에서는 애플리케이션의 일부로 PostgreSQL 데이터베이스를 프로비저닝할 수 있습니다.

다음 명령으로 데이터베이스를 생성합니다.

```
    heroku addons:create heroku-postgresql:hobby-dev
```

**Checkpoint:** 데이터베이스가 생성되었는지 확인하려면 다음과 같은 출력이 보여야 합니다.

```
    Creating heroku-postgresql:hobby-dev on ⬢ your-app-name... free
    Database has been created and is available
     ! This database is empty. If upgrading, you can transfer
     ! data from another database with pg:copy
    Created postgresql-parallel-73780 as DATABASE_URL
```

> **Note:** 앱이 Heroku에서 실행될 때 Heroku는 `DATABASE_URL` 환경 변수를 자동으로 설정합니다. Prisma schema(`prisma/schema.prisma`)의 _datasource_ 블록에서 `env("DATABASE_URL")`로 선언되어 있으므로 Prisma ORM은 이 환경 변수를 사용합니다.

## 6\. 푸시하여 배포

변경 사항을 Heroku 앱 저장소로 푸시하여 앱을 배포합니다.

```
    git push heroku main
```

이렇게 하면 빌드가 트리거되고 애플리케이션이 Heroku에 배포됩니다. 또한 Heroku는 `npx prisma migrate deploy` 명령을 실행해 앱 배포 전에 데이터베이스 스키마 생성을 위한 마이그레이션을 수행합니다(`Procfile`의 `release` 단계에 정의됨).

**Checkpoint:** `git push`는 빌드 및 release phase 로그를 출력하고 배포된 앱 URL을 표시해야 합니다.

```
    remote: -----> Launching...
    remote:  !     Release command declared: this new release will not be available until the command succeeds.
    remote:        Released v5
    remote:        https://your-app-name.herokuapp.com/ deployed to Heroku
    remote:
    remote: Verifying deploy... done.
    remote: Running release command...
    remote:
    remote: Prisma schema loaded from prisma/schema.prisma
    remote: Datasource "db": PostgreSQL database "your-db-name", schema "public" at "your-db-host.compute-1.amazonaws.com:5432"
    remote:
    remote: 1 migration found in prisma/migrations
    remote:
    remote: The following migration have been applied:
    remote:
    remote: migrations/
    remote:   └─ 20210310152103_init/
    remote:     └─ migration.sql
    remote:
    remote: All migrations have been successfully applied.
    remote: Waiting for release.... done.
```

> **Note:** Heroku는 애플리케이션이 바인딩할 `PORT` 환경 변수도 설정합니다.

## 7\. 배포된 애플리케이션 테스트

정적 프런트엔드를 사용해 preview URL을 통해 배포한 API와 상호작용할 수 있습니다.

브라우저에서 preview URL을 열어보세요. URL은 `https://APP_NAME.herokuapp.com` 형태여야 합니다. 다음 화면이 표시됩니다.

![브라우저에서 Check API status, Seed data, Load feed 버튼이 보이는 배포된 Prisma 앱 프런트엔드.](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/heroku-deployed.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

버튼을 사용하면 REST API에 요청을 보내고 응답을 확인할 수 있습니다.

- **Check API status** : `{"up":true}`를 반환하는 REST API 상태 엔드포인트를 호출합니다.
- **Seed data** : 테스트용 `user`와 `post`를 데이터베이스에 시드합니다. 생성된 사용자들을 반환합니다.
- **Load feed** : 데이터베이스의 모든 `users`를 관련 `profiles`와 함께 로드합니다.

Prisma Client API를 더 자세히 보려면 `src/index.js` 파일의 라우트 핸들러를 확인하세요.

`heroku logs --tail` 명령으로 애플리케이션 로그를 볼 수 있습니다.

```
    2020-07-07T14:39:07.396544+00:00 app[web.1]:
    2020-07-07T14:39:07.396569+00:00 app[web.1]: > prisma-heroku@1.0.0 start /app
    2020-07-07T14:39:07.396569+00:00 app[web.1]: > node src/index.js
    2020-07-07T14:39:07.396570+00:00 app[web.1]:
    2020-07-07T14:39:07.657505+00:00 app[web.1]: 🚀 Server ready at: http://localhost:12516
    2020-07-07T14:39:07.657526+00:00 app[web.1]: ⭐️ See sample requests: http://pris.ly/e/ts/rest-express#3-using-the-rest-api
    2020-07-07T14:39:07.842546+00:00 heroku[web.1]: State changed from starting to up
```

## Heroku 관련 참고 사항

이 가이드에서 다루는 Heroku 관련 구현 세부 사항 중 다시 강조할 만한 내용은 다음과 같습니다.

- **포트 바인딩** : 웹 서버는 연결을 수락하기 위해 포트에 바인딩합니다. Heroku에 배포하면 `PORT` 환경 변수는 Heroku가 설정합니다. 배포 후 애플리케이션이 요청을 받을 수 있도록 `process.env.PORT`에 바인딩해야 합니다. 일반적인 패턴은 먼저 `process.env.PORT` 바인딩을 시도하고, 실패하면 미리 정한 포트를 사용하는 것입니다.

```
    const PORT = process.env.PORT || 3000;
    const server = app.listen(PORT, () => {
      console.log(`app running on port ${PORT}`);
    });
```

- **데이터베이스 URL** : Heroku 프로비저닝 과정의 일부로 `DATABASE_URL` config var가 앱 설정에 추가됩니다. 여기에는 앱이 데이터베이스에 접근할 때 사용할 URL이 들어 있습니다. Prisma Client가 데이터베이스에 성공적으로 연결할 수 있도록 `schema.prisma` 파일에서 `env("DATABASE_URL")`을 사용해야 합니다.

- **SSL 인증서 검증 비활성화** : `PrismaPg` 어댑터를 `DATABASE_URL`과 함께 사용할 때는 [Heroku 가이드라인](https://devcenter.heroku.com/articles/connecting-heroku-postgres#connecting-in-node-js)에 따라 SSL 인증서 검증을 비활성화해야 합니다. 그렇지 않으면 `P1010 DriverAdapterError: DatabaseAccessDenied` 오류가 발생할 수 있습니다. 데이터베이스가 로컬인지 Heroku에서 호스팅되는지에 따라 조건부로 처리할 수 있습니다.

```
    const isSecureDb = !process.env.DATABASE_URL.includes("@127.0.0.1");

    export const db = new PrismaClient({
      adapter: new PrismaPg({
        connectionString: process.env.DATABASE_URL + (isSecureDb ? `?sslmode=no-verify` : ""),
      }),
    });
```

## 요약

축하합니다! Prisma ORM을 사용한 Node.js 앱을 Heroku에 성공적으로 배포했습니다.

예제 소스 코드는 [이 GitHub 저장소](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/heroku)에서 확인할 수 있습니다.

Prisma Client API를 더 자세히 보려면 `src/index.js` 파일의 라우트 핸들러를 확인하세요.
