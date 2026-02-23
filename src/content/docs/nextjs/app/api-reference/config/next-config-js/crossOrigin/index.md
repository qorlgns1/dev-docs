---
title: 'next.config.js: crossOrigin'
description: '옵션을 사용하면  컴포넌트가 생성하는 모든  태그에  속성을 추가하고, 교차 출처 요청을 처리하는 방식을 정의할 수 있습니다.'
---

# next.config.js: crossOrigin | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin

# crossOrigin

마지막 업데이트: 2026년 2월 20일

`crossOrigin` 옵션을 사용하면 [`next/script`](https://nextjs.org/docs/app/guides/scripts) 컴포넌트가 생성하는 모든 `<script>` 태그에 [`crossOrigin` 속성](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin)을 추가하고, 교차 출처 요청을 처리하는 방식을 정의할 수 있습니다.

next.config.js
```
    module.exports = {
      crossOrigin: 'anonymous',
    }
```

## 옵션[](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin#options)

  * `'anonymous'`: [`crossOrigin="anonymous"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#anonymous) 속성을 추가합니다.
  * `'use-credentials'`: [`crossOrigin="use-credentials"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#use-credentials) 속성을 추가합니다.

보내기