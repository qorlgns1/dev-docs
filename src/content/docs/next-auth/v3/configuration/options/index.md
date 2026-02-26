---
title: '환경 변수[\u200b](https://next-auth.js.org/v3/configuration/options#environment-variables "Direct link to heading")'
description: "프로덕션에 배포할 때는  환경 변수를 사이트의 정식 URL로 설정하세요."
---

Source URL: https://next-auth.js.org/v3/configuration/options

# 옵션 | NextAuth.js

버전: v3

## 환경 변수[​](https://next-auth.js.org/v3/configuration/options#environment-variables "Direct link to heading")

### NEXTAUTH_URL[​](https://next-auth.js.org/v3/configuration/options#nextauth_url "Direct link to heading")

프로덕션에 배포할 때는 `NEXTAUTH_URL` 환경 변수를 사이트의 정식 URL로 설정하세요.

```
    NEXTAUTH_URL=https://example.com

```

Next.js 애플리케이션에서 커스텀 base path를 사용하는 경우, API 엔드포인트 경로를 전체 경로로 지정하세요.

_예: `NEXTAUTH_URL=https://example.com/custom-route/api/auth`_

tip

Vercel에서 환경 변수를 설정하려면 [dashboard](https://vercel.com/dashboard) 또는 `vercel env` 명령어를 사용할 수 있습니다.

### NEXTAUTH_URL_INTERNAL[​](https://next-auth.js.org/v3/configuration/options#nextauth_url_internal "Direct link to heading")

설정하면 서버 사이드 호출에서 `NEXTAUTH_URL` 대신 이 값을 사용합니다. 서버가 사이트의 정식 URL에 접근할 수 없는 환경에서 유용합니다. 기본값은 `NEXTAUTH_URL`입니다.

```
    NEXTAUTH_URL_INTERNAL=http://10.240.8.16

```

---

## 옵션[​](https://next-auth.js.org/v3/configuration/options#options "Direct link to heading")

옵션은 API 라우트에서 NextAuth.js를 초기화할 때 전달됩니다.

### providers[​](https://next-auth.js.org/v3/configuration/options#providers "Direct link to heading")

- **기본값** : `[]`
- **필수** : _예_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description "Direct link to heading")

로그인에 사용할 인증 제공자 배열입니다(예: Google, Facebook, Twitter, GitHub, Email 등). 순서는 자유롭게 지정할 수 있습니다. 내장 제공자 중 하나이거나 커스텀 제공자 객체를 사용할 수 있습니다.

지원되는 제공자 목록과 사용 방법은 [providers 문서](https://next-auth.js.org/configuration/providers/oauth)를 참고하세요.

---

### database[​](https://next-auth.js.org/v3/configuration/options#database "Direct link to heading")

- **기본값** : `null`
- **필수** : _아니요 (email provider 사용 시 제외)_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-1 "Direct link to heading")

[데이터베이스 연결 문자열 또는 설정 객체입니다.](https://next-auth.js.org/configuration/databases)

---

### secret[​](https://next-auth.js.org/v3/configuration/options#secret "Direct link to heading")

- **기본값** : `string` (_"options" 객체의 SHA 해시_)
- **필수** : _아니요 - 하지만 강력히 권장됩니다!_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-2 "Direct link to heading")

토큰 해시, 쿠키 서명, 암호화 키 생성에 사용되는 랜덤 문자열입니다.

지정하지 않으면 엔트로피를 위해 Client ID / Secrets를 포함한 모든 설정 옵션의 해시를 사용합니다.

기본 동작은 변경 가능성이 크므로, 설정 변경 배포 시 최종 사용자 세션이 무효화되는 것을 피하려면 값을 명시적으로 지정하는 것을 강력히 권장합니다.

---

### session[​](https://next-auth.js.org/v3/configuration/options#session "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-3 "Direct link to heading")

`session` 객체와 그 안의 모든 속성은 선택 사항입니다.

이 옵션의 기본값은 아래와 같습니다.

```
    session: {
      // Use JSON Web Tokens for session instead of database sessions.
      // This option can be used with or without a database for users/accounts.
      // Note: `jwt` is automatically set to `true` if no database is specified.
      jwt: false,

      // Seconds - How long until an idle session expires and is no longer valid.
      maxAge: 30 * 24 * 60 * 60, // 30 days

      // Seconds - Throttle how frequently to write to database to extend a session.
      // Use it to limit write operations. Set to 0 to always update the database.
      // Note: This option is ignored if using JSON Web Tokens
      updateAge: 24 * 60 * 60, // 24 hours
    }

```

