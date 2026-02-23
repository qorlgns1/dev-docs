---
title: 'next.config.js: staleTimes'
description: '이 기능은 현재 실험적 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 시도해 보고 GitHub에서 피드백을 공유해 주세요.'
---

# next.config.js: staleTimes | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes

# staleTimes

이 기능은 현재 실험적 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 시도해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

`staleTimes`는 [클라이언트 라우터 캐시](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)에서 페이지 세그먼트를 캐싱할 수 있게 해 주는 실험적 기능입니다.

다음과 같이 실험적 `staleTimes` 플래그를 설정하면 이 기능을 활성화하고 사용자 지정 재검증 시간을 지정할 수 있습니다:

next.config.js
```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}

module.exports = nextConfig
```

`static`과 `dynamic` 속성은 서로 다른 유형의 [링크 프리페치](https://nextjs.org/docs/app/api-reference/components/link#prefetch)에 따라 기간(초)을 지정합니다.

  * `dynamic` 속성은 페이지가 정적으로 생성되지 않았거나 `prefetch={true}`와 같이 완전히 프리페치되지 않은 경우 사용됩니다.
    * 기본값: 0초(캐시하지 않음)
  * `static` 속성은 정적으로 생성된 페이지이거나 `Link`의 `prefetch` prop을 `true`로 설정했을 때, 또는 [`router.prefetch`](https://nextjs.org/docs/app/guides/caching#routerprefetch)를 호출할 때 사용됩니다.
    * 기본값: 5분

> **알아두면 좋은 점:**
>
>   * [로딩 경계](https://nextjs.org/docs/app/api-reference/file-conventions/loading)는 이 설정에서 정의한 `static` 기간 동안 재사용 가능한 것으로 간주됩니다.
>   * 이는 [부분 렌더링](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)에 영향을 주지 않으며, **공유 레이아웃은 내비게이션마다 자동으로 다시 가져오지 않고 변경된 페이지 세그먼트만 다시 가져옵니다.**
>   * 이는 레이아웃 시프트와 브라우저 스크롤 위치 손실을 방지하기 위해 [뒤로/앞으로 캐싱](https://nextjs.org/docs/app/guides/caching#client-side-router-cache) 동작을 변경하지 않습니다.
>

클라이언트 라우터 캐시에 대해 더 알아보려면 [여기](https://nextjs.org/docs/app/guides/caching#client-side-router-cache)를 참고하세요.

### 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes#version-history)

버전| 변경 사항
---|---
`v15.0.0`| `dynamic` `staleTimes` 기본값이 30초에서 0초로 변경되었습니다.
`v14.2.0`| 실험적 `staleTimes`가 도입되었습니다.

보내기