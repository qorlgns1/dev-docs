---
title: 'Query Filters'
description: '일부 TanStack Query 메서드는  또는  객체를 받습니다.'
---

# 필터

일부 TanStack Query 메서드는 `QueryFilters` 또는 `MutationFilters` 객체를 받습니다.

## `Query Filters`

쿼리 필터는 특정 조건을 통해 쿼리를 매칭하는 객체입니다:

```tsx
// Cancel all queries
await queryClient.cancelQueries()

// Remove all inactive queries that begin with `posts` in the key
queryClient.removeQueries({ queryKey: ['posts'], type: 'inactive' })

// Refetch all active queries
await queryClient.refetchQueries({ type: 'active' })

// Refetch all active queries that begin with `posts` in the key
await queryClient.refetchQueries({ queryKey: ['posts'], type: 'active' })
```

쿼리 필터 객체는 다음 속성을 지원합니다:

- `queryKey?: QueryKey`
  - 매칭할 쿼리 키를 정의하려면 이 속성을 설정하세요.
- `exact?: boolean`
  - 쿼리 키를 포함 검색하지 않으려면 `exact: true` 옵션을 전달해 지정한 쿼리 키와 정확히 일치하는 쿼리만 반환하도록 합니다.
- `type?: 'active' | 'inactive' | 'all'`
  - 기본값은 `all`
  - `active`로 설정하면 활성 쿼리를 매칭합니다.
  - `inactive`로 설정하면 비활성 쿼리를 매칭합니다.
- `stale?: boolean`
  - `true`로 설정하면 오래된 쿼리를 매칭합니다.
  - `false`로 설정하면 최신 쿼리를 매칭합니다.
- `fetchStatus?: FetchStatus`
  - `fetching`으로 설정하면 현재 패치 중인 쿼리를 매칭합니다.
  - `paused`로 설정하면 패치하려 했지만 `paused` 상태인 쿼리를 매칭합니다.
  - `idle`로 설정하면 패치 중이 아닌 쿼리를 매칭합니다.
- `predicate?: (query: Query) => boolean`
  - 이 프레디킷 함수는 모든 매칭 쿼리에 대한 최종 필터로 사용됩니다. 다른 필터가 지정되지 않았다면, 캐시의 모든 쿼리에 대해 이 함수가 평가됩니다.

## `Mutation Filters`

뮤테이션 필터는 특정 조건을 통해 뮤테이션을 매칭하는 객체입니다:

```tsx
// Get the number of all fetching mutations
await queryClient.isMutating()

// Filter mutations by mutationKey
await queryClient.isMutating({ mutationKey: ['post'] })

// Filter mutations using a predicate function
await queryClient.isMutating({
  predicate: (mutation) => mutation.state.variables?.id === 1,
})
```

뮤테이션 필터 객체는 다음 속성을 지원합니다:

- `mutationKey?: MutationKey`
  - 매칭할 뮤테이션 키를 정의하려면 이 속성을 설정하세요.
- `exact?: boolean`
  - 뮤테이션 키를 포함 검색하지 않으려면 `exact: true` 옵션을 전달해 지정한 뮤테이션 키와 정확히 일치하는 뮤테이션만 반환하도록 합니다.
- `status?: MutationStatus`
  - 뮤테이션 상태에 따라 필터링할 수 있습니다.
- `predicate?: (mutation: Mutation) => boolean`
  - 이 프레디킷 함수는 모든 매칭 뮤테이션에 대한 최종 필터로 사용됩니다. 다른 필터가 지정되지 않았다면, 캐시의 모든 뮤테이션에 대해 이 함수가 평가됩니다.

## Utils

### `matchQuery`

```tsx
const isMatching = matchQuery(filters, query)
```

쿼리가 제공된 쿼리 필터 집합과 일치하는지 여부를 나타내는 불리언을 반환합니다.

### `matchMutation`

```tsx
const isMatching = matchMutation(filters, mutation)
```

뮤테이션이 제공된 뮤테이션 필터 집합과 일치하는지 여부를 나타내는 불리언을 반환합니다.

