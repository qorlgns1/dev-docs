---
title: '함수: fetch'
description: 'Next.js는 Web  API를 확장해 서버에서 수행되는 각 요청이 고유한 영구 캐싱 및 재검증 규칙을 설정할 수 있게 합니다.'
---

# 함수: fetch | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/fetch

Copy page

# fetch

마지막 업데이트 2026년 2월 20일

Next.js는 [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API)를 확장해 서버에서 수행되는 각 요청이 고유한 영구 캐싱 및 재검증 규칙을 설정할 수 있게 합니다.

브라우저에서는 `cache` 옵션이 fetch 요청이 _브라우저_ HTTP 캐시와 어떻게 상호작용할지 나타냅니다. 이 확장을 통해 `cache`는 _서버 측_ fetch 요청이 프레임워크의 영구 [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)와 어떻게 상호작용할지 나타냅니다.

Server Component 내부에서 `async`/`await`와 함께 직접 `fetch`를 호출할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      let data = await fetch('https://api.vercel.app/blog')
      let posts = await data.json()
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

## `fetch(url, options)`[](https://nextjs.org/docs/app/api-reference/functions/fetch#fetchurl-options)

Next.js는 [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API)를 확장하므로, [사용 가능한 네이티브 옵션](https://developer.mozilla.org/docs/Web/API/fetch#parameters)을 모두 사용할 수 있습니다.

### `options.cache`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionscache)

요청이 Next.js [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache)와 어떻게 상호작용할지 구성합니다.
[code]
    fetch(`https://...`, { cache: 'force-cache' | 'no-store' })
[/code]

  * **`auto no cache`** (기본값): 개발 환경에서는 Next.js가 매 요청마다 원격 서버에서 리소스를 가져오지만, 경로가 정적으로 사전 렌더링되므로 `next build` 중에는 한 번만 가져옵니다. 경로에서 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)를 감지하면 Next.js는 매 요청마다 리소스를 가져옵니다.
  * **`no-store`**: 경로에서 Dynamic API가 감지되지 않았더라도 매 요청마다 Next.js가 원격 서버에서 리소스를 가져옵니다.
  * **`force-cache`**: Next.js가 Data Cache에서 일치하는 요청을 찾습니다.
    * 일치 항목이 있고 최신이면 캐시에서 반환됩니다.
    * 일치 항목이 없거나 만료되었으면 Next.js가 원격 서버에서 리소스를 가져와 다운로드한 리소스로 캐시를 업데이트합니다.

### `options.next.revalidate`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnextrevalidate)
[code]
    fetch(`https://...`, { next: { revalidate: false | 0 | number } })
[/code]

리소스의 캐시 수명을 초 단위로 설정합니다. [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache).

  * **`false`** \- 리소스를 무기한 캐시합니다. 의미상 `revalidate: Infinity`와 같습니다. HTTP 캐시는 시간이 지나면 오래된 리소스를 제거할 수 있습니다.
  * **`0`** \- 리소스 캐싱을 방지합니다.
  * **`number`** \- (초) 리소스가 최대 `n`초 동안 캐시 수명을 갖도록 지정합니다.

> **알아두면 좋은 점** :
>
>   * 개별 `fetch()` 요청이 경로의 [기본 `revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate)보다 낮은 `revalidate` 값을 설정하면 전체 경로의 재검증 주기가 그 값으로 단축됩니다.
>   * 동일한 경로에서 동일한 URL을 사용하는 두 fetch 요청의 `revalidate` 값이 다르면 더 낮은 값이 사용됩니다.
>   * `{ revalidate: 3600, cache: 'no-store' }`처럼 충돌하는 옵션은 허용되지 않으며, 둘 다 무시되고 개발 모드에서는 터미널에 경고가 출력됩니다.
>

### `options.next.tags`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnexttags)
[code]
    fetch(`https://...`, { next: { tags: ['collection'] } })
[/code]

리소스의 캐시 태그를 설정합니다. 이후 [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)를 사용해 필요 시 데이터를 재검증할 수 있습니다. 사용자 정의 태그의 최대 길이는 256자이며 태그 항목은 최대 128개입니다.

## 문제 해결[](https://nextjs.org/docs/app/api-reference/functions/fetch#troubleshooting)

### 기본 `auto no store` 및 `cache: 'no-store'`가 개발 환경에서 최신 데이터를 보여주지 않는 경우[](https://nextjs.org/docs/app/api-reference/functions/fetch#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development)

Next.js는 응답 속도를 높이고 과금되는 API 호출 비용을 줄이기 위해 로컬 개발에서 Hot Module Replacement(HMR) 동안 Server Component의 `fetch` 응답을 캐시합니다.

기본적으로 [HMR 캐시](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)는 기본 `auto no cache` 및 `cache: 'no-store'` 옵션을 포함해 모든 fetch 요청에 적용됩니다. 따라서 캐시되지 않은 요청도 HMR 새로 고침 사이에서는 최신 데이터를 보여주지 않습니다. 단, 네비게이션 또는 전체 페이지 새로 고침 시 캐시가 지워집니다.

자세한 내용은 [`serverComponentsHmrCache`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) 문서를 참고하세요.

### 개발 환경에서 하드 새로 고침과 캐싱[](https://nextjs.org/docs/app/api-reference/functions/fetch#hard-refresh-and-caching-in-development)

개발 모드에서 요청에 `cache-control: no-cache` 헤더가 포함되면 `options.cache`, `options.next.revalidate`, `options.next.tags`가 모두 무시되고 `fetch` 요청이 소스에서 직접 제공됩니다.

브라우저는 일반적으로 개발자 도구에서 캐시를 비활성화했을 때나 하드 새로 고침 중에 `cache-control: no-cache`를 포함합니다.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/fetch#version-history)

Version| Changes
---|---
`v13.0.0`| `fetch` 도입.

supported.

Send
