---
title: 'OnlineManager'
description: '는 TanStack Query에서 온라인 상태를 관리합니다. 기본 이벤트 리스너를 변경하거나 온라인 상태를 수동으로 바꾸는 데 사용할 수 있습니다.'
---

# OnlineManager

`OnlineManager`는 TanStack Query에서 온라인 상태를 관리합니다. 기본 이벤트 리스너를 변경하거나 온라인 상태를 수동으로 바꾸는 데 사용할 수 있습니다.

> 기본적으로 `onlineManager`는 활성 네트워크 연결을 가정하며, 상태 변화를 감지하기 위해 `window` 객체의 `online` 및 `offline` 이벤트를 청취합니다.

> 이전 버전에서는 `navigator.onLine`으로 네트워크 상태를 판단했지만, Chromium 기반 브라우저에서는 잘 동작하지 않습니다. 잘못된 음성(false negative)으로 인해 Query가 부정확하게 `offline`으로 표시되는 [많은 이슈](https://bugs.chromium.org/p/chromium/issues/list?q=navigator.online)가 있습니다.

> 이를 피하기 위해 이제 항상 `online: true`로 시작하고, 상태를 업데이트하기 위해 `online`과 `offline` 이벤트만 청취합니다.

> 이렇게 하면 잘못된 음성 가능성이 줄어들지만, serviceWorker를 통해 로드되어 인터넷 연결 없이도 동작할 수 있는 오프라인 앱에서는 잘못된 양성(false positive)이 발생할 수 있습니다.

사용 가능한 메서드는 다음과 같습니다.

- [`setEventListener`](#onlinemanagerseteventlistener)
- [`subscribe`](#onlinemanagersubscribe)
- [`setOnline`](#onlinemanagersetonline)
- [`isOnline`](#onlinemanagerisonline)

## `onlineManager.setEventListener`

`setEventListener`는 사용자 정의 이벤트 리스너를 설정할 때 사용할 수 있습니다.

```tsx
import NetInfo from '@react-native-community/netinfo'
import { onlineManager } from '@tanstack/react-query'

onlineManager.setEventListener((setOnline) => {
  return NetInfo.addEventListener((state) => {
    setOnline(!!state.isConnected)
  })
})
```

## `onlineManager.subscribe`

`subscribe`는 온라인 상태 변화를 구독하는 데 사용할 수 있습니다. 구독 해지 함수(unsubscribe function)를 반환합니다.

```tsx
import { onlineManager } from '@tanstack/react-query'

const unsubscribe = onlineManager.subscribe((isOnline) => {
  console.log('isOnline', isOnline)
})
```

## `onlineManager.setOnline`

`setOnline`은 온라인 상태를 수동으로 설정하는 데 사용할 수 있습니다.

```tsx
import { onlineManager } from '@tanstack/react-query'

// Set to online
onlineManager.setOnline(true)

// Set to offline
onlineManager.setOnline(false)
```

**Options**

- `online: boolean`

## `onlineManager.isOnline`

`isOnline`은 현재 온라인 상태를 가져오는 데 사용할 수 있습니다.

```tsx
const isOnline = onlineManager.isOnline()
```

