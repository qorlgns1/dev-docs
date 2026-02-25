---
title: 'TanStack Query v5로 마이그레이션하기'
description: 'v5는 메이저 버전이므로 알아두어야 할 파괴적 변경 사항이 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/guides/migrating-to-v5

# TanStack Query v5로 마이그레이션하기

## 주요 변경 사항

v5는 메이저 버전이므로 알아두어야 할 파괴적 변경 사항이 있습니다.

### 하나의 시그니처, 단일 객체만 지원

useQuery 및 관련 훅들은 이전에는 TypeScript에서 다양한 오버로드를 제공해 여러 방식으로 호출할 수 있었습니다. 이는 타입 유지가 어렵고, 첫 번째와 두 번째 인자의 타입을 런타임에서 검사해야 옵션을 올바르게 구성할 수 있었기 때문입니다.

이제는 객체 형식만 지원합니다.

```tsx
useQuery(key, fn, options) // [!code --]
useQuery({ queryKey, queryFn, ...options }) // [!code ++]
useInfiniteQuery(key, fn, options) // [!code --]
useInfiniteQuery({ queryKey, queryFn, ...options }) // [!code ++]
useMutation(fn, options) // [!code --]
useMutation({ mutationFn, ...options }) // [!code ++]
useIsFetching(key, filters) // [!code --]
useIsFetching({ queryKey, ...filters }) // [!code ++]
useIsMutating(key, filters) // [!code --]
useIsMutating({ mutationKey, ...filters }) // [!code ++]
```

```tsx
queryClient.isFetching(key, filters) // [!code --]
queryClient.isFetching({ queryKey, ...filters }) // [!code ++]
queryClient.ensureQueryData(key, filters) // [!code --]
queryClient.ensureQueryData({ queryKey, ...filters }) // [!code ++]
queryClient.getQueriesData(key, filters) // [!code --]
queryClient.getQueriesData({ queryKey, ...filters }) // [!code ++]
queryClient.setQueriesData(key, updater, filters, options) // [!code --]
queryClient.setQueriesData({ queryKey, ...filters }, updater, options) // [!code ++]
queryClient.removeQueries(key, filters) // [!code --]
queryClient.removeQueries({ queryKey, ...filters }) // [!code ++]
queryClient.resetQueries(key, filters, options) // [!code --]
queryClient.resetQueries({ queryKey, ...filters }, options) // [!code ++]
queryClient.cancelQueries(key, filters, options) // [!code --]
queryClient.cancelQueries({ queryKey, ...filters }, options) // [!code ++]
queryClient.invalidateQueries(key, filters, options) // [!code --]
queryClient.invalidateQueries({ queryKey, ...filters }, options) // [!code ++]
queryClient.refetchQueries(key, filters, options) // [!code --]
queryClient.refetchQueries({ queryKey, ...filters }, options) // [!code ++]
queryClient.fetchQuery(key, fn, options) // [!code --]
queryClient.fetchQuery({ queryKey, queryFn, ...options }) // [!code ++]
queryClient.prefetchQuery(key, fn, options) // [!code --]
queryClient.prefetchQuery({ queryKey, queryFn, ...options }) // [!code ++]
queryClient.fetchInfiniteQuery(key, fn, options) // [!code --]
queryClient.fetchInfiniteQuery({ queryKey, queryFn, ...options }) // [!code ++]
queryClient.prefetchInfiniteQuery(key, fn, options) // [!code --]
queryClient.prefetchInfiniteQuery({ queryKey, queryFn, ...options }) // [!code ++]
```

```tsx
queryCache.find(key, filters) // [!code --]
queryCache.find({ queryKey, ...filters }) // [!code ++]
queryCache.findAll(key, filters) // [!code --]
queryCache.findAll({ queryKey, ...filters }) // [!code ++]
```

### `queryClient.getQueryData`는 이제 인자로 queryKey만 허용

`queryClient.getQueryData`의 인자는 이제 `queryKey`만 받을 수 있습니다.

```tsx
queryClient.getQueryData(queryKey, filters) // [!code --]
queryClient.getQueryData(queryKey) // [!code ++]
```

### `queryClient.getQueryState`는 이제 인자로 queryKey만 허용

