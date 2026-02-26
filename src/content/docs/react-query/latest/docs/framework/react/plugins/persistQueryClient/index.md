---
title: 'persistQueryClient'
description: '이는 나중에 사용할 수 있도록 queryClient를 저장하는 “persister”와 상호작용하기 위한 유틸리티 세트입니다. 서로 다른 persister를 사용하여 클라이언트와 캐시를 다양한 스토리지 계층에 저장할 수 있습니다.'
---

# persistQueryClient

이는 나중에 사용할 수 있도록 queryClient를 저장하는 “persister”와 상호작용하기 위한 유틸리티 세트입니다. 서로 다른 **persister**를 사용하여 클라이언트와 캐시를 다양한 스토리지 계층에 저장할 수 있습니다.

## Build Persisters

- [createSyncStoragePersister](https://tanstack.com/query/latest/docs/framework/react/plugins/createSyncStoragePersister.md)
- [createAsyncStoragePersister](https://tanstack.com/query/latest/docs/framework/react/plugins/createAsyncStoragePersister.md)
- [create a custom persister](#persisters)

## How It Works

**중요** - 지속(persist)이 제대로 작동하려면, 수화(hydration) 중 기본값을 재정의하도록 `QueryClient`에 `gcTime` 값을 전달하는 것이 좋습니다(위 예시 참고).

`QueryClient` 인스턴스를 생성할 때 설정하지 않으면, 수화 시 기본적으로 `300000`(5분)으로 설정되며 저장된 캐시는 5분 동안 활동이 없으면 폐기됩니다. 이것이 기본 가비지 컬렉션 동작입니다.

이 값은 persistQueryClient의 `maxAge` 옵션과 같거나 더 커야 합니다. 예를 들어 `maxAge`가 24시간(기본값)이라면 `gcTime`도 24시간 이상이어야 합니다. 만약 `gcTime`이 `maxAge`보다 작으면, 가비지 컬렉션이 더 일찍 실행되어 저장된 캐시가 예상보다 빨리 폐기됩니다.

가비지 컬렉션 동작을 완전히 비활성화하려면 `Infinity`를 전달할 수도 있습니다.

JavaScript 한계 때문에 허용되는 최대 `gcTime`은 약 [24일](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout#maximum_delay_value)이지만, [timeoutManager.setTimeoutProvider](https://tanstack.com/query/latest/docs/reference/timeoutManager.md#timeoutmanagersettimeoutprovider)를 사용하여 이 제한을 우회할 수 있습니다.

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
})
```

### Cache Busting

애플리케이션이나 데이터가 즉시 모든 캐시된 데이터를 무효화할 정도로 변경될 때가 있습니다. 이런 상황에서 `buster` 문자열 옵션을 전달할 수 있습니다. 저장된 캐시에서 해당 buster 문자열을 찾지 못하면 캐시는 폐기됩니다. 다음 함수들이 이 옵션을 지원합니다:

```tsx
persistQueryClient({ queryClient, persister, buster: buildHash })
persistQueryClientSave({ queryClient, persister, buster: buildHash })
persistQueryClientRestore({ queryClient, persister, buster: buildHash })
```

### Removal

데이터가 아래 중 하나로 판별되면:

1. 만료됨(`maxAge` 참조)
2. 손상됨(`buster` 참조)
3. 오류(ex: `throws ...`)
4. 비어 있음(ex: `undefined`)

persister `removeClient()`가 호출되고 캐시는 즉시 폐기됩니다.

## API

### `persistQueryClientSave`

- 제공한 persister가 쿼리/뮤테이션을 [`dehydrated`](https://tanstack.com/query/latest/docs/framework/react/reference/hydration.md#dehydrate) 상태로 저장합니다.
- `createSyncStoragePersister`와 `createAsyncStoragePersister`는 비용이 큰 쓰기를 줄이기 위해 이 동작을 최대 1초에 한 번만 수행하도록 스로틀합니다. 스로틀 타이밍을 커스터마이즈하는 방법은 해당 문서를 확인하세요.

선택한 시점에 명시적으로 캐시를 지속시키는 데 사용할 수 있습니다.

```tsx
persistQueryClientSave({
  queryClient,
  persister,
  buster = '',
  dehydrateOptions = undefined,
})
```

### `persistQueryClientSubscribe`

`queryClient` 캐시가 변경될 때마다 `persistQueryClientSave`를 실행합니다. 예를 들어 사용자가 로그인하면서 “Remember me”를 체크할 때 `subscribe`를 초기화할 수 있습니다.

- `unsubscribe` 함수를 반환하며, 이를 사용해 모니터를 중단하고 지속된 캐시 업데이트를 멈출 수 있습니다.
- `unsubscribe` 이후에 지속된 캐시를 지우고 싶다면, 새로운 `buster`를 `persistQueryClientRestore`에 전달하여 persister의 `removeClient` 함수를 트리거하고 지속된 캐시를 폐기할 수 있습니다.

```tsx
persistQueryClientSubscribe({
  queryClient,
  persister,
  buster = '',
  dehydrateOptions = undefined,
})
```

### `persistQueryClientRestore`

- persister에 지속된 dehydrated 쿼리/뮤테이션 캐시를 전달된 query client의 쿼리 캐시에 다시 [`hydrate`](https://tanstack.com/query/latest/docs/framework/react/reference/hydration.md#hydrate)하려고 시도합니다.
- `maxAge`보다 오래된 캐시(기본값 24시간)를 발견하면 폐기합니다. 이 타이밍은 필요에 따라 조정할 수 있습니다.

원하는 시점에 캐시를 복원하는 데 사용할 수 있습니다.

```tsx
persistQueryClientRestore({
  queryClient,
  persister,
  maxAge = 1000 * 60 * 60 * 24, // 24 hours
  buster = '',
  hydrateOptions = undefined,
})
```

### `persistQueryClient`

다음 작업을 수행합니다:

1. 지속된 캐시를 즉시 복원합니다([`persistQueryClientRestore`](#persistqueryclientrestore) 참조)
2. 쿼리 캐시에 구독하고 `unsubscribe` 함수를 반환합니다([`persistQueryClientSubscribe`](#persistqueryclientsubscribe) 참조).

이 기능은 3.x 버전에서 유지되었습니다.

```tsx
persistQueryClient({
  queryClient,
  persister,
  maxAge = 1000 * 60 * 60 * 24, // 24 hours
  buster = '',
  hydrateOptions = undefined,
  dehydrateOptions = undefined,
})
```

### `Options`

사용 가능한 모든 옵션은 다음과 같습니다:

```tsx
interface PersistQueryClientOptions {
  /** The QueryClient to persist */
  queryClient: QueryClient
  /** The Persister interface for storing and restoring the cache
   * to/from a persisted location */
  persister: Persister
  /** The max-allowed age of the cache in milliseconds.
   * If a persisted cache is found that is older than this
   * time, it will be **silently** discarded
   * (defaults to 24 hours) */
  maxAge?: number
  /** A unique string that can be used to forcefully
   * invalidate existing caches if they do not share the same buster string */
  buster?: string
  /** The options passed to the hydrate function
   * Not used on `persistQueryClientSave` or `persistQueryClientSubscribe` */
  hydrateOptions?: HydrateOptions
  /** The options passed to the dehydrate function
   * Not used on `persistQueryClientRestore` */
  dehydrateOptions?: DehydrateOptions
}
```

실제로 세 가지 인터페이스가 있습니다:

- `PersistedQueryClientSaveOptions`는 `persistQueryClientSave`와 `persistQueryClientSubscribe`에 사용됩니다(`hydrateOptions`는 사용하지 않음).
- `PersistedQueryClientRestoreOptions`는 `persistQueryClientRestore`에 사용됩니다(`dehydrateOptions`는 사용하지 않음).
- `PersistQueryClientOptions`는 `persistQueryClient`에 사용됩니다.

## Usage with React

[persistQueryClient](#persistQueryClient)는 캐시를 복원하려 시도하고 자동으로 추가 변경 사항을 구독하여, 클라이언트를 제공된 스토리지와 동기화합니다.

그러나 모든 persister는 본질적으로 비동기이므로, App을 복원하는 동안 렌더링하면 쿼리가 마운트되면서 동시에 fetch를 수행할 때 경쟁 상태가 발생할 수 있습니다.

또한 React 컴포넌트 생명주기 밖에서 변경 사항에 구독하면 구독을 해제할 방법이 없습니다:

```tsx
// 🚨 never unsubscribes from syncing
persistQueryClient({
  queryClient,
  persister: localStoragePersister,
})

// 🚨 happens at the same time as restoring
ReactDOM.createRoot(rootElement).render(<App />)
```

### PersistQueryClientProvider

이 경우 `PersistQueryClientProvider`를 사용할 수 있습니다. React 컴포넌트 생명주기에 따라 올바르게 구독/구독 해제를 보장하고, 복원 중에는 쿼리가 fetch를 시작하지 않도록 합니다. 쿼리는 여전히 렌더링되지만, 데이터가 복원될 때까지 `fetchingState: 'idle'` 상태로 유지됩니다. 이후, 복원된 데이터가 충분히 _fresh_ 하면 refetch하지 않고, _initialData_ 역시 존중됩니다. 일반 [QueryClientProvider](https://tanstack.com/query/latest/docs/framework/react/reference/QueryClientProvider.md) 대신 사용할 수 있습니다:

```tsx
import { PersistQueryClientProvider } from '@tanstack/react-query-persist-client'
import { createAsyncStoragePersister } from '@tanstack/query-async-storage-persister'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
})

