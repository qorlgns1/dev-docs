---
title: "AdonisJS와 함께 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면, 먼저 새 AdonisJS 프로젝트를 생성하세요. 가장 일반적인 방법은 Create AdonisJS를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/adonisjs

# AdonisJS와 함께 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 프로젝트가 없다면, 먼저 새 AdonisJS 프로젝트를 생성하세요. 가장 일반적인 방법은 [Create AdonisJS](https://docs.adonisjs.com/guides/getting-started/installation)를 사용하는 것입니다.

Terminal

```
    npm init adonisjs@latest my-project -- --kit=webcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/vite`와 해당 피어 의존성을 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성하기

Vite 구성에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { defineConfig } from 'vite'import adonisjs from '@adonisjs/vite/client'import tailwindcss from '@tailwindcss/vite'export default defineConfig({  plugins: [    tailwindcss(),    adonisjs({      // …    }),  ],})
```

04

#### Tailwind CSS 가져오기

Tailwind CSS 스타일을 가져오도록 `./resources/css/app.css`에 `@import`를 추가하세요. 또한 유틸리티 클래스를 찾을 수 있도록 `resources/views` 디렉터리를 스캔하라고 Tailwind CSS에 알려주세요.

app.css

```
    @import "tailwindcss";@source "../views";
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

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 다음, Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

home.edge

```
    <!doctype html><html>  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    @vite(['resources/css/app.css', 'resources/js/app.js'])  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
