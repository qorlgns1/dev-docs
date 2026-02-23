---
title: 'Functions: cacheLife'
description: '함수는 함수나 컴포넌트의 캐시 수명을 설정하는 데 사용됩니다.  지시문과 함께, 해당 함수나 컴포넌트 범위 내에서 사용해야 합니다.'
---

# Functions: cacheLife | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/functions/cacheLife

Copy page

# cacheLife

마지막 업데이트: 2026년 2월 20일

`cacheLife` 함수는 함수나 컴포넌트의 캐시 수명을 설정하는 데 사용됩니다. [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 지시문과 함께, 해당 함수나 컴포넌트 범위 내에서 사용해야 합니다.

## Usage[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#usage)

### Basic setup[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#basic-setup)

`cacheLife`를 사용하려면 먼저 `next.config.js` 파일에서 [`cacheComponents` 플래그](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)를 활성화하세요:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
    }

    export default nextConfig
```

`cacheLife`는 `use cache` 지시문이 필요하며, 파일 수준 또는 비동기 함수·컴포넌트의 최상단에 배치해야 합니다.

> **알아두면 좋아요** :
>
>   * `use cache` 지시문이 파일 수준에 있더라도, `cacheLife`는 해당 함수의 출력이 캐시되는 함수 내부에 배치해야 합니다.
>   * 함수 실행당 `cacheLife`는 한 번만 호출되어야 합니다. 서로 다른 제어 흐름 분기에서 호출할 수 있지만, 실행 시점에는 하나만 실행되도록 보장하세요. [조건부 캐시 수명](https://nextjs.org/docs/app/api-reference/functions/cacheLife#conditional-cache-lifetimes) 예시를 참고하세요.
>

### Using preset profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-preset-profiles)

Next.js는 일반적인 캐싱 요구를 충족하는 프리셋 캐시 프로필을 제공합니다. 각 프로필은 다음 세 가지 요소를 균형 있게 조절합니다:

  * 사용자가 서버 확인 없이 캐시된 콘텐츠를 보는 기간(클라이언트 측)
  * 서버에서 최신 콘텐츠를 생성하는 빈도
  * 오래된 콘텐츠가 완전히 만료되는 시점

콘텐츠 변경 빈도에 따라 프로필을 선택하세요:

  * **`seconds`** - 실시간 데이터(주가, 실시간 점수)
  * **`minutes`** - 자주 업데이트되는 콘텐츠(소셜 피드, 뉴스)
  * **`hours`** - 하루에도 여러 번 바뀌는 콘텐츠(제품 재고, 날씨)
  * **`days`** - 일일 업데이트 콘텐츠(블로그 글, 기사)
  * **`weeks`** - 주 단위 업데이트 콘텐츠(팟캐스트, 뉴스레터)
  * **`max`** - 거의 변하지 않는 콘텐츠(법률 페이지, 보관 자료)

`cacheLife`를 import하고 프로필 이름을 전달하세요:

app/blog/page.tsx
```
    'use cache'
    import { cacheLife } from 'next/cache'

    export default async function BlogPage() {
      cacheLife('days') // Blog content updated daily

      const posts = await getBlogPosts()
      return <div>{/* render posts */}</div>
    }
```

프로필 이름은 Next.js에 함수 전체 출력의 캐시 방법을 알려줍니다. `cacheLife`를 호출하지 않으면 `default` 프로필이 사용됩니다. 타이밍 세부 정보는 [preset cache profiles](https://nextjs.org/docs/app/api-reference/functions/cacheLife#preset-cache-profiles)를 참고하세요.

## Reference[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#reference)

### Cache profile properties[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#cache-profile-properties)

캐시 프로필은 세 가지 타이밍 속성으로 캐싱 동작을 제어합니다:

  * **[`stale`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#stale)** : 클라이언트가 서버 확인 없이 캐시된 데이터를 사용할 수 있는 기간
  * **[`revalidate`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#revalidate)** : 이 시간이 지난 후 도착한 다음 요청이 백그라운드 새로 고침을 트리거하는 시점
  * **[`expire`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#expire)** : 일정 기간 요청이 없을 때, 다음 요청이 새 콘텐츠를 기다려야 하는 시점

#### `stale`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#stale)

**클라이언트 측:** 클라이언트가 서버 확인 없이 캐시된 데이터를 사용할 수 있는 기간입니다.

이 시간 동안 클라이언트 라우터는 네트워크 요청 없이 즉시 캐시된 콘텐츠를 표시합니다. 기간이 지나면 다음 탐색 또는 요청 시 서버에 확인해야 합니다. 이 방식은 즉각적인 페이지 로드를 제공하지만 데이터가 오래될 수 있습니다.

  * 설정하지 않으면 `default` 프로필의 `stale` 값(5분, [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) 참조)을 따릅니다.

```
    cacheLife({ stale: 300 }) // 5 minutes
