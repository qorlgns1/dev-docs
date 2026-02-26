---
title: "REST API"
description: "NextAuth.js는 NextAuth.js 클라이언트에서 사용하는 REST API를 제공합니다."
---

Source URL: https://next-auth.js.org/getting-started/rest-api

# REST API | NextAuth.js

버전: v4

NextAuth.js는 NextAuth.js 클라이언트에서 사용하는 REST API를 제공합니다.

#### `GET` /api/auth/signin[​](https://next-auth.js.org/getting-started/rest-api#get-apiauthsignin "Direct link to heading")

기본 제공되는(브랜드 미적용) 로그인 페이지를 표시합니다.

#### `POST` /api/auth/signin/:provider[​](https://next-auth.js.org/getting-started/rest-api#post-apiauthsigninprovider "Direct link to heading")

provider별 로그인 플로우를 시작합니다.

`POST` 제출에는 `/api/auth/csrf`의 CSRF 토큰이 필요합니다.

OAuth provider의 경우, 이 엔드포인트를 호출하면 Identity Provider로 Authorization Request가 시작됩니다. 자세한 내용은 [OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1)을 참고하세요.

Email provider를 사용하는 경우, 이 엔드포인트를 호출하면 사용자 이메일 주소로 로그인 URL을 전송합니다.

이 엔드포인트는 내부적으로 [`signIn`](https://next-auth.js.org/getting-started/client#signin) 메서드에서도 사용됩니다.

#### `GET`/`POST` /api/auth/callback/:provider[​](https://next-auth.js.org/getting-started/rest-api#getpost-apiauthcallbackprovider "Direct link to heading")

로그인 중 OAuth 서비스에서 반환되는 요청을 처리합니다.

`checks: ["state"]` 옵션을 지원하는 OAuth 2.0 provider의 경우, state 파라미터를 로그인 플로우 시작 시 생성된 값과 대조합니다. 이 과정에서는 CSRF 토큰의 해시를 사용하며, 로그인 중 `POST`와 `GET` 호출 모두에서 반드시(MUST) 일치해야 합니다.

자세한 내용은 [OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2)을 참고하세요.

#### `GET` /api/auth/signout[​](https://next-auth.js.org/getting-started/rest-api#get-apiauthsignout "Direct link to heading")

기본 제공되는(브랜드 미적용) 로그아웃 페이지를 표시합니다.

#### `POST` /api/auth/signout[​](https://next-auth.js.org/getting-started/rest-api#post-apiauthsignout "Direct link to heading")

사용자 로그아웃을 처리합니다. 이는 악성 링크가 사용자 동의 없이 로그아웃을 유발하지 못하도록 `POST`로 제출됩니다. 사용자 세션은 [store sessions](https://next-auth.js.org/configuration/options#session) 방식 설정에 따라 cookie/database에서 무효화되거나 제거됩니다.

`POST` 제출에는 `/api/auth/csrf`의 CSRF 토큰이 필요합니다.

이 엔드포인트는 내부적으로 [`signOut`](https://next-auth.js.org/getting-started/client#signout) 메서드에서도 사용됩니다.

#### `GET` /api/auth/session[​](https://next-auth.js.org/getting-started/rest-api#get-apiauthsession "Direct link to heading")

클라이언트에 안전한 session object를 반환하며, 세션이 없으면 빈 객체를 반환합니다.

반환되는 session object의 내용은 [`session` callback](https://next-auth.js.org/configuration/callbacks#session-callback)으로 설정할 수 있습니다.

#### `GET` /api/auth/csrf[​](https://next-auth.js.org/getting-started/rest-api#get-apiauthcsrf "Direct link to heading")

CSRF 토큰이 포함된 객체를 반환합니다. NextAuth.js에서는 모든 인증 라우트에 CSRF 보호가 적용됩니다. "double submit cookie method"를 사용하며, 서명된 HttpOnly host-only cookie를 사용합니다.

이 엔드포인트에서 반환된 CSRF 토큰은 모든 API 엔드포인트에 대한 모든 `POST` 제출에서 `csrfToken`이라는 이름의 form 변수로 전달되어야 합니다.

#### `GET` /api/auth/providers[​](https://next-auth.js.org/getting-started/rest-api#get-apiauthproviders "Direct link to heading")

설정된 OAuth 서비스 목록과 각 서비스의 세부 정보(예: 로그인 및 callback URL)를 반환합니다.

커스텀 회원가입 페이지를 동적으로 생성하고, 설정된 각 OAuth provider의 callback URL 구성을 확인할 때 유용합니다.

---

참고

기본 base path는 `/api/auth`이지만 `NEXTAUTH_URL`에 커스텀 경로를 지정해 변경할 수 있습니다.

예:

`NEXTAUTH_URL=https://example.com/myapp/api/authentication`

`/api/auth/signin` -> `/myapp/api/authentication/signin`
