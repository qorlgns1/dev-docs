---
title: 'QueryErrorResetBoundary'
description: '쿼리에서 suspense 또는 throwOnError를 사용할 때는 오류 발생 후 다시 렌더링하면서 재시도를 원한다는 사실을 쿼리에 알려줄 방법이 필요합니다.  컴포넌트를 사용하면 해당 컴포넌트의 경계 내에서 어떤 쿼리 오류든 초기화할 수 있습니다.'
---

# QueryErrorResetBoundary

쿼리에서 **suspense** 또는 **throwOnError**를 사용할 때는 오류 발생 후 다시 렌더링하면서 재시도를 원한다는 사실을 쿼리에 알려줄 방법이 필요합니다. `QueryErrorResetBoundary` 컴포넌트를 사용하면 해당 컴포넌트의 경계 내에서 어떤 쿼리 오류든 초기화할 수 있습니다.

```tsx
import { QueryErrorResetBoundary } from '@tanstack/react-query'
import { ErrorBoundary } from 'react-error-boundary'

const App = () => (
  <QueryErrorResetBoundary>
    {({ reset }) => (
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
    )}
  </QueryErrorResetBoundary>
)
```

