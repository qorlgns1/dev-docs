---
title: 'next.config.js: browserDebugInfoInTerminal'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 직접 사용해 보고 GitHub에 의견을 공유해 주세요.'
---

# next.config.js: browserDebugInfoInTerminal | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal

# browserDebugInfoInTerminal

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 직접 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에 의견을 공유해 주세요.

최종 업데이트 2026년 2월 20일

`experimental.browserDebugInfoInTerminal` 옵션은 브라우저에서 발생한 console 출력과 런타임 오류를 개발 서버 터미널로 전달합니다.

이 옵션은 기본적으로 비활성화되어 있으며, 활성화하더라도 개발 모드에서만 동작합니다.

## 사용 방법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#usage)

포워딩을 활성화하세요:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: true,
      },
    }

    export default nextConfig
[/code]

### 직렬화 한계[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#serialization-limits)

깊이 중첩된 객체/배열은 **합리적인 기본값**으로 잘립니다. 다음 한계를 조정할 수 있습니다.

  * **depthLimit** : (선택 사항) 중첩 객체/배열의 문자열화 깊이 제한. 기본값: 5
  * **edgeLimit** : (선택 사항) 객체 또는 배열당 포함할 최대 프로퍼티/요소 수. 기본값: 100

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: {
          depthLimit: 5,
          edgeLimit: 100,
        },
      },
    }

    export default nextConfig
[/code]

### 소스 위치[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#source-location)

이 기능을 활성화하면 소스 위치가 기본적으로 포함됩니다.

app/page.tsx
[code]
    'use client'

    export default function Home() {
      return (
        <button
          type="button"
          onClick={() => {
            console.log('Hello World')
          }}
        >
          Click me
        </button>
      )
    }
[/code]

버튼을 클릭하면 이 메시지가 터미널에 출력됩니다.

터미널
[code]
    [browser] Hello World (app/page.tsx:8:17)
[/code]

이를 숨기려면 `showSourceLocation: false`로 설정하세요.

  * **showSourceLocation** : 가능할 때 소스 위치 정보를 포함합니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        browserDebugInfoInTerminal: {
          showSourceLocation: false,
        },
      },
    }

    export default nextConfig
[/code]

Version| Changes
---|---
`v15.4.0`| 실험적 `browserDebugInfoInTerminal` 도입

보내기
