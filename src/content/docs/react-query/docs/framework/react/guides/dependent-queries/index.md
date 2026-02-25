---
title: '종속 쿼리'
description: '종속(또는 직렬) 쿼리는 앞선 쿼리가 완료되어야 실행할 수 있습니다. 이를 구현하는 가장 쉬운 방법은  옵션을 사용해 쿼리가 언제 실행 준비가 되었는지 알려주는 것입니다.'
---

# 종속 쿼리

## useQuery 종속 쿼리

종속(또는 직렬) 쿼리는 앞선 쿼리가 완료되어야 실행할 수 있습니다. 이를 구현하는 가장 쉬운 방법은 `enabled` 옵션을 사용해 쿼리가 언제 실행 준비가 되었는지 알려주는 것입니다.

[//]: # '예시'

```tsx
// Get the user
const { data: user } = useQuery({
  queryKey: ['user', email],
  queryFn: getUserByEmail,
})

const userId = user?.id

// Then get the user's projects
const {
  status,
  fetchStatus,
  data: projects,
} = useQuery({
  queryKey: ['projects', userId],
  queryFn: getProjectsByUser,
  // The query will not execute until the userId exists
  enabled: !!userId,
})
```

[//]: # '예시'

`projects` 쿼리는 다음 상태로 시작합니다:

```tsx
status: 'pending'
isPending: true
fetchStatus: 'idle'
```

`user` 가 준비되는 즉시 `projects` 쿼리가 `enabled` 되고 다음 상태로 전환됩니다:

```tsx
status: 'pending'
isPending: true
fetchStatus: 'fetching'
```

프로젝트를 모두 가져오면 다음 상태로 이동합니다:

```tsx
status: 'success'
isPending: false
fetchStatus: 'idle'
```

## useQueries 종속 쿼리

동적 병렬 쿼리인 `useQueries` 역시 이전 쿼리에 의존할 수 있으며, 다음과 같이 구현합니다:

[//]: # '예시2'

```tsx
// Get the users ids
const { data: userIds } = useQuery({
  queryKey: ['users'],
  queryFn: getUsersData,
  select: (users) => users.map((user) => user.id),
})

// Then get the users messages
const usersMessages = useQueries({
  queries: userIds
    ? userIds.map((id) => {
        return {
          queryKey: ['messages', id],
          queryFn: () => getMessagesByUsers(id),
        }
      })
    : [], // if userIds is undefined, an empty array will be returned
})
```

[//]: # '예시2'

**주의**: `useQueries` 는 **쿼리 결과 배열**을 반환합니다.

## 성능 관련 참고 사항

종속 쿼리는 정의상 [request waterfall](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md)의 한 형태이므로 성능에 악영향을 줄 수 있습니다. 두 쿼리가 동일한 시간이 걸린다고 가정하면, 병렬 대신 직렬로 실행하면 항상 두 배의 시간이 들며 지연 시간이 큰 클라이언트에서는 특히 문제가 됩니다. 가능하다면 백엔드 API를 재구성해 두 쿼리를 병렬로 가져오는 편이 좋지만, 항상 실현 가능한 것은 아닙니다.

위 예시에서는 `getProjectsByUser` 를 호출하기 위해 먼저 `getUserByEmail` 을 가져오는 대신, 새로운 `getProjectsByUserEmail` 쿼리를 도입하면 워터폴 구조를 평탄화할 수 있습니다.

