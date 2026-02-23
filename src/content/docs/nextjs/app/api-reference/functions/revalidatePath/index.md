---
title: '함수: revalidatePath'
description: '는 특정 경로에 대해 필요할 때 캐시된 데이터를 무효화할 수 있게 해줍니다.'
---

# 함수: revalidatePath | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/revalidatePath

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)revalidatePath

Copy page

# revalidatePath

Last updated February 20, 2026

`revalidatePath`는 특정 경로에 대해 필요할 때 [캐시된 데이터](https://nextjs.org/docs/app/guides/caching)를 무효화할 수 있게 해줍니다.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#usage)

`revalidatePath`는 Server Functions와 Route Handlers에서 호출할 수 있습니다.

`revalidatePath`는 클라이언트 컴포넌트나 Proxy에서 호출할 수 없으며, 서버 환경에서만 작동합니다.

> **알아두면 좋아요** :
> 
>   * **Server Functions** : (영향받는 경로를 보고 있다면) UI를 즉시 업데이트합니다. 현재는 이전에 방문했던 모든 페이지도 다시 이동하면 새로고침되는 부작용이 있습니다. 이 동작은 임시이며 향후 특정 경로에만 적용되도록 업데이트될 예정입니다.
>   * **Route Handlers** : 경로를 재검증 대상으로 표시합니다. 재검증은 지정된 경로를 다음에 방문할 때 수행됩니다. 따라서 동적 경로 세그먼트를 포함한 `revalidatePath` 호출은 즉시 많은 재검증을 트리거하지 않습니다. 무효화는 해당 경로가 다음에 방문될 때만 일어납니다.
> 

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#parameters)
[code] 
    revalidatePath(path: string, type?: 'page' | 'layout'): void;
[/code]

  * `path`: 재검증하려는 데이터에 대응하는 라우트 패턴(예: `/product/[slug]`) 또는 특정 URL(`/product/123`). `/page`나 `/layout`을 덧붙이지 말고 대신 `type` 매개변수를 사용하세요. 1024자를 초과할 수 없으며 대소문자를 구분합니다.
  * `type`: (선택 사항) 재검증할 경로 유형을 바꾸는 `'page'` 또는 `'layout'` 문자열입니다. `path`에 `/product/[slug]`처럼 동적 세그먼트가 포함되면 필수이고, `/product/1`처럼 특정 URL이면 생략합니다.

단일 [페이지](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url)를 새로고침하려면 특정 URL을 사용하세요. 여러 [URL](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path)을 새로고침하려면 라우트 패턴과 `type`을 함께 사용하세요.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#returns)

`revalidatePath`는 값을 반환하지 않습니다.

## What can be invalidated[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#what-can-be-invalidated)

`path` 매개변수는 페이지, 레이아웃 또는 Route Handler를 가리킬 수 있습니다.

  * **Pages** : 해당 페이지만 무효화합니다.
  * **Layouts** : 해당 세그먼트의 `layout.tsx`, 그 아래 모든 중첩 레이아웃, 그리고 그 아래 모든 페이지를 무효화합니다.
  * **Route Handlers** : Route Handler에서 접근한 Data Cache 항목을 무효화합니다. 예를 들어 `revalidatePath("/api/data")`는 아래 GET 핸들러를 무효화합니다.

app/api/data/route.ts
[code]
    export async function GET() {
      const data = await fetch('https://api.vercel.app/blog', {
        cache: 'force-cache',
      })
     
      return Response.json(await data.json())
    }
[/code]

## Relationship with `revalidateTag` and `updateTag`[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#relationship-with-revalidatetag-and-updatetag)

`revalidatePath`, [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)는 서로 다른 목적을 가집니다.

  * **`revalidatePath`** : 특정 페이지 또는 레이아웃 경로를 무효화합니다.
  * **`revalidateTag`** : 특정 태그가 달린 데이터를 **stale** 상태로 표시해, 해당 태그를 사용하는 모든 페이지에 적용됩니다.
  * **`updateTag`** : 특정 태그가 달린 데이터를 만료시켜, 해당 태그를 사용하는 모든 페이지에 적용됩니다.

`revalidatePath`를 호출하면 지정된 경로만 다음 방문 시 새 데이터를 가져옵니다. 동일한 데이터 태그를 사용하는 다른 페이지는 해당 태그가 재검증될 때까지 캐시된 데이터를 계속 제공합니다.
[code] 
    // Page A: /blog
    const posts = await fetch('https://api.vercel.app/blog', {
      next: { tags: ['posts'] },
    })
     
    // Page B: /dashboard
    const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
      next: { tags: ['posts'] },
    })
