---
title: 'Functions: unstable_noStore'
description: '이 API는 레거시로 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.'
---

# Functions: unstable_noStore | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/unstable_noStore

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)unstable_noStore

Copy page

# unstable_noStore

이 API는 레거시로 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.

최종 업데이트 2026년 2월 20일

**버전 15에서는 `unstable_noStore` 대신 [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection)을 사용하는 것을 권장합니다.**

`unstable_noStore`를 사용하면 정적 렌더링을 선언적으로 비활성화하고 특정 컴포넌트를 캐싱하지 말아야 함을 나타낼 수 있습니다.
[code] 
    import { unstable_noStore as noStore } from 'next/cache';
     
    export default async function ServerComponent() {
      noStore();
      const result = await db.query(...);
      ...
    }
[/code]

> **알아두면 좋은 점** :
> 
>   * `unstable_noStore`는 `fetch`에서 `cache: 'no-store'`와 동일합니다.
>   * `unstable_noStore`는 더 세밀하고 컴포넌트 단위로 사용할 수 있으므로 `export const dynamic = 'force-dynamic'`보다 선호됩니다.
> 


  * [`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache) 내부에서 `unstable_noStore`를 사용해도 정적 생성에서 제외되지 않습니다. 대신 캐시 구성에 따라 결과를 캐시할지 여부가 결정됩니다.



## Usage[](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore#usage)

`fetch`에 `cache: 'no-store'`, `next: { revalidate: 0 }` 같은 추가 옵션을 전달하고 싶지 않거나 `fetch`를 사용할 수 없는 경우, 모든 이러한 사용 사례를 대신해 `noStore()`를 사용할 수 있습니다.
[code] 
    import { unstable_noStore as noStore } from 'next/cache';
     
    export default async function ServerComponent() {
      noStore();
      const result = await db.query(...);
      ...
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore#version-history)

Version| Changes  
---|---  
`v15.0.0`| `unstable_noStore`가 `connection`으로 대체되도록 deprecated되었습니다.  
`v14.0.0`| `unstable_noStore`가 도입되었습니다.  
  
도움이 되었나요?

supported.

Send
