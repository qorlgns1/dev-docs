---
title: '시작하기: 캐싱과 재검증'
description: '캐싱은 데이터 페칭과 기타 연산의 결과를 저장해 동일한 데이터에 대한 향후 요청을 더 빠르게 처리하도록, 동일한 작업을 반복하지 않고도 응답할 수 있게 하는 기법입니다. 재검증은 애플리케이션 전체를 다시 빌드하지 않고도 캐시 항목을 최신 상태로 업데이트할 수 있게 해 ...'
---

# 시작하기: 캐싱과 재검증 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/caching-and-revalidating

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Caching and Revalidating

Copy page

# 캐싱과 재검증

최종 업데이트 2026년 2월 20일

캐싱은 데이터 페칭과 기타 연산의 결과를 저장해 동일한 데이터에 대한 향후 요청을 더 빠르게 처리하도록, 동일한 작업을 반복하지 않고도 응답할 수 있게 하는 기법입니다. 재검증은 애플리케이션 전체를 다시 빌드하지 않고도 캐시 항목을 최신 상태로 업데이트할 수 있게 해 줍니다.

Next.js는 캐싱과 재검증을 처리하기 위한 여러 API를 제공합니다. 이 가이드는 각 API를 언제, 어떻게 사용하는지 안내합니다.

  * [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)
  * [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)
  * [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)
  * [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)
  * [`revalidatePath`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)
  * [`unstable_cache`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache) (레거시)

## `fetch`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)

기본적으로 [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch) 요청은 캐시되지 않습니다. `cache` 옵션을 `'force-cache'`로 설정하면 개별 요청을 캐시할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
```
    export default async function Page() {
      const data = await fetch('https://...', { cache: 'force-cache' })
    }
```

> **알아두면 좋아요** : `fetch` 요청은 기본적으로 캐시되지 않지만, Next.js는 `fetch` 요청이 있는 라우트를 [사전 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering)하고 HTML을 캐시합니다. 라우트를 확실히 [동적](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 유지하려면 [`connection` API](https://nextjs.org/docs/app/api-reference/functions/connection)를 사용하세요.

`fetch` 요청으로 반환된 데이터를 재검증하려면 `next.revalidate` 옵션을 사용할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
```
    export default async function Page() {
      const data = await fetch('https://...', { next: { revalidate: 3600 } })
    }
```

이 설정은 지정된 초가 지난 후 데이터를 재검증합니다.

또한 `fetch` 요청에 태그를 지정해 온디맨드 캐시 무효화를 활성화할 수 있습니다.

app/lib/data.ts

JavaScriptTypeScript
```
    export async function getUserById(id: string) {
      const data = await fetch(`https://...`, {
        next: {
          tags: ['user'],
        },
      })
    }
```

자세한 내용은 [`fetch` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/fetch)를 확인하세요.

## `cacheTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)

[`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)는 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)에서 캐시된 데이터에 태그를 지정해 온디맨드로 재검증할 수 있게 합니다. 이전에는 캐시 태깅이 `fetch` 요청으로만 제한되었고, 다른 작업을 캐시하려면 실험적 `unstable_cache` API가 필요했습니다.

Cache Components에서는 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문으로 임의의 연산을 캐시하고, `cacheTag`로 태그를 지정할 수 있습니다. 이는 데이터베이스 쿼리, 파일 시스템 작업, 기타 서버 측 작업에 모두 적용됩니다.

app/lib/data.ts

JavaScriptTypeScript
```
    import { cacheTag } from 'next/cache'

    export async function getProducts() {
      'use cache'
      cacheTag('products')

      const products = await db.query('SELECT * FROM products')
      return products
    }
```

태그를 지정하면 [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag) 또는 [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)를 사용해 제품 캐시 항목을 무효화할 수 있습니다.

> **알아두면 좋아요** : `cacheTag`는 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)와 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문과 함께 사용됩니다. 이는 `fetch`를 넘어 캐싱과 재검증 영역을 확장합니다.

자세한 내용은 [`cacheTag` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/cacheTag)를 확인하세요.

## `revalidateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)

`revalidateTag`는 태그와 이벤트를 기반으로 캐시 항목을 재검증하는 데 사용됩니다. 이 함수는 다음 두 가지 동작을 지원합니다.

  * **`profile="max"` 사용 시**: stale-while-revalidate 방식으로, 새 콘텐츠를 가져오는 동안 기존 콘텐츠를 제공합니다.
  * **두 번째 인수 없이** : 캐시를 즉시 만료시키는 레거시 동작(더 이상 권장되지 않음)

캐시된 데이터에 태그를 지정했거나 [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)에서 `next.tags`를 사용했거나 [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)를 사용했다면, [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)나 서버 액션에서 `revalidateTag`를 호출할 수 있습니다.

app/lib/actions.ts

