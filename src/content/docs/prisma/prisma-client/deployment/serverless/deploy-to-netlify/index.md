---
title: "Netlify에 배포하기"
description: "Prisma Client를 사용하는 Node.js 및 TypeScript 애플리케이션을 Netlify에 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify

# Netlify에 배포하기

마크다운 복사열기

Prisma Client를 사용하는 Node.js 및 TypeScript 애플리케이션을 Netlify에 배포하는 방법을 알아보세요.

이 가이드는 Prisma ORM을 사용하는 애플리케이션을 [Netlify](https://www.netlify.com/)에 배포하기 위해 필요한 단계를 설명합니다.

Netlify는 지속적 배포, 정적 사이트, 서버리스 함수를 위한 클라우드 플랫폼입니다. Netlify는 GitHub와 원활하게 통합되어 커밋 시 자동 배포를 수행합니다. 아래 단계를 따르면 이 방식을 사용해 GitHub 리포지토리에서 애플리케이션을 배포하는 CI/CD 파이프라인을 만들게 됩니다.

## 사전 준비

이 가이드를 진행하기 전에 Netlify 배포를 시작할 수 있도록 애플리케이션을 설정해야 합니다. 빠른 개요는 ["Get started with Netlify"](https://docs.netlify.com/get-started/) 가이드를, 배포 옵션의 심화 내용은 ["Deploy functions"](https://docs.netlify.com/functions/deploy/?fn-language=ts)를 권장합니다.

## Netlify에 환경 변수 저장하기

민감한 연결 문자열 유출을 방지하기 위해 `.env` 파일을 `.gitignore`에 유지하는 것을 권장합니다. 대신 Netlify CLI를 사용해 [값을 netlify로 직접 가져올 수 있습니다](https://docs.netlify.com/environment-variables/get-started/#import-variables-with-the-netlify-cli).

다음과 같은 파일이 있다고 가정해 보겠습니다.

.env

```
    # Connect to DB
    DATABASE_URL="postgresql://postgres:__PASSWORD__@__HOST__:__PORT__/__DB_NAME__"
```

`env:import` 명령으로 해당 파일을 환경 변수로 업로드할 수 있습니다.

```
    netlify env:import .env
```

```
    site: my-very-very-cool-site
    ---------------------------------------------------------------------------------.
                             Imported environment variables                          |
    ---------------------------------------------------------------------------------|
         Key      |                              Value                               |
    --------------|------------------------------------------------------------------|
     DATABASE_URL | postgresql://postgres:__PASSWORD__@__HOST__:__PORT__/__DB_NAME__ |
    ---------------------------------------------------------------------------------'
```

`.env` 파일을 사용하지 않는 경우

데이터베이스 연결 문자열 및 기타 환경 변수를 다른 방식으로 저장하고 있다면, 환경 변수를 Netlify에 수동으로 업로드해야 합니다. 이 옵션들은 [Netlify 문서](https://docs.netlify.com/environment-variables/get-started/)에서 설명되어 있으며, 그중 하나인 UI를 통한 업로드 방법을 아래에 소개합니다.

1. 사이트의 Netlify 관리자 UI를 엽니다. 다음과 같이 Netlify CLI를 사용할 수 있습니다.

```
netlify open --admin
```

2. **Site settings**를 클릭합니다. : ![Netlify admin UI](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/serverless/images/500-06-deploy-to-netlify-site-settings.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)
3. 왼쪽 사이드바에서 **Build & deploy**로 이동한 뒤 **Environment**를 선택합니다.
4. **Edit variables**를 클릭하고 키가 `DATABASE_URL`인 변수를 만든 다음, 값으로 데이터베이스 연결 문자열을 설정합니다. ![Netlify environment variables](https://docs.prisma.io/docs/img/orm/prisma-client/deployment/serverless/images/500-07-deploy-to-netlify-environment-variables-settings.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)
5. **Save**를 클릭합니다.

이제 새로 업로드한 환경 변수를 새 빌드에서 사용할 수 있도록 Netlify 빌드 및 배포를 새로 시작하세요.

```
    netlify deploy
```

이제 배포된 애플리케이션을 테스트할 수 있습니다.

## 연결 풀링

Netlify 같은 Function-as-a-Service 제공자를 사용할 때는 성능상의 이유로 데이터베이스 연결 풀링이 유리합니다. 함수가 호출될 때마다 데이터베이스에 새 연결이 생성될 수 있으며, 이로 인해 사용 가능한 연결 수가 빠르게 소진될 수 있기 때문입니다.

기본 연결 풀링이 내장된 [Prisma Postgres](https://docs.prisma.io/docs/postgres)를 사용하면 Prisma Client 번들 크기를 줄이고 콜드 스타트를 피할 수 있습니다.

서버리스 환경의 연결 관리에 대한 자세한 내용은 [연결 관리 가이드](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)를 참고하세요.
