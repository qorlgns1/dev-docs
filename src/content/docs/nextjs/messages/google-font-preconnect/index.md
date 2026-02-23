---
title: 'Google Font Preconnect'
description: '> 참고: Next.js는 버전  이후 자동으로 를 추가합니다.'
---

# Google Font Preconnect | Next.js

출처 URL: https://nextjs.org/docs/messages/google-font-preconnect

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)Google Font Preconnect

# Google Font Preconnect

> **참고**: Next.js는 버전 `12.0.1` 이후 자동으로 `<link rel="preconnect" />`를 추가합니다.

> Google Fonts를 사용할 때 `preconnect`를 반드시 사용하세요.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/google-font-preconnect#why-this-error-occurred)

Google Fonts 도메인에 대한 요청에 preconnect 리소스 힌트가 사용되지 않았습니다. 원본에 미리 연결을 설정할 수 있도록 `preconnect`를 추가하는 것이 권장됩니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/google-font-preconnect#possible-ways-to-fix-it)

Google Font 도메인의 `<link>` 태그에 `rel="preconnect"`를 추가하세요:

pages/_document.js
```
    <link rel="preconnect" href="https://fonts.gstatic.com" />
```

> **참고**: `preconnect`를 지원하지 않는 브라우저를 위한 폴백으로 `dns-prefetch`가 있는 **별도의** 링크를 사용할 수 있지만 필수는 아닙니다.

## 유용한 링크[](https://nextjs.org/docs/messages/google-font-preconnect#useful-links)

  * [필요한 출처에 Preconnect](https://web.dev/uses-rel-preconnect/)
  * [Preconnect와 dns-prefetch](https://web.dev/preconnect-and-dns-prefetch/#resolve-domain-name-early-with-reldns-prefetch)
  * [Next.js Font Optimization](https://nextjs.org/docs/pages/api-reference/components/font)