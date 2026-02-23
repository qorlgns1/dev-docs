---
title: 'next.config.js: compress'
description: '기본적으로 Next.js는  또는 커스텀 서버를 사용할 때 렌더링된 콘텐츠와 정적 파일을 압축하기 위해 을 사용합니다. 이는 압축이 구성되어 있지 않은 애플리케이션을 위한 최적화입니다. 커스텀 서버를 통해 애플리케이션에서 이미 압축을 구성한 경우 Next.js는 압축을...'
---

# next.config.js: compress | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/compress

# compress

마지막 업데이트 2026년 2월 20일

기본적으로 Next.js는 `next start` 또는 커스텀 서버를 사용할 때 렌더링된 콘텐츠와 정적 파일을 압축하기 위해 `gzip`을 사용합니다. 이는 압축이 구성되어 있지 않은 애플리케이션을 위한 최적화입니다. 커스텀 서버를 통해 애플리케이션에서 이미 압축을 구성한 경우 Next.js는 압축을 추가하지 않습니다.

압축 활성화 여부와 사용 중인 알고리즘은 응답의 [`Accept-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) (브라우저가 허용하는 옵션) 및 [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) (현재 사용 중인 값) 헤더를 확인하여 알 수 있습니다.

## 압축 비활성화[](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress#disabling-compression)

**compression** 을 비활성화하려면 `compress` 구성 옵션을 `false`로 설정하세요:

next.config.js
```
    module.exports = {
      compress: false,
    }
```

압축은 대역폭 사용량을 줄이고 애플리케이션 성능을 개선하므로, 서버에서 압축을 구성해 두지 않았다면 **압축 비활성화를 권장하지 않습니다**. 예를 들어 [nginx](https://nginx.org/)를 사용 중이며 `brotli`로 전환하려는 경우, nginx가 압축을 처리하도록 `compress` 옵션을 `false`로 설정하세요.

supported.