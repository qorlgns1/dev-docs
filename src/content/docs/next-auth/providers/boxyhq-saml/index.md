---
title: "BoxyHQ SAML"
description: "BoxyHQ SAML은 SAML 로그인 흐름을 OAuth 2.0 흐름으로 처리하여 SAML 프로토콜의 모든 복잡성을 추상화해 주는 오픈 소스 서비스입니다."
---

Source URL: https://next-auth.js.org/providers/boxyhq-saml

# BoxyHQ SAML | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/boxyhq-saml#documentation "Direct link to heading")

BoxyHQ SAML은 SAML 로그인 흐름을 OAuth 2.0 흐름으로 처리하여 SAML 프로토콜의 모든 복잡성을 추상화해 주는 오픈 소스 서비스입니다.

BoxyHQ SAML을 별도 서비스로 배포하거나, NPM 라이브러리를 사용해 앱에 임베드할 수 있습니다. [자세한 내용은 문서를 확인하세요](https://boxyhq.com/docs/jackson/deploy)

## 구성[​](https://next-auth.js.org/providers/boxyhq-saml#configuration "Direct link to heading")

SAML 로그인에는 각 테넌트마다 설정이 필요합니다. 일반적인 방법 중 하나는 이메일 주소의 도메인을 사용해 사용자가 어떤 테넌트에 속하는지 파악하는 것입니다. 이를 위해 백엔드의 고유한 테넌트 ID (string)를 사용할 수도 있으며, 보통 계정 또는 조직 ID 형태입니다.

자세한 내용은 [문서](https://boxyhq.com/docs/jackson/saml-flow#2-saml-config-api)를 확인하세요.

## 옵션[​](https://next-auth.js.org/providers/boxyhq-saml#options "Direct link to heading")

**BoxyHQ SAML Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [BoxyHQ Provider 옵션](https://github.com/nextauthjs/next-auth/tree/v4/packages/next-auth/src/providers/boxyhq-saml.ts)

원하는 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/boxyhq-saml#example "Direct link to heading")

```
    import BoxyHQSAMLProvider from "next-auth/providers/boxyhq-saml"
    ...
    providers: [
      BoxyHQSAMLProvider({
        issuer: "http://localhost:5225",
        clientId: "dummy", // The dummy here is necessary since we'll pass tenant and product custom attributes in the client code
        clientSecret: "dummy", // The dummy here is necessary since we'll pass tenant and product custom attributes in the client code
      })
    }
    ...

```

클라이언트 측에서는 `signIn` 함수에 `tenant`와 `product`라는 추가 파라미터를 전달해야 합니다. 이렇게 하면 BoxyHQL SAML이 올바른 SAML 구성을 파악하고, 사용자를 로그인할 수 있도록 적절한 SAML Identity Provider로 안내할 수 있습니다.

```
    import { signIn } from "next-auth/react";
    ...

      // Map your users's email to a tenant and product
      const tenant = email.split("@")[1];
      const product = 'my_awesome_product';
    ...
    ...

```
