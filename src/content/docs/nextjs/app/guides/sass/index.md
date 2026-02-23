---
title: '가이드: Sass'
description: 'Next.js는 패키지를 설치한 뒤 와  확장자를 모두 활용하여 Sass와 통합할 수 있도록 기본 지원합니다. CSS Modules와  또는  확장자를 사용하면 컴포넌트 수준의 Sass를 사용할 수 있습니다.'
---

# 가이드: Sass | Next.js

출처 URL: https://nextjs.org/docs/app/guides/sass

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Sass

Copy page

# Sass를 사용하는 방법

최종 업데이트 2026년 2월 20일

Next.js는 패키지를 설치한 뒤 `.scss`와 `.sass` 확장자를 모두 활용하여 Sass와 통합할 수 있도록 기본 지원합니다. CSS Modules와 `.module.scss` 또는 `.module.sass` 확장자를 사용하면 컴포넌트 수준의 Sass를 사용할 수 있습니다.

먼저 [`sass`](https://github.com/sass/sass)를 설치하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add -D sass
[/code]

> **알아 두면 좋아요** :
> 
> Sass는 확장자가 다른 [두 가지 문법](https://sass-lang.com/documentation/syntax)을 지원합니다. `.scss` 확장자는 [SCSS 문법](https://sass-lang.com/documentation/syntax#scss)을 요구하고, `.sass` 확장자는 [들여쓰기 문법("Sass")](https://sass-lang.com/documentation/syntax#the-indented-syntax)을 요구합니다.
> 
> 어떤 것을 선택할지 확신이 없다면, CSS의 상위 집합이면서 들여쓰기 문법("Sass")을 새로 배울 필요가 없는 `.scss` 확장자부터 시작하세요.

### Sass 옵션 사용자 정의[](https://nextjs.org/docs/app/guides/sass#customizing-sass-options)

Sass 옵션을 구성하려면 `next.config`에서 `sassOptions`를 사용하세요.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      sassOptions: {
        additionalData: `$var: red;`,
      },
    }
     
    export default nextConfig
[/code]

#### 구현[](https://nextjs.org/docs/app/guides/sass#implementation)

사용할 Sass 구현체를 지정하려면 `implementation` 속성을 사용할 수 있습니다. 기본적으로 Next.js는 [`sass`](https://www.npmjs.com/package/sass) 패키지를 사용합니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      sassOptions: {
        implementation: 'sass-embedded',
      },
    }
     
    export default nextConfig
[/code]

### Sass 변수[](https://nextjs.org/docs/app/guides/sass#sass-variables)

Next.js는 CSS Module 파일에서 export된 Sass 변수를 지원합니다.

예를 들어 export된 `primaryColor` Sass 변수를 사용하는 방법은 다음과 같습니다.

app/variables.module.scss
[code]
    $primary-color: #64ff00;
     
    :export {
      primaryColor: $primary-color;
    }
[/code]

app/page.js
[code]
    // maps to root `/` URL
     
    import variables from './variables.module.scss'
     
    export default function Page() {
      return <h1 style={{ color: variables.primaryColor }}>Hello, Next.js!</h1>
    }
[/code]

도움이 되었나요?

지원됨.

전송
