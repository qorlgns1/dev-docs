---
title: "Angular로 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 프로젝트가 준비되어 있지 않다면 먼저 새 Angular 프로젝트를 생성하세요. 가장 일반적인 방법은 Angular CLI를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/angular

# Angular로 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성

아직 프로젝트가 준비되어 있지 않다면 먼저 새 Angular 프로젝트를 생성하세요. 가장 일반적인 방법은 [Angular CLI](https://angular.dev/tools/cli/setup-local)를 사용하는 것입니다.

터미널

```
    ng new my-project --style csscd my-project
```

02

#### Tailwind CSS 설치

npm을 통해 `@tailwindcss/postcss`와 해당 peer dependencies를 설치하세요.

터미널

```
    npm install tailwindcss @tailwindcss/postcss postcss --force
```

03

#### PostCSS 플러그인 구성

프로젝트 루트에 `.postcssrc.json` 파일을 만들고, PostCSS 설정에 `@tailwindcss/postcss` 플러그인을 추가하세요.

.postcssrc.json

```
    {  "plugins": {    "@tailwindcss/postcss": {}  }}
```

04

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./src/styles.css`에 `@import`를 추가하세요.

styles.css

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작

`ng serve`로 빌드 프로세스를 실행하세요.

터미널

```
    ng serve
```

06

#### 프로젝트에서 Tailwind 사용 시작

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

app.component.html

```
    <h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
