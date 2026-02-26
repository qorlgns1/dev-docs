---
title: "Amazon Cognito"
description: "Cognito 대시보드로 이동하려면 AWS 리전을 선택해야 합니다."
---

Source URL: https://next-auth.js.org/v3/providers/cognito

# Amazon Cognito | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/cognito#documentation "Direct link to heading")

<https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html>

## 구성[​](https://next-auth.js.org/v3/providers/cognito#configuration "Direct link to heading")

<https://console.aws.amazon.com/cognito/users/>

Cognito 대시보드로 이동하려면 AWS 리전을 선택해야 합니다.

## 옵션[​](https://next-auth.js.org/v3/providers/cognito#options "Direct link to heading")

**Amazon Cognito Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Amazon Cognito Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/cognito.js)

사용 사례에 맞게 옵션을 자유롭게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/cognito#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Cognito({
        clientId: process.env.COGNITO_CLIENT_ID,
        clientSecret: process.env.COGNITO_CLIENT_SECRET,
        domain: process.env.COGNITO_DOMAIN,
      })
    ]
    ...

```

danger

적절한 클라이언트 설정을 모두 선택해야 합니다. 그렇지 않으면 OAuth 흐름이 동작하지 않습니다.

![cognito](https://user-images.githubusercontent.com/7902980/83951604-cd096e80-a832-11ea-8bd2-c496ec9a16cb.PNG)
