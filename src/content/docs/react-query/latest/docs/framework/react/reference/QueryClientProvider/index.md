---
title: 'QueryClientProvider'
description: '컴포넌트를 사용해 애플리케이션에 를 연결하고 제공합니다:'
---

# QueryClientProvider

`QueryClientProvider` 컴포넌트를 사용해 애플리케이션에 `QueryClient`를 연결하고 제공합니다:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```

**옵션**

- `client: QueryClient`
  - **필수**
  - 제공할 QueryClient 인스턴스

