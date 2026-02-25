---
title: 'React Query 4로 마이그레이션하기'
description: 'Using add-doc skill for translation.'
---

Using add-doc skill for translation.

# React Query 4로 마이그레이션하기

## 주요 변경 사항

v4는 메이저 버전이므로 알아두어야 할 주요 변경 사항이 있습니다.

### react-query가 @tanstack/react-query로 변경됨

의존성을 제거/설치하고 import를 변경해야 합니다.

```
npm uninstall react-query
npm install @tanstack/react-query
npm install @tanstack/react-query-devtools
```

```tsx
- import { useQuery } from 'react-query' // [!code --]
- import { ReactQueryDevtools } from 'react-query/devtools' // [!code --]

+ import { useQuery } from '@tanstack/react-query' // [!code ++]
+ import { ReactQueryDevtools } from '@tanstack/react-query-devtools' // [!code ++]
```

#### Codemod

import 마이그레이션을 쉽게 하기 위해 v4에는 codemod가 포함되어 있습니다.

> codemod는 주요 변경 사항을 마이그레이션하도록 돕기 위한 최선의 시도입니다. 생성된 코드를 반드시 꼼꼼히 검토하세요! 또한 codemod가 찾을 수 없는 엣지 케이스가 있으므로 로그 출력도 주의 깊게 확인해 주세요.

다음 명령 중 하나(또는 둘 다)를 사용해 손쉽게 적용할 수 있습니다.

`.js` 또는 `.jsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift ./path/to/src/ \
  --extensions=js,jsx \
  --transform=./node_modules/@tanstack/react-query/codemods/v4/replace-import-specifier.js
```

`.ts` 또는 `.tsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift ./path/to/src/ \
  --extensions=ts,tsx \
  --parser=tsx \
  --transform=./node_modules/@tanstack/react-query/codemods/v4/replace-import-specifier.js
```

`TypeScript`의 경우 파서를 반드시 `tsx`로 지정해야 합니다. 그렇지 않으면 codemod가 제대로 적용되지 않습니다!

**참고:** codemod를 적용하면 코드 포매팅이 깨질 수 있으니, 적용 후 `prettier` 및/또는 `eslint` 실행을 잊지 마세요!

**참고:** codemod는 import만 변경합니다. devtools 패키지는 별도로 직접 설치해야 합니다.

### Query Key(및 Mutation Key)는 배열이어야 함

