---
title: '환경 변수[\u200b](https://next-auth.js.org/configuration/options#environment-variables "Direct link to heading")'
description: "프로덕션에 배포할 때는  환경 변수를 사이트의 정식 URL로 설정하세요."
---

Source URL: https://next-auth.js.org/configuration/options

# 옵션 | NextAuth.js

Version: v4

## 환경 변수[​](https://next-auth.js.org/configuration/options#environment-variables "Direct link to heading")

### NEXTAUTH_URL[​](https://next-auth.js.org/configuration/options#nextauth_url "Direct link to heading")

프로덕션에 배포할 때는 `NEXTAUTH_URL` 환경 변수를 사이트의 정식 URL로 설정하세요.

```
    NEXTAUTH_URL=https://example.com

```

Next.js 애플리케이션에서 custom base path를 사용하는 경우, API endpoint 경로를 전체 형태로 지정하세요. custom base path 사용법에 대한 자세한 내용은 [여기](https://next-auth.js.org/getting-started/client#custom-base-path)를 참고하세요.

_예:`NEXTAUTH_URL=https://example.com/custom-route/api/auth`_

tip

custom base path를 사용하는 경우 `<SessionProvider>`에 `basePath` page prop을 전달해야 합니다. 자세한 내용은 [여기](https://next-auth.js.org/getting-started/client#custom-base-path)를 참고하세요.

note

[System Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables)를 사용하면 [Vercel](https://vercel.com)에 배포할 때 자동으로 감지되므로 이 변수를 직접 정의할 필요가 없습니다. Project Settings에서 **Automatically expose System Environment Variables**가 체크되어 있는지 확인하세요.

### NEXTAUTH_SECRET[​](https://next-auth.js.org/configuration/options#nextauth_secret "Direct link to heading")

NextAuth.js JWT를 암호화하고 [email verification tokens](https://authjs.dev/guides/creating-a-database-adapter#verification-tokens)를 해시하는 데 사용됩니다. 이는 [NextAuth](https://next-auth.js.org/configuration/options#secret)와 [Middleware](https://next-auth.js.org/configuration/nextjs#secret)의 `secret` 옵션 기본값입니다. 또는 별칭인 `AUTH_SECRET`를 설정할 수도 있으며, 앞으로는 이 이름 사용이 권장됩니다.

tip

프로젝트 루트에서 `npx auth secret` \- 우리의 [CLI](https://cli.authjs.dev) \- 를 실행하면 무작위 값을 자동 생성해 `.env.local` 파일에 넣어줍니다.

### NEXTAUTH_URL_INTERNAL[​](https://next-auth.js.org/configuration/options#nextauth_url_internal "Direct link to heading")

설정하면 서버 측 호출에서 `NEXTAUTH_URL` 대신 이 값을 사용합니다. 서버가 사이트의 정식 URL에 접근할 수 없는 환경에서 유용합니다. 기본값은 `NEXTAUTH_URL`입니다.

```
    NEXTAUTH_URL_INTERNAL=http://10.240.8.16

```

---

## 옵션[​](https://next-auth.js.org/configuration/options#options "Direct link to heading")

옵션은 API route에서 NextAuth.js를 초기화할 때 전달됩니다.

### providers[​](https://next-auth.js.org/configuration/options#providers "Direct link to heading")

- **기본값** : `[]`
- **필수** : _예_

#### 설명[​](https://next-auth.js.org/configuration/options#description "Direct link to heading")

로그인에 사용할 인증 provider 배열입니다(예: Google, Facebook, Twitter, GitHub, Email 등). 순서는 자유롭습니다. 내장 provider 중 하나를 사용할 수도 있고, custom provider 객체를 사용할 수도 있습니다.

지원되는 provider 목록과 사용 방법은 [providers 문서](https://next-auth.js.org/configuration/providers/oauth)를 참고하세요.

---

### secret[​](https://next-auth.js.org/configuration/options#secret "Direct link to heading")

- **기본값** : 개발 환경에서는 `string` (_"options" 객체의 SHA hash_), 프로덕션 환경에서는 기본값 없음.
- **필수** : _예, 프로덕션에서는 필수!_

#### 설명[​](https://next-auth.js.org/configuration/options#description-1 "Direct link to heading")

무작위 문자열은 token 해시, cookie 서명/암호화, 그리고 암호화 키 생성에 사용됩니다.

환경 변수로 [`NEXTAUTH_SECRET`](https://next-auth.js.org/configuration/options#nextauth_secret)를 설정하면 이 옵션을 따로 정의할 필요가 없습니다.

개발 환경에서 값이 지정되지 않았고(`NEXTAUTH_SECRET` 변수도 없는 경우), 엔트로피를 위해 OAuth Client ID / Secrets를 포함한 모든 구성 옵션의 hash를 사용합니다.

danger

프로덕션에서 `secret` 또는 `NEXTAUTH_SECRET`를 제공하지 않으면 [error](https://next-auth.js.org/errors#no_secret)가 발생합니다.

커맨드 라인에서 아래 `openssl` 명령으로 좋은 값을 빠르게 만들 수 있습니다.

```
    $ openssl rand -base64 32

```

tip

개발 환경에서 기본 secret 생성에 의존하면, 구성을 변경할 때마다 secret이 바뀌므로 JWT 복호화 오류가 발생할 수 있습니다. 명시적으로 secret을 정의하면 이 문제가 사라집니다. 앞으로는 개발 환경에서도 이 옵션을 필수로 만들 가능성이 높습니다.

---

### session[​](https://next-auth.js.org/configuration/options#session "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-2 "Direct link to heading")

`session` 객체와 그 안의 모든 속성은 선택 사항입니다.

이 옵션의 기본값은 아래와 같습니다:

```
    session: {
      // Choose how you want to save the user session.
      // The default is `"jwt"`, an encrypted JWT (JWE) stored in the session cookie.
      // If you use an `adapter` however, we default it to `"database"` instead.
      // You can still force a JWT session by explicitly defining `"jwt"`.
      // When using `"database"`, the session cookie will only contain a `sessionToken` value,
      // which is used to look up the session in the database.
      strategy: "database",

      // Seconds - How long until an idle session expires and is no longer valid.
      maxAge: 30 * 24 * 60 * 60, // 30 days

      // Seconds - Throttle how frequently to write to database to extend a session.
      // Use it to limit write operations. Set to 0 to always update the database.
      // Note: This option is ignored if using JSON Web Tokens
      updateAge: 24 * 60 * 60, // 24 hours

      // The session token is usually either a random UUID or string, however if you
      // need a more customized session token string, you can define your own generate function.
      generateSessionToken: () => {
        return randomUUID?.() ?? randomBytes(32).toString("hex")
      }
    }

```

---

### jwt[​](https://next-auth.js.org/configuration/options#jwt "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-3 "Direct link to heading")

`session: { strategy: "jwt" }` 옵션을 활성화하면 session token으로 JSON Web Token을 사용할 수 있습니다. adapter를 지정하지 않았다면 기본적으로 JSON Web Token이 활성화됩니다. JSON Web Token은 기본적으로 암호화(JWE)됩니다. 이 동작을 유지하는 것을 권장합니다. 고급 옵션인 [Override JWT `encode` and `decode` methods](https://next-auth.js.org/configuration/options#override-jwt-encode-and-decode-methods)를 참고하세요.

#### JSON Web Token 옵션[​](https://next-auth.js.org/configuration/options#json-web-token-options "Direct link to heading")

```
    jwt: {
      // The maximum age of the NextAuth.js issued JWT in seconds.
      // Defaults to `session.maxAge`.
      maxAge: 60 * 60 * 24 * 30,
      // You can define your own encode/decode functions for signing and encryption
      async encode() {},
      async decode() {},
    }

```

JSON Web Token 예시는 다음과 같은 payload를 포함합니다:

```
    {
      name: 'Iain Collins',
      email: 'me@iaincollins.com',
      picture: 'https://example.com/image.jpg',
      iat: 1594601838,
      exp: 1597193838
    }

```

#### JWT Helper[​](https://next-auth.js.org/configuration/options#jwt-helper "Direct link to heading")

내장 `getToken()` helper 메서드를 사용해 다음과 같이 token을 검증하고 복호화할 수 있습니다:

```
    import { getToken } from "next-auth/jwt"

    const secret = process.env.NEXTAUTH_SECRET

    export default async function handler(req, res) {
      // if using `NEXTAUTH_SECRET` env variable, we detect it, and you won't actually need to `secret`
      // const token = await getToken({ req })
      const token = await getToken({ req, secret })
      console.log("JSON Web Token", token)
      res.end()
    }

```

_편의를 위해 이 helper 함수는 `Authorization: 'Bearer token'` HTTP header로 전달된 token도 읽고 decode할 수 있습니다._

**필수**

getToken() helper에는 다음 옵션이 필요합니다:

- `req` \- (object) 요청 객체
- `secret` \- (string) JWT Secret. 대신 `NEXTAUTH_SECRET`를 사용하세요.

helper에 *`jwt` 옵션에 구성된 모든 옵션*도 전달해야 합니다.

예: custom session `maxAge`, custom signing and/or encryption keys 또는 options를 포함하는 경우

**선택**

다음 옵션도 지원합니다:

- `secureCookie` \- (boolean) secure 접두사가 붙은 cookie 이름 사용

기본적으로 helper 함수는 secure 접두사 cookie를 사용해야 하는지 판단하려고 시도합니다(예: 프로덕션에서는 `true`, 개발에서는 `false`, 단 NEXTAUTH_URL에 HTTPS URL이 포함된 경우는 예외).

- `cookieName` \- (string) session token cookie 이름

`cookieName`을 명시적으로 지정하면 `secureCookie` 옵션은 무시됩니다.

- `raw` \- (boolean) raw token 가져오기(decode하지 않음)

`true`로 설정하면 복호화나 검증 없이 raw token을 반환합니다.

tip

custom session token `cookieName`을 사용할 때는 `getToken`에도 같은 이름을 제공해야 합니다. Next.js [`withAuth`](https://next-auth.js.org/configuration/nextjs#middleware) middleware를 사용하는 경우에도 동일한 `cookieName`으로 설정해야 합니다.

note

JWT는 Session Token cookie에 저장되며, database session token에 사용하는 것과 동일한 cookie입니다.

---

### pages[​](https://next-auth.js.org/configuration/options#pages "Direct link to heading")

- **기본값** : `{}`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-4 "Direct link to heading")

custom sign in, sign out, error 페이지를 만들고 싶다면 사용할 URL을 지정하세요.

지정된 페이지는 해당 내장 페이지를 덮어씁니다.

_예시:_

```
     pages: {
      signIn: '/auth/signin',
      signOut: '/auth/signout',
      error: '/auth/error', // Error code passed in query string as ?error=
      verifyRequest: '/auth/verify-request', // (used for check email message)
      newUser: '/auth/new-user' // New users will be directed here on first sign in (leave the property out if not of interest)
    }

```

note

이 구성을 사용할 때는 해당 페이지가 실제로 존재하는지 확인하세요. 예를 들어 `error: '/auth/error'`는 `pages/auth/error.js`에 있는 페이지 파일을 가리킵니다.

자세한 내용은 [pages 옵션](https://next-auth.js.org/configuration/pages) 문서를 참고하세요.

---

### callbacks[​](https://next-auth.js.org/configuration/options#callbacks "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-5 "Direct link to heading")

Callbacks는 작업이 수행될 때 어떤 일이 일어날지 제어할 수 있는 비동기 함수입니다.

Callbacks는 매우 강력하며, 특히 JSON Web Token 관련 시나리오에서 데이터베이스 없이 접근 제어를 구현하고 외부 데이터베이스 또는 API와 통합할 수 있게 해줍니다.

아래 각 callback에 대해 handler를 지정할 수 있습니다.

```
    callbacks: {
      async signIn({ user, account, profile, email, credentials }) {
        return true
      },
      async redirect({ url, baseUrl }) {
        return baseUrl
      },
      async session({ session, token, user }) {
        return session
      },
      async jwt({ token, user, account, profile, isNewUser }) {
        return token
      }
    }

```

callback 함수 사용법에 대한 자세한 내용은 [callbacks 문서](https://next-auth.js.org/configuration/callbacks)를 참고하세요.

---

### events[​](https://next-auth.js.org/configuration/options#events "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-6 "Direct link to heading")

Events는 응답을 반환하지 않는 비동기 함수이며, 감사 로그(audit logging)에 유용합니다.

아래 각 event에 대해 handler를 지정할 수 있습니다. 예: 디버깅 또는 감사 로그 생성.

message 객체의 내용은 흐름에 따라 달라집니다(예: OAuth 또는 Email 인증 흐름, JWT 또는 database session 등). 각 message 객체의 형태와 event 함수 사용법은 [events 문서](https://next-auth.js.org/configuration/events)를 참고하세요.

```
    events: {
      async signIn(message) { /* on successful sign in */ },
      async signOut(message) { /* on signout */ },
      async createUser(message) { /* user created */ },
      async updateUser(message) { /* user updated - e.g. their email was verified */ },
      async linkAccount(message) { /* account (e.g. Twitter) linked to a user */ },
      async session(message) { /* session is active */ },
    }

```

---

### adapter[​](https://next-auth.js.org/configuration/options#adapter "Direct link to heading")

- **기본값** : 없음
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-7 "Direct link to heading")

기본적으로 NextAuth.js에는 더 이상 adapter가 포함되지 않습니다. user/account 데이터를 영구 저장하려면 제공되는 여러 adapter 중 하나를 설치하세요. 자세한 내용은 [adapter 문서](https://authjs.dev/getting-started/database)에서 확인할 수 있습니다.

---

### debug[​](https://next-auth.js.org/configuration/options#debug "Direct link to heading")

- **기본값** : `false`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-8 "Direct link to heading")

인증 및 database 작업에 대한 디버그 메시지를 활성화하려면 debug를 `true`로 설정하세요.

---

### logger[​](https://next-auth.js.org/configuration/options#logger "Direct link to heading")

- **기본값** : `console`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-9 "Direct link to heading")

logger 레벨을 원하는 대로 재정의하고(`undefined` 레벨은 내장 logger 사용), NextAuth.js의 로그를 가로챌 수 있습니다. 이를 사용해 NextAuth.js 로그를 서드파티 로깅 서비스로 보낼 수 있습니다.

`error`와 `warn`의 `code` 파라미터는 각각 [Warnings](https://next-auth.js.org/warnings) 및 [Errors](https://next-auth.js.org/errors) 페이지에서 설명합니다.

예시:

/pages/api/auth/[...nextauth].js

```
    import log from "logging-service"

    export default NextAuth({
      ...
      logger: {
        error(code, metadata) {
          log.error(code, metadata)
        },
        warn(code) {
          log.warn(code)
        },
        debug(code, metadata) {
          log.debug(code, metadata)
        }
      }
      ...
    })

```

note

사용자가 `debug` 레벨을 정의하면 `debug: false` [option](https://next-auth.js.org/configuration/options#debug)과 관계없이 호출됩니다.

---

### theme[​](https://next-auth.js.org/configuration/options#theme "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-10 "Direct link to heading")

[pages](https://next-auth.js.org/configuration/pages)의 색상 테마를 변경하고, 몇 가지 사소한 사용자 지정도 허용합니다. 페이지를 항상 밝게 고정하려면 `theme.colorScheme`을 `"light"`로 설정하세요. 페이지를 항상 어둡게 고정하려면 `"dark"`로 설정하세요. 페이지가 시스템의 선호 테마를 따르도록 하려면 `"auto"`로 설정하세요(또는 이 옵션을 생략하세요). ([prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 쿼리를 사용합니다.)

또한 `theme.logo`에 로고 URL을 정의할 수 있으며, 이 로고는 기본 signin/signout/error/verify-request 페이지의 메인 카드 위에 렌더링됩니다. 그리고 `theme.brandColor`를 설정하면 이 페이지들의 강조 색상에 반영됩니다.

sign-in 버튼의 배경색은 `brandColor`와 일치하며 기본값은 `"#346df1"`입니다. 텍스트 색상 기본값은 `#fff`이지만, 브랜드 색상의 대비가 약하다면 `buttonText` 색상 옵션으로 보정하세요.

```
    theme: {
      colorScheme: "auto", // "auto" | "dark" | "light"
      brandColor: "", // Hex color code
      logo: "", // Absolute URL to image
      buttonText: "" // Hex color code
    }

```

---

## 고급 옵션[​](https://next-auth.js.org/configuration/options#advanced-options "Direct link to heading")

고급 옵션은 기본 옵션과 동일한 방식으로 전달되지만, 복잡한 영향이나 부작용이 있을 수 있습니다. 충분히 익숙하지 않다면 고급 옵션 사용은 피하는 것이 좋습니다.

---

### useSecureCookies[​](https://next-auth.js.org/configuration/options#usesecurecookies "Direct link to heading")

- **기본값** : HTTPS 사이트는 `true` / HTTP 사이트는 `false`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-11 "Direct link to heading")

`true`로 설정하면 (`https://`로 시작하는 모든 사이트 URL의 기본값), NextAuth.js가 설정하는 모든 쿠키는 HTTPS URL에서만 접근할 수 있습니다.

개발 편의를 위해 `http://`로 시작하는 URL(예: `http://localhost:3000`)에서는 이 옵션의 기본값이 `false`입니다.

참고

명시한 사용자 정의 `cookies`의 모든 속성은 이 옵션을 덮어씁니다.

주의

프로덕션에서 이 옵션을 *false*로 설정하면 보안 위험이 있으며, 실제 운영 환경에서 세션 하이재킹을 허용할 수 있습니다. 이 옵션은 개발 및 테스트 지원용입니다. 이 옵션 사용은 권장되지 않습니다.

---

### cookies[​](https://next-auth.js.org/configuration/options#cookies "Direct link to heading")

- **기본값** : `{}`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/configuration/options#description-12 "Direct link to heading")

NextAuth.js의 쿠키는 기본적으로 청크 처리됩니다. 즉, 4kb 제한에 도달하면 `.{number}` 접미사가 붙은 새 쿠키를 만들고, 이를 파싱/읽기할 때 올바른 순서로 다시 조합합니다. 이는 예를 들어 사용자가 `sessionToken`에 추가 데이터를 저장하려 할 때 발생할 수 있는 크기 제한을 피하기 위해 도입되었습니다.

NextAuth.js가 사용하는 모든 쿠키의 기본 이름과 옵션을 재정의할 수 있습니다.

이것은 고급 옵션이며, 잘못 사용하면 인증이 깨지거나 애플리케이션에 보안 취약점을 도입할 수 있으므로 권장되지 않습니다.

하나 이상의 쿠키에 사용자 정의 속성을 지정할 수 있지만, 특정 쿠키에 사용자 정의 옵션을 지정했다면 해당 쿠키의 모든 옵션을 제공해야 합니다.

이 기능을 사용하면 내장된 동적 정책을 사용하지 않게 되므로, 개발 빌드와 프로덕션 빌드에서 서로 다른 쿠키 정책을 설정할 수 있도록 조건부 동작을 만드는 것이 일반적입니다.

팁

이 옵션의 사용 사례 예시는 하위 도메인 간 세션 토큰 공유를 지원하는 것입니다.

#### 예시[​](https://next-auth.js.org/configuration/options#example "Direct link to heading")

```
    cookies: {
      sessionToken: {
        name: `__Secure-next-auth.session-token`,
        options: {
          httpOnly: true,
          sameSite: 'lax',
          path: '/',
          secure: true
        }
      },
      callbackUrl: {
        name: `__Secure-next-auth.callback-url`,
        options: {
          sameSite: 'lax',
          path: '/',
          secure: true
        }
      },
      csrfToken: {
        name: `__Host-next-auth.csrf-token`,
        options: {
          httpOnly: true,
          sameSite: 'lax',
          path: '/',
          secure: true
        }
      },
      pkceCodeVerifier: {
        name: `${cookiePrefix}next-auth.pkce.code_verifier`,
        options: {
          httpOnly: true,
          sameSite: 'lax',
          path: '/',
          secure: true,
          maxAge: 900
        }
      },
      state: {
        name: `${cookiePrefix}next-auth.state`,
        options: {
          httpOnly: true,
          sameSite: "lax",
          path: "/",
          secure: true,
          maxAge: 900
        },
      },
      nonce: {
        name: `${cookiePrefix}next-auth.nonce`,
        options: {
          httpOnly: true,
          sameSite: "lax",
          path: "/",
          secure: true,
        },
      },
    }

```

주의

사용자 정의 쿠키 정책을 사용하면 애플리케이션에 보안 취약점이 생길 수 있으며, 그 영향을 이해하는 고급 사용자를 위한 옵션입니다. 이 옵션 사용은 권장되지 않습니다.

---

### JWT `encode` 및 `decode` 메서드 재정의[​](https://next-auth.js.org/configuration/options#override-jwt-encode-and-decode-methods "Direct link to heading")

NextAuth.js는 기본적으로 암호화된 JSON Web Tokens([JWE](https://datatracker.ietf.org/doc/html/rfc7516))를 사용합니다. 특별한 이유가 없다면 이 동작을 유지하는 것을 권장합니다. 다만 `encode` 및 `decode` 메서드를 사용해 이를 재정의할 수 있습니다. 두 메서드는 반드시 동시에 정의해야 합니다.

**중요: 미들웨어로 라우트를 보호하는 경우, 동일한 메서드를 [`_middleware.ts` options](https://next-auth.js.org/configuration/nextjs#custom-jwt-decode-method)에도 설정해야 합니다.**

```
    jwt: {
      async encode(params: {
        token: JWT
        secret: string
        maxAge: number
      }): Promise<string> {
        // return a custom encoded JWT string
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
      },
      async decode(params: {
        token: string
        secret: string
      }): Promise<JWT | null> {
        // return a `JWT` object, or `null` if decoding failed
        return {}
      },
    }

```
