---
title: '뮤테이션으로 인한 무효화'
description: '쿼리를 무효화하는 것만으로는 절반의 전투에 불과합니다. 언제 무효화해야 하는지를 아는 것이 나머지 절반입니다. 보통 앱에서 뮤테이션이 성공하면, 그 뮤테이션의 새로운 변경 사항을 반영하기 위해 무효화하고 필요 시 다시 가져와야 하는 관련 쿼리가 애플리케이션에 존재할 가...'
---

<!-- Skipping add-doc skill: user only requested direct translation of provided Markdown. -->

# 뮤테이션으로 인한 무효화

쿼리를 무효화하는 것만으로는 절반의 전투에 불과합니다. **언제** 무효화해야 하는지를 아는 것이 나머지 절반입니다. 보통 앱에서 뮤테이션이 성공하면, 그 뮤테이션의 새로운 변경 사항을 반영하기 위해 무효화하고 필요 시 다시 가져와야 하는 관련 쿼리가 애플리케이션에 존재할 가능성이 매우 큽니다.

예를 들어, 새로운 todo를 게시하는 뮤테이션이 있다고 가정해 봅시다.

[//]: # 'Example'

```tsx
const mutation = useMutation({ mutationFn: postTodo })
```

[//]: # 'Example'

성공적인 `postTodo` 뮤테이션이 발생하면, 새로운 todo 아이템을 표시할 수 있도록 모든 `todos` 쿼리를 무효화하고 필요하다면 다시 가져오길 원할 것입니다. 이를 위해 `useMutation`의 `onSuccess` 옵션과 `client`의 `invalidateQueries` 함수를 사용할 수 있습니다.

[//]: # 'Example2'

```tsx
import { useMutation, useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient()

// When this mutation succeeds, invalidate any queries with the `todos` or `reminders` query key
const mutation = useMutation({
  mutationFn: addTodo,
  onSuccess: async () => {
    // If you're invalidating a single query
    await queryClient.invalidateQueries({ queryKey: ['todos'] })

    // If you're invalidating multiple queries
    await Promise.all([
      queryClient.invalidateQueries({ queryKey: ['todos'] }),
      queryClient.invalidateQueries({ queryKey: ['reminders'] }),
    ])
  },
})
```

[//]: # 'Example2'

`onSuccess`에서 Promise를 반환하면, 뮤테이션이 완전히 끝나기 전에 데이터가 업데이트되도록 보장합니다(즉, onSuccess가 완료될 때까지 isPending이 true 상태로 유지됩니다).

[//]: # 'Example2'

[`useMutation` 훅](https://tanstack.com/query/latest/docs/framework/react/guides/mutations.md)에 제공된 콜백 중 원하는 곳에 무효화를 연결할 수 있습니다.

[//]: # 'Materials'

## 추가 읽을거리

뮤테이션 이후에 쿼리를 자동으로 무효화하는 기법은 [TkDodo의 Automatic Query Invalidation after Mutations 글](https://tkdodo.eu/blog/automatic-query-invalidation-after-mutations)을 참고하세요.

[//]: # 'Materials'

