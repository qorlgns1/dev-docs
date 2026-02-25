---
title: 'QueryCache'
description: '는 TanStack Query의 스토리지 메커니즘으로, 포함된 모든 쿼리의 데이터, 메타 정보, 상태를 저장합니다.'
---

Source URL: https://tanstack.com/query/latest/docs/reference/QueryCache

# QueryCache

`QueryCache`는 TanStack Query의 스토리지 메커니즘으로, 포함된 모든 쿼리의 데이터, 메타 정보, 상태를 저장합니다.

**일반적으로는 `QueryCache`와 직접 상호작용하지 않고 특정 캐시에 대해 `QueryClient`를 사용합니다.**

```tsx
import { QueryCache } from '@tanstack/react-query'

const queryCache = new QueryCache({
  onError: (error) => {
    console.log(error)
  },
  onSuccess: (data) => {
    console.log(data)
  },
  onSettled: (data, error) => {
    console.log(data, error)
  },
})

const query = queryCache.find(['posts'])
```

사용 가능한 메서드는 다음과 같습니다.

- [`queryCache.find`](#querycachefind)
- [`queryCache.findAll`](#querycachefindall)
- [`queryCache.subscribe`](#querycachesubscribe)
- [`queryCache.clear`](#querycacheclear)
- [추가 자료](#further-reading)

**옵션**

- `onError?: (error: unknown, query: Query) => void`
  - 선택 사항
  - 어떤 쿼리에서 오류가 발생하면 호출됩니다.
- `onSuccess?: (data: unknown, query: Query) => void`
  - 선택 사항
  - 어떤 쿼리가 성공하면 호출됩니다.
- `onSettled?: (data: unknown | undefined, error: unknown | null, query: Query) => void`
  - 선택 사항
  - 어떤 쿼리가 완료될 때(성공이든 오류든) 호출됩니다.

## `queryCache.find`

`find`는 캐시에서 기존 쿼리 인스턴스를 가져오는 데 사용할 수 있는 약간 더 고급의 동기 메서드입니다. 이 인스턴스에는 쿼리의 **모든** 상태뿐 아니라 모든 인스턴스와 내부 동작까지 포함됩니다. 쿼리가 존재하지 않으면 `undefined`가 반환됩니다.

> 참고: 대부분의 애플리케이션에는 필요하지 않지만, 드물게 쿼리에 대한 추가 정보가 필요할 때 유용할 수 있습니다(예: `query.state.dataUpdatedAt` 타임스탬프를 확인해 초기 값으로 사용하기에 충분히 최신인지 판단).

```tsx
const query = queryCache.find(queryKey)
```

**옵션**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters#query-filters)

**반환값**

- `Query`
  - 캐시에서 가져온 쿼리 인스턴스

## `queryCache.findAll`

`findAll`은 쿼리 키가 부분적으로 일치하는 기존 쿼리 인스턴스를 캐시에서 가져올 수 있는, 더욱 고급의 동기 메서드입니다. 해당 쿼리가 없으면 빈 배열이 반환됩니다.

> 참고: 대부분의 애플리케이션에는 필요하지 않지만, 드물게 쿼리에 대한 추가 정보가 필요할 때 유용할 수 있습니다.

```tsx
const queries = queryCache.findAll(queryKey)
```

**옵션**

- `queryKey?: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)
- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)

**반환값**

- `Query[]`
  - 캐시에서 가져온 쿼리 인스턴스들

## `queryCache.subscribe`

`subscribe` 메서드는 쿼리 캐시에 전체적으로 구독하고, 쿼리 상태 변경이나 쿼리의 업데이트/추가/삭제 같은 안전하고 알려진 캐시 업데이트에 대해 통지받는 데 사용할 수 있습니다.

```tsx
const callback = (event) => {
  console.log(event.type, event.query)
}

const unsubscribe = queryCache.subscribe(callback)
```

**옵션**

- `callback: (event: QueryCacheNotifyEvent) => void`
  - 추적된 업데이트 메커니즘(예: `query.setState`, `queryClient.removeQueries` 등)을 통해 캐시가 업데이트될 때마다 쿼리 캐시와 함께 호출됩니다. 범위를 벗어난 캐시 변경은 권장되지 않으며 구독 콜백을 트리거하지 않습니다.

**반환값**

- `unsubscribe: Function => void`
  - 이 함수를 호출하면 콜백이 쿼리 캐시에서 구독 해제됩니다.

## `queryCache.clear`

`clear` 메서드는 캐시를 완전히 비우고 새롭게 시작할 때 사용할 수 있습니다.

```tsx
queryCache.clear()
```

[//]: # 'Materials'

## Further reading

QueryCache가 내부적으로 어떻게 작동하는지 더 잘 이해하려면 [TkDodo가 작성한 Inside React Query 글](https://tkdodo.eu/blog/inside-react-query)을 참고하세요.

[//]: # 'Materials'

