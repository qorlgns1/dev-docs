---
title: "테스트, 개발, 빌드 간 공유 설정"
description: "Vite의 config, transformers, resolvers, plugins를 사용합니다. 테스트를 실행할 때 앱과 동일한 설정을 사용하세요."
---

출처 URL: https://vitest.dev/guide/features

# 기능

## 테스트, 개발, 빌드 간 공유 설정

Vite의 config, transformers, resolvers, plugins를 사용합니다. 테스트를 실행할 때 앱과 동일한 설정을 사용하세요.

자세한 내용은 [Configuring Vitest](https://vitest.dev/guide/#configuring-vitest)에서 확인하세요.

## Watch 모드

```bash
$ vitest
```

소스 코드나 테스트 파일을 수정하면, Vitest는 Vite의 HMR 동작 방식처럼 모듈 그래프를 똑똑하게 탐색해 관련된 테스트만 다시 실행합니다.

`vitest`는 **개발 환경에서는 기본적으로** `watch mode`로 시작하고, CI 환경(`process.env.CI`가 존재할 때)에서는 `run mode`로 스마트하게 시작합니다. 원하는 모드를 명시적으로 지정하려면 `vitest watch` 또는 `vitest run`을 사용할 수 있습니다.

백그라운드에서 계속 실행하려면 `--standalone` 플래그로 Vitest를 시작하세요. 변경이 발생하기 전까지는 어떤 테스트도 실행하지 않습니다. 소스 코드를 import하는 테스트가 한 번 실행되기 전까지는, 해당 소스 코드가 변경되어도 Vitest는 테스트를 실행하지 않습니다.

## 기본 제공되는 일반적인 웹 관용구

기본 제공: ES Module / TypeScript / JSX 지원 / PostCSS

## Threads

기본적으로 Vitest는 [`node:child_process`](https://nodejs.org/api/child_process.html)를 사용해 [여러 프로세스](https://vitest.dev/guide/parallelism)에서 테스트 파일을 실행하므로 테스트를 동시에 실행할 수 있습니다. 테스트 스위트를 더 빠르게 만들고 싶다면 [`node:worker_threads`](https://nodejs.org/api/worker_threads.html)를 사용해 테스트를 실행하는 `--pool=threads` 활성화를 고려하세요(일부 패키지는 이 설정에서 동작하지 않을 수 있습니다).
단일 thread 또는 process에서 테스트를 실행하려면 [`fileParallelism`](https://vitest.dev/config/#fileParallelism)을 참고하세요.

Vitest는 각 파일의 환경도 격리하므로 한 파일에서의 env 변경이 다른 파일에 영향을 주지 않습니다. CLI에 `--no-isolate`를 전달하면 격리를 비활성화할 수 있습니다(정확성 대신 실행 성능을 선택하는 트레이드오프).

## 테스트 필터링

Vitest는 실행할 테스트를 좁히는 다양한 방법을 제공하여 테스트 속도를 높이고 개발에 집중할 수 있게 해줍니다.

자세한 내용은 [Test Filtering](https://vitest.dev/guide/filtering)을 참고하세요.

## 테스트 동시 실행

연속된 테스트에서 `.concurrent`를 사용하면 병렬로 시작할 수 있습니다.

```ts
import { describe, it } from "vitest";

// The two tests marked with concurrent will be started in parallel
describe("suite", () => {
  it("serial test", async () => {
    /* ... */
  });
  it.concurrent("concurrent test 1", async ({ expect }) => {
    /* ... */
  });
  it.concurrent("concurrent test 2", async ({ expect }) => {
    /* ... */
  });
});
```

suite에 `.concurrent`를 사용하면 그 안의 모든 테스트가 병렬로 시작됩니다.

```ts
import { describe, it } from "vitest";

// All tests within this suite will be started in parallel
describe.concurrent("suite", () => {
  it("concurrent test 1", async ({ expect }) => {
    /* ... */
  });
  it("concurrent test 2", async ({ expect }) => {
    /* ... */
  });
  it.concurrent("concurrent test 3", async ({ expect }) => {
    /* ... */
  });
});
```

동시 suite와 테스트에서도 `.skip`, `.only`, `.todo`를 함께 사용할 수 있습니다. 자세한 내용은 [API Reference](https://vitest.dev/api/#test-concurrent)를 참고하세요.

::: warning
동시 테스트를 실행할 때는 올바른 테스트를 감지할 수 있도록 Snapshot과 Assertion에서 로컬 [Test Context](https://vitest.dev/guide/test-context)의 `expect`를 사용해야 합니다.
:::

## Snapshot

[Jest-compatible](https://jestjs.io/docs/snapshot-testing) snapshot을 지원합니다.

```ts
import { expect, it } from "vitest";

it("renders correctly", () => {
  const result = render();
  expect(result).toMatchSnapshot();
});
```

자세한 내용은 [Snapshot](https://vitest.dev/guide/snapshot)에서 확인하세요.

## Chai 및 Jest `expect` 호환성

Assertion을 위해 [Chai](https://www.chaijs.com/)가 내장되어 있으며, [Jest `expect`](https://jestjs.io/docs/expect) 호환 API를 제공합니다.

matcher를 추가하는 서드파티 라이브러리를 사용한다면 [`test.globals`](https://vitest.dev/config/#globals)를 `true`로 설정했을 때 호환성이 더 좋아집니다.

## Mocking

`vi` 객체에서 `jest` 호환 API를 사용한 mocking을 위해 [Tinyspy](https://github.com/tinylibs/tinyspy)가 내장되어 있습니다.

```ts
import { expect, vi } from "vitest";

const fn = vi.fn();

fn("hello", 1);

expect(vi.isMockFunction(fn)).toBe(true);
expect(fn.mock.calls[0]).toEqual(["hello", 1]);

fn.mockImplementation((arg: string) => arg);

fn("world", 2);

expect(fn.mock.results[1].value).toBe("world");
```

Vitest는 DOM 및 브라우저 API mocking을 위해 [happy-dom](https://github.com/capricorn86/happy-dom) 또는 [jsdom](https://github.com/jsdom/jsdom)을 모두 지원합니다. 이들은 Vitest에 포함되어 있지 않으므로 별도로 설치해야 합니다.

::: code-group

```bash [happy-dom]
$ npm i -D happy-dom
```

```bash [jsdom]
$ npm i -D jsdom
```

:::

그다음 config 파일에서 `environment` 옵션을 변경하세요.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "happy-dom", // or 'jsdom', 'node'
  },
});
```

자세한 내용은 [Mocking](https://vitest.dev/guide/mocking)에서 확인하세요.

## Coverage

Vitest는 [`v8`](https://v8.dev/blog/javascript-code-coverage)을 통한 Native code coverage와 [`istanbul`](https://istanbul.js.org/)을 통한 instrumented code coverage를 지원합니다.

```json [package.json]
{
  "scripts": {
    "test": "vitest",
    "coverage": "vitest run --coverage"
  }
}
```

자세한 내용은 [Coverage](https://vitest.dev/guide/coverage)를 참고하세요.

## In-Source Testing

Vitest는 [Rust의 module tests](https://doc.rust-lang.org/book/ch11-03-test-organization.html#the-tests-module-and-cfgtest)와 유사하게, 구현 코드와 함께 소스 코드 내부에서 테스트를 실행하는 방법도 제공합니다.

이를 통해 테스트가 구현과 동일한 closure를 공유하게 되어 export 없이 private state를 테스트할 수 있습니다. 동시에 개발 시 피드백 루프를 더 가깝게 가져올 수 있습니다.

```ts [src/index.ts]
// the implementation
export function add(...args: number[]): number {
  return args.reduce((a, b) => a + b, 0);
}

// in-source test suites
if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest;
  it("add", () => {
    expect(add()).toBe(0);
    expect(add(1)).toBe(1);
    expect(add(1, 2, 3)).toBe(6);
  });
}
```

자세한 내용은 [In-source testing](https://vitest.dev/guide/in-source)을 참고하세요.

## Benchmarking Experimental {#benchmarking}

[Tinybench](https://github.com/tinylibs/tinybench)를 통해 [`bench`](https://vitest.dev/api/#bench) 함수를 사용해 benchmark 테스트를 실행하고 성능 결과를 비교할 수 있습니다.

```ts [sort.bench.ts]
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

## Type Testing Experimental {#type-testing}

타입 회귀를 잡아내기 위해 [테스트를 작성](https://vitest.dev/guide/testing-types)할 수 있습니다. Vitest는 유사하면서 이해하기 쉬운 API를 제공하기 위해 [`expect-type`](https://github.com/mmkal/expect-type) 패키지를 함께 제공합니다.

```ts [types.test-d.ts]
import { assertType, expectTypeOf, test } from "vitest";
import { mount } from "./mount.js";

test("my types work properly", () => {
  expectTypeOf(mount).toBeFunction();
  expectTypeOf(mount).parameter(0).toExtend<{ name: string }>();

  // @ts-expect-error name is a string
  assertType(mount({ name: 42 }));
});
```

## Sharding

[`--shard`](https://vitest.dev/guide/cli#shard) 및 [`--reporter=blob`](https://vitest.dev/guide/reporters#blob-reporter) 플래그를 사용해 서로 다른 머신에서 테스트를 실행하세요.
모든 테스트 및 coverage 결과는 CI 파이프라인 마지막에서 `--merge-reports` 명령으로 병합할 수 있습니다.

```bash
vitest --shard=1/2 --reporter=blob --coverage
vitest --shard=2/2 --reporter=blob --coverage
vitest --merge-reports --reporter=junit --coverage
```

자세한 내용은 [`Improving Performance | Sharding`](https://vitest.dev/guide/improving-performance#sharding)을 참고하세요.

## Environment Variables

Vitest는 프론트엔드 관련 테스트와의 호환성을 유지하기 위해 `.env` 파일에서 `VITE_` 접두사가 붙은 환경 변수만 자동 로드합니다. 이는 [Vite의 기존 규약](https://vitejs.dev/guide/env-and-mode.html#env-files)을 따릅니다. 그래도 `.env` 파일의 모든 환경 변수를 로드하려면 `vite`에서 import한 `loadEnv` 메서드를 사용할 수 있습니다.

```ts [vitest.config.ts]
import { loadEnv } from "vite";
import { defineConfig } from "vitest/config";

export default defineConfig(({ mode }) => ({
  test: {
    // mode defines what ".env.{mode}" file to choose if exists
    env: loadEnv(mode, process.cwd(), ""),
  },
}));
```

## Unhandled Errors

기본적으로 Vitest는 모든 [unhandled rejections](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event), [uncaught exceptions](https://nodejs.org/api/process.html#event-uncaughtexception)(Node.js에서), 그리고 [error](https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event) 이벤트([browser](https://vitest.dev/guide/browser/)에서)를 포착하고 보고합니다.

직접 포착해서 이 동작을 비활성화할 수 있습니다. Vitest는 해당 callback을 사용자가 처리한다고 가정하고 오류를 보고하지 않습니다.

::: code-group

```ts [setup.node.js]
// in Node.js
process.on("unhandledRejection", () => {
  // your own handler
});

process.on("uncaughtException", () => {
  // your own handler
});
```

```ts [setup.browser.js]
// in the browser
window.addEventListener("error", () => {
  // your own handler
});

window.addEventListener("unhandledrejection", () => {
  // your own handler
});
```

:::

또는 [`dangerouslyIgnoreUnhandledErrors`](https://vitest.dev/config/#dangerouslyignoreunhandlederrors) 옵션으로 보고된 오류를 무시할 수도 있습니다. Vitest는 계속 보고하지만 테스트 결과에는 영향을 주지 않습니다(exit code가 변경되지 않음).

오류가 포착되지 않았는지 테스트해야 한다면, 다음과 같은 테스트를 만들 수 있습니다.

```ts
test("my function throws uncaught error", async ({ onTestFinished }) => {
  const unhandledRejectionListener = vi.fn();
  process.on("unhandledRejection", unhandledRejectionListener);
  onTestFinished(() => {
    process.off("unhandledRejection", unhandledRejectionListener);
  });

  callMyFunctionThatRejectsError();

  await expect.poll(unhandledRejectionListener).toHaveBeenCalled();
});
```
