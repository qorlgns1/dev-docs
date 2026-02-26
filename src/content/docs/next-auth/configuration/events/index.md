---
title: '이벤트[​](https://next-auth.js.org/configuration/events#events "Direct link to heading")'
description: "원본 URL: https://next-auth.js.org/configuration/events"
---

원본 URL: https://next-auth.js.org/configuration/events

# 이벤트 | NextAuth.js

버전: v4

이벤트는 응답을 반환하지 않는 비동기 함수이며, 감사 로그 / 리포팅 또는 기타 부수 효과(side-effects)를 처리하는 데 유용합니다.

아래 이벤트 각각에 대해, 디버깅이나 감사 로그 목적의 핸들러를 지정할 수 있습니다.

note

인증 API의 실행은 이벤트 핸들러에 대한 `await` 때문에 블로킹됩니다. 이벤트 핸들러가 부담이 큰 작업을 시작한다면, 해당 작업으로 인해 자체 promise가 블로킹되지 않도록 해야 합니다.

## 이벤트[​](https://next-auth.js.org/configuration/events#events "Direct link to heading")

### signIn[​](https://next-auth.js.org/configuration/events#signin "Direct link to heading")

성공적인 로그인 시 전송됩니다.

메시지는 객체이며 다음을 포함합니다:

- `user` (어댑터에서 오거나, `credentials` 타입 provider인 경우 provider에서 옴)
- `account` (어댑터 또는 provider에서 옴)
- `profile` (provider에서 오며, `credentials` provider에서는 `undefined`이므로 대신 `user` 사용)
- `isNewUser` (어댑터에 이 계정용 사용자가 이미 있었는지 여부)

### signOut[​](https://next-auth.js.org/configuration/events#signout "Direct link to heading")

사용자가 로그아웃할 때 전송됩니다.

메시지 객체에는 JWT 또는 데이터베이스에 영속 저장된 세션 사용 여부에 따라 다음 중 하나가 포함됩니다:

- `token`: 이 세션의 JWT 토큰.
- `session`: 종료되는 어댑터의 세션 객체

### createUser[​](https://next-auth.js.org/configuration/events#createuser "Direct link to heading")

어댑터가 새 사용자를 생성하라는 지시를 받을 때 전송됩니다.

메시지 객체에는 사용자가 포함됩니다.

### updateUser[​](https://next-auth.js.org/configuration/events#updateuser "Direct link to heading")

어댑터가 기존 사용자를 업데이트하라는 지시를 받을 때 전송됩니다. 현재는 사용자가 이메일 주소를 인증할 때만 전송됩니다.

메시지 객체에는 사용자가 포함됩니다.

### linkAccount[​](https://next-auth.js.org/configuration/events#linkaccount "Direct link to heading")

특정 provider의 계정이 사용자 데이터베이스의 사용자와 연결될 때 전송됩니다. 예를 들어, 사용자가 Twitter로 가입하거나 기존 사용자가 Google 계정을 연결할 때입니다.

메시지 객체는 다음을 포함합니다:

- `user`: 어댑터의 사용자 객체.
- `account`: provider에서 반환된 객체.
- `profile`: OAuth provider의 `profile` 콜백에서 반환된 객체.

### session[​](https://next-auth.js.org/configuration/events#session "Direct link to heading")

현재 세션에 대한 요청이 끝날 때 전송됩니다.

메시지 객체에는 JWT 또는 데이터베이스에 영속 저장된 세션 사용 여부에 따라 다음 중 하나가 포함됩니다:

- `token`: 이 세션의 JWT 토큰.
- `session`: 어댑터의 세션 객체.
