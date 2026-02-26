---
title: 'useQueryClient'
description: 'The  hook returns the current  instance.'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/reference/useQueryClient

# useQueryClient

The `useQueryClient` hook returns the current `QueryClient` instance.

```tsx
import { useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient(queryClient?: QueryClient)
```

**Options**

- `queryClient?: QueryClient`
  - Use this to use a custom QueryClient. Otherwise, the one from the nearest context will be used.

