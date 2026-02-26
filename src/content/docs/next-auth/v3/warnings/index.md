---
title: '클라이언트[\u200b](https://next-auth.js.org/v3/warnings#client "Direct link to heading")'
description: "다음은 NextAuth.js의 경고 출력 목록입니다."
---

Source URL: https://next-auth.js.org/v3/warnings

# 경고 | NextAuth.js

Version: v3

다음은 NextAuth.js의 경고 출력 목록입니다.

모든 경고는 확인이 필요한 항목을 나타내지만, 정상 동작을 방해하지는 않습니다.

---

## 클라이언트[​](https://next-auth.js.org/v3/warnings#client "Direct link to heading")

#### NEXTAUTH_URL[​](https://next-auth.js.org/v3/warnings#nextauth_url "Direct link to heading")

환경 변수 `NEXTAUTH_URL`이(가) 없습니다. `.env` 파일에 설정해 주세요.

---

## 서버[​](https://next-auth.js.org/v3/warnings#server "Direct link to heading")

이 경고들은 터미널에 표시됩니다.

#### JWT_AUTO_GENERATED_SIGNING_KEY[​](https://next-auth.js.org/v3/warnings#jwt_auto_generated_signing_key "Direct link to heading")

이 경고를 해결하려면 다음 중 하나를 선택할 수 있습니다:

**Option 1** : `jwt` 옵션에 미리 생성된 Private Key(선택적으로 Public Key도 함께)를 전달합니다.

/pages/api/auth/[...nextauth].js

```
    jwt: {
      signingKey: process.env.JWT_SIGNING_PRIVATE_KEY,

      // You can also specify a public key for verification if using public/private key (but private only is fine)
      // verificationKey: process.env.JWT_SIGNING_PUBLIC_KEY,

      // If you want to use some key format other than HS512 you can specify custom options to use
      // when verifying (note: verificationOptions should include a value for maxTokenAge as well).
      // verificationOptions = {
      //   maxTokenAge: `${maxAge}s`, // e.g. `${30 * 24 * 60 * 60}s` = 30 days
      //   algorithms: ['HS512']
      // },
    }

```

명령줄에서 [node-jose-tools](https://www.npmjs.com/package/node-jose-tools)를 사용해 키를 생성하고 환경 변수로 설정할 수 있습니다. 예: `jose newkey -s 256 -t oct -a HS512`.

**Option 2** : `jwt` 객체에 사용자 정의 encode/decode 함수를 지정합니다. 이렇게 하면 서명 / 검증 / 기타 동작을 완전히 제어할 수 있습니다.

#### JWT_AUTO_GENERATED_ENCRYPTION_KEY[​](https://next-auth.js.org/v3/warnings#jwt_auto_generated_encryption_key "Direct link to heading")

#### SIGNIN_CALLBACK_REJECT_REDIRECT[​](https://next-auth.js.org/v3/warnings#signin_callback_reject_redirect "Direct link to heading")

`signIn` 콜백에서 무언가를 반환했는데, 이 방식은 더 이상 권장되지 않습니다(deprecated).

아마 콜백에 다음과 비슷한 코드가 있었을 것입니다:

```
    return Promise.reject("/some/url")

```

또는

```
    throw "/some/url"

```

이를 해결하려면 대신 url을 반환하면 됩니다:

```
    return "/some/url"

```

#### STATE_OPTION_DEPRECATION[​](https://next-auth.js.org/v3/warnings#state_option_deprecation "Direct link to heading")

provider 옵션으로 `state: true` 또는 `state: false`를 제공했습니다. 이는 이후 릴리스에서 각각 `protection: "state"` 및 `protection: "none"`으로 대체되며 deprecated될 예정입니다. 이 경고를 해결하려면:

- `state: true`를 사용 중이라면, 해당 옵션을 제거하면 됩니다. 기본값이 이미 `protection: "state"`입니다.
- `state: false`를 사용 중이라면, `protection: "none"`으로 설정하세요.
