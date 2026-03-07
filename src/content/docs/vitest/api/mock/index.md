---
title: "Mock"
description: "메서드를 사용하면 함수나 클래스를 mock으로 만들어 실행을 추적할 수 있습니다. 이미 생성된 객체의 프로퍼티를 추적하려면  메서드를 사용할 수 있습니다:"
---

출처 URL: https://vitest.dev/api/mock

# Mock

`vi.fn` 메서드를 사용하면 함수나 클래스를 mock으로 만들어 실행을 추적할 수 있습니다. 이미 생성된 객체의 프로퍼티를 추적하려면 `vi.spyOn` 메서드를 사용할 수 있습니다:

```js
import { vi } from "vitest";

const fn = vi.fn();
fn("hello world");
fn.mock.calls[0] === ["hello world"];

const market = {
  getApples: () => 100,
};

const getApplesSpy = vi.spyOn(market, "getApples");
market.getApples();
getApplesSpy.mock.calls.length === 1;
```

mock 결과를 검증하려면 [`expect`](https://vitest.dev/api/expect)에서 mock assertion(예: [`toHaveBeenCalled`](https://vitest.dev/api/expect#tohavebeencalled))을 사용해야 합니다. 이 API 레퍼런스에서는 mock 동작을 제어할 수 있는 프로퍼티와 메서드를 설명합니다.

::: warning IMPORTANT
Vitest spy는 초기화 시 구현의 [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length) 프로퍼티를 상속하지만, 이후 구현이 변경되면 이를 덮어쓰지는 않습니다:

::: code-group

```ts [vi.fn]
const fn = vi.fn((arg1) => {});
fn.length; // == 1

fn.mockImplementation(() => {});
fn.length; // == 1
```

```ts [vi.spyOn]
const example = {
  fn(arg1, arg2) {
    // ...
  },
};

const fn = vi.spyOn(example, "fn");
fn.length; // == 2

fn.mockImplementation(() => {});
fn.length; // == 2
```

:::

::: tip
아래 타입에서 사용자 정의 함수 구현은 제네릭 `<T>`로 표시됩니다.
:::

## getMockImplementation

```ts
function getMockImplementation(): T | undefined;
```

현재 mock 구현이 있으면 해당 구현을 반환합니다.

mock이 [`vi.fn`](https://vitest.dev/api/vi#vi-fn)으로 생성된 경우, 전달된 메서드를 mock 구현으로 사용합니다.

mock이 [`vi.spyOn`](https://vitest.dev/api/vi#vi-spyon)으로 생성된 경우, 사용자 정의 구현을 제공하지 않았다면 `undefined`를 반환합니다.

## getMockName

```ts
function getMockName(): string;
```

`.mockName(name)` 메서드로 mock에 지정된 이름을 반환할 때 사용합니다. 기본적으로 `vi.fn()` mock은 `'vi.fn()'`을 반환하고, `vi.spyOn`으로 생성된 spy는 원래 이름을 유지합니다.

## mockClear

```ts
function mockClear(): Mock<T>;
```

모든 호출 정보가 지워집니다. 호출 후에는 `.mock`의 모든 프로퍼티가 초기 상태로 돌아갑니다. 이 메서드는 구현을 재설정하지 않습니다. 서로 다른 assertion 사이에서 mock을 정리할 때 유용합니다.

```ts
const person = {
  greet: (name: string) => `Hello ${name}`,
};
const spy = vi.spyOn(person, "greet").mockImplementation(() => "mocked");
expect(person.greet("Alice")).toBe("mocked");
expect(spy.mock.calls).toEqual([["Alice"]]);

// clear call history but keep mock implementation
spy.mockClear();
expect(spy.mock.calls).toEqual([]);
expect(person.greet("Bob")).toBe("mocked");
expect(spy.mock.calls).toEqual([["Bob"]]);
```

각 테스트 전에 이 메서드를 자동 호출하려면 설정에서 [`clearMocks`](https://vitest.dev/config/#clearmocks)를 활성화하세요.

## mockName

```ts
function mockName(name: string): Mock<T>;
```

내부 mock 이름을 설정합니다. assertion 실패 시 어떤 mock인지 식별하는 데 유용합니다.

## mockImplementation

```ts
function mockImplementation(fn: T): Mock<T>;
```

mock 구현으로 사용할 함수를 받습니다. TypeScript는 인자와 반환 타입이 원본 함수와 일치하기를 기대합니다.

```ts
const mockFn = vi.fn().mockImplementation((apples: number) => apples + 1);
// or: vi.fn(apples => apples + 1);

const NelliesBucket = mockFn(0);
const BobsBucket = mockFn(1);

NelliesBucket === 1; // true
BobsBucket === 2; // true

mockFn.mock.calls[0][0] === 0; // true
mockFn.mock.calls[1][0] === 1; // true
```

## mockImplementationOnce

```ts
function mockImplementationOnce(fn: T): Mock<T>;
```

mock 구현으로 사용할 함수를 받습니다. TypeScript는 인자와 반환 타입이 원본 함수와 일치하기를 기대합니다. 이 메서드는 체이닝하여 여러 함수 호출에 대해 서로 다른 결과를 만들 수 있습니다.

```ts
const myMockFn = vi
  .fn()
  .mockImplementationOnce(() => true) // 1st call
  .mockImplementationOnce(() => false); // 2nd call

myMockFn(); // 1st call: true
myMockFn(); // 2nd call: false
```

mock 함수에서 구현이 소진되면, `vi.fn(() => defaultValue)` 또는 `.mockImplementation(() => defaultValue)`가 호출된 경우 거기서 설정한 기본 구현을 실행합니다:

```ts
const myMockFn = vi
  .fn(() => "default")
  .mockImplementationOnce(() => "first call")
  .mockImplementationOnce(() => "second call");

// 'first call', 'second call', 'default', 'default'
console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
```

## withImplementation

```ts
function withImplementation(fn: T, cb: () => void): Mock<T>;
function withImplementation(fn: T, cb: () => Promise<void>): Promise<Mock<T>>;
```

콜백이 실행되는 동안 원래 mock 구현을 일시적으로 덮어씁니다.

```js
const myMockFn = vi.fn(() => "original");

myMockFn.withImplementation(
  () => "temp",
  () => {
    myMockFn(); // 'temp'
  },
);

myMockFn(); // 'original'
```

비동기 콜백과 함께 사용할 수 있습니다. 이후 원래 구현을 사용하려면 이 메서드를 `await`해야 합니다.

```ts
test("async callback", () => {
  const myMockFn = vi.fn(() => "original");

  // We await this call since the callback is async
  await myMockFn.withImplementation(
    () => "temp",
    async () => {
      myMockFn(); // 'temp'
    },
  );

  myMockFn(); // 'original'
});
```

이 메서드는 [`mockImplementationOnce`](#mockimplementationonce)보다 우선 적용됩니다.

## mockRejectedValue

```ts
function mockRejectedValue(value: unknown): Mock<T>;
```

비동기 함수가 호출될 때 reject될 에러를 받습니다.

```ts
const asyncMock = vi.fn().mockRejectedValue(new Error("Async error"));

await asyncMock(); // throws Error<'Async error'>
```

## mockRejectedValueOnce

```ts
function mockRejectedValueOnce(value: unknown): Mock<T>;
```

다음 함수 호출에서 reject될 값을 받습니다. 체이닝하면 이후 각 호출에서 지정한 값이 순차적으로 reject됩니다.

```ts
const asyncMock = vi
  .fn()
  .mockResolvedValueOnce("first call")
  .mockRejectedValueOnce(new Error("Async error"));

await asyncMock(); // 'first call'
await asyncMock(); // throws Error<'Async error'>
```

## mockReset

```ts
function mockReset(): Mock<T>;
```

[`mockClear`](#mockClear)가 수행하는 작업을 하고 mock 구현도 재설정합니다. 또한 모든 "once" 구현도 재설정됩니다.

`vi.fn()`으로 만든 mock을 재설정하면 구현은 `undefined`를 반환하는 빈 함수로 설정됩니다.
`vi.fn(impl)`로 만든 mock을 재설정하면 구현은 `impl`로 되돌아갑니다.

mock을 원래 상태로 되돌리고 싶을 때 유용합니다.

```ts
const person = {
  greet: (name: string) => `Hello ${name}`,
};
const spy = vi.spyOn(person, "greet").mockImplementation(() => "mocked");
expect(person.greet("Alice")).toBe("mocked");
expect(spy.mock.calls).toEqual([["Alice"]]);

// clear call history and reset implementation, but method is still spied
spy.mockReset();
expect(spy.mock.calls).toEqual([]);
expect(person.greet).toBe(spy);
expect(person.greet("Bob")).toBe("Hello Bob");
expect(spy.mock.calls).toEqual([["Bob"]]);
```

각 테스트 전에 이 메서드를 자동 호출하려면 설정에서 [`mockReset`](https://vitest.dev/config/#mockreset)을 활성화하세요.

## mockRestore

```ts
function mockRestore(): Mock<T>;
```

[`mockReset`](#mockreset)이 수행하는 작업을 하고, mock이 [`vi.spyOn`](https://vitest.dev/api/vi#vi-spyon)으로 생성된 경우 spy 대상 객체의 원래 descriptor도 복원합니다.

`vi.fn()` mock에서 `mockRestore`는 [`mockReset`](#mockreset)과 동일합니다.

```ts
const person = {
  greet: (name: string) => `Hello ${name}`,
};
const spy = vi.spyOn(person, "greet").mockImplementation(() => "mocked");
expect(person.greet("Alice")).toBe("mocked");
expect(spy.mock.calls).toEqual([["Alice"]]);

// clear call history and restore spied object method
spy.mockRestore();
expect(spy.mock.calls).toEqual([]);
expect(person.greet).not.toBe(spy);
expect(person.greet("Bob")).toBe("Hello Bob");
expect(spy.mock.calls).toEqual([]);
```

각 테스트 전에 이 메서드를 자동 호출하려면 설정에서 [`restoreMocks`](https://vitest.dev/config/#restoremocks)를 활성화하세요.

## mockResolvedValue

```ts
function mockResolvedValue(value: Awaited<ReturnType<T>>): Mock<T>;
```

비동기 함수가 호출될 때 resolve될 값을 받습니다. TypeScript는 원본 함수의 반환 타입과 일치하는 값만 허용합니다.

```ts
const asyncMock = vi.fn().mockResolvedValue(42);

await asyncMock(); // 42
```

## mockResolvedValueOnce

```ts
function mockResolvedValueOnce(value: Awaited<ReturnType<T>>): Mock<T>;
```

다음 함수 호출에서 resolve될 값을 받습니다. TypeScript는 원본 함수의 반환 타입과 일치하는 값만 허용합니다. 체이닝하면 이후 각 호출에서 지정한 값이 순차적으로 resolve됩니다.

```ts
const asyncMock = vi
  .fn()
  .mockResolvedValue("default")
  .mockResolvedValueOnce("first call")
  .mockResolvedValueOnce("second call");

await asyncMock(); // first call
await asyncMock(); // second call
await asyncMock(); // default
await asyncMock(); // default
```

## mockReturnThis

```ts
function mockReturnThis(): Mock<T>;
```

실제 구현을 호출하지 않고 메서드에서 `this` 컨텍스트를 반환해야 할 때 사용합니다. 이는 다음의 축약형입니다:

```ts
spy.mockImplementation(function () {
  return this;
});
```

## mockReturnValue

```ts
function mockReturnValue(value: ReturnType<T>): Mock<T>;
```

mock 함수가 호출될 때마다 반환될 값을 받습니다. TypeScript는 원본 함수의 반환 타입과 일치하는 값만 허용합니다.

```ts
const mock = vi.fn();
mock.mockReturnValue(42);
mock(); // 42
mock.mockReturnValue(43);
mock(); // 43
```

## mockReturnValueOnce

```ts
function mockReturnValueOnce(value: ReturnType<T>): Mock<T>;
```

mock 함수가 호출될 때마다 반환될 값을 받습니다. TypeScript는 원본 함수의 반환 타입과 일치하는 값만 허용합니다.

mock 함수에서 구현이 소진되면, `vi.fn(() => defaultValue)` 또는 `.mockImplementation(() => defaultValue)`가 호출된 경우 거기서 설정한 기본 구현을 실행합니다:

```ts
const myMockFn = vi
  .fn()
  .mockReturnValue("default")
  .mockReturnValueOnce("first call")
  .mockReturnValueOnce("second call");

// 'first call', 'second call', 'default', 'default'
console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
```

## mock.calls

```ts
const calls: Parameters<T>[];
```

각 호출의 모든 인자를 담은 배열입니다. 배열의 각 항목은 해당 호출의 인자입니다.

```js
const fn = vi.fn();

fn("arg1", "arg2");
fn("arg3");

fn.mock.calls ===
  [
    ["arg1", "arg2"], // first call
    ["arg3"], // second call
  ];
```

:::warning Objects are Stored by Reference
Vitest는 `mock` 상태의 모든 프로퍼티에 객체를 항상 참조로 저장합니다. 즉, 코드에서 프로퍼티가 변경되면 [`.toHaveBeenCalledWith`](https://vitest.dev/api/expect#tohavebeencalledwith) 같은 일부 assertion은 통과하지 않을 수 있습니다:

```ts
const argument = {
  value: 0,
};
const fn = vi.fn();
fn(argument); // { value: 0 }

argument.value = 10;

expect(fn).toHaveBeenCalledWith({ value: 0 }); // [!code --]

// The equality check is done against the original argument,
// but its property was changed between the call and assertion
expect(fn).toHaveBeenCalledWith({ value: 10 }); // [!code ++]
```

이 경우 인자를 직접 복제할 수 있습니다:

```ts{6}
const calledArguments = []
const fn = vi.fn((arg) => {
  calledArguments.push(structuredClone(arg))
})

expect(calledArguments[0]).toEqual({ value: 0 })
```

:::

## mock.lastCall

```ts
const lastCall: Parameters<T> | undefined;
```

마지막 호출의 인자를 담고 있습니다. mock이 호출되지 않았다면 `undefined`를 반환합니다.

## mock.results

```ts
interface MockResultReturn<T> {
  type: "return";
  /**
   * The value that was returned from the function.
   * If the function returned a Promise, then this will be a resolved value.
   */
  value: T;
}

interface MockResultIncomplete {
  type: "incomplete";
  value: undefined;
}

interface MockResultThrow {
  type: "throw";
  /**
   * An error that was thrown during function execution.
   */
  value: any;
}

type MockResult<T> =
  | MockResultReturn<T>
  | MockResultThrow
  | MockResultIncomplete;

const results: MockResult<ReturnType<T>>[];
```

함수에서 `returned`된 모든 값을 담은 배열입니다. 배열의 각 항목은 `type`과 `value` 프로퍼티를 가진 객체입니다. 사용 가능한 type은 다음과 같습니다:

- `'return'` - 함수가 예외 없이 반환됨.
- `'throw'` - 함수가 값을 throw함.
- `'incomplete'` - 함수 실행이 아직 끝나지 않음.

`value` 프로퍼티에는 반환값 또는 throw된 에러가 들어 있습니다. 함수가 `Promise`를 반환한 경우, promise가 reject되더라도 `result`는 항상 `'return'`입니다.

```js
const fn = vi
  .fn()
  .mockReturnValueOnce("result")
  .mockImplementationOnce(() => {
    throw new Error("thrown error");
  });

const result = fn(); // returned 'result'

try {
  fn(); // threw Error
} catch {}

fn.mock.results ===
  [
    // first result
    {
      type: "return",
      value: "result",
    },
    // last result
    {
      type: "throw",
      value: Error,
    },
  ];
```

## mock.settledResults

```ts
interface MockSettledResultIncomplete {
  type: "incomplete";
  value: undefined;
}

interface MockSettledResultFulfilled<T> {
  type: "fulfilled";
  value: T;
}

interface MockSettledResultRejected {
  type: "rejected";
  value: any;
}

export type MockSettledResult<T> =
  | MockSettledResultFulfilled<T>
  | MockSettledResultRejected
  | MockSettledResultIncomplete;

const settledResults: MockSettledResult<Awaited<ReturnType<T>>>[];
```

함수에서 resolve 또는 reject된 모든 값을 담은 배열입니다.

함수가 non-promise 값을 반환한 경우 `value`는 그대로 유지되지만, `type`은 여전히 `fulfilled` 또는 `rejected`로 표시됩니다.

값이 resolve 또는 reject되기 전까지 `settledResult` type은 `incomplete`입니다.

```js
const fn = vi.fn().mockResolvedValueOnce("result");

const result = fn();

fn.mock.settledResults ===
  [
    {
      type: "incomplete",
      value: undefined,
    },
  ];

await result;

fn.mock.settledResults ===
  [
    {
      type: "fulfilled",
      value: "result",
    },
  ];
```

## mock.invocationCallOrder

```ts
const invocationCallOrder: number[];
```

이 프로퍼티는 mock 함수의 실행 순서를 반환합니다. 모든 정의된 mock 간에 공유되는 숫자 배열입니다.

```js
const fn1 = vi.fn();
const fn2 = vi.fn();

fn1();
fn2();
fn1();

fn1.mock.invocationCallOrder === [1, 3];
fn2.mock.invocationCallOrder === [2];
```

## mock.contexts

```ts
const contexts: ThisParameterType<T>[];
```

이 프로퍼티는 mock 함수의 각 호출에서 사용된 `this` 값의 배열입니다.

```js
const fn = vi.fn();
const context = {};

fn.apply(context);
fn.call(context);

fn.mock.contexts[0] === context;
fn.mock.contexts[1] === context;
```

## mock.instances

```ts
const instances: ReturnType<T>[];
```

이 프로퍼티는 mock이 `new` 키워드로 호출될 때 생성된 모든 인스턴스를 담은 배열입니다. 이는 반환값이 아니라 함수의 실제 컨텍스트(`this`)라는 점에 유의하세요.

::: warning
mock이 `new MyClass()`로 인스턴스화되면 `mock.instances`는 값 하나를 가진 배열이 됩니다:

```js
const MyClass = vi.fn();
const a = new MyClass();

MyClass.mock.instances[0] === a;
```

생성자에서 값을 반환하면 그 값은 `instances` 배열이 아니라 `results` 안에 들어갑니다:

```js
const Spy = vi.fn(() => ({ method: vi.fn() }));
const a = new Spy();

Spy.mock.instances[0] !== a;
Spy.mock.results[0] === a;
```

:::
