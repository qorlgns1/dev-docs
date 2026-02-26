---
title: '렌더링 최적화'
description: 'React Query는 컴포넌트가 실제로 필요할 때만 다시 렌더링되도록 몇 가지 최적화를 자동으로 적용합니다. 이는 다음 방법으로 이루어집니다:'
---

# 렌더링 최적화

React Query는 컴포넌트가 실제로 필요할 때만 다시 렌더링되도록 몇 가지 최적화를 자동으로 적용합니다. 이는 다음 방법으로 이루어집니다:

## 구조적 공유

React Query는 “structural sharing(구조적 공유)”이라는 기법을 사용해 가능한 많은 참조가 리렌더링 사이에서도 유지되도록 합니다. 네트워크로 데이터를 가져오면 보통 응답을 JSON으로 파싱하면서 완전히 새로운 참조가 생성됩니다. 하지만 데이터에 아무 변화가 없다면 React Query는 기존 참조를 그대로 유지합니다. 부분적으로 변경된 경우에는 변경되지 않은 부분은 유지하고 변경된 부분만 교체합니다.

> 참고: 이 최적화는 `queryFn`이 JSON 호환 데이터를 반환할 때만 동작합니다. 전역 혹은 개별 쿼리 단위로 `structuralSharing: false`를 설정해 비활성화하거나, 함수로 전달해서 직접 구조적 공유를 구현할 수도 있습니다.

### 참조 동일성

`useQuery`, `useInfiniteQuery`, `useMutation`이 반환하는 최상위 객체와 `useQueries`가 반환하는 배열은 **참조적으로 안정적이지 않습니다**. 매 렌더마다 새로운 참조가 됩니다. 그러나 이 훅들이 반환하는 `data` 속성은 가능한 한 안정적으로 유지됩니다.

## 추적된 속성

React Query는 `useQuery`가 반환한 속성 중 실제로 “사용된” 것이 있을 때만 리렌더링을 트리거합니다. 이를 위해 [Proxy 객체](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)를 사용합니다. 이 방식 덕분에 `isFetching`이나 `isStale`처럼 자주 변하지만 컴포넌트에서는 사용되지 않는 속성 때문에 발생하는 불필요한 리렌더링을 방지할 수 있습니다.

이 기능은 전역 혹은 개별 쿼리 단위로 `notifyOnChangeProps`를 직접 설정해 커스터마이즈할 수 있습니다. 기능을 끄려면 `notifyOnChangeProps: 'all'`로 설정하면 됩니다.

> 참고: 프록시의 get 트랩은 속성을 구조 분해하거나 직접 접근할 때마다 호출됩니다. 객체 나머지 구조 분해를 사용하면 이 최적화가 비활성화됩니다. 이러한 함정을 방지하기 위해 [lint 규칙](https://tanstack.com/query/latest/docs/eslint/no-rest-destructuring.md)을 제공하고 있습니다.

## select

컴포넌트가 구독해야 하는 데이터의 하위 집합을 선택하려면 `select` 옵션을 사용할 수 있습니다. 이는 고도로 최적화된 데이터 변환을 수행하거나 불필요한 리렌더링을 피하기에 유용합니다.

```js
export const useTodos = (select) => {
  return useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    select,
  })
}

export const useTodoCount = () => {
  return useTodos((data) => data.length)
}
```

`useTodoCount` 커스텀 훅을 사용하는 컴포넌트는 todos의 길이가 변경될 때만 다시 렌더링됩니다. 예를 들어 todo의 이름이 바뀌어도 다시 렌더링되지 **않습니다**.

> 참고: `select`는 성공적으로 캐시된 데이터에서만 동작하며, 에러를 던지기에 적합한 장소가 아닙니다. 에러에 대한 진실의 근원은 `queryFn`이며, 에러를 반환하는 `select` 함수는 `data`가 `undefined`이고 `isSuccess`가 `true`인 상태가 됩니다. 잘못된 데이터에서 쿼리를 실패시키려면 `queryFn`에서 에러를 처리하고, 캐싱과 관련 없는 에러 케이스는 쿼리 훅 외부에서 처리하는 것을 권장합니다.

### 메모이제이션

`select` 함수는 다음 두 조건 중 하나가 성립할 때만 다시 실행됩니다:

- `select` 함수 자체의 참조가 변경되었을 때
- `data`가 변경되었을 때

즉, 위 예시처럼 인라인으로 정의된 `select` 함수는 매 렌더마다 실행됩니다. 이를 피하려면 `select` 함수를 `useCallback`으로 감싸거나, 의존성이 없다면 안정적인 함수 참조로 분리하세요:

```js
// wrapped in useCallback
export const useTodoCount = () => {
  return useTodos(useCallback((data) => data.length, []))
}
```

```js
// extracted to a stable function reference
const selectTodoCount = (data) => data.length

export const useTodoCount = () => {
  return useTodos(selectTodoCount)
}
```

## 추가 자료

이 주제에 대한 심층 가이드는 TkDodo의 [React Query Render Optimizations](https://tkdodo.eu/blog/react-query-render-optimizations)를 참고하세요. `select` 옵션을 최적으로 사용하는 방법은 [React Query Selectors, Supercharged](https://tkdodo.eu/blog/react-query-selectors-supercharged)에서 확인할 수 있습니다.

