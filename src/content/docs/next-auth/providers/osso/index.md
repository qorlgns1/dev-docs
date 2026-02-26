---
title: "Osso"
description: "Osso는 Identity Provider를 대상으로 SAML 인증을 처리하고, 프로필을 정규화하며, 해당 프로필을 OAuth 2.0 code grant flow에서 사용할 수 있게 해주는 오픈 소스 서비스입니다."
---

Source URL: https://next-auth.js.org/providers/osso

# Osso | NextAuth.js

Version: v4

## 문서[​](https://next-auth.js.org/providers/osso#documentation "Direct link to heading")

Osso는 Identity Provider를 대상으로 SAML 인증을 처리하고, 프로필을 정규화하며, 해당 프로필을 OAuth 2.0 code grant flow에서 사용할 수 있게 해주는 오픈 소스 서비스입니다.

아직 Osso 인스턴스가 없다면 테스트 용도로 [Osso's Demo App](https://demo.ossoapp.com)을 사용할 수 있습니다. Osso 인스턴스 배포 문서는 <https://ossoapp.com/docs/deploy/overview/>를 참고하세요.

## 구성[​](https://next-auth.js.org/providers/osso#configuration "Direct link to heading")

Osso Admin UI(예: <https://demo.ossoapp.com/admin/config>)에서 OAuth Clients를 구성할 수 있습니다. Client ID와 Secret을 발급받고 redirect URI를 allow-list에 추가해야 합니다.

[SAML SSO differs a bit from OAuth](https://ossoapp.com/blog/saml-vs-oauth) \- 애플리케이션에 SAML로 로그인하려는 각 테넌트마다, 여러분과 고객은 Osso Admin UI 및 해당 테넌트 Identity Provider의 관리자 대시보드에서 여러 단계의 구성을 수행해야 합니다. Osso는 Okta, OneLogin 같은 provider에 대한 문서를 제공하며, 이들 클라우드 기반 IDP는 테스트에 유용한 개발자 계정도 제공합니다. 또한 Osso는 Identity Provider 서비스 가입 없이 테스트할 수 있는 [Mock IDP](https://idp.ossoapp.com)도 제공합니다.

Osso의 전체 구성 및 테스트 문서는 <https://ossoapp.com/docs/configure/overview>에서 확인하세요.

## 옵션[​](https://next-auth.js.org/providers/osso#options "Direct link to heading")

**Osso Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Osso Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/osso.js)

원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/osso#example "Direct link to heading")

전체 예제 애플리케이션은 <https://github.com/enterprise-oss/osso-next-auth-example> 및 <https://nextjs-demo.ossoapp.com>에서 확인할 수 있습니다.

```
    import OssoProvider from "next-auth/providers/osso";
    ...
    providers: [
      OssoProvider({
        clientId: process.env.OSSO_CLIENT_ID,
        clientSecret: process.env.OSSO_CLIENT_SECRET,
        issuer: process.env.OSSO_ISSUER
      })
    }
    ...

```

note

`issuer`는 정규화된 전체 도메인이어야 합니다. 예: `demo.ossoapp.com`
