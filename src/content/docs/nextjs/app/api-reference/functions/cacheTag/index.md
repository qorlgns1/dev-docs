---
title: '함수: cacheTag'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/functions/cacheTag'
---

# 함수: cacheTag | Next.js
원본 URL: https://nextjs.org/docs/app/api-reference/functions/cacheTag

# cacheTag

마지막 업데이트: 2026년 2월 20일

`cacheTag` 함수는 온디맨드 무효화를 위해 캐시된 데이터에 태그를 지정할 수 있도록 합니다. 캐시 항목에 태그를 연결하면 다른 캐시된 데이터에 영향을 주지 않고 특정 캐시 항목만 선택적으로 제거하거나 재검증할 수 있습니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#usage)

`cacheTag`를 사용하려면 `next.config.js` 파일에서 [`cacheComponents` 플래그](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)를 활성화하세요:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
    }

    export default nextConfig
```

`cacheTag` 함수는 하나 이상의 문자열 값을 받습니다.

app/data.ts

JavaScriptTypeScript
```
    import { cacheTag } from 'next/cache'

    export async function getData() {
      'use cache'
      cacheTag('my-data')
      const data = await fetch('/api/data')
      return data
    }
```

그런 다음 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) API를 사용해 필요할 때 캐시를 온디맨드로 비울 수 있습니다. 예를 들어 [route handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)나 [Server Action](https://nextjs.org/docs/app/getting-started/updating-data) 같은 다른 함수에서 활용할 수 있습니다:

app/action.ts

JavaScriptTypeScript
```
    'use server'

    import { revalidateTag } from 'next/cache'

    export default async function submit() {
      await addPost()
      revalidateTag('my-data')
    }
```

## 알아두면 좋은 점[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#good-to-know)

- **멱등 태그** : 동일한 태그를 여러 번 적용해도 추가 효과가 없습니다.
- **다중 태그** : `cacheTag`에 여러 문자열 값을 전달해 하나의 캐시 항목에 여러 태그를 지정할 수 있습니다.

```
    cacheTag('tag-one', 'tag-two')
```

- **제한 사항** : 사용자 지정 태그의 최대 길이는 256자이며 태그 항목 수는 최대 128개입니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#examples)

### 컴포넌트나 함수에 태그 지정[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#tagging-components-or-functions)

캐시된 함수나 컴포넌트 내부에서 `cacheTag`를 호출하여 캐시된 데이터에 태그를 지정하세요:

app/components/bookings.tsx

JavaScriptTypeScript
```
    import { cacheTag } from 'next/cache'

    interface BookingsProps {
      type: string
    }

    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      'use cache'
      cacheTag('bookings-data')

      async function getBookingsData() {
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        return data
      }

      return //...
    }
```

### 외부 데이터로 태그 생성[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#creating-tags-from-external-data)

비동기 함수에서 반환된 데이터를 사용해 캐시 항목에 태그를 지정할 수 있습니다.

app/components/bookings.tsx

JavaScriptTypeScript
```
    import { cacheTag } from 'next/cache'

    interface BookingsProps {
      type: string
    }

    export async function Bookings({ type = 'haircut' }: BookingsProps) {
      async function getBookingsData() {
        'use cache'
        const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
        cacheTag('bookings-data', data.id)
        return data
      }
      return //...
    }
```

### 태그된 캐시 무효화[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#invalidating-tagged-cache)

[`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용하면 필요할 때 특정 태그의 캐시를 무효화할 수 있습니다:

app/actions.ts

JavaScriptTypeScript
```
    'use server'

    import { revalidateTag } from 'next/cache'

    export async function updateBookings() {
      await updateBookingData()
      revalidateTag('bookings-data')
    }
```

## 관련

연관된 API 참고 자료를 확인하세요.

- [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Next.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.

- [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  - Next.js 애플리케이션에서 "use cache" 지시문으로 데이터를 캐싱하는 방법을 배워보세요.

- [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
  - revalidateTag 함수의 API 참고 자료입니다.

- [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
  - 캐시된 함수나 컴포넌트의 만료 시간을 설정하는 cacheLife 함수 사용법입니다.