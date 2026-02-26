---
title: '첫 번째 테스트'
description: 'React Query는 우리가 제공하는 훅이나 이를 감싸는 커스텀 훅을 통해 동작합니다.'
---

# 테스트

React Query는 우리가 제공하는 훅이나 이를 감싸는 커스텀 훅을 통해 동작합니다.

React 17 이하에서는 이러한 커스텀 훅의 단위 테스트를 [React Hooks Testing Library](https://react-hooks-testing-library.com/)로 작성할 수 있습니다.

다음 명령으로 설치하세요:

```sh
npm install @testing-library/react-hooks react-test-renderer --save-dev
```

(`react-test-renderer` 라이브러리는 `@testing-library/react-hooks`의 피어 의존성이므로, 사용 중인 React 버전과 맞춰 설치해야 합니다.)

_참고_: React 18 이상에서는 `renderHook`이 `@testing-library/react` 패키지에 직접 포함되므로 `@testing-library/react-hooks`가 더 이상 필요하지 않습니다.

## 첫 번째 테스트

설치가 끝났다면 간단한 테스트를 작성할 수 있습니다. 다음과 같은 커스텀 훅이 있다고 가정해 봅시다:

```tsx
export function useCustomHook() {
  return useQuery({ queryKey: ['customHook'], queryFn: () => 'Hello' })
}
```

이 훅을 위한 테스트는 다음과 같이 작성할 수 있습니다:

```tsx
import { renderHook, waitFor } from '@testing-library/react'

const queryClient = new QueryClient()
const wrapper = ({ children }) => (
  <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
)

const { result } = renderHook(() => useCustomHook(), { wrapper })

await waitFor(() => expect(result.current.isSuccess).toBe(true))

expect(result.current.data).toEqual('Hello')
```

`QueryClient`와 `QueryClientProvider`를 생성하는 커스텀 래퍼를 제공한다는 점에 주목하세요. 이렇게 하면 테스트가 다른 테스트와 완전히 분리된 상태로 유지됩니다.

이 래퍼를 한 번만 작성할 수도 있지만, 그 경우 각 테스트 전에 `QueryClient`를 초기화하고 테스트가 병렬로 실행되지 않도록 해야 합니다. 그렇지 않으면 한 테스트가 다른 테스트 결과에 영향을 줍니다.

## 재시도 끄기

라이브러리는 기본값으로 지수 백오프를 포함한 세 번의 재시도를 수행하므로, 오류가 발생하는 쿼리를 테스트할 때 테스트가 타임아웃될 가능성이 있습니다. 재시도를 끄는 가장 쉬운 방법은 QueryClientProvider를 이용하는 것입니다. 위 예제를 확장해 봅시다:

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // ✅ turns retries off
      retry: false,
    },
  },
})
const wrapper = ({ children }) => (
  <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
)
```

이렇게 하면 컴포넌트 트리의 모든 쿼리에 대한 기본값이 “재시도 없음”으로 설정됩니다. 실제 `useQuery`에 명시적으로 재시도를 설정하지 않은 경우에만 동작한다는 점이 중요합니다. 예를 들어 특정 쿼리가 재시도 5회를 요구하면, 기본값은 폴백일 뿐이므로 해당 쿼리 설정이 우선합니다.

## Jest에서 gcTime을 Infinity로 설정하기

Jest를 사용할 경우 `gcTime`을 `Infinity`로 설정하면 “Jest did not exit one second after the test run completed” 오류 메시지를 방지할 수 있습니다. 이는 서버에서의 기본 동작이며, 명시적으로 `gcTime`을 설정할 때만 필요합니다.

## 네트워크 호출 테스트

React Query의 주요 목적은 네트워크 요청을 캐싱하는 것이므로, 코드가 올바른 네트워크 요청을 수행하는지 테스트하는 것이 중요합니다.

테스트 방법은 다양하지만, 여기서는 [nock](https://www.npmjs.com/package/nock)을 사용해 보겠습니다.

다음과 같은 커스텀 훅이 있다고 가정합시다:

```tsx
function useFetchData() {
  return useQuery({
    queryKey: ['fetchData'],
    queryFn: () => request('/api/data'),
  })
}
```

이 훅을 위한 테스트는 다음과 같이 작성할 수 있습니다:

```tsx
const queryClient = new QueryClient()
const wrapper = ({ children }) => (
  <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
)

const expectation = nock('http://example.com').get('/api/data').reply(200, {
  answer: 42,
})

const { result } = renderHook(() => useFetchData(), { wrapper })

await waitFor(() => expect(result.current.isSuccess).toBe(true))

expect(result.current.data).toEqual({ answer: 42 })
```

여기서는 `waitFor`를 사용해 쿼리 상태가 요청 성공을 나타낼 때까지 기다립니다. 이렇게 하면 훅이 완료되었고 올바른 데이터를 갖고 있다는 것을 확인할 수 있습니다. _참고_: React 18을 사용할 때 `waitFor`의 의미론이 앞서 언급한 대로 변경되었습니다.

## Load More / 무한 스크롤 테스트

먼저 API 응답을 모킹해야 합니다.

```tsx
function generateMockedResponse(page) {
  return {
    page: page,
    items: [...]
  }
}
```

그다음 `nock` 구성은 페이지에 따라 응답을 구분해야 하며, 이를 위해 `uri`를 사용할 것입니다. 여기서 `uri` 값은 `"/?page=1"` 또는 `"/?page=2"` 같은 형태입니다.

```tsx
const expectation = nock('http://example.com')
  .persist()
  .query(true)
  .get('/api/data')
  .reply(200, (uri) => {
    const url = new URL(`http://example.com${uri}`)
    const { page } = Object.fromEntries(url.searchParams)
    return generateMockedResponse(page)
  })
```

(여러 번 같은 엔드포인트를 호출하므로 `.persist()`를 사용합니다.)

이제 안심하고 테스트를 실행할 수 있습니다. 핵심은 데이터 단정문이 통과할 때까지 기다리는 것입니다:

```tsx
const { result } = renderHook(() => useInfiniteQueryCustomHook(), {
  wrapper,
})

await waitFor(() => expect(result.current.isSuccess).toBe(true))

expect(result.current.data.pages).toStrictEqual(generateMockedResponse(1))

result.current.fetchNextPage()

await waitFor(() =>
  expect(result.current.data.pages).toStrictEqual([
    ...generateMockedResponse(1),
    ...generateMockedResponse(2),
  ]),
)

expectation.done()
```

_참고_: React 18을 사용할 때 `waitFor`의 의미론이 앞서 언급한 대로 변경되었습니다.

## 추가 읽을거리

`mock-service-worker`를 사용하는 대체 설정과 추가 팁은 [TkDodo의 Testing React Query 글](https://tkdodo.eu/blog/testing-react-query)을 참고하세요.

