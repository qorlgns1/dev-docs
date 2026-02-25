---
title: 'streamedQuery'
description: '는 AsyncIterable에서 데이터를 스트리밍하는 쿼리 함수를 만들기 위한 헬퍼 함수입니다. 데이터는 수신된 모든 청크를 담은 배열이 됩니다. 첫 번째 데이터 청크를 받을 때까지 쿼리는  상태로 유지되지만, 그 이후에는 로 전환됩니다. 스트림이 끝날 때까지 쿼리의 ...'
---

# streamedQuery

`streamedQuery`는 [AsyncIterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)에서 데이터를 스트리밍하는 쿼리 함수를 만들기 위한 헬퍼 함수입니다. 데이터는 수신된 모든 청크를 담은 배열이 됩니다. 첫 번째 데이터 청크를 받을 때까지 쿼리는 `pending` 상태로 유지되지만, 그 이후에는 `success`로 전환됩니다. 스트림이 끝날 때까지 쿼리의 fetchStatus는 `fetching`으로 유지됩니다.

`streamedQuery`가 실제로 어떻게 동작하는지 확인하려면 [GitHub의 examples/react/chat 디렉터리](https://github.com/TanStack/query/tree/main/examples/react/chat)에 있는 채팅 예제를 참고하세요.

```tsx
import { experimental_streamedQuery as streamedQuery } from '@tanstack/react-query'

const query = queryOptions({
  queryKey: ['data'],
  queryFn: streamedQuery({
    streamFn: fetchDataInChunks,
  }),
})
```

> 참고: `streamedQuery`는 커뮤니티 피드백을 수집하기 위해 현재 `experimental`로 표시되어 있습니다. API를 사용해 보고 의견이 있다면 이 [GitHub 토론](https://github.com/TanStack/query/discussions/9065)에 남겨 주세요.

**Options**

- `streamFn: (context: QueryFunctionContext) => Promise<AsyncIterable<TData>>`
  - **필수**
  - 스트리밍할 데이터를 담은 AsyncIterable을 반환하는 Promise를 돌려주는 함수입니다.
  - [QueryFunctionContext](https://tanstack.com/query/latest/docs/framework/react/guides/query-functions.md#queryfunctioncontext)를 인자로 받습니다.
- `refetchMode?: 'append' | 'reset' | 'replace'`
  - 선택 사항
  - 재조회가 처리되는 방식을 정의합니다.
  - 기본값은 `'reset'`입니다.
  - `'reset'`으로 설정하면 쿼리는 모든 데이터를 지우고 `pending` 상태로 돌아갑니다.
  - `'append'`로 설정하면 기존 데이터에 새 데이터가 추가됩니다.
  - `'replace'`로 설정하면 스트림이 끝난 후 모든 데이터가 캐시에 기록됩니다.
- `reducer?: (accumulator: TData, chunk: TQueryFnData) => TData`
  - 선택 사항
  - 스트리밍된 청크(`TQueryFnData`)를 최종 데이터 형태(`TData`)로 축약합니다.
  - 기본값: `TData`가 배열일 때 각 청크를 누산기의 끝에 추가합니다.
  - `TData`가 배열이 아니라면 사용자 지정 `reducer`를 제공해야 합니다.
- `initialValue?: TData = TQueryFnData`
  - 선택 사항
  - 첫 번째 청크가 페치되는 동안 사용할 초기 데이터를 정의하며, 스트림이 값을 내지 않을 때도 반환됩니다.
  - 사용자 지정 `reducer`를 제공하는 경우 필수입니다.
  - 기본값은 빈 배열입니다.

