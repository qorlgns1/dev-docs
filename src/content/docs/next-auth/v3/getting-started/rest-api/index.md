---
title: "REST API"
description: "NextAuth.js는 NextAuth.js 클라이언트에서 사용하는 REST API를 제공합니다."
---

Source URL: https://next-auth.js.org/v3/getting-started/rest-api

# REST API | NextAuth.js

버전: v3

NextAuth.js는 NextAuth.js 클라이언트에서 사용하는 REST API를 제공합니다.

#### `GET` /api/auth/signin[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsignin "Direct link to heading")

로그인 페이지를 표시합니다.

#### `POST` /api/auth/signin/:provider[​](https://next-auth.js.org/v3/getting-started/rest-api#post-apiauthsigninprovider "Direct link to heading")

지정한 provider에 대한 OAuth 로그인 플로우를 시작합니다.

`POST` 요청에는 `/api/auth/csrf`에서 발급한 CSRF 토큰이 필요합니다.

#### `GET` /api/auth/callback/:provider[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthcallbackprovider "Direct link to heading")

로그인 중 OAuth 서비스에서 돌아오는 요청을 처리합니다.

`state` 옵션을 지원하는 OAuth 2.0 provider의 경우, `state` 파라미터 값은 로그인 플로우 시작 시 생성된 값과 대조됩니다. 이 과정은 CSRF 토큰의 해시를 사용하며, 로그인 중의 POST 요청과 `GET` 요청 모두에서 반드시 일치해야 합니다.

#### `GET` /api/auth/signout[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsignout "Direct link to heading")

로그아웃 페이지를 표시합니다.

#### `POST` /api/auth/signout[​](https://next-auth.js.org/v3/getting-started/rest-api#post-apiauthsignout "Direct link to heading")

로그아웃을 처리합니다. 이는 악성 링크가 사용자 동의 없이 로그아웃을 유도하지 못하도록 `POST` 요청으로 처리됩니다.

`POST` 요청에는 `/api/auth/csrf`에서 발급한 CSRF 토큰이 필요합니다.

#### `GET` /api/auth/session[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthsession "Direct link to heading")

클라이언트에 안전한 세션 객체를 반환하며, 세션이 없으면 빈 객체를 반환합니다.

반환되는 세션 객체의 내용은 session callback으로 구성할 수 있습니다.

#### `GET` /api/auth/csrf[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthcsrf "Direct link to heading")

CSRF 토큰이 포함된 객체를 반환합니다. NextAuth.js에서는 모든 인증 라우트에 CSRF 보호가 적용됩니다. 이 보호는 서명된 HttpOnly, host-only 쿠키를 사용하는 "double submit cookie method"를 사용합니다.

이 엔드포인트에서 반환된 CSRF 토큰은 모든 API 엔드포인트로 보내는 모든 `POST` 요청에서 `csrfToken`이라는 이름의 form 변수로 전달되어야 합니다.

#### `GET` /api/auth/providers[​](https://next-auth.js.org/v3/getting-started/rest-api#get-apiauthproviders "Direct link to heading")

구성된 OAuth 서비스 목록과 각 서비스의 세부 정보(예: 로그인 및 callback URL)를 반환합니다.

동적으로 커스텀 회원가입 페이지를 생성하거나, 구성된 각 OAuth provider에 대해 어떤 callback URL이 설정되어 있는지 확인하는 데 사용할 수 있습니다.

---

참고

기본 base path는 `/api/auth`이며, `NEXTAUTH_URL`에 커스텀 경로를 지정해 변경할 수 있습니다.

예:

`NEXTAUTH_URL=https://example.com/myapp/api/authentication`

`/api/auth/signin` -> `/myapp/api/authentication/signin`
