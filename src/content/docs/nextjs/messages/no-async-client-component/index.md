---
title: '비동기 Client Component 금지'
description: '원본 URL: https://nextjs.org/docs/messages/no-async-client-component'
---

# 비동기 Client Component 금지 | Next.js

원본 URL: https://nextjs.org/docs/messages/no-async-client-component

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)비동기 Client Component 금지

# 비동기 Client Component 금지

> 클라이언트 컴포넌트는 async 함수가 될 수 없습니다.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-async-client-component#why-this-error-occurred)

Client Component를 async 함수로 정의하려고 할 때 오류가 발생합니다. React Client Component는 [async 함수를 지원하지 않습니다](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md#why-cant-client-components-be-async-functions). 예를 들어:
```
    'use client'

    // This will cause an error
    async function ClientComponent() {
      // ...
    }
```

## 해결 방법[](https://nextjs.org/docs/messages/no-async-client-component#possible-ways-to-fix-it)

  1. **Server Component로 전환**: 가능하다면 Client Component를 Server Component로 전환하세요. 이렇게 하면 컴포넌트 안에서 직접 `async`/`await`를 사용할 수 있습니다.
  2. **`async` 키워드 제거**: Client Component로 유지해야 한다면 `async` 키워드를 제거하고 다른 방식으로 데이터 패칭을 처리하세요.
  3. **데이터 패칭을 위한 React Hook 사용**: `useEffect` 같은 훅이나 서드파티 라이브러리를 활용해 클라이언트 측 데이터 패칭을 수행하세요.
  4. **Context Provider와 `use` API 활용**: 컨텍스트를 통해 자식 컴포넌트에 Promise를 전달한 뒤 `use` API로 이를 해소하세요.

### 권장: 서버 측 데이터 패칭[](https://nextjs.org/docs/messages/no-async-client-component#recommended-server-side-data-fetching)

데이터는 서버에서 패칭하는 것을 권장합니다. 예를 들어:

app/page.tsx
```
    export default async function Page() {
      const data = await fetch('https://api.vercel.app/blog')
      const posts = await data.json()
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
```

### Context Provider와 `use` 사용[](https://nextjs.org/docs/messages/no-async-client-component#using-use-with-context-provider)

다른 패턴으로는 React `use` API를 Context Provider와 함께 사용하는 방법이 있습니다. 이 방식은 Promise를 자식 컴포넌트로 전달하고 `use` API로 이를 해소할 수 있게 해 줍니다. 예시는 다음과 같습니다.

먼저 컨텍스트 프로바이더를 위한 별도 파일을 만듭니다:

app/context.tsx
```
    'use client'

    import { createContext, useContext } from 'react'

    export const BlogContext = createContext<Promise<any> | null>(null)

    export function BlogProvider({
      children,
      blogPromise,
    }: {
      children: React.ReactNode
      blogPromise: Promise<any>
    }) {
      return (
        <BlogContext.Provider value={blogPromise}>{children}</BlogContext.Provider>
      )
    }

    export function useBlogContext() {
      const context = useContext(BlogContext)
      if (!context) {
        throw new Error('useBlogContext must be used within a BlogProvider')
      }
      return context
    }
```

이제 Server Component에서 Promise를 만들어 클라이언트로 스트리밍합니다:

app/page.tsx
```
    import { BlogProvider } from './context'

    export default function Page() {
      const blogPromise = fetch('https://api.vercel.app/blog').then((res) =>
        res.json()
      )

      return (
        <BlogProvider blogPromise={blogPromise}>
          <BlogPosts />
        </BlogProvider>
      )
    }
```

다음은 블로그 게시물을 렌더링하는 컴포넌트입니다:

app/blog-posts.tsx
```
    'use client'

    import { use } from 'react'
    import { useBlogContext } from './context'

    export function BlogPosts() {
      const blogPromise = useBlogContext()
      const posts = use(blogPromise)

      return <div>{posts.length} blog posts</div>
    }
```

이 패턴을 사용하면 데이터를 미리 패칭해 Promise 형태로 자식 컴포넌트에 전달하고, 자식에서 `use` API로 준비된 데이터를 바로 사용할 수 있습니다.

### 클라이언트 측 데이터 패칭[](https://nextjs.org/docs/messages/no-async-client-component#client-side-data-fetching)

클라이언트에서 데이터를 가져와야 하는 상황이라면 `useEffect` 안에서 `fetch`를 호출할 수 있고(권장하지 않음), 혹은 [SWR](https://swr.vercel.app/)이나 [React Query](https://tanstack.com/query/latest) 같은 커뮤니티의 인기 있는 React 라이브러리를 활용할 수 있습니다.

app/page.tsx
```
    'use client'

    import { useState, useEffect } from 'react'

    export function Posts() {
      const [posts, setPosts] = useState(null)

      useEffect(() => {
        async function fetchPosts() {
          const res = await fetch('https://api.vercel.app/blog')
          const data = await res.json()
          setPosts(data)
        }
        fetchPosts()
      }, [])

      if (!posts) return <div>Loading...</div>

      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
```

보내기