---
title: "Rspack으로 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면 새 Rspack 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 Rspack CLI를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/rspack/vue

# Rspack으로 Tailwind CSS 설치 - Tailwind CSS

- ## [React 사용](https://tailwindcss.com/docs/installation/framework-guides/rspack/react)
  - ## [Vue 사용](https://tailwindcss.com/docs/installation/framework-guides/rspack/vue)

01

#### 프로젝트 만들기

아직 설정된 프로젝트가 없다면 새 Rspack 프로젝트를 먼저 만드세요. 가장 일반적인 방법은 [Rspack CLI](https://rspack.dev/guide/start/quick-start#using-the-rspack-cli)를 사용하는 것입니다.

터미널

```
    npm create rspack@latest
```

02

#### Tailwind CSS 설치

`@tailwindcss/postcss`와 해당 peer dependencies를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

03

#### PostCSS 지원 활성화

`rspack.config.js` 파일에서 PostCSS 로더를 활성화하세요. 자세한 내용은 [문서](https://rspack.dev/guide/tech/css#tailwind-css)를 참고하세요.

rspack.config.ts

```
    export default defineConfig({  // ...  module: {    rules: [      {        test: /\.css$/,        use: ["postcss-loader"],        type: "css",      },      // ...    ],  },}
```

04

#### PostCSS 플러그인 구성

프로젝트 루트에 `postcss.config.mjs` 파일을 만들고, PostCSS 구성에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  },};
```

05

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./src/style.css`에 `@import`를 추가하세요.

style.css

```
    @import "tailwindcss";
```

06

#### 빌드 프로세스 시작

`npm run dev`로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

07

#### 프로젝트에서 Tailwind 사용 시작

Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

App.vue

```
    <template>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></template>
```
