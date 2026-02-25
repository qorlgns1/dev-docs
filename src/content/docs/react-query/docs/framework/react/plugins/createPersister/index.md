---
title: 'experimental_createQueryPersister'
description: '이 유틸리티는 별도 패키지로 제공되며 에서 임포트할 수 있습니다.'
---

# experimental_createQueryPersister

## 설치

이 유틸리티는 별도 패키지로 제공되며 `'@tanstack/query-persist-client-core'`에서 임포트할 수 있습니다.

```bash
npm install @tanstack/query-persist-client-core
```

또는

```bash
pnpm add @tanstack/query-persist-client-core
```

또는

```bash
yarn add @tanstack/query-persist-client-core
```

또는

```bash
bun add @tanstack/query-persist-client-core
```

> 참고: 이 유틸은 `@tanstack/react-query-persist-client` 패키지에도 포함되어 있으므로 해당 패키지를 사용 중이라면 따로 설치할 필요가 없습니다.

## 사용법

- `experimental_createQueryPersister` 함수를 임포트합니다.
- 새로운 `experimental_createQueryPersister`를 생성합니다.
  - `AsyncStorage` 인터페이스를 준수하는 어떤 `storage`도 전달할 수 있습니다. 아래 예시는 React Native의 async-storage를 사용합니다.
- 생성한 `persister`를 Query 옵션으로 전달합니다. `QueryClient`의 `defaultOptions`에 전달하거나 특정 `useQuery` 훅 인스턴스에 전달하면 됩니다.
  - `defaultOptions`에 이 `persister`를 전달하면 모든 쿼리가 지정한 `storage`에 지속됩니다. 추가로 `filters`를 전달해 범위를 좁힐 수도 있습니다. `persistClient` 플러그인과 달리 전체 쿼리 클라이언트를 단일 항목으로 저장하지 않고, 각 쿼리를 별개로 저장합니다. 키로는 쿼리 해시가 사용됩니다.
  - 단일 `useQuery` 훅에 이 `persister`를 전달하면 해당 Query만 지속됩니다.
- 참고: `queryClient.setQueryData()` 작업은 지속되지 않습니다. 즉, 낙관적 업데이트를 수행한 뒤 쿼리가 무효화되기 전에 페이지를 새로고침하면 쿼리 데이터에 대한 변경 사항이 사라집니다. https://github.com/TanStack/query/issues/6310 참조

이 방식으로 전체 `QueryClient`를 저장할 필요 없이, 애플리케이션에서 지속할 가치가 있는 것만 선택할 수 있습니다. 각 쿼리는 지연 복원(쿼리가 처음 사용될 때)되고 지속(`queryFn`이 실행될 때마다)되므로 스로틀링할 필요가 없습니다. 쿼리 복원 후에도 `staleTime`이 존중되므로 데이터가 `stale`이면 복원 직후 즉시 다시 가져오고, 데이터가 `fresh`이면 `queryFn`이 실행되지 않습니다.

쿼리를 메모리에서 가비지 컬렉션해도 지속된 데이터에는 **영향이 없습니다**. 즉, 더 **메모리 효율적**이 되기 위해 쿼리를 메모리에 더 짧게 유지할 수 있습니다. 다음에 사용될 때는 다시 영구 저장소에서 복원됩니다.

```tsx
import AsyncStorage from '@react-native-async-storage/async-storage'
import { QueryClient } from '@tanstack/react-query'
import { experimental_createQueryPersister } from '@tanstack/query-persist-client-core'

const persister = experimental_createQueryPersister({
  storage: AsyncStorage,
  maxAge: 1000 * 60 * 60 * 12, // 12 hours
})

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 30, // 30 seconds
      persister: persister.persisterFn,
    },
  },
})
```

### 조정된 기본값

`createPersister` 플러그인은 기술적으로 `queryFn`을 감싸므로 `queryFn`이 실행되지 않으면 복원하지 않습니다. 이런 면에서 Query와 네트워크 사이의 캐시 계층처럼 동작합니다. 따라서 퍼시스터를 사용하면 `networkMode` 기본값이 `'offlineFirst'`로 설정되어, 네트워크 연결이 없어도 영구 저장소에서 복원이 가능합니다.

## 추가 유틸리티

`experimental_createQueryPersister`를 호출하면 구현을 쉽게 돕기 위해 `persisterFn` 외에도 추가 유틸리티가 반환됩니다.

### `persistQueryByKey(queryKey: QueryKey, queryClient: QueryClient): Promise<void>`

이 함수는 퍼시스터를 생성할 때 정의한 키로 `Query`를 스토리지에 저장합니다. 무효화를 기다리지 않고 `setQueryData`와 함께 사용해 낙관적 업데이트를 스토리지에 지속할 수 있습니다.