---

### jwt[​](https://next-auth.js.org/v3/configuration/options#jwt "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-4 "Direct link to heading")

`session: { jwt: true }` 옵션을 활성화하면 세션 토큰으로 JSON Web Token을 사용할 수 있습니다. 데이터베이스를 지정하지 않은 경우 기본적으로 JSON Web Token이 활성화됩니다.

기본적으로 JSON Web Token은 암호화(JWE)되지 않고 서명(JWS)만 됩니다. JWT 암호화는 추가 오버헤드를 유발하고 몇 가지 주의사항이 있기 때문입니다. `encryption: true`를 설정하면 암호화를 활성화할 수 있습니다.

#### JSON Web Token 옵션[​](https://next-auth.js.org/v3/configuration/options#json-web-token-options "Direct link to heading")

```
    jwt: {
      // A secret to use for key generation - you should set this explicitly
      // Defaults to NextAuth.js secret if not explicitly specified.
      // This is used to generate the actual signingKey and produces a warning
      // message if not defined explicitly.
      // secret: 'INp8IvdIyeMcoGAgFGoA61DdBglwwSqnXJZkgz8PSnw',
      // You can generate a signing key using `jose newkey -s 512 -t oct -a HS512`
      // This gives you direct knowledge of the key used to sign the token so you can use it
      // to authenticate indirectly (eg. to a database driver)
      // signingKey: {"kty":"oct","kid":"Dl893BEV-iVE-x9EC52TDmlJUgGm9oZ99_ZL025Hc5Q","alg":"HS512","k":"K7QqRmJOKRK2qcCKV_pi9PSBv3XP0fpTu30TP8xn4w01xR3ZMZM38yL2DnTVPVw6e4yhdh0jtoah-i4c_pZagA"},
      // If you chose something other than the default algorithm for the signingKey (HS512)
      // you also need to configure the algorithm
      // verificationOptions: {
      //    algorithms: ['HS256']
      // },
      // Set to true to use encryption. Defaults to false (signing only).
      // encryption: true,
      // encryptionKey: "",
      // decryptionKey = encryptionKey,
      // decryptionOptions = {
      //    algorithms: ['A256GCM']
      // },
      // You can define your own encode/decode functions for signing and encryption
      // if you want to override the default behaviour.
      // async encode({ secret, token, maxAge }) {},
      // async decode({ secret, token, maxAge }) {},
    }

```

JSON Web Token 예시는 다음과 같은 payload를 포함합니다.

```
    {
      name: 'Iain Collins',
      email: 'me@iaincollins.com',
      picture: 'https://example.com/image.jpg',
      iat: 1594601838,
      exp: 1597193838
    }

```

#### JWT 헬퍼[​](https://next-auth.js.org/v3/configuration/options#jwt-helper "Direct link to heading")

내장 `getToken()` 헬퍼 메서드를 사용해 다음과 같이 토큰을 검증하고 복호화할 수 있습니다.

```
    import jwt from "next-auth/jwt"

    const secret = process.env.JWT_SECRET

    export default async (req, res) => {
      const token = await jwt.getToken({ req, secret })
      console.log("JSON Web Token", token)
      res.end()
    }

```

_편의를 위해 이 헬퍼 함수는 HTTP Bearer 헤더로 전달된 토큰도 읽고 디코드할 수 있습니다._

**필수**

getToken() 헬퍼에는 다음 옵션이 필요합니다.

- `req` \- (object) Request 객체
- `secret` \- (string) JWT Secret

또한 헬퍼에 *`jwt` 옵션에 설정한 모든 옵션*도 함께 전달해야 합니다.

예: 커스텀 세션 `maxAge`, 커스텀 서명 및/또는 암호화 키나 옵션 포함

**선택**

다음 옵션도 지원합니다.

- `secureCookie` \- (boolean) secure 접두사가 붙은 쿠키 이름 사용

기본적으로 헬퍼 함수는 secure 접두사 쿠키를 사용해야 하는지 자동으로 판단합니다(예: 프로덕션에서는 `true`, 개발에서는 `false`, 단 NEXTAUTH_URL에 HTTPS URL이 포함된 경우 제외).

- `cookieName` \- (string) 세션 토큰 쿠키 이름

`cookieName`을 명시적으로 지정하면 `secureCookie` 옵션은 무시됩니다.

- `raw` \- (boolean) 원시 토큰 가져오기(디코드하지 않음)

`true`로 설정하면 복호화 또는 검증 없이 원시 토큰을 반환합니다.

