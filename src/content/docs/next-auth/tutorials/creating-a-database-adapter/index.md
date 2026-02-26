---
title: "어댑터 만들기"
description: "커스텀 어댑터를 사용하면 어떤 데이터베이스 백엔드든, 심지어 여러 개의 서로 다른 데이터베이스에도 연결할 수 있습니다. 커뮤니티에서 만들고 유지 관리하는 공식 어댑터는 adapters 패키지에서 찾을 수 있습니다. 프로젝트의 커스텀 어댑터를 저장소에 자유롭게 추가하거나..."
---

Source URL: https://next-auth.js.org/tutorials/creating-a-database-adapter

# 어댑터 만들기 | NextAuth.js

버전: v4

커스텀 어댑터를 사용하면 어떤 데이터베이스 백엔드든, 심지어 여러 개의 서로 다른 데이터베이스에도 연결할 수 있습니다. 커뮤니티에서 만들고 유지 관리하는 공식 어댑터는 [adapters](https://github.com/nextauthjs/next-auth/tree/main/packages) 패키지에서 찾을 수 있습니다. 프로젝트의 커스텀 어댑터를 저장소에 자유롭게 추가하거나, 특정 어댑터의 메인테이너가 될 수도 있습니다. 커스텀 어댑터는 저장소에 추가하지 않아도 프로젝트에서 계속 생성하고 사용할 수 있습니다.

## 어댑터 생성 방법[​](https://next-auth.js.org/tutorials/creating-a-database-adapter#how-to-create-an-adapter "Direct link to heading")

어댑터 생성에 대한 자세한 내용은 [이 가이드](https://authjs.dev/guides/creating-a-database-adapter)를 참고하세요.

_실용적인 예시는 아래 코드를 참고하세요._

### 예제 코드[​](https://next-auth.js.org/tutorials/creating-a-database-adapter#example-code "Direct link to heading")

```
    /** @return { import("next-auth/adapters").Adapter } */
    export default function MyAdapter(client, options = {}) {
      return {
        async createUser(user) {
          return
        },
        async getUser(id) {
          return
        },
        async getUserByEmail(email) {
          return
        },
        async getUserByAccount({ providerAccountId, provider }) {
          return
        },
        async updateUser(user) {
          return
        },
        async deleteUser(userId) {
          return
        },
        async linkAccount(account) {
          return
        },
        async unlinkAccount({ providerAccountId, provider }) {
          return
        },
        async createSession({ sessionToken, userId, expires }) {
          return
        },
        async getSessionAndUser(sessionToken) {
          return
        },
        async updateSession({ sessionToken }) {
          return
        },
        async deleteSession(sessionToken) {
          return
        },
        async createVerificationToken({ identifier, expires, token }) {
          return
        },
        async useVerificationToken({ identifier, token }) {
          return
        },
      }
    }

```

### 필수 메서드[​](https://next-auth.js.org/tutorials/creating-a-database-adapter#required-methods "Direct link to heading")

이 메서드들은 모든 로그인 흐름에서 필수입니다:

- `createUser`
- `getUser`
- `getUserByEmail`
- `getUserByAccount`
- `linkAccount`
- `createSession`
- `getSessionAndUser`
- `updateSession`
- `deleteSession`
- `updateUser`

이 메서드들은 이메일 / passwordless 로그인 지원에 필수입니다:

- `createVerificationToken`
- `useVerificationToken`

### 아직 구현되지 않은 메서드[​](https://next-auth.js.org/tutorials/creating-a-database-adapter#unimplemented-methods "Direct link to heading")

이 메서드들은 향후 릴리스에서 필수가 될 예정이지만, 아직 호출되지는 않습니다:

- `deleteUser`
- `unlinkAccount`
