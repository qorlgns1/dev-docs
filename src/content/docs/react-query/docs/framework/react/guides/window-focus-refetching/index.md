---
title: 'Window Focus Refetching'
description: '사용자가 애플리케이션을 떠났다가 돌아왔을 때 쿼리 데이터가 오래되었다면, TanStack Query가 백그라운드에서 자동으로 최신 데이터를 가져옵니다. 이 동작은  옵션을 사용해 전역 또는 쿼리별로 비활성화할 수 있습니다.'
---

# Window Focus Refetching

사용자가 애플리케이션을 떠났다가 돌아왔을 때 쿼리 데이터가 오래되었다면, **TanStack Query가 백그라운드에서 자동으로 최신 데이터를 가져옵니다.** 이 동작은 `refetchOnWindowFocus` 옵션을 사용해 전역 또는 쿼리별로 비활성화할 수 있습니다.

#### Disabling Globally

[//]: # 'Example'

```tsx
//
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false, // default: true
    },
  },
})

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```

[//]: # 'Example'

#### Disabling Per-Query

[//]: # 'Example2'

```tsx
useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodos,
  refetchOnWindowFocus: false,
})
```

[//]: # 'Example2'

## Custom Window Focus Event

드물게는 창 포커스 이벤트를 직접 관리하여 TanStack Query가 다시 검증하도록 만들고 싶을 수 있습니다. 이때 TanStack Query는 창에 포커스가 맞춰졌을 때 실행해야 하는 콜백을 제공하고 사용자가 직접 이벤트를 설정할 수 있게 해주는 `focusManager.setEventListener` 함수를 제공합니다. `focusManager.setEventListener`를 호출하면 이전에 설정된 핸들러(대부분 기본 핸들러)가 제거되고 새 핸들러가 대신 사용됩니다. 예를 들어, 다음은 기본 핸들러입니다.

[//]: # 'Example3'

```tsx
focusManager.setEventListener((handleFocus) => {
  // Listen to visibilitychange
  if (typeof window !== 'undefined' && window.addEventListener) {
    const visibilitychangeHandler = () => {
      handleFocus(document.visibilityState === 'visible')
    }
    window.addEventListener('visibilitychange', visibilitychangeHandler, false)
    return () => {
      // Be sure to unsubscribe if a new handler is set
      window.removeEventListener('visibilitychange', visibilitychangeHandler)
    }
  }
})
```

[//]: # 'Example3'
[//]: # 'ReactNative'

## Managing Focus in React Native

`window` 이벤트 리스너 대신 React Native는 [`AppState` 모듈](https://reactnative.dev/docs/appstate#app-states)을 통해 포커스 정보를 제공합니다. 앱 상태가 "active"로 변경될 때 업데이트를 트리거하려면 `AppState`의 "change" 이벤트를 사용할 수 있습니다.

```tsx
import { AppState } from 'react-native'
import { focusManager } from '@tanstack/react-query'

function onAppStateChange(status: AppStateStatus) {
  if (Platform.OS !== 'web') {
    focusManager.setFocused(status === 'active')
  }
}

useEffect(() => {
  const subscription = AppState.addEventListener('change', onAppStateChange)

  return () => subscription.remove()
}, [])
```

[//]: # 'ReactNative'

## Managing focus state

[//]: # 'Example4'

```tsx
import { focusManager } from '@tanstack/react-query'

// Override the default focus state
focusManager.setFocused(true)

// Fallback to the default focus check
focusManager.setFocused(undefined)
```

[//]: # 'Example4'

