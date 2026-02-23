---
title: '시작하기: 프로젝트 구조'
description: '이 페이지는 Next.js의 모든 폴더와 파일 규칙, 그리고 프로젝트 구성에 대한 권장 사항을 개괄합니다.'
---

# 시작하기: 프로젝트 구조 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/project-structure

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Project Structure

Copy page

# 프로젝트 구조 및 구성

마지막 업데이트: 2026년 2월 20일

이 페이지는 Next.js의 **모든** 폴더와 파일 규칙, 그리고 프로젝트 구성에 대한 권장 사항을 개괄합니다.

## 폴더 및 파일 규칙[](https://nextjs.org/docs/app/getting-started/project-structure#folder-and-file-conventions)

### 최상위 폴더[](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders)

최상위 폴더는 애플리케이션 코드와 정적 자산을 구성하는 데 사용됩니다.

|
---|---
[`app`](https://nextjs.org/docs/app)| App Router
[`pages`](https://nextjs.org/docs/pages/building-your-application/routing)| Pages Router
[`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)| 제공할 정적 자산
[`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)| 선택적 애플리케이션 소스 폴더

### 최상위 파일[](https://nextjs.org/docs/app/getting-started/project-structure#top-level-files)

최상위 파일은 애플리케이션을 구성하고, 의존성을 관리하고, 프록시를 실행하고, 모니터링 도구를 통합하고, 환경 변수를 정의하는 데 사용됩니다.

|
---|---
**Next.js**|
[`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)| Next.js 구성 파일
[`package.json`](https://nextjs.org/docs/app/getting-started/installation#manual-installation)| 프로젝트 의존성과 스크립트
[`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation)| OpenTelemetry 및 Instrumentation 파일
[`proxy.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)| Next.js 요청 프록시
[`.env`](https://nextjs.org/docs/app/guides/environment-variables)| 환경 변수(버전 관리에서 제외)
[`.env.local`](https://nextjs.org/docs/app/guides/environment-variables)| 로컬 환경 변수(버전 관리에서 제외)
[`.env.production`](https://nextjs.org/docs/app/guides/environment-variables)| 프로덕션 환경 변수(버전 관리에서 제외)
[`.env.development`](https://nextjs.org/docs/app/guides/environment-variables)| 개발 환경 변수(버전 관리에서 제외)
[`eslint.config.mjs`](https://nextjs.org/docs/app/api-reference/config/eslint)| ESLint 구성 파일
`.gitignore`| 무시할 Git 파일 및 폴더
[`next-env.d.ts`](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts)| Next.js용 TypeScript 선언 파일(버전 관리에서 제외)
`tsconfig.json`| TypeScript 구성 파일
`jsconfig.json`| JavaScript 구성 파일

### 라우팅 파일[](https://nextjs.org/docs/app/getting-started/project-structure#routing-files)

`page`는 라우트를 노출하고, `layout`은 헤더·내비·푸터 같은 공유 UI, `loading`은 스켈레톤, `error`는 에러 바운더리, `route`는 API에 사용합니다.

| |
---|---|---
[`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout)| `.js` `.jsx` `.tsx`| Layout
[`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page)| `.js` `.jsx` `.tsx`| Page
[`loading`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)| `.js` `.jsx` `.tsx`| Loading UI
[`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)| `.js` `.jsx` `.tsx`| Not found UI
[`error`](https://nextjs.org/docs/app/api-reference/file-conventions/error)| `.js` `.jsx` `.tsx`| Error UI
[`global-error`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error)| `.js` `.jsx` `.tsx`| Global error UI
[`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route)| `.js` `.ts`| API endpoint
[`template`](https://nextjs.org/docs/app/api-reference/file-conventions/template)| `.js` `.jsx` `.tsx`| 재렌더링되는 layout
[`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default)| `.js` `.jsx` `.tsx`| Parallel route fallback page

### 중첩 라우트[](https://nextjs.org/docs/app/getting-started/project-structure#nested-routes)

폴더가 URL 세그먼트를 정의하며, 폴더를 중첩하면 세그먼트도 중첩됩니다. 어느 수준의 layout이든 자식 세그먼트를 감싸며, `page` 또는 `route` 파일이 존재하면 그 라우트가 공개됩니다.

Path| URL 패턴| 비고
---|---|---
`app/layout.tsx`| —| 루트 layout이 모든 라우트를 감쌉니다
`app/blog/layout.tsx`| —| `/blog`와 하위를 감쌉니다
`app/page.tsx`| `/`| 공개 라우트
`app/blog/page.tsx`| `/blog`| 공개 라우트
`app/blog/authors/page.tsx`| `/blog/authors`| 공개 라우트

### 동적 라우트[](https://nextjs.org/docs/app/getting-started/project-structure#dynamic-routes)

대괄호로 세그먼트를 파라미터화합니다. 단일 파라미터는 `[segment]`, 전체 포착은 `[...segment]`, 선택적 전체 포착은 `[[...segment]]`를 사용합니다. 값은 [`params`](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional) prop으로 접근합니다.

Path| URL 패턴
---|---
`app/blog/[slug]/page.tsx`| `/blog/my-first-post`
`app/shop/[...slug]/page.tsx`| `/shop/clothing`, `/shop/clothing/shirts`
`app/docs/[[...slug]]/page.tsx`| `/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router`

### 라우트 그룹과 프라이빗 폴더[](https://nextjs.org/docs/app/getting-started/project-structure#route-groups-and-private-folders)

[`(group)`](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#convention) 라우트 그룹으로 URL을 변경하지 않고 코드를 구성하고, [`_folder`](https://nextjs.org/docs/app/getting-started/project-structure#private-folders) 프라이빗 폴더로 라우팅되지 않는 파일을 같은 위치에 둘 수 있습니다.

Path| URL 패턴| 비고
---|---|---
`app/(marketing)/page.tsx`| `/`| 그룹이 URL에서 생략됩니다
`app/(shop)/cart/page.tsx`| `/cart`| `(shop)` 내부에서 layout 공유
`app/blog/_components/Post.tsx`| —| 라우팅되지 않음; UI 유틸 저장
`app/blog/_lib/data.ts`| —| 라우팅되지 않음; 유틸 저장

### Parallel 및 Intercepted Routes[](https://nextjs.org/docs/app/getting-started/project-structure#parallel-and-intercepted-routes)

이 기능은 슬롯 기반 layout이나 모달 라우팅처럼 특정 UI 패턴에 적합합니다.

부모 layout이 렌더링하는 이름 있는 슬롯에는 `@slot`을 사용합니다. URL을 변경하지 않고 현재 layout 안에서 다른 라우트를 렌더링하려면 intercept 패턴을 사용합니다. 예: 목록 위에 상세 모달을 표시.

패턴(문서)| 의미| 일반 사례
---|---|---
[`@folder`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots)| 이름 있는 슬롯| 사이드바 + 메인 콘텐츠
[`(.)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)| 동일 레벨 intercept| 형제 라우트를 모달로 미리 보기
[`(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)| 부모 intercept| 부모의 자식을 오버레이로 열기
[`(..)(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)| 두 레벨 intercept| 깊은 중첩 오버레이
[`(...)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)| 루트에서 intercept| 임의 라우트를 현재 뷰에 표시

### 메타데이터 파일 규칙[](https://nextjs.org/docs/app/getting-started/project-structure#metadata-file-conventions)

#### App 아이콘[](https://nextjs.org/docs/app/getting-started/project-structure#app-icons)

| |
---|---|---
[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)| `.ico`| 파비콘 파일
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)| `.ico` `.jpg` `.jpeg` `.png` `.svg`| 앱 아이콘 파일
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)| `.js` `.ts` `.tsx`| 코드로 생성한 앱 아이콘
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)| `.jpg` `.jpeg`, `.png`| Apple 앱 아이콘 파일
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)| `.js` `.ts` `.tsx`| 코드로 생성한 Apple 앱 아이콘

#### Open Graph 및 Twitter 이미지[](https://nextjs.org/docs/app/getting-started/project-structure#open-graph-and-twitter-images)

| |
---|---|---
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)| `.jpg` `.jpeg` `.png` `.gif`| Open Graph 이미지 파일
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)| `.js` `.ts` `.tsx`| 코드로 생성한 Open Graph 이미지
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)| `.jpg` `.jpeg` `.png` `.gif`| Twitter 이미지 파일
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)| `.js` `.ts` `.tsx`| 코드로 생성한 Twitter 이미지

