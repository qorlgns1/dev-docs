---
title: "Mocking Globals"
description: "기본적으로 Vitest는 이러한 전역값을 재설정하지 않지만, 각 테스트 후 원래 값을 복원하도록 설정에서  옵션을 켜거나 를 수동으로 호출할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/mocking/globals

# Mocking Globals

[`vi.stubGlobal`](https://vitest.dev/api/vi#vi-stubglobal) 헬퍼를 사용하면 `jsdom` 또는 `node`에 존재하지 않는 전역 변수를 모킹할 수 있습니다. 이 헬퍼는 전역 변수의 값을 `globalThis` 객체에 넣습니다.

기본적으로 Vitest는 이러한 전역값을 재설정하지 않지만, 각 테스트 후 원래 값을 복원하도록 설정에서 [`unstubGlobals`](https://vitest.dev/config/#unstubglobals) 옵션을 켜거나 [`vi.unstubAllGlobals()`](https://vitest.dev/api/vi#vi-unstuballglobals)를 수동으로 호출할 수 있습니다.

```ts
import { vi } from "vitest";

const IntersectionObserverMock = vi.fn(
  class {
    disconnect = vi.fn();
    observe = vi.fn();
    takeRecords = vi.fn();
    unobserve = vi.fn();
  },
);

vi.stubGlobal("IntersectionObserver", IntersectionObserverMock);

// now you can access it as `IntersectionObserver` or `window.IntersectionObserver`
```
