---
title: 'Guides: CSS-in-JS'
description: '마지막 업데이트 2026년 2월 20일'
---

# Guides: CSS-in-JS | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/css-in-js

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)CSS-in-JS

페이지 복사

# CSS-in-JS 라이브러리를 사용하는 방법

마지막 업데이트 2026년 2월 20일

예제

  * [Styled JSX](https://github.com/vercel/next.js/tree/canary/examples/with-styled-jsx)
  * [Styled Components](https://github.com/vercel/next.js/tree/canary/examples/with-styled-components)
  * [Emotion](https://github.com/vercel/next.js/tree/canary/examples/with-emotion)
  * [Linaria](https://github.com/vercel/next.js/tree/canary/examples/with-linaria)
  * [Styletron](https://github.com/vercel/next.js/tree/canary/examples/with-styletron)
  * [Cxs](https://github.com/vercel/next.js/tree/canary/examples/with-cxs)
  * [Fela](https://github.com/vercel/next.js/tree/canary/examples/with-fela)
  * [Stitches](https://github.com/vercel/next.js/tree/canary/examples/with-stitches)



기존 CSS-in-JS 솔루션은 모두 사용할 수 있습니다. 가장 간단한 방법은 인라인 스타일입니다:
[code]
    function HiThere() {
      return <p style={{ color: 'red' }}>hi there</p>
    }
     
    export default HiThere
[/code]

우리는 [styled-jsx](https://github.com/vercel/styled-jsx)를 번들링해 격리된 범위의 CSS를 지원합니다. 목표는 Web Components와 유사한 "shadow CSS"를 지원하는 것이지만, 안타깝게도 [서버 렌더링을 지원하지 않고 JS 전용](https://github.com/w3c/webcomponents/issues/71)입니다.

Styled Components와 같은 다른 인기 있는 CSS-in-JS 솔루션은 위의 예제를 참고하세요.

`styled-jsx`를 사용하는 컴포넌트는 다음과 같습니다:
[code]
    function HelloWorld() {
      return (
        <div>
          Hello world
          <p>scoped!</p>
          <style jsx>{`
            p {
              color: blue;
            }
            div {
              background: red;
            }
            @media (max-width: 600px) {
              div {
                background: blue;
              }
            }
          `}</style>
          <style global jsx>{`
            body {
              background: black;
            }
          `}</style>
        </div>
      )
    }
     
    export default HelloWorld
[/code]

더 많은 예시는 [styled-jsx 문서](https://github.com/vercel/styled-jsx)를 참고하세요.

### JavaScript 비활성화[](https://nextjs.org/docs/pages/guides/css-in-js#disabling-javascript)

네. JavaScript를 비활성화해도 프로덕션 빌드(`next start`)에서는 CSS가 계속 로드됩니다. 개발 중에는 [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh)를 통한 최상의 개발자 경험을 제공하기 위해 JavaScript 활성화가 필요합니다.

도움이 되었나요?

지원됨.

전송
