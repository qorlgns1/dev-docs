---
title: 'createAsyncStoragePersister'
description: '이 유틸리티는 별도 패키지로 제공되며 에서 임포트할 수 있습니다.'
---

# createAsyncStoragePersister

## 설치

이 유틸리티는 별도 패키지로 제공되며 `'@tanstack/query-async-storage-persister'`에서 임포트할 수 있습니다.

```bash
npm install @tanstack/query-async-storage-persister @tanstack/react-query-persist-client
```

또는

```bash
pnpm add @tanstack/query-async-storage-persister @tanstack/react-query-persist-client
```

또는

```bash
yarn add @tanstack/query-async-storage-persister @tanstack/react-query-persist-client
```

또는

```bash
bun add @tanstack/query-async-storage-persister @tanstack/react-query-persist-client
```

## 사용법

- `createAsyncStoragePersister` 함수를 임포트합니다.
- 새 asyncStoragePersister를 생성합니다.
  - `AsyncStorage` 인터페이스를 준수하는 어떤 `storage`든 전달할 수 있으며, 아래 예제에서는 React Native의 async-storage를 사용합니다.
  - `window.localstorage`처럼 동기적으로 읽고 쓰는 스토리지 역시 `AsyncStorage` 인터페이스를 준수하므로 `createAsyncStoragePersister`와 함께 사용할 수 있습니다.
- [`PersistQueryClientProvider`](https://tanstack.com/query/latest/docs/framework/react/plugins/persistQueryClient.md#persistqueryclientprovider) 컴포넌트로 앱을 래핑합니다.

```tsx
import AsyncStorage from '@react-native-async-storage/async-storage'
import { QueryClient } from '@tanstack/react-query'
import { PersistQueryClientProvider } from '@tanstack/react-query-persist-client'
import { createAsyncStoragePersister } from '@tanstack/query-async-storage-persister'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
})

const asyncStoragePersister = createAsyncStoragePersister({
  storage: AsyncStorage,
})

const Root = () => (
  <PersistQueryClientProvider
    client={queryClient}
    persistOptions={{ persister: asyncStoragePersister }}
  >
    <App />
  </PersistQueryClientProvider>
)

export default Root
```

## 재시도

재시도 동작은 [SyncStoragePersister](https://tanstack.com/query/latest/docs/framework/react/plugins/createSyncStoragePersister.md)와 동일하지만, 비동기로도 수행될 수 있습니다. 미리 정의된 모든 재시도 핸들러를 그대로 사용할 수 있습니다.

## API

### `createAsyncStoragePersister`

이 함수를 호출해, 나중에 `persistQueryClient`와 함께 사용할 asyncStoragePersister를 생성합니다.

```tsx
createAsyncStoragePersister(options: CreateAsyncStoragePersisterOptions)
```

### `Options`

```tsx
interface CreateAsyncStoragePersisterOptions {
  /** The storage client used for setting an retrieving items from cache */
  storage: AsyncStorage | undefined | null
  /** The key to use when storing the cache to localStorage */
  key?: string
  /** To avoid localStorage spamming,
   * pass a time in ms to throttle saving the cache to disk */
  throttleTime?: number
  /** How to serialize the data to storage */
  serialize?: (client: PersistedClient) => string
  /** How to deserialize the data from storage */
  deserialize?: (cachedString: string) => PersistedClient
  /** How to retry persistence on error **/
  retry?: AsyncPersistRetryer
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
  key = `REACT_QUERY_OFFLINE_CACHE`,
  throttleTime = 1000,
  serialize = JSON.stringify,
  deserialize = JSON.parse,
}
```

