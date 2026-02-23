---
title: '파일 시스템 규칙: Route Groups'
description: '라우트 그룹은 폴더 이름을 기준으로 경로를 팀이나 카테고리별로 구성할 수 있게 해주는 폴더 규칙입니다.'
---

# 파일 시스템 규칙: Route Groups | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/route-groups

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)Route Groups

# 라우트 그룹

마지막 업데이트 2026년 2월 20일

라우트 그룹은 폴더 이름을 기준으로 경로를 팀이나 카테고리별로 구성할 수 있게 해주는 폴더 규칙입니다.

## 규칙[](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#convention)

폴더 이름을 괄호로 감싸 `(folderName)` 형식으로 작성하면 라우트 그룹을 만들 수 있습니다.

이 규칙은 해당 폴더가 조직화를 위한 것임을 나타내며, 라우트의 URL 경로에 **포함되지 않아야** 함을 의미합니다.

## 사용 사례[](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#use-cases)

  * 라우트를 팀, 관심사, 기능별로 구성.
  * 여러 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)을 정의.
  * 특정 라우트 세그먼트만 레이아웃을 공유하도록 선택하고 나머지는 분리.

## 주의 사항[](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#caveats)

  * **전체 페이지 로드**: 서로 다른 루트 레이아웃을 사용하는 라우트 간에 이동하면 전체 페이지 새로고침이 발생합니다. 예를 들어 `/cart`에서 `app/(shop)/layout.js`를, `/blog`에서 `app/(marketing)/layout.js`를 사용하는 경우입니다. 이는 **여러 루트 레이아웃**을 사용할 때만 해당됩니다.
  * **경로 충돌**: 서로 다른 그룹의 라우트가 동일한 URL 경로로 해석되면 안 됩니다. 예를 들어 `(marketing)/about/page.js`와 `(shop)/about/page.js`는 모두 `/about`으로 해석되어 오류가 발생합니다.
  * **최상위 루트 레이아웃**: 최상위 `layout.js` 없이 여러 루트 레이아웃을 사용하는 경우 홈 라우트(/)가 반드시 하나의 라우트 그룹 안에 정의되어 있어야 합니다. 예: app/(marketing)/page.js.

보내기