---
title: '시작하기: 서버 및 클라이언트 컴포넌트'
description: '기본적으로 레이아웃과 페이지는 서버 컴포넌트이며, 이를 통해 서버에서 데이터를 가져오고 UI 일부를 렌더링한 뒤 결과를 캐시하거나 클라이언트로 스트리밍할 수 있습니다. 상호작용이나 브라우저 API가 필요할 때는 클라이언트 컴포넌트를 사용해 기능을 추가할 수 있습니다.'
---

# 시작하기: 서버 및 클라이언트 컴포넌트 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/server-and-client-components

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)서버 및 클라이언트 컴포넌트

# 서버 및 클라이언트 컴포넌트

최종 업데이트 2026년 2월 20일

기본적으로 레이아웃과 페이지는 [서버 컴포넌트](https://react.dev/reference/rsc/server-components)이며, 이를 통해 서버에서 데이터를 가져오고 UI 일부를 렌더링한 뒤 결과를 캐시하거나 클라이언트로 스트리밍할 수 있습니다. 상호작용이나 브라우저 API가 필요할 때는 [클라이언트 컴포넌트](https://react.dev/reference/rsc/use-client)를 사용해 기능을 추가할 수 있습니다.

이 페이지는 Next.js에서 서버 및 클라이언트 컴포넌트가 어떻게 동작하는지, 언제 사용해야 하는지, 그리고 애플리케이션에서 둘을 조합하는 방법에 대한 예제를 설명합니다.

## 서버 및 클라이언트 컴포넌트를 언제 사용해야 할까요?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#when-to-use-server-and-client-components)

클라이언트와 서버 환경은 서로 다른 기능을 제공합니다. 서버 및 클라이언트 컴포넌트를 사용하면 사용 사례에 따라 각 환경에서 로직을 실행할 수 있습니다.

다음이 필요할 때는 **클라이언트 컴포넌트**를 사용하세요:

  * [상태](https://react.dev/learn/managing-state)와 [이벤트 핸들러](https://react.dev/learn/responding-to-events). 예: `onClick`, `onChange`.
  * [라이프사이클 로직](https://react.dev/learn/lifecycle-of-reactive-effects). 예: `useEffect`.
  * 브라우저 전용 API. 예: `localStorage`, `window`, `Navigator.geolocation` 등.
  * [커스텀 훅](https://react.dev/learn/reusing-logic-with-custom-hooks).

다음이 필요할 때는 **서버 컴포넌트**를 사용하세요:

  * 데이터 소스와 가까운 데이터베이스나 API에서 데이터를 가져오기.
  * API 키, 토큰 등 비밀 값을 클라이언트에 노출하지 않고 사용하기.
  * 브라우저로 전송되는 JavaScript 양을 줄이기.
  * [First Contentful Paint(FCP)](https://web.dev/fcp/)를 개선하고, 콘텐츠를 클라이언트로 점진적으로 스트리밍하기.

예를 들어 `<Page>` 컴포넌트는 게시물에 대한 데이터를 가져오는 서버 컴포넌트이며, 이 데이터를 클라이언트 측 상호작용을 처리하는 `<LikeButton>`에 props로 전달합니다.

app/[id]/page.tsx

JavaScript/TypeScript
```
    import LikeButton from '@/app/ui/like-button'
    import { getPost } from '@/lib/data'

    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const post = await getPost(id)

      return (
        <div>
          <main>
            <h1>{post.title}</h1>
            {/* ... */}
            <LikeButton likes={post.likes} />
          </main>
        </div>
      )
    }
```

app/ui/like-button.tsx

JavaScript/TypeScript
```
    'use client'

    import { useState } from 'react'

    export default function LikeButton({ likes }: { likes: number }) {
      // ...
    }
```

## Next.js에서 서버 및 클라이언트 컴포넌트는 어떻게 동작하나요?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)

### 서버에서[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-server)

서버에서는 Next.js가 React의 API를 사용해 렌더링을 오케스트레이션합니다. 렌더링 작업은 개별 라우트 세그먼트([레이아웃과 페이지](https://nextjs.org/docs/app/getting-started/layouts-and-pages))별로 청크로 나뉩니다.

  * **서버 컴포넌트**는 React Server Component Payload(RSC Payload)라는 특수 데이터 형식으로 렌더링됩니다.
  * **클라이언트 컴포넌트**와 RSC Payload는 함께 HTML을 [사전 렌더링](https://nextjs.org/docs/app/guides/caching#rendering-strategies)하는 데 사용됩니다.

> **React Server Component Payload(RSC)란 무엇인가요?**
>
> RSC Payload는 렌더링된 React 서버 컴포넌트 트리를 압축한 이진 표현입니다. 이는 클라이언트의 React가 브라우저 DOM을 업데이트하는 데 사용됩니다. RSC Payload에는 다음이 포함됩니다.
>
>   * 서버 컴포넌트의 렌더링 결과
>   * 클라이언트 컴포넌트를 렌더링할 위치와 해당 JavaScript 파일에 대한 참조
>   * 서버 컴포넌트에서 클라이언트 컴포넌트로 전달되는 모든 props
>

### 클라이언트에서(첫 로드)[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-client-first-load)

이후 클라이언트에서는 다음 순서로 처리합니다.

  1. **HTML**은 사용자에게 빠른 비상호작용 라우트 미리보기를 즉시 보여 줍니다.
  2. **RSC Payload**는 클라이언트와 서버 컴포넌트 트리를 동기화하는 데 사용됩니다.
  3. **JavaScript**는 클라이언트 컴포넌트를 하이드레이트하고 애플리케이션을 인터랙티브하게 만듭니다.

> **하이드레이션이란 무엇인가요?**
>
> 하이드레이션은 React가 DOM에 [이벤트 핸들러](https://react.dev/learn/responding-to-events)를 연결하여 정적 HTML을 인터랙티브하게 만드는 과정입니다.

### 이후 내비게이션[](https://nextjs.org/docs/app/getting-started/server-and-client-components#subsequent-navigations)

이후 내비게이션에서는 다음과 같이 진행됩니다.

  * **RSC Payload**를 사전 가져와 캐시하여 즉시 내비게이션할 수 있습니다.
  * **클라이언트 컴포넌트**는 서버 렌더링된 HTML 없이 전적으로 클라이언트에서 렌더링됩니다.

## 예제[](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples)

### 클라이언트 컴포넌트 사용하기[](https://nextjs.org/docs/app/getting-started/server-and-client-components#using-client-components)

파일 상단, import 위에 [`"use client"`](https://react.dev/reference/react/use-client) 지시문을 추가하면 클라이언트 컴포넌트를 만들 수 있습니다.

app/ui/counter.tsx

JavaScript/TypeScript
```
    'use client'

    import { useState } from 'react'

    export default function Counter() {
      const [count, setCount] = useState(0)

      return (
        <div>
          <p>{count} likes</p>
          <button onClick={() => setCount(count + 1)}>Click me</button>
        </div>
      )
    }
```

`"use client"`는 서버와 클라이언트 모듈 그래프(트리) 사이의 **경계**를 선언하는 데 사용됩니다.

파일에 `"use client"`가 표시되면 **해당 파일의 모든 import와 자식 컴포넌트가 클라이언트 번들에 포함**됩니다. 즉, 클라이언트용으로 의도된 모든 컴포넌트에 지시문을 반복해서 추가할 필요가 없습니다.

### JS 번들 크기 줄이기[](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size)

클라이언트 JavaScript 번들 크기를 줄이려면 `'use client'`를 UI의 큰 부분이 아닌 특정 인터랙티브 컴포넌트에만 추가하세요.

예를 들어 `<Layout>` 컴포넌트에는 로고와 내비게이션 링크 같은 정적인 요소가 대부분이지만, 인터랙티브한 검색 바가 포함되어 있습니다. `<Search />`는 인터랙티브하므로 클라이언트 컴포넌트여야 하지만, 나머지 레이아웃은 서버 컴포넌트로 유지할 수 있습니다.

app/layout.tsx

JavaScript/TypeScript
```
    // Client Component
    import Search from './search'
    // Server Component
    import Logo from './logo'

    // Layout is a Server Component by default
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <>
          <nav>
            <Logo />
            <Search />
          </nav>
          <main>{children}</main>
        </>
      )
    }
```

app/ui/search.tsx

JavaScript/TypeScript
```
    'use client'

    export default function Search() {
      // ...
    }
```

### 서버에서 클라이언트 컴포넌트로 데이터 전달하기[](https://nextjs.org/docs/app/getting-started/server-and-client-components#passing-data-from-server-to-client-components)

서버 컴포넌트에서 클라이언트 컴포넌트로 props를 사용해 데이터를 전달할 수 있습니다.

app/[id]/page.tsx

JavaScript/TypeScript
```
    import LikeButton from '@/app/ui/like-button'
    import { getPost } from '@/lib/data'

    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const post = await getPost(id)

      return <LikeButton likes={post.likes} />
    }
```

app/ui/like-button.tsx

JavaScript/TypeScript
```
    'use client'

    export default function LikeButton({ likes }: { likes: number }) {
      // ...
    }
```

또는 [`use` API](https://react.dev/reference/react/use)를 사용해 서버 컴포넌트에서 클라이언트 컴포넌트로 데이터를 스트리밍할 수도 있습니다. [예제](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api)를 참고하세요.

> **알아두면 좋아요**: 클라이언트 컴포넌트에 전달되는 props는 React가 [직렬화할 수 있어야](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values) 합니다.

### 서버와 클라이언트 컴포넌트 교차 배치하기[](https://nextjs.org/docs/app/getting-started/server-and-client-components#interleaving-server-and-client-components)

서버 컴포넌트를 클라이언트 컴포넌트의 props로 전달할 수 있습니다. 이렇게 하면 클라이언트 컴포넌트 내에서 서버 렌더링된 UI를 시각적으로 중첩할 수 있습니다.

일반적인 패턴은 `<ClientComponent>` 안에 _slot_을 만들기 위해 `children`을 사용하는 것입니다. 예를 들어 가시성을 토글하기 위해 클라이언트 상태를 사용하는 `<Modal>` 컴포넌트 안에, 서버에서 데이터를 가져오는 `<Cart>` 컴포넌트를 배치할 수 있습니다.

app/ui/modal.tsx

JavaScript/TypeScript
```
    'use client'

    export default function Modal({ children }: { children: React.ReactNode }) {
      return <div>{children}</div>
    }
```

그런 다음 상위 서버 컴포넌트(예: `<Page>`)에서 `<Cart>`를 `<Modal>`의 자식으로 전달할 수 있습니다.

app/page.tsx

JavaScript/TypeScript
```
    import Modal from './ui/modal'
    import Cart from './ui/cart'

    export default function Page() {
      return (
        <Modal>
          <Cart />
        </Modal>
      )
    }
```

이 패턴에서는 props로 전달된 컴포넌트를 포함해 모든 서버 컴포넌트가 사전에 서버에서 렌더링됩니다. 결과 RSC Payload에는 컴포넌트 트리 내에서 클라이언트 컴포넌트가 렌더링되어야 할 위치에 대한 참조가 포함됩니다.

### 컨텍스트 프로바이더[](https://nextjs.org/docs/app/getting-started/server-and-client-components#context-providers)

[React 컨텍스트](https://react.dev/learn/passing-data-deeply-with-context)는 현재 테마 같은 전역 상태를 공유하는 데 자주 사용됩니다. 그러나 서버 컴포넌트에서는 React 컨텍스트를 지원하지 않습니다.

컨텍스트를 사용하려면 `children`을 받는 클라이언트 컴포넌트를 생성하세요.

app/theme-provider.tsx

JavaScript/TypeScript
```
    'use client'

    import { createContext } from 'react'

    export const ThemeContext = createContext({})

    export default function ThemeProvider({
      children,
    }: {
      children: React.ReactNode
    }) {
      return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
    }
```

그런 다음 서버 컴포넌트(예: `layout`)에 이를 import합니다.

app/layout.tsx

JavaScript/TypeScript
```
    import ThemeProvider from './theme-provider'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html>
          <body>
            <ThemeProvider>{children}</ThemeProvider>
          </body>
        </html>
      )
    }
```

이제 서버 컴포넌트가 프로바이더를 직접 렌더링할 수 있으며, 앱 전반의 다른 클라이언트 컴포넌트에서도 이 컨텍스트를 사용할 수 있습니다.

> **알아두면 좋아요**: 프로바이더는 트리에서 가능한 한 깊은 곳에 렌더링해야 합니다. `ThemeProvider`가 전체 `<html>` 문서를 감싸지 않고 `{children}`만 감싸는 이유입니다. 이렇게 하면 Next.js가 서버 컴포넌트의 정적 부분을 최적화하기 쉽습니다.

### 컨텍스트와 React.cache로 데이터 공유하기[](https://nextjs.org/docs/app/getting-started/server-and-client-components#sharing-data-with-context-and-reactcache)

[`React.cache`](https://react.dev/reference/react/cache)를 컨텍스트 프로바이더와 결합하면 서버와 클라이언트 컴포넌트 모두에서 가져온 데이터를 공유할 수 있습니다.

데이터를 가져오는 캐시된 함수를 생성합니다:

app/lib/user.ts

JavaScriptTypeScript
```
    import { cache } from 'react'

    export const getUser = cache(async () => {
      const res = await fetch('https://api.example.com/user')
      return res.json()
    })
```

프로미스를 저장하는 컨텍스트 프로바이더를 생성합니다:

app/user-provider.tsx

JavaScriptTypeScript
```
    'use client'

    import { createContext } from 'react'

    type User = {
      id: string
      name: string
    }

    export const UserContext = createContext<Promise<User> | null>(null)

    export default function UserProvider({
      children,
      userPromise,
    }: {
      children: React.ReactNode
      userPromise: Promise<User>
    }) {
      return <UserContext value={userPromise}>{children}</UserContext>
    }
```

레이아웃에서 프로미스를 await 하지 않은 채 프로바이더로 전달합니다:

app/layout.tsx

JavaScriptTypeScript
```
    import UserProvider from './user-provider'
    import { getUser } from './lib/user'

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const userPromise = getUser() // Don't await

      return (
        <html>
          <body>
            <UserProvider userPromise={userPromise}>{children}</UserProvider>
          </body>
        </html>
      )
    }
```

클라이언트 컴포넌트는 컨텍스트에서 프로미스를 해소하기 위해 [`use()`](https://react.dev/reference/react/use)를 사용하고, 폴백 UI를 위해 `<Suspense>`로 감쌉니다:

app/ui/profile.tsx

JavaScriptTypeScript
```
    'use client'

    import { use, useContext } from 'react'
    import { UserContext } from '../user-provider'

    export function Profile() {
      const userPromise = useContext(UserContext)
      if (!userPromise) {
        throw new Error('useContext must be used within a UserProvider')
      }
      const user = use(userPromise)
      return <p>Welcome, {user.name}</p>
    }
```

app/page.tsx

JavaScriptTypeScript
```
    import { Suspense } from 'react'
    import { Profile } from './ui/profile'

    export default function Page() {
      return (
        <Suspense fallback={<div>Loading profile...</div>}>
          <Profile />
        </Suspense>
      )
    }
```

서버 컴포넌트도 `getUser()`를 직접 호출할 수 있습니다:

app/dashboard/page.tsx

JavaScriptTypeScript
```
    import { getUser } from '../lib/user'

    export default async function DashboardPage() {
      const user = await getUser() // Cached - same request, no duplicate fetch
      return <h1>Dashboard for {user.name}</h1>
    }
```

`getUser`가 `React.cache`로 감싸져 있으므로, 동일한 요청 내에서 여러 번 호출해도 서버 컴포넌트에서 직접 호출하거나 클라이언트 컴포넌트에서 컨텍스트를 통해 해소하든 같은 메모이즈된 결과를 반환합니다.

> **알아두면 좋은 점**: `React.cache`는 현재 요청 범위에만 적용됩니다. 각 요청은 자체 메모이제이션 범위를 가지며 요청 간에는 공유되지 않습니다.

### Third-party components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#third-party-components)

클라이언트 전용 기능에 의존하는 서드파티 컴포넌트를 사용할 때는, 예상대로 작동하도록 클라이언트 컴포넌트로 감쌀 수 있습니다.

예를 들어 `<Carousel />`은 `acme-carousel` 패키지에서 가져올 수 있습니다. 이 컴포넌트는 `useState`를 사용하지만 아직 `"use client"` 지시문이 없습니다.

`<Carousel />`을 클라이언트 컴포넌트에서 사용하면 예상대로 작동합니다:

app/gallery.tsx

JavaScriptTypeScript
```
    'use client'

    import { useState } from 'react'
    import { Carousel } from 'acme-carousel'

    export default function Gallery() {
      const [isOpen, setIsOpen] = useState(false)

      return (
        <div>
          <button onClick={() => setIsOpen(true)}>View pictures</button>
          {/* Works, since Carousel is used within a Client Component */}
          {isOpen && <Carousel />}
        </div>
      )
    }
```

그러나 서버 컴포넌트에서 직접 사용하려 하면 오류가 발생합니다. Next.js가 `<Carousel />`이 클라이언트 전용 기능을 사용한다는 사실을 알 수 없기 때문입니다.

이를 해결하려면 클라이언트 전용 기능에 의존하는 서드파티 컴포넌트를 자체 클라이언트 컴포넌트로 감싸면 됩니다:

app/carousel.tsx

JavaScriptTypeScript
```
    'use client'

    import { Carousel } from 'acme-carousel'

    export default Carousel
```

이제 서버 컴포넌트에서 `<Carousel />`을 직접 사용할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
```
    import Carousel from './carousel'

    export default function Page() {
      return (
        <div>
          <p>View pictures</p>
          {/*  Works, since Carousel is a Client Component */}
          <Carousel />
        </div>
      )
    }
```

> **라이브러리 작성자를 위한 조언**
>
> 컴포넌트 라이브러리를 구축 중이라면, 클라이언트 전용 기능에 의존하는 엔트리 포인트에 `"use client"` 지시문을 추가하세요. 그러면 사용자가 래퍼를 만들 필요 없이 서버 컴포넌트에 컴포넌트를 가져올 수 있습니다.
>
> 일부 번들러는 `"use client"` 지시문을 제거할 수 있다는 점에 유의하세요. `"use client"` 지시문을 유지하도록 esbuild를 구성하는 예시는 [React Wrap Balancer](https://github.com/shuding/react-wrap-balancer/blob/main/tsup.config.ts#L10-L13)와 [Vercel Analytics](https://github.com/vercel/analytics/blob/main/packages/web/tsup.config.js#L26-L30) 저장소에서 확인할 수 있습니다.

### Preventing environment poisoning[](https://nextjs.org/docs/app/getting-started/server-and-client-components#preventing-environment-poisoning)

JavaScript 모듈은 서버와 클라이언트 컴포넌트 모듈 모두에서 공유될 수 있습니다. 이는 서버 전용 코드를 클라이언트에 실수로 가져올 위험이 있음을 의미합니다. 예를 들어 다음 함수를 살펴보세요:

lib/data.ts

JavaScriptTypeScript
```
    export async function getData() {
      const res = await fetch('https://external-service.com/data', {
        headers: {
          authorization: process.env.API_KEY,
        },
      })

      return res.json()
    }
```

이 함수에는 클라이언트에 노출되어서는 안 되는 `API_KEY`가 포함되어 있습니다.

Next.js에서는 `NEXT_PUBLIC_` 접두사가 붙은 환경 변수만 클라이언트 번들에 포함됩니다. 접두사가 없으면 Next.js가 빈 문자열로 바꿉니다.

따라서 `getData()`를 클라이언트에서 가져와 실행할 수 있다 하더라도 기대대로 동작하지 않습니다.

클라이언트 컴포넌트에서의 실수로 인한 사용을 방지하려면 [`server-only` 패키지](https://www.npmjs.com/package/server-only)를 사용할 수 있습니다.

그런 다음 서버 전용 코드가 포함된 파일에 해당 패키지를 가져옵니다:

lib/data.js
```
    import 'server-only'

    export async function getData() {
      const res = await fetch('https://external-service.com/data', {
        headers: {
          authorization: process.env.API_KEY,
        },
      })

      return res.json()
    }
```

이제 클라이언트 컴포넌트에서 모듈을 가져오려 하면 빌드 시 오류가 발생합니다.

[`client-only` 패키지](https://www.npmjs.com/package/client-only)는 `window` 객체에 접근하는 코드처럼 클라이언트 전용 로직이 포함된 모듈을 표시하는 데 사용할 수 있습니다.

Next.js에서는 `server-only` 또는 `client-only` 설치가 **선택 사항**입니다. 다만 린팅 규칙이 불필요한 의존성을 경고한다면 문제를 피하기 위해 설치할 수 있습니다.

pnpmnpmyarnbun

Terminal
```
    pnpm add server-only
```

Next.js는 모듈이 잘못된 환경에서 사용될 때 더 명확한 오류 메시지를 제공하기 위해 내부적으로 `server-only` 및 `client-only` 가져오기를 처리합니다. NPM에서 제공되는 해당 패키지의 실제 내용은 Next.js에서 사용되지 않습니다.

또한 Next.js는 [`noUncheckedSideEffectImports`](https://www.typescriptlang.org/tsconfig/#noUncheckedSideEffectImports)가 활성화된 TypeScript 구성에서 `server-only` 및 `client-only`를 위한 자체 타입 선언을 제공합니다.

## Next Steps

이 페이지에 언급된 API에 대해 더 알아보세요.

- [use client](https://nextjs.org/docs/app/api-reference/directives/use-client)
  - 클라이언트에서 컴포넌트를 렌더링하기 위해 use client 지시문을 사용하는 방법을 알아보세요.

supported.

Send