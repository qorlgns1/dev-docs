---
title: 'hydration'
description: '는 의 고정된 표현을 만들어  또는 로 다시 하이드레이션할 수 있게 합니다. 이는 서버에서 클라이언트로 미리 가져온 쿼리를 전달하거나 로컬 스토리지 등 영구 저장소에 쿼리를 보존할 때 유용합니다. 기본적으로 현재 성공한 쿼리만 포함됩니다.'
---

# hydration

## `dehydrate`

`dehydrate`는 `cache`의 고정된 표현을 만들어 `HydrationBoundary` 또는 `hydrate`로 다시 하이드레이션할 수 있게 합니다. 이는 서버에서 클라이언트로 미리 가져온 쿼리를 전달하거나 로컬 스토리지 등 영구 저장소에 쿼리를 보존할 때 유용합니다. 기본적으로 현재 성공한 쿼리만 포함됩니다.

```tsx
import { dehydrate } from '@tanstack/react-query'

const dehydratedState = dehydrate(queryClient, {
  shouldDehydrateQuery,
  shouldDehydrateMutation,
})
```

**옵션**

- `client: QueryClient`
  - **필수**
  - 하이드레이션을 위해 비워 둘 `queryClient`
- `options: DehydrateOptions`
  - 선택 사항
  - `shouldDehydrateMutation: (mutation: Mutation) => boolean`
    - 선택 사항
    - 변이를 디하이드레이션할지 여부
    - 캐시에 있는 각 변이에 대해 호출됩니다
      - 이 변이를 디하이드레이션에 포함하려면 `true`, 아니면 `false`를 반환
    - 기본값은 일시 중단된 변이만 포함
    - 기본 동작을 유지하면서 함수를 확장하고 싶다면 `defaultShouldDehydrateMutation`을 가져와 반환문에서 실행
  - `shouldDehydrateQuery: (query: Query) => boolean`
    - 선택 사항
    - 쿼리를 디하이드레이션할지 여부
    - 캐시에 있는 각 쿼리에 대해 호출됩니다
      - 이 쿼리를 디하이드레이션에 포함하려면 `true`, 아니면 `false`를 반환
    - 기본값은 성공한 쿼리만 포함
    - 기본 동작을 유지하면서 함수를 확장하고 싶다면 `defaultShouldDehydrateQuery`를 가져와 반환문에서 실행
  - `serializeData?: (data: any) => any` 디하이드레이션 중 데이터를 변환(직렬화)하는 함수
  - `shouldRedactErrors?: (error: unknown) => boolean`
    - 선택 사항
    - 디하이드레이션 중 서버의 오류를 숨길지 여부
    - 캐시에 있는 각 오류에 대해 호출됩니다
      - 이 오류를 숨기려면 `true`, 아니면 `false`를 반환
    - 기본값은 모든 오류를 숨김

**반환값**

- `dehydratedState: DehydratedState`
  - 나중에 `queryClient`를 하이드레이션하는 데 필요한 모든 것이 포함됩니다
  - 이 응답의 정확한 형식에 의존해서는 안 됩니다. 공개 API가 아니며 언제든지 변경될 수 있습니다
  - 결과는 직렬화된 형태가 아니므로 필요하다면 직접 직렬화해야 합니다

### 제한 사항

일부 스토리지 시스템(예: 브라우저 [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API))은 JSON 직렬화 가능한 값만 허용합니다. JSON으로 자동 직렬화되지 않는 값(`Error`, `undefined` 등)을 디하이드레이션해야 한다면 직접 직렬화해야 합니다. 기본적으로 성공한 쿼리만 포함되므로 `Errors`까지 포함하려면 `shouldDehydrateQuery`를 제공해야 하며, 예시는 다음과 같습니다:

```tsx
// server
const state = dehydrate(client, { shouldDehydrateQuery: () => true }) // to also include Errors
const serializedState = mySerialize(state) // transform Error instances to objects

// client
const state = myDeserialize(serializedState) // transform objects back to Error instances
hydrate(client, state)
```

## `hydrate`

`hydrate`는 이전에 디하이드레이션된 상태를 `cache`에 추가합니다.

```tsx
import { hydrate } from '@tanstack/react-query'

hydrate(queryClient, dehydratedState, options)
```

**옵션**

- `client: QueryClient`
  - **필수**
  - 상태를 하이드레이션할 `queryClient`
- `dehydratedState: DehydratedState`
  - **필수**
  - 클라이언트에 하이드레이션할 상태
- `options: HydrateOptions`
  - 선택 사항
  - `defaultOptions: DefaultOptions`
    - 선택 사항
    - `mutations: MutationOptions` 하이드레이션된 변이에 사용할 기본 변이 옵션
    - `queries: QueryOptions` 하이드레이션된 쿼리에 사용할 기본 쿼리 옵션
    - `deserializeData?: (data: any) => any` 캐시에 넣기 전에 데이터를 변환(역직렬화)하는 함수
  - `queryClient?: QueryClient`
    - 커스텀 QueryClient를 사용하려면 지정합니다. 그렇지 않으면 가장 가까운 컨텍스트의 클라이언트가 사용됩니다

### 제한 사항

하이드레이션하려는 쿼리가 이미 queryCache에 있으면, `hydrate`는 캐시에 있는 데이터보다 최신 데이터일 때만 덮어씁니다. 그렇지 않으면 적용되지 않습니다.

[//]: # 'HydrationBoundary'

## `HydrationBoundary`

`HydrationBoundary`는 이전에 디하이드레이션된 상태를 `useQueryClient()`가 반환하는 `queryClient`에 추가합니다. 클라이언트에 이미 데이터가 있는 경우, 새 쿼리는 업데이트 타임스탬프를 기준으로 지능적으로 병합됩니다.

```tsx
import { HydrationBoundary } from '@tanstack/react-query'

function App() {
  return <HydrationBoundary state={dehydratedState}>...</HydrationBoundary>
}
```

> 참고: `HydrationBoundary`에서는 `queries`만 디하이드레이션할 수 있습니다.

**옵션**

- `state: DehydratedState`
  - 하이드레이션할 상태
- `options: HydrateOptions`
  - 선택 사항
  - `defaultOptions: QueryOptions`
    - 하이드레이션된 쿼리에 사용할 기본 쿼리 옵션
  - `queryClient?: QueryClient`
    - 커스텀 QueryClient를 사용하려면 지정합니다. 그렇지 않으면 가장 가까운 컨텍스트의 클라이언트가 사용됩니다

[//]: # 'HydrationBoundary'

