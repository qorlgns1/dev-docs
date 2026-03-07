---
title: "Nuxt에 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면, 먼저 새 Nuxt 프로젝트를 생성하세요. 가장 일반적인 방법은 Create Nuxt를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/nuxt

# Nuxt에 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 만들기

아직 설정된 프로젝트가 없다면, 먼저 새 Nuxt 프로젝트를 생성하세요. 가장 일반적인 방법은 [Create Nuxt](https://nuxt.com/docs/4.x/getting-started/installation#new-project)를 사용하는 것입니다.

터미널

```
    npm create nuxt my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/vite`와 해당 피어 의존성을 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성하기

Nuxt 설정에 `@tailwindcss/vite` 플러그인을 Vite 플러그인으로 추가하세요.

nuxt.config.ts

```
    import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({  compatibilityDate: "2025-07-15",  devtools: { enabled: true },  vite: {    plugins: [      tailwindcss(),    ],  },});
```

04

#### Tailwind CSS 가져오기

`./app/assets/css/main.css` 파일을 만들고 Tailwind CSS를 가져오는 `@import`를 추가하세요.

main.css

```
    @import "tailwindcss";
```

05

#### CSS 파일을 전역으로 추가하기

새로 만든 `./app/assets/css/main.css`를 `nuxt.config.ts` 파일의 `css` 배열에 추가하세요.

nuxt.config.ts

```
    import tailwindcss from "@tailwindcss/vite";export default defineNuxtConfig({  compatibilityDate: "2025-07-15",  devtools: { enabled: true },  css: ['./app/assets/css/main.css'],  vite: {    plugins: [      tailwindcss(),    ],  },});
```

06

#### 빌드 프로세스 시작하기

`npm run dev`로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

07

#### 프로젝트에서 Tailwind 사용 시작하기

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

app.vue

```
    <template>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></template>
```
