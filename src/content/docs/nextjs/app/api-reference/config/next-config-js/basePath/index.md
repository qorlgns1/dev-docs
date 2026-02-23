---
title: 'next.config.js: basePath'
description: '소스 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath'
---

# next.config.js: basePath | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)basePath

페이지 복사

# basePath

마지막 업데이트 2026년 2월 20일

Next.js 애플리케이션을 도메인의 하위 경로에 배포하려면 `basePath` 구성 옵션을 사용할 수 있습니다.

`basePath`를 사용하면 애플리케이션에 대한 경로 접두사를 설정할 수 있습니다. 예를 들어 기본값인 `''` 대신 `/docs`를 쓰려면 `next.config.js`를 열고 `basePath` 구성을 추가하세요:

next.config.js
[code]
    module.exports = {
      basePath: '/docs',
    }
[/code]

> **알아두면 좋아요** : 이 값은 빌드 시점에 설정해야 하며 클라이언트 측 번들에 인라인되므로 다시 빌드하지 않으면 변경할 수 없습니다.

### 링크[](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath#links)

`next/link`와 `next/router`로 다른 페이지에 링크할 때는 `basePath`가 자동으로 적용됩니다.

예를 들어 `/about`을 사용하면 `basePath`가 `/docs`로 설정돼 있을 때 자동으로 `/docs/about`으로 변환됩니다.
[code] 
    export default function HomePage() {
      return (
        <>
          <Link href="/about">About Page</Link>
        </>
      )
    }
[/code]

출력 HTML:
[code] 
    <a href="/docs/about">About Page</a>
[/code]

이 덕분에 `basePath` 값을 변경할 때 애플리케이션의 모든 링크를 일일이 수정할 필요가 없습니다.

### 이미지[](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath#images)

[`next/image`](https://nextjs.org/docs/app/api-reference/components/image) 컴포넌트를 사용할 때는 `src` 앞에 `basePath`를 추가해야 합니다.

예를 들어 `/docs/me.png`를 사용하면 `basePath`가 `/docs`로 설정된 상태에서 이미지를 올바르게 제공할 수 있습니다.
[code] 
    import Image from 'next/image'
     
    function Home() {
      return (
        <>
          <h1>My Homepage</h1>
          <Image
            src="/docs/me.png"
            alt="Picture of the author"
            width={500}
            height={500}
          />
          <p>Welcome to my homepage!</p>
        </>
      )
    }
     
    export default Home
[/code]

도움이 되었나요?

지원됨.

전송
