---
title: 'next.config.js Options: crossOrigin'
description: '옵션을 사용하면 와  컴포넌트가 생성하는 모든  태그에  속성을 추가하고, 크로스 오리진 요청을 어떻게 처리할지 정의할 수 있습니다.'
---

# next.config.js Options: crossOrigin | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin

Copy page

# crossOrigin

Last updated February 20, 2026

`crossOrigin` 옵션을 사용하면 [`next/script`](https://nextjs.org/docs/pages/guides/scripts)와 [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head) 컴포넌트가 생성하는 모든 `<script>` 태그에 [`crossOrigin` 속성](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin)을 추가하고, 크로스 오리진 요청을 어떻게 처리할지 정의할 수 있습니다.

next.config.js
```
    module.exports = {
      crossOrigin: 'anonymous',
    }
```

## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin#options)

  * `'anonymous'`: [`crossOrigin="anonymous"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#anonymous) 속성을 추가합니다.
  * `'use-credentials'`: [`crossOrigin="use-credentials"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#use-credentials) 속성을 추가합니다.

Was this helpful?

supported.

Send