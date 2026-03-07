---
title: "index"
description: 'timeout 또는 interval이 포함된 코드를 테스트할 때, 테스트가 시간이 지나기를 기다리거나 timeout되게 두는 대신,  및  호출을 모킹하는 "fake" 타이머를 사용해 테스트를 더 빠르게 실행할 수 있습니다.'
---

출처 URL: https://vitest.dev/guide/mocking/timers

# 타이머

timeout 또는 interval이 포함된 코드를 테스트할 때, 테스트가 시간이 지나기를 기다리거나 timeout되게 두는 대신, `setTimeout` 및 `setInterval` 호출을 모킹하는 "fake" 타이머를 사용해 테스트를 더 빠르게 실행할 수 있습니다.

더 자세한 API 설명은 [`vi.useFakeTimers` API 섹션](https://vitest.dev/api/vi#vi-usefaketimers)을 참고하세요.

## 예제

```js
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

function executeAfterTwoHours(func) {
  setTimeout(func, 1000 * 60 * 60 * 2); // 2 hours
}

function executeEveryMinute(func) {
  setInterval(func, 1000 * 60); // 1 minute
}

const mock = vi.fn(() => console.log("executed"));

describe("delayed execution", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });
  afterEach(() => {
    vi.restoreAllMocks();
  });
  it("should execute the function", () => {
    executeAfterTwoHours(mock);
    vi.runAllTimers();
    expect(mock).toHaveBeenCalledTimes(1);
  });
  it("should not execute the function", () => {
    executeAfterTwoHours(mock);
    // advancing by 2ms won't trigger the func
    vi.advanceTimersByTime(2);
    expect(mock).not.toHaveBeenCalled();
  });
  it("should execute every minute", () => {
    executeEveryMinute(mock);
    vi.advanceTimersToNextTimer();
    expect(mock).toHaveBeenCalledTimes(1);
    vi.advanceTimersToNextTimer();
    expect(mock).toHaveBeenCalledTimes(2);
  });
});
```
