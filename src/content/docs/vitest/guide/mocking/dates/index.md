---
title: "날짜 모킹"
description: "테스트 시 일관성을 보장하려면 날짜를 직접 제어해야 할 때가 있습니다. Vitest는 타이머와 시스템 날짜를 조작하기 위해  패키지를 사용합니다. 특정 API에 대한 자세한 내용은 여기에서 확인할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/mocking/dates

# 날짜 모킹

테스트 시 일관성을 보장하려면 날짜를 직접 제어해야 할 때가 있습니다. Vitest는 타이머와 시스템 날짜를 조작하기 위해 [`@sinonjs/fake-timers`](https://github.com/sinonjs/fake-timers) 패키지를 사용합니다. 특정 API에 대한 자세한 내용은 [여기](https://vitest.dev/api/vi#vi-setsystemtime)에서 확인할 수 있습니다.

## 예시

```js
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

const businessHours = [9, 17];

function purchase() {
  const currentHour = new Date().getHours();
  const [open, close] = businessHours;

  if (currentHour > open && currentHour < close) {
    return { message: "Success" };
  }

  return { message: "Error" };
}

describe("purchasing flow", () => {
  beforeEach(() => {
    // tell vitest we use mocked time
    vi.useFakeTimers();
  });

  afterEach(() => {
    // restoring date after each test run
    vi.useRealTimers();
  });

  it("allows purchases within business hours", () => {
    // set hour within business hours
    const date = new Date(2000, 1, 1, 13);
    vi.setSystemTime(date);

    // access Date.now() will result in the date set above
    expect(purchase()).toEqual({ message: "Success" });
  });

  it("disallows purchases outside of business hours", () => {
    // set hour outside business hours
    const date = new Date(2000, 1, 1, 19);
    vi.setSystemTime(date);

    // access Date.now() will result in the date set above
    expect(purchase()).toEqual({ message: "Error" });
  });
});
```