```tsx
const persister = experimental_createQueryPersister({
  storage: AsyncStorage,
  maxAge: 1000 * 60 * 60 * 12, // 12 hours
})

const queryClient = useQueryClient()

useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    ...
    // Optimistically update to the new value
    queryClient.setQueryData(['todos'], (old) => [...old, newTodo])
    // And persist it to storage
    persister.persistQueryByKey(['todos'], queryClient)
    ...
  },
})
```

### `retrieveQuery<T>(queryHash: string): Promise<T | undefined>`

이 함수는 `queryHash`로 지속된 쿼리를 가져오려고 시도합니다. `query`가 `expired`, `busted`, `malformed` 상태라면 대신 스토리지에서 제거되며 `undefined`가 반환됩니다.

### `persisterGc(): Promise<void>`

이 함수는 스토리지에서 `expired`, `busted`, `malformed` 항목을 간헐적으로 정리할 때 사용할 수 있습니다.

이 함수가 작동하려면 스토리지가 `key-value tuple array`를 반환하는 `entries` 메서드를 제공해야 합니다. 예를 들어 `localStorage`의 경우 `Object.entries(localStorage)`, `idb-keyval`의 경우 `entries`가 해당합니다.

### `restoreQueries(queryClient: QueryClient, filters): Promise<void>`

이 함수는 현재 퍼시스터에 저장된 쿼리를 복원할 때 사용할 수 있습니다. 예를 들어 앱이 오프라인 모드로 시작할 때나 이전 세션의 전체 또는 특정 데이터를 중간 `loading` 상태 없이 바로 사용할 수 있게 하고 싶을 때 사용할 수 있습니다.

필터 객체는 다음 속성을 지원합니다.

- `queryKey?: QueryKey`
  - 일치시킬 쿼리 키를 지정하려면 이 속성을 설정합니다.
- `exact?: boolean`
  - 쿼리 키를 포함 검색하고 싶지 않다면 `exact: true` 옵션을 전달해 정확히 일치하는 쿼리만 반환하도록 할 수 있습니다.

이 함수가 작동하려면 스토리지가 `key-value tuple array`를 반환하는 `entries` 메서드를 제공해야 합니다. 예를 들어 `localStorage`의 경우 `Object.entries(localStorage)`, `idb-keyval`의 경우 `entries`가 해당합니다.

## API

### `experimental_createQueryPersister`

```tsx
experimental_createQueryPersister(options: StoragePersisterOptions)
```

#### `Options`

```tsx
export interface StoragePersisterOptions {
  /** The storage client used for setting and retrieving items from cache.
   * For SSR pass in `undefined`.
   */
  storage: AsyncStorage | Storage | undefined | null
  /**
   * How to serialize the data to storage.
   * @default `JSON.stringify`
   */
  serialize?: (persistedQuery: PersistedQuery) => string
  /**
   * How to deserialize the data from storage.
   * @default `JSON.parse`
   */
  deserialize?: (cachedString: string) => PersistedQuery
  /**
   * A unique string that can be used to forcefully invalidate existing caches,
   * if they do not share the same buster string
   */
  buster?: string
  /**
   * The max-allowed age of the cache in milliseconds.
   * If a persisted cache is found that is older than this
   * time, it will be discarded
   * @default 24 hours
   */
  maxAge?: number
  /**
   * Prefix to be used for storage key.
   * Storage key is a combination of prefix and query hash in a form of `prefix-queryHash`.
   */
  prefix?: string
  /**
   * If set to `true`, the query will refetch on successful query restoration if the data is stale.
   * If set to `false`, the query will not refetch on successful query restoration.
   * If set to `'always'`, the query will always refetch on successful query restoration.
   * Defaults to `true`.
   */
  refetchOnRestore?: boolean | 'always'
  /**
   * Filters to narrow down which Queries should be persisted.
   */
  filters?: QueryFilters
}

interface AsyncStorage<TStorageValue = string> {
  getItem: (key: string) => MaybePromise<TStorageValue | undefined | null>
  setItem: (key: string, value: TStorageValue) => MaybePromise<unknown>
  removeItem: (key: string) => MaybePromise<void>
  entries?: () => MaybePromise<Array<[key: string, value: TStorageValue]>>
}
```

기본 옵션은 다음과 같습니다.

```tsx
{
  prefix = 'tanstack-query',
  maxAge = 1000 * 60 * 60 * 24,
  serialize = JSON.stringify,
  deserialize = JSON.parse,
  refetchOnRestore = true,
}
```

