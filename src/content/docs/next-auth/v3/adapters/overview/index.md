---
title: '사용자 정의 Adapter[​](https://next-auth.js.org/v3/adapters/overview#custom-adapter "Direct link to heading")'
description: "NextAuth.js의 Adapter는 사용자 계정, 세션 등의 데이터를 저장하기 위해 애플리케이션을 원하는 데이터베이스 또는 백엔드 시스템에 연결해 줍니다."
---

Source URL: https://next-auth.js.org/v3/adapters/overview

# 개요 | NextAuth.js

버전: v3

NextAuth.js의 **Adapter**는 사용자 계정, 세션 등의 데이터를 저장하기 위해 애플리케이션을 원하는 데이터베이스 또는 백엔드 시스템에 연결해 줍니다.

어댑터들은 [`nextauthjs/adapters`](https://github.com/nextauthjs/adapters) 아래의 별도 저장소에서 찾을 수 있습니다.

여기에서 다음 어댑터들을 확인할 수 있습니다:

- [`typeorm-legacy`](https://next-auth.js.org/v3/adapters/typeorm/typeorm-overview)
- [`prisma`](https://next-auth.js.org/v3/adapters/prisma)
- [`prisma-legacy`](https://next-auth.js.org/v3/adapters/prisma-legacy)
- [`fauna`](https://next-auth.js.org/v3/adapters/fauna)
- [`dynamodb`](https://next-auth.js.org/v3/adapters/dynamodb)
- [`firebase`](https://next-auth.js.org/v3/adapters/firebase)

## 사용자 정의 Adapter[​](https://next-auth.js.org/v3/adapters/overview#custom-adapter "Direct link to heading")

사용자 정의 Adapter를 만드는 방법에 대한 자세한 내용은 [데이터베이스 Adapter 만들기](https://next-auth.js.org/tutorials/creating-a-database-adapter) 튜토리얼을 참고하세요. 커뮤니티에서 유지 관리하는 사용자 정의 Adapter를 확인하거나 직접 추가하려면 [Adapter repository](https://github.com/nextauthjs/adapters)를 살펴보세요.

### 에디터 통합[​](https://next-auth.js.org/v3/adapters/overview#editor-integration "Direct link to heading")

순수 JavaScript로 사용자 정의 Adapter를 작성할 때는 다음과 같이 **JSDoc**을 사용해 유용한 에디터 힌트와 자동 완성을 얻을 수 있습니다:

```
    /** @type { import("next-auth/adapters").Adapter } */
    const MyAdapter = () => {
      return {
        async getAdapter() {
          return {
            // your adapter methods here
          }
        },
      }
    }

```

note

이는 VSCode 또는 WebStorm처럼 TypeScript 통합이 강력한 코드 에디터에서 작동합니다. VIM이나 Atom 같은 더 가벼운 에디터를 사용하는 경우에는 작동하지 않을 수 있습니다.
