---
title: "Credentials"
description: "Credentials provider를 사용하면 사용자 이름과 비밀번호, 도메인, 또는 2단계 인증이나 하드웨어 디바이스(예: YubiKey U2F / FIDO) 같은 임의의 자격 증명으로 로그인 처리를 할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/credentials

# Credentials | NextAuth.js

버전: v4

## 개요[​](https://next-auth.js.org/providers/credentials#overview "Direct link to heading")

Credentials provider를 사용하면 사용자 이름과 비밀번호, 도메인, 또는 2단계 인증이나 하드웨어 디바이스(예: YubiKey U2F / FIDO) 같은 임의의 자격 증명으로 로그인 처리를 할 수 있습니다.

기존에 사용자 인증을 수행하는 시스템이 이미 있는 사용 사례를 지원하기 위한 용도입니다.

이 방식으로 인증된 사용자는 데이터베이스에 영속 저장되지 않는다는 제약이 있으며, 따라서 세션에 JSON Web Token이 활성화된 경우에만 Credentials provider를 사용할 수 있습니다.

danger

자격 증명 기반 인증 기능은 비밀번호 사용에 따르는 고유한 보안 위험과 사용자 이름/비밀번호 지원에 필요한 추가 복잡성 때문에, 비밀번호 사용을 지양하도록 의도적으로 제한되어 있습니다.

## 옵션[​](https://next-auth.js.org/providers/credentials#options "Direct link to heading")

**Credentials Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Credentials Provider options](https://github.com/nextauthjs/next-auth/blob/main/packages/core/src/providers/credentials.ts)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시 - 사용자 이름 / 비밀번호[​](https://next-auth.js.org/providers/credentials#example---username--password "Direct link to heading")

Credentials provider는 다른 provider와 동일하게 지정하지만, `authorize()` 핸들러를 정의해야 한다는 점이 다릅니다. 이 핸들러는 HTTP POST로 제출된 자격 증명을 입력으로 받아 다음 중 하나를 반환합니다.

1. 자격 증명이 유효함을 나타내는 `user` 객체.

객체를 반환하면 JSON Web Token에 저장되고 사용자는 로그인됩니다. 단, 이후 이를 거부하도록 사용자 지정 `signIn()` callback이 구성된 경우는 예외입니다.

2. `null`을 반환하면 사용자에게 입력 정보를 확인하라는 오류가 표시됩니다.

3. Error를 throw하면 오류 메시지가 쿼리 파라미터로 포함된 상태로 사용자가 오류 페이지로 이동합니다.

Credentials provider의 `authorize()` 메서드는 두 번째 파라미터로 request 객체도 제공합니다(아래 예시 참고).

pages/api/auth/[...nextauth]/route.js

```
    import CredentialsProvider from "next-auth/providers/credentials";
    ...
    providers: [
      CredentialsProvider({
        // The name to display on the sign in form (e.g. "Sign in with...")
        name: "Credentials",
        // `credentials` is used to generate a form on the sign in page.
        // You can specify which fields should be submitted, by adding keys to the `credentials` object.
        // e.g. domain, username, password, 2FA token, etc.
        // You can pass any HTML attribute to the <input> tag through the object.
        credentials: {
          username: { label: "Username", type: "text", placeholder: "jsmith" },
          password: { label: "Password", type: "password" }
        },
        async authorize(credentials, req) {
          // Add logic here to look up the user from the credentials supplied
          const user = { id: "1", name: "J Smith", email: "jsmith@example.com" }

          if (user) {
            // Any object returned will be saved in `user` property of the JWT
            return user
          } else {
            // If you return null then an error will be displayed advising the user to check their details.
            return null

            // You can also Reject this callback with an Error thus the user will be sent to the error page with the error message as a query parameter
          }
        }
      })
    ]
    ...

```

토큰과 상호작용하는 방법에 대한 자세한 내용은 [callbacks documentation](https://next-auth.js.org/configuration/callbacks)을 참고하세요.

## 예시 - Web3 / Signin With Ethereum[​](https://next-auth.js.org/providers/credentials#example---web3--signin-with-ethereum "Direct link to heading")

credentials provider는 [Sign-in With Ethereum](https://login.xyz) 같은 서비스와 통합하는 데에도 사용할 수 있습니다.

자세한 내용은 아래 링크를 확인하세요.

- [튜토리얼](https://docs.login.xyz/integrations/nextauth.js)
- [예제 앱 리포지토리](https://github.com/spruceid/siwe-next-auth-example).
- [예제 앱 데모](https://siwe-next-auth-example2.vercel.app/).

## 여러 provider 사용[​](https://next-auth.js.org/providers/credentials#multiple-providers "Direct link to heading")

### 예시[​](https://next-auth.js.org/providers/credentials#example "Direct link to heading")

각 provider에 고유한 `id`를 지정하면 credentials provider를 둘 이상 지정할 수 있습니다.

다른 provider 옵션과 함께 조합해서 사용할 수도 있습니다.

모든 provider와 마찬가지로, 지정한 순서가 로그인 페이지에 표시되는 순서입니다.

```
    providers: [
      CredentialsProvider({
        id: "domain-login",
        name: "Domain Account",
        async authorize(credentials, req) {
          const user = {
            /* add function to get user */
          }
          return user
        },
        credentials: {
          domain: {
            label: "Domain",
            type: "text ",
            placeholder: "CORPNET",
            value: "CORPNET",
          },
          username: { label: "Username", type: "text ", placeholder: "jsmith" },
          password: { label: "Password", type: "password" },
        },
      }),
      CredentialsProvider({
        id: "intranet-credentials",
        name: "Two Factor Auth",
        async authorize(credentials, req) {
          const user = {
            /* add function to get user */
          }
          return user
        },
        credentials: {
          username: { label: "Username", type: "text ", placeholder: "jsmith" },
          "2fa-key": { label: "2FA Key" },
        },
      }),
      /* ... additional providers ... /*/
    ]

```

![](https://next-auth.js.org/assets/images/signin-complex-ee85e2ba139b73903bbb9723aa846865.png)