#### SEO[](https://nextjs.org/docs/app/getting-started/project-structure#seo)

| |
---|---|---
[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml)| `.xml`| 사이트맵 파일
[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts)| `.js` `.ts`| 코드로 생성한 사이트맵
[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)| `.txt`| Robots 파일
[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)| `.js` `.ts`| 코드로 생성한 Robots 파일

## 프로젝트 구성[](https://nextjs.org/docs/app/getting-started/project-structure#organizing-your-project)

Next.js는 프로젝트 파일을 어떻게 구성하고 같은 위치에 둘지에 대해 **의견을 강제하지 않지만**, 프로젝트 구성을 돕는 여러 기능을 제공합니다.

### 컴포넌트 계층[](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy)

특수 파일에 정의된 컴포넌트는 특정 계층으로 렌더링됩니다:

  * `layout.js`
  * `template.js`
  * `error.js` (React error boundary)
  * `loading.js` (React suspense boundary)
  * `not-found.js` ("not found" UI용 React error boundary)
  * `page.js` 또는 중첩된 `layout.js`

중첩 라우트에서는 컴포넌트가 재귀적으로 렌더링되어, 라우트 세그먼트의 컴포넌트가 부모 세그먼트의 컴포넌트 **안쪽에** 중첩됩니다.

