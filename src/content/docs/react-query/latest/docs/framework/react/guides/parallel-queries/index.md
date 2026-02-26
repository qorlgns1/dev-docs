---
title: '병렬 쿼리'
description: '“병렬” 쿼리는 동시에 실행되어 가져오기 동시성을 극대화하는 쿼리입니다.'
---

# 병렬 쿼리

“병렬” 쿼리는 동시에 실행되어 가져오기 동시성을 극대화하는 쿼리입니다.

## 수동 병렬 쿼리

병렬 쿼리의 개수가 변하지 않는다면, 병렬 쿼리를 사용하기 위해 **추가 작업이 필요 없습니다**. TanStack Query의 `useQuery`와 `useInfiniteQuery` 훅을 원하는 만큼 나란히 사용하면 됩니다!

[//]: # 'Example'

```tsx
function App () {
  // The following queries will execute in parallel
  const usersQuery = useQuery({ queryKey: ['users'], queryFn: fetchUsers })
  const teamsQuery = useQuery({ queryKey: ['teams'], queryFn: fetchTeams })
  const projectsQuery = useQuery({ queryKey: ['projects'], queryFn: fetchProjects })
  ...
}
```

[//]: # 'Example'
[//]: # 'Info'

> React Query를 서스펜스 모드에서 사용할 때는 이러한 병렬 패턴이 동작하지 않습니다. 첫 번째 쿼리가 내부적으로 프로미스를 throw하면서, 나머지 쿼리가 실행되기 전에 컴포넌트가 서스펜드되기 때문입니다. 이를 우회하려면 `useSuspenseQueries` 훅을 사용(권장)하거나, 각 `useSuspenseQuery` 인스턴스마다 별도의 컴포넌트를 두어 직접 병렬 실행을 구성해야 합니다.

[//]: # 'Info'

## `useQueries`로 동적 병렬 쿼리 실행

[//]: # 'DynamicParallelIntro'

렌더링마다 실행해야 하는 쿼리 수가 달라진다면, 훅의 규칙을 위반하게 되므로 수동 쿼리를 사용할 수 없습니다. 대신 TanStack Query는 `useQueries` 훅을 제공하며, 이를 통해 원하는 수만큼의 쿼리를 동적으로 병렬 실행할 수 있습니다.

[//]: # 'DynamicParallelIntro'

`useQueries`는 **옵션 객체**를 받으며, 이 객체의 **queries 키**에는 **쿼리 객체 배열**을 전달합니다. 반환값은 **쿼리 결과 배열**입니다:

[//]: # 'Example2'

```tsx
function App({ users }) {
  const userQueries = useQueries({
    queries: users.map((user) => {
      return {
        queryKey: ['user', user.id],
        queryFn: () => fetchUserById(user.id),
      }
    }),
  })
}
```

[//]: # 'Example2'

