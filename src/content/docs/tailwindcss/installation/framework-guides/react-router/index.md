---
title: "React Router와 함께 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 React Router 프로젝트가 없다면 새 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 Create React Router를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/react-router

# React Router와 함께 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 React Router 프로젝트가 없다면 새 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 [Create React Router](https://reactrouter.com/start/framework/installation)를 사용하는 것입니다.

터미널

```
    npx create-react-router@latest my-projectcd my-project
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

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { reactRouter } from "@react-router/dev/vite";import { defineConfig } from "vite";import tsconfigPaths from "vite-tsconfig-paths";import tailwindcss from "@tailwindcss/vite";export default defineConfig({  plugins: [    tailwindcss(),    reactRouter(),    tsconfigPaths(),  ],});
```

04

#### Tailwind CSS 가져오기

`./app/app.css`에 Tailwind CSS를 가져오는 `@import`를 추가하세요.

app.css

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

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

home.tsx

```
    export default function Home() {  return (    <h1 className="text-3xl font-bold underline">      Hello world!    </h1>  )}
```