`queryClient.getQueryState`의 인자는 이제 `queryKey`만 받을 수 있습니다.

```tsx
queryClient.getQueryState(queryKey, filters) // [!code --]
queryClient.getQueryState(queryKey) // [!code ++]
```

#### Codemod

오버로드 제거 마이그레이션을 쉽게 하기 위해 v5에는 codemod가 포함됩니다.

> 이 codemod는 파괴적 변경을 도와주는 최선의 시도입니다. 생성된 코드를 반드시 꼼꼼히 검토하세요! 또한 codemod가 찾을 수 없는 엣지 케이스가 있으므로 로그 출력에도 주의를 기울이세요.

`.js` 또는 `.jsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift@latest ./path/to/src/ \
  --extensions=js,jsx \
  --transform=./node_modules/@tanstack/react-query/build/codemods/src/v5/remove-overloads/remove-overloads.cjs
```

`.ts` 또는 `.tsx` 파일에 실행하려면 아래 명령을 사용하세요.

```
npx jscodeshift@latest ./path/to/src/ \
  --extensions=ts,tsx \
  --parser=tsx \
  --transform=./node_modules/@tanstack/react-query/build/codemods/src/v5/remove-overloads/remove-overloads.cjs
```

`TypeScript`의 경우 파서를 `tsx`로 지정해야 합니다. 그렇지 않으면 codemod가 제대로 적용되지 않습니다.

**참고:** codemod를 적용하면 코드 포맷이 깨질 수 있으니, 적용 후 `prettier`와/또는 `eslint`를 꼭 실행하세요!

codemod 작동 방식에 대한 몇 가지 메모:

- 일반적으로 첫 번째 인자가 객체 리터럴이고 그 안에 "queryKey" 또는 "mutationKey" 속성이 있는 행운의 경우를 찾습니다(변환되는 훅/메서드 호출에 따라 다름). 이 조건을 만족하면 이미 새로운 시그니처와 일치하므로 codemod는 해당 코드를 수정하지 않습니다. 🎉
- 위 조건이 충족되지 않으면 첫 번째 인자가 배열 리터럴이거나 배열 리터럴을 참조하는 식별자인지 확인합니다. 해당되면 codemod가 이를 객체 리터럴로 감싸 첫 번째 인자로 만듭니다.
- 객체 인자를 유추할 수 있으면 codemod가 기존 속성을 새 객체로 복사하려고 시도합니다.
- codemod가 사용 방식을 유추할 수 없으면 콘솔에 메시지를 남깁니다. 메시지에는 파일 이름과 사용 라인 번호가 포함되며, 이 경우 수동으로 마이그레이션해야 합니다.
- 변환 결과 오류가 발생하면 콘솔 메시지가 나타납니다. 예상치 못한 일이 발생했음을 알리고 수동으로 마이그레이션해야 함을 알려줍니다.

### useQuery(및 QueryObserver)에서 콜백 제거