```

#### `revalidate`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#revalidate)

서버가 백그라운드에서 캐시된 콘텐츠를 다시 생성하는 빈도입니다.

  * 이 기간 이후 요청이 도착하면 서버는:
    1. (가능하면) 캐시된 버전을 즉시 제공
    2. 백그라운드에서 콘텐츠 재생성
    3. 새 콘텐츠로 캐시 업데이트
  * [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/app/guides/incremental-static-regeneration)과 유사합니다.
  * 설정하지 않으면 `default` 프로필의 `revalidate` 값(15분)을 따릅니다.

```
    cacheLife({ revalidate: 900 }) // 15 minutes
```

#### `expire`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#expire)

서버가 반드시 캐시된 콘텐츠를 재생성해야 하는 최대 시간입니다.

  * 이 기간 동안 트래픽이 없으면 다음 요청에서 서버가 동기적으로 콘텐츠를 재생성합니다.
  * `revalidate`와 `expire`를 모두 설정할 때는 `expire`가 `revalidate`보다 길어야 합니다. Next.js는 이를 검증하고 잘못된 구성 시 오류를 발생시킵니다.
  * 설정하지 않으면 `default` 프로필의 `expire` 값(만료 없음)을 따릅니다.

```
    cacheLife({ expire: 3600 }) // 1 hour
```

### Preset cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#preset-cache-profiles)

프로필을 지정하지 않으면 Next.js는 `default` 프로필을 사용합니다. 캐싱 동작을 명확히 하기 위해 프로필을 명시적으로 설정하는 것이 좋습니다.

**Profile**| **Use Case**| `stale`| `revalidate`| `expire`
---|---|---|---|---
`default`| Standard content| 5 minutes| 15 minutes| never
`seconds`| Real-time data| 30 seconds| 1 second| 1 minute
`minutes`| Frequently updated content| 5 minutes| 1 minute| 1 hour
`hours`| Content updated multiple times per day| 5 minutes| 1 hour| 1 day
`days`| Content updated daily| 5 minutes| 1 day| 1 week
`weeks`| Content updated weekly| 5 minutes| 1 week| 30 days
`max`| Stable content that rarely changes| 5 minutes| 30 days| 1 year

### Custom cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#custom-cache-profiles)

`next.config.ts` 파일에 재사용 가능한 캐시 프로필을 정의하세요:

next.config.ts
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
      cacheLife: {
        biweekly: {
          stale: 60 * 60 * 24 * 14, // 14 days
          revalidate: 60 * 60 * 24, // 1 day
          expire: 60 * 60 * 24 * 14, // 14 days
        },
      },
    }

    export default nextConfig
```

위 예시는 14일 동안 캐시하고, 매일 업데이트를 확인하며, 14일 후 캐시를 만료합니다. 그런 다음 애플리케이션 전체에서 이 프로필 이름을 참조할 수 있습니다:

> **알아두면 좋아요** : 사용자 정의 프로필에서 생략한 속성은 `default` 프로필에서 상속됩니다. 이는 `cacheLife()`에 인라인 프로필 객체를 전달할 때도 적용됩니다.

app/page.tsx
```
    'use cache'
    import { cacheLife } from 'next/cache'

    export default async function Page() {
      cacheLife('biweekly')
      return <div>Page</div>
    }
```

### Overriding the default cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#overriding-the-default-cache-profiles)

기본 캐시 프로필은 캐시 가능한 출력이 얼마나 최신 또는 오래되었는지를 판단하는 데 유용하지만, 애플리케이션의 캐싱 전략에 더 맞는 이름을 선호할 수도 있습니다.

기본 프로필과 동일한 이름으로 새 구성을 만들어 기본 이름의 캐시 프로필을 재정의할 수 있습니다.

아래 예시는 기본 `"days"` 캐시 프로필을 재정의하는 방법을 보여줍니다:

next.config.ts
```
    const nextConfig = {
      cacheComponents: true,
      cacheLife: {
        // Override the 'days' profile
        days: {
          stale: 3600, // 1 hour
          revalidate: 900, // 15 minutes
          expire: 86400, // 1 day
        },
      },
    }

    export default nextConfig
```

### Inline cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-cache-profiles)

일회성 사례의 경우 프로필 객체를 직접 `cacheLife`에 전달하세요:

app/page.tsx
```
    'use cache'
    import { cacheLife } from 'next/cache'

    export default async function Page() {
      cacheLife({
        stale: 3600,
        revalidate: 900,
        expire: 86400,
      })

      return <div>Page</div>
    }
```

