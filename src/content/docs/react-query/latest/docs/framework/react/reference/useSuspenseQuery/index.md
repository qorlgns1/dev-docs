---
title: 'useSuspenseQuery'
description: 'const result = useSuspenseQuery(options)'
---

# useSuspenseQuery

```tsx
const result = useSuspenseQuery(options)
```

**옵션**

[useQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)와 동일하지만 다음 옵션은 예외입니다:

- `throwOnError`
- `enabled`
- `placeholderData`

**반환값**

[useQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)와 같은 객체를 반환하지만 다음이 다릅니다:

- `data`가 항상 정의되어 있습니다.
- `isPlaceholderData`가 없습니다.
- `status`는 `success` 또는 `error` 중 하나이며,
  - 이에 따라 파생 플래그가 설정됩니다.

**주의 사항**

[Cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md)이 동작하지 않습니다.

