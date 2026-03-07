---
title: "Vite로 Tailwind CSS 설치하기 - Tailwind CSS"
description: "Vite 플러그인으로 Tailwind CSS를 설치하는 것은 Laravel, SvelteKit, React Router, Nuxt, SolidJS 같은 프레임워크와 가장 매끄럽게 통합하는 방법입니다."
---

출처 URL: https://tailwindcss.com/docs/installation

# Vite로 Tailwind CSS 설치하기 - Tailwind CSS

## 설치

- ## [Vite 사용](https://tailwindcss.com/docs/installation/using-vite)
- ## [PostCSS 사용](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [프레임워크 가이드](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Vite 플러그인으로 Tailwind CSS 설치하기

Vite 플러그인으로 Tailwind CSS를 설치하는 것은 Laravel, SvelteKit, React Router, Nuxt, SolidJS 같은 프레임워크와 가장 매끄럽게 통합하는 방법입니다.

01

#### 프로젝트 생성

아직 프로젝트가 없다면 먼저 새 Vite 프로젝트를 만드세요. 가장 일반적인 방법은 [Create Vite](https://vite.dev/guide/#scaffolding-your-first-vite-project)를 사용하는 것입니다.

터미널

```
    npm create vite@latest my-projectcd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `tailwindcss`와 `@tailwindcss/vite`를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { defineConfig } from 'vite'import tailwindcss from '@tailwindcss/vite'export default defineConfig({  plugins: [    tailwindcss(),  ],})
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 불러오도록 CSS 파일에 `@import`를 추가하세요.

CSS

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작

`npm run dev` 또는 `package.json` 파일에 설정된 명령어로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

06

#### HTML에서 Tailwind 사용 시작

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 뒤 _(프레임워크가 이 과정을 대신 처리할 수도 있습니다)_ Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

HTML

```
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/src/style.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

**막히셨나요?** Vite와 함께 Tailwind를 설정하는 방식은 빌드 도구마다 조금씩 다를 수 있습니다. 현재 구성에 더 맞는 구체적인 안내가 있는지 프레임워크 가이드를 확인해 보세요.

[프레임워크 가이드 살펴보기](https://tailwindcss.com/docs/installation/framework-guides)
