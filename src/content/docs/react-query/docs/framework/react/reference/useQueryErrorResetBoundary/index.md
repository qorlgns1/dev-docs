---
title: 'useQueryErrorResetBoundary'
description: '이 훅은 가장 가까운  안에서 발생한 모든 쿼리 오류를 재설정합니다. 경계가 정의되어 있지 않은 경우 전역적으로 오류를 재설정합니다:'
---

# useQueryErrorResetBoundary

이 훅은 가장 가까운 `QueryErrorResetBoundary` 안에서 발생한 모든 쿼리 오류를 재설정합니다. 경계가 정의되어 있지 않은 경우 전역적으로 오류를 재설정합니다:

```tsx
import { useQueryErrorResetBoundary } from '@tanstack/react-query'
import { ErrorBoundary } from 'react-error-boundary'

const App = () => {
  const { reset } = useQueryErrorResetBoundary()
  return (
    <ErrorBoundary
      onReset={reset}
      fallbackRender={({ resetErrorBoundary }) => (
        <div>
          There was an error!
          <Button onClick={() => resetErrorBoundary()}>Try again</Button>
        </div>
      )}
    >
      <Page />
    </ErrorBoundary>
  )
}
```