[/code]

`revalidatePath('/blog')` 호출 이후:

  * **Page A (/blog)** : 최신 데이터를 표시합니다(페이지가 다시 렌더링됨).
  * **Page B (/dashboard)** : 여전히 오래된 데이터를 표시합니다(`posts` 캐시 태그가 무효화되지 않음).

[`revalidateTag`와 `updateTag`의 차이점](https://nextjs.org/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag)을 알아보세요.

### Building revalidation utilities[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#building-revalidation-utilities)

`revalidatePath`와 `updateTag`는 애플리케이션 전반의 데이터 일관성을 보장하기 위해 유틸리티 함수에서 함께 사용되는 보완적인 프리미티브입니다.
[code] 
    'use server'
     
    import { revalidatePath, updateTag } from 'next/cache'
     
    export async function updatePost() {
      await updatePostInDatabase()
     
      revalidatePath('/blog') // Refresh the blog page
      updateTag('posts') // Refresh all pages using 'posts' tag
    }
[/code]

이 패턴은 특정 페이지와 동일한 데이터를 사용하는 다른 페이지 모두가 일관된 상태를 유지하도록 합니다.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#examples)

### Revalidating a specific URL[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/post-1')
[/code]

이 코드는 특정 URL 하나를 다음 페이지 방문 시 재검증하도록 무효화합니다.

### Revalidating a Page path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/[slug]', 'page')
    // or with route groups
    revalidatePath('/(main)/blog/[slug]', 'page')
[/code]

이는 제공된 `page` 파일과 일치하는 모든 URL을 다음 페이지 방문 시 재검증하도록 무효화합니다. 특정 페이지 아래의 페이지는 무효화되지 않습니다. 예를 들어 `/blog/[slug]`는 `/blog/[slug]/[author]`를 무효화하지 않습니다.

### Revalidating a Layout path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-layout-path)
[code] 
    import { revalidatePath } from 'next/cache'
    revalidatePath('/blog/[slug]', 'layout')
    // or with route groups
    revalidatePath('/(main)/post/[slug]', 'layout')
[/code]

이는 제공된 `layout` 파일과 일치하는 모든 URL을 다음 페이지 방문 시 재검증하도록 무효화합니다. 동일한 레이아웃을 공유하는 하위 페이지들도 다음 방문 시 무효화되고 재검증됩니다. 예를 들어 위 사례에서는 `/blog/[slug]/[another]`도 다음 방문 시 무효화됩니다.

### Revalidating all data[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-all-data)
[code] 
    import { revalidatePath } from 'next/cache'
     
    revalidatePath('/', 'layout')
[/code]

이는 클라이언트 측 라우터 캐시를 비우고, 다음 페이지 방문 시 재검증을 위해 데이터 캐시를 무효화합니다.

### Server Function[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#server-function)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidatePath } from 'next/cache'
     
    export default async function submit() {
      await submitForm()
      revalidatePath('/')
    }
[/code]

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#route-handler)

app/api/revalidate/route.ts

JavaScriptTypeScript
[code]
    import { revalidatePath } from 'next/cache'
    import type { NextRequest } from 'next/server'
     
    export async function GET(request: NextRequest) {
      const path = request.nextUrl.searchParams.get('path')
     
      if (path) {
        revalidatePath(path)
        return Response.json({ revalidated: true, now: Date.now() })
      }
     
      return Response.json({
        revalidated: false,
        now: Date.now(),
        message: 'Missing path to revalidate',
      })
    }
[/code]

Was this helpful?

supported.

Send
