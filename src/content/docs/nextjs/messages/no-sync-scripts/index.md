---
title: '동기 스크립트 없음'
description: '동기 스크립트를 사용하면 웹페이지 성능에 영향을 줄 수 있습니다.'
---

# 동기 스크립트 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-sync-scripts

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)동기 스크립트 없음

# 동기 스크립트 없음

> 동기 스크립트를 방지하세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-sync-scripts#why-this-error-occurred)

동기 스크립트를 사용하면 웹페이지 성능에 영향을 줄 수 있습니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/no-sync-scripts#possible-ways-to-fix-it)

### Script 컴포넌트(권장)[](https://nextjs.org/docs/messages/no-sync-scripts#script-component-recommended)

pages/index.js
[code]
    import Script from 'next/script'
     
    function Home() {
      return (
        <div class="container">
          <Script src="https://third-party-script.js"></Script>
          <div>Home Page</div>
        </div>
      )
    }
     
    export default Home
[/code]

### `async` 또는 `defer` 사용[](https://nextjs.org/docs/messages/no-sync-scripts#use-async-or-defer)
[code] 
    <script src="https://third-party-script.js" async />
    <script src="https://third-party-script.js" defer />
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/no-sync-scripts#useful-links)

  * [타사 JavaScript를 효율적으로 로드하기](https://web.dev/efficiently-load-third-party-javascript/)



도움이 되셨나요?

지원됨.

전송
