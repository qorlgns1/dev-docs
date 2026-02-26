---
title: 'useQueryClient'
description: "import { useQueryClient } from '@tanstack/react-query'"
---

# useQueryClient

`useQueryClient` 훅은 현재 `QueryClient` 인스턴스를 반환합니다.

```tsx
import { useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient(queryClient?: QueryClient)
```

**옵션**

- `queryClient?: QueryClient`
  - 사용자 정의 QueryClient를 사용하려면 이 값을 지정합니다. 그렇지 않으면 가장 가까운 컨텍스트의 인스턴스가 사용됩니다.

