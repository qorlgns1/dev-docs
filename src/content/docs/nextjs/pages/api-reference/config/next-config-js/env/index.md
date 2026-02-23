---
title: 'next.config.js 옵션: env'
description: '> Next.js 9.4 릴리스 이후로 환경 변수를 추가하는 경험이 더욱 직관적이고 편리해졌습니다. 직접 사용해 보세요!'
---

# next.config.js 옵션: env | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/env

Copy page

# env

마지막 업데이트: 2026년 2월 20일

> [Next.js 9.4](https://nextjs.org/blog/next-9-4) 릴리스 이후로 [환경 변수를 추가](https://nextjs.org/docs/pages/guides/environment-variables)하는 경험이 더욱 직관적이고 편리해졌습니다. 직접 사용해 보세요!

> **알아 두면 좋은 점**: 이 방식으로 지정한 환경 변수는 **항상** JavaScript 번들에 포함됩니다. 환경 변수 이름 앞에 `NEXT_PUBLIC_` 접두사를 붙이는 것은 [환경이나 .env 파일을 통해 지정](https://nextjs.org/docs/pages/guides/environment-variables)할 때만 효과가 있습니다.

JavaScript 번들에 환경 변수를 추가하려면 `next.config.js`를 열고 `env` 구성을 추가합니다:

next.config.js
[code]
    module.exports = {
      env: {
        customKey: 'my-value',
      },
    }
[/code]

이제 코드에서 `process.env.customKey`에 접근할 수 있습니다. 예를 들어:
[code]
    function Page() {
      return <h1>The value of customKey is: {process.env.customKey}</h1>
    }

    export default Page
[/code]

Next.js는 빌드 시점에 `process.env.customKey`를 `'my-value'`로 대체합니다. webpack [DefinePlugin](https://webpack.js.org/plugins/define-plugin/)의 특성상 `process.env` 변수를 구조 분해하려고 하면 동작하지 않습니다.

예를 들어, 다음과 같은 줄은:
[code]
    return <h1>The value of customKey is: {process.env.customKey}</h1>
[/code]

다음과 같이 바뀝니다:
[code]
    return <h1>The value of customKey is: {'my-value'}</h1>
[/code]

supported.

Send
