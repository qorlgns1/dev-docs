---
title: '아키텍처: 접근성'
description: '마지막 업데이트 2026년 2월 20일'
---

# 아키텍처: 접근성 | Next.js

Source URL: https://nextjs.org/docs/architecture/accessibility

[Next.js Docs](https://nextjs.org/docs)[Architecture](https://nextjs.org/docs/architecture)Accessibility

Copy page

# 접근성

마지막 업데이트 2026년 2월 20일

Next.js 팀은 모든 개발자(및 최종 사용자)가 Next.js를 활용할 수 있도록 접근성을 보장하기 위해 노력하고 있습니다. 기본적으로 Next.js에 접근성 기능을 추가해 두어 모두에게 더 포괄적인 웹을 제공하는 것이 목표입니다.

## Route Announcements[](https://nextjs.org/docs/architecture/accessibility#route-announcements)

서버에서 렌더링된 페이지 간 이동 시(예: `<a href>` 태그 사용) 화면 읽기 프로그램과 기타 보조 기술은 페이지가 로드될 때 페이지 제목을 안내하여 사용자가 페이지가 변경되었음을 이해하도록 합니다.

전통적인 페이지 내비게이션 외에도 Next.js는 성능 향상을 위해 클라이언트 측 전환(`next/link` 사용)을 지원합니다. 클라이언트 측 전환도 보조 기술에 의해 안내되도록, Next.js는 기본적으로 라우트 알리미를 포함합니다.

Next.js 라우트 알리미는 안내할 페이지 이름을 찾기 위해 먼저 `document.title`, 그다음 `<h1>` 요소, 마지막으로 URL 경로 이름을 검사합니다. 가장 접근성 높은 사용자 경험을 위해 애플리케이션의 각 페이지에 고유하고 설명적인 제목을 지정하세요.

## Linting[](https://nextjs.org/docs/architecture/accessibility#linting)

Next.js는 Next.js 전용 커스텀 규칙을 포함한 [통합 ESLint 환경](https://nextjs.org/docs/pages/api-reference/config/eslint)을 기본 제공하며, `eslint-plugin-jsx-a11y`를 포함해 접근성 문제를 조기에 포착하도록 돕습니다. 기본 경고 대상은 다음과 같습니다.

  * [aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
  * [aria-proptypes](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-proptypes.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
  * [aria-unsupported-elements](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-unsupported-elements.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
  * [role-has-required-aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/role-has-required-aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
  * [role-supports-aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/role-supports-aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)



예를 들어, 이 플러그인은 `img` 태그에 alt 텍스트를 추가하고, 올바른 `aria-*` 속성과 `role` 속성을 사용하는 등 다양한 접근성 요구 사항을 충족하도록 도와줍니다.

## 접근성 리소스[](https://nextjs.org/docs/architecture/accessibility#accessibility-resources)

  * [WebAIM WCAG 체크리스트](https://webaim.org/standards/wcag/checklist)
  * [WCAG 2.2 가이드라인](https://www.w3.org/TR/WCAG22/)
  * [The A11y Project](https://www.a11yproject.com/)
  * 전경과 배경 요소 간의 [색 대비 비율](https://developer.mozilla.org/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast)을 확인하세요.
  * 애니메이션 작업 시 [`prefers-reduced-motion`](https://web.dev/prefers-reduced-motion/)을 활용하세요.



유용했나요?

supported.

Send
