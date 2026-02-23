---
title: 'Functions: updateTag'
description: '는 Server Actions 내에서 특정 캐시 태그의 캐시된 데이터를 필요할 때 업데이트할 수 있게 해 줍니다.'
---

# Functions: updateTag | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/updateTag

# updateTag

마지막 업데이트 2026년 2월 20일

`updateTag`는 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) 내에서 특정 캐시 태그의 [캐시된 데이터](https://nextjs.org/docs/app/guides/caching)를 필요할 때 업데이트할 수 있게 해 줍니다.

이 함수는 사용자가 변경 사항(예: 게시물 생성)을 만든 직후에 UI가 오래된 데이터 대신 즉시 해당 변경을 보여 주어야 하는 **read-your-own-writes** 시나리오에 맞춰 설계되었습니다.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/updateTag#usage)

`updateTag`는 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) 내부에서만 호출할 수 있습니다. Route Handler, Client Component, 기타 다른 컨텍스트에서는 사용할 수 없습니다.

Route Handler나 다른 컨텍스트에서 캐시 태그를 무효화해야 한다면 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용하세요.

> **알아두면 좋아요**: `updateTag`는 지정된 태그의 캐시된 데이터를 즉시 만료시킵니다. 다음 요청은 캐시에 있는 오래된 콘텐츠를 제공하는 대신 새 데이터를 가져올 때까지 대기하므로, 사용자는 즉시 자신의 변경 사항을 확인할 수 있습니다.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/updateTag#parameters)
[code]
    updateTag(tag: string): void;
[/code]

  * `tag`: 업데이트하려는 데이터와 연결된 캐시 태그를 나타내는 문자열입니다. 256자를 초과할 수 없으며, 대소문자를 구분합니다.

태그는 먼저 캐시된 데이터에 할당되어야 합니다. 방법은 두 가지입니다.

  * 외부 API 요청을 캐시하기 위해 `fetch`와 함께 [`next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) 옵션을 사용하는 방법:

[code]
    fetch(url, { next: { tags: ['posts'] } })
[/code]

  * `'use cache'` 지시어를 사용하는 캐시된 함수나 컴포넌트 내부에서 [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag)를 호출하는 방법:

[code]
    import { cacheTag } from 'next/cache'

    async function getData() {
      'use cache'
      cacheTag('posts')
      // ...
    }
[/code]

## Returns[](https://nextjs.org/docs/app/api-reference/functions/updateTag#returns)

`updateTag`는 값을 반환하지 않습니다.

## Differences from revalidateTag[](https://nextjs.org/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag)

`updateTag`와 `revalidateTag` 모두 캐시된 데이터를 무효화하지만, 목적이 다릅니다.

  * **`updateTag`** :

    * Server Action에서만 사용 가능
    * 다음 요청은 새 데이터를 기다리며, 오래된 콘텐츠를 제공하지 않음
    * read-your-own-writes 시나리오에 최적화
  * **`revalidateTag`** :

    * Server Action과 Route Handler 모두에서 사용 가능
    * `profile="max"`(권장)을 사용하면 새 데이터를 백그라운드에서 가져오는 동안 캐시 데이터를 제공함(stale-while-revalidate)
    * 사용자 지정 프로필을 사용하면 고급 용도로 임의의 캐시 수명 프로필을 구성 가능
    * 프로필 없이 사용하면 `updateTag`와 동일한 레거시 동작

## Examples[](https://nextjs.org/docs/app/api-reference/functions/updateTag#examples)

### Server Action with Read-Your-Own-Writes[](https://nextjs.org/docs/app/api-reference/functions/updateTag#server-action-with-read-your-own-writes)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { updateTag } from 'next/cache'
    import { redirect } from 'next/navigation'

    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')

      // Create the post in your database
      const post = await db.post.create({
        data: { title, content },
      })

      // Invalidate cache tags so the new post is immediately visible
      // 'posts' tag: affects any page that displays a list of posts
      updateTag('posts')
      // 'post-{id}' tag: affects the individual post detail page
      updateTag(`post-${post.id}`)

      // Redirect to the new post - user will see fresh data, not cached
      redirect(`/posts/${post.id}`)
    }
[/code]

### Error when used outside Server Actions[](https://nextjs.org/docs/app/api-reference/functions/updateTag#error-when-used-outside-server-actions)

app/api/posts/route.ts

JavaScriptTypeScript
[code]
    import { updateTag } from 'next/cache'

    export async function POST() {
      // This will throw an error
      updateTag('posts')
      // Error: updateTag can only be called from within a Server Action

      // Use revalidateTag instead in Route Handlers
      revalidateTag('posts', 'max')
    }
[/code]

## When to use updateTag[](https://nextjs.org/docs/app/api-reference/functions/updateTag#when-to-use-updatetag)

다음과 같은 경우 `updateTag`를 사용하세요.

  * Server Action 내에 있을 때
  * read-your-own-writes를 위해 즉시 캐시 무효화가 필요할 때
  * 다음 요청에서 업데이트된 데이터를 확실히 보여야 할 때

다음과 같은 경우에는 `revalidateTag`를 사용하세요.

  * Route Handler 또는 다른 non-action 컨텍스트에 있을 때
  * stale-while-revalidate 동작이 필요할 때
  * 캐시 무효화를 위한 웹후크나 API 엔드포인트를 구축할 때

## Related[](https://nextjs.org/docs/app/api-reference/functions/updateTag#related)

  * [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) \- Route Handler에서 태그 무효화
  * [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) \- 특정 경로 무효화

보내기