### Colocation[](https://nextjs.org/docs/app/getting-started/project-structure#colocation)

`app` 디렉터리에서 중첩 폴더는 라우트 구조를 정의합니다. 각 폴더는 URL 경로의 해당 세그먼트에 매핑되는 라우트 세그먼트를 나타냅니다.

하지만 라우트 구조가 폴더를 통해 정의되더라도, `page.js` 또는 `route.js` 파일이 라우트 세그먼트에 추가되기 전까지는 라우트가 **공개적으로 접근 가능하지 않습니다**.

또한 라우트가 공개되더라도, 클라이언트로 전송되는 것은 `page.js` 또는 `route.js`가 반환하는 **콘텐츠뿐**입니다.

따라서 `app` 디렉터리의 라우트 세그먼트 안에 있는 **프로젝트 파일을 안전하게 같은 위치에 둘 수 있으며**, 실수로 라우팅되는 일은 없습니다.

> **좋은 정보**: 프로젝트 파일을 `app` 안에 같이 둘 수도 있지만 **반드시** 그렇게 해야 하는 것은 아닙니다. 원한다면 [이 파일들을 `app` 디렉터리 밖에 둘 수도 있습니다](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app).

### 비공개 폴더[](https://nextjs.org/docs/app/getting-started/project-structure#private-folders)

비공개 폴더는 폴더 이름 앞에 밑줄을 붙여 `_folderName`처럼 만들면 됩니다.

이는 해당 폴더가 라우팅 시스템에서 제외되어 **폴더와 모든 하위 폴더를** 라우팅 대상에서 옵트아웃하는 내부 구현 세부사항임을 의미합니다.

