---
title: '기본 쿼리 함수'
description: '앱 전체에서 동일한 쿼리 함수를 공유하고 쿼리 키로 가져올 대상을 식별하고 싶다면, TanStack Query에 기본 쿼리 함수를 제공해 그렇게 할 수 있습니다.'
---

# 기본 쿼리 함수

앱 전체에서 동일한 쿼리 함수를 공유하고 쿼리 키로 가져올 대상을 식별하고 싶다면, TanStack Query에 **기본 쿼리 함수**를 제공해 그렇게 할 수 있습니다.

[//]: # 'Example'

```tsx
// Define a default query function that will receive the query key
const defaultQueryFn = async ({ queryKey }) => {
  const { data } = await axios.get(
    `https://jsonplaceholder.typicode.com${queryKey[0]}`,
  )
  return data
}

// provide the default query function to your app with defaultOptions
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      queryFn: defaultQueryFn,
    },
  },
})

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <YourApp />
    </QueryClientProvider>
  )
}

// All you have to do now is pass a key!
function Posts() {
  const { status, data, error, isFetching } = useQuery({ queryKey: ['/posts'] })

  // ...
}

// You can even leave out the queryFn and just go straight into options
function Post({ postId }) {
  const { status, data, error, isFetching } = useQuery({
    queryKey: [`/posts/${postId}`],
    enabled: !!postId,
  })

  // ...
}
```

[//]: # 'Example'

기본 `queryFn`을 언제든지 재정의하고 싶다면, 평소처럼 직접 제공하면 됩니다.