v3에서는 Query 및 Mutation Key를 문자열 또는 배열로 사용할 수 있었습니다. 내부적으로 React Query는 항상 배열 키만 사용했고, 이를 간혹 외부에 노출하기도 했습니다. 예를 들어 `queryFn`에서는 [기본 Query 함수](https://tanstack.com/query/latest/docs/framework/react/guides/default-query-function.md)를 쉽게 사용하도록 키를 항상 배열로 받았습니다.

하지만 이 개념을 모든 API에 일관되게 적용하지는 못했습니다. 예를 들어 [Query Filter](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md)에서 `predicate` 함수를 사용할 때는 원본 Query Key를 받았습니다. 문자열과 배열이 섞인 Query Key를 쓰면 이런 함수들을 다루기 어려웠고, 전역 콜백에서도 마찬가지였습니다.

모든 API를 일관되게 만들기 위해 모든 키를 배열로만 사용하기로 했습니다.

```tsx
;-useQuery('todos', fetchTodos) + // [!code --]
  useQuery(['todos'], fetchTodos) // [!code ++]
```

#### Codemod

이 마이그레이션을 쉽게 하려고 codemod를 제공합니다.

> codemod는 주요 변경 사항을 마이그레이션하도록 돕기 위한 최선의 시도입니다. 생성된 코드를 반드시 꼼꼼히 검토하세요! 또한 codemod가 찾을 수 없는 엣지 케이스가 있으므로 로그 출력도 주의 깊게 확인해 주세요.

다음 명령 중 하나(또는 둘 다)를 사용해 손쉽게 적용할 수 있습니다.

`.js` 또는 `.jsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift ./path/to/src/ \
  --extensions=js,jsx \
  --transform=./node_modules/@tanstack/react-query/codemods/v4/key-transformation.js
```

`.ts` 또는 `.tsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift ./path/to/src/ \
  --extensions=ts,tsx \
  --parser=tsx \
  --transform=./node_modules/@tanstack/react-query/codemods/v4/key-transformation.js
```

`TypeScript`의 경우 파서를 반드시 `tsx`로 지정해야 합니다. 그렇지 않으면 codemod가 제대로 적용되지 않습니다!

**참고:** codemod를 적용하면 코드 포매팅이 깨질 수 있으니, 적용 후 `prettier` 및/또는 `eslint` 실행을 잊지 마세요!

### idle 상태가 제거됨

더 나은 오프라인 지원을 위한 새로운 [fetchStatus](https://tanstack.com/query/latest/docs/framework/react/guides/queries.md#fetchstatus)가 도입되면서 `idle` 상태가 의미를 잃었습니다. `fetchStatus: 'idle'`이 동일한 상태를 더 명확하게 표현하기 때문입니다. 자세한 내용은 [왜 두 가지 상태인가](https://tanstack.com/query/latest/docs/framework/react/guides/queries.md#why-two-different-states)를 참고하세요.

이는 주로 아직 `data`가 없는 `disabled` 쿼리에 영향을 줍니다. 이전에는 해당 쿼리가 `idle` 상태였습니다.

```tsx
- status: 'idle' // [!code --]
+ status: 'loading'  // [!code ++]
+ fetchStatus: 'idle' // [!code ++]
```

또한 [의존 쿼리 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/dependent-queries.md)도 확인하세요.

#### disabled 쿼리

이 변경으로 인해 `disabled` 쿼리(일시 비활성화 포함)는 `loading` 상태로 시작합니다. 로딩 스피너를 표시할 시점을 알기 쉽게 하려면 `isLoading` 대신 `isInitialLoading`을 확인하세요.

```tsx
;-isLoading + // [!code --]
  isInitialLoading // [!code ++]
```

[쿼리 비활성화 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/disabling-queries.md#isInitialLoading)도 참고하세요.

### `useQueries`의 새로운 API

이제 `useQueries` 훅은 입력으로 `queries` prop을 가진 객체를 받습니다. `queries` prop의 값은 쿼리 배열이며, 이는 v3에서 `useQueries`에 전달하던 배열과 동일합니다.

```tsx
;-useQueries([
  { queryKey1, queryFn1, options1 },
  { queryKey2, queryFn2, options2 },
]) + // [!code --]
  useQueries({
    queries: [
      { queryKey1, queryFn1, options1 },
      { queryKey2, queryFn2, options2 },
    ],
  }) // [!code ++]
```

### 성공한 쿼리에서 `undefined`는 허용되지 않는 캐시 값

업데이트를 건너뛰기 위해 `undefined`를 반환할 수 있도록 하려면 `undefined`를 캐시 값으로 허용할 수 없습니다. 이는 react-query의 다른 개념과도 일치합니다. 예를 들어 [initialData 함수](https://tanstack.com/query/latest/docs/framework/react/guides/initial-query-data.md#initial-data-function)에서 `undefined`를 반환해도 데이터가 설정되지 않습니다.

또한 `queryFn`에서 로깅을 추가하다 보면 쉽게 `Promise<void>`를 만들 수 있습니다.

```tsx
useQuery(['key'], () =>
  axios.get(url).then((result) => console.log(result.data)),
)
```

이제 타입 레벨에서 금지되며, 런타임에서는 `undefined`가 _실패한 Promise_ 로 변환되어 `error`가 발생하고 개발 모드에서는 콘솔에도 로그가 출력됩니다.

### 기본적으로 쿼리와 뮤테이션은 네트워크 연결이 필요함

온라인/오프라인 지원에 대한 [새 기능 발표](#proper-offline-support)와 [네트워크 모드](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md) 전용 페이지를 읽어 주세요.

React Query는 어떤 Promise 생산자와도 함께 쓸 수 있는 비동기 상태 관리자지만, 대부분 데이터 패칭 라이브러리와 함께 데이터 패칭에 사용됩니다. 그래서 기본적으로 네트워크 연결이 없으면 쿼리와 뮤테이션이 `paused` 상태가 됩니다. 이전 동작으로 돌아가고 싶다면 쿼리와 뮤테이션 모두에 대해 전역으로 `networkMode: offlineFirst`를 설정하세요.

```tsx
new QueryClient({
  defaultOptions: {
    queries: {
      networkMode: 'offlineFirst',
    },
    mutations: {
      networkMode: 'offlineFirst',
    },
  },
})
```

### `notifyOnChangeProps` 속성은 더 이상 `"tracked"` 값을 받지 않음

`notifyOnChangeProps` 옵션은 이제 `"tracked"` 값을 허용하지 않습니다. 대신 `useQuery`가 기본적으로 속성을 추적합니다. `notifyOnChangeProps: "tracked"`를 사용하던 모든 쿼리는 이 옵션을 제거해야 합니다.

v3의 기본 동작처럼 쿼리가 변경될 때마다 리렌더링되도록 우회하고 싶다면, `notifyOnChangeProps`에 `"all"` 값을 전달해 기본 스마트 추적 최적화를 비활성화할 수 있습니다.

### `notifyOnChangePropsExclusion`이 제거됨

v4에서는 `notifyOnChangeProps`의 기본값이 `undefined`가 아니라 v3의 `"tracked"` 동작입니다. 이제 `"tracked"`가 기본이므로 이 설정 옵션은 더 이상 의미가 없습니다.

### `cancelRefetch`의 일관된 동작

`cancelRefetch` 옵션은 쿼리를 명령형으로 패칭하는 모든 함수에 전달할 수 있습니다.

- `queryClient.refetchQueries`
- `queryClient.invalidateQueries`
- `queryClient.resetQueries`
- `useQuery`에서 반환되는 `refetch`
- `useInfiniteQuery`에서 반환되는 `fetchNextPage` 및 `fetchPreviousPage`

`fetchNextPage`와 `fetchPreviousPage`를 제외하면 이 플래그의 기본값이 `false`였는데, 이는 일관되지 않고 문제가 될 수 있었습니다. 예를 들어 뮤테이션 이후 `refetchQueries`나 `invalidateQueries`를 호출할 때, 이전에 실행 중이던 느린 fetch가 있다면 이번 refetch가 건너뛰어져 최신 결과를 얻지 못할 수 있었습니다.

우리는 여러분이 작성한 코드로 쿼리를 적극적으로 다시 패칭한다면 기본적으로 fetch를 재시작해야 한다고 봅니다.

따라서 위에 언급한 모든 메서드에서 이 플래그의 기본값이 이제 _true_ 입니다. 즉, `refetchQueries`를 연달아 두 번 호출하면서 기다리지 않으면 첫 번째 fetch를 취소하고 두 번째로 다시 시작합니다.

```
queryClient.refetchQueries({ queryKey: ['todos'] })
// this will abort the previous refetch and start a new fetch
queryClient.refetchQueries({ queryKey: ['todos'] })
```

이 동작을 원하지 않으면 `cancelRefetch:false`를 명시적으로 전달해 제외할 수 있습니다.

```
queryClient.refetchQueries({ queryKey: ['todos'] })
// this will not abort the previous refetch - it will just be ignored
queryClient.refetchQueries({ queryKey: ['todos'] }, { cancelRefetch: false })
```

> 참고: 쿼리가 마운트되거나 창 포커스 refetch 등으로 자동으로 트리거되는 fetch 동작은 변하지 않았습니다.

### Query Filter

[Query filter](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md)는 특정 조건으로 쿼리를 매칭하는 객체입니다. 과거에는 옵션이 대부분 불리언 플래그 조합이었습니다. 하지만 이 플래그들을 조합하면 모순되는 상태가 생기곤 했습니다. 특히 아래와 같습니다.

```
active?: boolean
  - When set to true it will match active queries.
  - When set to false it will match inactive queries.
inactive?: boolean
  - When set to true it will match inactive queries.
  - When set to false it will match active queries.
```

이 플래그들은 서로 배타적이어서 함께 사용할 때 제대로 동작하지 않습니다. 두 플래그를 모두 `false`로 설정하면 설명상 모든 쿼리에 매칭될 수도, 전혀 매칭되지 않을 수도 있어 의미가 없습니다.

v4에서는 이러한 필터를 하나의 필터로 결합해 의도를 더 명확히 했습니다.

```tsx
- active?: boolean // [!code --]
- inactive?: boolean // [!code --]
+ type?: 'active' | 'inactive' | 'all' // [!code ++]
```

기본값은 `all`이며, `active` 또는 `inactive`만 매칭하도록 선택할 수 있습니다.

#### refetchActive / refetchInactive

[queryClient.invalidateQueries](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientinvalidatequeries)에도 비슷한 플래그 두 개가 있었습니다.

```
refetchActive: Boolean
  - Defaults to true
  - When set to false, queries that match the refetch predicate and are actively being rendered
    via useQuery and friends will NOT be refetched in the background, and only marked as invalid.
refetchInactive: Boolean
  - Defaults to false
  - When set to true, queries that match the refetch predicate and are not being rendered
    via useQuery and friends will be both marked as invalid and also refetched in the background
```

같은 이유로 이들도 통합되었습니다.

```tsx
- refetchActive?: boolean // [!code --]
- refetchInactive?: boolean // [!code --]
+ refetchType?: 'active' | 'inactive' | 'all' | 'none' // [!code ++]
```

이 플래그의 기본값은 `active`인데, 이는 `refetchActive`의 기본값이 `true`였기 때문입니다. 따라서 `invalidateQueries`가 전혀 refetch하지 않도록 지시하는 방법도 필요해 네 번째 옵션(`none`)이 추가되었습니다.

### `setQueryData`에서 더 이상 `onSuccess`가 호출되지 않음

많은 사람에게 혼란을 주고, `onSuccess` 내부에서 `setQueryData`를 호출하면 무한 루프가 발생했습니다. `staleTime`과 함께 사용하면 캐시에서 데이터만 읽었을 때 `onSuccess`가 호출되지 않아 에러가 생기기도 했습니다.

`onError`, `onSettled`와 마찬가지로, 이제 `onSuccess` 콜백은 요청이 실제로 발생했을 때만 연결됩니다. 요청이 없으면 콜백도 없습니다.

`data` 필드 변경을 감시하고 싶다면, `data`를 의존성 배열에 넣은 `useEffect`를 사용하는 것이 가장 좋습니다. React Query는 구조적 공유를 통해 안정적인 데이터를 보장하므로, 백그라운드 refetch마다 실행되지 않고 데이터 내부가 실제로 변경될 때만 실행됩니다.

```
const { data } = useQuery({ queryKey, queryFn })
React.useEffect(() => mySideEffectHere(data), [data])
```

### `persistQueryClient`와 해당 persister 플러그인은 더 이상 실험 단계가 아니며 이름이 변경됨

플러그인 `createWebStoragePersistor`와 `createAsyncStoragePersistor`는 각각 [`createSyncStoragePersister`](https://tanstack.com/query/latest/docs/framework/react/plugins/createSyncStoragePersister.md)와 [`createAsyncStoragePersister`](https://tanstack.com/query/latest/docs/framework/react/plugins/createAsyncStoragePersister.md)로 이름이 바뀌었습니다. `persistQueryClient`의 `Persistor` 인터페이스도 `Persister`로 변경되었습니다. 이러한 변경의 이유는 [이 스택익스체인지 글](https://english.stackexchange.com/questions/206893/persister-or-persistor)을 참고하세요.

이 플러그인들이 더 이상 실험 단계가 아니므로 import 경로도 업데이트되었습니다.

```tsx
- import { persistQueryClient } from 'react-query/persistQueryClient-experimental' // [!code --]
- import { createWebStoragePersistor } from 'react-query/createWebStoragePersistor-experimental' // [!code --]
- import { createAsyncStoragePersistor } from 'react-query/createAsyncStoragePersistor-experimental' // [!code --]

+ import { persistQueryClient } from '@tanstack/react-query-persist-client' // [!code ++]
+ import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister' // [!code ++]
+ import { createAsyncStoragePersister } from '@tanstack/query-async-storage-persister'  // [!code ++]
```

### Promise의 `cancel` 메서드는 더 이상 지원되지 않음

Promise에 `cancel` 함수를 정의해 라이브러리가 쿼리 취소를 지원하도록 하던 [이전 `cancel` 메서드](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md#old-cancel-function)는 제거되었습니다. 내부적으로 [`AbortController` API](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)를 사용하고 쿼리 함수에 [`AbortSignal` 인스턴스](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)를 제공하는 [새로운 API](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md)(v3.30.0에서 도입)를 사용할 것을 권장합니다.

### TypeScript

이제 TypeScript v4.1 이상이 필요합니다.

### 지원되는 브라우저

v4부터 React Query는 최신 브라우저에 최적화되었습니다. 더 현대적이고 고성능이며 번들 크기가 더 작은 결과를 위해 browserslist를 업데이트했습니다. 요구 사항에 대해서는 [여기](https://tanstack.com/query/latest/docs/framework/react/installation#requirements)를 참고하세요.

### `setLogger` 제거

이전에는 `setLogger`를 호출해 전역적으로 로거를 변경할 수 있었습니다. v4에서는 이 함수가 `QueryClient`를 생성할 때 선택적으로 제공하는 필드로 대체되었습니다.

```tsx
- import { QueryClient, setLogger } from 'react-query'; // [!code --]
+ import { QueryClient } from '@tanstack/react-query'; // [!code ++]

- setLogger(customLogger) // [!code --]
- const queryClient = new QueryClient(); // [!code --]
+ const queryClient = new QueryClient({ logger: customLogger }) // [!code ++]
```

### 서버사이드에서 _기본_ 수동 가비지 컬렉션 없음

v3에서는 React Query가 쿼리 결과를 기본 5분 동안 캐시한 뒤 수동으로 가비지 컬렉션을 수행했습니다. 이 기본값은 서버사이드 React Query에도 적용되었습니다.

이로 인해 메모리 사용량이 높아지고, 수동 가비지 컬렉션이 완료되길 기다리느라 프로세스가 멈추는 문제가 발생했습니다. v4에서는 기본적으로 서버사이드 `cacheTime`이 `Infinity`로 설정되어 수동 가비지 컬렉션이 사실상 비활성화됩니다(요청이 끝나면 NodeJS 프로세스가 모든 것을 정리합니다).

이 변경 사항은 Next.js와 같이 서버사이드 React Query를 사용하는 사용자에게만 영향을 줍니다. 직접 `cacheTime`을 설정하고 있다면 영향은 없지만, 새로운 동작을 참고해 맞춰 보는 것이 좋습니다.

### 프로덕션 로깅

v4부터는 프로덕션 모드에서 react-query가 더 이상 콘솔에 오류(예: 실패한 fetch)를 기록하지 않습니다. 이는 많은 사용자에게 혼란을 줬기 때문입니다. 개발 모드에서는 여전히 오류가 표시됩니다.

### ESM 지원

React Query는 이제 [package.json `"exports"`](https://nodejs.org/api/packages.html#exports)를 지원하며 CommonJS와 ESM 모두에 대해 Node의 네이티브 모듈 해석과 완전히 호환됩니다. 대부분의 사용자에게 파괴적인 변경은 아니지만, 이제 공식적으로 지원하는 엔트리 포인트만 프로젝트에서 import할 수 있습니다.

### 간소화된 NotifyEvents

`QueryCache`에 수동으로 구독하면 항상 `QueryCacheNotifyEvent`를 받았지만, `MutationCache`에는 그렇지 않았습니다. 이제 동작을 일관되게 만들고 이벤트 이름도 조정했습니다.

#### QueryCacheNotifyEvent

```tsx
- type: 'queryAdded' // [!code --]
+ type: 'added' // [!code ++]
- type: 'queryRemoved' // [!code --]
+ type: 'removed' // [!code ++]
- type: 'queryUpdated' // [!code --]
+ type: 'updated' // [!code ++]
```

#### MutationCacheNotifyEvent

`MutationCacheNotifyEvent`는 `QueryCacheNotifyEvent`와 동일한 타입을 사용합니다.

> 참고: 이는 `queryCache.subscribe` 또는 `mutationCache.subscribe`를 통해 캐시에 수동으로 구독하는 경우에만 관련이 있습니다.

### 별도의 hydration export 제거

버전 [3.22.0](https://github.com/tannerlinsley/react-query/releases/tag/v3.22.0)부터 hydration 유틸리티가 React Query 코어로 이동했습니다. v3에서는 여전히 `react-query/hydration`에서 기존 export를 사용할 수 있었지만, v4에서는 이 export가 제거되었습니다.

```tsx
- import { dehydrate, hydrate, useHydrate, Hydrate } from 'react-query/hydration' // [!code --]
+ import { dehydrate, hydrate, useHydrate, Hydrate } from '@tanstack/react-query' // [!code ++]
```

### `queryClient`, `query`, `mutation`에서 문서화되지 않은 메서드 제거

`QueryClient`의 `cancelMutations`와 `executeMutation` 메서드는 문서화되지 않았고 내부에서도 사용되지 않아 제거했습니다. `executeMutation`은 `mutationCache`에 이미 있는 메서드를 감싸는 래퍼였으므로, 해당 기능은 계속 사용할 수 있습니다.

```tsx
- executeMutation< // [!code --]
-   TData = unknown, // [!code --]
-   TError = unknown, // [!code --]
-   TVariables = void, // [!code --]
-   TContext = unknown // [!code --]
- >( // [!code --]
-   options: MutationOptions<TData, TError, TVariables, TContext> // [!code --]
- ): Promise<TData> { // [!code --]
-   return this.mutationCache.build(this, options).execute() // [!code --]
- } // [!code --]
```

추가로, 사용되지 않던 `query.setDefaultOptions`도 제거되었습니다. `mutation.cancel`은 실제로 진행 중인 요청을 취소하지 못했기 때문에 삭제했습니다.

### `src/react` 디렉터리가 `src/reactjs`로 변경

기존에는 React Query에 `react`라는 디렉터리가 있었고, 그 안에서 `react` 모듈을 import했습니다. 이 때문에 일부 Jest 설정에서 문제가 발생해 다음과 같은 테스트 오류가 나올 수 있었습니다:

```
TypeError: Cannot read property 'createContext' of undefined
```

디렉터리 이름을 변경하면서 이러한 문제가 사라졌습니다.

프로젝트에서 `'react-query/react'`를 직접 import하고 있었다면(단순히 `'react-query'`가 아닌), 다음처럼 import 경로를 수정해야 합니다:

```tsx
- import { QueryClientProvider } from 'react-query/react'; // [!code --]
+ import { QueryClientProvider } from '@tanstack/react-query/reactjs'; // [!code ++]
```

## 새로운 기능 🚀

v4에는 훌륭한 신규 기능이 다수 포함되어 있습니다.

### React 18 지원

올해 초 출시된 React 18과 그에 따른 새로운 동시성 기능을 v4가 완전하게 지원합니다.

### 완전한 오프라인 지원

v3에서는 React Query가 항상 쿼리와 뮤테이션을 실행했지만, 재시도하려면 인터넷에 연결돼 있어야 한다고 가정했습니다. 이로 인해 다음과 같은 혼란스러운 상황들이 있었습니다:

- 오프라인 상태에서 쿼리를 마운트하면 로딩 상태로 진입하고 요청은 실패하며, 실제로 fetch를 수행하지 않더라도 온라인이 될 때까지 로딩 상태에 머무릅니다.
- 마찬가지로, 오프라인이면서 재시도가 비활성화되어 있으면 쿼리가 실행되고 실패해 곧바로 오류 상태가 됩니다.
- 오프라인 상태에서 네트워크 연결이 반드시 필요하지 않은 쿼리를 실행하고 싶을 때(React Query를 데이터 fetch 외의 용도로도 사용할 수 있기 때문) 다른 이유로 실패하면, 해당 쿼리는 온라인이 될 때까지 일시 중단됩니다.
- 오프라인일 때 창 포커스 refetch는 아무 동작도 하지 않았습니다.

v4는 이러한 문제를 해결하기 위해 새로운 `networkMode`를 도입했습니다. 자세한 내용은 [네트워크 모드](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode) 전용 페이지를 참고하세요.

### 기본값으로 추적되는 쿼리

React Query는 기본적으로 쿼리 속성을 “추적”하도록 설정되어 렌더링 최적화에 도움이 됩니다. 이 기능은 [v3.6.0](https://github.com/tannerlinsley/react-query/releases/tag/v3.6.0)부터 존재했지만, v4에서 기본 동작이 되었습니다.

### setQueryData로 업데이트 건너뛰기

[setQueryData의 함수형 업데이트 폼](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientsetquerydata)을 사용할 때 `undefined`를 반환하면 업데이트를 건너뛸 수 있습니다. 이는 `previousValue`가 `undefined`인 경우, 즉 현재 캐시된 항목이 없어 생성하지 않으려는 상황(예: todo 토글)에서 유용합니다:

```tsx
queryClient.setQueryData(['todo', id], (previousTodo) =>
  previousTodo ? { ...previousTodo, done: true } : undefined,
)
```

### 뮤테이션 캐시 가비지 컬렉션

이제 뮤테이션도 쿼리처럼 자동으로 가비지 컬렉션됩니다. 뮤테이션의 기본 `cacheTime` 역시 5분으로 설정됩니다.

### 다중 Provider를 위한 커스텀 컨텍스트

이제 커스텀 컨텍스트를 지정해 훅과 해당 `Provider`를 매칭할 수 있습니다. 컴포넌트 트리에 여러 React Query `Provider` 인스턴스가 존재할 수 있는 상황에서, 특정 훅이 올바른 `Provider`를 사용하도록 보장하는 데 필수적입니다.

예시:

1. 데이터 패키지를 생성합니다.

```tsx
// Our first data package: @my-scope/container-data

const context = React.createContext<QueryClient | undefined>(undefined)
const queryClient = new QueryClient()

export const useUser = () => {
  return useQuery(USER_KEY, USER_FETCHER, {
    context,
  })
}

export const ContainerDataProvider = ({
  children,
}: {
  children: React.ReactNode
}) => {
  return (
    <QueryClientProvider client={queryClient} context={context}>
      {children}
    </QueryClientProvider>
  )
}
```

2. 두 번째 데이터 패키지를 생성합니다.

```tsx
// Our second data package: @my-scope/my-component-data

const context = React.createContext<QueryClient | undefined>(undefined)
const queryClient = new QueryClient()

export const useItems = () => {
  return useQuery(ITEMS_KEY, ITEMS_FETCHER, {
    context,
  })
}

export const MyComponentDataProvider = ({
  children,
}: {
  children: React.ReactNode
}) => {
  return (
    <QueryClientProvider client={queryClient} context={context}>
      {children}
    </QueryClientProvider>
  )
}
```

3. 애플리케이션에서 이 두 데이터 패키지를 사용합니다.

```tsx
// Our application

import { ContainerDataProvider, useUser } from "@my-scope/container-data";
import { AppDataProvider } from "@my-scope/app-data";
import { MyComponentDataProvider, useItems } from "@my-scope/my-component-data";

<ContainerDataProvider> // <-- Provides container data (like "user") using its own React Query provider
  ...
  <AppDataProvider> // <-- Provides app data using its own React Query provider (unused in this example)
    ...
      <MyComponentDataProvider> // <-- Provides component data (like "items") using its own React Query provider
        <MyComponent />
      </MyComponentDataProvider>
    ...
  </AppDataProvider>
  ...
</ContainerDataProvider>

// Example of hooks provided by the "DataProvider" components above:
const MyComponent = () => {
  const user = useUser() // <-- Uses the context specified in ContainerDataProvider.
  const items = useItems() // <-- Uses the context specified in MyComponentDataProvider
  ...
}
```

