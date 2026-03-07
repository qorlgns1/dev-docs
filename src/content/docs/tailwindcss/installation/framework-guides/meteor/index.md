---
title: "Meteor로 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 프로젝트가 없다면 새 Meteor 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 Meteor CLI를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/meteor

# Meteor로 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 프로젝트가 없다면 새 Meteor 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 [Meteor CLI](https://docs.meteor.com/about/install.html)를 사용하는 것입니다.

Terminal

```
    npx meteor create my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/postcss`와 해당 peer dependency를 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss postcss postcss-load-config
```

03

#### PostCSS 플러그인 설정하기

프로젝트 루트에 `postcss.config.mjs` 파일을 만들고, PostCSS 설정에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  },};
```

04

#### Tailwind CSS 가져오기

`./client/main.css` 파일에 Tailwind CSS용 `@import`를 추가하세요.

main.css

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작하기

`npm run start`로 빌드 프로세스를 실행하세요.

Terminal

```
    npm run start
```

06

#### 프로젝트에서 Tailwind 사용 시작하기

Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

App.jsx

```
    export const App = () => (  <h1 className="text-3xl font-bold underline">    Hello world!  </h1>)
```
