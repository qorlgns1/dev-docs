---
title: 'React Native'
description: 'React Query는 React Native에서도 별도의 설정 없이 바로 사용할 수 있도록 설계되었습니다.'
---

# React Native

React Query는 React Native에서도 별도의 설정 없이 바로 사용할 수 있도록 설계되었습니다.

## DevTools 지원

React Native DevTools 통합에는 다음과 같은 옵션이 있습니다.

1. **네이티브 macOS 앱**: JS 기반 애플리케이션에서 React Query 디버깅을 위한 서드파티 앱:
   https://github.com/LovesWorking/rn-better-dev-tools

2. **Flipper 플러그인**: Flipper 사용자를 위한 서드파티 플러그인:
   https://github.com/bgaleotti/react-query-native-devtools

3. **Reactotron 플러그인**: Reactotron 사용자를 위한 서드파티 플러그인:
   https://github.com/hsndmr/reactotron-react-query

## 온라인 상태 관리

React Query는 웹 브라우저에서 재연결 시 자동으로 refetch를 이미 지원합니다.
React Native에서 동일한 동작을 추가하려면 아래 예시처럼 React Query의 `onlineManager`를 사용해야 합니다.

```tsx
import NetInfo from '@react-native-community/netinfo'
import { onlineManager } from '@tanstack/react-query'

onlineManager.setEventListener((setOnline) => {
  return NetInfo.addEventListener((state) => {
    setOnline(!!state.isConnected)
  })
})
```

또는

```tsx
import { onlineManager } from '@tanstack/react-query'
import * as Network from 'expo-network'

onlineManager.setEventListener((setOnline) => {
  const eventSubscription = Network.addNetworkStateListener((state) => {
    setOnline(!!state.isConnected)
  })
  return eventSubscription.remove
})
```

## 앱 포커스 시 Refetch

React Native에서는 `window` 이벤트 리스너 대신 [`AppState` 모듈](https://reactnative.dev/docs/appstate#app-states)을 통해 포커스 정보를 제공합니다. 앱 상태가 "active"로 바뀔 때 업데이트를 트리거하려면 `AppState`의 "change" 이벤트를 사용할 수 있습니다.

```tsx
import { useEffect } from 'react'
import { AppState, Platform } from 'react-native'
import type { AppStateStatus } from 'react-native'
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

## 화면 포커스 시 Refresh

특정 상황에서는 React Native 화면이 다시 포커스를 받을 때 쿼리를 refetch하고 싶을 수 있습니다.
이 커스텀 훅은 화면이 다시 포커스를 받을 때 **모든 활성 상태의 stale 쿼리**를 refetch합니다.

```tsx
import React from 'react'
import { useFocusEffect } from '@react-navigation/native'
import { useQueryClient } from '@tanstack/react-query'

export function useRefreshOnFocus() {
  const queryClient = useQueryClient()
  const firstTimeRef = React.useRef(true)

  useFocusEffect(
    React.useCallback(() => {
      if (firstTimeRef.current) {
        firstTimeRef.current = false
        return
      }

      // refetch all stale active queries
      queryClient.refetchQueries({
        queryKey: ['posts'],
        stale: true,
        type: 'active',
      })
    }, [queryClient]),
  )
}
```

위 코드에서 첫 번째 포커스(화면이 초기 마운트될 때)는 건너뛰는데, 그 이유는 `useFocusEffect`가 화면 포커스뿐 아니라 마운트 시에도 콜백을 호출하기 때문입니다.

## 포커스를 잃은 화면에서 쿼리 비활성화

화면이 포커스를 잃는 동안 특정 쿼리가 “라이브” 상태로 유지되길 원하지 않는다면 useQuery의 `subscribed` prop을 사용할 수 있습니다. 이 prop을 통해 쿼리가 업데이트 구독을 유지할지 제어할 수 있습니다. React Navigation의 `useIsFocused`와 결합하면 화면이 포커스되지 않을 때 쿼리 구독을 끊고, 다시 포커스를 받을 때 자연스럽게 재구독하도록 만들 수 있습니다.

예시 사용법:

```tsx
import React from 'react'
import { useIsFocused } from '@react-navigation/native'
import { useQuery } from '@tanstack/react-query'
import { Text } from 'react-native'

function MyComponent() {
  const isFocused = useIsFocused()

  const { dataUpdatedAt } = useQuery({
    queryKey: ['key'],
    queryFn: () => fetch(...),
    subscribed: isFocused,
  })

  return <Text>DataUpdatedAt: {dataUpdatedAt}</Text>
}
```

`subscribed`가 false이면 해당 쿼리는 업데이트 구독을 해제하여 해당 화면에서 리렌더를 트리거하거나 새 데이터를 가져오지 않습니다. 다시 true가 되면(예: 화면이 포커스를 되찾을 때) 쿼리가 재구독되어 최신 상태를 유지합니다.

