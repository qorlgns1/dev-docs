---
title: '가이드: Babel'
description: 'Next.js는 React 애플리케이션과 서버 측 코드를 컴파일하는 데 필요한 모든 항목을 포함한  프리셋을 앱에 기본 제공합니다. 그러나 기본 Babel 구성을 확장하고 싶다면 그렇게 할 수도 있습니다.'
---

# 가이드: Babel | Next.js

Source URL: https://nextjs.org/docs/pages/guides/babel

# Next.js에서 Babel 구성 방법

최종 업데이트 2026년 2월 20일

예시

  * [Babel 구성 사용자 지정](https://github.com/vercel/next.js/tree/canary/examples/with-custom-babel-config)

Next.js는 React 애플리케이션과 서버 측 코드를 컴파일하는 데 필요한 모든 항목을 포함한 `next/babel` 프리셋을 앱에 기본 제공합니다. 그러나 기본 Babel 구성을 확장하고 싶다면 그렇게 할 수도 있습니다.

## 프리셋과 플러그인 추가[](https://nextjs.org/docs/pages/guides/babel#adding-presets-and-plugins)

시작하려면 프로젝트 루트 디렉터리에 `.babelrc` 파일(또는 `babel.config.js`)만 정의하면 됩니다. 해당 파일이 발견되면 _단일 진실 공급원_ 으로 간주되므로, Next.js가 필요로 하는 `next/babel` 프리셋도 정의해야 합니다.

다음은 예시 `.babelrc` 파일입니다:

.babelrc
```
    {
      "presets": ["next/babel"],
      "plugins": []
    }
```

`next/babel`이 포함하는 프리셋을 배우려면 [이 파일을 확인](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/babel/preset.ts)해 보세요.

프리셋/플러그인을 **추가 구성 없이** 넣으려면 다음과 같이 하면 됩니다:

.babelrc
```
    {
      "presets": ["next/babel"],
      "plugins": ["@babel/plugin-proposal-do-expressions"]
    }
```

## 프리셋과 플러그인 사용자 지정[](https://nextjs.org/docs/pages/guides/babel#customizing-presets-and-plugins)

프리셋/플러그인을 **사용자 지정 구성과 함께** 추가하려면 `next/babel` 프리셋에 다음과 같이 설정하세요:

.babelrc
```
    {
      "presets": [
        [
          "next/babel",
          {
            "preset-env": {},
            "transform-runtime": {},
            "styled-jsx": {},
            "class-properties": {}
          }
        ]
      ],
      "plugins": []
    }
```

각 구성에서 사용 가능한 옵션을 더 알아보려면 babel [문서](https://babeljs.io/docs/) 사이트를 방문하세요.

> **알아두면 좋은 점** :
>
>   * Next.js는 서버 측 컴파일에 [**현재** Node.js 버전](https://github.com/nodejs/release#release-schedule)을 사용합니다.
>   * `"preset-env"`의 `modules` 옵션은 `false`로 유지해야 하며, 그렇지 않으면 webpack 코드 분할이 비활성화됩니다.
>