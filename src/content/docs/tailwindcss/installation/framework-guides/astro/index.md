---
title: "Astro와 함께 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 Astro 프로젝트가 없다면 새 Astro 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 create astro를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/astro

# Astro와 함께 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 Astro 프로젝트가 없다면 새 Astro 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 [create astro](https://docs.astro.build/en/install-and-setup/#install-from-the-cli-wizard)를 사용하는 것입니다.

터미널

```
    npm create astro@latest my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/vite`와 해당 peer dependency를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성하기

Astro 설정 파일의 Vite 플러그인에 `@tailwindcss/vite` 플러그인을 추가하세요.

astro.config.mjs

```
    // @ts-checkimport { defineConfig } from "astro/config";import tailwindcss from "@tailwindcss/vite";// https://astro.build/configexport default defineConfig({  vite: {    plugins: [tailwindcss()],  },});
```

04

#### Tailwind CSS 가져오기

`./src/styles/global.css` 파일을 만들고 Tailwind CSS를 위한 `@import`를 추가하세요.

global.css

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작하기

`npm run dev`로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

06

#### 프로젝트에서 Tailwind 사용 시작하기

새로 만든 CSS 파일을 import하는 것을 잊지 말고, Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

index.astro

```
    ---import "../styles/global.css";---<h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
