---
title: '이벤트[\u200b](https://next-auth.js.org/v3/configuration/events#events "Direct link to heading")'
description: "이벤트는 응답을 반환하지 않는 비동기 함수이며, 감사 로그/리포팅에 유용합니다."
---

Source URL: https://next-auth.js.org/v3/configuration/events

# 이벤트 | NextAuth.js

버전: v3

이벤트는 응답을 반환하지 않는 비동기 함수이며, 감사 로그/리포팅에 유용합니다.

아래 이벤트 각각에 대해 핸들러를 지정해 디버깅 또는 감사 로그에 활용할 수 있습니다.

참고

인증 API 실행은 이벤트 핸들러에 대한 `await`로 인해 블로킹됩니다. 이벤트 핸들러가 부담이 큰 작업을 시작한다면, 해당 작업이 자체 promise를 블로킹하지 않도록 해야 합니다.

## 이벤트[​](https://next-auth.js.org/v3/configuration/events#events "Direct link to heading")

### signIn[​](https://next-auth.js.org/v3/configuration/events#signin "Direct link to heading")

로그인 성공 시 전송됩니다.

메시지는 객체이며 다음을 포함합니다:

- `user` (어댑터에서 오거나, `credentials` 유형 provider인 경우 provider에서 옴)
- `account` (어댑터 또는 provider에서 옴)
- `isNewUser` (어댑터에 이 account에 해당하는 사용자가 이미 있었는지 여부)

### signOut[​](https://next-auth.js.org/v3/configuration/events#signout "Direct link to heading")

사용자가 로그아웃할 때 전송됩니다.

메시지 객체는 JWT를 사용하는 경우 해당 JWT이며, 그렇지 않으면 종료되는 session의 어댑터 session 객체입니다.

### createUser[​](https://next-auth.js.org/v3/configuration/events#createuser "Direct link to heading")

어댑터가 새 사용자를 생성하라는 지시를 받을 때 전송됩니다.

메시지 객체는 user입니다.

### updateUser[​](https://next-auth.js.org/v3/configuration/events#updateuser "Direct link to heading")

어댑터가 기존 사용자를 업데이트하라는 지시를 받을 때 전송됩니다. 현재는 사용자가 이메일 주소를 인증할 때만 전송됩니다.

메시지 객체는 user입니다.

### linkAccount[​](https://next-auth.js.org/v3/configuration/events#linkaccount "Direct link to heading")

특정 provider의 account가 사용자 데이터베이스의 사용자와 연결될 때 전송됩니다. 예를 들어, 사용자가 Twitter로 가입하거나 기존 사용자가 자신의 Google account를 연결할 때입니다.

메시지는 객체이며 다음을 포함합니다:

- `user`: 어댑터의 user 객체
- `providerAccount`: provider에서 반환된 객체

### session[​](https://next-auth.js.org/v3/configuration/events#session "Direct link to heading")

현재 session에 대한 요청이 끝날 때 전송됩니다.

메시지는 객체이며 다음을 포함합니다:

- `session`: 어댑터의 session 객체
- `jwt`: JWT를 사용하는 경우, 이 session의 token

### error[​](https://next-auth.js.org/v3/configuration/events#error "Direct link to heading")

오류가 발생할 때 전송됩니다

메시지는 오류를 설명하는 데 관련된 어떤 객체든 될 수 있습니다.
