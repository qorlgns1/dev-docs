---
title: "테스트 API 레퍼런스"
description: "아래 타입들은 아래의 타입 시그니처에서 사용됩니다."
---

출처 URL: https://vitest.dev/api

# 테스트 API 레퍼런스

아래 타입들은 아래의 타입 시그니처에서 사용됩니다.

```ts
type Awaitable<T> = T | PromiseLike<T>;
type TestFunction = () => Awaitable<void>;

interface TestOptions {
  /**
   * Will fail the test if it takes too long to execute
   */
  timeout?: number;
  /**
   * Will retry the test specific number of times if it fails
   *
   * @default 0
   */
  retry?: number;
  /**
   * Will repeat the same test several times even if it fails each time
   * If you have "retry" option and it fails, it will use every retry in each cycle
   * Useful for debugging random failings
   *
   * @default 0
   */
  repeats?: number;
}
```

테스트 함수가 promise를 반환하면, 러너는 비동기 기대값을 수집하기 위해 해당 promise가 resolve될 때까지 기다립니다. promise가 reject되면 테스트는 실패합니다.

::: tip
Jest에서는 `TestFunction`이 `(done: DoneCallback) => void` 타입일 수도 있습니다. 이 형태를 사용하면 `done`이 호출될 때까지 테스트가 종료되지 않습니다. 동일한 동작은 `async` 함수를 사용해 구현할 수 있습니다. [Migration guide Done Callback section](https://vitest.dev/guide/migration#done-callback)을 참고하세요.
:::

함수에 프로퍼티를 체이닝하여 옵션을 정의할 수 있습니다.

```ts
import { test } from "vitest";

test.skip("skipped test", () => {
  // some logic that fails right now
});

test.concurrent.skip("skipped concurrent test", () => {
  // some logic that fails right now
});
```

하지만 두 번째 인수로 객체를 전달할 수도 있습니다.

```ts
import { test } from "vitest";

test("skipped test", { skip: true }, () => {
  // some logic that fails right now
});

test("skipped concurrent test", { skip: true, concurrent: true }, () => {
  // some logic that fails right now
});
```

두 방식은 완전히 동일하게 동작합니다. 어느 쪽을 사용할지는 순전히 스타일 선택입니다.

`timeout`을 마지막 인수로 제공하는 경우에는 더 이상 options를 사용할 수 없다는 점에 유의하세요.

```ts
import { test } from "vitest";

// ✅ this works
test.skip("heavy test", () => {
  // ...
}, 10_000);

// ❌ this doesn't work
test(
  "heavy test",
  { skip: true },
  () => {
    // ...
  },
  10_000,
);
```

하지만 객체 내부에 timeout을 넣어 전달할 수는 있습니다.

```ts
import { test } from "vitest";

// ✅ this works
test("heavy test", { skip: true, timeout: 10_000 }, () => {
  // ...
});
```

## test

- **별칭:** `it`

`test`는 서로 관련된 기대값 집합을 정의합니다. 테스트 이름과, 테스트할 기대값을 담은 함수를 인수로 받습니다.

선택적으로, 종료 전까지 대기 시간을 지정하는 timeout(밀리초)을 제공할 수 있습니다. 기본값은 5초이며, [testTimeout](https://vitest.dev/config/#testtimeout)으로 전역 설정할 수 있습니다.

```ts
import { expect, test } from "vitest";

test("should work as expected", () => {
  expect(Math.sqrt(4)).toBe(2);
});
```

### test.extend {#test-extended}

- **별칭:** `it.extend`

`test.extend`를 사용해 테스트 컨텍스트를 커스텀 fixture로 확장할 수 있습니다. 이는 새로운 `test`를 반환하며, 그 자체로도 확장 가능하므로 필요에 따라 fixture를 더 조합하거나 기존 fixture를 오버라이드할 수 있습니다. 자세한 내용은 [Extend Test Context](https://vitest.dev/guide/test-context.html#test-extend)를 참고하세요.

```ts
import { expect, test } from "vitest";

const todos = [];
const archive = [];

const myTest = test.extend({
  todos: async ({ task }, use) => {
    todos.push(1, 2, 3);
    await use(todos);
    todos.length = 0;
  },
  archive,
});

myTest("add item", ({ todos }) => {
  expect(todos.length).toBe(3);

  todos.push(4);
  expect(todos.length).toBe(4);
});
```

### test.skip

- **별칭:** `it.skip`

특정 테스트 실행을 건너뛰고 싶지만 어떤 이유로 코드를 삭제하고 싶지 않다면, `test.skip`을 사용해 실행을 피할 수 있습니다.

```ts
import { assert, test } from "vitest";

test.skip("skipped test", () => {
  // Test skipped, no error
  assert.equal(Math.sqrt(4), 3);
});
```

[context](https://vitest.dev/guide/test-context)에서 `skip`을 동적으로 호출해 테스트를 건너뛸 수도 있습니다.

```ts
import { assert, test } from "vitest";

test("skipped test", (context) => {
  context.skip();
  // Test skipped, no error
  assert.equal(Math.sqrt(4), 3);
});
```

Vitest 3.1부터는 조건이 불명확한 경우, 첫 번째 인수로 조건을 `skip` 메서드에 전달할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("skipped test", (context) => {
  context.skip(Math.random() < 0.5, "optional message");
  // Test skipped, no error
  assert.equal(Math.sqrt(4), 3);
});
```

### test.skipIf

- **별칭:** `it.skipIf`

경우에 따라 서로 다른 환경에서 테스트를 여러 번 실행할 수 있고, 일부 테스트는 환경에 종속적일 수 있습니다. 테스트 코드를 `if`로 감싸는 대신, 조건이 truthy일 때마다 테스트를 건너뛰도록 `test.skipIf`를 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

const isDev = process.env.NODE_ENV === "development";

test.skipIf(isDev)("prod only test", () => {
  // this test only runs in production
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### test.runIf

- **별칭:** `it.runIf`

[test.skipIf](#test-skipif)의 반대입니다.

```ts
import { assert, test } from "vitest";

const isDev = process.env.NODE_ENV === "development";

test.runIf(isDev)("dev only test", () => {
  // this test only runs in development
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### test.only

- **별칭:** `it.only`

주어진 스위트에서 특정 테스트만 실행하려면 `test.only`를 사용하세요. 디버깅할 때 유용합니다.

선택적으로, 종료 전까지 대기 시간을 지정하는 timeout(밀리초)을 제공할 수 있습니다. 기본값은 5초이며, [testTimeout](https://vitest.dev/config/#testtimeout)으로 전역 설정할 수 있습니다.

```ts
import { assert, test } from "vitest";

test.only("test", () => {
  // Only this test (and others marked with only) are run
  assert.equal(Math.sqrt(4), 2);
});
```

때로는 전체 테스트 스위트의 다른 모든 테스트를 무시하고 특정 파일의 `only` 테스트만 실행하는 것이 매우 유용합니다. 다른 테스트가 출력 결과를 오염시킬 수 있기 때문입니다.

이를 위해 해당 테스트가 들어 있는 특정 파일을 지정하여 `vitest`를 실행하세요.

```
# vitest interesting.test.ts
```

### test.concurrent

- **별칭:** `it.concurrent`

`test.concurrent`는 연속된 테스트를 병렬 실행하도록 표시합니다. 테스트 이름, 수집할 테스트를 담은 async 함수, 그리고 선택적 timeout(밀리초)을 받습니다.

```ts
import { describe, test } from "vitest";

// The two tests marked with concurrent will be run in parallel
describe("suite", () => {
  test("serial test", async () => {
    /* ... */
  });
  test.concurrent("concurrent test 1", async () => {
    /* ... */
  });
  test.concurrent("concurrent test 2", async () => {
    /* ... */
  });
});
```

`test.skip`, `test.only`, `test.todo`는 concurrent 테스트와 함께 동작합니다. 아래 조합은 모두 유효합니다.

```ts
test.concurrent(/* ... */);
test.skip.concurrent(/* ... */); // or test.concurrent.skip(/* ... */)
test.only.concurrent(/* ... */); // or test.concurrent.only(/* ... */)
test.todo.concurrent(/* ... */); // or test.concurrent.todo(/* ... */)
```

concurrent 테스트를 실행할 때는 올바른 테스트를 감지할 수 있도록 Snapshot과 Assertion에서 로컬 [Test Context](https://vitest.dev/guide/test-context.md)의 `expect`를 사용해야 합니다.

```ts
test.concurrent("test 1", async ({ expect }) => {
  expect(foo).toMatchSnapshot();
});
test.concurrent("test 2", async ({ expect }) => {
  expect(foo).toMatchSnapshot();
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### test.sequential

- **별칭:** `it.sequential`

`test.sequential`은 테스트를 순차 실행으로 표시합니다. `describe.concurrent` 내부에서 또는 `--sequence.concurrent` 명령 옵션과 함께 테스트를 순서대로 실행하고 싶을 때 유용합니다.

```ts
import { describe, test } from "vitest";

// with config option { sequence: { concurrent: true } }
test("concurrent test 1", async () => {
  /* ... */
});
test("concurrent test 2", async () => {
  /* ... */
});

test.sequential("sequential test 1", async () => {
  /* ... */
});
test.sequential("sequential test 2", async () => {
  /* ... */
});

// within concurrent suite
describe.concurrent("suite", () => {
  test("concurrent test 1", async () => {
    /* ... */
  });
  test("concurrent test 2", async () => {
    /* ... */
  });

  test.sequential("sequential test 1", async () => {
    /* ... */
  });
  test.sequential("sequential test 2", async () => {
    /* ... */
  });
});
```

### test.todo

- **별칭:** `it.todo`

나중에 구현할 테스트의 스텁을 만들려면 `test.todo`를 사용하세요. 아직 구현이 필요한 테스트 수를 알 수 있도록 리포트에 항목이 표시됩니다.

```ts
// An entry will be shown in the report for this test
test.todo("unimplemented test");
```

### test.fails

- **별칭:** `it.fails`

Assertion이 명시적으로 실패해야 함을 나타내려면 `test.fails`를 사용하세요.

```ts
import { expect, test } from "vitest";

function myAsyncFunc() {
  return new Promise((resolve) => resolve(1));
}
test.fails("fail test", async () => {
  await expect(myAsyncFunc()).rejects.toBe(1);
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### test.each

- **별칭:** `it.each`

::: tip
`test.each`는 Jest 호환성을 위해 제공되지만,
Vitest는 [`TestContext`](https://vitest.dev/guide/test-context)를 통합하는 추가 기능이 있는 [`test.for`](#test-for)도 제공합니다.
:::

서로 다른 변수로 동일한 테스트를 실행해야 할 때 `test.each`를 사용합니다.
테스트 이름에 [printf formatting](https://nodejs.org/api/util.html#util_util_format_format_args)을 사용해 테스트 함수 파라미터 순서대로 매개변수를 주입할 수 있습니다.

- `%s`: 문자열
- `%d`: 숫자
- `%i`: 정수
- `%f`: 부동소수점 값
- `%j`: json
- `%o`: 객체
- `%#`: 테스트 케이스의 0 기반 인덱스
- `%$`: 테스트 케이스의 1 기반 인덱스
- `%%`: 퍼센트 기호 하나('%')

```ts
import { expect, test } from "vitest";

test.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add(%i, %i) -> %i", (a, b, expected) => {
  expect(a + b).toBe(expected);
});

// this will return
// ✓ add(1, 1) -> 2
// ✓ add(1, 2) -> 3
// ✓ add(2, 1) -> 3
```

`$` 접두사를 사용해 객체 프로퍼티와 배열 요소에도 접근할 수 있습니다.

```ts
test.each([
  { a: 1, b: 1, expected: 2 },
  { a: 1, b: 2, expected: 3 },
  { a: 2, b: 1, expected: 3 },
])("add($a, $b) -> $expected", ({ a, b, expected }) => {
  expect(a + b).toBe(expected);
});

// this will return
// ✓ add(1, 1) -> 2
// ✓ add(1, 2) -> 3
// ✓ add(2, 1) -> 3

test.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add($0, $1) -> $2", (a, b, expected) => {
  expect(a + b).toBe(expected);
});

// this will return
// ✓ add(1, 1) -> 2
// ✓ add(1, 2) -> 3
// ✓ add(2, 1) -> 3
```

인수로 객체를 사용하는 경우 `.`을 사용해 객체 속성에도 접근할 수 있습니다.

```ts
test.each`
  a             | b      | expected
  ${{ val: 1 }} | ${"b"} | ${"1b"}
  ${{ val: 2 }} | ${"b"} | ${"2b"}
  ${{ val: 3 }} | ${"b"} | ${"3b"}
`("add($a.val, $b) -> $expected", ({ a, b, expected }) => {
  expect(a.val + b).toBe(expected);
});

// this will return
// ✓ add(1, b) -> 1b
// ✓ add(2, b) -> 2b
// ✓ add(3, b) -> 3b
```

- 첫 번째 행은 `|`로 구분된 컬럼 이름이어야 합니다.
- 그다음 하나 이상의 데이터 행은 `${value}` 문법의 템플릿 리터럴 표현식으로 제공됩니다.

```ts
import { expect, test } from "vitest";

test.each`
  a             | b      | expected
  ${1}          | ${1}   | ${2}
  ${"a"}        | ${"b"} | ${"ab"}
  ${[]}         | ${"b"} | ${"b"}
  ${{}}         | ${"b"} | ${"[object Object]b"}
  ${{ asd: 1 }} | ${"b"} | ${"[object Object]b"}
`("returns $expected when $a is added $b", ({ a, b, expected }) => {
  expect(a + b).toBe(expected);
});
```

::: tip
Vitest는 `$values`를 Chai의 `format` 메서드로 처리합니다. 값이 너무 많이 잘린다면, 설정 파일에서 [chaiConfig.truncateThreshold](https://vitest.dev/config/#chaiconfig-truncatethreshold)를 늘릴 수 있습니다.
:::

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### test.for

- **별칭:** `it.for`

[`TestContext`](https://vitest.dev/guide/test-context)를 제공하는 `test.each`의 대안입니다.

`test.each`와의 차이는 인수에서 배열을 제공하는 방식에 있습니다.
`test.for`의 비배열 인수(템플릿 문자열 사용 포함)는 `test.each`와 정확히 동일하게 동작합니다.

```ts
// `each` spreads arrays
test.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add(%i, %i) -> %i", (a, b, expected) => {
  // [!code --]
  expect(a + b).toBe(expected);
});

// `for` doesn't spread arrays (notice the square brackets around the arguments)
test.for([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add(%i, %i) -> %i", ([a, b, expected]) => {
  // [!code ++]
  expect(a + b).toBe(expected);
});
```

두 번째 인수는 [`TestContext`](https://vitest.dev/guide/test-context)이며, 예를 들어 concurrent snapshot에 사용할 수 있습니다.

```ts
test.concurrent.for([
  [1, 1],
  [1, 2],
  [2, 1],
])("add(%i, %i)", ([a, b], { expect }) => {
  expect(a + b).matchSnapshot();
});
```

## bench

- **타입:** `(name: string | Function, fn: BenchFunction, options?: BenchOptions) => void`

`bench`는 벤치마크를 정의합니다. Vitest에서 벤치마크는 일련의 연산을 정의하는 함수입니다. Vitest는 이 함수를 여러 번 실행해 다양한 성능 결과를 표시합니다.

Vitest는 내부적으로 [`tinybench`](https://github.com/tinylibs/tinybench) 라이브러리를 사용하며, 세 번째 인수로 사용할 수 있는 해당 라이브러리의 모든 옵션을 상속합니다.

```ts
import { bench } from "vitest";

bench(
  "normal sorting",
  () => {
    const x = [1, 5, 4, 2, 3];
    x.sort((a, b) => {
      return a - b;
    });
  },
  { time: 1000 },
);
```

```ts
export interface Options {
  /**
   * time needed for running a benchmark task (milliseconds)
   * @default 500
   */
  time?: number;

  /**
   * number of times that a task should run if even the time option is finished
   * @default 10
   */
  iterations?: number;

  /**
   * function to get the current timestamp in milliseconds
   */
  now?: () => number;

  /**
   * An AbortSignal for aborting the benchmark
   */
  signal?: AbortSignal;

  /**
   * Throw if a task fails (events will not work if true)
   */
  throws?: boolean;

  /**
   * warmup time (milliseconds)
   * @default 100ms
   */
  warmupTime?: number;

  /**
   * warmup iterations
   * @default 5
   */
  warmupIterations?: number;

  /**
   * setup function to run before each benchmark task (cycle)
   */
  setup?: Hook;

  /**
   * teardown function to run after each benchmark task (cycle)
   */
  teardown?: Hook;
}
```

테스트 케이스 실행 후 출력 구조 정보는 다음과 같습니다.

```
  name                      hz     min     max    mean     p75     p99    p995    p999     rme  samples
· normal sorting  6,526,368.12  0.0001  0.3638  0.0002  0.0002  0.0002  0.0002  0.0004  ±1.41%   652638
```

```ts
export interface TaskResult {
  /*
   * the last error that was thrown while running the task
   */
  error?: unknown;

  /**
   * The amount of time in milliseconds to run the benchmark task (cycle).
   */
  totalTime: number;

  /**
   * the minimum value in the samples
   */
  min: number;
  /**
   * the maximum value in the samples
   */
  max: number;

  /**
   * the number of operations per second
   */
  hz: number;

  /**
   * how long each operation takes (ms)
   */
  period: number;

  /**
   * task samples of each task iteration time (ms)
   */
  samples: number[];

  /**
   * samples mean/average (estimate of the population mean)
   */
  mean: number;

  /**
   * samples variance (estimate of the population variance)
   */
  variance: number;

  /**
   * samples standard deviation (estimate of the population standard deviation)
   */
  sd: number;

  /**
   * standard error of the mean (a.k.a. the standard deviation of the sampling distribution of the sample mean)
   */
  sem: number;

  /**
   * degrees of freedom
   */
  df: number;

  /**
   * critical value of the samples
   */
  critical: number;

  /**
   * margin of error
   */
  moe: number;

  /**
   * relative margin of error
   */
  rme: number;

  /**
   * median absolute deviation
   */
  mad: number;

  /**
   * p50/median percentile
   */
  p50: number;

  /**
   * p75 percentile
   */
  p75: number;

  /**
   * p99 percentile
   */
  p99: number;

  /**
   * p995 percentile
   */
  p995: number;

  /**
   * p999 percentile
   */
  p999: number;
}
```

### bench.skip

- **타입:** `(name: string | Function, fn: BenchFunction, options?: BenchOptions) => void`

특정 벤치마크 실행을 건너뛰려면 `bench.skip` 문법을 사용할 수 있습니다.

```ts
import { bench } from "vitest";

bench.skip("normal sorting", () => {
  const x = [1, 5, 4, 2, 3];
  x.sort((a, b) => {
    return a - b;
  });
});
```

### bench.only

- **타입:** `(name: string | Function, fn: BenchFunction, options?: BenchOptions) => void`

주어진 스위트에서 특정 벤치마크만 실행하려면 `bench.only`를 사용하세요. 디버깅할 때 유용합니다.

```ts
import { bench } from "vitest";

bench.only("normal sorting", () => {
  const x = [1, 5, 4, 2, 3];
  x.sort((a, b) => {
    return a - b;
  });
});
```

### bench.todo

- **타입:** `(name: string | Function) => void`

나중에 구현할 벤치마크의 스텁을 만들려면 `bench.todo`를 사용하세요.

```ts
import { bench } from "vitest";

bench.todo("unimplemented test");
```

## describe

파일 최상위 레벨에서 `test` 또는 `bench`를 사용하면 해당 파일의 암묵적 스위트 일부로 수집됩니다. `describe`를 사용하면 현재 컨텍스트에 새 스위트를 정의할 수 있으며, 이는 서로 관련된 테스트나 벤치마크, 그리고 기타 중첩 스위트의 집합입니다. 스위트를 사용하면 테스트와 벤치마크를 정리해 리포트를 더 명확하게 만들 수 있습니다.

```ts
// basic.spec.ts
// organizing tests

import { describe, expect, test } from "vitest";

const person = {
  isActive: true,
  age: 32,
};

describe("person", () => {
  test("person is defined", () => {
    expect(person).toBeDefined();
  });

  test("is active", () => {
    expect(person.isActive).toBeTruthy();
  });

  test("age limit", () => {
    expect(person.age).toBeLessThanOrEqual(32);
  });
});
```

```ts
// basic.bench.ts
// organizing benchmarks

import { bench, describe } from "vitest";

describe("sort", () => {
  bench("normal", () => {
    const x = [1, 5, 4, 2, 3];
    x.sort((a, b) => {
      return a - b;
    });
  });

  bench("reverse", () => {
    const x = [1, 5, 4, 2, 3];
    x.reverse().sort((a, b) => {
      return a - b;
    });
  });
});
```

테스트 또는 벤치마크에 계층 구조가 있는 경우 describe 블록을 중첩할 수도 있습니다.

```ts
import { describe, expect, test } from "vitest";

function numberToCurrency(value: number | string) {
  if (typeof value !== "number") {
    throw new TypeError("Value must be a number");
  }

  return value
    .toFixed(2)
    .toString()
    .replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

describe("numberToCurrency", () => {
  describe("given an invalid number", () => {
    test("composed of non-numbers to throw error", () => {
      expect(() => numberToCurrency("abc")).toThrowError();
    });
  });

  describe("given a valid number", () => {
    test("returns the correct currency format", () => {
      expect(numberToCurrency(10000)).toBe("10,000.00");
    });
  });
});
```

### describe.skip

- **별칭:** `suite.skip`

특정 describe 블록 실행을 피하려면 스위트에서 `describe.skip`을 사용하세요.

```ts
import { assert, describe, test } from "vitest";

describe.skip("skipped suite", () => {
  test("sqrt", () => {
    // Suite skipped, no error
    assert.equal(Math.sqrt(4), 3);
  });
});
```

### describe.skipIf

- **별칭:** `suite.skipIf`

경우에 따라 서로 다른 환경에서 스위트를 여러 번 실행할 수 있고, 일부 스위트는 환경에 종속적일 수 있습니다. 스위트를 `if`로 감싸는 대신, 조건이 truthy일 때마다 스위트를 건너뛰도록 `describe.skipIf`를 사용할 수 있습니다.

```ts
import { describe, test } from "vitest";

const isDev = process.env.NODE_ENV === "development";

describe.skipIf(isDev)("prod only test suite", () => {
  // this test suite only runs in production
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### describe.runIf

- **별칭:** `suite.runIf`

[describe.skipIf](#describe-skipif)의 반대입니다.

```ts
import { assert, describe, test } from "vitest";

const isDev = process.env.NODE_ENV === "development";

describe.runIf(isDev)("dev only test suite", () => {
  // this test suite only runs in development
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### describe.only

- **타입:** `(name: string | Function, fn: TestFunction, options?: number | TestOptions) => void`

특정 스위트만 실행하려면 `describe.only`를 사용하세요.

```ts
import { assert, describe, test } from "vitest";

// Only this suite (and others marked with only) are run
describe.only("suite", () => {
  test("sqrt", () => {
    assert.equal(Math.sqrt(4), 3);
  });
});

describe("other suite", () => {
  // ... will be skipped
});
```

때로는 전체 테스트 스위트의 다른 모든 테스트를 무시하고 특정 파일의 `only` 테스트만 실행하는 것이 매우 유용합니다. 다른 테스트가 출력 결과를 오염시킬 수 있기 때문입니다.

이를 위해 해당 테스트가 들어 있는 특정 파일을 지정하여 `vitest`를 실행하세요.

```
# vitest interesting.test.ts
```

### describe.concurrent

- **별칭:** `suite.concurrent`

`describe.concurrent`는 내부의 모든 스위트와 테스트를 병렬 실행합니다.

```ts
import { describe, test } from "vitest";

// All suites and tests within this suite will be run in parallel
describe.concurrent("suite", () => {
  test("concurrent test 1", async () => {
    /* ... */
  });
  describe("concurrent suite 2", async () => {
    test("concurrent test inner 1", async () => {
      /* ... */
    });
    test("concurrent test inner 2", async () => {
      /* ... */
    });
  });
  test.concurrent("concurrent test 3", async () => {
    /* ... */
  });
});
```

`.skip`, `.only`, `.todo`는 concurrent 스위트와 함께 동작합니다. 아래 조합은 모두 유효합니다.

```ts
describe.concurrent(/* ... */);
describe.skip.concurrent(/* ... */); // or describe.concurrent.skip(/* ... */)
describe.only.concurrent(/* ... */); // or describe.concurrent.only(/* ... */)
describe.todo.concurrent(/* ... */); // or describe.concurrent.todo(/* ... */)
```

concurrent 테스트를 실행할 때는 올바른 테스트를 감지할 수 있도록 Snapshot과 Assertion에서 로컬 [Test Context](https://vitest.dev/guide/test-context)의 `expect`를 사용해야 합니다.

```ts
describe.concurrent("suite", () => {
  test("concurrent test 1", async ({ expect }) => {
    expect(foo).toMatchSnapshot();
  });
  test("concurrent test 2", async ({ expect }) => {
    expect(foo).toMatchSnapshot();
  });
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### describe.sequential

- **별칭:** `suite.sequential`

스위트에서 `describe.sequential`은 모든 테스트를 순차 실행으로 표시합니다. `describe.concurrent` 내부에서 또는 `--sequence.concurrent` 명령 옵션과 함께 테스트를 순서대로 실행하고 싶을 때 유용합니다.

```ts
import { describe, test } from "vitest";

describe.concurrent("suite", () => {
  test("concurrent test 1", async () => {
    /* ... */
  });
  test("concurrent test 2", async () => {
    /* ... */
  });

  describe.sequential("", () => {
    test("sequential test 1", async () => {
      /* ... */
    });
    test("sequential test 2", async () => {
      /* ... */
    });
  });
});
```

### describe.shuffle

- **별칭:** `suite.shuffle`

Vitest는 CLI 플래그 [`--sequence.shuffle`](https://vitest.dev/guide/cli) 또는 설정 옵션 [`sequence.shuffle`](https://vitest.dev/config/#sequence-shuffle)을 통해 모든 테스트를 무작위 순서로 실행하는 방법을 제공하지만, 테스트 스위트의 일부만 무작위 순서로 실행하고 싶다면 이 플래그로 표시할 수 있습니다.

```ts
import { describe, test } from "vitest";

// or describe('suite', { shuffle: true }, ...)
describe.shuffle("suite", () => {
  test("random test 1", async () => {
    /* ... */
  });
  test("random test 2", async () => {
    /* ... */
  });
  test("random test 3", async () => {
    /* ... */
  });

  // `shuffle` is inherited
  describe("still random", () => {
    test("random 4.1", async () => {
      /* ... */
    });
    test("random 4.2", async () => {
      /* ... */
    });
  });

  // disable shuffle inside
  describe("not random", { shuffle: false }, () => {
    test("in order 5.1", async () => {
      /* ... */
    });
    test("in order 5.2", async () => {
      /* ... */
    });
  });
});
// order depends on sequence.seed option in config (Date.now() by default)
```

`.skip`, `.only`, `.todo`는 무작위 스위트와 함께 동작합니다.

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용할 때는 이 문법을 사용할 수 없습니다.
:::

### describe.todo

- **별칭:** `suite.todo`

나중에 구현할 스위트의 스텁을 만들려면 `describe.todo`를 사용하세요. 아직 구현이 필요한 테스트 수를 알 수 있도록 리포트에 항목이 표시됩니다.

```ts
// An entry will be shown in the report for this suite
describe.todo("unimplemented suite");
```

### describe.each

- **별칭:** `suite.each`

::: tip
`describe.each`는 Jest 호환성을 위해 제공되지만,
Vitest는 인수 타입을 단순화하고 [`test.for`](#test-for)와 정렬되는 [`describe.for`](#describe-for)도 제공합니다.
:::

같은 데이터에 의존하는 테스트가 둘 이상이면 `describe.each`를 사용하세요.

```ts
import { describe, expect, test } from "vitest";

describe.each([
  { a: 1, b: 1, expected: 2 },
  { a: 1, b: 2, expected: 3 },
  { a: 2, b: 1, expected: 3 },
])("describe object add($a, $b)", ({ a, b, expected }) => {
  test(`returns ${expected}`, () => {
    expect(a + b).toBe(expected);
  });

  test(`returned value not be greater than ${expected}`, () => {
    expect(a + b).not.toBeGreaterThan(expected);
  });

  test(`returned value not be less than ${expected}`, () => {
    expect(a + b).not.toBeLessThan(expected);
  });
});
```

- 첫 번째 행은 `|`로 구분된 컬럼 이름이어야 합니다;
- 그 다음에는 `${value}` 문법을 사용하는 템플릿 리터럴 표현식으로 하나 이상의 데이터 행을 제공합니다.

```ts
import { describe, expect, test } from "vitest";

describe.each`
  a             | b      | expected
  ${1}          | ${1}   | ${2}
  ${"a"}        | ${"b"} | ${"ab"}
  ${[]}         | ${"b"} | ${"b"}
  ${{}}         | ${"b"} | ${"[object Object]b"}
  ${{ asd: 1 }} | ${"b"} | ${"[object Object]b"}
`("describe template string add($a, $b)", ({ a, b, expected }) => {
  test(`returns ${expected}`, () => {
    expect(a + b).toBe(expected);
  });
});
```

::: warning
Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용하는 경우에는 이 문법을 사용할 수 없습니다.
:::

### describe.for

- **별칭:** `suite.for`

`describe.each`와의 차이점은 배열 케이스를 인수로 전달하는 방식입니다.
배열이 아닌 다른 케이스(템플릿 문자열 사용 포함)는 완전히 동일하게 동작합니다.

```ts
// `each` spreads array case
describe.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add(%i, %i) -> %i", (a, b, expected) => {
  // [!code --]
  test("test", () => {
    expect(a + b).toBe(expected);
  });
});

// `for` doesn't spread array case
describe.for([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])("add(%i, %i) -> %i", ([a, b, expected]) => {
  // [!code ++]
  test("test", () => {
    expect(a + b).toBe(expected);
  });
});
```

## Setup and Teardown

이 함수들을 사용하면 테스트 생명주기에 훅을 걸어 setup 및 teardown 코드를 반복하지 않아도 됩니다. 이 함수들은 현재 컨텍스트에 적용됩니다. 즉, 최상위 레벨에서 사용하면 파일에 적용되고, `describe` 블록 내부에서 사용하면 현재 suite에 적용됩니다. Vitest를 타입 체커로 실행 중일 때는 이 훅들이 호출되지 않습니다.

### beforeEach

- **타입:** `beforeEach(fn: () => Awaitable<void>, timeout?: number)`

현재 컨텍스트의 각 테스트가 실행되기 전에 호출될 콜백을 등록합니다.
함수가 promise를 반환하면, Vitest는 해당 promise가 resolve될 때까지 기다린 뒤 테스트를 실행합니다.

선택적으로 종료 전 대기 시간을 정의하는 timeout(밀리초)을 전달할 수 있습니다. 기본값은 5초입니다.

```ts
import { beforeEach } from "vitest";

beforeEach(async () => {
  // Clear mocks and add some testing data before each test run
  await stopMocking();
  await addUser({ name: "John" });
});
```

여기서 `beforeEach`는 각 테스트마다 사용자가 추가되도록 보장합니다.

`beforeEach`는 선택적 cleanup 함수도 받을 수 있습니다(`afterEach`와 동일).

```ts
import { beforeEach } from "vitest";

beforeEach(async () => {
  // called once before each test run
  await prepareSomething();

  // clean up function, called once after each test run
  return async () => {
    await resetSomething();
  };
});
```

### afterEach

- **타입:** `afterEach(fn: () => Awaitable<void>, timeout?: number)`

현재 컨텍스트의 각 테스트가 완료된 뒤 호출될 콜백을 등록합니다.
함수가 promise를 반환하면, Vitest는 해당 promise가 resolve될 때까지 기다린 후 계속 진행합니다.

선택적으로 종료 전 대기 시간을 지정하는 timeout(밀리초)을 제공할 수 있습니다. 기본값은 5초입니다.

```ts
import { afterEach } from "vitest";

afterEach(async () => {
  await clearTestingData(); // clear testing data after each test run
});
```

여기서 `afterEach`는 각 테스트 실행 후 테스트 데이터가 정리되도록 보장합니다.

::: tip
테스트 실행 중 [`onTestFinished`](#ontestfinished)를 사용해 테스트가 완료된 뒤 상태를 정리할 수도 있습니다.
:::

### beforeAll

- **타입:** `beforeAll(fn: () => Awaitable<void>, timeout?: number)`

현재 컨텍스트의 모든 테스트 실행을 시작하기 전에 한 번 호출될 콜백을 등록합니다.
함수가 promise를 반환하면, Vitest는 해당 promise가 resolve될 때까지 기다린 뒤 테스트를 실행합니다.

선택적으로 종료 전 대기 시간을 지정하는 timeout(밀리초)을 제공할 수 있습니다. 기본값은 5초입니다.

```ts
import { beforeAll } from "vitest";

beforeAll(async () => {
  await startMocking(); // called once before all tests run
});
```

여기서 `beforeAll`은 테스트가 실행되기 전에 mock 데이터가 설정되도록 보장합니다.

`beforeAll`은 선택적 cleanup 함수도 받을 수 있습니다(`afterAll`과 동일).

```ts
import { beforeAll } from "vitest";

beforeAll(async () => {
  // called once before all tests run
  await startMocking();

  // clean up function, called once after all tests run
  return async () => {
    await stopMocking();
  };
});
```

### afterAll

- **타입:** `afterAll(fn: () => Awaitable<void>, timeout?: number)`

현재 컨텍스트의 모든 테스트가 실행된 뒤 한 번 호출될 콜백을 등록합니다.
함수가 promise를 반환하면, Vitest는 해당 promise가 resolve될 때까지 기다린 후 계속 진행합니다.

선택적으로 종료 전 대기 시간을 지정하는 timeout(밀리초)을 제공할 수 있습니다. 기본값은 5초입니다.

```ts
import { afterAll } from "vitest";

afterAll(async () => {
  await stopMocking(); // this method is called after all tests run
});
```

여기서 `afterAll`은 모든 테스트 실행 후 `stopMocking` 메서드가 호출되도록 보장합니다.

## Test Hooks

Vitest는 테스트가 완료된 뒤 상태를 정리할 수 있도록 테스트 실행 _중_ 호출할 수 있는 몇 가지 훅을 제공합니다.

::: warning
이 훅들은 테스트 본문 외부에서 호출하면 오류를 발생시킵니다.
:::

### onTestFinished {#ontestfinished}

이 훅은 테스트 실행이 완료된 뒤 항상 호출됩니다. `afterEach` 훅은 테스트 결과에 영향을 줄 수 있으므로, 이 훅은 `afterEach` 이후에 호출됩니다. `beforeEach`와 `afterEach`처럼 `ExtendedContext` 객체를 전달받습니다.

```ts {1,5}
import { onTestFinished, test } from "vitest";

test("performs a query", () => {
  const db = connectDb();
  onTestFinished(() => db.close());
  db.query("SELECT * FROM users");
});
```

::: warning
테스트를 동시 실행하는 경우, Vitest는 전역 훅에서 동시 테스트를 추적하지 않으므로 항상 테스트 컨텍스트의 `onTestFinished` 훅을 사용해야 합니다:

```ts {3,5}
import { test } from "vitest";

test.concurrent("performs a query", ({ onTestFinished }) => {
  const db = connectDb();
  onTestFinished(() => db.close());
  db.query("SELECT * FROM users");
});
```

:::

이 훅은 재사용 가능한 로직을 만들 때 특히 유용합니다:

```ts
// this can be in a separate file
function getTestDb() {
  const db = connectMockedDb();
  onTestFinished(() => db.close());
  return db;
}

test("performs a user query", async () => {
  const db = getTestDb();
  expect(await db.query("SELECT * from users").perform()).toEqual([]);
});

test("performs an organization query", async () => {
  const db = getTestDb();
  expect(await db.query("SELECT * from organizations").perform()).toEqual([]);
});
```

::: tip
이 훅은 항상 역순으로 호출되며 [`sequence.hooks`](https://vitest.dev/config/#sequence-hooks) 옵션의 영향을 받지 않습니다.
:::

### onTestFailed

이 훅은 테스트가 실패한 뒤에만 호출됩니다. `afterEach` 훅은 테스트 결과에 영향을 줄 수 있으므로, 이 훅은 `afterEach` 이후에 호출됩니다. `beforeEach`와 `afterEach`처럼 `ExtendedContext` 객체를 전달받습니다. 이 훅은 디버깅에 유용합니다.

```ts {1,5-7}
import { onTestFailed, test } from "vitest";

test("performs a query", () => {
  const db = connectDb();
  onTestFailed(({ task }) => {
    console.log(task.result.errors);
  });
  db.query("SELECT * FROM users");
});
```

::: warning
테스트를 동시 실행하는 경우, Vitest는 전역 훅에서 동시 테스트를 추적하지 않으므로 항상 테스트 컨텍스트의 `onTestFailed` 훅을 사용해야 합니다:

```ts {3,5-7}
import { test } from "vitest";

test.concurrent("performs a query", ({ onTestFailed }) => {
  const db = connectDb();
  onTestFailed(({ task }) => {
    console.log(task.result.errors);
  });
  db.query("SELECT * FROM users");
});
```

:::
