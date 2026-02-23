---
title: 'Functions: revalidateTag'
description: '는 특정 캐시 태그에 대해 캐시된 데이터를 온디맨드로 무효화할 수 있게 해줍니다.'
---

# Functions: revalidateTag | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/revalidateTag

# revalidateTag

최종 업데이트 2026년 2월 20일

`revalidateTag`는 특정 캐시 태그에 대해 [캐시된 데이터](https://nextjs.org/docs/app/guides/caching)를 온디맨드로 무효화할 수 있게 해줍니다.

이 함수는 블로그 게시물, 제품 카탈로그, 문서처럼 업데이트에 약간의 지연이 허용되는 콘텐츠에 이상적입니다. 사용자는 새 데이터가 백그라운드에서 로드되는 동안 오래된 콘텐츠를 계속 받습니다.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#usage)

`revalidateTag`는 서버 함수와 라우트 핸들러에서 호출할 수 있습니다.

`revalidateTag`는 클라이언트 컴포넌트나 Proxy에서는 호출할 수 없으며, 서버 환경에서만 동작합니다.

### Revalidation Behavior[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#revalidation-behavior)

재검증 동작은 두 번째 인자를 제공하는지 여부에 따라 달라집니다.

  * **`profile="max"` 사용(권장)**: 태그 항목이 오래된 것으로 표시되고, 해당 태그가 있는 리소스가 다음에 방문될 때 stale-while-revalidate 방식으로 동작합니다. 즉, 오래된 콘텐츠를 제공하면서 백그라운드에서 최신 콘텐츠를 가져옵니다.
  * **사용자 정의 캐시 수명 프로필 사용**: 애플리케이션에 정의된 어떤 캐시 수명 프로필도 지정할 수 있어, 구체적인 캐싱 요구 사항에 맞는 맞춤 재검증 동작을 구현할 수 있습니다.
  * **두 번째 인자 미사용(사용 중단 예정)**: 태그 항목이 즉시 만료되며, 해당 리소스에 대한 다음 요청은 차단되는 재검증/캐시 미스가 됩니다. 이 동작은 사용 중단 예정이므로 `profile="max"`를 사용하거나 [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)로 마이그레이션해야 합니다.

> **유용한 정보**: `profile="max"`를 사용할 때 `revalidateTag`는 태그가 지정된 데이터를 오래된 것으로 표시하지만, 해당 태그를 사용하는 페이지가 다음에 방문될 때만 새 데이터를 가져옵니다. 즉, `revalidateTag`를 호출한다고 해서 즉시 많은 재검증이 일어나지 않고, 해당 태그를 사용하는 페이지가 다음에 방문될 때 무효화가 발생합니다.

## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#parameters)
```
    revalidateTag(tag: string, profile: string | { expire?: number }): void;
```

  * `tag`: 재검증하려는 데이터에 연결된 캐시 태그를 나타내는 문자열입니다. 256자를 초과할 수 없으며 대소문자를 구분합니다.
  * `profile`: 재검증 동작을 지정하는 문자열입니다. stale-while-revalidate 방식의 `"max"`가 권장되며, [`cacheLife`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)에 정의된 다른 기본 또는 사용자 정의 프로필도 사용할 수 있습니다. 또는 `expire` 속성이 있는 객체를 전달해 맞춤 만료 동작을 지정할 수 있습니다.

태그는 먼저 캐시된 데이터에 할당되어야 하며, 다음 두 방법 중 하나로 설정할 수 있습니다.

  * 외부 API 요청을 캐시하기 위해 `fetch`의 [`next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) 옵션 사용:

```
    fetch(url, { next: { tags: ['posts'] } })
```

  * `'use cache'` 지시문과 함께 캐시된 함수나 컴포넌트 내부에서 [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) 사용:

```
    import { cacheTag } from 'next/cache'

    async function getData() {
      'use cache'
      cacheTag('posts')
      // ...
    }
```

> **유용한 정보**: 단일 인자 형태인 `revalidateTag(tag)`는 사용 중단 예정입니다. 현재는 TypeScript 오류를 무시하면 동작하지만, 향후 버전에서 제거될 수 있으므로 두 개의 인자를 사용하는 시그니처로 업데이트하세요.

## Returns[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#returns)

`revalidateTag`는 값을 반환하지 않습니다.

## Relationship with `revalidatePath`[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#relationship-with-revalidatepath)

`revalidateTag`는 특정 태그를 사용하는 모든 페이지 전반에서 해당 데이터를 무효화하는 반면, [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)는 특정 페이지나 레이아웃 경로를 무효화합니다.

> **유용한 정보**: 두 함수는 목적이 다르며, 데이터 일관성을 완전히 확보하려면 함께 사용해야 할 수도 있습니다. 자세한 예시와 고려 사항은 [relationship with revalidateTag and updateTag](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#relationship-with-revalidatetag-and-updatetag)를 참고하세요.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#examples)

다음 예제들은 서로 다른 컨텍스트에서 `revalidateTag`를 사용하는 방법을 보여줍니다. 두 경우 모두 데이터를 오래된 상태로 표시하고 stale-while-revalidate 방식을 적용하는 `profile="max"`를 사용하며, 대부분의 사용 사례에서 권장되는 접근법입니다.

### Server Action[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#server-action)

app/actions.ts

JavaScriptTypeScript
```
    'use server'

    import { revalidateTag } from 'next/cache'

    export default async function submit() {
      await addPost()
      revalidateTag('posts', 'max')
    }
```

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#route-handler)

app/api/revalidate/route.ts

JavaScriptTypeScript
```
    import type { NextRequest } from 'next/server'
    import { revalidateTag } from 'next/cache'

    export async function GET(request: NextRequest) {
      const tag = request.nextUrl.searchParams.get('tag')

      if (tag) {
        revalidateTag(tag, 'max')
        return Response.json({ revalidated: true, now: Date.now() })
      }

      return Response.json({
        revalidated: false,
        now: Date.now(),
        message: 'Missing tag to revalidate',
      })
    }
```

> **유용한 정보**: 즉시 만료가 필요한 웹훅이나 서드파티 서비스에는 두 번째 인자로 `{ expire: 0 }`을 전달해 `revalidateTag(tag, { expire: 0 })`를 사용할 수 있습니다. 외부 시스템이 라우트 핸들러를 호출하고 데이터를 즉시 만료시켜야 할 때 필요한 패턴입니다. 그 밖의 대부분 상황에서는 즉각적인 업데이트를 위해 서버 액션에서 [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag)를 사용하는 것이 좋습니다.