---
title: 'next.config.js Options: urlImports'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 직접 사용해 보고 GitHub에 피드백을 남겨 주세요.'
---

# next.config.js Options: urlImports | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports

[구성](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)urlImports

Copy page

# urlImports

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 직접 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에 피드백을 남겨 주세요.

Last updated February 20, 2026

URL Imports는 로컬 디스크가 아닌 외부 서버에서 모듈을 직접 가져올 수 있게 해 주는 실험적 기능입니다.

> **경고** : 신뢰할 수 있는 도메인에서만 다운로드 및 실행하세요. 기능이 안정화될 때까지는 신중하게 판단해 주시기 바랍니다.

이 기능을 사용하려면 `next.config.js`에 허용할 URL 접두사를 추가하세요:

next.config.js
[code]
    module.exports = {
      experimental: {
        urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
      },
    }
[/code]

그런 다음 URL에서 모듈을 직접 가져올 수 있습니다:
[code] 
    import { a, b, c } from 'https://example.com/assets/some/module.js'
[/code]

URL Imports는 일반 패키지 import가 허용되는 모든 곳에서 사용할 수 있습니다.

## Security Model[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#security-model)

이 기능은 **보안을 최우선**으로 두고 설계되고 있습니다. 먼저 실험용 플래그를 도입해 URL Imports를 허용할 도메인을 명시적으로 등록하도록 했습니다. 이어서 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)을 사용해 브라우저 샌드박스 내에서만 URL Imports가 실행되도록 제한하는 방향으로 작업 중입니다.

## Lockfile[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#lockfile)

URL Imports를 사용하면 Next.js가 lockfile과 가져온 에셋을 포함하는 `next.lock` 디렉터리를 생성합니다. 이 디렉터리는 `.gitignore`로 제외하지 말고 **반드시 Git에 커밋해야 합니다**.

  * `next dev`를 실행하면 Next.js가 새로 발견한 모든 URL Imports를 다운로드해 lockfile에 추가합니다.
  * `next build`를 실행하면 Next.js는 프로덕션 빌드를 위해 lockfile만 사용합니다.



일반적으로 네트워크 요청이 필요 없으며, lockfile이 오래되면 빌드가 실패합니다. 예외적으로 `Cache-Control: no-cache`로 응답하는 리소스는 lockfile에 `no-cache` 항목으로 표시되며 매 빌드마다 네트워크에서 다시 가져옵니다.

## Examples[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#examples)

### Skypack[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#skypack)
[code] 
    import confetti from 'https://cdn.skypack.dev/canvas-confetti'
    import { useEffect } from 'react'
     
    export default () => {
      useEffect(() => {
        confetti()
      })
      return <p>Hello</p>
    }
[/code]

### Static Image Imports[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#static-image-imports)
[code] 
    import Image from 'next/image'
    import logo from 'https://example.com/assets/logo.png'
     
    export default () => (
      <div>
        <Image src={logo} placeholder="blur" />
      </div>
    )
[/code]

### URLs in CSS[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#urls-in-css)
[code] 
    .className {
      background: url('https://example.com/assets/hero.jpg');
    }
[/code]

### Asset Imports[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#asset-imports)
[code] 
    const logo = new URL('https://example.com/assets/file.txt', import.meta.url)
     
    console.log(logo.pathname)
     
    // prints "/_next/static/media/file.a9727b5d.txt"
[/code]

Was this helpful?

supported.

Send
