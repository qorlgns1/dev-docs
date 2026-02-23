---
title: 'next.config.js: urlImports'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서 사용하는 것은 권장되지 않습니다. 사용해 보고 GitHub에 피드백을 공유해 주세요.'
---

# next.config.js: urlImports | Next.js
출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports

# urlImports

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서 사용하는 것은 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에 피드백을 공유해 주세요.

최종 업데이트 2026년 2월 20일

URL import는 외부 서버(로컬 디스크 대신)에서 모듈을 직접 import할 수 있는 실험적 기능입니다.

> **경고** : 신뢰할 수 있는 도메인에서만 다운로드하여 로컬에서 실행하세요. 기능이 안정화되기 전까지는 주의 깊게 판단하고 사용해 주세요.

사용하려면 `next.config.js` 안에 허용할 URL 접두사를 추가하세요:

next.config.js
```
    module.exports = {
      experimental: {
        urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
      },
    }
```

그다음, URL에서 직접 모듈을 import할 수 있습니다:
```
    import { a, b, c } from 'https://example.com/assets/some/module.js'
```

URL import는 일반 패키지 import를 사용할 수 있는 모든 곳에서 사용할 수 있습니다.

## 보안 모델[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#security-model)

이 기능은 **보안을 최우선**으로 두고 설계되고 있습니다. 우선적으로, URL import를 허용할 도메인을 명시적으로 지정하도록 강제하는 실험 플래그를 추가했습니다. 이어서 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)을 사용해 URL import 실행을 브라우저 샌드박스로 제한하는 방향으로 확장하고 있습니다.

## Lockfile[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#lockfile)

URL import를 사용할 때 Next.js는 lockfile과 가져온 자산이 들어 있는 `next.lock` 디렉터리를 생성합니다. 이 디렉터리는 `.gitignore`로 무시하지 말고 **Git에 커밋해야 합니다**.

  * `next dev`를 실행하면 Next.js가 새로 발견된 모든 URL import를 다운로드하여 lockfile에 추가합니다.
  * `next build`를 실행하면 Next.js는 lockfile만 사용해 프로덕션용 애플리케이션을 빌드합니다.

일반적으로 네트워크 요청은 필요 없으며, lockfile이 오래되면 빌드가 실패합니다. 예외는 `Cache-Control: no-cache`로 응답하는 리소스입니다. 이러한 리소스는 lockfile에 `no-cache` 항목으로 기록되며, 빌드할 때마다 네트워크에서 항상 다시 가져옵니다.

## 예시[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#examples)

### Skypack[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#skypack)
```
    import confetti from 'https://cdn.skypack.dev/canvas-confetti'
    import { useEffect } from 'react'

    export default () => {
      useEffect(() => {
        confetti()
      })
      return <p>Hello</p>
    }
```

### 정적 이미지 import[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#static-image-imports)
```
    import Image from 'next/image'
    import logo from 'https://example.com/assets/logo.png'

    export default () => (
      <div>
        <Image src={logo} placeholder="blur" />
      </div>
    )
```

### CSS의 URL[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#urls-in-css)
```
    .className {
      background: url('https://example.com/assets/hero.jpg');
    }
```

### 자산 import[](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports#asset-imports)
```
    const logo = new URL('https://example.com/assets/file.txt', import.meta.url)

    console.log(logo.pathname)

    // prints "/_next/static/media/file.a9727b5d.txt"
```

보내기