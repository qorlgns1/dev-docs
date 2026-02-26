---
title: 'Client[​](https://next-auth.js.org/v3/errors#client "제목으로 바로 가는 링크")'
description: "다음은 NextAuth.js에서 출력되는 오류 목록입니다."
---

Source URL: https://next-auth.js.org/v3/errors

# 오류 | NextAuth.js

버전: v3

다음은 NextAuth.js에서 출력되는 오류 목록입니다.

모든 오류는 예기치 않은 문제를 나타내며, 오류가 발생하는 상황은 정상으로 기대하면 안 됩니다.

콘솔에서 이러한 오류 중 하나라도 보인다면 무언가 잘못된 것입니다.

---

## Client[​](https://next-auth.js.org/v3/errors#client "제목으로 바로 가는 링크")

이 오류들은 클라이언트에서 반환됩니다. 클라이언트는 [Universal JavaScript (or "Isomorphic JavaScript")](https://en.wikipedia.org/wiki/Isomorphic_JavaScript)이므로 클라이언트 또는 서버에서 실행될 수 있어, 이 오류들은 터미널과 브라우저 콘솔 모두에서 발생할 수 있습니다.

#### CLIENT_USE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#client_use_session_error "제목으로 바로 가는 링크")

`useSession()` React Hook이 세션 데이터를 가져오는 과정에서 문제가 있을 때 이 오류가 발생합니다.

#### CLIENT_FETCH_ERROR[​](https://next-auth.js.org/v3/errors#client_fetch_error "제목으로 바로 가는 링크")

`CLIENT_FETCH_ERROR`가 보이면 `NEXTAUTH_URL` 환경 변수가 올바르게 설정되어 있는지 확인하세요.

---

## Server[​](https://next-auth.js.org/v3/errors#server "제목으로 바로 가는 링크")

이 오류들은 터미널에 표시됩니다.

### OAuth[​](https://next-auth.js.org/v3/errors#oauth "제목으로 바로 가는 링크")

#### OAUTH_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/v3/errors#oauth_get_access_token_error "제목으로 바로 가는 링크")

#### OAUTH_V1_GET_ACCESS_TOKEN_ERROR[​](https://next-auth.js.org/v3/errors#oauth_v1_get_access_token_error "제목으로 바로 가는 링크")

#### OAUTH_GET_PROFILE_ERROR[​](https://next-auth.js.org/v3/errors#oauth_get_profile_error "제목으로 바로 가는 링크")

#### OAUTH_PARSE_PROFILE_ERROR[​](https://next-auth.js.org/v3/errors#oauth_parse_profile_error "제목으로 바로 가는 링크")

#### OAUTH_CALLBACK_HANDLER_ERROR[​](https://next-auth.js.org/v3/errors#oauth_callback_handler_error "제목으로 바로 가는 링크")

---

### Signin / Callback[​](https://next-auth.js.org/v3/errors#signin--callback "제목으로 바로 가는 링크")

#### GET_AUTHORIZATION_URL_ERROR[​](https://next-auth.js.org/v3/errors#get_authorization_url_error "제목으로 바로 가는 링크")

#### SIGNIN_OAUTH_ERROR[​](https://next-auth.js.org/v3/errors#signin_oauth_error "제목으로 바로 가는 링크")

#### CALLBACK_OAUTH_ERROR[​](https://next-auth.js.org/v3/errors#callback_oauth_error "제목으로 바로 가는 링크")

#### SIGNIN_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#signin_email_error "제목으로 바로 가는 링크")

#### CALLBACK_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#callback_email_error "제목으로 바로 가는 링크")

#### EMAIL_REQUIRES_ADAPTER_ERROR[​](https://next-auth.js.org/v3/errors#email_requires_adapter_error "제목으로 바로 가는 링크")

Email 인증 Provider는 데이터베이스가 구성된 경우에만 사용할 수 있습니다.

#### CALLBACK_CREDENTIALS_JWT_ERROR[​](https://next-auth.js.org/v3/errors#callback_credentials_jwt_error "제목으로 바로 가는 링크")

Credentials Provider는 세션에 JSON Web Tokens를 사용하는 경우에만 사용할 수 있습니다.

데이터베이스를 지정하지 않았다면 기본적으로 세션에 JSON Web Tokens가 사용됩니다. 하지만 데이터베이스를 사용 중이라면 기본적으로 Database Sessions가 활성화되므로, Credentials Provider를 사용하려면 [JWT Sessions를 명시적으로 활성화](https://next-auth.js.org/configuration/options#session)해야 합니다.

Credentials Provider를 사용하는 경우, NextAuth.js는 사용자나 세션을 데이터베이스에 영속화하지 않습니다. Credentials Provider와 함께 사용하는 사용자 계정은 NextAuth.js 외부에서 생성 및 관리해야 합니다.

_대부분의 경우_ NextAuth.js 옵션에서 데이터베이스를 지정하면서 Credentials Provider도 함께 지원하는 것은 합리적이지 않습니다.

#### CALLBACK_CREDENTIALS_HANDLER_ERROR[​](https://next-auth.js.org/v3/errors#callback_credentials_handler_error "제목으로 바로 가는 링크")

#### PKCE_ERROR[​](https://next-auth.js.org/v3/errors#pkce_error "제목으로 바로 가는 링크")

사용하려던 provider가 [PKCE 또는 Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636#section-4.2)를 설정하는 과정에서 실패했습니다. `code_verifier`는 (기본적으로) `__Secure-next-auth.pkce.code_verifier`라는 쿠키에 저장되며 15분 후 만료됩니다. `cookies.pkceCodeVerifier`가 올바르게 구성되었는지 확인하세요. 기본 `code_challenge_method`는 `"S256"`입니다. `"plain"`은 권장되지 않으며 대부분의 경우 하위 호환성을 위해서만 지원되므로 현재 설정할 수 없습니다.

---

### Session Handling[​](https://next-auth.js.org/v3/errors#session-handling "제목으로 바로 가는 링크")

#### JWT_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#jwt_session_error "제목으로 바로 가는 링크")

<https://next-auth.js.org/errors#jwt_session_error> JWKKeySupport: the key does not support HS512 verify algorithm

키 생성에 사용된 알고리즘이 지원 목록에 없습니다. 다음을 사용해 HS512 키를 생성할 수 있습니다.

```
      jose newkey -s 512 -t oct -a HS512

```

HS512 키를 사용할 수 없는 경우(예: 다른 서비스와 상호 운용해야 하는 경우) 다음을 사용해 지원 대상을 정의할 수 있습니다.

```
      jwt: {
        signingKey: {"kty":"oct","kid":"--","alg":"HS256","k":"--"},
        verificationOptions: {
          algorithms: ["HS256"]
        }
      }

```

#### SESSION_ERROR[​](https://next-auth.js.org/v3/errors#session_error "제목으로 바로 가는 링크")

---

### Signout[​](https://next-auth.js.org/v3/errors#signout "제목으로 바로 가는 링크")

#### SIGNOUT_ERROR[​](https://next-auth.js.org/v3/errors#signout_error "제목으로 바로 가는 링크")

---

### Database[​](https://next-auth.js.org/v3/errors#database "제목으로 바로 가는 링크")

이 오류들은 기본 데이터베이스 어댑터인 TypeORM Adapter에서 기록됩니다.

모두 데이터베이스와 상호작용하는 과정의 문제를 나타냅니다.

#### ADAPTER_CONNECTION_ERROR[​](https://next-auth.js.org/v3/errors#adapter_connection_error "제목으로 바로 가는 링크")

#### CREATE_USER_ERROR[​](https://next-auth.js.org/v3/errors#create_user_error "제목으로 바로 가는 링크")

#### GET_USER_BY_ID_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_id_error "제목으로 바로 가는 링크")

#### GET_USER_BY_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_email_error "제목으로 바로 가는 링크")

#### GET_USER_BY_PROVIDER_ACCOUNT_ID_ERROR[​](https://next-auth.js.org/v3/errors#get_user_by_provider_account_id_error "제목으로 바로 가는 링크")

#### LINK_ACCOUNT_ERROR[​](https://next-auth.js.org/v3/errors#link_account_error "제목으로 바로 가는 링크")

#### CREATE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#create_session_error "제목으로 바로 가는 링크")

#### GET_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#get_session_error "제목으로 바로 가는 링크")

#### UPDATE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#update_session_error "제목으로 바로 가는 링크")

#### DELETE_SESSION_ERROR[​](https://next-auth.js.org/v3/errors#delete_session_error "제목으로 바로 가는 링크")

#### CREATE_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#create_verification_request_error "제목으로 바로 가는 링크")

#### GET_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#get_verification_request_error "제목으로 바로 가는 링크")

#### DELETE_VERIFICATION_REQUEST_ERROR[​](https://next-auth.js.org/v3/errors#delete_verification_request_error "제목으로 바로 가는 링크")

---

### Other[​](https://next-auth.js.org/v3/errors#other "제목으로 바로 가는 링크")

#### SEND_VERIFICATION_EMAIL_ERROR[​](https://next-auth.js.org/v3/errors#send_verification_email_error "제목으로 바로 가는 링크")

Email Authentication Provider가 이메일을 전송하지 못할 때 이 오류가 발생합니다.

메일 서버 구성을 확인하세요.

#### MISSING_NEXTAUTH_API_ROUTE_ERROR[​](https://next-auth.js.org/v3/errors#missing_nextauth_api_route_error "제목으로 바로 가는 링크")

`pages/api/auth` 내부에서 `[...nextauth].js` 파일을 찾을 수 없을 때 이 오류가 발생합니다.

파일이 해당 위치에 있는지, 그리고 파일명이 올바르게 작성되었는지 확인하세요.