const persister = createAsyncStoragePersister({
  storage: window.localStorage,
})

ReactDOM.createRoot(rootElement).render(
  <PersistQueryClientProvider
    client={queryClient}
    persistOptions={{ persister }}
  >
    <App />
  </PersistQueryClientProvider>,
)
```

#### Props

`PersistQueryClientProvider`는 [QueryClientProvider](https://tanstack.com/query/latest/docs/framework/react/reference/QueryClientProvider.md)와 동일한 props를 받고, 추가로 아래를 지원합니다:

- `persistOptions: PersistQueryClientOptions`
  - [persistQueryClient](#persistqueryclient)에 전달할 수 있는 모든 [옵션](#options)에서 QueryClient 자체를 제외한 것
- `onSuccess?: () => Promise<unknown> | unknown`
  - 선택 사항
  - 초기 복원이 완료되면 호출됩니다
  - [resumePausedMutations](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientresumepausedmutations)에 사용할 수 있습니다
  - Promise를 반환하면 해당 Promise가 완료될 때까지 대기하며, 그동안 복원이 진행 중으로 간주됩니다
- `onError?: () => Promise<unknown> | unknown`
  - 선택 사항
  - 복원 중 오류가 발생하면 호출됩니다
  - Promise를 반환하면 완료될 때까지 대기합니다

### useIsRestoring

`PersistQueryClientProvider`를 사용할 때, 복원이 진행 중인지 확인하려면 `useIsRestoring` 훅도 함께 사용할 수 있습니다. `useQuery` 등도 내부적으로 이를 확인하여 복원과 쿼리 마운트 사이의 경쟁 상태를 피합니다.

## Persisters

### Persisters Interface

Persister는 다음 인터페이스를 가집니다:

```tsx
export interface Persister {
  persistClient(persistClient: PersistedClient): Promisable<void>
  restoreClient(): Promisable<PersistedClient | undefined>
  removeClient(): Promisable<void>
}
```

Persisted Client 항목은 다음 인터페이스를 가집니다:

```tsx
export interface PersistedClient {
  timestamp: number
  buster: string
  clientState: DehydratedState
}
```

다음처럼 가져와서(persistor를 구축하기 위해) 사용할 수 있습니다:

```tsx
import {
  PersistedClient,
  Persister,
} from '@tanstack/react-query-persist-client'
```

### Building A Persister

원하는 방식으로 지속할 수 있습니다. 다음은 [Indexed DB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) persister를 구축하는 예시입니다. `Web Storage API`와 비교하면 Indexed DB는 더 빠르고, 5MB 이상을 저장할 수 있으며 직렬화가 필요 없습니다. 즉, `Date`, `File`과 같은 JavaScript 네이티브 타입을 그대로 저장할 수 있습니다.

```tsx
import { get, set, del } from 'idb-keyval'
import {
  PersistedClient,
  Persister,
} from '@tanstack/react-query-persist-client'

/**
 * Creates an Indexed DB persister
 * @see https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
 */
export function createIDBPersister(idbValidKey: IDBValidKey = 'reactQuery') {
  return {
    persistClient: async (client: PersistedClient) => {
      await set(idbValidKey, client)
    },
    restoreClient: async () => {
      return await get<PersistedClient>(idbValidKey)
    },
    removeClient: async () => {
      await del(idbValidKey)
    },
  } satisfies Persister
}
```

