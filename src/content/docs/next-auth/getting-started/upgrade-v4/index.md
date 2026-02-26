---
title: "업그레이드 가이드 (v4)"
description: "원본 URL: https://next-auth.js.org/getting-started/upgrade-v4"
---

원본 URL: https://next-auth.js.org/getting-started/upgrade-v4

# 업그레이드 가이드 (v4) | NextAuth.js

버전: v4

NextAuth.js 버전 4에는 이전 메이저 버전(3.x) 대비 몇 가지 호환성 깨짐 변경 사항이 포함되어 있습니다. 그래서 여러분의 애플리케이션을 가능한 한 원활하게 업그레이드할 수 있도록 이 가이드를 준비했습니다. 아래 마이그레이션 단계를 따르면 3.x의 어떤 버전에서든 최신 4 릴리스로 업그레이드할 수 있습니다.

note

버전 4가 GA로 출시되었습니다 🚨

사용해 보시고, 발견하는 모든 이슈를 보고해 주시길 권장합니다.

다음 명령을 실행하여 새 버전으로 업그레이드할 수 있습니다:

- npm
- yarn
- pnpm

```
    npm install next-auth
```

```
    yarn add next-auth
```

```
    pnpm add next-auth
```

## `next-auth/jwt`[​](https://next-auth.js.org/getting-started/upgrade-v4#next-authjwt "헤딩으로 바로 가는 링크")

이제 `next-auth/jwt`에는 default export가 없습니다. 이에 맞추려면 다음과 같이 변경하세요:

```
    - import jwt from "next-auth/jwt"
    + import { getToken } from "next-auth/jwt"

```

## `next-auth/react`[​](https://next-auth.js.org/getting-started/upgrade-v4#next-authreact "헤딩으로 바로 가는 링크")

클라이언트 사이드 import 소스 이름이 `next-auth/react`로 변경되었습니다. 이 변경에 맞추려면 `next-auth/client`를 사용하던 모든 위치의 이름만 바꾸면 됩니다.

예를 들면:

```
    - import { useSession } from "next-auth/client"
    + import { useSession } from "next-auth/react"

```

또한 export 이름이 다음과 같이 변경되었습니다:

