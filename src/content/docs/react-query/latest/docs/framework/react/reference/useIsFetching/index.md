---
title: 'useIsFetching'
description: '는 애플리케이션이 백그라운드에서 로딩하거나 가져오는 쿼리의  값을 반환하는 선택적 훅으로, 앱 전역 로딩 인디케이터에 유용합니다.'
---

출처 URL: https://tanstack.com/query/latest/docs/framework/react/reference/useIsFetching

# useIsFetching

`useIsFetching`는 애플리케이션이 백그라운드에서 로딩하거나 가져오는 쿼리의 `number` 값을 반환하는 선택적 훅으로, 앱 전역 로딩 인디케이터에 유용합니다.

```tsx
import { useIsFetching } from '@tanstack/react-query'
// How many queries are fetching?
const isFetching = useIsFetching()
// How many queries matching the posts prefix are fetching?
const isFetchingPosts = useIsFetching({ queryKey: ['posts'] })
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
- `queryClient?: QueryClient`
  - 커스텀 QueryClient를 사용하려면 이 값을 지정하세요. 그렇지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.

**Returns**

- `isFetching: number`
  - 애플리케이션이 현재 백그라운드에서 로딩하거나 가져오는 쿼리의 `number` 값입니다.

