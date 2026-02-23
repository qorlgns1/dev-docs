---
title: 'next.config.js 옵션: assetPrefix'
description: '> 주의 : Vercel에 배포하면 Next.js 프로젝트를 위한 전역 CDN이 자동으로 설정됩니다. Asset Prefix를 수동으로 설정할 필요가 없습니다.'
---

# next.config.js 옵션: assetPrefix | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js)assetPrefix

페이지 복사

# assetPrefix

최종 업데이트 2026년 2월 20일

> **주의** : [Vercel에 배포](https://nextjs.org/docs/pages/getting-started/deploying)하면 Next.js 프로젝트를 위한 전역 CDN이 자동으로 설정됩니다. Asset Prefix를 수동으로 설정할 필요가 없습니다.

> **알아두면 좋아요** : Next.js 9.5+에서는 사용자 정의 [Base Path](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)를 지원하며, `/docs` 같은 하위 경로에 애플리케이션을 호스팅할 때 더 적합합니다. 이 용도에는 사용자 정의 Asset Prefix 사용을 권장하지 않습니다.

## CDN 설정[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix#set-up-a-cdn)

[CDN](https://en.wikipedia.org/wiki/Content_delivery_network)을 설정하려면 asset prefix를 지정하고 CDN의 오리진이 Next.js가 호스팅된 도메인을 가리키도록 구성하면 됩니다.

`next.config.mjs`를 열고 [phase](https://nextjs.org/docs/app/api-reference/config/next-config-js#async-configuration)에 따라 `assetPrefix` 설정을 추가하세요:

next.config.mjs
[code]
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
[/code]

Next.js는 `/_next/` 경로(`.next/static/` 폴더)에서 로드하는 JavaScript 및 CSS 파일에 지정한 asset prefix를 자동으로 사용합니다. 예를 들어 위 설정에서는 JS 청크 요청이 다음과 같습니다:
[code] 
    /_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
    
[/code]

그러면 다음과 같은 요청으로 바뀝니다:
[code] 
    https://cdn.mydomain.com/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
    
[/code]

특정 CDN에 파일을 업로드하는 정확한 방법은 사용하는 CDN에 따라 달라집니다. CDN에 호스팅해야 하는 폴더는 `.next/static/`의 내용뿐이며, 위 URL 요청에서 보이듯 `_next/static/`으로 업로드해야 합니다. **`.next/` 폴더의 나머지는 업로드하지 마세요**, 서버 코드와 기타 구성이 공개되지 않아야 합니다.

`assetPrefix`는 `_next/static` 요청을 처리하지만 다음 경로에는 영향을 주지 않습니다:

  * [public](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) 폴더의 파일. 이를 CDN으로 제공하려면 직접 prefix를 추가해야 합니다.
  * `getServerSideProps` 페이지의 `/_next/data/` 요청. 정적이 아니므로 항상 메인 도메인으로 요청합니다.
  * `getStaticProps` 페이지의 `/_next/data/` 요청. [Incremental Static Generation](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)을 지원하기 위해, 사용 여부와 관계없이 항상 메인 도메인으로 요청합니다(일관성을 위한 동작).



도움이 되었나요?

지원됨.

전송
