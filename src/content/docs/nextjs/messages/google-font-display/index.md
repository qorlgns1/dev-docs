---
title: 'Google Font Display'
description: '> Google Fonts에서 font-display 동작을 강제합니다.'
---

# Google Font Display | Next.js

Source URL: https://nextjs.org/docs/messages/google-font-display

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Google Font Display

# Google Font Display

> Google Fonts에서 font-display 동작을 강제합니다.

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/google-font-display#why-this-error-occurred)

Google Font에서 font-display 디스크립터가 누락되었거나 `auto`, `block`, `fallback`으로 설정되어 있었는데, 이는 권장되지 않는 값입니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/google-font-display#possible-ways-to-fix-it)

대부분의 경우, 커스텀 폰트에 가장 적합한 font-display 전략은 `optional`입니다.

pages/index.js
[code]
    import Head from 'next/head'

    export default function IndexPage() {
      return (
        <div>
          <Head>
            <link
              href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
              rel="stylesheet"
            />
          </Head>
        </div>
      )
    }
[/code]

`display=optional`을 지정하면 보이지 않는 텍스트나 레이아웃 이동 위험을 최소화합니다. 폰트가 로드된 뒤 커스텀 폰트로 교체되는 것이 중요하다면 `display=swap`을 사용하세요.

### 사용하지 말아야 할 때[](https://nextjs.org/docs/messages/google-font-display#when-not-to-use-it)

`auto`, `block`, `fallback` 전략으로 폰트를 명시적으로 표시하려는 경우 이 규칙을 비활성화하면 됩니다.

## 유용한 링크[](https://nextjs.org/docs/messages/google-font-display#useful-links)

  * [font-display로 폰트 성능 제어하기](https://developer.chrome.com/blog/font-display/)
  * [Google Fonts API 문서](https://developers.google.com/fonts/docs/css2#use_font-display)
  * [CSS `font-display` 속성](https://www.w3.org/TR/css-fonts-4/#font-display-desc)

보내기
