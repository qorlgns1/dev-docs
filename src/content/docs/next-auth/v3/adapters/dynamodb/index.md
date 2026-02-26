---
title: "DynamoDB"
description: "이것은 next-auth용 AWS DynamoDB Adapter입니다. 이 패키지는 기본 next-auth 패키지와 함께 사용할 때만 동작합니다. 독립형 패키지가 아닙니다."
---

Source URL: https://next-auth.js.org/v3/adapters/dynamodb

버전: v3

# DynamoDB

이것은 next-auth용 AWS DynamoDB Adapter입니다. 이 패키지는 기본 next-auth 패키지와 함께 사용할 때만 동작합니다. 독립형 패키지가 아닙니다.

`pk` 파티션 키와 `sk` 정렬 키를 가진 테이블이 필요합니다. 또한 테이블에는 `GSI1PK`를 파티션 키로, `GSI1SK`를 정렬 키로 사용하는 `GSI1`이라는 글로벌 보조 인덱스가 필요합니다. 테이블 이름과 과금 방식은 원하는 대로 설정할 수 있습니다.

전체 스키마는 아래 테이블 구조 섹션에서 확인할 수 있습니다.

## 시작하기[​](https://next-auth.js.org/v3/adapters/dynamodb#getting-started "제목으로 바로 가는 링크")

1. `next-auth`와 `@next-auth/dynamodb-adapter@canary`를 설치합니다.

```
    npm install next-auth @next-auth/dynamodb-adapter@canary

```

2. 이 어댑터를 `pages/api/auth/[...nextauth].js` next-auth 설정 객체에 추가합니다.

어댑터에 `aws-sdk`의 `DocumentClient` 인스턴스를 전달해야 합니다. 기본 테이블 이름은 `next-auth`이지만, 어댑터의 두 번째 파라미터로 `{ tableName: 'your-table-name' }`를 전달해 변경할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import AWS from "aws-sdk";
    import NextAuth from "next-auth";
    import Providers from "next-auth/providers";
    import { DynamoDBAdapter } from "@next-auth/dynamodb-adapter"

    AWS.config.update({
      accessKeyId: process.env.NEXT_AUTH_AWS_ACCESS_KEY,
      secretAccessKey: process.env.NEXT_AUTH_AWS_SECRET_KEY,
      region: process.env.NEXT_AUTH_AWS_REGION,
    });

    export default NextAuth({
      // Configure one or more authentication providers
      providers: [
        Providers.GitHub({
          clientId: process.env.GITHUB_ID,
          clientSecret: process.env.GITHUB_SECRET,
        }),
        Providers.Email({
          server: process.env.EMAIL_SERVER,
          from: process.env.EMAIL_FROM,
        }),
        // ...add more providers here
      ],
      adapter: DynamoDBAdapter(
        new AWS.DynamoDB.DocumentClient()
      ),
      ...
    });

```

(`NEXT_AUTH_`로 시작하는 AWS 시크릿을 사용하면 [Vercel의 예약된 환경 변수](https://vercel.com/docs/environment-variables#reserved-environment-variables)와 충돌하지 않습니다.)

## 스키마[​](https://next-auth.js.org/v3/adapters/dynamodb#schema "제목으로 바로 가는 링크")

이 테이블은 단일 테이블 설계 패턴을 따릅니다. 이는 여러 장점이 있습니다.

- 관리, 모니터링, 프로비저닝해야 할 테이블이 하나뿐입니다.
- 관계 조회가 다중 테이블 스키마보다 더 빠릅니다(예: 특정 사용자의 모든 세션 조회).
- 멀티 리전으로 운영하려는 경우 복제해야 할 테이블도 하나뿐입니다.

다음은 테이블 스키마입니다:

![DynamoDB 테이블](https://i.imgur.com/hGZtWDq.png)
