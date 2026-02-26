---
title: "Okta"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/okta

# Okta | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/okta#documentation "Direct link to heading")

<https://developer.okta.com/docs/reference/api/oidc>

## 옵션[​](https://next-auth.js.org/v3/providers/okta#options "Direct link to heading")

**Okta Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Okta Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/okta.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/okta#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Okta({
        clientId: process.env.OKTA_CLIENT_ID,
        clientSecret: process.env.OKTA_CLIENT_SECRET,
        domain: process.env.OKTA_DOMAIN
      })
    ]
    ...

```
