---
title: "모듈 모킹"
description: "Vitest는  헬퍼를 통해 작업을 도와주는 유틸리티 함수를 제공합니다. 전역으로 접근할 수 있으며(globals configuration이 활성화된 경우), 또는 에서 직접 import할 수 있습니다:"
---

출처 URL: https://vitest.dev/api/vi

# Vi

Vitest는 `vi` 헬퍼를 통해 작업을 도와주는 유틸리티 함수를 제공합니다. 전역으로 접근할 수 있으며([globals configuration](https://vitest.dev/config/#globals)이 활성화된 경우), 또는 `vitest`에서 직접 import할 수 있습니다:

```js
import { vi } from "vitest";
```

## 모듈 모킹

이 섹션에서는 [모듈을 모킹](https://vitest.dev/guide/mocking/modules)할 때 사용할 수 있는 API를 설명합니다. Vitest는 `require()`로 import된 모듈의 모킹을 지원하지 않는다는 점에 유의하세요.

### vi.mock

```ts
interface MockOptions {
  spy?: boolean;
}

interface MockFactory<T> {
  (importOriginal: () => T): unknown;
}

function mock(path: string, factory?: MockOptions | MockFactory<unknown>): void;
function mock<T>(
  module: Promise<T>,
  factory?: MockOptions | MockFactory<T>,
): void;
```

제공된 `path`에서 import된 모든 모듈을 다른 모듈로 대체합니다. 경로 안에서 설정된 Vite alias를 사용할 수 있습니다. `vi.mock` 호출은 호이스팅되므로 어디에서 호출하든 상관없습니다. 항상 모든 import보다 먼저 실행됩니다. 스코프 밖의 변수를 참조해야 한다면 [`vi.hoisted`](#vi-hoisted) 안에 정의하고 `vi.mock` 내부에서 참조할 수 있습니다.

::: warning
`vi.mock`은 `import` 키워드로 import된 모듈에서만 동작합니다. `require`에서는 동작하지 않습니다.

`vi.mock`을 호이스팅하기 위해 Vitest는 파일을 정적으로 분석합니다. 이 때문에 `vitest` 패키지에서 직접 import하지 않은 `vi`(예: 유틸리티 파일에서 가져온 경우)는 사용할 수 없습니다. `vitest`에서 import한 `vi`와 함께 `vi.mock`을 사용하거나 [`globals`](https://vitest.dev/config/#globals) 설정 옵션을 활성화하세요.

Vitest는 [setup file](https://vitest.dev/config/setupfiles) 내부에서 import된 모듈은 모킹하지 않습니다. 테스트 파일이 실행될 때는 이미 캐시되어 있기 때문입니다. 테스트 파일 실행 전에 모든 모듈 캐시를 지우려면 [`vi.hoisted`](#vi-hoisted) 내부에서 [`vi.resetModules()`](#vi-resetmodules)를 호출할 수 있습니다.
:::

`factory` 함수가 정의되어 있으면 모든 import는 해당 함수의 결과를 반환합니다. Vitest는 factory를 한 번만 호출하고, 이후 import에서는 [`vi.unmock`](#vi-unmock) 또는 [`vi.doUnmock`](#vi-dounmock)가 호출될 때까지 결과를 캐시합니다.

`jest`와 달리 factory는 비동기일 수 있습니다. 첫 번째 인자로 전달된 factory 내부에서 [`vi.importActual`](#vi-importactual) 또는 헬퍼를 사용해 원본 모듈을 가져올 수 있습니다.

factory 함수 대신 `spy` 속성을 가진 객체를 제공할 수도 있습니다. `spy`가 `true`이면 Vitest는 평소처럼 모듈을 automock하지만 export 구현은 덮어쓰지 않습니다. 다른 메서드가 export된 메서드를 올바르게 호출했는지만 검증하고 싶을 때 유용합니다.

```ts
import { calculator } from "./src/calculator.ts";

vi.mock("./src/calculator.ts", { spy: true });

// calls the original implementation,
// but allows asserting the behaviour later
const result = calculator(1, 2);

expect(result).toBe(3);
expect(calculator).toHaveBeenCalledWith(1, 2);
expect(calculator).toHaveReturnedWith(3);
```

Vitest는 더 나은 IDE 지원을 위해 `vi.mock` 및 `vi.doMock` 메서드에서 문자열 대신 module promise도 지원합니다. 파일이 이동되면 경로가 업데이트되고, `importOriginal`은 타입도 자동으로 상속합니다. 이 시그니처를 사용하면 factory 반환 타입이 원본 모듈과 호환되는지도 강제됩니다(export는 optional 유지).

```ts twoslash
// @filename: ./path/to/module.js
export declare function total(...numbers: number[]): number;
// @filename: test.js
import { vi } from "vitest";
// ---cut---
vi.mock(import("./path/to/module.js"), async (importOriginal) => {
  const mod = await importOriginal(); // type is inferred
  //    ^?
  return {
    ...mod,
    // replace some exports
    total: vi.fn(),
  };
});
```

내부적으로 Vitest는 여전히 module object가 아닌 문자열 기반으로 동작합니다.

하지만 `tsconfig.json`에서 `paths` alias를 설정한 TypeScript를 사용하는 경우, 컴파일러가 import 타입을 올바르게 해석하지 못할 수 있습니다.
이 기능이 동작하게 하려면 alias import를 해당 상대 경로로 모두 바꾸세요.
예: `import('@/module')` 대신 `import('./path/to/module.js')` 사용.

::: warning
`vi.mock`은 호이스팅됩니다(즉, **파일 최상단**으로 *이동*됩니다). 따라서 어디에 작성하든(`beforeEach`든 `test`든) 실제로는 그보다 먼저 호출됩니다.

이는 factory 외부에서 정의된 변수를 factory 내부에서 사용할 수 없다는 뜻이기도 합니다.

factory 내부에서 변수를 사용해야 한다면 [`vi.doMock`](#vi-domock)을 사용해 보세요. 동작은 같지만 호이스팅되지 않습니다. 단, 이후 import에만 모킹이 적용됩니다.

`vi.mock`보다 먼저 선언했다면 `vi.hoisted` 메서드로 정의한 변수도 참조할 수 있습니다:

```ts
import { namedExport } from "./path/to/module.js";

const mocks = vi.hoisted(() => {
  return {
    namedExport: vi.fn(),
  };
});

vi.mock("./path/to/module.js", () => {
  return {
    namedExport: mocks.namedExport,
  };
});

vi.mocked(namedExport).mockReturnValue(100);

expect(namedExport()).toBe(100);
expect(namedExport).toBe(mocks.namedExport);
```

:::

::: warning
default export가 있는 모듈을 모킹하는 경우, factory 함수가 반환하는 객체 안에 `default` 키를 제공해야 합니다. 이는 ES module 고유의 주의사항이므로 CommonJS를 사용하는 `jest` 문서와는 다를 수 있습니다. 예:

```ts
vi.mock("./path/to/module.js", () => {
  return {
    default: { myDefaultKey: vi.fn() },
    namedExport: vi.fn(),
    // etc...
  };
});
```

:::

모킹하는 파일 옆에 `__mocks__` 폴더가 있고 factory를 제공하지 않으면, Vitest는 `__mocks__` 하위 폴더에서 같은 이름의 파일을 찾아 실제 모듈로 사용하려고 시도합니다. 의존성을 모킹하는 경우, Vitest는 프로젝트 [root](https://vitest.dev/config/#root)(기본값: `process.cwd()`)에서 `__mocks__` 폴더를 찾으려 합니다. 의존성 위치는 [`deps.moduleDirectories`](https://vitest.dev/config/#deps-moduledirectories) 설정 옵션으로 지정할 수 있습니다.

예를 들어 다음과 같은 파일 구조가 있다고 가정해 보겠습니다:

```
- __mocks__
  - axios.js
- src
  __mocks__
    - increment.js
  - increment.js
- tests
  - increment.test.js
```

테스트 파일에서 factory나 옵션 없이 `vi.mock`을 호출하면, `__mocks__` 폴더의 파일을 모듈로 사용합니다:

```ts [increment.test.js]
import { vi } from "vitest";

// axios is a default export from `__mocks__/axios.js`
import axios from "axios";

// increment is a named export from `src/__mocks__/increment.js`
import { increment } from "../increment.js";

vi.mock("axios");
vi.mock("../increment.js");

axios.get(`/apples/${increment(1)}`);
```

::: warning
`vi.mock`을 호출하지 않으면 모듈은 자동으로 모킹되지 않는다는 점에 유의하세요. Jest의 automocking 동작을 재현하려면 [`setupFiles`](https://vitest.dev/config/setupfiles) 안에서 필요한 각 모듈마다 `vi.mock`을 호출하세요.
:::

`__mocks__` 폴더도 없고 factory도 제공하지 않으면, Vitest는 원본 모듈을 import한 뒤 모든 export를 automock합니다. 적용 규칙은 [algorithm](https://vitest.dev/guide/mocking/modules#automocking-algorithm)을 참고하세요.

### vi.doMock

```ts
function doMock(
  path: string,
  factory?: MockOptions | MockFactory<unknown>,
): void;
function doMock<T>(
  module: Promise<T>,
  factory?: MockOptions | MockFactory<T>,
): void;
```

[`vi.mock`](#vi-mock)과 동일하지만 파일 최상단으로 호이스팅되지 않으므로 파일 전역 스코프의 변수를 참조할 수 있습니다. 해당 모듈에 대한 다음 [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)는 모킹됩니다.

::: warning
이 호출 이전에 import된 모듈은 모킹되지 않습니다. ESM의 모든 정적 import는 항상 [hoisted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#hoisting)된다는 점을 잊지 마세요. 따라서 정적 import 앞에 이것을 두어도 import보다 먼저 호출되도록 강제할 수는 없습니다:

```ts
vi.doMock("./increment.js"); // this will be called _after_ the import statement

import { increment } from "./increment.js";
```

:::

```ts [increment.js]
export function increment(number) {
  return number + 1;
}
```

```ts [increment.test.js]
import { beforeEach, test } from "vitest";
import { increment } from "./increment.js";

// the module is not mocked, because vi.doMock is not called yet
increment(1) === 2;

let mockedIncrement = 100;

beforeEach(() => {
  // you can access variables inside a factory
  vi.doMock("./increment.js", () => ({ increment: () => ++mockedIncrement }));
});

test("importing the next module imports mocked one", async () => {
  // original import WAS NOT MOCKED, because vi.doMock is evaluated AFTER imports
  expect(increment(1)).toBe(2);
  const { increment: mockedIncrement } = await import("./increment.js");
  // new dynamic import returns mocked module
  expect(mockedIncrement(1)).toBe(101);
  expect(mockedIncrement(1)).toBe(102);
  expect(mockedIncrement(1)).toBe(103);
});
```

### vi.mocked

```ts
function mocked<T>(object: T, deep?: boolean): MaybeMockedDeep<T>;
function mocked<T>(
  object: T,
  options?: { partial?: boolean; deep?: boolean },
): MaybePartiallyMockedDeep<T>;
```

TypeScript용 타입 헬퍼입니다. 전달된 객체를 그대로 반환합니다.

`partial`이 `true`이면 반환값으로 `Partial<T>`를 기대합니다. 기본적으로는 첫 번째 레벨 값만 모킹된 것으로 TypeScript가 인식합니다. 실제로 전체 객체가 모킹된 경우 두 번째 인자로 `{ deep: true }`를 전달해 전체 객체가 모킹되었다고 TypeScript에 알릴 수 있습니다.

```ts [example.ts]
export function add(x: number, y: number): number {
  return x + y;
}

export function fetchSomething(): Promise<Response> {
  return fetch("https://vitest.dev/");
}
```

```ts [example.test.ts]
import * as example from "./example";

vi.mock("./example");

test("1 + 1 equals 10", async () => {
  vi.mocked(example.add).mockReturnValue(10);
  expect(example.add(1, 1)).toBe(10);
});

test("mock return value with only partially correct typing", async () => {
  vi.mocked(example.fetchSomething).mockResolvedValue(new Response("hello"));
  vi.mocked(example.fetchSomething, { partial: true }).mockResolvedValue({
    ok: false,
  });
  // vi.mocked(example.someFn).mockResolvedValue({ ok: false }) // this is a type error
});
```

### vi.importActual

```ts
function importActual<T>(path: string): Promise<T>;
```

모킹 여부에 대한 모든 체크를 우회하고 모듈을 import합니다. 모듈을 부분적으로 모킹하고 싶을 때 유용할 수 있습니다.

```ts
vi.mock("./example.js", async () => {
  const originalModule = await vi.importActual("./example.js");

  return { ...originalModule, get: vi.fn() };
});
```

### vi.importMock

```ts
function importMock<T>(path: string): Promise<MaybeMockedDeep<T>>;
```

모듈의 모든 속성(중첩 속성 포함)을 모킹한 상태로 import합니다. [`vi.mock`](#vi-mock)과 동일한 규칙을 따릅니다. 적용 규칙은 [algorithm](https://vitest.dev/guide/mocking/modules#automocking-algorithm)을 참고하세요.

### vi.unmock

```ts
function unmock(path: string | Promise<Module>): void;
```

모킹 레지스트리에서 모듈을 제거합니다. 이전에 모킹했더라도 이후의 모든 import 호출은 원본 모듈을 반환합니다. 이 호출은 파일 최상단으로 호이스팅되므로 예를 들어 `setupFiles`에서 정의된 모듈만 unmock합니다.

### vi.doUnmock

```ts
function doUnmock(path: string | Promise<Module>): void;
```

[`vi.unmock`](#vi-unmock)과 동일하지만 파일 최상단으로 호이스팅되지 않습니다. 해당 모듈의 다음 import는 mock 대신 원본 모듈을 import합니다. 이미 import된 모듈은 unmock되지 않습니다.

```ts [increment.js]
export function increment(number) {
  return number + 1;
}
```

```ts [increment.test.js]
import { increment } from "./increment.js";

// increment is already mocked, because vi.mock is hoisted
increment(1) === 100;

// this is hoisted, and factory is called before the import on line 1
vi.mock("./increment.js", () => ({ increment: () => 100 }));

// all calls are mocked, and `increment` always returns 100
increment(1) === 100;
increment(30) === 100;

// this is not hoisted, so other import will return unmocked module
vi.doUnmock("./increment.js");

// this STILL returns 100, because `vi.doUnmock` doesn't reevaluate a module
increment(1) === 100;
increment(30) === 100;

// the next import is unmocked, now `increment` is the original function that returns count + 1
const { increment: unmockedIncrement } = await import("./increment.js");

unmockedIncrement(1) === 2;
unmockedIncrement(30) === 31;
```

### vi.resetModules

```ts
function resetModules(): Vitest;
```

모든 모듈의 캐시를 지워 모듈 레지스트리를 초기화합니다. 이렇게 하면 다시 import할 때 모듈이 재평가됩니다. 최상위 import는 재평가할 수 없습니다. 테스트 간 로컬 상태 충돌이 있는 모듈을 격리할 때 유용할 수 있습니다.

```ts
import { vi } from "vitest";

import { data } from "./data.js"; // Will not get reevaluated beforeEach test

beforeEach(() => {
  vi.resetModules();
});

test("change state", async () => {
  const mod = await import("./some/path.js"); // Will get reevaluated
  mod.changeLocalState("new value");
  expect(mod.getLocalState()).toBe("new value");
});

test("module has old state", async () => {
  const mod = await import("./some/path.js"); // Will get reevaluated
  expect(mod.getLocalState()).toBe("old value");
});
```

::: warning
mock 레지스트리는 초기화하지 않습니다. mock 레지스트리를 비우려면 [`vi.unmock`](#vi-unmock) 또는 [`vi.doUnmock`](#vi-dounmock)을 사용하세요.
:::

### vi.dynamicImportSettled

```ts
function dynamicImportSettled(): Promise<void>;
```

모든 import가 로드될 때까지 기다립니다. 동기 호출이 모듈 import를 시작하지만 다른 방식으로 대기할 수 없을 때 유용합니다.

```ts
import { expect, test } from "vitest";

// cannot track import because Promise is not returned
function renderComponent() {
  import("./component.js").then(({ render }) => {
    render();
  });
}

test("operations are resolved", async () => {
  renderComponent();
  await vi.dynamicImportSettled();
  expect(document.querySelector(".component")).not.toBeNull();
});
```

::: tip
dynamic import 도중 또 다른 dynamic import가 시작되면, 이 메서드는 그것들이 모두 resolve될 때까지 기다립니다.

또한 import가 resolve된 뒤 다음 `setTimeout` tick까지 기다리므로, resolve 시점에는 모든 동기 작업이 완료되어 있어야 합니다.
:::

## 함수와 객체 모킹

이 섹션에서는 [method mocks](https://vitest.dev/api/mock)를 다루는 방법과 환경 변수 및 전역 변수를 교체하는 방법을 설명합니다.

### vi.fn

```ts
function fn(fn?: Procedure | Constructable): Mock;
```

함수에 대한 spy를 생성하며, 함수 없이도 초기화할 수 있습니다. 함수가 호출될 때마다 호출 인자, 반환값, 인스턴스를 저장합니다. 추가로 [methods](https://vitest.dev/api/mock)로 동작을 조작할 수 있습니다.
함수를 전달하지 않으면 mock은 호출 시 `undefined`를 반환합니다.

```ts
const getApples = vi.fn(() => 0);

getApples();

expect(getApples).toHaveBeenCalled();
expect(getApples).toHaveReturnedWith(0);

getApples.mockReturnValueOnce(5);

const res = getApples();
expect(res).toBe(5);
expect(getApples).toHaveNthReturnedWith(2, 5);
```

`vi.fn`에 class를 전달할 수도 있습니다:

```ts
const Cart = vi.fn(
  class {
    get = () => 0;
  },
);

const cart = new Cart();
expect(Cart).toHaveBeenCalled();
```

### vi.mockObject 3.2.0

```ts
function mockObject<T>(value: T, options?: MockOptions): MaybeMockedDeep<T>;
```

`vi.mock()`이 모듈 export를 모킹하는 방식과 동일하게, 주어진 객체의 속성과 메서드를 깊게 모킹합니다. 자세한 내용은 [automocking](https://vitest.dev/guide/mocking.html#automocking-algorithm)을 참고하세요.

```ts
const original = {
  simple: () => "value",
  nested: {
    method: () => "real",
  },
  prop: "foo",
};

const mocked = vi.mockObject(original);
expect(mocked.simple()).toBe(undefined);
expect(mocked.nested.method()).toBe(undefined);
expect(mocked.prop).toBe("foo");

mocked.simple.mockReturnValue("mocked");
mocked.nested.method.mockReturnValue("mocked nested");

expect(mocked.simple()).toBe("mocked");
expect(mocked.nested.method()).toBe("mocked nested");
```

`vi.mock()`과 마찬가지로 두 번째 인자로 `{ spy: true }`를 전달해 함수 구현을 유지할 수 있습니다:

```ts
const spied = vi.mockObject(original, { spy: true });
expect(spied.simple()).toBe("value");
expect(spied.simple).toHaveBeenCalled();
expect(spied.simple.mock.results[0]).toEqual({
  type: "return",
  value: "value",
});
```

### vi.isMockFunction

```ts
function isMockFunction(fn: unknown): asserts fn is Mock;
```

주어진 파라미터가 mock 함수인지 확인합니다. TypeScript를 사용하는 경우 타입도 좁혀집니다.

### vi.clearAllMocks

```ts
function clearAllMocks(): Vitest;
```

모든 spy에 대해 [`.mockClear()`](https://vitest.dev/api/mock#mockclear)를 호출합니다.
mock 구현에는 영향을 주지 않고 mock 히스토리만 지웁니다.

### vi.resetAllMocks

```ts
function resetAllMocks(): Vitest;
```

모든 spy에 대해 [`.mockReset()`](https://vitest.dev/api/mock#mockreset)를 호출합니다.
mock 히스토리를 지우고 각 mock의 구현을 초기화합니다.

### vi.restoreAllMocks

```ts
function restoreAllMocks(): Vitest;
```

[`vi.spyOn`](#vi-spyon)으로 생성된 spy의 모든 원본 구현을 복원합니다.

mock이 복원된 뒤에는 다시 spy를 걸 수 있습니다.

::: warning
이 메서드는 [automocking](https://vitest.dev/guide/mocking/modules#mocking-a-module) 중 생성된 mock에도 영향을 주지 않습니다.

또한 [`mock.mockRestore`](https://vitest.dev/api/mock#mockrestore)와 달리, `vi.restoreAllMocks`는 mock 히스토리를 지우거나 mock 구현을 초기화하지 않습니다.
:::

### vi.spyOn

```ts
function spyOn<T, K extends keyof T>(
  object: T,
  key: K,
  accessor?: "get" | "set",
): Mock<T[K]>;
```

[`vi.fn()`](#vi-fn)과 유사하게 객체의 메서드 또는 getter/setter에 spy를 생성합니다. [mock function](https://vitest.dev/api/mock)을 반환합니다.

```ts
let apples = 0;
const cart = {
  getApples: () => 42,
};

const spy = vi.spyOn(cart, "getApples").mockImplementation(() => apples);
apples = 1;

expect(cart.getApples()).toBe(1);

expect(spy).toHaveBeenCalled();
expect(spy).toHaveReturnedWith(1);
```

spy 대상 메서드가 class 정의라면, mock 구현은 `function` 또는 `class` 키워드를 사용해야 합니다:

```ts {12-14,16-20}
const cart = {
  Apples: class Apples {
    getApples() {
      return 42;
    }
  },
};

const spy = vi
  .spyOn(cart, "Apples")
  .mockImplementation(() => ({ getApples: () => 0 })) // [!code --]
  // with a function keyword
  .mockImplementation(function () {
    this.getApples = () => 0;
  })
  // with a custom class
  .mockImplementation(
    class MockApples {
      getApples() {
        return 0;
      }
    },
  );
```

화살표 함수를 제공하면 mock 호출 시 [`<anonymous> is not a constructor` error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_constructor)가 발생합니다.

::: tip
[Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management)를 지원하는 환경에서는 `const` 대신 `using`을 사용해 포함 블록을 벗어날 때 모킹된 함수의 `mockRestore`를 자동 호출할 수 있습니다. 특히 spy된 메서드에서 유용합니다:

```ts
it("calls console.log", () => {
  using spy = vi.spyOn(console, "log").mockImplementation(() => {});
  debug("message");
  expect(spy).toHaveBeenCalled();
});
// console.log is restored here
```

:::

::: tip
각 테스트 후 모든 메서드를 원본 구현으로 복원하려면 [`afterEach`](https://vitest.dev/api/#aftereach) 내부에서 [`vi.restoreAllMocks`](#vi-restoreallmocks)를 호출하거나 [`test.restoreMocks`](https://vitest.dev/config/#restoreMocks)를 활성화할 수 있습니다. 이렇게 하면 원본 [object descriptor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)가 복원되므로, 다시 spy를 걸지 않는 한 더 이상 메서드 구현을 변경할 수 없습니다:

```ts
const cart = {
  getApples: () => 42,
};

const spy = vi.spyOn(cart, "getApples").mockReturnValue(10);

console.log(cart.getApples()); // 10
vi.restoreAllMocks();
console.log(cart.getApples()); // 42
spy.mockReturnValue(10);
console.log(cart.getApples()); // still 42!
```

:::

::: tip
[Browser Mode](https://vitest.dev/guide/browser/)에서는 export된 메서드를 spy할 수 없습니다. 대신 `vi.mock("./file-path.js", { spy: true })`를 호출해 모든 export된 메서드를 spy할 수 있습니다. 이렇게 하면 모든 export가 mock 처리되지만 구현은 그대로 유지되므로, 메서드가 올바르게 호출되었는지 단언할 수 있습니다.

```ts
import { calculator } from "./src/calculator.ts";

vi.mock("./src/calculator.ts", { spy: true });

calculator(1, 2);

expect(calculator).toHaveBeenCalledWith(1, 2);
expect(calculator).toHaveReturned(3);
```

그리고 `jsdom` 또는 다른 Node.js 환경에서는 exports를 spy할 수 있지만, 이는 향후 변경될 수 있습니다.
:::

### vi.stubEnv {#vi-stubenv}

```ts
function stubEnv<T extends string>(
  name: T,
  value: T extends "PROD" | "DEV" | "SSR" ? boolean : string | undefined,
): Vitest;
```

`process.env`와 `import.meta.env`의 환경 변수 값을 변경합니다. `vi.unstubAllEnvs`를 호출해 값을 복원할 수 있습니다.

```ts
import { vi } from "vitest";

// `process.env.NODE_ENV` and `import.meta.env.NODE_ENV`
// are "development" before calling "vi.stubEnv"

vi.stubEnv("NODE_ENV", "production");

process.env.NODE_ENV === "production";
import.meta.env.NODE_ENV === "production";

vi.stubEnv("NODE_ENV", undefined);

process.env.NODE_ENV === undefined;
import.meta.env.NODE_ENV === undefined;

// doesn't change other envs
import.meta.env.MODE === "development";
```

:::tip
단순히 할당해서 값을 변경할 수도 있지만, 이 경우 이전 값을 복원할 때 `vi.unstubAllEnvs`를 사용할 수 없습니다:

```ts
import.meta.env.MODE = "test";
```

:::

### vi.unstubAllEnvs {#vi-unstuballenvs}

```ts
function unstubAllEnvs(): Vitest;
```

`vi.stubEnv`로 변경한 모든 `import.meta.env` 및 `process.env` 값을 복원합니다. 처음 호출될 때 Vitest는 원래 값을 기억해 저장하고, `unstubAllEnvs`가 다시 호출될 때까지 이를 유지합니다.

```ts
import { vi } from "vitest";

// `process.env.NODE_ENV` and `import.meta.env.NODE_ENV`
// are "development" before calling stubEnv

vi.stubEnv("NODE_ENV", "production");

process.env.NODE_ENV === "production";
import.meta.env.NODE_ENV === "production";

vi.stubEnv("NODE_ENV", "staging");

process.env.NODE_ENV === "staging";
import.meta.env.NODE_ENV === "staging";

vi.unstubAllEnvs();

// restores to the value that were stored before the first "stubEnv" call
process.env.NODE_ENV === "development";
import.meta.env.NODE_ENV === "development";
```

### vi.stubGlobal

```ts
function stubGlobal(name: string | number | symbol, value: unknown): Vitest;
```

전역 변수 값을 변경합니다. `vi.unstubAllGlobals`를 호출해 원래 값을 복원할 수 있습니다.

```ts
import { vi } from "vitest";

// `innerWidth` is "0" before calling stubGlobal

vi.stubGlobal("innerWidth", 100);

innerWidth === 100;
globalThis.innerWidth === 100;
// if you are using jsdom or happy-dom
window.innerWidth === 100;
```

:::tip
`globalThis` 또는 `window`(`jsdom` 또는 `happy-dom` 환경 사용 시)에 직접 할당해 값을 변경할 수도 있지만, 이 경우 원래 값을 복원할 때 `vi.unstubAllGlobals`를 사용할 수 없습니다:

```ts
globalThis.innerWidth = 100;
// if you are using jsdom or happy-dom
window.innerWidth = 100;
```

:::

### vi.unstubAllGlobals {#vi-unstuballglobals}

```ts
function unstubAllGlobals(): Vitest;
```

`vi.stubGlobal`로 변경된 `globalThis`/`global`(그리고 `jsdom` 또는 `happy-dom` 환경 사용 시 `window`/`top`/`self`/`parent`)의 모든 전역 값을 복원합니다. 처음 호출될 때 Vitest는 원래 값을 기억해 저장하고, `unstubAllGlobals`가 다시 호출될 때까지 이를 유지합니다.

```ts
import { vi } from "vitest";

const Mock = vi.fn();

// IntersectionObserver is "undefined" before calling "stubGlobal"

vi.stubGlobal("IntersectionObserver", Mock);

IntersectionObserver === Mock;
global.IntersectionObserver === Mock;
globalThis.IntersectionObserver === Mock;
// if you are using jsdom or happy-dom
window.IntersectionObserver === Mock;

vi.unstubAllGlobals();

globalThis.IntersectionObserver === undefined;
"IntersectionObserver" in globalThis === false;
// throws ReferenceError, because it's not defined
IntersectionObserver === undefined;
```

## Fake Timers

이 섹션에서는 [fake timers](https://vitest.dev/guide/mocking/timers)를 다루는 방법을 설명합니다.

### vi.advanceTimersByTime

```ts
function advanceTimersByTime(ms: number): Vitest;
```

이 메서드는 지정한 밀리초가 경과하거나 큐가 빌 때까지, 먼저 도달하는 조건까지 시작된 모든 타이머를 호출합니다.

```ts
let i = 0;
setInterval(() => console.log(++i), 50);

vi.advanceTimersByTime(150);

// log: 1
// log: 2
// log: 3
```

### vi.advanceTimersByTimeAsync

```ts
function advanceTimersByTimeAsync(ms: number): Promise<Vitest>;
```

이 메서드는 지정한 밀리초가 경과하거나 큐가 빌 때까지, 먼저 도달하는 조건까지 시작된 모든 타이머를 호출합니다. 비동기로 설정된 타이머도 포함됩니다.

```ts
let i = 0;
setInterval(() => Promise.resolve().then(() => console.log(++i)), 50);

await vi.advanceTimersByTimeAsync(150);

// log: 1
// log: 2
// log: 3
```

### vi.advanceTimersToNextTimer

```ts
function advanceTimersToNextTimer(): Vitest;
```

다음으로 사용 가능한 타이머를 호출합니다. 각 타이머 호출 사이에서 단언할 때 유용합니다. 이 메서드를 연쇄 호출하여 타이머를 직접 제어할 수 있습니다.

```ts
let i = 0;
setInterval(() => console.log(++i), 50);

vi.advanceTimersToNextTimer() // log: 1
  .advanceTimersToNextTimer() // log: 2
  .advanceTimersToNextTimer(); // log: 3
```

### vi.advanceTimersToNextTimerAsync

```ts
function advanceTimersToNextTimerAsync(): Promise<Vitest>;
```

다음으로 사용 가능한 타이머를 호출하고, 비동기로 설정된 경우 해결될 때까지 기다립니다. 각 타이머 호출 사이에서 단언할 때 유용합니다.

```ts
let i = 0;
setInterval(() => Promise.resolve().then(() => console.log(++i)), 50);

await vi.advanceTimersToNextTimerAsync(); // log: 1
expect(console.log).toHaveBeenCalledWith(1);

await vi.advanceTimersToNextTimerAsync(); // log: 2
await vi.advanceTimersToNextTimerAsync(); // log: 3
```

### vi.advanceTimersToNextFrame {#vi-advancetimerstonextframe}

```ts
function advanceTimersToNextFrame(): Vitest;
```

[`vi.advanceTimersByTime`](https://vitest.dev/api/vi#vi-advancetimersbytime)와 유사하지만, 현재 `requestAnimationFrame`으로 예약된 콜백을 실행하는 데 필요한 밀리초만큼 타이머를 진행합니다.

```ts
let frameRendered = false;

requestAnimationFrame(() => {
  frameRendered = true;
});

vi.advanceTimersToNextFrame();

expect(frameRendered).toBe(true);
```

### vi.getTimerCount

```ts
function getTimerCount(): number;
```

대기 중인 타이머 개수를 가져옵니다.

### vi.clearAllTimers

```ts
function clearAllTimers(): void;
```

실행 예정인 모든 타이머를 제거합니다. 이 타이머들은 이후에 실행되지 않습니다.

### vi.getMockedSystemTime

```ts
function getMockedSystemTime(): Date | null;
```

mock된 현재 날짜를 반환합니다. 날짜가 mock되지 않았다면 `null`을 반환합니다.

### vi.getRealSystemTime

```ts
function getRealSystemTime(): number;
```

`vi.useFakeTimers`를 사용할 때 `Date.now` 호출은 mock됩니다. 실제 시간을 밀리초로 가져와야 한다면 이 함수를 호출할 수 있습니다.

### vi.runAllTicks

```ts
function runAllTicks(): Vitest;
```

`process.nextTick`으로 큐에 들어간 모든 마이크로태스크를 호출합니다. 마이크로태스크가 스스로 예약한 다른 마이크로태스크도 모두 실행합니다.

### vi.runAllTimers

```ts
function runAllTimers(): Vitest;
```

이 메서드는 타이머 큐가 빌 때까지 시작된 모든 타이머를 호출합니다. 즉, `runAllTimers` 실행 중에 생성된 모든 타이머도 실행됩니다. 무한 interval이 있으면 10,000회 시도 후 예외를 던집니다([`fakeTimers.loopLimit`](https://vitest.dev/config/#faketimers-looplimit)로 설정 가능).

```ts
let i = 0;
setTimeout(() => console.log(++i));
const interval = setInterval(() => {
  console.log(++i);
  if (i === 3) {
    clearInterval(interval);
  }
}, 50);

vi.runAllTimers();

// log: 1
// log: 2
// log: 3
```

### vi.runAllTimersAsync

```ts
function runAllTimersAsync(): Promise<Vitest>;
```

이 메서드는 타이머 큐가 빌 때까지 시작된 모든 타이머를 비동기로 호출합니다. 즉, `runAllTimersAsync` 실행 중에 생성된 타이머는 비동기 타이머를 포함해 모두 실행됩니다. 무한 interval이 있으면
10,000회 시도 후 예외를 던집니다([`fakeTimers.loopLimit`](https://vitest.dev/config/#faketimers-looplimit)로 설정 가능).

```ts
setTimeout(async () => {
  console.log(await Promise.resolve("result"));
}, 100);

await vi.runAllTimersAsync();

// log: result
```

### vi.runOnlyPendingTimers

```ts
function runOnlyPendingTimers(): Vitest;
```

이 메서드는 [`vi.useFakeTimers`](#vi-usefaketimers) 호출 이후 시작된 모든 타이머를 호출합니다. 실행 중에 새로 시작된 타이머는 실행하지 않습니다.

```ts
let i = 0;
setInterval(() => console.log(++i), 50);

vi.runOnlyPendingTimers();

// log: 1
```

### vi.runOnlyPendingTimersAsync

```ts
function runOnlyPendingTimersAsync(): Promise<Vitest>;
```

이 메서드는 [`vi.useFakeTimers`](#vi-usefaketimers) 호출 이후 시작된 모든 타이머를 비동기로 호출하며, 비동기 타이머도 포함합니다. 실행 중에 새로 시작된 타이머는 실행하지 않습니다.

```ts
setTimeout(() => {
  console.log(1);
}, 100);
setTimeout(() => {
  Promise.resolve().then(() => {
    console.log(2);
    setInterval(() => {
      console.log(3);
    }, 40);
  });
}, 10);

await vi.runOnlyPendingTimersAsync();

// log: 2
// log: 3
// log: 3
// log: 1
```

### vi.setSystemTime

```ts
function setSystemTime(date: string | number | Date): Vitest;
```

fake timers가 활성화된 경우, 이 메서드는 사용자가 시스템 시계를 변경한 상황을 시뮬레이션합니다(`hrtime`, `performance.now`, `new Date()` 같은 날짜 관련 API에 영향을 줌). 다만 어떤 타이머도 실행되지는 않습니다. fake timers가 활성화되지 않은 경우에는 `Date.*` 호출만 mock합니다.

현재 날짜에 의존하는 것을 테스트해야 할 때 유용합니다. 예를 들어 코드 내부의 [Luxon](https://github.com/moment/luxon/) 호출이 이에 해당합니다.

`Date`와 동일한 문자열 및 숫자 인수를 받습니다.

```ts
const date = new Date(1998, 11, 19);

vi.useFakeTimers();
vi.setSystemTime(date);

expect(Date.now()).toBe(date.valueOf());

vi.useRealTimers();
```

### vi.useFakeTimers

```ts
function useFakeTimers(config?: FakeTimerInstallOpts): Vitest;
```

타이머 mocking을 활성화하려면 이 메서드를 호출해야 합니다. 그러면 [`vi.useRealTimers()`](#vi-userealtimers)가 호출될 때까지 이후의 모든 타이머 호출(`setTimeout`, `setInterval`, `clearTimeout`, `clearInterval`, `setImmediate`, `clearImmediate`, `Date` 등)을 래핑합니다.

`--pool=forks`를 사용해 `node:child_process` 내부에서 Vitest를 실행할 때는 `nextTick` mocking이 지원되지 않습니다. NodeJS는 `node:child_process` 내부에서 `process.nextTick`을 내부적으로 사용하며, 이를 mock하면 멈춥니다. `--pool=threads`로 Vitest를 실행할 때는 `nextTick` mocking이 지원됩니다.

내부 구현은 [`@sinonjs/fake-timers`](https://github.com/sinonjs/fake-timers)를 기반으로 합니다.

::: tip
`vi.useFakeTimers()`는 `process.nextTick`과 `queueMicrotask`를 자동으로 mock하지 않습니다.
하지만 `toFake` 인수에 옵션을 지정해 활성화할 수 있습니다: `vi.useFakeTimers({ toFake: ['nextTick', 'queueMicrotask'] })`.
:::

### vi.isFakeTimers {#vi-isfaketimers}

```ts
function isFakeTimers(): boolean;
```

fake timers가 활성화되어 있으면 `true`를 반환합니다.

### vi.useRealTimers

```ts
function useRealTimers(): Vitest;
```

타이머 실행이 끝난 뒤 이 메서드를 호출해 mock된 타이머를 원래 구현으로 되돌릴 수 있습니다. 이전에 예약된 모든 타이머는 폐기됩니다.

## Miscellaneous

Vitest가 제공하는 유용한 헬퍼 함수 모음입니다.

### vi.waitFor {#vi-waitfor}

```ts
function waitFor<T>(
  callback: WaitForCallback<T>,
  options?: number | WaitForOptions,
): Promise<T>;
```

콜백이 성공적으로 실행될 때까지 기다립니다. 콜백이 에러를 던지거나 reject된 promise를 반환하면, 성공하거나 타임아웃될 때까지 계속 기다립니다.

options가 숫자로 설정되면 `{ timeout: options }`를 설정한 것과 동일한 효과입니다.

일부 비동기 작업이 완료될 때까지 기다려야 할 때 매우 유용합니다. 예를 들어 서버를 시작한 뒤 실제로 시작될 때까지 기다려야 하는 경우가 그렇습니다.

```ts
import { expect, test, vi } from "vitest";
import { createServer } from "./server.js";

test("Server started successfully", async () => {
  const server = createServer();

  await vi.waitFor(
    () => {
      if (!server.isReady) {
        throw new Error("Server not started");
      }

      console.log("Server started");
    },
    {
      timeout: 500, // default is 1000
      interval: 20, // default is 50
    },
  );
  expect(server.isReady).toBe(true);
});
```

비동기 콜백에도 동작합니다.

```ts
// @vitest-environment jsdom

import { expect, test, vi } from "vitest";
import { getDOMElementAsync, populateDOMAsync } from "./dom.js";

test("Element exists in a DOM", async () => {
  // start populating DOM
  populateDOMAsync();

  const element = await vi.waitFor(
    async () => {
      // try to get the element until it exists
      const element = (await getDOMElementAsync()) as HTMLElement | null;
      expect(element).toBeTruthy();
      expect(element.dataset.initialized).toBeTruthy();
      return element;
    },
    {
      timeout: 500, // default is 1000
      interval: 20, // default is 50
    },
  );
  expect(element).toBeInstanceOf(HTMLElement);
});
```

`vi.useFakeTimers`를 사용하면 `vi.waitFor`는 각 체크 콜백마다 자동으로 `vi.advanceTimersByTime(interval)`을 호출합니다.

### vi.waitUntil {#vi-waituntil}

```ts
function waitUntil<T>(
  callback: WaitUntilCallback<T>,
  options?: number | WaitUntilOptions,
): Promise<T>;
```

이는 `vi.waitFor`와 유사하지만, 콜백이 에러를 던지면 실행이 즉시 중단되고 에러 메시지를 받습니다. 콜백이 falsy 값을 반환하면 truthy 값을 반환할 때까지 다음 체크가 계속됩니다. 다음 단계로 넘어가기 전에 어떤 대상이 존재할 때까지 기다려야 할 때 유용합니다.

아래 예제를 보세요. `vi.waitUntil`을 사용해 요소가 페이지에 나타날 때까지 기다린 다음, 그 요소로 작업을 수행할 수 있습니다.

```ts
import { expect, test, vi } from "vitest";

test("Element render correctly", async () => {
  const element = await vi.waitUntil(() => document.querySelector(".element"), {
    timeout: 500, // default is 1000
    interval: 20, // default is 50
  });

  // do something with the element
  expect(element.querySelector(".element-child")).toBeTruthy();
});
```

### vi.hoisted {#vi-hoisted}

```ts
function hoisted<T>(factory: () => T): T;
```

ES modules의 모든 정적 `import` 구문은 파일 최상단으로 hoist되므로, import보다 앞에 정의한 코드는 실제로 import 평가 이후에 실행됩니다.

하지만 모듈을 import하기 전에 날짜를 mock하는 등 일부 부수 효과를 실행해야 하는 경우가 있습니다.

이 제한을 우회하려면 다음과 같이 정적 import를 동적 import로 다시 작성할 수 있습니다:

```diff
callFunctionWithSideEffect()
- import { value } from './some/module.js'
+ const { value } = await import('./some/module.js')
```

`vitest` 실행 시 `vi.hoisted` 메서드를 사용하면 이를 자동으로 처리할 수 있습니다. 내부적으로 Vitest는 정적 import를 live-binding을 유지한 동적 import로 변환합니다.

```diff
- callFunctionWithSideEffect()
import { value } from './some/module.js'
+ vi.hoisted(() => callFunctionWithSideEffect())
```

::: warning IMPORTS ARE NOT AVAILABLE
import 이전에 코드를 실행한다는 것은, import된 변수들이 아직 정의되지 않았기 때문에 접근할 수 없다는 뜻입니다:

```ts
import { value } from "./some/module.js";

vi.hoisted(() => {
  value;
}); // throws an error // [!code warning]
```

이 코드는 에러를 발생시킵니다:

```
Cannot access '__vi_import_0__' before initialization
```

`vi.hoisted` 내부에서 다른 모듈의 변수에 접근해야 한다면 동적 import를 사용하세요:

```ts
await vi.hoisted(async () => {
  const { value } = await import("./some/module.js");
});
```

하지만 import는 이미 hoist되므로 `vi.hoisted` 내부에서 무엇이든 import하는 것은 권장되지 않습니다. 테스트 실행 전에 무언가를 실행해야 한다면, import된 모듈 자체에서 실행하면 됩니다.
:::

이 메서드는 factory가 반환한 값을 반환합니다. 로컬에 정의된 변수에 쉽게 접근해야 한다면 해당 값을 `vi.mock` factory에서 사용할 수 있습니다:

```ts
import { expect, vi } from "vitest";
import { originalMethod } from "./path/to/module.js";

const { mockedMethod } = vi.hoisted(() => {
  return { mockedMethod: vi.fn() };
});

vi.mock("./path/to/module.js", () => {
  return { originalMethod: mockedMethod };
});

mockedMethod.mockReturnValue(100);
expect(originalMethod()).toBe(100);
```

또한 이 메서드는 환경이 top-level await를 지원하지 않더라도 비동기로 호출할 수 있습니다:

```ts
const json = await vi.hoisted(async () => {
  const response = await fetch("https://jsonplaceholder.typicode.com/posts");
  return response.json();
});
```

### vi.setConfig

```ts
function setConfig(config: RuntimeOptions): void;
```

현재 테스트 파일의 config를 업데이트합니다. 이 메서드는 현재 테스트 파일에 영향을 주는 config 옵션만 지원합니다:

```ts
vi.setConfig({
  allowOnly: true,
  testTimeout: 10_000,
  hookTimeout: 10_000,
  clearMocks: true,
  restoreMocks: true,
  fakeTimers: {
    now: new Date(2021, 11, 19),
    // supports the whole object
  },
  maxConcurrency: 10,
  sequence: {
    hooks: "stack",
    // supports only "sequence.hooks"
  },
});
```

### vi.resetConfig

```ts
function resetConfig(): void;
```

이전에 [`vi.setConfig`](#vi-setconfig)가 호출되었다면, config를 원래 상태로 재설정합니다.
