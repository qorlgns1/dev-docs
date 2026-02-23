---
title: 'next.config.js: proxyClientMaxBodySize'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 사용을 권장하지 않습니다. 직접 사용해 보고 GitHub에서 피드백을 공유하세요.'
---

# next.config.js: proxyClientMaxBodySize | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize

# proxyClientMaxBodySize

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 사용을 권장하지 않습니다. 직접 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유하세요.

마지막 업데이트: 2026년 2월 20일

프록시가 사용될 때, Next.js는 요청 본문을 자동으로 복제해 메모리에 버퍼링하여 프록시와 하위 라우트 핸들러 모두에서 여러 번 읽을 수 있도록 합니다. 과도한 메모리 사용을 방지하기 위해, 이 구성 옵션은 버퍼링되는 본문의 크기 제한을 설정합니다.

기본적으로 최대 본문 크기는 **10MB**입니다. 요청 본문이 이 한계를 넘으면 본문은 한계까지만 버퍼링되며, 어떤 라우트가 한계를 초과했는지 콘솔에 경고가 기록됩니다.

## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#options)

### String format (recommended)[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#string-format-recommended)

사람이 읽기 쉬운 문자열 형식으로 크기를 지정합니다.

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        proxyClientMaxBodySize: '1mb',
      },
    }

    export default nextConfig
```

지원 단위: `b`, `kb`, `mb`, `gb`

### Number format[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#number-format)

또는 숫자로 바이트 단위 크기를 지정합니다.

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        proxyClientMaxBodySize: 1048576, // 1MB in bytes
      },
    }

    export default nextConfig
```

## Behavior[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#behavior)

요청 본문이 설정된 한계를 초과하면 다음이 발생합니다.

  1. Next.js가 처음 N바이트(한계까지)만 버퍼링합니다.
  2. 어떤 라우트가 한계를 초과했는지 콘솔에 경고가 기록됩니다.
  3. 요청은 정상적으로 계속 처리되지만, 사용할 수 있는 본문은 부분 데이터뿐입니다.
  4. 요청이 실패하거나 클라이언트에 오류를 반환하지는 않습니다.

애플리케이션이 전체 요청 본문을 처리해야 한다면 다음 중 하나를 수행하세요.

  * `proxyClientMaxBodySize` 한계를 높입니다.
  * 애플리케이션 로직에서 부분 본문을 적절히 처리합니다.

## Example[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#example)

proxy.ts
```
    import { NextRequest, NextResponse } from 'next/server'

    export async function proxy(request: NextRequest) {
      // Next.js automatically buffers the body with the configured size limit
      // You can read the body in proxy...
      const body = await request.text()

      // If the body exceeded the limit, only partial data will be available
      console.log('Body size:', body.length)

      return NextResponse.next()
    }
```

app/api/upload/route.ts
```
    import { NextRequest, NextResponse } from 'next/server'

    export async function POST(request: NextRequest) {
      // ...and the body is still available in your route handler
      const body = await request.text()

      console.log('Body in route handler:', body.length)

      return NextResponse.json({ received: body.length })
    }
```

## Good to know[](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize#good-to-know)

  * 이 설정은 애플리케이션에서 프록시를 사용할 때만 적용됩니다.
  * 10MB 기본 한도는 메모리 사용량과 일반적인 사용 사례 사이의 균형을 맞추기 위해 설계되었습니다.
  * 이 한도는 모든 동시 요청에 대해 전역이 아니라 요청별로 적용됩니다.
  * 대용량 파일 업로드를 처리하는 애플리케이션이라면 필요에 따라 한도를 높이세요.

supported.

Send
