---
title: "Play CDN - Tailwind CSS"
description: "빌드 단계 없이 브라우저에서 바로 Tailwind를 사용해 보려면 Play CDN을 사용하세요. Play CDN은 개발 용도로만 설계되었으며, 프로덕션 용도로는 사용하도록 의도되지 않았습니다."
---

# Play CDN - Tailwind CSS

## 설치

- ## [Vite 사용하기](https://tailwindcss.com/docs/installation/using-vite)
- ## [PostCSS 사용하기](https://tailwindcss.com/docs/installation/using-postcss)
- ## [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)
- ## [프레임워크 가이드](https://tailwindcss.com/docs/installation/framework-guides)
- ## [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

### Play CDN 사용하기

빌드 단계 없이 브라우저에서 바로 Tailwind를 사용해 보려면 Play CDN을 사용하세요. Play CDN은 개발 용도로만 설계되었으며, 프로덕션 용도로는 사용하도록 의도되지 않았습니다.

01

#### HTML에 Play CDN 스크립트 추가하기

HTML 파일의 `<head>`에 Play CDN 스크립트 태그를 추가하고, Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```

02

#### 사용자 정의 CSS 추가해 보기

Tailwind의 모든 CSS 기능을 지원하는 사용자 정의 CSS를 추가하려면 `type="text/tailwindcss"`를 사용하세요.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>    <style type="text/tailwindcss">      @theme {        --color-clifford: #da373d;      }    </style>  </head>  <body>    <h1 class="text-3xl font-bold underline text-clifford">      Hello world!    </h1>  </body></html>
```
