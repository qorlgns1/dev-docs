---
title: "Parcel로 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면 새 Parcel 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 시작 가이드에 설명된 대로 프로젝트에 Parcel을 dev-dependency로 추가하는 것입니다."
---

# Parcel로 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 프로젝트가 없다면 새 Parcel 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 [시작 가이드](https://parceljs.org/getting-started/webapp/)에 설명된 대로 프로젝트에 Parcel을 dev-dependency로 추가하는 것입니다.

Terminal

```
    mkdir my-projectcd my-projectnpm init -ynpm install parcelmkdir srctouch src/index.html
```

02

#### Tailwind CSS 설치하기

npm을 통해 `@tailwindcss/postcss`와 해당 peer dependency를 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss
```

03

#### PostCSS 구성하기

프로젝트 루트에 `.postcssrc` 파일을 만들고 `@tailwindcss/postcss` 플러그인을 활성화하세요.

.postcssrc

```
    {  "plugins": {    "@tailwindcss/postcss": {}  }}
```

04

#### Tailwind CSS 가져오기

`./src/index.css` 파일을 만들고 Tailwind CSS를 위한 `@import`를 추가하세요.

index.css

```
    @import "tailwindcss";
```

05

#### 빌드 프로세스 시작하기

`npx parcel src/index.html`로 빌드 프로세스를 실행하세요.

Terminal

```
    npx parcel src/index.html
```

06

#### 프로젝트에서 Tailwind 사용 시작하기

CSS 파일을 `<head>`에 추가하고 Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <link href="./index.css" type="text/css" rel="stylesheet" />  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
