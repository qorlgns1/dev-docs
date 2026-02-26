---
title: "Amazon Cognito"
description: "원본 URL: https://next-auth.js.org/providers/cognito"
---

원본 URL: https://next-auth.js.org/providers/cognito

# Amazon Cognito | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/cognito#documentation "Direct link to heading")

<https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html>

## 구성[​](https://next-auth.js.org/providers/cognito#configuration "Direct link to heading")

<https://console.aws.amazon.com/cognito/users/>

Cognito 대시보드로 이동하려면 AWS 리전을 선택해야 합니다.

## 옵션[​](https://next-auth.js.org/providers/cognito#options "Direct link to heading")

**Amazon Cognito Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Amazon Cognito Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/cognito.ts)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/cognito#example "Direct link to heading")

```
    import CognitoProvider from "next-auth/providers/cognito";
    ...
    providers: [
      CognitoProvider({
        clientId: process.env.COGNITO_CLIENT_ID,
        clientSecret: process.env.COGNITO_CLIENT_SECRET,
        issuer: process.env.COGNITO_ISSUER,
      })
    ]
    ...

```

팁

issuer는 다음과 같은 형태의 URL입니다: `https://cognito-idp.{region}.amazonaws.com/{PoolId}`

`PoolId`는 App Client ID와 혼동하면 안 되며, Cognito의 `General Settings`에서 확인할 수 있습니다.

주의

적절한 클라이언트 설정을 모두 선택하지 않으면 OAuth flow가 동작하지 않습니다.

팁

이 설정을 지정하기 전에 먼저 [Amazon Cognito hosted domain을 설정](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)해야 합니다. 해당 설정은 `App Client/Edit Hosted UI`에서 찾을 수 있습니다.
