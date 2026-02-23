---
title: '시작하기: 프로젝트 구조'
description: '이 페이지는 Next.js의 모든 폴더 및 파일 규칙과 프로젝트 구성에 대한 권장 사항을 개괄합니다.'
---

# 시작하기: 프로젝트 구조 | Next.js

출처 URL: https://nextjs.org/docs/pages/getting-started/project-structure

[페이지 라우터](https://nextjs.org/docs/pages)[시작하기](https://nextjs.org/docs/pages/getting-started)프로젝트 구조

페이지 복사

# 프로젝트 구조와 구성

2026년 2월 20일 업데이트

이 페이지는 Next.js의 **모든** 폴더 및 파일 규칙과 프로젝트 구성에 대한 권장 사항을 개괄합니다.

## 폴더 및 파일 규칙[](https://nextjs.org/docs/pages/getting-started/project-structure#folder-and-file-conventions)

### 최상위 폴더[](https://nextjs.org/docs/pages/getting-started/project-structure#top-level-folders)

최상위 폴더는 애플리케이션 코드와 정적 자산을 구성하는 데 사용됩니다.

|   
---|---  
[`app`](https://nextjs.org/docs/app)| 앱 라우터  
[`pages`](https://nextjs.org/docs/pages/building-your-application/routing)| 페이지 라우터  
[`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)| 서비스할 정적 자산  
[`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)| 선택적 애플리케이션 소스 폴더  
  
### 최상위 파일[](https://nextjs.org/docs/pages/getting-started/project-structure#top-level-files)

최상위 파일은 애플리케이션 구성, 의존성 관리, 프록시 실행, 모니터링 도구 통합, 환경 변수 정의에 사용됩니다.

|   
---|---  
**Next.js**|   
[`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)| Next.js 구성 파일  
[`package.json`](https://nextjs.org/docs/app/getting-started/installation#manual-installation)| 프로젝트 의존성과 스크립트  
[`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation)| OpenTelemetry 및 계측 파일  
[`proxy.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)| Next.js 요청 프록시  
[`.env`](https://nextjs.org/docs/app/guides/environment-variables)| 환경 변수(버전 관리에 추적하면 안 됨)  
[`.env.local`](https://nextjs.org/docs/app/guides/environment-variables)| 로컬 환경 변수(버전 관리에 추적하면 안 됨)  
[`.env.production`](https://nextjs.org/docs/app/guides/environment-variables)| 프로덕션 환경 변수(버전 관리에 추적하면 안 됨)  
[`.env.development`](https://nextjs.org/docs/app/guides/environment-variables)| 개발 환경 변수(버전 관리에 추적하면 안 됨)  
[`eslint.config.mjs`](https://nextjs.org/docs/app/api-reference/config/eslint)| ESLint 구성 파일  
`.gitignore`| 무시할 Git 파일 및 폴더  
[`next-env.d.ts`](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts)| Next.js용 TypeScript 선언 파일(버전 관리에 추적하면 안 됨)  
`tsconfig.json`| TypeScript 구성 파일  
`jsconfig.json`| JavaScript 구성 파일  
  
### 파일 규칙[](https://nextjs.org/docs/pages/getting-started/project-structure#file-conventions)

| |   
---|---|---  
[`_app`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)| `.js` `.jsx` `.tsx`| 사용자 지정 App  
[`_document`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)| `.js` `.jsx` `.tsx`| 사용자 지정 Document  
[`_error`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#more-advanced-error-page-customizing)| `.js` `.jsx` `.tsx`| 사용자 지정 오류 페이지  
[`404`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)| `.js` `.jsx` `.tsx`| 404 오류 페이지  
[`500`](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page)| `.js` `.jsx` `.tsx`| 500 오류 페이지  
  
### 라우트[](https://nextjs.org/docs/pages/getting-started/project-structure#routes)

| |   
---|---|---  
**폴더 규칙**| |   
[`index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)| `.js` `.jsx` `.tsx`| 홈 페이지  
[`folder/index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)| `.js` `.jsx` `.tsx`| 중첩 페이지  
**파일 규칙**| |   
[`index`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#index-routes)| `.js` `.jsx` `.tsx`| 홈 페이지  
[`file`](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)| `.js` `.jsx` `.tsx`| 중첩 페이지  
  
### 동적 라우트[](https://nextjs.org/docs/pages/getting-started/project-structure#dynamic-routes-1)

| |   
---|---|---  
**폴더 규칙**| |   
[`[folder]/index`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)| `.js` `.jsx` `.tsx`| 동적 라우트 세그먼트  
[`[...folder]/index`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)| `.js` `.jsx` `.tsx`| 캐치올 라우트 세그먼트  
[`[[...folder]]/index`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)| `.js` `.jsx` `.tsx`| 선택적 캐치올 라우트 세그먼트  
**파일 규칙**| |   
[`[file]`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)| `.js` `.jsx` `.tsx`| 동적 라우트 세그먼트  
[`[...file]`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)| `.js` `.jsx` `.tsx`| 캐치올 라우트 세그먼트  
[`[[...file]]`](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)| `.js` `.jsx` `.tsx`| 선택적 캐치올 라우트 세그먼트  
  
도움이 되었나요?

지원됨.

전송