JavaScriptTypeScript
```
    import { revalidateTag } from 'next/cache'

    export async function updateUser(id: string) {
      // Mutate data
      revalidateTag('user', 'max') // Recommended: Uses stale-while-revalidate
    }
```

동일한 태그를 여러 함수에서 재사용해 한 번에 모두 재검증할 수 있습니다.

자세한 내용은 [`revalidateTag` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 확인하세요.

## `updateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)

`updateTag`는 서버 액션 전용으로 설계되었으며, 읽기-즉시-쓰기(read-your-own-writes) 시나리오에서 캐시된 데이터를 즉시 만료시킵니다. `revalidateTag`와 달리 서버 액션 내부에서만 사용할 수 있으며 캐시 항목을 즉시 만료시킵니다.

app/lib/actions.ts

JavaScriptTypeScript
```
    import { updateTag } from 'next/cache'
    import { redirect } from 'next/navigation'

    export async function createPost(formData: FormData) {
      // Create post in database
      const post = await db.post.create({
        data: {
          title: formData.get('title'),
          content: formData.get('content'),
        },
      })

      // Immediately expire cache so the new post is visible
      updateTag('posts')
      updateTag(`post-${post.id}`)

      redirect(`/posts/${post.id}`)
    }
```

`revalidateTag`와 `updateTag`의 주요 차이점은 다음과 같습니다.

  * **`updateTag`** : 서버 액션에서만 사용, 캐시를 즉시 만료, 읽기-즉시-쓰기용
  * **`revalidateTag`** : 서버 액션과 Route Handler에서 사용, `profile="max"`로 stale-while-revalidate 지원

자세한 내용은 [`updateTag` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/updateTag)를 확인하세요.

## `revalidatePath`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)

`revalidatePath`는 특정 라우트와 그에 따른 이벤트를 재검증하는 데 사용됩니다. 이를 사용하려면 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)나 서버 액션에서 호출하세요.

app/lib/actions.ts

JavaScriptTypeScript
```
    import { revalidatePath } from 'next/cache'

    export async function updateUser(id: string) {
      // Mutate data
      revalidatePath('/profile')
```

자세한 내용은 [`revalidatePath` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)를 확인하세요.

## `unstable_cache`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache)

> **알아두면 좋아요** : `unstable_cache`는 실험적 API입니다. [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)에 참여하고 `unstable_cache`를 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문으로 대체하는 것을 권장합니다. 자세한 내용은 [Cache Components 문서](https://nextjs.org/docs/app/getting-started/cache-components)를 참고하세요.

`unstable_cache`는 데이터베이스 쿼리와 기타 비동기 함수의 결과를 캐시할 수 있게 해 줍니다. 사용하려면 `unstable_cache`로 함수를 감싸면 됩니다. 예를 들면 다음과 같습니다.

app/lib/data.ts

JavaScriptTypeScript
```
    import { db } from '@/lib/db'
    export async function getUserById(id: string) {
      return db
        .select()
        .from(users)
        .where(eq(users.id, id))
        .then((res) => res[0])
    }
```

app/page.tsx

JavaScriptTypeScript
```
    import { unstable_cache } from 'next/cache'
    import { getUserById } from '@/app/lib/data'

    export default async function Page({
      params,
    }: {
      params: Promise<{ userId: string }>
    }) {
      const { userId } = await params

      const getCachedUser = unstable_cache(
        async () => {
          return getUserById(userId)
        },
        [userId] // add the user ID to the cache key
      )
    }
```

이 함수는 캐시 재검증 방식을 정의하는 세 번째 선택적 객체를 받습니다. 다음 옵션을 지원합니다.

  * `tags`: Next.js가 캐시를 재검증할 때 사용하는 태그 배열.
  * `revalidate`: 캐시를 재검증할 초 단위 기준.

app/page.tsx

JavaScriptTypeScript
```
    const getCachedUser = unstable_cache(
      async () => {
        return getUserById(userId)
      },
      [userId],
      {
        tags: ['user'],
        revalidate: 3600,
      }
    )
```

자세한 내용은 [`unstable_cache` API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)를 확인하세요.

## API Reference

이 페이지에서 언급한 기능은 API Reference에서 더 자세히 알아볼 수 있습니다.

- [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)
  - 확장 fetch 함수에 대한 API 레퍼런스입니다.

- [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
  - Next.js 애플리케이션에서 캐시 무효화를 관리하기 위해 cacheTag 함수를 사용하는 방법을 설명합니다.

- [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
  - revalidateTag 함수에 대한 API Reference입니다.

- [updateTag](https://nextjs.org/docs/app/api-reference/functions/updateTag)
  - updateTag 함수에 대한 API Reference입니다.

- [revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
  - revalidatePath 함수에 대한 API Reference입니다.

- [unstable_cache](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)
  - unstable_cache 함수에 대한 API Reference입니다.

supported.

Send