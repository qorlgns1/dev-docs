---
title: "SvelteKit에 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면 먼저 새 SvelteKit 프로젝트를 생성하세요. 가장 일반적인 방법은 SvelteKit 문서에 설명되어 있습니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/sveltekit

# SvelteKit에 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 프로젝트가 없다면 먼저 새 SvelteKit 프로젝트를 생성하세요. 가장 일반적인 방법은 [SvelteKit](https://svelte.dev/docs/kit/creating-a-project) 문서에 설명되어 있습니다.

터미널

```
    npx sv create my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/vite`와 해당 peer dependencies를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/vite
```

03

#### Vite 플러그인 구성하기

Vite 설정에 `@tailwindcss/vite` 플러그인을 추가하세요.

vite.config.ts

```
    import { sveltekit } from '@sveltejs/kit/vite';import { defineConfig } from 'vite';import tailwindcss from '@tailwindcss/vite';export default defineConfig({  plugins: [    tailwindcss(),    sveltekit(),  ],});
```

04

#### Tailwind CSS 가져오기

`./src/app.css` 파일을 생성하고 Tailwind CSS를 가져오는 `@import`를 추가하세요.

app.css

```
    @import "tailwindcss";
```

05

#### CSS 파일 가져오기

`./src/routes/+layout.svelte` 파일을 생성하고 새로 만든 `app.css` 파일을 가져오세요.

+layout.svelte

```
    <script>  let { children } = $props();  import "../app.css";</script>{@render children()}
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

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요. Tailwind로 처리해야 하는 `<style>` 블록이 있다면 Tailwind CSS 테마를 반드시 가져오세요.

+page.svelte

```
    <h1 class="text-3xl font-bold underline">  Hello world!</h1><style lang="postcss">  @reference "tailwindcss";  :global(html) {    background-color: theme(--color-gray-100);  }</style>
```
