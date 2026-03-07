---
title: "Mocking"
description: '테스트를 작성하다 보면 내부 또는 외부 서비스의 "가짜" 버전을 만들어야 할 때가 반드시 옵니다. 이를 일반적으로 mocking이라고 합니다. Vitest는  헬퍼를 통해 이를 도와주는 유틸리티 함수를 제공합니다. 에서 import할 수도 있고,  configurati...'
---

출처 URL: https://vitest.dev/guide/mocking

# Mocking

테스트를 작성하다 보면 내부 또는 외부 서비스의 "가짜" 버전을 만들어야 할 때가 반드시 옵니다. 이를 일반적으로 **mocking**이라고 합니다. Vitest는 `vi` 헬퍼를 통해 이를 도와주는 유틸리티 함수를 제공합니다. `vitest`에서 import할 수도 있고, [`global` configuration](https://vitest.dev/config/#globals)이 활성화되어 있다면 전역으로 접근할 수도 있습니다.

::: warning
각 테스트 실행 전후에 mock을 clear 또는 restore해서 실행 간 mock 상태 변경을 되돌리는 것을 항상 잊지 마세요! 자세한 내용은 [`mockReset`](https://vitest.dev/api/mock#mockreset) 문서를 참고하세요.
:::

`vi.fn`, `vi.mock`, `vi.spyOn` 메서드가 익숙하지 않다면 먼저 [API section](https://vitest.dev/api/vi)을 확인하세요.

Vitest는 mocking과 관련된 가이드를 폭넓게 제공합니다:

- 클래스 모킹
- 날짜 모킹
- 파일 시스템 모킹
- 함수 모킹
- 전역값 모킹
- 모듈 모킹
- 요청 모킹
- 타이머 모킹

mocking을 더 간단하고 빠르게 시작하려면 아래 Cheat Sheet를 확인하세요.

## Cheat Sheet

다음을 하고 싶어요…

### export된 변수 모킹

```js [example.js]
export const getter = "variable";
```

```ts [example.test.ts]
import * as exports from "./example.js";

vi.spyOn(exports, "getter", "get").mockReturnValue("mocked");
```

::: warning
이 방법은 Browser Mode에서는 동작하지 않습니다. 우회 방법은 [Limitations](https://vitest.dev/guide/browser/#spying-on-module-exports)를 참고하세요.
:::

### export된 함수 모킹

1. `vi.mock` 사용 예시:

::: warning
`vi.mock` 호출은 파일 최상단으로 hoist된다는 점을 잊지 마세요. 모든 import보다 먼저 항상 실행됩니다.
:::

```ts [example.js]
export function method() {}
```

```ts
import { method } from "./example.js";

vi.mock("./example.js", () => ({
  method: vi.fn(),
}));
```

2. `vi.spyOn` 사용 예시:

```ts
import * as exports from "./example.js";

vi.spyOn(exports, "method").mockImplementation(() => {});
```

::: warning
`vi.spyOn` 예시는 Browser Mode에서 동작하지 않습니다. 우회 방법은 [Limitations](https://vitest.dev/guide/browser/#spying-on-module-exports)를 참고하세요.
:::

### export된 class 구현 모킹

1. 가짜 `class` 사용 예시:

```ts [example.js]
export class SomeClass {}
```

```ts
import { SomeClass } from "./example.js";

vi.mock(import("./example.js"), () => {
  const SomeClass = vi.fn(
    class FakeClass {
      someMethod = vi.fn();
    },
  );
  return { SomeClass };
});
```

2. `vi.spyOn` 사용 예시:

```ts
import * as mod from "./example.js";

vi.spyOn(mod, "SomeClass").mockImplementation(
  class FakeClass {
    someMethod = vi.fn();
  },
);
```

::: warning
`vi.spyOn` 예시는 Browser Mode에서 동작하지 않습니다. 우회 방법은 [Limitations](https://vitest.dev/guide/browser/#spying-on-module-exports)를 참고하세요.
:::

### 함수가 반환한 객체에 spy 적용

1. 캐시 사용 예시:

```ts [example.js]
export function useObject() {
  return { method: () => true };
}
```

```ts [useObject.js]
import { useObject } from "./example.js";

const obj = useObject();
obj.method();
```

```ts [useObject.test.js]
import { useObject } from "./example.js";

vi.mock(import("./example.js"), () => {
  let _cache;
  const useObject = () => {
    if (!_cache) {
      _cache = {
        method: vi.fn(),
      };
    }
    // now every time that useObject() is called it will
    // return the same object reference
    return _cache;
  };
  return { useObject };
});

const obj = useObject();
// obj.method was called inside some-path
expect(obj.method).toHaveBeenCalled();
```

### 모듈의 일부만 모킹

```ts
import { mocked, original } from "./some-path.js";

vi.mock(import("./some-path.js"), async (importOriginal) => {
  const mod = await importOriginal();
  return {
    ...mod,
    mocked: vi.fn(),
  };
});
original(); // has original behaviour
mocked(); // is a spy function
```

::: warning
이것은 [_외부_ 접근만 모킹한다는 점](#mocking-pitfalls)을 잊지 마세요. 이 예시에서 `original`이 내부적으로 `mocked`를 호출하면, mock factory가 아니라 모듈에 정의된 함수를 항상 호출합니다.
:::

### 현재 날짜 모킹

`Date`의 시간을 모킹하려면 `vi.setSystemTime` 헬퍼 함수를 사용할 수 있습니다. 이 값은 서로 다른 테스트 간에 자동으로 reset되지 **않습니다**.

`vi.useFakeTimers`를 사용하면 `Date`의 시간도 함께 변경된다는 점에 유의하세요.

```ts
const mockDate = new Date(2022, 0, 1);
vi.setSystemTime(mockDate);
const now = new Date();
expect(now.valueOf()).toBe(mockDate.valueOf());
// reset mocked time
vi.useRealTimers();
```

### 전역 변수 모킹

`globalThis`에 값을 할당하거나 [`vi.stubGlobal`](https://vitest.dev/api/vi#vi-stubglobal) 헬퍼를 사용해 전역 변수를 설정할 수 있습니다. `vi.stubGlobal`을 사용할 때는 [`unstubGlobals`](https://vitest.dev/config/#unstubglobals) config 옵션을 활성화하거나 [`vi.unstubAllGlobals`](https://vitest.dev/api/vi#vi-unstuballglobals)를 호출하지 않는 한, 서로 다른 테스트 간에 자동으로 reset되지 **않습니다**.

```ts
vi.stubGlobal("__VERSION__", "1.0.0");
expect(__VERSION__).toBe("1.0.0");
```

### `import.meta.env` 모킹

1. 환경 변수를 변경하려면 새 값을 직접 할당하면 됩니다.

::: warning
환경 변수 값은 서로 다른 테스트 간에 자동으로 reset되지 **_않습니다_**.
:::

```ts
import { beforeEach, expect, it } from "vitest";

// you can reset it in beforeEach hook manually
const originalViteEnv = import.meta.env.VITE_ENV;

beforeEach(() => {
  import.meta.env.VITE_ENV = originalViteEnv;
});

it("changes value", () => {
  import.meta.env.VITE_ENV = "staging";
  expect(import.meta.env.VITE_ENV).toBe("staging");
});
```

2. 값들을 자동으로 reset하고 싶다면 [`unstubEnvs`](https://vitest.dev/config/#unstubenvs) config 옵션을 활성화한 상태에서 `vi.stubEnv` 헬퍼를 사용할 수 있습니다(또는 `beforeEach` hook에서 [`vi.unstubAllEnvs`](https://vitest.dev/api/vi#vi-unstuballenvs)를 수동 호출):

```ts
import { expect, it, vi } from "vitest";

// before running tests "VITE_ENV" is "test"
import.meta.env.VITE_ENV === "test";

it("changes value", () => {
  vi.stubEnv("VITE_ENV", "staging");
  expect(import.meta.env.VITE_ENV).toBe("staging");
});

it("the value is restored before running an other test", () => {
  expect(import.meta.env.VITE_ENV).toBe("test");
});
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    unstubEnvs: true,
  },
});
```
