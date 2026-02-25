---
title: 'queryOptions'
description: 'add-doc skill: translating provided TanStack Query snippet.'
---

add-doc skill: translating provided TanStack Query snippet.

# queryOptions

```tsx
queryOptions({
  queryKey,
  ...options,
})
```

**옵션**

[`useQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)에 전달할 수 있는 모든 것을 일반적으로 `queryOptions`에도 전달할 수 있습니다. 일부 옵션은 `queryClient.prefetchQuery` 같은 함수로 전달되면 효과가 없지만, TypeScript는 이러한 초과 속성을 허용합니다.

- `queryKey: QueryKey`
  - **필수**
  - 옵션을 생성할 때 사용할 쿼리 키입니다.
- `experimental_prefetchInRender?: boolean`
  - 선택 사항
  - 기본값은 `false`
  - `true`로 설정하면 렌더링 중에 쿼리를 프리페치하여 특정 최적화 시나리오에 유용할 수 있습니다.
  - 실험적인 `useQuery().promise` 기능을 사용하려면 활성화해야 합니다.

[//]: # 'Materials'

## 추가 읽을거리

`QueryOptions`에 대해 더 알아보려면 [TkDodo의 The Query Options API 글](https://tkdodo.eu/blog/the-query-options-api)을 참고하세요.

[//]: # 'Materials'