`onSuccess`, `onError`, `onSettled`는 Query에서 제거되었습니다. Mutation에는 영향을 주지 않았습니다. 이 변경의 이유와 대안은 [해당 RFC](https://github.com/TanStack/query/discussions/5279)를 참고하세요.

### `refetchInterval` 콜백은 이제 `query`만 전달받음

이 변경으로 콜백 호출 방식이 단순화되었습니다(`refetchOnWindowFocus`, `refetchOnMount`, `refetchOnReconnect` 콜백도 모두 query만 전달받습니다). 또한 `select`로 변환된 데이터를 콜백이 받을 때 발생하던 타입 문제를 해결합니다.

```tsx
- refetchInterval: number | false | ((data: TData | undefined, query: Query) => number | false | undefined) // [!code --]
+ refetchInterval: number | false | ((query: Query) => number | false | undefined) // [!code ++]
```

여전히 `query.state.data`로 데이터에 접근할 수 있지만, 이는 `select`로 변환된 데이터가 아닙니다. 변환된 데이터가 필요하면 `query.state.data`에 변환을 다시 적용하세요.

### useQuery의 `remove` 메서드 제거

이전에는 remove 메서드가 관찰자에게 알리지 않고 queryCache에서 쿼리를 제거했습니다. 이는 더 이상 필요 없는 데이터를 명령형으로 제거할 때, 예를 들어 사용자 로그아웃 시 유용했습니다.

그러나 쿼리가 아직 활성 상태인 동안 이를 수행해도 다음 렌더링에서 하드 로딩 상태만 발생합니다.

그래도 쿼리를 제거해야 한다면 `queryClient.removeQueries({queryKey: key})`를 사용할 수 있습니다.

```tsx
const queryClient = useQueryClient()
const query = useQuery({ queryKey, queryFn })

query.remove() // [!code --]
queryClient.removeQueries({ queryKey }) // [!code ++]
```

### 최소 요구 TypeScript 버전이 4.7로 상향

타입 추론과 관련된 중요한 수정이 포함되었기 때문입니다. 자세한 내용은 [해당 TypeScript 이슈](https://github.com/microsoft/TypeScript/issues/43371)를 참고하세요.

### useQuery에서 `isDataEqual` 옵션 제거

이 함수는 이전에 `data`를 유지할지(`true`) 또는 새 데이터를 사용할지(`false`)를 나타내는 데 사용되었습니다.

대신 `structuralSharing`에 함수를 전달하여 동일한 기능을 구현할 수 있습니다.

```tsx
import { replaceEqualDeep } from '@tanstack/react-query'

- isDataEqual: (oldData, newData) => customCheck(oldData, newData) // [!code --]
+ structuralSharing: (oldData, newData) => customCheck(oldData, newData) ? oldData : replaceEqualDeep(oldData, newData) // [!code ++]
```

### 사용 중단된 커스텀 로거 제거

커스텀 로거는 v4에서 이미 사용 중단되었고 이번 버전에서 제거되었습니다. 로깅은 개발 모드에서만 영향이 있었고, 이때 커스텀 로거를 전달할 필요가 없습니다.

### 지원 브라우저

더 현대적이고 성능이 좋으며 번들이 작은 결과를 위해 browserslist를 업데이트했습니다. 요구 사항은 [여기](https://tanstack.com/query/latest/docs/framework/react/installation#requirements)에서 확인할 수 있습니다.

### 프라이빗 클래스 필드 및 메서드

TanStack Query는 항상 클래스에 프라이빗 필드와 메서드가 있었지만, 실제로는 프라이빗하지 않았고 `TypeScript` 상에서만 프라이빗이었습니다. 이제 [ECMAScript 프라이빗 클래스 기능](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields)을 사용하여 런타임에서 외부에서 접근할 수 없는 진정한 프라이빗 필드를 제공합니다.

### `cacheTime`을 `gcTime`으로 이름 변경

대부분 `cacheTime`을 “데이터가 캐시되는 시간”으로 잘못 이해합니다. 이는 정확하지 않습니다.

`cacheTime`은 쿼리가 사용 중인 동안 아무 작업도 하지 않습니다. 쿼리가 미사용 상태가 되면 작동하며, 시간이 지나면 캐시가 커지는 것을 막기 위해 데이터가 “가비지 컬렉션”됩니다.

`gc`는 “garbage collect” 시간을 의미합니다. 더 기술적이지만 컴퓨터 과학에서 꽤 [잘 알려진 약어](https://tanstack.com/query/latest/docs/framework/react/guides/<https:/en.wikipedia.org/wiki/Garbage_collection_(computer_science)>)입니다.

```tsx
const MINUTE = 1000 * 60;

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
-      cacheTime: 10 * MINUTE, // [!code --]
+      gcTime: 10 * MINUTE, // [!code ++]
    },
  },
})
```

### `useErrorBoundary` 옵션을 `throwOnError`로 이름 변경

`useErrorBoundary` 옵션을 더 프레임워크 불가지론적으로 만들고, React 훅의 일반적인 접두사 "`use`" 및 "ErrorBoundary" 컴포넌트 이름과의 혼동을 피하기 위해 `throwOnError`로 이름이 변경되었습니다. 새로운 이름이 기능을 더 정확히 설명합니다.

### TypeScript: 기본 오류 타입이 `unknown`에서 `Error`로 변경

JavaScript에서는 무엇이든 `throw`할 수 있으므로 `unknown`이 가장 정확한 타입이지만, 거의 항상 `Error`(또는 그 하위 클래스)가 throw됩니다. 이 변경으로 대부분의 경우 TypeScript에서 `error` 필드를 다루기가 더 쉬워졌습니다.

Error가 아닌 것을 throw하려면 이제 직접 제네릭을 설정해야 합니다.

```ts
useQuery<number, string>({
  queryKey: ['some-query'],
  queryFn: async () => {
    if (Math.random() > 0.5) {
      throw 'some error'
    }
    return 42
  },
})
```

다른 종류의 Error를 전역으로 설정하는 방법은 [TypeScript 가이드](https://tanstack.com/query/latest/docs/framework/react/typescript.md#registering-a-global-error)를 참고하세요.

### eslint `prefer-query-object-syntax` 규칙 제거

이제 객체 구문만 지원하므로 해당 규칙은 더 이상 필요하지 않습니다.

### `keepPreviousData` 제거 및 `placeholderData` 아이덴티티 함수 사용

`keepPreviousData` 옵션과 `isPreviousData` 플래그는 `placeholderData` 및 `isPlaceholderData`와 거의 동일한 기능을 했기 때문에 제거되었습니다.

`keepPreviousData`와 동일한 기능을 얻기 위해 이전 쿼리 `data`를 `placeholderData`에 인자로 추가했고, 이 함수는 아이덴티티 함수를 받을 수 있습니다. 따라서 `placeholderData`에 아이덴티티 함수를 제공하거나 TanStack Query에서 제공하는 `keepPreviousData` 함수를 사용하면 됩니다.

> 참고로 `useQueries`의 `placeholderData` 함수는 인자로 `previousData`를 받지 않습니다. 이는 배열로 전달되는 쿼리의 동적 특성 때문에 placeholder와 queryFn의 결과 형태가 다를 수 있기 때문입니다.

```tsx
import {
   useQuery,
+  keepPreviousData // [!code ++]
} from "@tanstack/react-query";

const {
   data,
-  isPreviousData, // [!code --]
+  isPlaceholderData, // [!code ++]
} = useQuery({
  queryKey,
  queryFn,
- keepPreviousData: true, // [!code --]
+ placeholderData: keepPreviousData // [!code ++]
});
```

TanStack Query 맥락에서 아이덴티티 함수는 제공된 인자(즉 데이터)를 변경 없이 그대로 반환하는 함수를 의미합니다.

```ts
useQuery({
  queryKey,
  queryFn,
  placeholderData: (previousData, previousQuery) => previousData, // identity function with the same behaviour as `keepPreviousData`
})
```

이 변경에는 알아두어야 할 몇 가지 주의 사항이 있습니다.

- `placeholderData`는 항상 `success` 상태로 전환하지만, `keepPreviousData`는 이전 쿼리의 상태를 유지했습니다. 예를 들어 데이터를 성공적으로 가져온 뒤 백그라운드 리패치에서 오류가 발생하면 상태가 `error`일 수 있습니다. 그러나 오류 자체가 공유되지는 않았으므로, 우리는 `placeholderData`의 동작을 유지하기로 결정했습니다.
- `keepPreviousData`는 이전 데이터의 `dataUpdatedAt` 타임스탬프를 제공했지만 `placeholderData`에서는 `dataUpdatedAt`이 0으로 유지됩니다. 화면에 타임스탬프를 계속 표시하려면 다소 번거로울 수 있으나 `useEffect`로 우회할 수 있습니다.

  ```ts
  const [updatedAt, setUpdatedAt] = useState(0)

  const { data, dataUpdatedAt } = useQuery({
    queryKey: ['projects', page],
    queryFn: () => fetchProjects(page),
  })

  useEffect(() => {
    if (dataUpdatedAt > updatedAt) {
      setUpdatedAt(dataUpdatedAt)
    }
  }, [dataUpdatedAt])
  ```

### 창 포커스 리패칭이 더 이상 `focus` 이벤트를 청취하지 않음

이제 `visibilitychange` 이벤트만 사용합니다. 지원하는 브라우저가 `visibilitychange`를 모두 지원하기 때문에 가능한 변경입니다. 이는 [여기에 나열된 여러 문제](https://github.com/TanStack/query/pull/4805)를 해결합니다.

### 네트워크 상태가 더 이상 `navigator.onLine`에 의존하지 않음

`navigator.onLine`은 Chromium 기반 브라우저에서 제대로 동작하지 않습니다. [많은 이슈](https://bugs.chromium.org/p/chromium/issues/list?q=navigator.online)에서 false negative 문제가 보고되어 쿼리가 잘못 `offline`으로 표시되는 경우가 있습니다.

이를 피하기 위해 이제 항상 `online: true`로 시작하고, 상태 업데이트를 위해 `online`과 `offline` 이벤트만 청취합니다.

이로 인해 false negative 가능성은 줄어들지만, serviceWorker로 로드되어 인터넷 연결 없이도 동작하는 오프라인 앱에서는 false positive가 발생할 수 있습니다.

### 커스텀 `context` prop 제거, 대신 커스텀 `queryClient` 인스턴스 사용

v4에서는 모든 react-query 훅에 커스텀 `context`를 전달해 MicroFrontend 사용 시 올바른 격리를 제공했습니다.

그러나 `context`는 React에 한정된 기능입니다. `context`가 하는 일은 `queryClient`에 접근하게 해주는 것뿐입니다. 대신 커스텀 `queryClient`를 직접 전달할 수 있게 하면 동일한 격리를 달성할 수 있습니다.
이로써 다른 프레임워크에서도 프레임워크 불가지론적으로 동일한 기능을 사용할 수 있습니다.

```tsx
import { queryClient } from './my-client'

const { data } = useQuery(
  {
    queryKey: ['users', id],
    queryFn: () => fetch(...),
-   context: customContext // [!code --]
  },
+  queryClient, // [!code ++]
)
```

### `refetchPage` 제거, `maxPages` 도입

v4에서는 `refetchPage` 함수를 통해 무한 쿼리에서 리패칭할 페이지를 정의할 수 있었습니다.

그러나 모든 페이지를 리패치하면 UI 불일치가 발생할 수 있습니다. 또한 이 옵션은 `queryClient.refetchQueries` 등에서도 제공되지만, 무한 쿼리에서만 동작하고 “일반” 쿼리에서는 아무 작업도 하지 않습니다.

v5에서는 무한 쿼리의 쿼리 데이터와 리패치할 페이지 수를 제한하는 새로운 `maxPages` 옵션이 도입되었습니다. 이 기능은 `refetchPage`가 처음 의도했던 사용 사례를 관련 문제 없이 처리합니다.

### 새로운 `dehydrate` API

`dehydrate`에 전달할 수 있는 옵션이 단순화되었습니다. 기본 구현에 따라 Query와 Mutation은 항상 탈수(dehydrate)됩니다. 이 동작을 바꾸려면 제거된 불리언 옵션 `dehydrateMutations`, `dehydrateQueries` 대신 `shouldDehydrateQuery` 또는 `shouldDehydrateMutation` 함수를 구현하세요. 예전처럼 쿼리/뮤테이션을 전혀 하이드레이트하지 않으려면 `() => false`를 전달하면 됩니다.

```tsx
- dehydrateMutations?: boolean // [!code --]
- dehydrateQueries?: boolean // [!code --]
```

### 이제 무한 쿼리에 `initialPageParam`이 필요합니다

이전에는 `queryFn`에 `pageParam`으로 `undefined`를 전달했고, `queryFn` 함수 시그니처에서 `pageParam` 매개변수에 기본값을 지정할 수 있었습니다. 하지만 이렇게 하면 직렬화할 수 없는 `undefined`가 `queryCache`에 저장되는 단점이 있었습니다.

이제는 무한 쿼리 옵션에 명시적인 `initialPageParam`을 전달해야 합니다. 이는 첫 번째 페이지의 `pageParam`으로 사용됩니다.

```tsx
useInfiniteQuery({
   queryKey,
-  queryFn: ({ pageParam = 0 }) => fetchSomething(pageParam), // [!code --]
+  queryFn: ({ pageParam }) => fetchSomething(pageParam), // [!code ++]
+  initialPageParam: 0, // [!code ++]
   getNextPageParam: (lastPage) => lastPage.next,
})
```

### 무한 쿼리의 수동 모드가 제거되었습니다

이전에는 `fetchNextPage` 또는 `fetchPreviousPage`에 `pageParam` 값을 직접 전달하여 `getNextPageParam` 또는 `getPreviousPageParam`에서 반환될 `pageParams`를 덮어쓸 수 있었습니다. 이 기능은 리패치 시 전혀 동작하지 않았고 널리 알려지거나 사용되지도 않았습니다. 따라서 이제 무한 쿼리에서는 `getNextPageParam`이 필수가 되었습니다.

### `getNextPageParam` 또는 `getPreviousPageParam`에서 `null`을 반환하면 더 이상 페이지가 없음을 나타냅니다

v4에서는 더 이상 페이지가 없음을 나타내기 위해 명시적으로 `undefined`를 반환해야 했습니다. 이제 이 검사를 `null`까지 확장했습니다.

### 서버에서는 재시도를 수행하지 않습니다

서버에서는 `retry` 기본값이 이제 `3`이 아닌 `0`입니다. 프리패칭에서는 항상 기본적으로 재시도 횟수를 `0`으로 설정했지만, React18 이후 `suspense`가 활성화된 쿼리도 서버에서 직접 실행될 수 있으므로 서버에서 재시도를 전혀 하지 않도록 해야 합니다.

### `status: loading`이 `status: pending`으로, `isLoading`이 `isPending`으로 변경되었고 `isInitialLoading`은 이제 `isLoading`으로 이름이 바뀌었습니다

`loading` 상태는 `pending`으로 이름이 바뀌었고, 유도된 `isLoading` 플래그 역시 `isPending`으로 변경되었습니다.

뮤테이션에서도 `status`가 `loading`에서 `pending`으로, `isLoading` 플래그가 `isPending`으로 변경되었습니다.

마지막으로, 쿼리에 새로운 유도 플래그 `isLoading`이 추가되었으며, 이는 `isPending && isFetching`으로 구현됩니다. 즉, `isLoading`과 `isInitialLoading`이 동일한 의미를 갖지만, `isInitialLoading`은 이제 더 이상 권장되지 않으며 다음 메이저 버전에서 제거될 예정입니다.

이 변경의 배경을 이해하려면 [v5 로드맵 토론](https://github.com/TanStack/query/discussions/4252)을 확인하세요.

### `hashQueryKey`가 `hashKey`로 이름이 바뀌었습니다

이제 이 함수가 뮤테이션 키도 해싱하며, 뮤테이션이 전달되는 `useIsMutating` 및 `useMutationState`의 `predicate` 함수 내부에서도 사용할 수 있기 때문입니다.

[//]: # 'FrameworkSpecificBreakingChanges'

### 필요한 최소 React 버전은 이제 18.0입니다

React Query v5는 React 18.0 이상이 필요합니다. 이는 React 18.0 이상에서만 제공되는 새로운 `useSyncExternalStore` 훅을 사용하기 때문입니다. 이전에는 React에서 제공하는 shim을 사용했습니다.

### QueryClientProvider에서 `contextSharing` prop이 제거되었습니다

이전에는 `contextSharing` 속성을 사용해 창 전체에서 쿼리 클라이언트 컨텍스트의 첫 번째(그리고 최소 한 개의) 인스턴스를 공유할 수 있었습니다. 이를 통해 TanStack Query가 서로 다른 번들이나 마이크로프런트엔드에서 사용되더라도 모듈 스코핑과 상관없이 동일한 컨텍스트 인스턴스를 사용하도록 할 수 있었습니다.

v5에서 커스텀 컨텍스트 prop이 제거되었으므로, [커스텀 queryClient 인스턴스를 통한 커스텀 컨텍스트 prop 제거](#removed-custom-context-prop-in-favor-of-custom-queryclient-instance) 섹션을 참고하세요. 애플리케이션의 여러 패키지에서 동일한 쿼리 클라이언트를 공유하려면 공유하는 커스텀 `queryClient` 인스턴스를 직접 전달하면 됩니다.

### React 및 React Native에서 더 이상 `unstable_batchedUpdates`를 배치 함수로 사용하지 않습니다

React 18에서는 `unstable_batchedUpdates` 함수가 noop이므로 더 이상 `react-query`에서 자동으로 배치 함수로 설정되지 않습니다.

프레임워크가 커스텀 배치 함수를 지원한다면, `notifyManager.setBatchNotifyFunction`을 호출하여 TanStack Query에 이를 알려줄 수 있습니다.

예를 들어, `solid-query`에서는 다음과 같이 배치 함수를 설정합니다.

```ts
import { notifyManager } from '@tanstack/query-core'
import { batch } from 'solid-js'

notifyManager.setBatchNotifyFunction(batch)
```

### Hydration API 변경 사항

동시성 기능과 전환을 더 잘 지원하기 위해 Hydration API를 일부 변경했습니다. `Hydrate` 컴포넌트는 `HydrationBoundary`로 이름이 바뀌었고 `useHydrate` 훅은 제거되었습니다.

`HydrationBoundary`는 더 이상 뮤테이션을 하이드레이트하지 않고, 쿼리만 하이드레이트합니다. 뮤테이션을 하이드레이트하려면 로우레벨 `hydrate` API 또는 `persistQueryClient` 플러그인을 사용하세요.

마지막으로 기술적인 세부사항으로, 쿼리가 하이드레이트되는 타이밍이 약간 변경되었습니다. 새로운 쿼리는 여전히 렌더 단계에서 하이드레이트되어 SSR이 기존처럼 동작하지만, 캐시에 이미 존재하는 쿼리는 (데이터가 캐시에 있는 것보다 더 최신일 경우) 이제 이펙트에서 하이드레이트됩니다. 애플리케이션 시작 시 한 번만 하이드레이션하는 일반적인 경우에는 영향이 없지만, 서버 컴포넌트를 사용해 페이지 이동 시 최신 데이터를 내려보내 하이드레이션한다면 페이지가 즉시 리렌더링되기 전에 이전 데이터가 잠깐 보일 수 있습니다.

이 마지막 변경은 기술적으로 브레이킹 변경이며, 페이지 전환이 완전히 커밋되기 전에 _기존_ 페이지의 콘텐츠를 조기에 업데이트하지 않기 위해 도입되었습니다. 별도의 조치는 필요하지 않습니다.

```tsx
- import { Hydrate } from '@tanstack/react-query' // [!code --]
+ import { HydrationBoundary } from '@tanstack/react-query' // [!code ++]

- <Hydrate state={dehydratedState}> // [!code --]
+ <HydrationBoundary state={dehydratedState}> // [!code ++]
  <App />
- </Hydrate> // [!code --]
+ </HydrationBoundary> // [!code ++]
```

### 쿼리 기본값 변경

`queryClient.getQueryDefaults`는 이제 첫 번째 일치 항목만 반환하는 대신 모든 일치 등록을 병합합니다.

그 결과, `queryClient.setQueryDefaults` 호출은 특정성이 _높아지는_ 순서대로 진행해야 합니다. 즉, 등록은 **가장 일반적인 키**에서 **가장 구체적인 키** 순으로 이루어져야 합니다.

예시는 다음과 같습니다.

```ts
+ queryClient.setQueryDefaults(['todo'], {   // [!code ++]
+   retry: false,  // [!code ++]
+   staleTime: 60_000,  // [!code ++]
+ })  // [!code ++]
queryClient.setQueryDefaults(['todo', 'detail'], {
+   retry: true,  // [!code --]
  retryDelay: 1_000,
  staleTime: 10_000,
})
- queryClient.setQueryDefaults(['todo'], { // [!code --]
-   retry: false, // [!code --]
-   staleTime: 60_000, // [!code --]
- }) // [!code --]
```

이 예시에서는 이제 더 일반적인 등록에서 상속되는 `retry: false`를 상쇄하기 위해 `['todo', 'detail']` 등록에 `retry: true`를 추가했습니다. 정확한 동작을 유지하기 위한 구체적인 변경 사항은 기본값에 따라 달라집니다.

[//]: # 'FrameworkSpecificBreakingChanges'

## 새로운 기능 🚀

v5에는 다음과 같은 새로운 기능도 포함됩니다.

### 단순화된 낙관적 업데이트

`useMutation`에서 반환되는 `variables`를 활용해 낙관적 업데이트를 수행하는 새로운 간단한 방법이 도입되었습니다.

```tsx
const queryInfo = useTodos()
const addTodoMutation = useMutation({
  mutationFn: (newTodo: string) => axios.post('/api/data', { text: newTodo }),
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todos'] }),
})

if (queryInfo.data) {
  return (
    <ul>
      {queryInfo.data.items.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
      ))}
      {addTodoMutation.isPending && (
        <li key={String(addTodoMutation.submittedAt)} style={{ opacity: 0.5 }}>
          {addTodoMutation.variables}
        </li>
      )}
    </ul>
  )
}
```

여기서는 캐시에 직접 데이터를 작성하는 대신 뮤테이션이 실행되는 동안 UI가 어떻게 보일지를 변경하고 있습니다. 낙관적 업데이트를 보여줘야 하는 위치가 하나뿐일 때 가장 효과적입니다. 자세한 내용은 [낙관적 업데이트 문서](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates.md)를 참고하세요.

### 새로운 `maxPages` 옵션을 통한 제한된 무한 쿼리

무한 스크롤이나 페이지 매김이 필요할 때 무한 쿼리가 유용합니다. 하지만 더 많은 페이지를 가져올수록 더 많은 메모리를 사용하게 되고, 모든 페이지를 순차적으로 리패치하기 때문에 쿼리 리패치 과정도 느려집니다.

버전 5에는 무한 쿼리에서 `maxPages` 옵션이 새롭게 추가되어, 쿼리 데이터에 저장되고 이후 리패치되는 페이지 수를 개발자가 제한할 수 있습니다. 제공하려는 UX와 리패치 성능에 맞춰 `maxPages` 값을 조정할 수 있습니다.

무한 리스트는 양방향으로 동작해야 하므로 `getNextPageParam`과 `getPreviousPageParam`이 모두 정의되어 있어야 한다는 점에 유의하세요.

### 무한 쿼리는 여러 페이지를 사전 패치할 수 있습니다

무한 쿼리도 일반 쿼리처럼 프리패치할 수 있습니다. 기본적으로 쿼리의 첫 번째 페이지만 프리패치되어 지정된 QueryKey 하에 저장됩니다. 한 페이지 이상을 프리패치하고 싶다면 `pages` 옵션을 사용할 수 있습니다. 자세한 내용은 [프리패칭 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)를 참고하세요.

### `useQueries`용 새로운 `combine` 옵션

자세한 내용은 [useQueries 문서](https://tanstack.com/query/latest/docs/framework/react/reference/useQueries.md#combine)를 확인하세요.

### 실험적 `fine grained storage persister`

자세한 내용은 [experimental_createPersister 문서](https://tanstack.com/query/latest/docs/framework/react/plugins/createPersister.md)를 참고하세요.

[//]: # 'FrameworkSpecificNewFeatures'

### 타입 안전한 Query Options 생성 방식

자세한 내용은 [TypeScript 문서](https://tanstack.com/query/latest/docs/framework/react/typescript.md#typing-query-options)를 참고하세요.

### 서스펜스를 위한 새로운 훅

v5에서는 데이터 페칭에 대한 서스펜스가 마침내 “안정” 상태가 되었습니다. `useSuspenseQuery`, `useSuspenseInfiniteQuery`, `useSuspenseQueries` 훅을 새로 추가했습니다. 이 훅들을 사용하면 타입 수준에서 `data`가 절대 `undefined`가 되지 않습니다.

```js
const { data: post } = useSuspenseQuery({
  // ^? const post: Post
  queryKey: ['post', postId],
  queryFn: () => fetchPost(postId),
})
```

쿼리 훅에서 실험적으로 제공되던 `suspense: boolean` 플래그는 제거되었습니다.

자세한 내용은 [서스펜스 문서](https://tanstack.com/query/latest/docs/framework/react/guides/suspense.md)를 참고하세요.

[//]: # 'FrameworkSpecificNewFeatures'

