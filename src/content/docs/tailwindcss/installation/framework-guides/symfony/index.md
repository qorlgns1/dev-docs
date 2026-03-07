---
title: "Symfony와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 프로젝트를 설정하지 않았다면, 먼저 새 Symfony 프로젝트를 생성하세요. 가장 일반적인 방법은 Symfony Installer를 사용하는 것입니다."
---

# Symfony와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 프로젝트를 설정하지 않았다면, 먼저 새 Symfony 프로젝트를 생성하세요. 가장 일반적인 방법은 [Symfony Installer](https://symfony.com/download)를 사용하는 것입니다.

터미널

```
    symfony new --webapp my-projectcd my-project
```

02

#### Webpack Encore 설치하기

에셋 빌드를 담당하는 Webpack Encore를 설치하세요. 자세한 내용은 [문서](https://symfony.com/doc/current/frontend.html)를 참고하세요.

터미널

```
    composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundlecomposer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle
```

03

#### Tailwind CSS 설치하기

npm을 사용해 `@tailwindcss/postcss`와 해당 peer dependencies, 그리고 `postcss-loader`를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

04

#### PostCSS 지원 활성화하기

`webpack.config.js` 파일에서 PostCSS Loader를 활성화하세요. 자세한 내용은 [문서](https://symfony.com/doc/current/frontend/encore/postcss.html)를 참고하세요.

webpack.config.js

```
    Encore  .enablePostCssLoader();
```

05

#### PostCSS 플러그인 구성하기

프로젝트 루트에 `postcss.config.mjs` 파일을 생성하고, PostCSS 설정에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  },};
```

06

#### Tailwind CSS 가져오기

`./assets/styles/app.css`에 Tailwind CSS를 가져오는 `@import`를 추가하고, watch 모드에서 재컴파일 루프를 방지하기 위해 public 디렉터리를 무시하는 `@source`를 추가하세요.

app.css

```
    @import "tailwindcss";@source not "../../public";
```

07

#### 빌드 프로세스 시작하기

`npm run watch`로 빌드 프로세스를 실행하세요.

터미널

```
    npm run watch
```

08

#### 프로젝트에서 Tailwind 사용 시작하기

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 다음, Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

base.html.twig

```
    <!doctype html><html>  <head>    <meta charset="utf-8" />    <meta      name="viewport"      content="width=device-width, initial-scale=1.0"    />    {% block stylesheets %}      {{ encore_entry_link_tags('app') }}    {% endblock %}  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
