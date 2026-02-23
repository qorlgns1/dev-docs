---
title: 'next.config.js 옵션: compress'
description: '기본적으로 Next.js는  또는 커스텀 서버를 사용할 때 렌더링된 콘텐츠와 정적 파일을 으로 압축합니다. 이는 압축을 별도로 구성하지 않은 애플리케이션을 위한 최적화입니다. 커스텀 서버를 통해 애플리케이션에 이미 압축이 구성되어 있다면 Next.js는 추가 압축을 적...'
---

# next.config.js 옵션: compress | Next.js
출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)compress

페이지 복사

# compress

마지막 업데이트 2026년 2월 20일

기본적으로 Next.js는 `next start` 또는 커스텀 서버를 사용할 때 렌더링된 콘텐츠와 정적 파일을 `gzip`으로 압축합니다. 이는 압축을 별도로 구성하지 않은 애플리케이션을 위한 최적화입니다. 커스텀 서버를 통해 애플리케이션에 이미 압축이 구성되어 있다면 Next.js는 추가 압축을 적용하지 않습니다.

응답의 [`Accept-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) 헤더(브라우저에서 허용하는 옵션)와 [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) 헤더(현재 사용 중)를 확인하여 압축이 활성화되어 있는지와 사용 중인 알고리즘을 확인할 수 있습니다.

## 압축 비활성화[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress#disabling-compression)

**compression** 을 비활성화하려면 `compress` 구성 옵션을 `false`로 설정하세요:

next.config.js
[code]
    module.exports = {
      compress: false,
    }
[/code]

압축은 대역폭 사용량을 줄이고 애플리케이션 성능을 향상시키므로, 서버에 이미 압축이 구성되어 있는 경우가 아니라면 압축을 비활성화하지 않는 것이 좋습니다. 예를 들어 [nginx](https://nginx.org/)를 사용하면서 `brotli`로 전환하려는 경우, `compress` 옵션을 `false`로 설정해 nginx가 압축을 처리하도록 하세요.

도움이 되었나요?

지원됨.

전송
