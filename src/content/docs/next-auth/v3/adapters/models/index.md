---
title: 'User[\u200b](https://next-auth.js.org/v3/adapters/models#user "Direct link to heading")'
description: "NextAuth.js의 모델은 ANSI SQL을 기준으로 설계되었지만 다형성을 가지며, 사용 중인 데이터베이스에 맞게 변환됩니다. 특정 데이터 타입(예: datetime, text 필드 등)에는 약간의 차이가 있지만, 가능한 한 동작 일관성을 유지하면서 기능적으로는 동..."
---

Source URL: https://next-auth.js.org/v3/adapters/models

# 모델 | NextAuth.js

버전: v3

NextAuth.js의 모델은 ANSI SQL을 기준으로 설계되었지만 다형성을 가지며, 사용 중인 데이터베이스에 맞게 변환됩니다. 특정 데이터 타입(예: datetime, text 필드 등)에는 약간의 차이가 있지만, 가능한 한 동작 일관성을 유지하면서 기능적으로는 동일합니다.

내장 모델의 모든 테이블/컬렉션 이름은 복수형이며, SQL 데이터베이스에서는 모든 테이블 이름과 컬럼 이름에 `snake_case`를 사용하고 Document 데이터베이스에서는 `camelCase`를 사용합니다.

참고

지원되는 데이터베이스 외의 환경에서 NextAuth.js를 사용하려면, [내장 모델을 확장](https://next-auth.js.org/v3/tutorials/typeorm-custom-models)하거나 [직접 데이터베이스 어댑터를 생성](https://next-auth.js.org/tutorials/creating-a-database-adapter)할 수도 있습니다.

---

## User[​](https://next-auth.js.org/v3/adapters/models#user "Direct link to heading")

Table: `users`

**설명:**

User 모델은 사용자 이름, 이메일 주소와 같은 정보를 위한 모델입니다.

이메일 주소는 선택 사항이지만, User에 지정된 경우 반드시 고유해야 합니다.

참고

사용자가 OAuth로 처음 로그인하면, OAuth 제공자가 이메일을 반환하는 경우 OAuth 프로필의 이메일 주소가 자동으로 채워집니다.

이렇게 하면 사용자에게 연락할 수 있고, 향후 OAuth 제공자로 로그인할 수 없게 되더라도(이메일 로그인이 구성된 경우) 사용자가 계정 접근 권한을 유지하고 이메일로 로그인할 수 있습니다.

## Account[​](https://next-auth.js.org/v3/adapters/models#account "Direct link to heading")

Table: `accounts`

**설명:**

Account 모델은 User와 연결된 OAuth 계정 정보를 위한 모델입니다.

하나의 User는 여러 Account를 가질 수 있고, 각 Account는 하나의 User만 가질 수 있습니다.

## Session[​](https://next-auth.js.org/v3/adapters/models#session "Direct link to heading")

Table: `sessions`

**설명:**

Session 모델은 데이터베이스 세션에 사용됩니다. JSON Web Tokens가 활성화된 경우에는 사용되지 않습니다.

하나의 User는 여러 Session을 가질 수 있고, 각 Session은 하나의 User만 가질 수 있습니다.

## Verification Request[​](https://next-auth.js.org/v3/adapters/models#verification-request "Direct link to heading")

Table: `verification_requests`

**설명:**

Verification Request 모델은 비밀번호 없는 이메일 로그인용 토큰을 저장하는 데 사용됩니다.

하나의 User는 여러 개의 열린 Verification Request를 가질 수 있습니다(예: 서로 다른 디바이스에서 로그인).

향후 다른 검증 목적(예: 2FA / short codes)으로도 확장할 수 있도록 설계되었습니다.
