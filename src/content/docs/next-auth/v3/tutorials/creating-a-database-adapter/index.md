---
title: "데이터베이스 어댑터 만들기"
description: "커스텀 어댑터를 사용하면 어떤 데이터베이스 백엔드든, 심지어 서로 다른 여러 데이터베이스에도 연결할 수 있습니다. 커뮤니티에서 만들고 유지 관리하는 커스텀 어댑터는 adapters repository에서 확인할 수 있습니다. 여러분의 프로젝트에서 만든 커스텀 어댑터를 ..."
---

Source URL: https://next-auth.js.org/v3/tutorials/creating-a-database-adapter

# 데이터베이스 어댑터 만들기 | NextAuth.js

버전: v3

커스텀 어댑터를 사용하면 어떤 데이터베이스 백엔드든, 심지어 서로 다른 여러 데이터베이스에도 연결할 수 있습니다. 커뮤니티에서 만들고 유지 관리하는 커스텀 어댑터는 [adapters repository](https://github.com/nextauthjs/adapters)에서 확인할 수 있습니다. 여러분의 프로젝트에서 만든 커스텀 어댑터를 저장소에 추가하거나, 특정 어댑터의 메인테이너가 되어도 좋습니다. 저장소에 추가하지 않아도 프로젝트에서 커스텀 어댑터를 만들고 사용할 수 있습니다.

커스텀 어댑터를 만드는 일은 상당한 작업이 될 수 있으며, 내장 어댑터를 참고해 리버스 엔지니어링을 하면서 시행착오를 거쳐야 할 수 있습니다.

## 어댑터를 만드는 방법[​](https://next-auth.js.org/v3/tutorials/creating-a-database-adapter#how-to-create-an-adapter "헤딩으로 직접 연결")

구현 관점에서 NextAuth.js의 어댑터는 async `getAdapter()` 메서드를 반환하는 함수입니다. 그리고 이 `getAdapter()`는 사용자 생성, 사용자와 OAuth 계정 연결, 세션 읽기/쓰기 처리 같은 작업을 다루는 함수 목록을 담은 Promise를 반환합니다.

이 방식은 데이터베이스 연결 로직을 `getAdapter()` 메서드 안에 두기 위해 사용됩니다. 작업이 필요해지기 직전에 이 함수를 호출하면, 데이터베이스 연결 상태를 확인하고 필요할 때 데이터베이스 연결/재연결을 처리할 수 있습니다.

_실제 예시는 아래 코드를 참고하세요._

### 필수 메서드[​](https://next-auth.js.org/v3/tutorials/creating-a-database-adapter#required-methods "헤딩으로 직접 연결")

다음 메서드는 모든 로그인 플로우에 필요합니다:

- createUser
- getUser
- getUserByEmail
- getUserByProviderAccountId
- linkAccount
- createSession
- getSession
- updateSession
- deleteSession
- updateUser

다음 메서드는 이메일 / 비밀번호 없는 로그인(passwordless sign in)을 지원하기 위해 필요합니다:

- createVerificationRequest
- getVerificationRequest
- deleteVerificationRequest

### 아직 구현되지 않은 메서드[​](https://next-auth.js.org/v3/tutorials/creating-a-database-adapter#unimplemented-methods "헤딩으로 직접 연결")

다음 메서드는 향후 릴리스에서 필요해지지만, 아직 호출되지는 않습니다:

- deleteUser
- unlinkAccount

### 예제 코드[​](https://next-auth.js.org/v3/tutorials/creating-a-database-adapter#example-code "헤딩으로 직접 연결")

```
    export default function YourAdapter (config, options = {}) {
      return {
        async getAdapter (appOptions) {
          async createUser (profile) {
            return null
          },
          async getUser (id) {
            return null
          },
          async getUserByEmail (email) {
            return null
          },
          async getUserByProviderAccountId (
            providerId,
            providerAccountId
          ) {
            return null
          },
          async updateUser (user) {
            return null
          },
          async deleteUser (userId) {
            return null
          },
          async linkAccount (
            userId,
            providerId,
            providerType,
            providerAccountId,
            refreshToken,
            accessToken,
            accessTokenExpires
          ) {
            return null
          },
          async unlinkAccount (
            userId,
            providerId,
            providerAccountId
          ) {
            return null
          },
          async createSession (user) {
            return null
          },
          async getSession (sessionToken) {
            return null
          },
          async updateSession (
            session,
            force
          ) {
            return null
          },
          async deleteSession (sessionToken) {
            return null
          },
          async createVerificationRequest (
            identifier,
            url,
            token,
            secret,
            provider
          ) {
            return null
          },
          async getVerificationRequest (
            identifier,
            token,
            secret,
            provider
          ) {
            return null
          },
          async deleteVerificationRequest (
            identifier,
            token,
            secret,
            provider
          ) {
            return null
          }
        }
      }
    }

```
