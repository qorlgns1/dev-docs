---
title: 'next.config.js: assetPrefix'
description: '마지막 업데이트: 2026년 2월 20일'
---

# next.config.js: assetPrefix | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)assetPrefix

페이지 복사

# assetPrefix

마지막 업데이트: 2026년 2월 20일

> **주의**: [Vercel에 배포](https://nextjs.org/docs/app/getting-started/deploying)하면 Next.js 프로젝트에 대한 글로벌 CDN이 자동으로 구성됩니다. Asset Prefix를 수동으로 설정할 필요가 없습니다.
>
> **알아두기 좋습니다**: Next.js 9.5+에서는 사용자 정의 가능한 [Base Path](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)를 지원하며, `/docs` 같은 하위 경로에서 애플리케이션을 호스팅할 때 더 적합합니다. 이 사용 사례에는 사용자 정의 Asset Prefix 사용을 권장하지 않습니다.

## CDN 설정[](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix#set-up-a-cdn)

[CDN](https://en.wikipedia.org/wiki/Content_delivery_network)을 설정하려면 asset prefix를 지정하고 CDN의 오리진이 Next.js가 호스팅되는 도메인을 가리키도록 구성하면 됩니다.

`next.config.mjs`를 열고 [phase](https://nextjs.org/docs/app/api-reference/config/next-config-js#async-configuration)에 따라 `assetPrefix` 설정을 추가하세요:

next.config.mjs
```
// @ts-check
import { PHASE_DEVELOPMENT_SERVER } from 'next/constants'
 
export default (phase) => {
  const isDev = phase === PHASE_DEVELOPMENT_SERVER
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    assetPrefix: isDev ? undefined : 'https://cdn.mydomain.com',
  }
  return nextConfig
}
```

Next.js는 `/_next/` 경로(`.next/static/` 폴더)에서 로드하는 JavaScript 및 CSS 파일에 자동으로 asset prefix를 적용합니다. 예를 들어 위 구성에서 다음 JS 청크 요청은:
```
/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

다음과 같이 변경됩니다:
```
https://cdn.mydomain.com/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

CDN에 파일을 업로드하는 정확한 방식은 선택한 CDN에 따라 달라집니다. CDN에 호스팅해야 하는 유일한 폴더는 `.next/static/`의 내용이며, 위 URL 요청에서 알 수 있듯 `_next/static/`으로 업로드해야 합니다. **나머지 `.next/` 폴더는 업로드하지 마세요**, 서버 코드와 기타 구성을 외부에 노출해서는 안 됩니다.

`assetPrefix`는 `_next/static`에 대한 요청만 다루며, 다음 경로에는 영향을 주지 않습니다:

- [public](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) 폴더 내 파일. 해당 자산을 CDN으로 제공하려면 직접 prefix를 추가해야 합니다.

도움이 되었나요?

지원됩니다.

보내기
