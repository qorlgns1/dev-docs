---
title: "Next.js와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면 먼저 새 Next.js 프로젝트를 만드세요. 가장 일반적인 방법은 Create Next App을 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/nextjs

# Next.js와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 생성

아직 설정된 프로젝트가 없다면 먼저 새 Next.js 프로젝트를 만드세요. 가장 일반적인 방법은 [Create Next App](https://nextjs.org/docs/api-reference/create-next-app)을 사용하는 것입니다.

터미널

```
    npx create-next-app@latest my-project --typescript --eslint --appcd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/postcss`와 해당 peer dependency를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/postcss postcss
```

03

#### PostCSS 플러그인 구성

프로젝트 루트에 `postcss.config.mjs` 파일을 만들고, PostCSS 구성에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.mjs

```
    const config = {  plugins: {    "@tailwindcss/postcss": {},  },};export default config;
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./app/globals.css`에 `@import`를 추가하세요.

globals.css

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

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

page.tsx

```
    export default function Home() {  return (    <h1 className="text-3xl font-bold underline">      Hello world!    </h1>  )}
```
