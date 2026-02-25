---
title: 'useIsMutating'
description: '은 애플리케이션이 현재 가져오고 있는 변이의 를 반환하는 선택적 훅으로, 앱 전역 로딩 인디케이터에 유용합니다.'
---

# useIsMutating

`useIsMutating`은 애플리케이션이 현재 가져오고 있는 변이의 `number`를 반환하는 선택적 훅으로, 앱 전역 로딩 인디케이터에 유용합니다.

```tsx
import { useIsMutating } from '@tanstack/react-query'
// How many mutations are fetching?
const isMutating = useIsMutating()
// How many mutations matching the posts prefix are fetching?
const isMutatingPosts = useIsMutating({ mutationKey: ['posts'] })
```

**Options**

- `filters?: MutationFilters`: [Mutation Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#mutation-filters)
- `queryClient?: QueryClient`
  - 사용자 정의 QueryClient를 사용하려면 이 옵션을 지정하세요. 지정하지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.

**Returns**

- `isMutating: number`
  - 애플리케이션이 현재 가져오는 변이의 `number`입니다.

