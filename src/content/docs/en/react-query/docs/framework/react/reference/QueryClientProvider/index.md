---
title: 'QueryClientProvider'
description: 'Use the  component to connect and provide a  to your application:'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/reference/QueryClientProvider

# QueryClientProvider

Use the `QueryClientProvider` component to connect and provide a `QueryClient` to your application:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```

**Options**

- `client: QueryClient`
  - **Required**
  - the QueryClient instance to provide

