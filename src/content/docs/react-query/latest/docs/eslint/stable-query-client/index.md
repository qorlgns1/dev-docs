---
title: '안정적인 Query Client'
description: 'QueryClient는 QueryCache를 포함하므로, 애플리케이션의 생명주기 동안 QueryClient 인스턴스는 하나만 생성해야 하며 렌더링할 때마다 새 인스턴스를 만들면 안 됩니다.'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/stable-query-client

# 안정적인 Query Client

QueryClient는 QueryCache를 포함하므로, 애플리케이션의 생명주기 동안 QueryClient 인스턴스는 하나만 생성해야 하며 렌더링할 때마다 새 인스턴스를 만들면 안 됩니다.

> 예외: async 함수가 서버에서 한 번만 호출되므로, async Server Component 내부에서 새 QueryClient를 생성하는 것은 허용됩니다.

## 규칙 세부사항

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/stable-query-client": "error" */

function App() {
  const queryClient = new QueryClient()
  return (
    <QueryClientProvider client={queryClient}>
      <Home />
    </QueryClientProvider>
  )
}
```

이 규칙에서 **올바른** 코드 예시:

```tsx
function App() {
  const [queryClient] = useState(() => new QueryClient())
  return (
    <QueryClientProvider client={queryClient}>
      <Home />
    </QueryClientProvider>
  )
}
```

```tsx
const queryClient = new QueryClient()
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Home />
    </QueryClientProvider>
  )
}
```

```tsx
async function App() {
  const queryClient = new QueryClient()
  await queryClient.prefetchQuery(options)
}
```

## 속성

- [x] ✅ 권장
- [x] 🔧 자동 수정 가능

