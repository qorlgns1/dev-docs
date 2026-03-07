---
title: "Sevalla에 배포하기"
description: "Prisma ORM을 사용하는 Node.js 서버를 Sevalla에 배포하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-sevalla

# Sevalla에 배포하기

Prisma ORM을 사용하는 Node.js 서버를 Sevalla에 배포하는 방법을 알아보세요

이 가이드는 Prisma ORM과 PostgreSQL을 사용하는 Node.js 서버를 [Sevalla](https://sevalla.com)에 배포하는 방법을 설명합니다. 이 앱은 REST API를 노출하며, PostgreSQL 데이터베이스를 조회하기 위해 Prisma Client를 사용합니다. 앱과 데이터베이스는 모두 Sevalla에서 호스팅됩니다.

Sevalla는 애플리케이션 및 서버 배포를 단순화하도록 설계된 개발자 중심 PaaS 플랫폼입니다. 애플리케이션, 데이터베이스, 오브젝트 스토리지, 정적 사이트를 쉽게 호스팅할 수 있습니다.

Git 기반 배포, Dockerfiles, Procfiles를 지원하며 Google Kubernetes Engine에서 실행되고 Cloudflare를 통해 전역 전달을 제공합니다.

이 예제를 위해 알아두면 좋은 내용:

- Sevalla는 내장 오토스케일링과 유연한 pod 크기를 갖춘 장기 실행 “serverful” 애플리케이션을 지원합니다.
- Git 기반 배포는 GitHub, GitLab, Bitbucket과 통합됩니다.
- PostgreSQL, MySQL, MariaDB, Redis, Valkey 데이터베이스를 네이티브로 지원합니다.
- 애플리케이션과 데이터베이스는 자동 환경 변수 주입과 함께 프라이빗 네트워킹을 통해 안전하게 연결할 수 있습니다.

## 사전 준비

시작하려면 다음만 있으면 됩니다:

- [Sevalla 계정](https://sevalla.com) (무료 크레딧 $50 제공)
- 애플리케이션 코드가 있는 GitHub 리포지토리

> **참고:** 아직 준비된 프로젝트가 없다면 [Prisma 예제 프로젝트](https://github.com/sevalla-templates/express-prisma-demo)를 사용할 수 있습니다. Prisma ORM을 사용하는 간단한 Express.js 애플리케이션으로, REST API, 엔드포인트 테스트용 프런트엔드, 마이그레이션이 포함된 정의된 Prisma 스키마, 선택적 데이터베이스 시딩 스크립트를 포함합니다.

## Sevalla에서 앱 생성하기

먼저 Sevalla 대시보드에서 새 애플리케이션을 생성합니다. 사이드바에서 **Applications**를 클릭한 다음 아래와 같이 **Create an app** 버튼을 클릭합니다.

![Sevalla 앱 생성 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-app-creation.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

다음으로 Git 리포지토리를 선택합니다. Sevalla는 비공개 및 공개 리포지토리 모두에서 배포를 지원합니다. 예제 프로젝트를 사용하는 경우 포크할 필요 없이 URL `https://github.com/sevalla-templates/express-prisma-demo`를 입력하면 됩니다.

![Sevalla의 리포지토리 선택 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-choose-repository.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

적절한 브랜치(보통 `main` 또는 `master`)를 선택하고, 애플리케이션 이름을 설정하고, 원하는 배포 리전을 선택한 뒤, pod 크기를 고릅니다. (무료 크레딧으로 0.5 CPU / 1GB RAM부터 시작할 수 있습니다)

![Sevalla의 애플리케이션 이름 설정 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-name-application.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

**Create**를 클릭하되, 아직 데이터베이스를 추가하지 않았으므로 실패하지 않도록 지금은 배포 단계는 건너뛰세요.

## Sevalla에서 데이터베이스 설정하기

Sevalla 대시보드에서 **Databases** > **Add database**를 클릭합니다. **PostgreSQL**(또는 원하는 구성된 데이터베이스 유형)을 선택한 다음 데이터베이스 이름, 사용자 이름, 비밀번호를 입력하거나 기본으로 생성된 정보를 그대로 사용합니다.

![Sevalla의 데이터베이스 생성 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-create-database.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

다음으로 Sevalla 대시보드에서 쉽게 식별할 수 있도록 데이터베이스에 알아보기 쉬운 이름을 지정합니다. 애플리케이션과 **같은 리전**을 선택했는지 확인하고, 적절한 데이터베이스 크기를 고른 뒤 **Create**를 클릭합니다.

데이터베이스가 생성되면 아래로 스크롤하여 **Connected Applications** 섹션에서 **Add Connection**을 클릭합니다.

앞에서 생성한 애플리케이션을 선택하고 "Add environment variables"를 활성화합니다. 변수 이름이 `DATABASE_URL`로 설정되어 있는지 확인하세요 (`DB_URL`로 기본 설정되어 있다면 알맞게 변경하세요).

![Sevalla의 앱 내부 연결 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-app-internal-connection.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

마지막으로 **Add connection**을 클릭합니다. 이렇게 하면 애플리케이션이 데이터베이스와 안전하게 연결되고 필요한 환경 변수가 구성됩니다.

## 배포 트리거

이제 애플리케이션과 데이터베이스가 연결되었으므로 애플리케이션의 **Deployment** 탭으로 돌아가 **Deploy**를 클릭합니다.

> **참고:** Sevalla는 Nixpacks를 사용해 애플리케이션을 자동으로 빌드하며, 프로젝트의 `package.json`과 `start` 스크립트를 감지합니다. Dockerfile 또는 Buildpacks를 사용하고 싶다면 **Settings** > **Build**로 이동한 뒤 **Build environment** 섹션의 **Update Settings**를 클릭해 빌드 방식을 사용자 지정하세요.

## 데이터베이스 시드(선택 사항)

프로젝트에 시드 스크립트(일반적으로 `prisma/seed.js` 위치)가 포함되어 있다면, 애플리케이션 배포 후 초기 데이터 또는 데모 데이터로 데이터베이스를 채울 수 있습니다.

이렇게 하려면 애플리케이션의 **Web Terminal**(**Applications** > **[Your App]** > **Web Terminal**)로 이동해 다음 명령을 실행합니다:

npm

pnpm

yarn

bun

```
    npx prisma db seed
```

웹 터미널은 다음과 같이 보입니다:

![Sevalla 웹 터미널 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-web-terminal.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

이 작업이 완료되면 Sevalla의 내장 인터랙티브 스튜디오를 통해 데이터베이스를 직접 관리하고 상호작용할 수 있습니다. 아래와 같이 시드된 데이터를 확인할 수 있습니다:

![Sevalla 데이터베이스 스튜디오 인터페이스](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-database-studio.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

축하합니다! Prisma ORM을 사용하는 Node.js 애플리케이션을 Sevalla에 성공적으로 배포했습니다. 이제 앱과 데이터베이스가 연결되었고, 보안이 적용되었으며, 프로덕션 준비가 완료되었습니다!
