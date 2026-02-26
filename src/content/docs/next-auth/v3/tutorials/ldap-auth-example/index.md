---
title: "LDAP 인증"
description: "NextAuth.js는 custom Credential provider를 설정할 수 있는 기능을 제공하며, 이를 활용해 기존 LDAP 서버를 대상으로 사용자를 인증할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/tutorials/ldap-auth-example

# LDAP 인증 | NextAuth.js

버전: v3

NextAuth.js는 [custom Credential provider](https://next-auth.js.org/configuration/providers/credentials)를 설정할 수 있는 기능을 제공하며, 이를 활용해 기존 LDAP 서버를 대상으로 사용자를 인증할 수 있습니다.

추가 의존성인 `ldapjs`가 필요하며, `npm install ldapjs`를 실행해 설치할 수 있습니다.

그다음 아래와 같이 `Providers.Credentials()` provider key를 설정해야 합니다:

[...nextauth].js

```
    const ldap = require("ldapjs")
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"

    export default NextAuth({
      providers: [
        Providers.Credentials({
          name: "LDAP",
          credentials: {
            username: { label: "DN", type: "text", placeholder: "" },
            password: { label: "Password", type: "password" },
          },
          async authorize(credentials, req) {
            // You might want to pull this call out so we're not making a new LDAP client on every login attemp
            const client = ldap.createClient({
              url: process.env.LDAP_URI,
            })

            // Essentially promisify the LDAPJS client.bind function
            return new Promise((resolve, reject) => {
              client.bind(credentials.username, credentials.password, (error) => {
                if (error) {
                  console.error("Failed")
                  reject()
                } else {
                  console.log("Logged in")
                  resolve({
                    username: credentials.username,
                    password: credentials.password,
                  })
                }
              })
            })
          },
        }),
      ],
      callbacks: {
        async jwt(token, user, account, profile, isNewUser) {
          const isSignIn = user ? true : false
          if (isSignIn) {
            token.username = user.username
            token.password = user.password
          }
          return token
        },
        async session(session, user) {
          return { ...session, user: { username: user.username } }
        },
      },
      secret: process.env.NEXTAUTH_SECRET,
      jwt: {
        secret: process.env.NEXTAUTH_SECRET,
        encryption: true, // Very important to encrypt the JWT, otherwise you're leaking username+password into the browser
      },
    })

```

핵심 아이디어는 LDAP 서버 인증이 완료되면 username/DN과 password를 브라우저에 저장된 JWT로 함께 전달할 수 있다는 점입니다.

이 값은 이후 모든 API route로 다시 전달되며, 다음과 같이 가져올 수 있습니다:

/pages/api/doLDAPWork.js

```
    token = await jwt.getToken({
      req,
      secret: process.env.NEXTAUTH_SECRET,
    })
    const { username, password } = token

```

> 코드 예제를 제공해 준 [Winwardo](https://github.com/Winwardo)에게 감사드립니다.
