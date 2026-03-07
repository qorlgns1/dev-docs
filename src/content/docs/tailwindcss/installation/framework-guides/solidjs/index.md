---
title: "SolidJS와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면 먼저 새 SolidJS 프로젝트를 생성하세요. 가장 일반적인 방법은 SolidJS Vite 템플릿을 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/solidjs

# SolidJS와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 생성

아직 설정된 프로젝트가 없다면 먼저 새 SolidJS 프로젝트를 생성하세요. 가장 일반적인 방법은 [SolidJS Vite 템플릿](https://www.solidjs.com/guides/getting-started)을 사용하는 것입니다.

터미널

```
    npx degit solidjs/templates/js my-projectcd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/vite`와 해당 peer dependencies를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { defineConfig } from 'vite';import solidPlugin from 'vite-plugin-solid';import tailwindcss from '@tailwindcss/vite';export default defineConfig({  plugins: [    tailwindcss(),    solidPlugin(),  ],  server: {    port: 3000,  },  build: {    target: 'esnext',  },});
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./src/index.css`에 `@import`를 추가하세요.

index.css

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

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

App.jsx

```
    export default function App() {  return (    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  )}
```