`app` 디렉터리의 파일은 [기본적으로 안전하게 공동 위치에 둘 수 있으므로](https://nextjs.org/docs/app/getting-started/project-structure#colocation) 비공개 폴더가 필수는 아닙니다. 하지만 다음과 같은 용도로 유용합니다.

  * UI 로직과 라우팅 로직을 분리
  * 프로젝트 전체와 Next.js 생태계에서 내부 파일을 일관되게 구성
  * 코드 편집기에서 파일을 정렬·그룹화
  * 향후 Next.js 파일 컨벤션과 잠재적인 이름 충돌 방지

> **알아 두면 좋아요** :
>
>   * 프레임워크 컨벤션은 아니지만, 비공개 폴더 밖의 파일에도 동일한 밑줄 패턴을 사용해 “비공개” 표시를 고려할 수 있습니다.
>   * 폴더 이름 앞에 밑줄의 URL 인코딩 형태인 `%5F`를 붙여 `%5FfolderName`처럼 만들면 밑줄로 시작하는 URL 세그먼트를 생성할 수 있습니다.
>   * 비공개 폴더를 사용하지 않는 경우, 예기치 않은 이름 충돌을 피하려면 Next.js [특수 파일 컨벤션](https://nextjs.org/docs/app/getting-started/project-structure#routing-files)을 알아두면 도움이 됩니다.
>

### 라우트 그룹[](https://nextjs.org/docs/app/getting-started/project-structure#route-groups)

라우트 그룹은 폴더를 괄호로 감싸 `(folderName)`처럼 만들면 생성할 수 있습니다.

이는 해당 폴더가 조직 목적용이며 라우트의 URL 경로에 **포함되지 않아야 함**을 의미합니다.

라우트 그룹은 다음과 같은 경우에 유용합니다.

  * 사이트 섹션, 의도, 팀별로 라우트를 구성 (예: 마케팅 페이지, 관리자 페이지 등)
  * 동일한 라우트 세그먼트 레벨에서 중첩 레이아웃을 활성화:
    * [동일 세그먼트에서 여러 중첩 레이아웃(여러 루트 레이아웃 포함) 생성](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)
    * [공통 세그먼트 내 일부 라우트에만 레이아웃 추가](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)

### `src` 폴더[](https://nextjs.org/docs/app/getting-started/project-structure#src-folder)

Next.js는 `app`을 포함한 애플리케이션 코드를 선택적 [`src` 폴더](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)에 저장하는 것을 지원합니다. 이는 프로젝트 루트에 위치한 구성 파일과 애플리케이션 코드를 분리합니다.

## 예시[](https://nextjs.org/docs/app/getting-started/project-structure#examples)

다음 섹션은 일반적인 전략의 매우 상위 수준 개요입니다. 가장 간단한 요약은 팀에 맞는 전략을 선택하고 프로젝트 전체에서 일관되게 유지하는 것입니다.

> **알아 두면 좋아요** : 아래 예시에서는 `components`와 `lib` 폴더를 범용 플레이스홀더로 사용합니다. 이름에 특별한 프레임워크 의미는 없으며, 프로젝트마다 `ui`, `utils`, `hooks`, `styles` 등 다른 폴더를 사용할 수 있습니다.

### `app` 밖에 프로젝트 파일 저장[](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app)

이 전략은 모든 애플리케이션 코드를 프로젝트 **루트의 공유 폴더**에 두고 `app` 디렉터리를 순수 라우팅 용도로 유지합니다.

### `app` 내부 최상위 폴더에 프로젝트 파일 저장[](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-in-top-level-folders-inside-of-app)

이 전략은 모든 애플리케이션 코드를 `app` 디렉터리 **루트의 공유 폴더**에 저장합니다.

### 기능 또는 라우트별로 프로젝트 파일 분할[](https://nextjs.org/docs/app/getting-started/project-structure#split-project-files-by-feature-or-route)

이 전략은 전역 공유 애플리케이션 코드를 루트 `app` 디렉터리에 두고, 보다 구체적인 애플리케이션 코드를 해당 라우트 세그먼트로 **분할**합니다.

### URL 경로에 영향을 주지 않고 라우트 구성[](https://nextjs.org/docs/app/getting-started/project-structure#organize-routes-without-affecting-the-url-path)

URL에 영향을 주지 않고 라우트를 구성하려면 관련 라우트를 함께 유지할 그룹을 생성하세요. 괄호 안 폴더는 URL에서 생략됩니다 (예: `(marketing)` 또는 `(shop)`).

`(marketing)`과 `(shop)` 내부의 라우트가 동일한 URL 계층을 공유하더라도, 각 폴더에 `layout.js` 파일을 추가하면 그룹마다 다른 레이아웃을 생성할 수 있습니다.

### 특정 세그먼트를 레이아웃에 옵트인[](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)

특정 라우트를 레이아웃에 옵트인하려면 새 라우트 그룹(예: `(shop)`)을 만들고 동일한 레이아웃을 공유하는 라우트(예: `account`, `cart`)를 그 그룹으로 이동하세요. 그룹 밖의 라우트(예: `checkout`)는 해당 레이아웃을 공유하지 않습니다.

### 특정 라우트에 로딩 스켈레톤 적용[](https://nextjs.org/docs/app/getting-started/project-structure#opting-for-loading-skeletons-on-a-specific-route)

`loading.js` 파일을 통해 특정 라우트에 [로딩 스켈레톤](https://nextjs.org/docs/app/api-reference/file-conventions/loading)을 적용하려면 새 라우트 그룹(예: `/(overview)`)을 만들고 `loading.tsx`를 그 라우트 그룹 안으로 이동하세요.

이제 `loading.tsx` 파일은 URL 경로 구조에 영향을 주지 않고 전체 대시보드가 아니라 대시보드 → overview 페이지에만 적용됩니다.

### 여러 루트 레이아웃 생성[](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)

여러 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)을 만들려면 최상위 `layout.js` 파일을 제거하고 각 라우트 그룹 내부에 `layout.js` 파일을 추가하세요. 이는 완전히 다른 UI나 경험을 가진 섹션으로 애플리케이션을 분할하는 데 유용합니다. 각 루트 레이아웃에는 `<html>` 및 `<body>` 태그를 추가해야 합니다.

위 예시에서 `(marketing)`과 `(shop)` 모두 고유한 루트 레이아웃을 가집니다.

Was this helpful?

supported.

Send