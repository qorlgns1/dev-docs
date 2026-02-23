---
title: '가이드: PostCSS'
description: 'Next.js는 내장 CSS 지원을 위해 CSS를 PostCSS로 컴파일합니다.'
---

# 가이드: PostCSS | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/post-css

# Next.js에서 PostCSS를 구성하는 방법

마지막 업데이트: 2026년 2월 20일

## 기본 동작[](https://nextjs.org/docs/pages/guides/post-css#default-behavior)

Next.js는 [내장 CSS 지원](https://nextjs.org/docs/app/getting-started/css)을 위해 CSS를 PostCSS로 컴파일합니다.

별도 설정 없이도 Next.js는 다음과 같은 변환으로 CSS를 컴파일합니다.

  * [Autoprefixer](https://github.com/postcss/autoprefixer)는 CSS 규칙에 벤더 프리픽스를 자동으로 추가합니다(IE11까지 지원).
  * [브라우저 간 Flexbox 버그](https://github.com/philipwalton/flexbugs)를 수정하여 [명세](https://www.w3.org/TR/css-flexbox-1/)와 동일하게 동작하도록 합니다.
  * 새로운 CSS 기능을 Internet Explorer 11과 호환되도록 자동으로 컴파일합니다.
    * [`all` 속성](https://developer.mozilla.org/docs/Web/CSS/all)
    * [Break 속성](https://developer.mozilla.org/docs/Web/CSS/break-after)
    * [`font-variant` 속성](https://developer.mozilla.org/docs/Web/CSS/font-variant)
    * [Gap 속성](https://developer.mozilla.org/docs/Web/CSS/gap)
    * [미디어 쿼리 범위](https://developer.mozilla.org/docs/Web/CSS/Media_Queries/Using_media_queries#Syntax_improvements_in_Level_4)

기본적으로 [CSS Grid](https://www.w3.org/TR/css-grid-1/)와 [사용자 정의 속성](https://developer.mozilla.org/docs/Web/CSS/var)(CSS 변수)은 IE11 지원을 위해 **컴파일되지 않습니다**.

[CSS Grid Layout](https://developer.mozilla.org/docs/Web/CSS/grid)을 IE11용으로 컴파일하려면 CSS 파일 상단에 다음 주석을 추가하세요.
[code]
    /* autoprefixer grid: autoplace */
[/code]

프로젝트 전체에서 [CSS Grid Layout](https://developer.mozilla.org/docs/Web/CSS/grid)에 IE11 지원을 적용하려면 아래(접힌) 구성으로 autoprefixer를 설정할 수 있습니다. 자세한 내용은 아래 ["플러그인 사용자 정의"](https://nextjs.org/docs/pages/guides/post-css#customizing-plugins)를 참조하세요.

CSS Grid Layout을 활성화하는 구성을 보려면 클릭하세요

postcss.config.json
[code]
    {
      "plugins": [
        "postcss-flexbugs-fixes",
        [
          "postcss-preset-env",
          {
            "autoprefixer": {
              "flexbox": "no-2009",
              "grid": "autoplace"
            },
            "stage": 3,
            "features": {
              "custom-properties": false
            }
          }
        ]
      ]
    }
[/code]

CSS 변수는 [안전하게 컴파일할 수 없기 때문](https://github.com/MadLittleMods/postcss-css-variables#caveats)에 컴파일되지 않습니다. 변수를 반드시 사용해야 한다면 [Sass](https://sass-lang.com/)가 컴파일해 제거하는 [Sass 변수](https://sass-lang.com/documentation/variables) 같은 대안을 고려하세요.

## 대상 브라우저 사용자 정의[](https://nextjs.org/docs/pages/guides/post-css#customizing-target-browsers)

Next.js는 [Browserslist](https://github.com/browserslist/browserslist)를 통해 ( [Autoprefixer](https://github.com/postcss/autoprefixer)와 컴파일되는 CSS 기능에 대한) 대상 브라우저를 설정할 수 있게 해줍니다.

browserslist를 사용자 정의하려면 `package.json`에 `browserslist` 키를 다음과 같이 추가하세요.

package.json
[code]
    {
      "browserslist": [">0.3%", "not dead", "not op_mini all"]
    }
[/code]

[browsersl.ist](https://browsersl.ist/?q=%3E0.3%25%2C+not+ie+11%2C+not+dead%2C+not+op_mini+all) 도구를 사용하면 타깃팅 중인 브라우저를 시각화할 수 있습니다.

## CSS 모듈[](https://nextjs.org/docs/pages/guides/post-css#css-modules)

CSS 모듈을 지원하는 데 별도 설정이 필요하지 않습니다. 파일 확장을 `.module.css`로 바꾸면 해당 파일에 CSS 모듈이 활성화됩니다.

[Next.js의 CSS 모듈 지원](https://nextjs.org/docs/app/getting-started/css)에 대해 더 알아보세요.

## 플러그인 사용자 정의[](https://nextjs.org/docs/pages/guides/post-css#customizing-plugins)

> **경고** : 사용자 지정 PostCSS 구성 파일을 정의하면 Next.js는 [기본 동작](https://nextjs.org/docs/pages/guides/post-css#default-behavior)을 **완전히 비활성화**합니다. [Autoprefixer](https://github.com/postcss/autoprefixer)를 포함해 필요한 기능을 모두 직접 설정해야 합니다. 또한 사용자 지정 구성에 포함된 플러그인은 `npm install postcss-flexbugs-fixes postcss-preset-env`처럼 수동으로 설치해야 합니다.

PostCSS 구성을 사용자 정의하려면 프로젝트 루트에 `postcss.config.json` 파일을 만드세요.

다음은 Next.js가 사용하는 기본 구성입니다.

postcss.config.json
[code]
    {
      "plugins": [
        "postcss-flexbugs-fixes",
        [
          "postcss-preset-env",
          {
            "autoprefixer": {
              "flexbox": "no-2009"
            },
            "stage": 3,
            "features": {
              "custom-properties": false
            }
          }
        ]
      ]
    }
[/code]

> **알아두면 좋아요** : Next.js는 이 파일을 `.postcssrc.json`으로 이름 붙이거나, `package.json`의 `postcss` 키에서 읽을 수도 있습니다.

환경에 따라 플러그인을 조건부로 포함하고 싶을 때 유용한 `postcss.config.js` 파일로 PostCSS를 설정하는 것도 가능합니다.

postcss.config.js
[code]
    module.exports = {
      plugins:
        process.env.NODE_ENV === 'production'
          ? [
              'postcss-flexbugs-fixes',
              [
                'postcss-preset-env',
                {
                  autoprefixer: {
                    flexbox: 'no-2009',
                  },
                  stage: 3,
                  features: {
                    'custom-properties': false,
                  },
                },
              ],
            ]
          : [
              // No transformations in development
            ],
    }
[/code]

> **알아두면 좋아요** : Next.js는 이 파일을 `.postcssrc.js`로 이름 붙이는 것도 허용합니다.

PostCSS 플러그인을 가져올 때는 **`require()`를 사용하지 마세요**. 플러그인은 문자열로 제공해야 합니다.

> **알아두면 좋아요** : 동일한 프로젝트에서 `postcss.config.js`가 다른 비-Next.js 도구도 지원해야 한다면, 다음과 같이 상호 운용 가능한 객체 기반 형식을 사용해야 합니다.
[code]
>     module.exports = {
>       plugins: {
>         'postcss-flexbugs-fixes': {},
>         'postcss-preset-env': {
>           autoprefixer: {
>             flexbox: 'no-2009',
>           },
>           stage: 3,
>           features: {
>             'custom-properties': false,
>           },
>         },
>       },
>     }
[/code]

보내기
