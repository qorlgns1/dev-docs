---
title: "fakeTimers"
description: "지정한 Unix epoch으로 fake timer를 설치합니다."
---

출처 URL: https://vitest.dev/config/faketimers

# fakeTimers

- **타입:** `FakeTimerInstallOpts`

[`vi.useFakeTimers()`](https://vitest.dev/api/vi#vi-usefaketimers)을 사용할 때 Vitest가 [`@sinon/fake-timers`](https://www.npmjs.com/package/@sinonjs/fake-timers)에 전달하는 옵션입니다.

## fakeTimers.now

- **타입:** `number | Date`
- **기본값:** `Date.now()`

지정한 Unix epoch으로 fake timer를 설치합니다.

## fakeTimers.toFake

- **타입:** `('setTimeout' | 'clearTimeout' | 'setImmediate' | 'clearImmediate' | 'setInterval' | 'clearInterval' | 'Date' | 'nextTick' | 'hrtime' | 'requestAnimationFrame' | 'cancelAnimationFrame' | 'requestIdleCallback' | 'cancelIdleCallback' | 'performance' | 'queueMicrotask')[]`
- **기본값:** `nextTick` 및 `queueMicrotask`를 제외한 전역에서 사용 가능한 모든 항목

fake 처리할 전역 메서드와 API 이름 배열입니다.

`setTimeout()`과 `nextTick()`만 모킹하려면 이 속성을 `['setTimeout', 'nextTick']`로 지정하세요.

`--pool=forks`를 사용해 `node:child_process` 내부에서 Vitest를 실행하는 경우 `nextTick` 모킹은 지원되지 않습니다. NodeJS는 `node:child_process` 내부적으로 `process.nextTick`을 사용하므로, 이를 모킹하면 멈추게 됩니다. `--pool=threads`로 Vitest를 실행하는 경우에는 `nextTick` 모킹이 지원됩니다.

## fakeTimers.loopLimit

- **타입:** `number`
- **기본값:** `10_000`

[`vi.runAllTimers()`](https://vitest.dev/api/vi#vi-runalltimers) 호출 시 실행될 timer의 최대 개수입니다.

## fakeTimers.shouldAdvanceTime

- **타입:** `boolean`
- **기본값:** `false`

실제 시스템 시간 변화에 따라 모킹된 시간을 자동으로 증가시키도록 @sinonjs/fake-timers에 지시합니다(예: 실제 시스템 시간이 20ms 변할 때마다 모킹된 시간도 20ms 증가).

## fakeTimers.advanceTimeDelta

- **타입:** `number`
- **기본값:** `20`

`shouldAdvanceTime: true`와 함께 사용할 때만 관련됩니다. 실제 시스템 시간이 `advanceTimeDelta`ms 변할 때마다 모킹된 시간을 `advanceTimeDelta`ms만큼 증가시킵니다.

## fakeTimers.shouldClearNativeTimers

- **타입:** `boolean`
- **기본값:** `true`

각각의 핸들러에 위임하여 "native"(즉, fake가 아닌) timer를 정리하도록 fake timer에 지시합니다. 비활성화하면 fake timer 세션 시작 전에 존재하던 timer로 인해 예상치 못한 동작이 발생할 수 있습니다.
