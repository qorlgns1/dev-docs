---
title: '가이드: 테스트'
description: 'React와 Next.js에서는 목적과 사용 사례가 다른 여러 종류의 테스트를 작성할 수 있습니다. 이 페이지는 애플리케이션을 테스트할 때 활용할 수 있는 테스트 유형과 널리 쓰이는 도구를 개괄합니다.'
---

# 가이드: 테스트 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/testing

[Pages Router](https://nextjs.org/docs/pages)[가이드](https://nextjs.org/docs/pages/guides)테스트

페이지 복사

# 테스트

마지막 업데이트 2026년 2월 20일

React와 Next.js에서는 목적과 사용 사례가 다른 여러 종류의 테스트를 작성할 수 있습니다. 이 페이지는 애플리케이션을 테스트할 때 활용할 수 있는 테스트 유형과 널리 쓰이는 도구를 개괄합니다.

## 테스트 유형[](https://nextjs.org/docs/pages/guides/testing#types-of-tests)

  * **단위 테스트(Unit Testing)**는 개별 유닛(또는 코드 블록)을 고립된 상태에서 검증합니다. React에서 유닛은 하나의 함수, 훅, 또는 컴포넌트가 될 수 있습니다.
  * **컴포넌트 테스트(Component Testing)**는 주된 대상이 React 컴포넌트인, 보다 초점을 맞춘 단위 테스트입니다. 여기에는 컴포넌트 렌더링 방식, props와의 상호작용, 사용자 이벤트에 대한 동작을 검증하는 작업이 포함될 수 있습니다.
  * **통합 테스트(Integration Testing)**는 여러 유닛이 함께 작동하는 방식을 검증합니다. 컴포넌트, 훅, 함수의 조합이 될 수 있습니다.
  * **엔드 투 엔드(E2E) 테스트**는 브라우저처럼 실제 사용자 시나리오를 모사한 환경에서 사용자 플로우를 검증합니다. 이는 프로덕션과 유사한 환경에서 특정 작업(예: 가입 플로우)을 테스트한다는 뜻입니다.
  * **스냅샷 테스트(Snapshot Testing)**는 컴포넌트가 렌더링한 출력물을 캡처해 스냅샷 파일로 저장합니다. 테스트 실행 시 컴포넌트의 현재 렌더링 결과를 저장된 스냅샷과 비교하며, 스냅샷의 변경 사항은 예상치 못한 동작 변화를 나타내는 신호로 사용됩니다.



## 가이드[](https://nextjs.org/docs/pages/guides/testing#guides)

아래 가이드를 통해 Next.js를 널리 사용되는 테스트 도구와 함께 설정하는 방법을 알아보세요.

### [Cypress와 함께 Next.js를 설정해 엔드 투 엔드(E2E) 및 컴포넌트 테스트를 수행하는 방법을 알아보세요.](https://nextjs.org/docs/pages/guides/testing/cypress)### [Jest와 함께 Next.js를 설정해 단위 테스트를 수행하는 방법을 알아보세요.](https://nextjs.org/docs/pages/guides/testing/jest)### [Playwright와 함께 Next.js를 설정해 엔드 투 엔드(E2E) 및 통합 테스트를 수행하는 방법을 알아보세요.](https://nextjs.org/docs/pages/guides/testing/playwright)### [Vitest와 React Testing Library(두 가지 인기 있는 단위 테스트 라이브러리)로 Next.js를 설정하는 방법을 알아보세요.](https://nextjs.org/docs/pages/guides/testing/vitest)

도움이 되었나요?

지원됨.

보내기
