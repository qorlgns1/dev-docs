---
title: 'createSyncStoragePersister'
description: "이 플러그인은 더 이상 사용되지 않으며 다음 메이저 버전에서 제거될 예정입니다. 대신 '@tanstack/query-async-storage-persister'를 그대로 사용하면 됩니다."
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/plugins/createSyncStoragePersister

# createSyncStoragePersister

## Deprecated

이 플러그인은 더 이상 사용되지 않으며 다음 메이저 버전에서 제거될 예정입니다. 대신 ['@tanstack/query-async-storage-persister'](https://tanstack.com/query/latest/docs/framework/react/plugins/createAsyncStoragePersister.md)를 그대로 사용하면 됩니다.

## Installation

이 유틸리티는 별도 패키지로 제공되며 `'@tanstack/query-sync-storage-persister'`에서 import 할 수 있습니다.

```bash
npm install @tanstack/query-sync-storage-persister @tanstack/react-query-persist-client
```

or

```bash
pnpm add @tanstack/query-sync-storage-persister @tanstack/react-query-persist-client
```

or

```bash
yarn add @tanstack/query-sync-storage-persister @tanstack/react-query-persist-client
```

or

```bash
bun add @tanstack/query-sync-storage-persister @tanstack/react-query-persist-client
```

## Usage

- `createSyncStoragePersister` 함수를 import 합니다.
- 새로운 syncStoragePersister를 생성합니다.
- [`persistQueryClient`](https://tanstack.com/query/latest/docs/framework/react/plugins/persistQueryClient.md) 함수에 전달합니다.

```tsx
import { persistQueryClient } from '@tanstack/react-query-persist-client'
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
})

const localStoragePersister = createSyncStoragePersister({
  storage: window.localStorage,
})
// const sessionStoragePersister = createSyncStoragePersister({ storage: window.sessionStorage })

persistQueryClient({
  queryClient,
  persister: localStoragePersister,
})
```

## Retries

스토리지에서 사용 가능한 공간을 초과하는 등 다양한 이유로 퍼시스턴스가 실패할 수 있습니다. 퍼시스터에 `retry` 함수를 제공하면 오류를 우아하게 처리할 수 있습니다.

retry 함수는 저장하려던 `persistedClient`, `error`, `errorCount`를 입력으로 받습니다. _새로운_ `PersistedClient`를 반환해야 하며, 이를 다시 퍼시스트하려고 시도합니다. _undefined_ 를 반환하면 추가 시도는 이루어지지 않습니다.

```tsx
export type PersistRetryer = (props: {
  persistedClient: PersistedClient
  error: Error
  errorCount: number
}) => PersistedClient | undefined
```

### Predefined strategies

기본적으로는 retry가 발생하지 않습니다. 미리 정의된 전략을 사용해 retry를 처리할 수 있으며, `from '@tanstack/react-query-persist-client'`에서 import 할 수 있습니다.

- `removeOldestQuery`
  - 가장 오래된 쿼리를 제거한 새로운 `PersistedClient`를 반환합니다.

```tsx
const localStoragePersister = createSyncStoragePersister({
  storage: window.localStorage,
  retry: removeOldestQuery,
})
```

## API

### `createSyncStoragePersister`

이 함수를 호출해 나중에 `persistQueryClient`와 함께 사용할 syncStoragePersister를 생성합니다.

```tsx
createSyncStoragePersister(options: CreateSyncStoragePersisterOptions)
```

### `Options`

```tsx
interface CreateSyncStoragePersisterOptions {
  /** The storage client used for setting an retrieving items from cache (window.localStorage or window.sessionStorage) */
  storage: Storage | undefined | null
  /** The key to use when storing the cache */
  key?: string
  /** To avoid spamming,
   * pass a time in ms to throttle saving the cache to disk */
  throttleTime?: number
  /** How to serialize the data to storage */
  serialize?: (client: PersistedClient) => string
  /** How to deserialize the data from storage */
  deserialize?: (cachedString: string) => PersistedClient
  /** How to retry persistence on error **/
  retry?: PersistRetryer
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

#### `serialize` 및 `deserialize` 옵션

`localStorage`에 저장할 수 있는 데이터 양에는 제한이 있습니다. `localStorage`에 더 많은 데이터를 저장해야 한다면 [lz-string](https://github.com/pieroxy/lz-string/) 같은 라이브러리를 사용해 데이터를 압축/해제하도록 `serialize`와 `deserialize` 함수를 재정의할 수 있습니다.

```tsx
import { QueryClient } from '@tanstack/react-query'
import { persistQueryClient } from '@tanstack/react-query-persist-client'
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister'

import { compress, decompress } from 'lz-string'

const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: Infinity } },
})

persistQueryClient({
  queryClient: queryClient,
  persister: createSyncStoragePersister({
    storage: window.localStorage,
    serialize: (data) => compress(JSON.stringify(data)),
    deserialize: (data) => JSON.parse(decompress(data)),
  }),
  maxAge: Infinity,
})
```

