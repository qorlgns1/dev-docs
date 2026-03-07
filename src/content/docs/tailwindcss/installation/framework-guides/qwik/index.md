---
title: "Qwik과 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 프로젝트가 없다면 먼저 새로운 Qwik 프로젝트를 만드세요. 가장 일반적인 방법은 Create Qwik을 사용하는 것입니다."
---

# Qwik과 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 만들기

아직 프로젝트가 없다면 먼저 새로운 Qwik 프로젝트를 만드세요. 가장 일반적인 방법은 [Create Qwik](https://qwik.dev/docs/getting-started/#create-an-app-using-the-cli)을 사용하는 것입니다.

터미널

```
    npm create qwik@latest empty my-projectcd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/vite`와 해당 피어 의존성을 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { defineConfig } from 'vite'import { qwikVite } from "@builder.io/qwik/optimizer";import { qwikCity } from "@builder.io/qwik-city/vite";// …import tailwindcss from '@tailwindcss/vite'export default defineConfig(({ command, mode }): UserConfig => {  return {    plugins: [      tailwindcss(),      qwikCity(),      qwikVite(),      tsconfigPaths(),    ],    // …  }})
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./src/global.css`에 `@import`를 추가하세요.

global.css

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작

`npm run dev`로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

06

#### 프로젝트에서 Tailwind 사용 시작

Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

index.tsx

```
    import { component$ } from '@builder.io/qwik'export default component$(() => {  return (    <h1 class="text-3xl font-bold underline">      Hello World!    </h1>  )})
```
