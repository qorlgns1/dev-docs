---
title: "Koyeb에 배포하기"
description: "Prisma ORM을 사용하는 Node.js 서버를 Koyeb Serverless Platform에 배포하는 방법을 알아봅니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-koyeb

# Koyeb에 배포하기

Prisma ORM을 사용하는 Node.js 서버를 Koyeb Serverless Platform에 배포하는 방법을 알아봅니다.

이 가이드에서는 PostgreSQL과 함께 Prisma ORM을 사용하는 Node.js 서버를 [Koyeb](https://www.koyeb.com/)에 설정하고 배포합니다. 이 애플리케이션은 REST API를 노출하며, Prisma Client를 사용해 데이터베이스에서 레코드를 조회, 생성, 삭제합니다.

Koyeb은 앱을 전 세계에 배포할 수 있도록 돕는 개발자 친화적인 서버리스 플랫폼입니다. 이 플랫폼은 git 기반 배포, TLS 암호화, 네이티브 오토스케일링, 글로벌 엣지 네트워크, 내장 서비스 메시 및 서비스 디스커버리를 통해 Docker 컨테이너, 웹 앱, API를 매끄럽게 실행할 수 있게 해줍니다.

[Koyeb git 기반 배포](https://www.koyeb.com/docs/build-and-deploy/build-from-git) 방식을 사용하면 GitHub 저장소에 코드 변경 사항을 푸시할 때마다 Koyeb Serverless Platform에서 새 빌드와 배포가 자동으로 트리거됩니다. 이 가이드에서는 후자의 접근 방식을 사용하며, 앱의 GitHub 저장소에 코드를 푸시하게 됩니다.

이 애플리케이션은 다음 구성 요소로 이루어져 있습니다.

- **Backend** : Express.js로 구축된 Node.js REST API로, 리소스 엔드포인트가 Prisma Client를 사용해 PostgreSQL 데이터베이스(예: Heroku에 호스팅) 대상 데이터베이스 작업을 처리합니다.
- **Frontend** : API와 상호작용하기 위한 정적 HTML 페이지.

![Prisma Client가 포함된 Node.js 백엔드, 정적 프론트엔드, PostgreSQL 데이터베이스를 보여주는 Koyeb 배포 아키텍처 다이어그램.](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/koyeb-architecture.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

이 가이드의 핵심은 Prisma ORM을 사용하는 프로젝트를 Koyeb에 배포하는 방법을 보여주는 것입니다. 시작점은 [Prisma Koyeb 예제](https://github.com/koyeb/example-prisma)이며, 여기에는 사전 구성된 REST 엔드포인트 몇 개와 간단한 프론트엔드를 갖춘 Express.js 서버가 포함되어 있습니다.

> **참고:** 가이드 전반에 있는 다양한 **체크포인트**를 통해 단계를 올바르게 수행했는지 검증할 수 있습니다.

## 사전 준비 사항

- 접근 가능한 URL이 있는 호스팅 PostgreSQL 데이터베이스(예: `postgresql://username:password@your_postgres_db.cloud.com/db_identifier`)가 필요합니다. [무료 플랜](https://dev.to/prisma/set-up-a-free-postgresql-database-on-supabase-to-use-with-prisma-3pk6)을 제공하는 Supabase를 사용할 수 있습니다.
- 코드를 푸시하는 데 사용할 비어 있는 공개 저장소를 가진 [GitHub](https://github.com) 계정
- [Koyeb](https://www.koyeb.com) 계정
- 설치된 Node.js

## Prisma ORM 워크플로

Prisma ORM의 핵심에는 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)가 있습니다. 이는 데이터 모델과 Prisma ORM 관련 기타 설정을 정의하는 선언적 구성입니다. Prisma schema는 Prisma Client와 Prisma Migrate 모두의 단일 진실 공급원(single source of truth)이기도 합니다.

이 가이드에서는 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용해 데이터베이스 스키마를 생성합니다. Prisma Migrate는 Prisma schema를 기반으로 하며, 데이터베이스에 실행되는 `.sql` 마이그레이션 파일을 생성하는 방식으로 동작합니다.

Migrate에는 두 가지 주요 워크플로가 있습니다.

- `prisma migrate dev`로 로컬 개발 중 마이그레이션 생성 및 적용
- `prisma migrate deploy`로 프로덕션에 생성된 마이그레이션 적용

간결성을 위해 이 가이드는 `prisma migrate dev`로 마이그레이션을 생성하는 방법은 다루지 않습니다. 대신 프로덕션 워크플로에 집중하며, 예제 코드에 포함된 Prisma schema와 SQL 마이그레이션을 사용합니다.

Koyeb의 [build step](https://www.koyeb.com/docs/build-and-deploy/build-from-git#the-buildpack-build-process)을 사용해 `prisma migrate deploy` 명령을 실행하여 애플리케이션 시작 전에 마이그레이션이 적용되도록 할 것입니다.

Prisma Migrate로 마이그레이션을 생성하는 방법을 더 알아보려면 [처음부터 시작하기 가이드](https://docs.prisma.io/docs/prisma-orm/quickstart/postgresql)를 확인하세요.

## 1\. 예제 다운로드 및 의존성 설치

터미널을 열고 원하는 위치로 이동합니다. 애플리케이션 코드를 담을 디렉터리를 만들고 예제 코드를 다운로드합니다.

```
    mkdir prisma-on-koyeb
    cd prisma-on-koyeb
    curl https://github.com/koyeb/example-prisma/tarball/main/latest | tar xz  --strip=1
```

**체크포인트:** `tree` 명령을 실행하면 다음 디렉터리와 파일이 표시되어야 합니다.

```
    .
    ├── README.md
    ├── package.json
    ├── prisma
    │   ├── migrations
    │   │   ├── 20210310152103_init
    │   │   │   └── migration.sql
    │   │   └── migration_lock.toml
    │   └── schema.prisma
    ├── public
    │   └── index.html
    └── src
        └── index.js

    5 directories, 8 files
```

의존성을 설치합니다.

npm

pnpm

yarn

bun

```
    npm install
```

## 2\. Git 저장소 초기화 및 GitHub로 애플리케이션 코드 푸시

이전 단계에서 코드를 다운로드했습니다. 이 단계에서는 배포를 위해 GitHub 저장소로 푸시할 수 있도록 코드로부터 저장소를 생성합니다.

이를 위해 소스 코드 폴더에서 `git init`을 실행합니다.

```
    git init
    > Initialized empty Git repository in /Users/edouardb/prisma-on-koyeb/.git/
```

저장소가 초기화되면 파일을 추가하고 커밋합니다.

```
    git add .
    git commit -m 'Initial commit'
```

**체크포인트:** `git log -1`을 실행하면 다음 커밋이 표시되어야 합니다.

```
    git log -1
    commit 895534590fdd260acee6396e2e1c0438d1be7fed (HEAD -> main)
```

그런 다음 원격 저장소를 추가해 GitHub 저장소로 코드를 푸시합니다.

```
    git remote add origin git@github.com:<YOUR_GITHUB_USERNAME>/<YOUR_GITHUB_REPOSITORY_NAME>.git
    git push -u origin main
```

## 3\. Koyeb에 애플리케이션 배포

[Koyeb Control Panel](https://app.koyeb.com)에서 **Create App** 버튼을 클릭합니다.

Koyeb 앱 생성 페이지로 이동하면 배포 방식, 저장소 URL, 배포할 브랜치, 실행할 빌드/실행 명령 등 배포할 애플리케이션 정보를 입력하라는 안내가 표시됩니다.

배포 방식으로 GitHub를 선택하고 애플리케이션이 있는 GitHub 저장소를 선택한 뒤, 배포 브랜치를 `main`으로 설정합니다.

> **참고:** Koyeb을 처음 사용하는 경우 GitHub 계정에 Koyeb 앱 설치를 요청받게 됩니다.

**Environment variables** 섹션에서 `DATABASE_URL`이라는 새 환경 변수를 Secret 타입으로 생성합니다. 값 필드에서 **Create Secret** 을 클릭하고 시크릿 이름을 `prisma-pg-url`로 지정한 다음 PostgreSQL 데이터베이스 연결 문자열을 시크릿 값으로 설정합니다. 형식은 다음과 같아야 합니다: `postgresql://__USER__:__PASSWORD__@__HOST__/__DATABASE__`. [Koyeb Secrets](https://www.koyeb.com/docs/reference/secrets)는 API 토큰, 데이터베이스 연결 문자열 같은 민감한 정보를 안전하게 저장하고 조회할 수 있게 해줍니다. 하드코딩된 자격 증명을 제거해 코드를 안전하게 만들고, 애플리케이션에 환경 변수를 안전하게 전달할 수 있습니다.

마지막으로 애플리케이션 이름을 지정하고 **Create App** 버튼을 클릭합니다.

**체크포인트:** 배포된 앱의 스크린샷을 클릭해 앱을 엽니다. 페이지가 로드되면 **Check API status** 버튼을 클릭했을 때 `{"up":true}`가 반환되어야 합니다.

![환경 변수 설정 및 Create App 버튼을 보여주는 Koyeb 앱 생성 인터페이스.](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/koyeb-app-creation.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

축하합니다! Koyeb에 앱을 성공적으로 배포했습니다.

Koyeb이 애플리케이션을 빌드하고 배포합니다. 이후 GitHub 저장소에 추가 커밋을 푸시하면 Koyeb에서 새 빌드와 배포가 트리거됩니다.

**체크포인트:** 빌드와 배포가 완료되면 Koyeb 제어판에서 `koyeb.app`으로 끝나는 App URL을 클릭해 애플리케이션에 접속할 수 있습니다. 앱 페이지가 로드된 뒤 **Check API status** 버튼을 클릭하면 `{"up":true}`가 반환되어야 합니다.

## 4\. 배포된 애플리케이션 테스트

프리뷰 URL을 통해 배포한 API와 상호작용하려면 정적 프론트엔드를 사용할 수 있습니다.

브라우저에서 프리뷰 URL을 엽니다. URL은 `https://APP_NAME-ORG_NAME.koyeb.app`와 같은 형태여야 합니다. 다음과 같은 화면이 보여야 합니다.

![브라우저에서 Check API status, Seed data, Load feed 버튼을 보여주는 배포된 Prisma 앱 프론트엔드.](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/koyeb-deployed.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

버튼을 사용해 REST API에 요청을 보내고 응답을 확인할 수 있습니다.

- **Check API status** : REST API 상태 엔드포인트를 호출하며 `{"up":true}`를 반환합니다.
- **Seed data** : 테스트 `user`와 `post`를 데이터베이스에 시드합니다. 생성된 users를 반환합니다.
- **Load feed** : 데이터베이스의 모든 `users`와 관련된 `profiles`를 로드합니다.

Prisma Client API를 더 자세히 보려면 `src/index.js` 파일의 라우트 핸들러를 확인하세요.

Koyeb 제어판에서 앱 서비스의 `Runtime logs` 탭을 클릭하면 애플리케이션 로그를 볼 수 있습니다.

```
    node-72d14691	stdout	> prisma-koyeb@1.0.0 start
    node-72d14691	stdout	> node src/index.js
    node-72d14691	stdout	🚀 Server ready at: http://localhost:8080
    node-72d14691	stdout	⭐️ See sample requests: http://pris.ly/e/ts/rest-express#3-using-the-rest-api
```

## Koyeb 관련 참고 사항

- 빌드

기본적으로 Node.js 런타임을 사용하는 애플리케이션에서 `package.json`에 `build` 스크립트가 있으면 Koyeb이 의존성 설치 후 이를 자동으로 실행합니다. 예제에서는 `build` 스크립트로 `prisma generate && prisma migrate deploy && next build`를 실행합니다.

- 배포

기본적으로 Node.js 런타임을 사용하는 애플리케이션에서 `package.json`에 `start` 스크립트가 있으면 Koyeb이 애플리케이션 실행을 위해 이를 자동으로 실행합니다. 예제에서는 `start` 스크립트로 `node src/index.js`를 실행합니다.

- 데이터베이스 마이그레이션 및 배포

배포한 예제에서는 Koyeb 빌드 중 `prisma migrate deploy` 명령으로 마이그레이션을 적용합니다(`package.json`의 `build` 스크립트에 정의됨).

- 추가 참고 사항

이 가이드에서는 리전, 인스턴스 크기, 수평 확장에 대해 사전 설정된 값을 유지했습니다. 필요에 따라 사용자 지정할 수 있습니다.

> **참고:** Ports 섹션은 애플리케이션이 어떤 포트에서 수신 대기하는지 Koyeb에 알려 들어오는 HTTP 요청을 올바르게 라우팅하기 위해 사용됩니다. 새 애플리케이션 생성 시 기본 `PORT` 환경 변수는 `8080`으로 설정되며, 들어오는 HTTP 요청은 `/` 경로로 라우팅됩니다. 애플리케이션이 다른 포트에서 수신 대기한다면, 들어오는 HTTP 요청을 라우팅할 다른 포트를 정의할 수 있습니다.

## 요약

축하합니다! Prisma ORM을 사용하는 Node.js 앱을 Koyeb에 성공적으로 배포했습니다.

예제의 소스 코드는 [이 GitHub 저장소](https://github.com/koyeb/example-prisma)에서 확인할 수 있습니다.

Prisma Client API를 더 자세히 보려면 `src/index.js` 파일의 라우트 핸들러를 확인하세요.
