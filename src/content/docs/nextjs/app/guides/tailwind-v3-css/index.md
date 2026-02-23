---
title: '가이드: Tailwind CSS v3'
description: '마지막 업데이트 2026년 2월 20일'
---

# 가이드: Tailwind CSS v3 | Next.js

Source URL: https://nextjs.org/docs/app/guides/tailwind-v3-css

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)Tailwind CSS v3

페이지 복사

# Next.js 애플리케이션에 Tailwind CSS v3를 설치하는 방법

마지막 업데이트 2026년 2월 20일

이 가이드는 Next.js 애플리케이션에 [Tailwind CSS v3](https://v3.tailwindcss.com/)를 설치하는 방법을 단계별로 설명합니다.

> **참고:** 최신 Tailwind 4 설정은 [Tailwind CSS 설정 안내서](https://nextjs.org/docs/app/getting-started/css#tailwind-css)를 참고하세요.

## Tailwind v3 설치[](https://nextjs.org/docs/app/guides/tailwind-v3-css#installing-tailwind-v3)

Tailwind CSS와 해당 피어 의존성을 설치한 뒤, `init` 명령을 실행하여 `tailwind.config.js`와 `postcss.config.js` 파일을 생성합니다:

pnpmnpmyarnbun

터미널
[code]
    pnpm add -D tailwindcss@^3 postcss autoprefixer
    npx tailwindcss init -p
[/code]

## Tailwind v3 구성[](https://nextjs.org/docs/app/guides/tailwind-v3-css#configuring-tailwind-v3)

`tailwind.config.js` 파일에서 템플릿 경로를 설정합니다:

tailwind.config.js
[code]
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './app/**/*.{js,ts,jsx,tsx,mdx}',
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
[/code]

글로벌 CSS 파일에 Tailwind 지시문을 추가합니다:

app/globals.css
[code]
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
[/code]

루트 레이아웃에서 해당 CSS 파일을 가져옵니다:

app/layout.tsx

JavaScriptTypeScript
[code]
    import './globals.css'
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      return (
        <html lang="en">
          <body>{children}</body>
        </html>
      )
    }
[/code]

## 클래스 사용하기[](https://nextjs.org/docs/app/guides/tailwind-v3-css#using-classes)

Tailwind CSS를 설치하고 글로벌 스타일을 추가한 후에는 애플리케이션에서 Tailwind 유틸리티 클래스를 사용할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
    }
[/code]

## Turbopack과 함께 사용하기[](https://nextjs.org/docs/app/guides/tailwind-v3-css#usage-with-turbopack)

Next.js 13.1부터 Tailwind CSS와 PostCSS는 [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css)에서 지원됩니다.

도움이 되었나요?

지원됨.

보내기
