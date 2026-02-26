---
title: "Errors"
description: "다음은 NextAuth.js에서 출력되는 오류 목록입니다."
---

Source URL: https://next-auth.js.org/errors

# Errors | NextAuth.js

버전: v4

다음은 NextAuth.js에서 출력되는 오류 목록입니다.

모든 오류는 예상치 못한 문제를 나타내며, 일반적으로 오류가 나타나는 것을 기대하면 안 됩니다.

콘솔에서 이러한 오류가 보인다면 무언가 잘못된 상태입니다.

---

## Client[​](https://next-auth.js.org/errors#client "Direct link to heading")

이 오류들은 클라이언트에서 반환됩니다. 클라이언트는 [Universal JavaScript (or "Isomorphic JavaScript")](https://en.wikipedia.org/wiki/Isomorphic_JavaScript)이므로 클라이언트와 서버 모두에서 실행될 수 있어, 터미널과 브라우저 콘솔 양쪽에서 이러한 오류가 발생할 수 있습니다.

#### CLIENT_SESSION_ERROR[​](https://next-auth.js.org/errors#client_session_error "Direct link to heading")

`SessionProvider` Context가 세션 데이터를 가져오는 과정에서 문제가 있을 때 발생합니다.

#### CLIENT_FETCH_ERROR[​](https://next-auth.js.org/errors#client_fetch_error "Direct link to heading")

여러 이유로 발생할 수 있습니다. NextAuth.js를 올바르게 [configured](https://next-auth.js.org/configuration/initialization)했는지 확인하고, [`NEXTAUTH_URL`](https://next-auth.js.org/configuration/options#nextauth_url)을 사용했다면 올바르게 설정되어 있는지 확인하세요.

---

## Server[​](https://next-auth.js.org/errors#server "Direct link to heading")

이 오류들은 터미널에 표시됩니다.

### OAuth[​](https://next-auth.js.org/errors#oauth "Direct link to heading")

#### OAUTH_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/errors#oauth_get_access_token_error "Direct link to heading")

OAuth provider로 보내는 POST 요청에서 오류가 발생해 access token을 가져오지 못했을 때 발생합니다.

provider 설정을 다시 확인하세요.

#### OAUTH_V1_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/errors#oauth_v1_get_access_token_error "Direct link to heading")

이 오류는 오래된 OAuth v1.x provider와 명시적으로 관련되어 있습니다. 이를 사용 중이라면 가능한 모든 설정을 다시 확인하세요.

#### OAUTH_GET_PROFILE_ERROR[​](https://next-auth.js.org/errors#oauth_get_profile_error "Direct link to heading")

N/A

#### OAUTH_PARSE_PROFILE_ERROR[​](https://next-auth.js.org/errors#oauth_parse_profile_error "Direct link to heading")

이 오류는 provider 응답에 문제가 있거나 사용자가 provider에서 작업을 취소했을 때 발생할 수 있습니다. 안타깝게도 현재 정보만으로는 어느 쪽인지 구분할 수 없습니다.

이 오류가 발생하면 디버깅에 도움이 되도록 예외와 사용 가능한 `profileData`도 함께 로그에 남겨야 합니다.

#### OAUTH_CALLBACK_HANDLER_ERROR[​](https://next-auth.js.org/errors#oauth_callback_handler_error "Direct link to heading")

예를 들어 JSON request body를 파싱하는 데 문제가 있을 때 발생합니다.

이 오류가 발생하면 디버깅을 돕기 위해 오류가 발생한 내용과 request body 자체 같은 추가 세부 정보도 로그에 남아야 합니다.

---

### Signin / Callback[​](https://next-auth.js.org/errors#signin--callback "Direct link to heading")

#### SIGNIN_OAUTH_ERROR[​](https://next-auth.js.org/errors#signin_oauth_error "Direct link to heading")

OAuth provider의 authorization URL로 리디렉션하는 중에 발생합니다. 가능한 원인은 다음과 같습니다.

1. Cookie 처리 내부 state에서 PKCE code verifier 또는 CSRF token hash 생성이 실패했습니다.

[`cookies` configuration](https://next-auth.js.org/configuration/options#cookies)이 설정되어 있다면 확인하고, 브라우저가 cookie를 차단/제한하고 있지 않은지 확인하세요.

2. OAuth 설정 오류

OAuth provider를 확인하고 URL 및 기타 옵션이 올바르게 설정되어 있는지 확인하세요.

OAuth v1 provider를 사용 중이라면 OAuth v1 provider 설정, 특히 OAuth token과 OAuth token secret을 확인하세요.

3. `openid-client` 버전 불일치

`expected 200 OK with body but no body was returned`가 보인다면, `openid-client`(의존성으로 사용 중)와 node 버전 불일치 때문일 수 있습니다. 예를 들어 `openid-client`는 `lts/fermium`에 대해 `>=14.2.0`을 요구하며, 다른 버전에도 유사한 제한이 있습니다. 호환되는 node 버전 전체 목록은 [package.json](https://github.com/panva/node-openid-client/blob/2a84e46992e1ebeaf685c3f87b65663d126e81aa/package.json#L78)을 참고하세요.

#### OAUTH_CALLBACK_ERROR[​](https://next-auth.js.org/errors#oauth_callback_error "Direct link to heading")

콜백 처리 중 `code_verifier` cookie를 찾지 못했거나 OAuth provider에서 잘못된 state가 반환되면 발생할 수 있습니다.

#### SIGNIN_EMAIL_ERROR[​](https://next-auth.js.org/errors#signin_email_error "Direct link to heading")

사용자가 이메일 링크로 로그인하려고 할 때 발생할 수 있습니다. 예를 들어 이메일 token을 생성할 수 없거나 verification 요청이 실패한 경우입니다.

이메일 설정을 다시 확인하세요.

#### CALLBACK_EMAIL_ERROR[​](https://next-auth.js.org/errors#callback_email_error "Direct link to heading")

이메일 콜백 처리 중 발생할 수 있습니다. 구체적으로 이메일로 사용자 로그인 처리, jwt 인코딩 등에서 오류가 난 경우입니다.

Email 설정을 다시 확인하세요.

#### EMAIL_REQUIRES_ADAPTER_ERROR[​](https://next-auth.js.org/errors#email_requires_adapter_error "Direct link to heading")

Email authentication provider는 데이터베이스가 설정된 경우에만 사용할 수 있습니다.

verification token 저장을 위해 필요합니다. 자세한 내용은 [email provider](https://next-auth.js.org/providers/email#configuration)를 참고하세요.

#### CALLBACK_CREDENTIALS_JWT_ERROR[​](https://next-auth.js.org/errors#callback_credentials_jwt_error "Direct link to heading")

Credentials Provider는 세션에 JSON Web Tokens를 사용하는 경우에만 사용할 수 있습니다.

데이터베이스를 지정하지 않았다면 기본적으로 세션에 JSON Web Tokens가 사용됩니다. 하지만 데이터베이스를 사용 중이면 기본적으로 Database Sessions가 활성화되므로, Credentials Provider를 사용하려면 [explicitly enable JWT Sessions](https://next-auth.js.org/configuration/options#session) 해야 합니다.

Credentials Provider를 사용하는 경우 NextAuth.js는 사용자나 세션을 데이터베이스에 영속 저장하지 않습니다. Credentials Provider에서 사용하는 사용자 계정은 NextAuth.js 외부에서 생성하고 관리해야 합니다.

_대부분의 경우_ NextAuth.js 옵션에서 데이터베이스를 지정하면서 Credentials Provider를 함께 지원하는 것은 타당하지 않습니다.

#### CALLBACK_CREDENTIALS_HANDLER_ERROR[​](https://next-auth.js.org/errors#callback_credentials_handler_error "Direct link to heading")

credential authentication provider에 `authorize()` handler가 정의되어 있지 않으면 발생합니다.

#### PKCE_ERROR[​](https://next-auth.js.org/errors#pkce_error "Direct link to heading")

사용하려던 provider가 [PKCE or Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636#section-4)를 설정하는 과정에서 실패했습니다. `code_verifier`는 (기본값 기준) `__Secure-next-auth.pkce.code_verifier`라는 cookie에 저장되며 15분 후 만료됩니다. `cookies.pkceCodeVerifier`가 올바르게 설정되어 있는지 확인하세요.

기본 `code_challenge_method`는 `"S256"`입니다. 현재 이는 `"plain"`으로 설정할 수 없으며, [as per RFC7636](https://datatracker.ietf.org/doc/html/rfc7636#section-4.2):

> 클라이언트가 "S256"을 사용할 수 있다면 반드시 "S256"을 사용해야 하며, "S256"은 서버에서 필수 구현(MTI)입니다.

#### INVALID_CALLBACK_URL_ERROR[​](https://next-auth.js.org/errors#invalid_callback_url_error "Direct link to heading")

제공된 `callbackUrl`이 유효하지 않거나 정의되지 않았습니다. 자세한 내용은 [specifying a `callbackUrl`](https://next-auth.js.org/getting-started/client#specifying-a-callbackurl)을 참고하세요.

---

### Session Handling[​](https://next-auth.js.org/errors#session-handling "Direct link to heading")

#### JWT_SESSION_ERROR[​](https://next-auth.js.org/errors#jwt_session_error "Direct link to heading")

JWEDecryptionFailed: NextAuth.js는 JWT를 암호화하고 이메일 verification token을 해시하기 위해 `NEXTAUTH_SECRET` environment variable이 필요합니다. `NEXTAUTH_SECRET`을 변경했지만 이전 secret으로 활성 세션이 남아 있는 경우에도 발생할 수 있습니다. 다시 로그인하면 문제가 해결됩니다.

JWTKeySupport: the key does not support HS512 verify algorithm

키 생성에 사용된 알고리즘이 지원 목록에 없습니다. 다음을 사용해 HS512 키를 생성할 수 있습니다.

```
      jose newkey -s 512 -t oct -a HS512

```

#### SESSION_ERROR[​](https://next-auth.js.org/errors#session_error "Direct link to heading")

---

### Signout[​](https://next-auth.js.org/errors#signout "Direct link to heading")

#### SIGNOUT_ERROR[​](https://next-auth.js.org/errors#signout_error "Direct link to heading")

예를 들어 데이터베이스에서 세션을 삭제하는 데 문제가 있을 때 발생합니다.

---

### Configuration[​](https://next-auth.js.org/errors#configuration "Direct link to heading")

#### MISSING_NEXTAUTH_API_ROUTE_ERROR[​](https://next-auth.js.org/errors#missing_nextauth_api_route_error "Direct link to heading")

`pages/api/auth` 내부에서 `[...nextauth].js` 파일을 찾지 못했을 때 발생합니다.

파일이 해당 위치에 있는지, 파일명이 올바른지 확인하세요.

#### NO_SECRET[​](https://next-auth.js.org/errors#no_secret "Direct link to heading")

프로덕션에서는 설정에 `secret` 속성을 정의해야 합니다. 개발 환경에서는 편의를 위해 경고로 표시됩니다. [Read more](https://next-auth.js.org/configuration/options#secret)

#### AUTH_ON_ERROR_PAGE_ERROR[​](https://next-auth.js.org/errors#auth_on_error_page_error "Direct link to heading")

오류로 인해 렌더링된 custom error page가 정의되어 있지만, 해당 페이지에도 인증이 필요하도록 되어 있습니다. 무한 리디렉션 루프를 피하기 위해 NextAuth.js는 처리를 중단하고 기본 error page를 대신 렌더링했습니다.

Middleware를 사용 중이라면 `middleware.ts`와 `[...nextauth].ts` 파일에 동일한 `pages` configuration이 포함되어 있는지 확인하세요. 또는 `matcher` 옵션을 사용해 특정 사이트에서만 인증을 요구하고(custom error page는 제외) 설정하세요.

Middleware를 사용하지 않는다면 custom error page 접근 시 사용자를 sign-in page로 리디렉션하려고 하지 않는지 확인하세요.

유용한 링크:

- <https://next-auth.js.org/configuration/nextjs#pages>
- <https://next-auth.js.org/configuration/pages>
- <https://nextjs.org/docs/advanced-features/middleware#matcher>