- `setOptions`: 더 이상 노출되지 않으며, [`SessionProvider` props](https://next-auth.js.org/getting-started/client#options)를 사용하세요
- `options`: 더 이상 노출되지 않으며, [`SessionProvider` props](https://next-auth.js.org/getting-started/client#options)를 사용하세요
- `session`: `getSession`으로 이름 변경
- `providers`: `getProviders`로 이름 변경
- `csrfToken`: `getCsrfToken`으로 이름 변경
- `signin`: `signIn`으로 이름 변경
- `signout`: `signOut`으로 이름 변경
- `Provider`: `SessionProvider`로 이름 변경

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.12>에서 도입됨

## `SessionProvider`[​](https://next-auth.js.org/getting-started/upgrade-v4#sessionprovider "헤딩으로 바로 가는 링크")

버전 4에서는 `SessionProvider` 사용이 필수가 되었습니다. 즉, `useSession`을 사용하는 애플리케이션의 모든 부분을 (아직 그렇게 하지 않았다면) 이 provider로 감싸야 합니다. `SessionProvider`에는 추가로 몇 가지 변경 사항이 있습니다:

- `Provider`가 `SessionProvider`로 이름 변경됨
- options prop이 이제 SessionProvider의 props로 평탄화됨
- `keepAlive`가 `refetchInterval`로 이름 변경됨
- `clientMaxAge`는 기능이 겹치는 `refetchInterval`로 대체되어 제거됨. 차이점은 `refetchInterval`이 백그라운드에서 주기적으로 세션을 계속 다시 가져온다는 점입니다.

앱을 Providers로 감쌀 때의 모범 사례는 `pages/_app.jsx` 파일에서 처리하는 것입니다.

이 새로운 변경 사항을 반영한 사용 예시:

```
    import { SessionProvider } from "next-auth/react"

    export default function App({
      Component,
      pageProps: { session, ...pageProps },
    }) {
      return (
        // `session` comes from `getServerSideProps` or `getInitialProps`.
        // Avoids flickering/session loading on first load.
      )
    }

```

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.12>에서 도입됨

## Providers[​](https://next-auth.js.org/getting-started/upgrade-v4#providers "헤딩으로 바로 가는 링크")

이제 Providers는 개별적으로 import해야 합니다.

```
    - import Provider from "next-auth/providers"
    - Providers.Auth0({...})
    - Providers.Google({...})
    + import Auth0Provider from "next-auth/providers/auth0"
    + import GoogleProvider from "next-auth/providers/google"
    + Auth0Provider({...})
    + GoogleProvider({...})

```

1. `AzureADB2C` provider는 `AzureAD`로 이름이 변경되었습니다.
2. `Basecamp` provider는 제거되었습니다. 설명은 [여기](https://github.com/basecamp/api/blob/master/sections/authentication.md#on-authenticating-users-via-oauth)를 참고하세요.
3. GitHub provider는 기본적으로 이제 사용자 프로필에 대한 전체 쓰기 권한을 요청하지 않습니다. 이 scope가 필요하다면 scope 옵션에 `user`를 수동으로 추가하세요.

구성에서 Providers를 정의할 때 다음의 새 옵션을 사용할 수 있습니다:

1. `authorization` (`authorizationUrl`, `authorizationParams`, `scope` 대체)
2. `token` (`accessTokenUrl`, `headers`, `params` 대체)
3. `userinfo` (`profileUrl` 대체)
4. `issuer`(`domain` 대체)

사용 방법에 대한 자세한 내용은 OAuth Provider 문서의 [options](https://next-auth.js.org/configuration/providers/oauth#options) 섹션을 참고하세요.

리포지토리에 새 OAuth provider를 제출할 때, 이제 `profile` 콜백은 `id`, `name`, `email`, `image` 필드만 반환해야 합니다. 이들 중 값이 없는 항목은 `null`로 설정해야 합니다.

또한 `id`는 `string` 타입으로 반환되어야 한다는 점도 중요합니다(예: provider가 숫자로 반환한다면 `.toString()` 메서드로 캐스팅할 수 있습니다). 이렇게 하면 반환된 profile 객체가 모든 providers/accounts/adapters 전반에서 일관성을 갖게 되어, 앞으로 혼동이 줄어들 것입니다.

구현: [#2411](https://github.com/nextauthjs/next-auth/pull/2411) 도입: <https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.20>

## `useSession` Hook[​](https://next-auth.js.org/getting-started/upgrade-v4#usesession-hook "헤딩으로 바로 가는 링크")

`useSession` 훅은 이제 객체를 반환하도록 업데이트되었습니다. 이를 통해 새 `status` 옵션으로 상태를 훨씬 깔끔하게 검사할 수 있습니다.

```
    - const [ session, loading ] = useSession()
    + const { data: session, status } = useSession()
    + const loading = status === "loading"

```

`session.status`와 `session.data`의 가능한 값은 [문서](https://next-auth.js.org/getting-started/client#usesession)를 확인하세요.

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.18>에서 도입됨

## Named Parameters[​](https://next-auth.js.org/getting-started/upgrade-v4#named-parameters "헤딩으로 바로 가는 링크")

콜백 인자를 named parameters 패턴으로 변경했습니다. 이제 더 이상 더미 `_` placeholder나 기타 트릭을 사용할 필요가 없습니다.

### Callbacks[​](https://next-auth.js.org/getting-started/upgrade-v4#callbacks "헤딩으로 바로 가는 링크")

콜백 메서드 시그니처는 이제 다음과 같습니다:

```
    - signIn(user, account, profileOrEmailOrCredentials)
    + signIn({ user, account, profile, email, credentials })

```

```
    - redirect(url, baseUrl)
    + redirect({ url, baseUrl })

```

```
    - session(session, tokenOrUser)
    + session({ session, token, user })

```

```
    - jwt(token, user, account, OAuthProfile, isNewUser)
    + jwt({ token, user, account, profile, isNewUser })

```

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.17>에서 도입됨

### Events[​](https://next-auth.js.org/getting-started/upgrade-v4#events "헤딩으로 바로 가는 링크")

두 이벤트 시그니처(`signOut`, `updateUser`)도 named parameters 패턴을 사용하도록 변경되었습니다.

```
    // [...nextauth].js
    ...
    events: {
    - signOut(tokenOrSession),
    + signOut({ token, session }), // token if using JWT, session if DB persisted sessions.
    - updateUser(user)
    + updateUser({ user })
    }

```

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.20>에서 도입됨

## JWT configuration[​](https://next-auth.js.org/getting-started/upgrade-v4#jwt-configuration "헤딩으로 바로 가는 링크")

JSON Web Tokens 사용 시 일부 [configuration options](https://next-auth.js.org/configuration/options)을 제거했습니다. 자세한 맥락은 [이 PR](https://github.com/nextauthjs/next-auth/pull/3039)을 참고하세요.

```
    export default NextAuth({
      // ...
      jwt: {
        secret,
        maxAge,
    -   encryptionKey
    -   signingKey
    -   encryptionKey
    -   verificationOptions
        encode({
            token
            secret
            maxAge
    -       signingKey
    -       signingOptions
    -       encryptionKey
    -       encryptionOptions
    -       encryption
        }) {},
        decode({
            token
            secret
    -       maxAge
    -       signingKey
    -       verificationKey
    -       verificationOptions
    -       encryptionKey
    -       decryptionKey
    -       decryptionOptions
    -       encryption
        }) {}
      }
    })

```

## Logger API[​](https://next-auth.js.org/getting-started/upgrade-v4#logger-api "헤딩으로 바로 가는 링크")

Logger API는 최대 두 개의 매개변수를 사용하도록 단순화되었습니다. 두 번째는 보통 `error` 객체를 포함하는 객체(`metadata`)입니다. logger 설정을 사용하지 않는다면 이 변경은 무시해도 됩니다.

```
    // [...nextauth.js]
    import log from "some-logger-service"
    ...
    logger: {
    - error(code, ...message) {},
    + error(code, metadata) {},
    - warn(code, ...message) {},
    + warn(code) {}
    - debug(code, ...message) {}
    + debug(code, metadata) {}
    }

```

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.19>에서 도입됨

## `nodemailer`[​](https://next-auth.js.org/getting-started/upgrade-v4#nodemailer "헤딩으로 바로 가는 링크")

`typeorm`, `prisma`와 마찬가지로 [`nodemailer`](https://npmjs.com/package/nodemailer)는 더 이상 기본 의존성에 포함되지 않습니다. Email provider를 사용 중이라면 프로젝트에 수동으로 설치하거나, [`sendVerificationRequest`](https://next-auth.js.org/configuration/providers/email#options-1#:~:text=sendVerificationRequest) 콜백에서 다른 Email 라이브러리를 사용해야 합니다. 이렇게 하면 실제로 Email provider를 사용하지 않는 사용자에게 번들 크기를 줄일 수 있습니다. Email provider 사용 시에는 매직 링크 기능이 동작하려면 verification token을 더 오래 저장해야 하므로 데이터베이스 adapter를 함께 사용하는 것이 필수라는 점을 기억하세요.

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.2>에서 도입됨

## Theme[​](https://next-auth.js.org/getting-started/upgrade-v4#theme "헤딩으로 바로 가는 링크")

`signin`, `signout` 같은 내장 페이지에 기본 커스터마이징 옵션을 추가했습니다.

이 옵션들은 `theme` 구성 키 아래에서 설정할 수 있습니다. 이전에는 색상 스킴 옵션만 제어하는 문자열이었지만, 이제는 다음 옵션을 가진 객체입니다:

```
    theme: {
      colorScheme: "auto", // "auto" | "dark" | "light"
      brandColor: "", // Hex color value
      logo: "" // Absolute URL to logo image
    }

```

최소한의 구성/커스터마이징 옵션만으로도 사용자가 즉시 내장 페이지를 직접 구현한 페이지로 교체해야 한다고 느끼지 않기를 기대합니다.

새 theme 옵션의 자세한 내용과 스크린샷은 [configuration/pages](https://next-auth.js.org/configuration/pages#theming)에서 확인할 수 있습니다.

도입: [#2788](https://github.com/nextauthjs/next-auth/pull/2788)

## Session[​](https://next-auth.js.org/getting-started/upgrade-v4#session "헤딩으로 바로 가는 링크")

`session.jwt: boolean` 옵션은 `session.strategy: "jwt" | "database"`로 이름이 변경되었습니다. 목표는 사용자 옵션을 더 직관적으로 만드는 것입니다:

1. 어댑터 없음, `strategy: "jwt"`: 기본값입니다. 세션은 쿠키에 저장되며 어디에도 영구 저장되지 않습니다.
2. 어댑터 사용, `strategy: "database"`: 어댑터가 정의되어 있으면 이 값이 암묵적 설정이 됩니다. 사용자 설정은 필요 없습니다.
3. 어댑터 사용, `strategy: "jwt"`: 데이터베이스를 사용할 수 있어도 사용자가 `next-auth`에 JWT 사용을 명시적으로 지시할 수 있습니다. 이는 보안 저하를 감수하는 대신 조회 속도를 높일 수 있습니다. 자세한 내용: <https://next-auth.js.org/faq#json-web-tokens>

예시:

```
    session: {
    - jwt: true,
    + strategy: "jwt",
    }

```

도입: [#3144](https://github.com/nextauthjs/next-auth/pull/3144)

## Adapters[​](https://next-auth.js.org/getting-started/upgrade-v4#adapters "헤딩으로 바로 가는 링크")

가장 중요한 점은, 핵심 `next-auth` 패키지에 더 이상 `typeorm`이나 기타 데이터베이스 adapter가 기본 포함되지 않는다는 것입니다. 이로 인해 사용자 데이터를 데이터베이스에 저장할 필요가 없는 경우 기본 번들 크기가 크게 줄어듭니다.

공식 Adapters는 기본 monorepo([nextauthjs/next-auth](https://github.com/nextauthjs/next-auth))의 `packages` 디렉터리에서 찾을 수 있습니다. 물론 새롭고 [단순화된 Adapter API](https://github.com/nextauthjs/next-auth/pull/2361)로 직접 [생성](https://next-auth.js.org/tutorials/creating-a-database-adapter)할 수도 있습니다.

`3.x.x` 또는 그 이전 버전의 NextAuth.js로 생성된 데이터베이스가 있다면, 스키마를 새 버전 4 데이터베이스 모델로 업데이트하기 위해 마이그레이션을 실행해야 합니다. 데이터베이스별 마이그레이션 예시는 이 가이드 하단을 참고하세요.

1. 내장 TypeORM 또는 Prisma adapter를 사용 중이라면, 이들은 핵심 `next-auth` 패키지에서 제거되었습니다. 다행히 마이그레이션은 간단하며, 데이터베이스에 맞는 외부 패키지를 설치하고 `[...nextauth].js`의 import를 변경하면 됩니다.

`database` 옵션은 제거되었으며, 이제 대신 다음과 같이 해야 합니다:

```
    // [...nextauth].js
    import NextAuth from "next-auth"
    + import { TypeORMLegacyAdapter } from "@next-auth/typeorm-legacy-adapter"

    ...
    export default NextAuth({
    -  database: "yourconnectionstring",
    +  adapter: TypeORMLegacyAdapter("yourconnectionstring")
    })

```

2. `prisma-legacy` adapter는 제거되었습니다. 대신 [`@next-auth/prisma-adapter`](https://npmjs.com/package/@next-auth/prisma-adapter)를 사용하세요.

3. `typeorm-legacy` adapter는 최신 adapter API를 사용하도록 업그레이드되었지만, 이름은 `typeorm-legacy`를 유지했습니다. 앞으로는 데이터베이스 유형별로 더 가벼운 개별 adapter로 마이그레이션하거나 `typeorm`을 대체하는 것을 목표로 합니다.

4. MongoDB는 `@next-auth/mongodb-adapter` 아래의 독립 adapter로 이동했습니다. [MongoDB Adapter 문서](https://authjs.dev/getting-started/adapters/mongodb)를 참고하세요.

<https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.8> 및 [#2361](https://github.com/nextauthjs/next-auth/pull/2361)에서 도입됨

### Adapter API[​](https://next-auth.js.org/getting-started/upgrade-v4#adapter-api "헤딩으로 바로 가는 링크")

**사용자 측 변경은 필요하지 않습니다 - 이 변경은 adapter 전용 변경 사항입니다**

Adapter API는 NextAuth.js v4에서 재작성되어 크게 단순화되었습니다. 이제 [verification token](https://authjs.dev/concepts/database-models#verificationtoken) 해싱 같은 일부 기능이 NextAuth 코어로 이동되어 adapter가 처리해야 할 작업이 줄어들었습니다.

어댑터 메인테이너이거나 직접 어댑터를 작성하려는 경우, 이 변경 사항에 대한 자세한 내용은 [#2361](https://github.com/nextauthjs/next-auth/pull/2361) 및 릴리스 <https://github.com/nextauthjs/next-auth/releases/tag/v4.0.0-next.22>에서 확인할 수 있습니다.

### 스키마 변경사항[​](https://next-auth.js.org/getting-started/upgrade-v4#schema-changes "Direct link to heading")

어댑터로 데이터를 저장하는 방식이 약간 변경되었습니다. 새로운 Adapter API에서는 추가 필드로 데이터베이스를 더 쉽게 확장할 수 있도록 하는 데 중점을 두었습니다. 예를 들어 User에 `phone` 필드가 추가로 필요하다면, 데이터베이스 스키마에 해당 필드만 추가하면 되고 어댑터는 변경할 필요가 없습니다.

- 모든 Model에서 `created_at`/`createdAt` 및 `updated_at`/`updatedAt` 필드가 제거되었습니다.
- `user_id`/`userId`는 일관되게 `userId`로 명명됩니다.
- Account에서 `compound_id`/`compoundId`가 제거되었습니다.
- Session에서 `access_token`/`accessToken`이 제거되었습니다.
- User의 `email_verified`/`emailVerified`는 일관되게 `emailVerified`로 명명됩니다.
- Account의 `provider_id`/`providerId`가 `provider`로 이름이 변경되었습니다.
- Account의 `provider_type`/`providerType`이 `type`으로 이름이 변경되었습니다.
- Account의 `provider_account_id`/`providerAccountId`는 일관되게 `providerAccountId`로 명명됩니다.
- Account의 `access_token_expires`/`accessTokenExpires`가 `expires_at`으로 이름이 변경되었습니다.
- Account에 새 필드가 추가되었습니다: `token_type`, `scope`, `id_token`, `session_state`
- `verification_requests` 테이블 이름이 `verification_tokens`로 변경되었습니다.

변경 사항 보기

```
    User {
      id
      name
      email
    + emailVerified
    - email_verified
      image
    -  created_at
    -  updated_at
    }

    Account {
      id
    - compound_id
    - user_id
    + userId
    -  provider_type
    + type
    - provider_id
    + provider
    - provider_account_id
    + providerAccountId
      refresh_token
      access_token
    - access_token_expires
    + expires_in
    + expires_at
    + token_type
    + scope
    + id_token
    + session_state
    - created_at
    - updated_at
    }

    Session {
      id
      userId
      expires
      sessionToken
    - access_token
    - created_at
    - updated_at
    }

    VerificationToken {
      id
      token
      expires
      identifier
    -  created_at
    -  updated_at
    }

```

`

자세한 내용은 [Models page](https://authjs.dev/concepts/database-models)를 참고하세요.

### 데이터베이스 마이그레이션[​](https://next-auth.js.org/getting-started/upgrade-v4#database-migration "Direct link to heading")

NextAuth.js v4는 v3와 비교해 데이터베이스 스키마가 약간 다릅니다. 어댑터를 사용 중이며 업그레이드하려는 경우, 아래 스키마 중 하나를 사용할 수 있습니다.

이 스키마들은 데이터베이스 자체에 직접 실행하도록 설계되었습니다. 따라서 Prisma 문법용 하나, TypeORM 문법용 하나처럼 나누는 대신, 기반 데이터베이스 유형별로 하나씩 제공하기로 했습니다. 즉 Postgres용 하나, MySQL용 하나, MongoDB용 하나입니다.

#### MySQL[​](https://next-auth.js.org/getting-started/upgrade-v4#mysql "Direct link to heading")

```
    /* ACCOUNT */
    ALTER TABLE accounts
    CHANGE "access_token_expires" "expires_at" int
    CHANGE "user_id" "userId" varchar(255)
    ADD CONSTRAINT fk_user_id FOREIGN KEY (userId) REFERENCES users(id)
    RENAME COLUMN "provider_id" "provider"
    RENAME COLUMN "provider_account_id" "providerAccountId"
    DROP COLUMN "provider_type"
    DROP COLUMN "compound_id"
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    DROP COLUMN "created_at"
    DROP COLUMN "updated_at"

    ADD COLUMN "token_type" varchar(255) NULL
    ADD COLUMN "scope" varchar(255) NULL
    ADD COLUMN "id_token" varchar(255) NULL
    ADD COLUMN "session_state" varchar(255) NULL

    /* Note: These are only needed if you're going to be using the old Twitter OAuth 1.0 provider. */
    ADD COLUMN "oauth_token_secret" varchar(255) NULL
    ADD COLUMN "oauth_token" varchar(255) NULL

    /* USER */
    ALTER TABLE users
    RENAME COLUMN "email_verified" "emailVerified"
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    DROP COLUMN "created_at"
    DROP COLUMN "updated_at"

    /* SESSION */
    ALTER TABLE sessions
    RENAME COLUMN "session_token" "sessionToken"
    CHANGE "user_id" "userId" varchar(255)
    ADD CONSTRAINT fk_user_id FOREIGN KEY (userId) REFERENCES users(id)
    DROP COLUMN "access_token"
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    DROP COLUMN "created_at"
    DROP COLUMN "updated_at"

    /* VERIFICATION REQUESTS */
    ALTER TABLE verification_requests RENAME verification_tokens
    ALTER TABLE verification_tokens
    DROP COLUMN id
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    DROP COLUMN "created_at"
    DROP COLUMN "updated_at"

```

#### Postgres[​](https://next-auth.js.org/getting-started/upgrade-v4#postgres "Direct link to heading")

```
    /* ACCOUNT */
    ALTER TABLE accounts RENAME COLUMN "user_id" TO "userId";
    ALTER TABLE accounts RENAME COLUMN "provider_id" TO "provider";
    ALTER TABLE accounts RENAME COLUMN "provider_account_id" TO "providerAccountId";
    ALTER TABLE accounts RENAME COLUMN "access_token_expires" TO "expires_at";
    ALTER TABLE accounts RENAME COLUMN "provider_type" TO "type";

    /* Do conversion of TIMESTAMPTZ to BIGINT */
    ALTER TABLE accounts ALTER COLUMN "expires_at" TYPE TEXT USING CAST(extract(epoch FROM "expires_at") AS BIGINT)*1000;

    /* Keep id as SERIAL with autoincrement when using ORM. Using new v4 uuid format won't work because of incompatibility */
    /* ALTER TABLE accounts ALTER COLUMN "id" TYPE TEXT; */
    /* ALTER TABLE accounts ALTER COLUMN "userId" TYPE TEXT; */
    ALTER TABLE accounts ALTER COLUMN "type" TYPE TEXT;
    ALTER TABLE accounts ALTER COLUMN "provider" TYPE TEXT;
    ALTER TABLE accounts ALTER COLUMN "providerAccountId" TYPE TEXT;

    ALTER TABLE accounts ADD CONSTRAINT fk_user_id FOREIGN KEY ("userId") REFERENCES users(id);
    ALTER TABLE accounts
    DROP COLUMN IF EXISTS "compound_id";
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    ALTER TABLE accounts
    DROP COLUMN IF EXISTS "created_at",
    DROP COLUMN IF EXISTS "updated_at";

    ALTER TABLE accounts
    ADD COLUMN IF NOT EXISTS "token_type" TEXT NULL,
    ADD COLUMN IF NOT EXISTS "scope" TEXT NULL,
    ADD COLUMN IF NOT EXISTS "id_token" TEXT NULL,
    ADD COLUMN IF NOT EXISTS "session_state" TEXT NULL;
    /* Note: These are only needed if you're going to be using the old Twitter OAuth 1.0 provider. */
    /* ALTER TABLE accounts
    ADD COLUMN IF NOT EXISTS "oauth_token_secret" TEXT NULL,
    ADD COLUMN IF NOT EXISTS "oauth_token" TEXT NULL; */

    /* USER */
    ALTER TABLE users RENAME COLUMN "email_verified" TO "emailVerified";

    /* Keep id as SERIAL with autoincrement when using ORM. Using new v4 uuid format won't work because of incompatibility */
    /* ALTER TABLE users ALTER COLUMN "id" TYPE TEXT; */
    ALTER TABLE users ALTER COLUMN "name" TYPE TEXT;
    ALTER TABLE users ALTER COLUMN "email" TYPE TEXT;
    ALTER TABLE users ALTER COLUMN "image" TYPE TEXT;
    /* Do conversion of TIMESTAMPTZ to BIGINT and then TEXT */
    ALTER TABLE users ALTER COLUMN "emailVerified" TYPE TEXT USING CAST(CAST(extract(epoch FROM "emailVerified") AS BIGINT)*1000 AS TEXT);
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    ALTER TABLE users
    DROP COLUMN IF EXISTS "created_at",
    DROP COLUMN IF EXISTS "updated_at";

    /* SESSION */
    ALTER TABLE sessions RENAME COLUMN "session_token" TO "sessionToken";
    ALTER TABLE sessions RENAME COLUMN "user_id" TO "userId";

    /* Keep id as SERIAL with autoincrement when using ORM. Using new v4 uuid format won't work because of incompatibility */
    /* ALTER TABLE sessions ALTER COLUMN "id" TYPE TEXT; */
    /* ALTER TABLE sessions ALTER COLUMN "userId" TYPE TEXT; */
    ALTER TABLE sessions ALTER COLUMN "sessionToken" TYPE TEXT;
    ALTER TABLE sessions ADD CONSTRAINT fk_user_id FOREIGN KEY ("userId") REFERENCES users(id);
    /* Do conversion of TIMESTAMPTZ to BIGINT and then TEXT */
    ALTER TABLE sessions ALTER COLUMN "expires" TYPE TEXT USING CAST(CAST(extract(epoch FROM "expires") AS BIGINT)*1000 AS TEXT);
    ALTER TABLE sessions DROP COLUMN IF EXISTS "access_token";
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    ALTER TABLE sessions
    DROP COLUMN IF EXISTS "created_at",
    DROP COLUMN IF EXISTS "updated_at";

    /* VERIFICATION REQUESTS */
    ALTER TABLE verification_requests RENAME TO verification_tokens;
    /* Keep id as ORM needs it */
    /* ALTER TABLE verification_tokens DROP COLUMN IF EXISTS id; */
    ALTER TABLE verification_tokens ALTER COLUMN "identifier" TYPE TEXT;
    ALTER TABLE verification_tokens ALTER COLUMN "token" TYPE TEXT;
    /* Do conversion of TIMESTAMPTZ to BIGINT and then TEXT */
    ALTER TABLE verification_tokens ALTER COLUMN "expires" TYPE TEXT USING CAST(CAST(extract(epoch FROM "expires") AS BIGINT)*1000 AS TEXT);
    /* The following two timestamp columns have never been necessary for NextAuth.js to function, but can be kept if you want */
    ALTER TABLE verification_tokens
    DROP COLUMN IF EXISTS "created_at",
    DROP COLUMN IF EXISTS "updated_at";

```

#### MongoDB[​](https://next-auth.js.org/getting-started/upgrade-v4#mongodb "Direct link to heading")

MongoDB는 문서형 데이터베이스이므로 새 필드는 자동으로 채워집니다. 다만 재사용될 기존 필드의 이름은 업데이트해야 합니다.

```
    db.getCollection('accounts').updateMany({}, {
      $rename: {
        "provider_id": "provider",
        "provider_account_id": "providerAccountId",
        "user_id": "userId",
        "access_token_expires": "expires_at"
      }
    })
    db.getCollection('users').updateMany({}, {
      $rename: {
        "email_verified": "emailVerified"
      }
    })
    db.getCollection('sessions').updateMany({}, {
      $rename: {
        "session_token": "sessionToken",
        "user_id": "userId"
      }
    })

```

## 누락된 `secret`[​](https://next-auth.js.org/getting-started/upgrade-v4#missing-secret "Direct link to heading")

이전에는 사용자가 `secret`을 정의하지 않아도 편의를 위해 NextAuth.js가 자동으로 secret을 생성했습니다. 개발 환경에서는 유용할 수 있지만, 운영 환경에서는 문제가 될 수 있습니다. 문서에서 이를 항상 명확히 안내해 왔지만, 이제부터는 운영 환경에서 `secret` 속성을 정의하지 않으면 사용자에게 오류 페이지가 표시됩니다. 이 옵션에 대한 자세한 내용은 [여기](https://next-auth.js.org/configuration/options#secret)를 참고하세요.

다음 명령으로 `secret` 설정 옵션에 넣을 secret을 생성할 수 있습니다:

```
    $ openssl rand -base64 32

```

따라서 NextAuth.js 설정은 대략 다음과 같아야 합니다:

/pages/api/auth/[...nextauth].js

```
    ...
    export default NextAuth({
      ...
      providers: [...],
      secret: "LlKq6ZtYbr+hTC073mAmAh9/h2HwMfsFo4hrfCx5mLg=",
      ...
    })

```

[#3143](https://github.com/nextauthjs/next-auth/issues/3143)에서 도입됨

## Session `strategy`[​](https://next-auth.js.org/getting-started/upgrade-v4#session-strategy "Direct link to heading")

우리는 항상 두 가지 session 전략을 지원해 왔습니다. 첫 번째는 가장 널리 사용되고 기본값인 JWT 기반 전략입니다. 두 번째는 데이터베이스 어댑터에 영속화되는 session 전략입니다. 각각 장단점이 있으며, [FAQ](https://next-auth.js.org/faq) 페이지에서 자세히 확인할 수 있습니다.

이전에는 `session` 옵션의 `jwt: boolean` 플래그로 이를 설정했습니다. 옵션에서 `session`과 `jwt`라는 이름이 다소 중복 사용되어 혼동될 수 있었기 때문에, 보다 명확한 의미 전달을 위해 이 옵션 이름을 `strategy: "jwt" | "database"`로 변경했으며 위치는 여전히 `session` 객체 안입니다. 이로써 이 옵션의 목적이 더 분명해지고 어떤 session 유형을 사용할지 명확히 드러나길 바랍니다.

자세한 내용은 [`session` option docs](https://next-auth.js.org/configuration/options#session)를 참고하세요.

[#3144](https://github.com/nextauthjs/next-auth/pull/3144)에서 도입됨

## 요약[​](https://next-auth.js.org/getting-started/upgrade-v4#summary "Direct link to heading")

이번 마이그레이션이 여러분 모두에게 원활하게 진행되기를 바랍니다! 질문이 있거나 진행 중 막히는 부분이 있다면 GitHub에 [새 이슈](https://github.com/nextauthjs/next-auth/issues/new)를 자유롭게 생성해 주세요.
