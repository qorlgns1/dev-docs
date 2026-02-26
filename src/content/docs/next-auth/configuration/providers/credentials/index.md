---
title: "Credentials"
description: "Credentials provider를 사용하면 사용자 이름과 비밀번호, 2단계 인증, 하드웨어 장치(예: YubiKey U2F / FIDO) 같은 임의의 자격 증명으로 로그인 처리를 할 수 있습니다."
---

소스 URL: https://next-auth.js.org/configuration/providers/credentials

# Credentials | NextAuth.js

버전: v4

### 사용 방법[​](https://next-auth.js.org/configuration/providers/credentials#how-to "Direct link to heading")

Credentials provider를 사용하면 사용자 이름과 비밀번호, 2단계 인증, 하드웨어 장치(예: YubiKey U2F / FIDO) 같은 임의의 자격 증명으로 로그인 처리를 할 수 있습니다.

이 기능은 기존 시스템을 기준으로 사용자를 인증해야 하는 사용 사례를 지원하기 위한 것입니다.

pages/api/auth/[...nextauth].js

```
    import CredentialsProvider from "next-auth/providers/credentials"
    ...
    providers: [
      CredentialsProvider({
        // The name to display on the sign in form (e.g. 'Sign in with...')
        name: 'Credentials',
        // The credentials is used to generate a suitable form on the sign in page.
        // You can specify whatever fields you are expecting to be submitted.
        // e.g. domain, username, password, 2FA token, etc.
        // You can pass any HTML attribute to the <input> tag through the object.
        credentials: {
          username: { label: "Username", type: "text", placeholder: "jsmith" },
          password: { label: "Password", type: "password" }
        },
        async authorize(credentials, req) {
          // You need to provide your own logic here that takes the credentials
          // submitted and returns either a object representing a user or value
          // that is false/null if the credentials are invalid.
          // e.g. return { id: 1, name: 'J Smith', email: 'jsmith@example.com' }
          // You can also use the `req` object to obtain additional parameters
          // (i.e., the request IP address)
          const res = await fetch("/your/endpoint", {
            method: 'POST',
            body: JSON.stringify(credentials),
            headers: { "Content-Type": "application/json" }
          })
          const user = await res.json()

          // If no error and we have user data, return it
          if (res.ok && user) {
            return user
          }
          // Return null if user data could not be retrieved
          return null
        }
      })
    ]
    ...

```

자세한 내용은 [Credentials provider documentation](https://next-auth.js.org/providers/credentials)을 참고하세요.

note

Credentials provider는 세션에 대해 JSON Web Tokens가 활성화된 경우에만 사용할 수 있습니다. Credentials provider로 인증된 사용자는 데이터베이스에 영구 저장되지 않습니다.

### 옵션[​](https://next-auth.js.org/configuration/providers/credentials#options "Direct link to heading")

| Name        | 설명                                 | Type                                  | 필수 |
| ----------- | ------------------------------------ | ------------------------------------- | ---- |
| id          | provider의 고유 ID                   | `string`                              | 예   |
| name        | provider를 설명하는 이름             | `string`                              | 예   |
| type        | provider 유형, 이 경우 `credentials` | `"credentials"`                       | 예   |
| credentials | 로그인에 사용할 자격 증명            | `Object`                              | 예   |
| authorize   | 사용자 인가 시 실행되는 콜백         | `(credentials, req) => Promise<User>` | 예   |
