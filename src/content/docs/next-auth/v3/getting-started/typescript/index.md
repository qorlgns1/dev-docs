---
title: "TypeScript"
description: "NextAuth.js는 자체 타입 정의를 제공하므로 TypeScript 프로젝트에서 안전하게 사용할 수 있습니다. TypeScript를 사용하지 않더라도 VSCode 같은 IDE가 이를 인식해 더 나은 개발자 경험을 제공합니다. 코드를 입력하는 동안 특정 객체/함수의 ..."
---

Source URL: https://next-auth.js.org/v3/getting-started/typescript

# TypeScript | NextAuth.js

버전: v3

NextAuth.js는 자체 타입 정의를 제공하므로 TypeScript 프로젝트에서 안전하게 사용할 수 있습니다. TypeScript를 사용하지 않더라도 VSCode 같은 IDE가 이를 인식해 더 나은 개발자 경험을 제공합니다. 코드를 입력하는 동안 특정 객체/함수의 형태에 대한 제안을 받을 수 있고, 경우에 따라 문서, 예제, 기타 유용한 리소스로 연결되는 링크도 제공됩니다.

TypeScript가 적용된 Next.js 애플리케이션에서 `next-auth`를 사용하는 방법을 보여주는 예제 리포지토리를 확인해 보세요:
<https://github.com/nextauthjs/next-auth-typescript-example>

danger

[DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)의 `@types/next-auth` 타입은 이제 더 이상 사용이 권장되지 않으며, 유지보수도 중단되었습니다.

---

## 어댑터[​](https://next-auth.js.org/v3/getting-started/typescript#adapters "Direct link to heading")

직접 커스텀 Adapter를 작성하는 경우, 타입을 활용해 구현이 기대 사항에 맞는지 확인할 수 있습니다:

```
    import type { Adapter } from "next-auth/adapters"

    const MyAdapter: Adapter = () => {
      return {
        async getAdapter() {
          return {
            // your adapter methods here
          }
        },
      }
    }

```

순수 JavaScript로 커스텀 Adapter를 작성할 때도, 다음과 같이 **JSDoc**을 사용해 유용한 에디터 힌트와 자동 완성을 받을 수 있습니다:

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

이는 VSCode나 WebStorm처럼 TypeScript 통합이 강력한 코드 에디터에서 동작합니다. VIM이나 Atom 같은 더 가벼운 에디터에서는 동작하지 않을 수 있습니다.

## 모듈 보강[​](https://next-auth.js.org/v3/getting-started/typescript#module-augmentation "Direct link to heading")

`next-auth`에는 서브모듈 전반에서 공유되는 특정 타입/인터페이스가 있습니다. 대표적인 예가 `Session`과 `JWT`입니다. 이상적으로는 이런 타입을 한 곳에서만 정의하고, 참조되는 모든 위치에서 TS가 이를 인식해야 합니다. 다행히 Module Augmentation이 정확히 이 역할을 해줍니다. 공유 인터페이스를 한 곳에서 정의하면, `next-auth`(또는 그 서브모듈)를 사용할 때 애플리케이션 전반에서 타입 안정성을 확보할 수 있습니다.

### 메인 모듈[​](https://next-auth.js.org/v3/getting-started/typescript#main-module "Direct link to heading")

`Session`을 살펴보겠습니다:

pages/api/auth/[...nextauth].ts

```
    import NextAuth from "next-auth"

    export default NextAuth({
      callbacks: {
        session(session, token) {
          return session // The type here should match the one returned in `useSession()`
        },
      },
    })

```

pages/index.ts

```
    import { useSession } from "next-auth/client"

    export default function IndexPage() {
      // `session` should match `callbacks.session()` in `NextAuth()`
      const [session] = useSession()

      return (
        // Your component
      )
    }

```

이 타입을 확장/보강하려면 프로젝트에 `types/next-auth.d.ts` 파일을 만드세요:

types/next-auth.d.ts

```
    import NextAuth from "next-auth"

    declare module "next-auth" {
      /**
       * Returned by `useSession`, `getSession` and received as a prop on the `Provider` React Context
       */
      interface Session {
        user: {
          /** The user's postal address. */
          address: string
        }
      }
    }

```

#### 자주 보강하는 인터페이스[​](https://next-auth.js.org/v3/getting-started/typescript#popular-interfaces-to-augment "Direct link to heading")

거의 모든 항목을 보강할 수 있지만, `next-auth` 모듈에서 자주 재정의하는 인터페이스는 다음과 같습니다:

```
    /**
     * The shape of the user object returned in the OAuth providers' `profile` callback,
     * or the second parameter of the `session` callback, when using a database.
     */
    interface User {}
    /**
     * Usually contains information about the provider being used
     * and also extends `TokenSet`, which is different tokens returned by OAuth Providers.
     */
    interface Account {}
    /** The OAuth profile returned from your provider */
    interface Profile {}

```

프로젝트의 `tsconfig.json` 파일에서 `types` 폴더가 [`typeRoots`](https://www.typescriptlang.org/tsconfig/#typeRoots)에 추가되어 있는지 확인하세요.

### 서브모듈[​](https://next-auth.js.org/v3/getting-started/typescript#submodules "Direct link to heading")

`JWT` 인터페이스는 `next-auth/jwt` 서브모듈에서 찾을 수 있습니다:

types/next-auth.d.ts

```
    declare module "next-auth/jwt" {
      /** Returned by the `jwt` callback and `getToken`, when using JWT sessions */
      interface JWT {
        /** OpenID ID Token */
        idToken?: string
      }
    }

```

### 유용한 링크[​](https://next-auth.js.org/v3/getting-started/typescript#useful-links "Direct link to heading")

1. [TypeScript 문서: Module Augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation)
2. [Digital Ocean: TypeScript의 Module Augmentation](https://www.digitalocean.com/community/tutorials/typescript-module-augmentation)

## 기여하기[​](https://next-auth.js.org/v3/getting-started/typescript#contributing "Direct link to heading")

어떤 형태의 기여든 언제나 환영하며, 특히 TypeScript 관련 기여를 환영합니다. 다만 저희는 이 프로젝트를 여가 시간에 개발하는 소규모 팀이라는 점을 이해해 주세요. 최선을 다해 지원하겠지만, 문제에 대한 해결책이 있다고 생각하시면 PR을 열어 주세요!

note

TypeScript에 기여할 때 실제 JavaScript 사용자 API에 브레이킹 변경이 없다면, TypeScript 변경 사항은 마이너 릴리스에 포함해 배포할 권리를 보유합니다. 이는 더 빠른 릴리스 주기를 유지하기 위함입니다.
