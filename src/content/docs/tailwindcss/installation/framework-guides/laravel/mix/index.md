---
title: "Laravel에서 Tailwind CSS 설치 - Tailwind CSS"
description: "webpack.mix.js 파일에서 tailwindcss를 PostCSS 플러그인으로 추가하세요."
---

# Laravel에서 Tailwind CSS 설치 - Tailwind CSS

- ## [Vite 사용하기](https://tailwindcss.com/docs/installation/framework-guides/laravel/vite)
  - ## [Laravel Mix 사용하기](https://tailwindcss.com/docs/installation/framework-guides/laravel/mix)

01

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/postcss`와 해당 peer dependencies를 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss postcss
```

02

#### Laravel Mix 설정에 Tailwind 추가

`webpack.mix.js` 파일에서 `tailwindcss`를 PostCSS 플러그인으로 추가하세요.

webpack.mix.js

```
    mix  .js("resources/js/app.js", "public/js")  .postCss("resources/css/app.css", "public/css", [    require("@tailwindcss/postcss"),  ]);
```

03

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./resources/css/app.css`에 `@import`를 추가하세요. 또한 Tailwind CSS가 유틸리티를 위해 일부 디렉터리를 스캔하도록 설정하세요.

app.css

```
    @import "tailwindcss";@source "../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php";@source "../../storage/framework/views/*.php";@source "../**/*.blade.php";@source "../**/*.js";
```

04

#### 빌드 프로세스 시작

`npm run watch`로 빌드 프로세스를 실행하세요.

Terminal

```
    npm run watch
```

05

#### 프로젝트에서 Tailwind 사용 시작

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 다음, Tailwind의 유틸리티 클래스를 사용해 콘텐츠를 스타일링하세요.

app.blade.php

```
    <!doctype html><html>  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <link href="{{ asset('css/app.css') }}" rel="stylesheet" />  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
