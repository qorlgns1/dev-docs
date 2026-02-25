---
title: 'useSuspenseQuery'
description: 'const result = useSuspenseQuery(options)'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseQuery

# useSuspenseQuery

```tsx
const result = useSuspenseQuery(options)
```

**Options**

The same as for [useQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md), except for:

- `throwOnError`
- `enabled`
- `placeholderData`

**Returns**

Same object as [useQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md), except that:

- `data` is guaranteed to be defined
- `isPlaceholderData` is missing
- `status` is either `success` or `error`
  - the derived flags are set accordingly.

**Caveat**

[Cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md) does not work.

