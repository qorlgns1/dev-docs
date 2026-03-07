---
title: "AWS 플랫폼에 배포할 때의 주의사항"
description: "AWS 플랫폼에 배포할 때 알려진 주의사항"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/caveats-when-deploying-to-aws-platforms

# AWS 플랫폼에 배포할 때의 주의사항

AWS 플랫폼에 배포할 때 알려진 주의사항

다음은 서로 다른 AWS 플랫폼에 배포할 때 마주칠 수 있는 몇 가지 주의사항입니다.

## AWS RDS Proxy

Prisma ORM은 AWS RDS Proxy와 호환됩니다. 하지만 RDS Proxy가 연결을 고정(pin)하는 방식 때문에 Prisma ORM에서 커넥션 풀링 용도로 사용해도 이점이 없습니다.

> "프록시에 대한 연결은 pinning으로 알려진 상태에 들어갈 수 있습니다. 연결이 고정되면 세션이 종료될 때까지 이후의 각 트랜잭션은 동일한 기본 데이터베이스 연결을 사용합니다. 세션이 종료될 때까지 다른 클라이언트 연결도 해당 데이터베이스 연결을 재사용할 수 없습니다. Prisma Client의 연결이 끊기면 세션이 종료됩니다." - [AWS RDS Proxy Docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html)

[Prepared statements (크기에 관계없음) 또는 16 KB를 초과하는 쿼리 문은 RDS Proxy가 세션을 고정하도록 만듭니다.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-pinning.html) Prisma ORM은 모든 쿼리에 prepared statements를 사용하므로, Prisma ORM과 함께 RDS Proxy를 사용해도 이점을 얻을 수 없습니다.

## AWS Elastic Beanstalk

AWS Elastic Beanstalk는 인프라를 추상화하고 애플리케이션을 AWS에 빠르게 배포할 수 있게 해주는 PaaS 형태의 배포 서비스입니다.

Prisma Client를 사용하는 앱을 AWS Elastic Beanstalk에 배포할 때, Prisma ORM은 Prisma Client 코드를 `node_modules`에 생성합니다. 이는 일반적으로 `package.json`에 정의된 `postinstall` 훅에서 수행됩니다.

Beanstalk는 `postinstall` 훅에서 파일 시스템 쓰기 기능을 제한하므로, 프로젝트 루트에 [`.npmrc`](https://docs.npmjs.com/cli/v6/configuring-npm/npmrc/) 파일을 만들고 다음 설정을 추가해야 합니다.

.npmrc

```
    unsafe-perm=true
```

`unsafe-perm`을 활성화하면 _npm_ 이 _root_ 로 실행되도록 강제되어 파일 시스템 접근 문제를 피할 수 있고, 그 결과 `postinstall` 훅의 `prisma generate` 명령이 코드를 생성할 수 있게 됩니다.

- Error: @prisma/client did not initialize yet

이 오류는 AWS Elastic Beanstalk가 `devDependencies`를 설치하지 않기 때문에 발생하며, 그 결과 Prisma CLI를 가져오지 못합니다. 이를 해결하려면 다음 중 하나를 선택할 수 있습니다.

1. `prisma` CLI 패키지를 `devDependencies` 대신 `dependencies`에 추가합니다. (`package-lock.json` 업데이트를 위해 이후 `npm install` 실행 필요)
2. 또는 AWS Elastic Beanstalk 인스턴스에서 `devDependencies`를 설치합니다. 이를 위해 AWS Elastic Beanstalk의 `NPM_USE_PRODUCTION` 환경 속성을 false로 설정해야 합니다.

## AWS RDS Postgres

Prisma ORM을 AWS RDS Postgres와 함께 사용할 때, 마이그레이션 중 또는 런타임에 연결 문제나 다음 오류가 발생할 수 있습니다.

```
    Error: P1010: User <username> was denied access on the database <database>
```

- 원인

AWS RDS는 기본적으로 SSL 연결을 강제하며, Prisma는 데이터베이스 연결 문자열을 `rejectUnauthorized: true`로 파싱하므로 유효한 SSL 인증서가 필요합니다. 인증서가 올바르게 구성되지 않으면 Prisma가 데이터베이스에 연결할 수 없습니다.

- 해결 방법

이 문제를 해결하려면 `DATABASE_URL` 환경 변수에 `sslmode=no-verify` 옵션이 포함되도록 업데이트하세요. 이렇게 하면 엄격한 SSL 인증서 검증을 우회하고 Prisma가 데이터베이스에 연결할 수 있습니다. `.env` 파일을 다음과 같이 업데이트하세요.

```
    DATABASE_URL=postgresql://<username>:<password>@<host>/<database>?sslmode=no-verify&schema=public
```

- 이 방식이 동작하는 이유

`sslmode=no-verify` 설정은 [pg-connection-string](https://github.com/brianc/node-postgres/blob/95d7e620ef8b51743b4cbca05dd3c3ce858ecea7/packages/pg-connection-string/README.md?plain=1#L71) 패키지를 통해 SSL 구성에 `rejectUnauthorized: false`를 전달합니다. 이로 인해 엄격한 인증서 검증이 비활성화되어 Prisma가 RDS 데이터베이스와 연결을 수립할 수 있습니다.

- 참고

`sslmode=no-verify` 사용은 빠른 해결책이 될 수 있지만, SSL 검증을 우회하므로 프로덕션 환경의 보안 요구사항을 충족하지 못할 수 있습니다. 이런 경우 유효한 SSL 인증서가 올바르게 구성되어 있는지 확인하세요.