인라인 프로필은 해당 함수나 컴포넌트에만 적용됩니다. 재사용 가능한 구성이 필요하면 `next.config.ts`에 사용자 정의 프로필을 정의하세요.

빈 객체를 사용하는 `cacheLife({})`는 `default` 프로필 값을 적용합니다.

### Client router cache behavior[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#client-router-cache-behavior)

`stale` 속성은 `Cache-Control` 헤더가 아니라 클라이언트 측 라우터 캐시를 제어합니다:

  * 서버는 `x-nextjs-stale-time` 응답 헤더로 stale 시간을 전송합니다.
  * 클라이언트 라우터는 이 값으로 재검증 시점을 결정합니다.
  * 프리패치된 링크가 계속 사용 가능하도록 **최소 30초가 강제**됩니다.

이 30초 최소값은 사용자가 링크를 클릭하기 전에 프리패치된 데이터가 만료되는 것을 방지하며, 시간 기반 만료에만 적용됩니다.

Server Action에서 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag), [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh) 같은 재검증 함수를 호출하면, stale 시간을 무시하고 클라이언트 캐시 전체가 즉시 비워집니다.

> **알아두면 좋아요** : `cacheLife`의 `stale` 속성은 [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)와 다릅니다. `staleTimes`는 모든 라우트에 영향을 주는 전역 설정인 반면, `cacheLife`는 함수 또는 라우트별 구성을 제공합니다. `staleTimes.static`을 업데이트하면 `default` 캐시 프로필의 `stale` 값도 함께 갱신됩니다.

## Examples[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#examples)

### Using preset profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-preset-profiles-1)

프리셋 프로필을 사용하는 것이 캐싱을 구성하는 가장 간단한 방법입니다. 콘텐츠 업데이트 패턴에 맞는 프로필을 선택하세요:

app/blog/[slug]/page.tsx
```
    import { cacheLife } from 'next/cache'

    export default async function BlogPost() {
      'use cache'
      cacheLife('days') // Blog posts updated daily

      const post = await fetchBlogPost()
      return <article>{post.content}</article>
    }
```

app/products/[id]/page.tsx
```
    import { cacheLife } from 'next/cache'

    export default async function ProductPage() {
      'use cache'
      cacheLife('hours') // Product data updated multiple times per day

      const product = await fetchProduct()
      return <div>{product.name}</div>
    }
```

### Custom profiles for specific needs[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#custom-profiles-for-specific-needs)

프리셋 옵션이 요구 사항에 맞지 않을 때는 사용자 정의 프로필을 정의하세요:

next.config.ts

```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheComponents: true,
      cacheLife: {
        editorial: {
          stale: 600, // 10 minutes
          revalidate: 3600, // 1 hour
          expire: 86400, // 1 day
        },
        marketing: {
          stale: 300, // 5 minutes
          revalidate: 1800, // 30 minutes
          expire: 43200, // 12 hours
        },
      },
    }

    export default nextConfig
```

그런 다음 애플리케이션 전반에서 이러한 프로필을 사용하세요:

app/editorial/page.tsx
```
    import { cacheLife } from 'next/cache'

    export default async function EditorialPage() {
      'use cache'
      cacheLife('editorial')
      // ...
    }
```

### 고유한 사례를 위한 인라인 프로필[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-profiles-for-unique-cases)

특정 함수에 일회성 캐싱 동작이 필요할 때 인라인 프로필을 사용하세요:

app/api/limited-offer/route.ts
```
    import { cacheLife } from 'next/cache'
    import { getDb } from '@lib/db'

    async function getLimitedOffer() {
      'use cache'

      cacheLife({
        stale: 60, // 1 minute
        revalidate: 300, // 5 minutes
        expire: 3600, // 1 hour
      })

      const offer = await getDb().offer.findFirst({
        where: { type: 'limited' },
        orderBy: { created_at: 'desc' },
      })

      return offer
    }

    export async function GET() {
      const offer = await getLimitedOffer()

      return Response.json(offer)
    }
```

### 개별 함수 캐싱[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#caching-individual-functions)

세밀하게 제어하려면 유틸리티 함수에 캐싱을 적용하세요:

lib/api.ts
```
    import { cacheLife } from 'next/cache'

    export async function getSettings() {
      'use cache'
      cacheLife('max') // Settings rarely change

      return await fetchSettings()
    }
```

lib/stats.ts
```
    import { cacheLife } from 'next/cache'

    export async function getRealtimeStats() {
      'use cache'
      cacheLife('seconds') // Stats update constantly

      return await fetchStats()
    }
```

### 중첩 캐싱 동작[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#nested-caching-behavior)

