---
title: '가이드: 테스트'
description: '마지막 업데이트 2026년 2월 20일'
---

# 가이드: 테스트 | Next.js
Source URL: https://nextjs.org/docs/app/guides/testing

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)테스트

페이지 복사

# 테스트

마지막 업데이트 2026년 2월 20일

React와 Next.js에는 작성 목적과 활용 사례가 서로 다른 다양한 테스트 유형이 있습니다. 이 페이지에서는 애플리케이션을 테스트할 때 사용할 수 있는 테스트 유형과 일반적인 도구를 개괄합니다.

## 테스트 유형[](https://nextjs.org/docs/app/guides/testing#types-of-tests)

  * **단위 테스트(Unit Testing)** 는 개별 단위(코드 블록)를 독립적으로 검증합니다. React에서 단위는 하나의 함수, 훅, 또는 컴포넌트일 수 있습니다.
  * **컴포넌트 테스트(Component Testing)** 는 테스트 대상이 주로 React 컴포넌트인 단위 테스트의 확장형입니다. 컴포넌트 렌더링 방식, props 상호작용, 사용자 이벤트에 대한 동작 등을 검증할 수 있습니다.
  * **통합 테스트(Integration Testing)** 는 여러 단위가 함께 동작하는 방식을 검증합니다. 컴포넌트, 훅, 함수의 조합이 될 수 있습니다.
  * **엔드 투 엔드(E2E) 테스트** 는 브라우저처럼 실제 사용자 시나리오를 모사한 환경에서 사용자 플로우를 검증합니다. 예를 들어 가입 흐름 같은 특정 작업을 프로덕션과 유사한 환경에서 테스트합니다.
  * **스냅샷 테스트(Snapshot Testing)** 는 컴포넌트의 렌더링 결과를 스냅샷 파일로 저장합니다. 테스트 실행 시 현재 렌더링 결과를 저장된 스냅샷과 비교해 예기치 않은 동작 변화를 감지합니다.

## Async Server Components[](https://nextjs.org/docs/app/guides/testing#async-server-components)

`async` 서버 컴포넌트는 React 생태계에서 새롭기 때문에 일부 도구는 아직 완전하게 지원하지 않습니다. 그동안은 `async` 컴포넌트에 대해 **단위 테스트**보다 **엔드 투 엔드 테스트**를 사용하는 것을 권장합니다.

## 가이드[](https://nextjs.org/docs/app/guides/testing#guides)

아래 가이드를 통해 Next.js와 자주 사용되는 테스트 도구를 설정하는 방법을 알아보세요:

### [Cypress Next.js와 함께 End-to-End(E2E) 및 컴포넌트 테스트를 설정하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/testing/cypress)### [Jest Next.js와 함께 단위 테스트 및 스냅샷 테스트를 설정하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/testing/jest)### [Playwright Next.js와 함께 End-to-End(E2E) 테스트를 설정하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/testing/playwright)### [Vitest Next.js와 함께 단위 테스트를 설정하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/testing/vitest)

도움이 되었나요?

지원됨.

보내기
