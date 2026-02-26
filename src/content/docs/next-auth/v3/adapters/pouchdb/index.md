---
title: "PouchDB"
description: "원본 URL: https://next-auth.js.org/v3/adapters/pouchdb"
---

원본 URL: https://next-auth.js.org/v3/adapters/pouchdb

버전: v3

# PouchDB

이것은 [`next-auth`](https://next-auth.js.org)를 위한 PouchDB Adapter입니다. 이 패키지는 기본 `next-auth` 패키지와 함께 사용할 때만 사용할 수 있습니다. 독립형 패키지가 아닙니다.

아키텍처에 따라 PouchDB의 http adapter를 사용해 CouchDB 프로토콜을 준수하는 모든 데이터베이스(CouchDB, Cloudant, ...)에 연결하거나, 그 외 PouchDB와 호환되는 adapter(leveldb, in-memory, ...)를 사용할 수 있습니다.

## 시작하기[​](https://next-auth.js.org/v3/adapters/pouchdb#getting-started "Direct link to heading")

> **사전 요구 사항** : Adapter가 내부적으로 인덱스를 생성하고 관리할 때 사용하므로, PouchDB 인스턴스는 반드시 `pouchdb-find` plugin을 제공해야 합니다

1. `next-auth` 및 `@next-auth/pouchdb-adapter@canary`를 설치합니다

```
    npm install next-auth @next-auth/pouchdb-adapter@canary

```

2. `pages/api/auth/[...nextauth].js`의 next-auth 설정 객체에 이 adapter를 추가합니다

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import { PouchDBAdapter } from "@next-auth/pouchdb-adapter"
    import PouchDB from "pouchdb"

    // Setup your PouchDB instance and database
    PouchDB.plugin(require("pouchdb-adapter-leveldb")) // Any other adapter
      .plugin(require("pouchdb-find")) // Don't forget the `pouchdb-find` plugin

    const pouchdb = new PouchDB("auth_db", { adapter: "leveldb" })

    // For more information on each option (and a full list of options) go to
    // https://next-auth.js.org/configuration/options
    export default NextAuth({
      // https://providers.authjs.dev
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
        }),
      ],
      adapter: PouchDBAdapter(pouchdb),
      // ...
    })

```

## 고급[​](https://next-auth.js.org/v3/adapters/pouchdb#advanced "Direct link to heading")

### 메모리 우선 캐싱 전략[​](https://next-auth.js.org/v3/adapters/pouchdb#memory-first-caching-strategy "Direct link to heading")

인증 레이어의 성능을 높여야 한다면, PouchDB의 강력한 sync 기능과 다양한 adapter를 사용해 메모리 우선 캐싱 전략을 구성할 수 있습니다.

in-memory PouchDB를 기본 인증 데이터베이스로 사용하고, 이를 다른 영속형 PouchDB와 동기화하세요. 시작 시 영속형 PouchDB에서 in-memory PouchDB로 단방향 1회 복제를 수행한 뒤, 양방향의 연속적이고 재시도 가능한 sync를 수행할 수 있습니다.

동시성, 함수 시작 시간 증가 등 여러 이유로 인해 serverless 환경에서는 성능이 크게 향상되지 않을 가능성이 높습니다.

자세한 내용은 <https://pouchdb.com/api.html#sync>를 참고하세요.