note

JWT는 세션 토큰 쿠키에 저장되며, 데이터베이스 세션의 토큰과 동일한 쿠키를 사용합니다.

---

### pages[​](https://next-auth.js.org/v3/configuration/options#pages "Direct link to heading")

- **기본값** : `{}`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-5 "Direct link to heading")

커스텀 로그인, 로그아웃, 오류 페이지를 만들고 싶다면 사용할 URL을 지정하세요.

지정한 페이지는 해당 내장 페이지를 덮어씁니다.

_예:_

```
     pages: {
      signIn: '/auth/signin',
      signOut: '/auth/signout',
      error: '/auth/error', // Error code passed in query string as ?error=
      verifyRequest: '/auth/verify-request', // (used for check email message)
      newUser: null // If set, new users will be directed here on first sign in
    }

```

자세한 내용은 [pages 옵션](https://next-auth.js.org/configuration/pages) 문서를 참고하세요.

---

### callbacks[​](https://next-auth.js.org/v3/configuration/options#callbacks "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-6 "Direct link to heading")

콜백은 액션이 수행될 때의 동작을 제어하는 데 사용할 수 있는 비동기 함수입니다.

콜백은 매우 강력하며, 특히 JSON Web Token을 사용하는 시나리오에서 데이터베이스 없이 접근 제어를 구현하거나 외부 데이터베이스/API와 통합할 수 있게 해줍니다.

아래 콜백들 중 원하는 항목의 핸들러를 지정할 수 있습니다.

```
    callbacks: {
      async signIn(user, account, profile) {
        return true
      },
      async redirect(url, baseUrl) {
        return baseUrl
      },
      async session(session, user) {
        return session
      },
      async jwt(token, user, account, profile, isNewUser) {
        return token
      }
    }

```

콜백 함수 사용 방법에 대한 자세한 내용은 [callbacks 문서](https://next-auth.js.org/configuration/callbacks)를 참고하세요.

---

### events[​](https://next-auth.js.org/v3/configuration/options#events "Direct link to heading")

- **기본값** : `object`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-7 "Direct link to heading")

이벤트는 응답을 반환하지 않는 비동기 함수이며, 감사 로그에 유용합니다.

아래 이벤트들 중 원하는 항목의 핸들러를 지정할 수 있습니다. 예: 디버깅 또는 감사 로그 생성.

메시지 객체의 내용은 흐름에 따라 달라집니다(예: OAuth 또는 Email 인증 흐름, JWT 또는 데이터베이스 세션 등). 각 메시지 객체의 형태와 이벤트 함수 사용 방법은 [events 문서](https://next-auth.js.org/configuration/events)를 참고하세요.

```
    events: {
      async signIn(message) { /* on successful sign in */ },
      async signOut(message) { /* on signout */ },
      async createUser(message) { /* user created */ },
      async updateUser(message) { /* user updated - e.g. their email was verified */ },
      async linkAccount(message) { /* account (e.g. Twitter) linked to a user */ },
      async session(message) { /* session is active */ },
      async error(message) { /* error in authentication flow */ }
    }

```

---

### adapter[​](https://next-auth.js.org/v3/configuration/options#adapter "Direct link to heading")

- **기본값** : _Adapter.Default()_
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-8 "Direct link to heading")

기본적으로 NextAuth.js는 TypeORM 기반 데이터베이스 어댑터를 사용하며 MySQL, MariaDB, Postgres, MongoDB, SQLite를 지원합니다. 현재 MySQL, MariaDB, Postgres를 지원하는 Prisma 기반 대체 어댑터도 포함되어 있습니다.

`adapter` 옵션으로 Prisma 어댑터를 사용하거나, 내장 어댑터가 지원하지 않는 데이터베이스를 쓰고 싶다면 직접 어댑터를 전달할 수 있습니다.

자세한 내용은 [adapter 문서](https://authjs.dev/reference/adapters)를 참고하세요.

note

`adapter` 옵션을 지정하면 `database` 옵션보다 우선 적용되므로, 둘 중 하나만 지정하세요.

---

### debug[​](https://next-auth.js.org/v3/configuration/options#debug "Direct link to heading")

- **기본값** : `false`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-9 "Direct link to heading")

인증 및 데이터베이스 작업의 디버그 메시지를 활성화하려면 debug를 `true`로 설정하세요.

---

### logger[​](https://next-auth.js.org/v3/configuration/options#logger "Direct link to heading")

- **기본값** : `console`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-10 "Direct link to heading")

