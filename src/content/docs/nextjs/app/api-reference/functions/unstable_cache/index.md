---
title: 'Functions: unstable_cache'
description: '마지막 업데이트 2026년 2월 20일'
---

# Functions: unstable_cache | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/unstable_cache

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)unstable_cache

Copy page

# unstable_cache

마지막 업데이트 2026년 2월 20일

> **참고:** 이 API는 Next.js 16에서 [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)로 대체되었습니다. [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용하도록 전환하고 `unstable_cache`를 `use cache` 지시어로 교체하는 것을 권장합니다.

`unstable_cache`는 데이터베이스 쿼리 같은 비용이 큰 작업 결과를 캐싱하고 여러 요청에서 재사용할 수 있게 해 줍니다.
[code] 
    import { getUser } from './data';
    import { unstable_cache } from 'next/cache';
     
    const getCachedUser = unstable_cache(
      async (id) => getUser(id),
      ['my-app-user']
    );
     
    export default async function Component({ userID }) {
      const user = await getCachedUser(userID);
      ...
    }
[/code]

> **알아두면 좋은 점** :
> 
>   * 캐시 범위 안에서 `headers` 또는 `cookies` 같은 동적 데이터 소스에 접근하는 것은 지원되지 않습니다. 캐시된 함수 내부에서 이 데이터가 필요하면 `headers`를 캐시 함수 밖에서 호출하고 필요한 동적 데이터를 인자로 전달하세요.
>   * 이 API는 Next.js의 내장 [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)를 사용해 요청과 배포 간에 결과를 유지합니다.
> 


## Parameters[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#parameters)
[code] 
    const data = unstable_cache(fetchData, keyParts, options)()
[/code]

  * `fetchData`: 캐싱하려는 데이터를 가져오는 비동기 함수입니다. `Promise`를 반환해야 합니다.
  * `keyParts`: 캐시에 추가 식별 정보를 부여하는 키 배열입니다. 기본적으로 `unstable_cache`는 이미 인자와 함수의 문자열화 버전을 캐시 키로 사용합니다. 대부분의 경우 선택 사항이며, 매개변수로 전달하지 않은 외부 변수를 사용할 때만 필요합니다. 단, 매개변수로 전달하지 않은 클로저를 함수 안에서 사용한다면 반드시 추가해야 합니다.
  * `options`: 캐시 동작 방식을 제어하는 객체입니다. 다음 속성을 포함할 수 있습니다.
    * `tags`: 캐시 무효화를 제어하는 데 사용할 수 있는 태그 배열입니다. Next.js는 이를 함수의 고유 식별에 사용하지 않습니다.
    * `revalidate`: 캐시를 재검증해야 하는 초 단위 시간입니다. 생략하거나 `false`를 전달하면 동일한 `revalidateTag()` 또는 `revalidatePath()` 호출이 있을 때까지 무기한 캐시합니다.



## Returns[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#returns)

`unstable_cache`는 호출 시 캐시된 데이터로 해결되는 Promise를 반환하는 함수를 반환합니다. 데이터가 캐시에 없으면 제공된 함수가 실행되고 그 결과가 캐시된 뒤 반환됩니다.

## Example[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#example)

app/page.tsx

JavaScriptTypeScript
[code]
    import { unstable_cache } from 'next/cache'
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ userId: string }>
    }) {
      const { userId } = await params
      const getCachedUser = unstable_cache(
        async () => {
          return { id: userId }
        },
        [userId], // add the user ID to the cache key
        {
          tags: ['users'],
          revalidate: 60,
        }
      )
     
      //...
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#version-history)

Version| Changes  
---|---  
`v14.0.0`| `unstable_cache` 도입.  
  
Was this helpful?

supported.

Send
