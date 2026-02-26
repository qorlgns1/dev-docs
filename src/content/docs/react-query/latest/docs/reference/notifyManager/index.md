---
title: 'NotifyManager'
description: '는 TanStack Query에서 콜백의 스케줄링과 배치를 처리합니다.'
---

# NotifyManager

`notifyManager`는 TanStack Query에서 콜백의 스케줄링과 배치를 처리합니다.

다음 메서드를 제공합니다:

- [batch](#notifymanagerbatch)
- [batchCalls](#notifymanagerbatchcalls)
- [schedule](#notifymanagerschedule)
- [setNotifyFunction](#notifymanagersetnotifyfunction)
- [setBatchNotifyFunction](#notifymanagersetbatchnotifyfunction)
- [setScheduler](#notifymanagersetscheduler)

## `notifyManager.batch`

`batch`는 전달된 콜백 내부에서 스케줄된 모든 업데이트를 한 번에 배치하는 데 사용할 수 있습니다. 주로 queryClient 업데이트를 최적화하기 위해 내부적으로 사용됩니다.

```ts
function batch<T>(callback: () => T): T
```

## `notifyManager.batchCalls`

`batchCalls`는 콜백을 받아 래핑하는 고차 함수입니다. 래핑된 함수를 호출하면 모든 호출이 다음 배치에서 콜백을 실행하도록 스케줄됩니다.

```ts
type BatchCallsCallback<T extends Array<unknown>> = (...args: T) => void

function batchCalls<T extends Array<unknown>>(
  callback: BatchCallsCallback<T>,
): BatchCallsCallback<T>
```

## `notifyManager.schedule`

`schedule`은 다음 배치에서 실행할 함수를 스케줄합니다. 기본적으로 배치는 setTimeout을 통해 실행되지만, 필요에 따라 구성할 수 있습니다.

```ts
function schedule(callback: () => void): void
```

## `notifyManager.setNotifyFunction`

`setNotifyFunction`은 notify 함수를 재정의합니다. 이 함수는 실행 시점에 콜백을 전달받으며, 기본 notifyFunction은 단순히 해당 콜백을 호출합니다.

예를 들어 테스트를 실행할 때 알림을 `React.act`로 감싸고 싶다면 이 기능을 사용할 수 있습니다:

```ts
import { notifyManager } from '@tanstack/react-query'
import { act } from 'react-dom/test-utils'

notifyManager.setNotifyFunction(act)
```

## `notifyManager.setBatchNotifyFunction`

`setBatchNotifyFunction`은 배치된 업데이트에 사용할 함수를 설정합니다.

프레임워크에서 사용자 정의 배치 함수를 지원한다면 notifyManager.setBatchNotifyFunction을 호출하여 TanStack Query에 이를 알릴 수 있습니다.

예를 들어 solid-query에서는 다음과 같이 배치 함수를 설정합니다:

```ts
import { notifyManager } from '@tanstack/query-core'
import { batch } from 'solid-js'

notifyManager.setBatchNotifyFunction(batch)
```

## `notifyManager.setScheduler`

`setScheduler`는 다음 배치가 언제 실행될지 스케줄링하는 사용자 정의 콜백을 구성합니다. 기본 동작은 `setTimeout(callback, 0)`입니다.

```ts
import { notifyManager } from '@tanstack/react-query'

// Schedule batches in the next microtask
notifyManager.setScheduler(queueMicrotask)

// Schedule batches before the next frame is rendered
notifyManager.setScheduler(requestAnimationFrame)

// Schedule batches some time in the future
notifyManager.setScheduler((cb) => setTimeout(cb, 10))
```

