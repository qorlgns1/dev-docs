---
title: '쿼리 옵션'
description: '여러 위치에서 와 을 공유하면서도 서로 가까이 유지하는 가장 좋은 방법 중 하나는  헬퍼를 사용하는 것입니다. 런타임에서는 이 헬퍼가 넘겨준 값을 그대로 반환하지만, TypeScript와 함께 사용할 때 많은 장점이 있습니다. 쿼리에 필요한 모든 옵션을 한곳에서 정의할...'
---

# 쿼리 옵션

여러 위치에서 `queryKey`와 `queryFn`을 공유하면서도 서로 가까이 유지하는 가장 좋은 방법 중 하나는 `queryOptions` 헬퍼를 사용하는 것입니다. 런타임에서는 이 헬퍼가 넘겨준 값을 그대로 반환하지만, [TypeScript와 함께 사용할 때](https://tanstack.com/query/latest/docs/framework/react/typescript.md#typing-query-options) 많은 장점이 있습니다. 쿼리에 필요한 모든 옵션을 한곳에서 정의할 수 있고, 모든 옵션에 대해 타입 추론과 타입 안전성도 확보할 수 있습니다.

[//]: # 'Example1'

```ts
import { queryOptions } from '@tanstack/react-query'

function groupOptions(id: number) {
  return queryOptions({
    queryKey: ['groups', id],
    queryFn: () => fetchGroups(id),
    staleTime: 5 * 1000,
  })
}

// usage:

useQuery(groupOptions(1))
useSuspenseQuery(groupOptions(5))
useQueries({
  queries: [groupOptions(1), groupOptions(2)],
})
queryClient.prefetchQuery(groupOptions(23))
queryClient.setQueryData(groupOptions(42).queryKey, newGroups)
```

[//]: # 'Example1'

Infinite Query의 경우 별도의 [`infiniteQueryOptions`](https://tanstack.com/query/latest/docs/framework/react/reference/infiniteQueryOptions.md) 헬퍼를 사용할 수 있습니다.

컴포넌트 수준에서 일부 옵션을 계속 재정의할 수도 있습니다. 매우 일반적이면서 유용한 패턴은 컴포넌트별 [`select`](https://tanstack.com/query/latest/docs/framework/react/guides/render-optimizations.md#select) 함수를 만드는 것입니다.

[//]: # 'Example2'

```ts
// Type inference still works, so query.data will be the return type of select instead of queryFn

const query = useQuery({
  ...groupOptions(1),
  select: (data) => data.groupName,
})
```

[//]: # 'Example2'