logger 레벨을 원하는 대로 오버라이드하고(`undefined` 레벨은 내장 logger 사용), NextAuth 로그를 가로챌 수 있습니다. 이를 통해 NextAuth.js 로그를 서드파티 로깅 서비스로 보낼 수 있습니다.

예시:

/pages/api/auth/[...nextauth].js

```
    import log from "logging-service"

    export default NextAuth({
      ...
      logger: {
        error(code, ...message) {
          log.error(code, message)
        },
        warn(code, ...message) {
          log.warn(code, message)
        },
        debug(code, ...message) {
          log.debug(code, message)
        }
      }
      ...
    })

```

note

사용자가 `debug` 레벨을 정의하면 `debug: false` [option](https://next-auth.js.org/v3/configuration/options#debug)과 무관하게 호출됩니다.

---

### theme[​](https://next-auth.js.org/v3/configuration/options#theme "Direct link to heading")

- **기본값** : `"auto"`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-11 "Direct link to heading")

[pages](https://next-auth.js.org/configuration/pages)의 테마를 변경합니다. 페이지를 항상 라이트로 강제하려면 `"light"`로 설정하세요. 페이지를 항상 다크로 강제하려면 `"dark"`로 설정하세요. 시스템 선호 테마를 따르게 하려면 `"auto"`로 설정(또는 이 옵션 생략)하세요. ([prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 쿼리를 사용합니다.)

---

## 고급 옵션[​](https://next-auth.js.org/v3/configuration/options#advanced-options "Direct link to heading")

고급 옵션은 기본 옵션과 동일한 방식으로 전달되지만, 복잡한 영향이나 부작용이 있을 수 있습니다. 사용에 매우 익숙하지 않다면 고급 옵션 사용은 피하는 것이 좋습니다.

---

### useSecureCookies[​](https://next-auth.js.org/v3/configuration/options#usesecurecookies "Direct link to heading")

- **기본값** : HTTPS 사이트는 `true` / HTTP 사이트는 `false`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-12 "Direct link to heading")

`true`로 설정하면(`https://`로 시작하는 모든 사이트 URL의 기본값), NextAuth.js가 설정하는 모든 쿠키는 HTTPS URL에서만 접근할 수 있습니다.

개발 편의를 위해 `http://`로 시작하는 URL(예: `http://localhost:3000`)에서는 이 옵션의 기본값이 `false`입니다.

이 보안 기능을 비활성화하고 보안되지 않은 URL에서도 쿠키 접근을 허용하려면 이 옵션을 수동으로 `false`로 설정할 수 있습니다(권장하지 않음).

note

지정한 커스텀 `cookies`의 속성은 이 옵션을 덮어씁니다.

danger

프로덕션에서 이 옵션을 *false*로 설정하는 것은 보안 위험이며, 실제 운영 환경에서 세션 하이재킹을 허용할 수 있습니다. 이 옵션은 개발 및 테스트 지원용입니다. 사용을 권장하지 않습니다.

---

### cookies[​](https://next-auth.js.org/v3/configuration/options#cookies "Direct link to heading")

- **기본값** : `{}`
- **필수** : _아니요_

#### 설명[​](https://next-auth.js.org/v3/configuration/options#description-13 "Direct link to heading")

NextAuth.js에서 사용하는 쿠키의 기본 이름과 옵션을 재정의할 수 있습니다.

이것은 고급 옵션이며, 사용하면 인증이 깨지거나 애플리케이션에 보안 취약점이 생길 수 있으므로 권장되지 않습니다.

하나 이상의 쿠키에 사용자 지정 속성을 지정할 수 있지만, 특정 쿠키에 사용자 지정 옵션을 지정하는 경우 해당 쿠키의 모든 옵션을 제공해야 합니다.

이 기능을 사용하면 내장된 동적 정책을 사용하지 않게 되므로, 개발 빌드와 프로덕션 빌드에서 서로 다른 쿠키 정책을 설정할 수 있도록 조건부 동작을 만드는 것이 필요할 수 있습니다.

tip

이 옵션의 사용 사례 예시 중 하나는 서브도메인 간 세션 토큰 공유를 지원하는 것입니다.

#### 예시[​](https://next-auth.js.org/v3/configuration/options#example "Direct link to heading")

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
          secure: useSecureCookies
        }
      }
    }

```

danger

사용자 지정 쿠키 정책을 사용하면 애플리케이션에 보안 취약점이 생길 수 있으며, 그 영향을 이해하는 고급 사용자를 위한 옵션입니다. 이 옵션 사용은 권장되지 않습니다.
