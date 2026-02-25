---
title: 'useSuspenseQueries'
description: 'const result = useSuspenseQueries(options)'
---

<!-- Skipping add-doc skill because the user only requested translation, not the full add/update workflow. -->

# useSuspenseQueries

```tsx
const result = useSuspenseQueries(options)
```

**옵션**

각 `query`마다 다음을 포함할 수 없다는 점을 제외하면 [useQueries](https://tanstack.com/query/latest/docs/framework/react/reference/useQueries.md)와 동일합니다.

- `suspense`
- `throwOnError`
- `enabled`
- `placeholderData`

**반환값**

각 `query`에 대해 다음과 같은 차이가 있다는 점을 제외하면 [useQueries](https://tanstack.com/query/latest/docs/framework/react/reference/useQueries.md)와 동일한 구조입니다.

- `data`는 반드시 정의되어 있습니다.
- `isPlaceholderData`는 제공되지 않습니다.
- `status`는 `success` 또는 `error`이며
  - 이에 따라 파생 플래그가 설정됩니다.

**주의사항**

**모든 쿼리**가 로딩을 완료한 뒤에만 컴포넌트가 다시 마운트된다는 점을 기억하세요. 따라서 전체 쿼리가 완료될 때까지 걸린 시간 동안 특정 쿼리가 오래된 상태가 되었다면, 재마운트 시 다시 페치됩니다. 이를 피하려면 충분히 큰 `staleTime`을 설정하세요.

[취소](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md)는 작동하지 않습니다.

