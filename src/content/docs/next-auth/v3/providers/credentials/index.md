---
title: "자격 증명"
description: "Credentials provider를 사용하면 사용자 이름과 비밀번호, 도메인, 2단계 인증, 하드웨어 디바이스(예: YubiKey U2F / FIDO)처럼 임의의 자격 증명으로 로그인 처리를 할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/credentials

# 자격 증명 | NextAuth.js

Version: v3

## 개요[​](https://next-auth.js.org/v3/providers/credentials#overview "Direct link to heading")

Credentials provider를 사용하면 사용자 이름과 비밀번호, 도메인, 2단계 인증, 하드웨어 디바이스(예: YubiKey U2F / FIDO)처럼 임의의 자격 증명으로 로그인 처리를 할 수 있습니다.

이 provider는 기존 사용자 인증 시스템과 연동해야 하는 사용 사례를 지원하기 위한 것입니다.

이 방식으로 인증된 사용자는 데이터베이스에 영구 저장되지 않는다는 제약이 있으며, 따라서 Credentials provider는 세션에 JSON Web Token이 활성화된 경우에만 사용할 수 있습니다.

참고

자격 증명 기반 인증 기능은 의도적으로 제한되어 있습니다. 이는 비밀번호에 내재된 보안 위험과 사용자 이름/비밀번호 지원에 따르는 추가 복잡성 때문에 비밀번호 사용을 지양하도록 하기 위함입니다.

## 옵션[​](https://next-auth.js.org/v3/providers/credentials#options "Direct link to heading")

**Credentials Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Credentials Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/credentials.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/credentials#example "Direct link to heading")

Credentials provider는 다른 provider와 동일하게 지정하지만, HTTP POST로 제출된 자격 증명을 입력으로 받아 다음 중 하나를 반환하는 `authorize()` 핸들러를 정의해야 합니다.

1. 자격 증명이 유효함을 나타내는 `user` 객체.

객체를 반환하면 JSON Web Token에 저장되고, 이후 이를 거부하는 사용자 지정 `signIn()` callback이 설정되어 있지 않다면 사용자가 로그인됩니다.

2. 실패를 나타내는 `false` 또는 `null`.

`false` 또는 `null`을 반환하면 사용자에게 입력 정보를 확인하라는 오류가 표시됩니다.

3. Error 또는 URL(문자열)을 throw할 수 있습니다.

Error를 throw하면 오류 메시지가 쿼리 파라미터로 포함된 상태로 오류 페이지로 이동합니다. URL(문자열)을 throw하면 해당 URL로 리디렉션됩니다.

Credentials provider의 `authorize()` 메서드는 두 번째 파라미터로 request 객체도 제공합니다(아래 예제 참고).

pages/api/auth/[...nextauth].js

```
    import CredentialsProvider from 'next-auth/providers/credentials';
    ...
    providers: [
      CredentialsProvider({
        // The name to display on the sign in form (e.g. 'Sign in with...')
        name: 'Credentials',
        // The credentials is used to generate a suitable form on the sign in page.
        // You can specify whatever fields you are expecting to be submitted.
        // e.g. domain, username, password, 2FA token, etc.
        credentials: {
          username: { label: "Username", type: "text", placeholder: "jsmith" },
          password: {  label: "Password", type: "password" }
        },
        async authorize(credentials, req) {
          // Add logic here to look up the user from the credentials supplied
          const user = { id: 1, name: 'J Smith', email: 'jsmith@example.com' }

          if (user) {
            // Any object returned will be saved in `user` property of the JWT
            return user
          } else {
            // If you return null or false then the credentials will be rejected
            return null
            // You can also Reject this callback with an Error or with a URL:
            // throw new Error('error message') // Redirect to error page
            // throw '/path/to/redirect'        // Redirect to a URL
          }
        }
      })
    ]
    ...

```

토큰과 상호작용하는 방법에 대한 자세한 내용은 [callbacks documentation](https://next-auth.js.org/configuration/callbacks)를 참고하세요.

## 여러 provider[​](https://next-auth.js.org/v3/providers/credentials#multiple-providers "Direct link to heading")

### 예제 코드[​](https://next-auth.js.org/v3/providers/credentials#example-code "Direct link to heading")

각 provider에 고유한 `id`를 지정하면 credentials provider를 둘 이상 설정할 수 있습니다.

다른 provider 옵션과 함께 조합해서 사용할 수도 있습니다.

모든 provider와 마찬가지로, 지정한 순서대로 로그인 페이지에 표시됩니다.

```
    providers: [
      Providers.Credentials({
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
      Providers.Credentials({
        id: "intranet-credentials",
        name: "Two Factor Auth",
        async authorize(credentials, req) {
          const user = {
            /* add function to get user */
          }
          return user
        },
        credentials: {
          email: { label: "Username", type: "text ", placeholder: "jsmith" },
          "2fa-key": { label: "2FA Key" },
        },
      }),
      /* ... additional providers ... /*/
    ]

```

### 예제 UI[​](https://next-auth.js.org/v3/providers/credentials#example-ui "Direct link to heading")

아래 예제는 복잡한 구성이 내장 로그인 페이지에서 어떻게 렌더링되는지 보여줍니다.

사용자 경험을 커스텀하고 싶다면 [use a custom sign in page](https://next-auth.js.org/configuration/pages#credentials-sign-in)를 사용할 수도 있습니다.

![](https://next-auth.js.org/img/signin-complex.png)
