---
title: "Prisma Migrate로 데이터베이스 변경 사항 배포하기"
description: "Prisma Migrate로 데이터베이스 변경 사항을 배포하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate

# Prisma Migrate로 데이터베이스 변경 사항 배포하기

Prisma Migrate로 데이터베이스 변경 사항을 배포하는 방법을 알아보세요.

스테이징, 테스트 또는 프로덕션 환경에 대기 중인 마이그레이션을 적용하려면 CI/CD 파이프라인의 일부로 `migrate deploy` 명령을 실행하세요.

npm

pnpm

yarn

bun

```
    npx prisma migrate deploy
```

이 가이드는 **MongoDB에는 적용되지 않습니다**.
MongoDB에서는 `migrate deploy` 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다. 자세한 내용은 [MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)를 참고하세요.

`prisma migrate deploy`를 정확히 언제 실행할지는 플랫폼에 따라 다릅니다. 예를 들어, 단순화된 [Heroku](https://docs.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku) 워크플로에는 다음이 포함됩니다.

1. `./prisma/migration` 폴더가 소스 제어에 포함되어 있는지 확인
2. [release phase](https://devcenter.heroku.com/articles/release-phase) 동안 `prisma migrate deploy` 실행

이상적으로는 `migrate deploy`를 자동화된 CI/CD 파이프라인에 포함해야 하며, 일반적으로 프로덕션 데이터베이스에 변경 사항을 배포하기 위해 이 명령을 로컬에서 실행하는 것은 권장하지 않습니다(예: `DATABASE_URL` 환경 변수를 일시적으로 변경하는 방식). 일반적으로 프로덕션 데이터베이스 URL을 로컬에 저장하는 것은 좋은 관행으로 간주되지 않습니다.

`prisma migrate deploy` 명령을 실행하려면 보통 `devDependencies`에 추가되는 `prisma` 의존성에 접근할 수 있어야 한다는 점에 유의하세요. Vercel 같은 일부 플랫폼은 빌드 중 개발 의존성을 제거(prune)하므로 이 명령을 호출할 수 없게 됩니다. 이 문제는 `package.json`에서 `prisma`를 `dependencies`로 옮겨 프로덕션 의존성으로 만들면 해결할 수 있습니다. `migrate deploy` 명령에 대한 자세한 내용은 다음을 참고하세요.

- `migrate deploy` reference
- `migrate deploy`의 동작 방식
- 프로덕션 문제 해결

## GitHub Actions를 사용하여 데이터베이스 변경 사항 배포하기

CI/CD의 일부로 파이프라인에서 `prisma migrate deploy`를 실행하여 프로덕션 데이터베이스에 대기 중인 마이그레이션을 적용할 수 있습니다.

다음은 데이터베이스에 대해 마이그레이션을 실행하는 예시 액션입니다.

deploy.yml

```
    name: Deploy
    on:
      push:
        paths:
          - prisma/migrations/**
        branches:
          - main

    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repo
            uses: actions/checkout@v3
          - name: Setup Node
            uses: actions/setup-node@v3
          - name: Install dependencies
            run: npm install
          - name: Apply all pending migrations to the database
            run: npx prisma migrate deploy
            env:
              DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

강조된 줄은 `prisma/migrations` 디렉터리에 변경 사항이 있을 때만 이 액션이 실행된다는 것을 보여줍니다. 따라서 `npx prisma migrate deploy`도 마이그레이션이 업데이트될 때에만 실행됩니다.

연결 문자열을 따옴표로 감싸지 않은 상태로 `DATABASE_URL` 변수를 [리포지토리 시크릿으로 설정](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)했는지 확인하세요.
