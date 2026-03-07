---
title: "테스트 컨텍스트"
description: "각 테스트 콜백의 첫 번째 인자는 테스트 컨텍스트입니다."
---

출처 URL: https://vitest.dev/guide/test-context

# 테스트 컨텍스트

[Playwright Fixtures](https://playwright.dev/docs/test-fixtures)에서 영감을 받은 Vitest의 테스트 컨텍스트를 사용하면 테스트에서 사용할 유틸리티, 상태, 픽스처를 정의할 수 있습니다.

## 사용법

각 테스트 콜백의 첫 번째 인자는 테스트 컨텍스트입니다.

```ts
import { it } from "vitest";

it("should work", ({ task }) => {
  // prints name of the test
  console.log(task.name);
});
```

## 내장 테스트 컨텍스트

#### `task`

테스트에 대한 메타데이터를 담고 있는 읽기 전용 객체입니다.

#### `expect`

현재 테스트에 바인딩된 `expect` API입니다:

```ts
import { it } from "vitest";

it("math is easy", ({ expect }) => {
  expect(2 + 2).toBe(4);
});
```

전역 expect는 이를 추적할 수 없기 때문에, 이 API는 스냅샷 테스트를 동시 실행할 때 유용합니다:

```ts
import { it } from "vitest";

it.concurrent("math is easy", ({ expect }) => {
  expect(2 + 2).toMatchInlineSnapshot();
});

it.concurrent("math is hard", ({ expect }) => {
  expect(2 * 2).toMatchInlineSnapshot();
});
```

#### `skip`

```ts
function skip(note?: string): never;
function skip(condition: boolean, note?: string): void;
```

이후 테스트 실행을 건너뛰고 테스트를 skipped로 표시합니다:

```ts
import { expect, it } from "vitest";

it("math is hard", ({ skip }) => {
  skip();
  expect(2 + 2).toBe(5);
});
```

Vitest 3.1부터는 boolean 파라미터를 받아 조건부로 테스트를 건너뛸 수 있습니다:

```ts
it("math is hard", ({ skip, mind }) => {
  skip(mind === "foggy");
  expect(2 + 2).toBe(5);
});
```

#### `annotate` 3.2.0 {#annotate}

```ts
function annotate(
  message: string,
  attachment?: TestAttachment,
): Promise<TestAnnotation>;

function annotate(
  message: string,
  type?: string,
  attachment?: TestAttachment,
): Promise<TestAnnotation>;
```

[reporter](https://vitest.dev/config/#reporters)에 표시될 [test annotation](https://vitest.dev/guide/test-annotations)을 추가합니다.

```ts
test("annotations API", async ({ annotate }) => {
  await annotate("https://github.com/vitest-dev/vitest/pull/7953", "issues");
});
```

#### `signal` 3.2.0 {#signal}

Vitest에 의해 중단될 수 있는 [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)입니다. 다음 상황에서 signal이 중단됩니다:

- 테스트 타임아웃 발생
- 사용자가 Ctrl+C로 테스트 실행을 수동 취소
- [`vitest.cancelCurrentRun`](https://vitest.dev/api/advanced/vitest#cancelcurrentrun)이 프로그래밍 방식으로 호출됨
- 다른 테스트가 병렬 실행 중 실패했고 [`bail`](https://vitest.dev/config/#bail) 플래그가 설정됨

```ts
it("stop request when test times out", async ({ signal }) => {
  await fetch("/resource", { signal });
}, 2000);
```

#### `onTestFailed`

현재 테스트에 바인딩된 [`onTestFailed`](https://vitest.dev/api/#ontestfailed) 훅입니다. 테스트를 동시 실행 중이고 특정 테스트에만 특별한 처리가 필요할 때 유용합니다.

#### `onTestFinished`

현재 테스트에 바인딩된 [`onTestFinished`](https://vitest.dev/api/#ontestfailed) 훅입니다. 테스트를 동시 실행 중이고 특정 테스트에만 특별한 처리가 필요할 때 유용합니다.

## 테스트 컨텍스트 확장

Vitest는 테스트 컨텍스트 확장을 돕기 위해 두 가지 방법을 제공합니다.

### `test.extend`

[Playwright](https://playwright.dev/docs/api/class-test#test-extend)와 마찬가지로, 이 메서드를 사용해 커스텀 픽스처를 포함한 나만의 `test` API를 정의하고 어디서든 재사용할 수 있습니다.

예를 들어, 먼저 `todos`와 `archive` 두 개의 픽스처를 가진 `test` 컬렉터를 만듭니다.

```ts [my-test.ts]
import { test as baseTest } from "vitest";

const todos = [];
const archive = [];

export const test = baseTest.extend({
  todos: async ({}, use) => {
    // setup the fixture before each test function
    todos.push(1, 2, 3);

    // use the fixture value
    await use(todos);

    // cleanup the fixture after each test function
    todos.length = 0;
  },
  archive,
});
```

그다음 이를 import해서 사용할 수 있습니다.

```ts [my-test.test.ts]
import { expect } from "vitest";
import { test } from "./my-test.js";

test("add items to todos", ({ todos }) => {
  expect(todos.length).toBe(3);

  todos.push(4);
  expect(todos.length).toBe(4);
});

test("move items from todos to archive", ({ todos, archive }) => {
  expect(todos.length).toBe(3);
  expect(archive.length).toBe(0);

  archive.push(todos.pop());
  expect(todos.length).toBe(2);
  expect(archive.length).toBe(1);
});
```

`test`를 확장하여 픽스처를 더 추가하거나 기존 픽스처를 오버라이드할 수도 있습니다.

```ts
import { test as todosTest } from "./my-test.js";

export const test = todosTest.extend({
  settings: {
    // ...
  },
});
```

#### 픽스처 초기화

Vitest 러너는 사용 여부를 기반으로 픽스처를 똑똑하게 초기화하고 테스트 컨텍스트에 주입합니다.

```ts
import { test as baseTest } from "vitest";

const test = baseTest.extend<{
  todos: number[];
  archive: number[];
}>({
  todos: async ({ task }, use) => {
    await use([1, 2, 3]);
  },
  archive: [],
});

// todos will not run
test("skip", () => {});
test("skip", ({ archive }) => {});

// todos will run
test("run", ({ todos }) => {});
```

::: warning
픽스처와 함께 `test.extend()`를 사용할 때는 픽스처 함수와 테스트 함수 모두에서 컨텍스트 접근 시 항상 객체 구조 분해 패턴 `{ todos }`를 사용해야 합니다.

```ts
test("context must be destructured", (context) => {
  // [!code --]
  expect(context.todos.length).toBe(2);
});

test("context must be destructured", ({ todos }) => {
  // [!code ++]
  expect(todos.length).toBe(2);
});
```

:::

#### 자동 픽스처

Vitest는 픽스처에 대한 tuple 문법도 지원하므로, 각 픽스처에 옵션을 전달할 수 있습니다. 예를 들어 테스트에서 사용되지 않더라도 픽스처를 명시적으로 초기화할 수 있습니다.

```ts
import { test as base } from "vitest";

const test = base.extend({
  fixture: [
    async ({}, use) => {
      // this function will run
      setup();
      await use();
      teardown();
    },
    { auto: true }, // Mark as an automatic fixture
  ],
});

test("works correctly");
```

#### 기본 픽스처

Vitest 3부터는 서로 다른 [projects](https://vitest.dev/guide/projects)에서 서로 다른 값을 제공할 수 있습니다. 이 기능을 활성화하려면 옵션에 `{ injected: true }`를 전달하세요. 키가 [project configuration](https://vitest.dev/config/#provide)에 지정되지 않았다면 기본값이 사용됩니다.

:::code-group

```ts [fixtures.test.ts]
import { test as base } from "vitest";

const test = base.extend({
  url: [
    // default value if "url" is not defined in the config
    "/default",
    // mark the fixture as "injected" to allow the override
    { injected: true },
  ],
});

test("works correctly", ({ url }) => {
  // url is "/default" in "project-new"
  // url is "/full" in "project-full"
  // url is "/empty" in "project-empty"
});
```

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        test: {
          name: "project-new",
        },
      },
      {
        test: {
          name: "project-full",
          provide: {
            url: "/full",
          },
        },
      },
      {
        test: {
          name: "project-empty",
          provide: {
            url: "/empty",
          },
        },
      },
    ],
  },
});
```

:::

#### 스위트 단위 값 스코핑 3.1.0 {#scoping-values-to-suite}

Vitest 3.1부터는 `test.scoped` API를 사용해 스위트 및 그 하위 항목별로 컨텍스트 값을 오버라이드할 수 있습니다:

```ts
import { test as baseTest, describe, expect } from "vitest";

const test = baseTest.extend({
  dependency: "default",
  dependant: ({ dependency }, use) => use({ dependency }),
});

describe("use scoped values", () => {
  test.scoped({ dependency: "new" });

  test("uses scoped value", ({ dependant }) => {
    // `dependant` uses the new overridden value that is scoped
    // to all tests in this suite
    expect(dependant).toEqual({ dependency: "new" });
  });

  describe("keeps using scoped value", () => {
    test("uses scoped value", ({ dependant }) => {
      // nested suite inherited the value
      expect(dependant).toEqual({ dependency: "new" });
    });
  });
});

test("keep using the default values", ({ dependant }) => {
  // the `dependency` is using the default
  // value outside of the suite with .scoped
  expect(dependant).toEqual({ dependency: "default" });
});
```

이 API는 데이터베이스 연결처럼 동적 변수에 의존하는 컨텍스트 값이 있을 때 특히 유용합니다:

```ts
const test = baseTest.extend<{
  db: Database;
  schema: string;
}>({
  db: async ({ schema }, use) => {
    const db = await createDb({ schema });
    await use(db);
    await cleanup(db);
  },
  schema: "",
});

describe("one type of schema", () => {
  test.scoped({ schema: "schema-1" });

  // ... tests
});

describe("another type of schema", () => {
  test.scoped({ schema: "schema-2" });

  // ... tests
});
```

#### 스코프별 컨텍스트 3.2.0

파일 또는 워커마다 한 번만 초기화되는 컨텍스트를 정의할 수 있습니다. 일반 픽스처와 동일하게 객체 파라미터로 초기화됩니다:

```ts
import { test as baseTest } from "vitest";

export const test = baseTest.extend({
  perFile: [({}, use) => use([]), { scope: "file" }],
  perWorker: [({}, use) => use([]), { scope: "worker" }],
});
```

값은 테스트 중 처음 접근될 때 초기화되며, 픽스처 옵션에 `auto: true`가 있으면 어떤 테스트도 실행되기 전에 초기화됩니다.

```ts
const test = baseTest.extend({
  perFile: [
    ({}, use) => use([]),
    {
      scope: "file",
      // always run this hook before any test
      auto: true,
    },
  ],
});
```

::: warning
내장 [`task`](#task) 테스트 컨텍스트는 파일 스코프 또는 워커 스코프 픽스처에서 **사용할 수 없습니다**. 이 픽스처들은 `task` 같은 테스트 전용 속성이 포함되지 않은 다른 컨텍스트 객체(파일 또는 워커 컨텍스트)를 받습니다.

파일 경로 같은 파일 레벨 메타데이터가 필요하다면 대신 `expect.getState().testPath`를 사용하세요.
:::

`worker` 스코프는 워커당 한 번 픽스처를 실행합니다. 실행 중인 워커 수는 여러 요인에 따라 달라집니다. 기본적으로 각 파일은 별도 워커에서 실행되므로 `file`과 `worker` 스코프는 동일하게 동작합니다.

하지만 [isolation](https://vitest.dev/config/#isolate)을 비활성화하면 워커 수는 [`maxWorkers`](https://vitest.dev/config/#maxworkers) 설정으로 제한됩니다.

`vmThreads` 또는 `vmForks`에서 테스트를 실행할 때 `scope: 'worker'`를 지정해도 `scope: 'file'`과 동일하게 동작한다는 점에 유의하세요. 이는 각 테스트 파일이 자체 VM 컨텍스트를 가지기 때문입니다. 만약 Vitest가 이를 한 번만 초기화하면 하나의 컨텍스트가 다른 컨텍스트로 누출되어 다양한 참조 불일치가 발생할 수 있습니다(예: 같은 클래스의 인스턴스가 서로 다른 생성자를 참조).

#### TypeScript

모든 커스텀 컨텍스트에 픽스처 타입을 제공하려면 픽스처 타입을 제네릭으로 전달하면 됩니다.

```ts
interface MyFixtures {
  todos: number[];
  archive: number[];
}

const test = baseTest.extend<MyFixtures>({
  todos: [],
  archive: [],
});

test("types are defined correctly", ({ todos, archive }) => {
  expectTypeOf(todos).toEqualTypeOf<number[]>();
  expectTypeOf(archive).toEqualTypeOf<number[]>();
});
```

::: info Type Inferring
Vitest는 `use` 함수가 호출될 때 타입 추론을 지원하지 않습니다. `test.extend`를 호출할 때 전체 컨텍스트 타입을 제네릭 타입으로 전달하는 방식을 항상 권장합니다:

```ts
import { test as baseTest } from "vitest";

const test = baseTest.extend<{
  todos: number[];
  schema: string;
}>({
  todos: ({ schema }, use) => use([]),
  schema: "test",
});

test("types are correct", ({
  todos, // number[]
  schema, // string
}) => {
  // ...
});
```

:::

`test.extend`를 사용하면 확장된 `test` 객체가 새로운 컨텍스트를 인지하는 타입 안전한 `beforeEach` 및 `afterEach` 훅을 제공합니다:

```ts
const test = baseTest.extend<{
  todos: number[];
}>({
  todos: async ({}, use) => {
    await use([]);
  },
});

// Unlike global hooks, these hooks are aware of the extended context
test.beforeEach(({ todos }) => {
  todos.push(1);
});

test.afterEach(({ todos }) => {
  console.log(todos);
});
```
