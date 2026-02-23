---
title: '파일 시스템 규칙: src'
description: '프로젝트 루트에 특수한 Next.js  또는  디렉터리를 두는 대신, Next.js는 애플리케이션 코드를  폴더 아래에 두는 일반적인 패턴도 지원합니다.'
---

# 파일 시스템 규칙: src | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/src-folder

Copy page

# src 폴더

2026년 2월 20일 업데이트

프로젝트 루트에 특수한 Next.js `app` 또는 `pages` 디렉터리를 두는 대신, Next.js는 애플리케이션 코드를 `src` 폴더 아래에 두는 일반적인 패턴도 지원합니다.

이렇게 하면 프로젝트의 루트에 위치하는 구성 파일과 애플리케이션 코드를 분리할 수 있어, 일부 개인과 팀이 선호합니다.

`src` 폴더를 사용하려면 `app` Router 폴더 또는 `pages` Router 폴더를 각각 `src/app` 또는 `src/pages`로 이동하세요.

> **알아 두면 좋아요** :
>
>   * `/public` 디렉터리는 프로젝트 루트에 그대로 두어야 합니다.
>   * `package.json`, `next.config.js`, `tsconfig.json`과 같은 구성 파일은 프로젝트 루트에 유지해야 합니다.
>   * `.env.*` 파일은 프로젝트 루트에 유지해야 합니다.
>   * 루트 디렉터리에 `app` 또는 `pages`가 있으면 `src/app` 또는 `src/pages`는 무시됩니다.
>   * `src`를 사용한다면 `/components`나 `/lib` 같은 다른 애플리케이션 폴더도 함께 옮기는 경우가 많습니다.
>   * Proxy를 사용 중이라면 반드시 `src` 폴더 안에 배치하세요.
>   * Tailwind CSS를 사용한다면 [content section](https://tailwindcss.com/docs/content-configuration)의 `tailwind.config.js` 파일에 `/src` 접두사를 추가해야 합니다.
>   * `@/*`처럼 TypeScript 경로를 사용한다면 `tsconfig.json`의 `paths` 객체에 `src/`를 포함하도록 업데이트해야 합니다.
>

##

- [프로젝트 구조](https://nextjs.org/docs/app/getting-started/project-structure)
  - Next.js의 폴더 및 파일 규칙과 프로젝트 구성 방법을 알아보세요.

supported.

Send