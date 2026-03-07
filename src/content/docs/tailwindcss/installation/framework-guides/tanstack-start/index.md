---
title: "TanStack Start와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면, 먼저 새로운 TanStack Start 프로젝트를 생성하세요. 가장 일반적인 방법은 Create Start App을 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/tanstack-start

# TanStack Start와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 생성

아직 설정된 프로젝트가 없다면, 먼저 새로운 TanStack Start 프로젝트를 생성하세요. 가장 일반적인 방법은 [Create Start App](https://tanstack.com/start/latest/docs/framework/react/overview)을 사용하는 것입니다.

터미널

```
    npx create-start-app@latest my-projectcd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/vite`와 해당 피어 의존성을 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 설정

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { tanstackStart } from '@tanstack/react-start/plugin/vite';import { defineConfig } from 'vite';import tsConfigPaths from 'vite-tsconfig-paths';import tailwindcss from '@tailwindcss/vite'export default defineConfig({  plugins: [    tailwindcss()    tanstackStart(),    tsConfigPaths(),  ]});
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./src/styles.css`에 `@import`를 추가하세요.

src/styles.css

```
    @import "tailwindcss";
```

05

#### 루트 라우트에서 CSS 파일 가져오기

`?url` 쿼리와 함께 `__root.tsx` 파일에서 CSS 파일을 가져오세요.

src/routes/\_\_root.tsx

```
    // other imports...import appCss from '../styles.css?url'export const Route = createRootRoute({  head: () => ({    meta: [      // your meta tags and site config    ],    links: [{ rel: 'stylesheet', href: appCss }],    // other head config  }),  component: RootComponent,})
```

06

#### 프로젝트에서 Tailwind 사용 시작하기

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

src/routes/index.tsx

```
    import { createFileRoute } from '@tanstack/react-router'export const Route = createFileRoute('/')({  component: App,})function App() {  return (    <h1 class="text-3xl font-bold underline">      Hello World!    </h1>  )}
```
