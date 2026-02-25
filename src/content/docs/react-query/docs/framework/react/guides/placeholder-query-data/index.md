---
title: '플레이스홀더 쿼리 데이터'
description: '플레이스홀더 데이터는  옵션과 비슷하게 쿼리가 마치 이미 데이터를 가진 것처럼 동작하게 하지만, 그 데이터가 캐시에 유지되지 않는 기능입니다. 실제 데이터를 백그라운드에서 가져오는 동안에도 충분한 부분(또는 가짜) 데이터를 가지고 쿼리를 렌더링해야 하는 상황에 유용합니...'
---

# 플레이스홀더 쿼리 데이터

## 플레이스홀더 데이터란?

플레이스홀더 데이터는 `initialData` 옵션과 비슷하게 쿼리가 마치 이미 데이터를 가진 것처럼 동작하게 하지만, **그 데이터가 캐시에 유지되지 않는** 기능입니다. 실제 데이터를 백그라운드에서 가져오는 동안에도 충분한 부분(또는 가짜) 데이터를 가지고 쿼리를 렌더링해야 하는 상황에 유용합니다.

> 예: 단일 블로그 글 쿼리가 상위 블로그 글 목록에서 제목과 짧은 본문 발췌만 포함한 “미리보기” 데이터를 가져올 수 있습니다. 이 부분 데이터를 해당 쿼리 결과에 영구 보관하고 싶지는 않지만, 실제 쿼리가 전체 객체를 가져오는 동안 콘텐츠 레이아웃을 가능한 한 빨리 보여주는 데에는 도움이 됩니다.

쿼리에 필요한 순간 이전에 캐시에 플레이스홀더 데이터를 공급하는 방법은 몇 가지가 있습니다.

- 선언형 방식:
  - 쿼리에 `placeholderData` 를 제공해 캐시가 비어 있을 때 미리 채워 둡니다.
- 명령형 방식:
  - [`queryClient` 와 `placeholderData` 옵션을 사용해 데이터를 프리페치하거나 직접 가져옵니다](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)

`placeholderData` 를 사용하면 Query 는 `pending` 상태에 머무르지 않고, 표시할 `data` 가 있기 때문에 처음부터 `success` 상태로 시작합니다. 그 데이터가 단지 “플레이스홀더”일 뿐임을 구분하기 위해 Query 결과의 `isPlaceholderData` 플래그가 `true` 로 설정됩니다.

## 값으로서의 플레이스홀더 데이터

[//]: # 'ExampleValue'

```tsx
function Todos() {
  const result = useQuery({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    placeholderData: placeholderTodos,
  })
}
```

[//]: # 'ExampleValue'
[//]: # 'Memoization'

### 플레이스홀더 데이터 메모이제이션

쿼리의 플레이스홀더 데이터에 접근하는 과정이 비용이 크거나 매 렌더마다 수행하고 싶지 않다면, 해당 값을 메모이제이션할 수 있습니다.

```tsx
function Todos() {
  const placeholderData = useMemo(() => generateFakeTodos(), [])
  const result = useQuery({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    placeholderData,
  })
}
```

[//]: # 'Memoization'

## 함수로서의 플레이스홀더 데이터

`placeholderData` 는 함수가 될 수도 있으며, 이 경우 “이전” 성공 쿼리의 데이터와 Query 메타 정보를 가져올 수 있습니다. 하나의 쿼리 데이터를 다른 쿼리의 플레이스홀더로 재사용하고 싶은 상황에 유용합니다. 예를 들어 QueryKey 가 `['todos', 1]` 에서 `['todos', 2]` 로 바뀔 때, 데이터가 다음 Query 로 _전환_ 되는 동안 로딩 스피너를 보여 주는 대신 “이전” 데이터를 계속 표시할 수 있습니다. 자세한 내용은 [페이지네이션 쿼리](https://tanstack.com/query/latest/docs/framework/react/guides/paginated-queries.md)를 참고하세요.

[//]: # 'ExampleFunction'

```tsx
const result = useQuery({
  queryKey: ['todos', id],
  queryFn: () => fetch(`/todos/${id}`),
  placeholderData: (previousData, previousQuery) => previousData,
})
```

[//]: # 'ExampleFunction'

### 캐시에서 가져온 플레이스홀더 데이터

상황에 따라 다른 쿼리의 캐시된 결과를 사용해 플레이스홀더 데이터를 제공할 수도 있습니다. 대표적인 예로 블로그 글 목록 쿼리의 캐시에서 글 미리보기 데이터를 찾아, 이를 단일 글 쿼리의 플레이스홀더 데이터로 사용하는 방식이 있습니다.

[//]: # 'ExampleCache'

```tsx
function BlogPost({ blogPostId }) {
  const queryClient = useQueryClient()
  const result = useQuery({
    queryKey: ['blogPost', blogPostId],
    queryFn: () => fetch(`/blogPosts/${blogPostId}`),
    placeholderData: () => {
      // Use the smaller/preview version of the blogPost from the 'blogPosts'
      // query as the placeholder data for this blogPost query
      return queryClient
        .getQueryData(['blogPosts'])
        ?.find((d) => d.id === blogPostId)
    },
  })
}
```

[//]: # 'ExampleCache'
[//]: # 'Materials'

## 추가 자료

`Placeholder Data` 와 `Initial Data` 를 비교하려면 [TkDodo 의 글](https://tkdodo.eu/blog/placeholder-and-initial-data-in-react-query)을 참고하세요.

[//]: # 'Materials'

