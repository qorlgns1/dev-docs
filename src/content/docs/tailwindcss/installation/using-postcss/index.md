---
title: "PostCSS로 Tailwind CSS 설치하기 - Tailwind CSS"
description: "PostCSS 플러그인으로 Tailwind CSS를 설치하는 방법은 Next.js나 Angular 같은 프레임워크와 가장 매끄럽게 통합할 수 있는 방식입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/using-postcss

# PostCSS로 Tailwind CSS 설치하기 - Tailwind CSS

## 설치

- ## [Vite 사용하기](https://tailwindcss.com/docs/installation/using-vite)
- ## [PostCSS 사용하기](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [프레임워크 가이드](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### PostCSS 플러그인으로 Tailwind CSS 설치하기

PostCSS 플러그인으로 Tailwind CSS를 설치하는 방법은 Next.js나 Angular 같은 프레임워크와 가장 매끄럽게 통합할 수 있는 방식입니다.

01

#### Tailwind CSS 설치하기

npm을 통해 `tailwindcss`, `@tailwindcss/postcss`, `postcss`를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/postcss postcss
```

02

#### PostCSS 설정에 Tailwind 추가하기

`postcss.config.mjs` 파일(또는 프로젝트에서 PostCSS를 설정한 위치)에 `@tailwindcss/postcss`를 추가하세요.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  }}
```

03

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 CSS 파일에 `@import`를 추가하세요.

CSS

```
    @import "tailwindcss";
```

04

#### 빌드 프로세스 시작하기

`npm run dev` 또는 `package.json` 파일에 설정된 명령어로 빌드 프로세스를 실행하세요.

터미널

```
    npm run dev
```

05

#### HTML에서 Tailwind 사용 시작하기

컴파일된 CSS가 `<head>`에 포함되어 있는지 확인한 뒤 _(프레임워크가 이를 자동으로 처리할 수도 있습니다)_ , Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

HTML

```
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="/dist/styles.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```

**막히셨나요?** PostCSS와 함께 Tailwind를 설정하는 방법은 빌드 도구마다 조금씩 다를 수 있습니다. 현재 사용 중인 환경에 맞는 더 구체적인 안내가 있는지 프레임워크 가이드를 확인해 보세요.

[프레임워크 가이드 살펴보기](https://tailwindcss.com/docs/installation/framework-guides)
