---
title: "TypeScript"
description: "NextAuth.js는 TypeScript 프로젝트에서 안전하게 사용할 수 있도록 자체 타입 정의를 제공합니다. TypeScript를 사용하지 않더라도 VSCode 같은 IDE가 이를 인식해 더 나은 개발자 경험을 제공합니다. 타이핑하는 동안 특정 객체/함수의 형태에 ..."
---

원문 URL: https://next-auth.js.org/getting-started/typescript

# TypeScript | NextAuth.js

버전: v4

NextAuth.js는 TypeScript 프로젝트에서 안전하게 사용할 수 있도록 자체 타입 정의를 제공합니다. TypeScript를 사용하지 않더라도 VSCode 같은 IDE가 이를 인식해 더 나은 개발자 경험을 제공합니다. 타이핑하는 동안 특정 객체/함수의 형태에 대한 제안을 받고, 때로는 문서, 예제, 기타 유용한 리소스로 연결되는 링크도 확인할 수 있습니다.

TypeScript가 적용된 Next.js 애플리케이션에서 `next-auth`를 사용하는 방법을 보여주는 예제 저장소를 확인해 보세요:
<https://github.com/nextauthjs/next-auth-example>

---

## Adapters[​](https://next-auth.js.org/getting-started/typescript#adapters "Direct link to heading")

직접 커스텀 Adapter를 작성하고 있다면, 타입을 활용해 구현이 기대 사항에 맞는지 확인할 수 있습니다:

```
    import type { Adapter } from "next-auth/adapters"

    function MyAdapter(): Adapter {
      return {
        // your adapter methods here
      }
    }

```

일반 JavaScript로 직접 커스텀 Adapter를 작성할 때는, 다음과 같이 **JSDoc**을 사용해 유용한 에디터 힌트와 자동 완성을 받을 수 있습니다:

```
    /** @return { import("next-auth/adapters").Adapter } */
    function MyAdapter() {
      return {
        // your adapter methods here
      }
    }

```

note

이 기능은 VSCode나 WebStorm처럼 TypeScript 통합이 강력한 코드 에디터에서 동작합니다. VIM이나 Atom 같은 더 경량 에디터에서는 동작하지 않을 수 있습니다.

## Module Augmentation[​](https://next-auth.js.org/getting-started/typescript#module-augmentation "Direct link to heading")

`next-auth`에는 하위 모듈 간에 공유되는 특정 타입/인터페이스가 있습니다. 대표적인 예가 `Session`과 `JWT`입니다. 이상적으로는 이 타입들을 한 곳에서만 생성하고, 참조되는 모든 위치에서 TS가 이를 인식해야 합니다. 다행히 Module Augmentation이 바로 이를 가능하게 해줍니다. 공유 인터페이스를 한 곳에 정의하고, `next-auth`(또는 그 하위 모듈)를 사용할 때 애플리케이션 전반에서 타입 안정성을 확보할 수 있습니다.

### Main module[​](https://next-auth.js.org/getting-started/typescript#main-module "Direct link to heading")

`Session`을 살펴보겠습니다:

pages/api/auth/[...nextauth].ts

```
    import NextAuth from "next-auth"

    export default NextAuth({
      callbacks: {
        session({ session, token, user }) {
          return session // The return type will match the one returned in `useSession()`
        },
      },
    })

```

pages/index.ts

```
    import { useSession } from "next-auth/react"

    export default function IndexPage() {
      // `session` will match the returned value of `callbacks.session()` from `NextAuth()`
      const { data: session } = useSession()

      return (
        // Your component
      )
    }

```

이 타입을 확장/보강하려면, 프로젝트에 `types/next-auth.d.ts` 파일을 생성하세요:

types/next-auth.d.ts

```
    import NextAuth from "next-auth"

    declare module "next-auth" {
      /**
       * Returned by `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
       */
      interface Session {
        user: {
          /** The user's postal address. */
          address: string
        }
      }
    }

```

#### Extend default interface properties[​](https://next-auth.js.org/getting-started/typescript#extend-default-interface-properties "Direct link to heading")

기본적으로 TypeScript는 새 인터페이스 속성을 병합하고 기존 속성을 덮어씁니다. 이 경우 위에서 정의한 새 속성으로 기본 세션 사용자 속성이 덮어써집니다.

기본 세션 사용자 속성을 유지하려면, 새로 선언한 인터페이스에 해당 속성들을 다시 추가해야 합니다:

types/next-auth.d.ts

```
    import NextAuth, { DefaultSession } from "next-auth"

    declare module "next-auth" {
      /**
       * Returned by `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
       */
      interface Session {
        user: {
          /** The user's postal address. */
          address: string
        } & DefaultSession["user"]
      }
    }

```

#### Popular interfaces to augment[​](https://next-auth.js.org/getting-started/typescript#popular-interfaces-to-augment "Direct link to heading")

거의 모든 것을 보강할 수 있지만, `next-auth` 모듈에서 자주 재정의하게 되는 인터페이스는 다음과 같습니다:

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

### Submodules[​](https://next-auth.js.org/getting-started/typescript#submodules "Direct link to heading")

`JWT` 인터페이스는 `next-auth/jwt` 하위 모듈에서 찾을 수 있습니다:

types/next-auth.d.ts

```
    import { JWT } from "next-auth/jwt"

    declare module "next-auth/jwt" {
      /** Returned by the `jwt` callback and `getToken`, when using JWT sessions */
      interface JWT {
        /** OpenID ID Token */
        idToken?: string
      }
    }

```

### Useful links[​](https://next-auth.js.org/getting-started/typescript#useful-links "Direct link to heading")

1. [TypeScript documentation: Module Augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation)
2. [Digital Ocean: Module Augmentation in TypeScript](https://www.digitalocean.com/community/tutorials/typescript-module-augmentation)

## Contributing[​](https://next-auth.js.org/getting-started/typescript#contributing "Direct link to heading")

어떤 형태의 기여든 항상 환영하며, 특히 TypeScript 관련 기여를 환영합니다. 다만 저희는 이 프로젝트를 여가 시간에 작업하는 소규모 팀이라는 점을 참고해 주세요. 최대한 지원하려고 노력하겠지만, 문제에 대한 해결책이 있다고 생각하신다면 PR을 열어 주세요!

note

TypeScript에 기여할 때 실제 JavaScript 사용자 API가 호환성을 깨는 방식으로 바뀌지 않는다면, 저희는 TypeScript 변경 사항을 minor 릴리스에 포함해 배포할 권리를 보유합니다. 이를 통해 더 빠른 릴리스 사이클을 유지할 수 있습니다.