캐시된 함수 또는 컴포넌트가 다른 캐시된 함수 또는 컴포넌트를 사용할 때처럼 `use cache` 지시어를 중첩하면, 외부 캐시의 동작은 명시적 `cacheLife` 존재 여부에 따라 달라집니다.

#### 명시적 외부 cacheLife가 있는 경우[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#with-explicit-outer-cachelife)

외부 캐시는 내부 캐시 수명과 관계없이 자체 수명을 사용합니다. 외부 캐시가 적중하면 모든 중첩 데이터를 포함한 완전한 출력이 반환됩니다. 명시적 `cacheLife`는 내부 수명보다 길거나 짧더라도 항상 우선합니다.

app/dashboard/page.tsx
```
    import { cacheLife } from 'next/cache'
    import { Widget } from './widget'

    export default async function Dashboard() {
      'use cache'
      cacheLife('hours') // Outer scope sets its own lifetime

      return (
        <div>
          <h1>Dashboard</h1>
          <Widget /> {/* Inner scope has 'minutes' lifetime */}
        </div>
      )
    }
```

#### 명시적 외부 cacheLife가 없는 경우[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#without-explicit-outer-cachelife)

외부 캐시에서 `cacheLife`를 호출하지 않으면 `default` 프로필(재검증 15분)을 사용합니다. 수명이 더 짧은 내부 캐시는 외부 캐시의 `default` 수명을 줄일 수 있지만, 더 긴 내부 캐시는 이를 기본값 이상으로 연장할 수 없습니다.

app/dashboard/page.tsx
```
    import { Widget } from './widget'

    export default async function Dashboard() {
      'use cache'
      // No cacheLife call - uses default (15 min)
      // If Widget has 5 min → Dashboard becomes 5 min
      // If Widget has 1 hour → Dashboard stays 15 min

      return (
        <div>
          <h1>Dashboard</h1>
          <Widget />
        </div>
      )
    }
```

**명시적으로 `cacheLife`를 지정하는 것이 좋습니다.** 수명 값을 명시해 두면 캐시된 함수나 컴포넌트를 확인할 때 중첩 캐시를 추적하지 않고도 즉시 동작을 파악할 수 있습니다. 수명을 명시하지 않으면 동작이 내부 캐시 수명에 따라 달라져 파악하기가 어려워집니다.

### 조건부 캐시 수명[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#conditional-cache-lifetimes)

애플리케이션 로직에 따라 다른 코드 경로에서 `cacheLife`를 조건부로 호출하여 서로 다른 캐시 기간을 설정할 수 있습니다:

lib/posts.ts
```
    import { cacheLife, cacheTag } from 'next/cache'

    async function getPostContent(slug: string) {
      'use cache'

      const post = await fetchPost(slug)

      // Tag the cache entry for targeted revalidation
      cacheTag(`post-${slug}`)

      if (!post) {
        // Content may not be published yet or could be in draft
        // Cache briefly to reduce database load
        cacheLife('minutes')
        return null
      }

      // Published content can be cached longer
      cacheLife('days')

      // Return only the necessary data to keep cache size minimal
      return post.data
    }
```

이 패턴은 항목이 아직 없지만 나중에 제공될 가능성이 있는 경우처럼 서로 다른 결과에 서로 다른 캐시 기간이 필요한 상황에서 유용합니다.

#### 데이터 기반 동적 캐시 수명 사용[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-dynamic-cache-lifetimes-from-data)

예를 들어 가져온 데이터에서 값을 읽어 런타임에 캐시 수명을 계산하려면 [인라인 캐시 프로필](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-cache-profiles) 객체를 사용하세요:

lib/posts.ts
```
    import { cacheLife, cacheTag } from 'next/cache'

    async function getPostContent(slug: string) {
      'use cache'

      const post = await fetchPost(slug)
      cacheTag(`post-${slug}`)

      if (!post) {
        cacheLife('minutes')
        return null
      }

      // Use cache timing from CMS data directly as an object
      cacheLife({
        // Ensure post.revalidateSeconds is a number in seconds
        // stale and expire inherit from 'default' profile
        revalidate: post.revalidateSeconds ?? 3600,
      })

      return post.data
    }
```

## 관련 항목

관련 API 레퍼런스를 확인하세요.

- [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
  - Next.js에서 cacheComponents 플래그를 활성화하는 방법을 알아보세요.
- [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  - Next.js 애플리케이션에서 "use cache" 지시어를 사용해 데이터를 캐시하는 방법을 알아보세요.
- [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
  - revalidateTag 함수의 API 레퍼런스입니다.
- [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
  - Next.js 애플리케이션에서 cacheTag 함수를 사용해 캐시 무효화를 관리하는 방법을 알아보세요.