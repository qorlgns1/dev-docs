---
title: 'useSuspenseInfiniteQuery'
description: 'const result = useSuspenseInfiniteQuery(options)'
---

# useSuspenseInfiniteQuery

```tsx
const result = useSuspenseInfiniteQuery(options)
```

**옵션**

[useInfiniteQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery.md)와 동일하지만 다음 항목이 다릅니다.

- `suspense`
- `throwOnError`
- `enabled`
- `placeholderData`

**반환값**

[useInfiniteQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery.md)와 동일한 객체이지만 다음 차이가 있습니다.

- `data`가 항상 정의됩니다
- `isPlaceholderData`가 제외됩니다
- `status`는 `success` 또는 `error` 중 하나입니다
  - 파생 플래그가 상태에 맞게 설정됩니다.

**주의 사항**

[취소(Cancellation)](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md)는 작동하지 않습니다.

