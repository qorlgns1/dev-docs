---
title: "Laravel에 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 Laravel 프로젝트가 없다면 새 Laravel 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 Laravel installer를 사용하는 것입니다."
---

# Laravel에 Tailwind CSS 설치하기 - Tailwind CSS

- ## [Vite 사용](https://tailwindcss.com/docs/installation/framework-guides/laravel/vite)
  - ## [Laravel Mix 사용](https://tailwindcss.com/docs/installation/framework-guides/laravel/mix)

01

#### 프로젝트 생성하기

아직 설정된 Laravel 프로젝트가 없다면 새 Laravel 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 [Laravel installer](https://laravel.com/docs#creating-an-application)를 사용하는 것입니다.

Terminal

```
    laravel new my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/vite`와 해당 peer dependencies를 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite Plugin 구성하기

Vite 설정에 `@tailwindcss/vite` plugin을 추가하세요.

vite.config.ts

```
    import { defineConfig } from 'vite'import tailwindcss from '@tailwindcss/vite'export default defineConfig({  plugins: [    tailwindcss(),    // …  ],})
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./resources/css/app.css`에 `@import`를 추가하세요. 또한 Tailwind CSS가 유틸리티 클래스를 위해 일부 디렉터리를 스캔하도록 설정하세요.

app.css

```
    @import "tailwindcss";@source "../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php";@source "../../storage/framework/views/*.php";@source "../**/*.blade.php";@source "../**/*.js";
```

05

#### 빌드 프로세스 시작하기

`npm run dev`로 빌드 프로세스를 실행하세요.

Terminal

```
    npm run dev
```

06

#### 프로젝트에서 Tailwind 사용 시작하기

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 다음, Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

app.blade.php

```
    <!doctype html><html>  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    @vite('resources/css/app.css')  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
