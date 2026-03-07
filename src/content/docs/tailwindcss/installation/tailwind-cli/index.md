---
title: "Tailwind CLI - Tailwind CSS"
description: "처음부터 Tailwind CSS를 빠르게 시작하는 가장 간단하고 빠른 방법은 Tailwind CLI 도구를 사용하는 것입니다. Node.js를 설치하지 않고 사용하고 싶다면 CLI를 독립 실행 파일로도 사용할 수 있습니다."
---

출처 URL: https://tailwindcss.com/docs/installation/tailwind-cli

# Tailwind CLI - Tailwind CSS

## 설치

- ## [Vite 사용](https://tailwindcss.com/docs/installation/using-vite)
- ## [PostCSS 사용](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [프레임워크 가이드](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Tailwind CLI 설치하기

처음부터 Tailwind CSS를 빠르게 시작하는 가장 간단하고 빠른 방법은 Tailwind CLI 도구를 사용하는 것입니다. Node.js를 설치하지 않고 사용하고 싶다면 CLI를 [독립 실행 파일](https://github.com/tailwindlabs/tailwindcss/releases/latest)로도 사용할 수 있습니다.

01

#### Tailwind CSS 설치

npm을 통해 `tailwindcss`와 `@tailwindcss/cli`를 설치합니다.

터미널

```
    npm install tailwindcss @tailwindcss/cli
```

02

#### CSS에서 Tailwind 가져오기

메인 CSS 파일에 `@import "tailwindcss";` 가져오기를 추가합니다.

src/input.css

```
    @import "tailwindcss";
```

03

#### Tailwind CLI 빌드 프로세스 시작

CLI 도구를 실행해 소스 파일에서 클래스를 스캔하고 CSS를 빌드합니다.

터미널

```
    npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

04

#### HTML에서 Tailwind 사용 시작

컴파일된 CSS 파일을 `<head>`에 추가한 다음 Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용하세요.

src/index.html

```
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="./output.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>
```
