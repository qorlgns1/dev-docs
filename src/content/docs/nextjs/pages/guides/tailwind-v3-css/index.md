---
title: '가이드: Tailwind CSS'
description: '이 가이드는 Next.js 애플리케이션에 Tailwind CSS v3를 설치하는 방법을 안내합니다.'
---

# 가이드: Tailwind CSS | Next.js

Source URL: https://nextjs.org/docs/pages/guides/tailwind-v3-css

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Tailwind CSS

Copy page

# Tailwind CSS

Last updated February 20, 2026

이 가이드는 Next.js 애플리케이션에 [Tailwind CSS v3](https://v3.tailwindcss.com/)를 설치하는 방법을 안내합니다.

> **알아두면 좋아요:** 최신 Tailwind 4 설정은 [Tailwind CSS 설정 안내](https://nextjs.org/docs/app/getting-started/css#tailwind-css)를 참고하세요.

## Installing Tailwind v3[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#installing-tailwind-v3)

Tailwind CSS와 피어 의존성을 설치한 뒤 `init` 명령을 실행하여 `tailwind.config.js`와 `postcss.config.js` 파일을 생성하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D tailwindcss@^3 postcss autoprefixer
    npx tailwindcss init -p
[/code]

## Configuring Tailwind v3[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#configuring-tailwind-v3)

`tailwind.config.js` 파일에서 템플릿 경로를 설정하세요:

tailwind.config.js
[code]
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
[/code]

전역 CSS 파일에 Tailwind 지시문을 추가하세요:

styles/globals.css
[code]
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
[/code]

`pages/_app.js` 파일에서 CSS 파일을 가져오세요:

pages/_app.js
[code]
    import '@/styles/globals.css'

    export default function MyApp({ Component, pageProps }) {
      return <Component {...pageProps} />
    }
[/code]

## Using classes[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#using-classes)

Tailwind CSS 설치와 전역 스타일 추가를 마치면 애플리케이션에서 Tailwind 유틸리티 클래스를 사용할 수 있습니다.

pages/index.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
    }
[/code]

## Usage with Turbopack[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#usage-with-turbopack)

Next.js 13.1부터 Tailwind CSS와 PostCSS는 [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css)에서 지원됩니다.

Was this helpful?

supported.

Send
