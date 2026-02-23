---
title: '파일 시스템 규칙: src 디렉터리'
description: '프로젝트 루트에 있는 Next.js의 특수  또는  디렉터리를 사용하는 대신, Next.js는 애플리케이션 코드를  폴더 아래에 배치하는 일반적인 패턴도 지원합니다.'
---

# 파일 시스템 규칙: src 디렉터리 | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder

[API Reference](https://nextjs.org/docs/pages/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/pages/api-reference/file-conventions)src 디렉터리

# src 디렉터리

마지막 업데이트 2026년 2월 20일

프로젝트 루트에 있는 Next.js의 특수 `app` 또는 `pages` 디렉터리를 사용하는 대신, Next.js는 애플리케이션 코드를 `src` 폴더 아래에 배치하는 일반적인 패턴도 지원합니다.

이렇게 하면 대부분 프로젝트 루트에 있는 구성 파일과 애플리케이션 코드가 분리되며, 일부 개인이나 팀은 이 구조를 선호합니다.

`src` 폴더를 사용하려면 `app` 라우터 폴더나 `pages` 라우터 폴더를 각각 `src/app` 또는 `src/pages`로 이동하세요.

> **알아두면 좋아요** :
>
>   * `/public` 디렉터리는 프로젝트 루트에 유지해야 합니다.
>   * `package.json`, `next.config.js`, `tsconfig.json` 같은 구성 파일은 프로젝트 루트에 유지해야 합니다.
>   * `.env.*` 파일은 프로젝트 루트에 유지해야 합니다.
>   * 루트 디렉터리에 `app` 또는 `pages`가 있으면 `src/app` 또는 `src/pages`는 무시됩니다.
>   * `src`를 사용한다면 `/components`나 `/lib` 같은 다른 애플리케이션 폴더도 이동하게 될 가능성이 큽니다.
>   * 프록시를 사용 중이라면 반드시 `src` 폴더 내부에 배치하세요.
>   * Tailwind CSS를 사용 중이면 [content 섹션](https://tailwindcss.com/docs/content-configuration)의 `tailwind.config.js` 파일에 `/src` 접두사를 추가해야 합니다.
>   * `@/*`처럼 TypeScript 경로로 import를 사용 중이면 `tsconfig.json`의 `paths` 객체에 `src/`를 포함하도록 업데이트하세요.
>

보내기