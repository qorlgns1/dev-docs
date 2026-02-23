---
title: 'next.config.js: serverActions'
description: 'Next.js 애플리케이션에서 Server Actions 동작을 구성하기 위한 옵션입니다.'
---

# next.config.js: serverActions | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions

# serverActions

마지막 업데이트: 2026년 2월 20일

Next.js 애플리케이션에서 Server Actions 동작을 구성하기 위한 옵션입니다.

## `allowedOrigins`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#allowedorigins)

Server Actions를 호출할 수 있도록 허용할 추가 안전 출처 도메인 목록입니다. Next.js는 Server Action 요청의 origin을 호스트 도메인과 비교하여 일치하는지 확인함으로써 CSRF 공격을 방지합니다. 값을 지정하지 않으면 동일한 origin만 허용됩니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */

    module.exports = {
      experimental: {
        serverActions: {
          allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
        },
      },
    }
[/code]

## `bodySizeLimit`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#bodysizelimit)

기본적으로 Server Action에 전송되는 요청 본문의 최대 크기는 1MB이며, 이는 대량의 데이터를 파싱할 때 과도한 서버 리소스 소비와 잠재적인 DDoS 공격을 방지하기 위한 것입니다.

그러나 `serverActions.bodySizeLimit` 옵션을 사용해 이 제한을 구성할 수 있습니다. 바이트 수나 bytes 패키지가 지원하는 문자열 형식(`1000`, `'500kb'`, `'3mb'` 등)을 사용할 수 있습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */

    module.exports = {
      experimental: {
        serverActions: {
          bodySizeLimit: '2mb',
        },
      },
    }
[/code]

## Enabling Server Actions (v13)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#enabling-server-actions-v13)

Server Actions는 Next.js 14에서 안정적인 기능이 되었으며 기본적으로 활성화됩니다. 하지만 더 이전 버전의 Next.js를 사용 중이라면 `experimental.serverActions`를 `true`로 설정하여 활성화할 수 있습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const config = {
      experimental: {
        serverActions: true,
      },
    }

    module.exports = config
[/code]
