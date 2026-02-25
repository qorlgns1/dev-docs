---
title: 'FocusManager'
description: '는 TanStack Query 내부의 포커스 상태를 관리합니다.'
---

# FocusManager

`FocusManager`는 TanStack Query 내부의 포커스 상태를 관리합니다.

기본 이벤트 리스너를 변경하거나 포커스 상태를 수동으로 변경할 때 사용할 수 있습니다.

사용 가능한 메서드는 다음과 같습니다:

- [`setEventListener`](#focusmanagerseteventlistener)
- [`subscribe`](#focusmanagersubscribe)
- [`setFocused`](#focusmanagersetfocused)
- [`isFocused`](#focusmanagerisfocused)

## `focusManager.setEventListener`

`setEventListener`는 커스텀 이벤트 리스너를 설정할 때 사용할 수 있습니다:

```tsx
import { focusManager } from '@tanstack/react-query'

focusManager.setEventListener((handleFocus) => {
  // Listen to visibilitychange
  if (typeof window !== 'undefined' && window.addEventListener) {
    window.addEventListener('visibilitychange', handleFocus, false)
  }

  return () => {
    // Be sure to unsubscribe if a new handler is set
    window.removeEventListener('visibilitychange', handleFocus)
  }
})
```

## `focusManager.subscribe`

`subscribe`는 가시성 상태의 변화를 구독할 때 사용할 수 있습니다. 언구독 함수(unsubscribe function)를 반환합니다:

```tsx
import { focusManager } from '@tanstack/react-query'

const unsubscribe = focusManager.subscribe((isVisible) => {
  console.log('isVisible', isVisible)
})
```

## `focusManager.setFocused`

`setFocused`는 포커스 상태를 수동으로 설정할 때 사용할 수 있습니다. 기본 포커스 체크로 돌아가려면 `undefined`를 설정하세요.

```tsx
import { focusManager } from '@tanstack/react-query'

// Set focused
focusManager.setFocused(true)

// Set unfocused
focusManager.setFocused(false)

// Fallback to the default focus check
focusManager.setFocused(undefined)
```

**옵션**

- `focused: boolean | undefined`

## `focusManager.isFocused`

`isFocused`는 현재 포커스 상태를 가져올 때 사용할 수 있습니다.

```tsx
const isFocused = focusManager.isFocused()
```

