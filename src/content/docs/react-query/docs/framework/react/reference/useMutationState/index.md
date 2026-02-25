---
title: 'useMutationState'
description: '는 에 있는 모든 뮤테이션에 접근할 수 있는 훅입니다. 를 전달해 뮤테이션을 좁혀 볼 수 있고, 를 사용해 뮤테이션 상태를 변환할 수 있습니다.'
---

# useMutationState

`useMutationState`는 `MutationCache`에 있는 모든 뮤테이션에 접근할 수 있는 훅입니다. `filters`를 전달해 뮤테이션을 좁혀 볼 수 있고, `select`를 사용해 뮤테이션 상태를 변환할 수 있습니다.

**예시 1: 실행 중인 모든 뮤테이션의 변수 가져오기**

```tsx
import { useMutationState } from '@tanstack/react-query'

const variables = useMutationState({
  filters: { status: 'pending' },
  select: (mutation) => mutation.state.variables,
})
```

**예시 2: `mutationKey`를 통해 특정 뮤테이션의 모든 데이터 가져오기**

```tsx
import { useMutation, useMutationState } from '@tanstack/react-query'

const mutationKey = ['posts']

// Some mutation that we want to get the state for
const mutation = useMutation({
  mutationKey,
  mutationFn: (newPost) => {
    return axios.post('/posts', newPost)
  },
})

const data = useMutationState({
  // this mutation key needs to match the mutation key of the given mutation (see above)
  filters: { mutationKey },
  select: (mutation) => mutation.state.data,
})
```

**예시 3: `mutationKey`를 통해 최신 뮤테이션 데이터에 접근하기**  
`mutate`가 호출될 때마다 `gcTime` 밀리초 동안 유지되는 새로운 항목이 뮤테이션 캐시에 추가됩니다.

최신 호출에 접근하려면 `useMutationState`가 반환하는 마지막 항목을 확인하면 됩니다.

```tsx
import { useMutation, useMutationState } from '@tanstack/react-query'

const mutationKey = ['posts']

// Some mutation that we want to get the state for
const mutation = useMutation({
  mutationKey,
  mutationFn: (newPost) => {
    return axios.post('/posts', newPost)
  },
})

const data = useMutationState({
  // this mutation key needs to match the mutation key of the given mutation (see above)
  filters: { mutationKey },
  select: (mutation) => mutation.state.data,
})

// Latest mutation data
const latest = data[data.length - 1]
```

**옵션**

- `options`
  - `filters?: MutationFilters`: [Mutation Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#mutation-filters)
  - `select?: (mutation: Mutation) => TResult`
    - 이 옵션으로 뮤테이션 상태를 변환합니다.
- `queryClient?: QueryClient`
  - 사용자 지정 QueryClient를 사용하려면 지정합니다. 지정하지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.

**반환값**

- `Array<TResult>`
  - 매칭되는 각 뮤테이션에 대해 `select`가 반환한 값들로 구성된 배열입니다.

