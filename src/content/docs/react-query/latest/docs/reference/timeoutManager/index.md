---
title: 'TimeoutManager'
description: '는 TanStack Query에서 과  타이머를 처리합니다.'
---

# TimeoutManager

`TimeoutManager`는 TanStack Query에서 `setTimeout`과 `setInterval` 타이머를 처리합니다.

TanStack Query는 쿼리의 `staleTime`, `gcTime`, 재시도, 스로틀링, 디바운스와 같은 기능을 구현하기 위해 타이머를 사용합니다.

기본적으로 TimeoutManager는 전역 `setTimeout`과 `setInterval`을 사용하지만, 대신 커스텀 구현을 사용하도록 구성할 수 있습니다.

사용 가능한 메서드는 다음과 같습니다.

- [`timeoutManager.setTimeoutProvider`](#timeoutmanagersettimeoutprovider)
  - [`TimeoutProvider`](#timeoutprovider)
- [`timeoutManager.setTimeout`](#timeoutmanagersettimeout)
- [`timeoutManager.clearTimeout`](#timeoutmanagercleartimeout)
- [`timeoutManager.setInterval`](#timeoutmanagersetinterval)
- [`timeoutManager.clearInterval`](#timeoutmanagerclearinterval)

## `timeoutManager.setTimeoutProvider`

`setTimeoutProvider`는 `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval` 함수를 커스텀 구현으로 교체하는 데 사용할 수 있으며, 이를 `TimeoutProvider`라고 합니다.

수천 개의 쿼리로 인해 이벤트 루프 성능 문제가 발생하는 것이 보이면 유용할 수 있습니다. 커스텀 TimeoutProvider는 전역 `setTimeout`의 최대 지연 값(약 [24일](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout#maximum_delay_value))보다 긴 타이머 지연도 지원할 수 있습니다.

서로 다른 TimeoutProvider는 서로의 타이머를 취소할 수 없으므로, 모든 타이머에서 동일한 프로바이더를 일관되게 사용하도록 QueryClient나 쿼리를 생성하기 전에 `setTimeoutProvider`를 호출하는 것이 중요합니다.

```tsx
import { timeoutManager, QueryClient } from '@tanstack/react-query'
import { CustomTimeoutProvider } from './CustomTimeoutProvider'

timeoutManager.setTimeoutProvider(new CustomTimeoutProvider())

export const queryClient = new QueryClient()
```

### `TimeoutProvider`

타이머는 성능에 매우 민감합니다. 지연이 5초 미만인 단기 타이머는 일반적으로 레이턴시에 민감하며, 장기 타이머는 [계층형 타임 휠](https://www.npmjs.com/package/timer-wheel)과 같은 자료 구조를 이용해 유사한 마감 시점을 묶는 [타이머 코얼레싱](https://en.wikipedia.org/wiki/Timer_coalescing)으로부터 더 많은 이점을 얻을 수 있습니다.

`TimeoutProvider` 타입은 구현이 [Symbol.toPrimitive][toPrimitive]를 통해 `number`로 변환 가능한 타이머 ID 객체를 처리하도록 요구합니다. 이는 NodeJS와 같은 런타임이 전역 `setTimeout`과 `setInterval`에서 [객체][nodejs-timeout]를 반환하기 때문입니다. TimeoutProvider 구현체는 내부적으로 타이머 ID를 number로 강제 변환해도 되고, `{ [Symbol.toPrimitive]: () => number }`를 구현한 자체 커스텀 객체 타입을 반환해도 됩니다.

[nodejs-timeout]: https://nodejs.org/api/timers.html#class-timeout  
[toPrimitive]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive

```tsx
type ManagedTimerId = number | { [Symbol.toPrimitive]: () => number }

type TimeoutProvider<TTimerId extends ManagedTimerId = ManagedTimerId> = {
  readonly setTimeout: (callback: TimeoutCallback, delay: number) => TTimerId
  readonly clearTimeout: (timeoutId: TTimerId | undefined) => void

  readonly setInterval: (callback: TimeoutCallback, delay: number) => TTimerId
  readonly clearInterval: (intervalId: TTimerId | undefined) => void
}
```

## `timeoutManager.setTimeout`

`setTimeout(callback, delayMs)`는 전역 [setTimeout 함수](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)처럼 약 `delay` 밀리초 후에 콜백을 실행하도록 예약합니다. 이 콜백은 `timeoutManager.clearTimeout`으로 취소할 수 있습니다.

이 메서드는 타이머 ID를 반환하며, 이는 숫자이거나 [Symbol.toPrimitive][toPrimitive]를 통해 숫자로 변환 가능한 객체일 수 있습니다.

```tsx
import { timeoutManager } from '@tanstack/react-query'

const timeoutId = timeoutManager.setTimeout(
  () => console.log('ran at:', new Date()),
  1000,
)

const timeoutIdNumber: number = Number(timeoutId)
```

## `timeoutManager.clearTimeout`

`clearTimeout(timerId)`는 전역 [clearTimeout 함수](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearTimeout)처럼 `setTimeout`으로 예약된 타임아웃 콜백을 취소합니다. `timeoutManager.setTimeout`이 반환한 타이머 ID로 호출해야 합니다.

```tsx
import { timeoutManager } from '@tanstack/react-query'

const timeoutId = timeoutManager.setTimeout(
  () => console.log('ran at:', new Date()),
  1000,
)

timeoutManager.clearTimeout(timeoutId)
```

## `timeoutManager.setInterval`

`setInterval(callback, intervalMs)`는 전역 [setInterval 함수](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)처럼 약 `intervalMs`마다 콜백을 호출하도록 예약합니다.

`setTimeout`과 마찬가지로 타이머 ID를 반환하며, 이는 숫자이거나 [Symbol.toPrimitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)를 통해 숫자로 변환 가능한 객체일 수 있습니다.

```tsx
import { timeoutManager } from '@tanstack/react-query'

const intervalId = timeoutManager.setInterval(
  () => console.log('ran at:', new Date()),
  1000,
)
```

## `timeoutManager.clearInterval`

`clearInterval(intervalId)`는 전역 [clearInterval 함수](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearInterval)처럼 인터벌을 취소하는 데 사용할 수 있습니다. `timeoutManager.setInterval`이 반환한 인터벌 ID로 호출해야 합니다.

```tsx
import { timeoutManager } from '@tanstack/react-query'

const intervalId = timeoutManager.setInterval(
  () => console.log('ran at:', new Date()),
  1000,
)

timeoutManager.clearInterval(intervalId)
```

