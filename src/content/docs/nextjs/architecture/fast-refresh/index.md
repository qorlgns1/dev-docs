---
title: '아키텍처: Fast Refresh'
description: 'Fast Refresh는 Next.js에 통합된 React 기능으로, 파일을 저장할 때 임시 클라이언트 상태를 유지한 채 브라우저 페이지를 라이브 리로드할 수 있게 해줍니다. 9.4 이상의 모든 Next.js 애플리케이션에서 기본 활성화되어 있으며, Fast Refre...'
---

# 아키텍처: Fast Refresh | Next.js
출처 URL: https://nextjs.org/docs/architecture/fast-refresh
[Next.js 문서](https://nextjs.org/docs)[아키텍처](https://nextjs.org/docs/architecture)Fast Refresh

# Fast Refresh
마지막 업데이트 2026년 2월 20일

Fast Refresh는 Next.js에 통합된 React 기능으로, 파일을 저장할 때 임시 클라이언트 상태를 유지한 채 브라우저 페이지를 라이브 리로드할 수 있게 해줍니다. **9.4 이상**의 모든 Next.js 애플리케이션에서 기본 활성화되어 있으며, Fast Refresh가 켜져 있으면 대부분의 수정 사항이 1초 안에 보입니다.

## 작동 방식[](https://nextjs.org/docs/architecture/fast-refresh#how-it-works)
  * **React 컴포넌트만 export**하는 파일을 수정하면 Fast Refresh는 해당 파일의 코드만 갱신하고 컴포넌트를 다시 렌더링합니다. 스타일, 렌더링 로직, 이벤트 핸들러, 이펙트 등 파일 안의 어떤 부분도 수정할 수 있습니다.
  * React 컴포넌트가 아닌 export가 있는 파일을 수정하면 Fast Refresh는 그 파일과 이를 import하는 다른 파일을 모두 다시 실행합니다. 예를 들어 `Button.js`와 `Modal.js`가 `theme.js`를 import한다면, `theme.js`를 수정할 때 두 컴포넌트가 모두 업데이트됩니다.
  * 마지막으로, **React 트리 외부의 파일에서 import하는 파일**을 **수정**하면 Fast Refresh는 **전체 리로드로 폴백**합니다. React 컴포넌트를 렌더링하면서 동시에 **비-React 컴포넌트**가 import하는 값을 export하는 파일이 있을 수 있습니다. 예를 들어 컴포넌트가 상수를 export하고, 비-React 유틸리티 파일이 이를 import하는 경우입니다. 이런 상황에서는 상수를 별도 파일로 옮긴 뒤 두 파일에서 import하는 방식을 고려하세요. 이렇게 하면 Fast Refresh를 다시 사용할 수 있습니다. 다른 사례들도 대부분 비슷하게 해결됩니다.

## 오류 복원력[](https://nextjs.org/docs/architecture/fast-refresh#error-resilience)

### 구문 오류[](https://nextjs.org/docs/architecture/fast-refresh#syntax-errors)
개발 중 구문 오류를 만들었다면, 수정하고 파일을 다시 저장하면 됩니다. 오류는 자동으로 사라지므로 앱을 다시 로드할 필요가 없습니다. **컴포넌트 상태는 잃지 않습니다**.

### 런타임 오류[](https://nextjs.org/docs/architecture/fast-refresh#runtime-errors)
컴포넌트 내부에서 런타임 오류를 유발하면 상황별 오버레이가 나타납니다. 오류를 고치면 앱을 다시 로드하지 않아도 오버레이가 자동으로 닫힙니다.

오류가 렌더링 중에 발생하지 않았다면 컴포넌트 상태는 유지됩니다. 렌더링 중 발생했다면 React는 업데이트된 코드로 애플리케이션을 다시 마운트합니다.

앱에 [오류 경계](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)가 있다면(프로덕션에서 우아한 실패를 위해 권장) 렌더링 오류 이후 다음 수정 시 렌더링을 재시도합니다. 이는 오류 경계를 사용하면 항상 루트 앱 상태로 되돌아가는 것을 막을 수 있음을 의미합니다. 다만 오류 경계가 지나치게 세분화되지 않도록 주의하세요. 오류 경계는 프로덕션에서 React가 사용하는 기능이므로 항상 의도적으로 설계해야 합니다.

## 제한 사항[](https://nextjs.org/docs/architecture/fast-refresh#limitations)
Fast Refresh는 수정 중인 컴포넌트의 로컬 React 상태를 보존하려고 하지만, 안전한 경우에만 가능하며 다음과 같은 이유로 파일을 수정할 때마다 로컬 상태가 초기화될 수 있습니다.

  * 클래스 컴포넌트는 로컬 상태가 보존되지 않습니다(함수 컴포넌트와 Hooks만 상태를 유지).
  * 수정 중인 파일이 React 컴포넌트 외에도 _다른_ export를 포함할 수 있습니다.
  * 때때로 파일이 `HOC(WrappedComponent)` 같은 고차 컴포넌트 호출 결과를 export합니다. 반환된 컴포넌트가 클래스라면 상태가 초기화됩니다.
  * `export default () => <div />;`와 같은 익명 화살표 함수는 Fast Refresh가 로컬 컴포넌트 상태를 보존하지 못하게 합니다. 대규모 코드베이스에서는 [`name-default-component` codemod](https://nextjs.org/docs/pages/guides/upgrading/codemods#name-default-component)를 사용할 수 있습니다.

코드베이스의 더 많은 부분이 함수 컴포넌트와 Hooks로 전환될수록 상태가 보존되는 경우가 늘어납니다.

## 팁[](https://nextjs.org/docs/architecture/fast-refresh#tips)
  * Fast Refresh는 기본적으로 함수 컴포넌트(및 Hooks)의 React 로컬 상태를 보존합니다.
  * 때로는 상태를 _강제로_ 초기화하고 컴포넌트를 다시 마운트하고 싶을 수 있습니다. 예를 들어 마운트 시에만 실행되는 애니메이션을 조정할 때 유용합니다. 이를 위해 수정 중인 파일 어디든 `// @refresh reset`을 추가할 수 있습니다. 이 지시문은 파일 단위로 적용되며, 해당 파일에서 정의된 컴포넌트를 편집할 때마다 Fast Refresh가 다시 마운트하도록 지시합니다.
  * 개발 중 수정하는 컴포넌트 안에 `console.log`나 `debugger;`를 넣을 수 있습니다.
  * import는 대소문자를 구분합니다. 실제 파일명과 일치하지 않으면 Fast Refresh와 전체 리로드 모두 실패할 수 있습니다. 예: `'./header'` vs `'./Header'`.

## Fast Refresh와 Hooks[](https://nextjs.org/docs/architecture/fast-refresh#fast-refresh-and-hooks)
가능한 경우 Fast Refresh는 수정 사이에서 컴포넌트 상태를 보존하려 합니다. 특히 `useState`와 `useRef`는 인수나 Hook 호출 순서를 바꾸지 않는 한 이전 값을 유지합니다.

`useEffect`, `useMemo`, `useCallback`처럼 의존성이 있는 Hooks는 Fast Refresh 중에는 _항상_ 업데이트됩니다. Fast Refresh가 진행되는 동안에는 의존성 목록이 무시됩니다.

예를 들어 `useMemo(() => x * 2, [x])`를 `useMemo(() => x * 10, [x])`로 수정하면 의존성인 `x`가 변하지 않았더라도 다시 실행됩니다. React가 이렇게 하지 않으면 수정 사항이 화면에 반영되지 않습니다.

이 때문에 예상치 못한 결과가 나타날 수 있습니다. 예를 들어 의존성 배열이 비어 있는 `useEffect`도 Fast Refresh 동안 한 번은 다시 실행됩니다.

그러나 Fast Refresh가 없더라도 `useEffect`가 가끔 다시 실행되는 상황을 견딜 수 있도록 코드를 작성하는 것이 좋은 습관입니다. 이렇게 하면 나중에 새로운 의존성을 추가하기 쉽고, [React Strict Mode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)가 이를 강제하므로 활성화를 강력히 권장합니다.
