---
title: "expect"
description: "아래 타입 시그니처에서는 다음 타입을 사용합니다."
---

출처 URL: https://vitest.dev/api/expect

# expect

아래 타입 시그니처에서는 다음 타입을 사용합니다.

```ts
type Awaitable<T> = T | PromiseLike<T>;
```

`expect`는 assertion을 생성하는 데 사용됩니다. 이 맥락에서 `assertions`는 어떤 명제를 검증하기 위해 호출할 수 있는 함수입니다. Vitest는 기본적으로 `chai` assertion을 제공하며, `chai` 위에 구축된 `Jest` 호환 assertion도 제공합니다. `Jest`와 달리 Vitest는 두 번째 인수로 메시지를 지원합니다. assertion이 실패하면 오류 메시지는 해당 값과 동일해집니다.

```ts
export interface ExpectStatic
  extends Chai.ExpectStatic, AsymmetricMatchersContaining {
  <T>(actual: T, message?: string): Assertion<T>;
  extend: (expects: MatchersObject) => void;
  anything: () => any;
  any: (constructor: unknown) => any;
  getState: () => MatcherState;
  setState: (state: Partial<MatcherState>) => void;
  not: AsymmetricMatchersContaining;
}
```

예를 들어, 이 코드는 `input` 값이 `2`와 같은지 검증합니다. 같지 않으면 assertion이 오류를 던지고 테스트는 실패합니다.

```ts twoslash
import { expect } from "vitest";

const input = Math.sqrt(4);

expect(input).to.equal(2); // chai API
expect(input).toBe(2); // jest API
```

기술적으로 이 예제는 [`test`](https://vitest.dev/api/#test) 함수를 사용하지 않으므로, 콘솔에는 Vitest 출력 대신 Node.js 오류가 표시됩니다. `test`에 대해 더 알아보려면 [Test API Reference](https://vitest.dev/api/)를 읽어보세요.

또한 `expect`는 나중에 설명할 matcher 함수 등에 접근하기 위해 정적으로도 사용할 수 있습니다.

::: warning
표현식에 타입 오류가 없다면 `expect`는 타입 테스트에 영향을 주지 않습니다. Vitest를 [type checker](https://vitest.dev/guide/testing-types)로 사용하려면 [`expectTypeOf`](https://vitest.dev/api/expect-typeof) 또는 [`assertType`](https://vitest.dev/api/assert-type)를 사용하세요.
:::

## assert

- **Type:** `Chai.AssertStatic`

편의를 위해 Vitest는 chai의 [`assert` API](https://www.chaijs.com/api/assert/)를 `expect.assert`로 다시 내보냅니다. 지원되는 메서드는 [Assert API page](https://vitest.dev/api/assert)에서 확인할 수 있습니다.

이는 특히 타입을 좁혀야 할 때 유용합니다. `expect.to*` 메서드는 이를 지원하지 않기 때문입니다.

```ts
interface Cat {
  __type: "Cat";
  mew(): void;
}
interface Dog {
  __type: "Dog";
  bark(): void;
}
type Animal = Cat | Dog;

const animal: Animal = { __type: "Dog", bark: () => {} };

expect.assert(animal.__type === "Dog");
// does not show a type error!
expect(animal.bark()).toBeUndefined();
```

::: tip
`expect.assert`는 다른 타입 좁히기 메서드(`assert.isDefined`, `assert.exists` 등)도 지원합니다.
:::

## soft

- **Type:** `ExpectStatic & (actual: any) => Assertions`

`expect.soft`는 `expect`와 유사하게 동작하지만, assertion 실패 시 테스트 실행을 즉시 중단하지 않고 계속 실행하며 해당 실패를 테스트 실패로 표시합니다. 테스트 중 발생한 모든 오류는 테스트가 완료될 때까지 표시됩니다.

```ts
import { expect, test } from "vitest";

test("expect.soft test", () => {
  expect.soft(1 + 1).toBe(3); // mark the test as fail and continue
  expect.soft(1 + 2).toBe(4); // mark the test as fail and continue
});
// reporter will report both errors at the end of the run
```

`expect`와 함께 사용할 수도 있습니다. `expect` assertion이 실패하면 테스트는 종료되고 모든 오류가 표시됩니다.

```ts
import { expect, test } from "vitest";

test("expect.soft test", () => {
  expect.soft(1 + 1).toBe(3); // mark the test as fail and continue
  expect(1 + 2).toBe(4); // failed and terminate the test, all previous errors will be output
  expect.soft(1 + 3).toBe(5); // do not run
});
```

::: warning
`expect.soft`는 [`test`](https://vitest.dev/api/#test) 함수 내부에서만 사용할 수 있습니다.
:::

## poll

```ts
interface ExpectPoll extends ExpectStatic {
  (
    actual: () => T,
    options?: { interval?: number; timeout?: number; message?: string },
  ): Promise<Assertions<T>>;
}
```

`expect.poll`은 *assertion*이 성공할 때까지 다시 실행합니다. `interval` 및 `timeout` 옵션을 설정해 Vitest가 `expect.poll` 콜백을 몇 번 재실행할지 구성할 수 있습니다.

`expect.poll` 콜백 내부에서 오류가 발생하면, timeout이 만료될 때까지 Vitest가 다시 재시도합니다.

```ts
import { expect, test } from "vitest";

test("element exists", async () => {
  asyncInjectElement();

  await expect.poll(() => document.querySelector(".element")).toBeTruthy();
});
```

::: warning
`expect.poll`은 모든 assertion을 비동기로 만들기 때문에 `await`해야 합니다. Vitest 3부터는 `await`를 빼먹으면 테스트가 실패하며 경고가 표시됩니다.

`expect.poll`은 몇 가지 matcher와 함께 동작하지 않습니다.

- Snapshot matcher는 항상 성공하기 때문에 지원되지 않습니다. 조건이 flaky하다면, 먼저 이를 해결하기 위해 [`vi.waitFor`](https://vitest.dev/api/vi#vi-waitfor)를 사용하는 것을 고려하세요.

```ts
import { expect, vi } from "vitest";

const flakyValue = await vi.waitFor(() => getFlakyValue());
expect(flakyValue).toMatchSnapshot();
```

- `.resolves`와 `.rejects`는 지원되지 않습니다. `expect.poll`은 조건이 비동기이면 이미 이를 `await`합니다.
- `toThrow` 및 그 별칭은 지원되지 않습니다. `expect.poll` 조건은 matcher가 값을 받기 전에 항상 resolve되기 때문입니다.
  :::

## not

`not`을 사용하면 assertion이 부정됩니다. 예를 들어, 이 코드는 `input` 값이 `2`와 같지 않음을 검증합니다. 같다면 assertion이 오류를 던지고 테스트는 실패합니다.

```ts
import { expect, test } from "vitest";

const input = Math.sqrt(16);

expect(input).not.to.equal(2); // chai API
expect(input).not.toBe(2); // jest API
```

## toBe

- **Type:** `(value: any) => Awaitable<void>`

`toBe`는 원시값이 같은지, 또는 객체가 동일한 참조를 공유하는지 검증할 때 사용할 수 있습니다. 이는 `expect(Object.is(3, 3)).toBe(true)`를 호출하는 것과 같습니다. 객체가 동일하지 않지만 구조가 같은지 확인하려면 [`toEqual`](#toequal)을 사용할 수 있습니다.

예를 들어, 아래 코드는 상인이 사과 13개를 가지고 있는지 확인합니다.

```ts
import { expect, test } from "vitest";

const stock = {
  type: "apples",
  count: 13,
};

test("stock has 13 apples", () => {
  expect(stock.type).toBe("apples");
  expect(stock.count).toBe(13);
});

test("stocks are the same", () => {
  const refStock = stock; // same reference

  expect(stock).toBe(refStock);
});
```

부동소수점 수에는 `toBe`를 사용하지 않는 것이 좋습니다. JavaScript가 이를 반올림하기 때문에 `0.1 + 0.2`는 엄밀히 `0.3`이 아닙니다. 부동소수점을 신뢰성 있게 검증하려면 [`toBeCloseTo`](#tobecloseto) assertion을 사용하세요.

## toBeCloseTo

- **Type:** `(value: number, numDigits?: number) => Awaitable<void>`

부동소수점 수를 비교하려면 `toBeCloseTo`를 사용하세요. 선택적 `numDigits` 인수는 소수점 *이후*에 확인할 자릿수를 제한합니다. `numDigits`의 기본값은 2입니다. 예:

```ts
import { expect, test } from "vitest";

test.fails("decimals are not equal in javascript", () => {
  expect(0.2 + 0.1).toBe(0.3); // 0.2 + 0.1 is 0.30000000000000004
});

test("decimals are rounded to 5 after the point", () => {
  // 0.2 + 0.1 is 0.30000 | "000000000004" removed
  expect(0.2 + 0.1).toBeCloseTo(0.3, 5);
  // nothing from 0.30000000000000004 is removed
  expect(0.2 + 0.1).not.toBeCloseTo(0.3, 50);
});
```

## toBeDefined

- **Type:** `() => Awaitable<void>`

`toBeDefined`는 값이 `undefined`와 같지 않음을 검증합니다. 함수가 무언가를 _반환했는지_ 확인할 때 유용합니다.

```ts
import { expect, test } from "vitest";

function getApples() {
  return 3;
}

test("function returned something", () => {
  expect(getApples()).toBeDefined();
});
```

## toBeUndefined

- **Type:** `() => Awaitable<void>`

`toBeDefined`의 반대로, `toBeUndefined`는 값이 `undefined`와 같음을 검증합니다. 함수가 아무것도 _반환하지 않았는지_ 확인할 때 유용합니다.

```ts
import { expect, test } from "vitest";

function getApplesFromStock(stock: string) {
  if (stock === "Bill") {
    return 13;
  }
}

test("mary doesn't have a stock", () => {
  expect(getApplesFromStock("Mary")).toBeUndefined();
});
```

## toBeTruthy

- **Type:** `() => Awaitable<void>`

`toBeTruthy`는 값을 boolean으로 변환했을 때 true인지 검증합니다. 값 자체는 중요하지 않고 `true`로 변환 가능한지만 알고 싶을 때 유용합니다.

예를 들어, 아래 코드에서는 `stocks.getInfo`의 반환값이 무엇인지는 중요하지 않습니다. 복잡한 객체일 수도, 문자열일 수도, 그 외 어떤 값이어도 코드가 동작할 수 있습니다.

```ts
import { Stocks } from "./stocks.js";

const stocks = new Stocks();
stocks.sync("Bill");
if (stocks.getInfo("Bill")) {
  stocks.sell("apples", "Bill");
}
```

따라서 `stocks.getInfo`가 truthy인지 테스트하려면 다음과 같이 작성할 수 있습니다.

```ts
import { expect, test } from "vitest";
import { Stocks } from "./stocks.js";

const stocks = new Stocks();

test("if we know Bill stock, sell apples to him", () => {
  stocks.sync("Bill");
  expect(stocks.getInfo("Bill")).toBeTruthy();
});
```

JavaScript에서 `false`, `null`, `undefined`, `NaN`, `0`, `-0`, `0n`, `""`, `document.all`을 제외한 모든 값은 truthy입니다.

## toBeFalsy

- **Type:** `() => Awaitable<void>`

`toBeFalsy`는 값을 boolean으로 변환했을 때 false인지 검증합니다. 값 자체는 중요하지 않고 `false`로 변환 가능한지만 알고 싶을 때 유용합니다.

예를 들어, 아래 코드에서는 `stocks.stockFailed`의 반환값이 무엇인지는 중요하지 않습니다. 어떤 falsy 값을 반환해도 코드는 여전히 동작할 수 있습니다.

```ts
import { Stocks } from "./stocks.js";

const stocks = new Stocks();
stocks.sync("Bill");
if (!stocks.stockFailed("Bill")) {
  stocks.sell("apples", "Bill");
}
```

따라서 `stocks.stockFailed`가 falsy인지 테스트하려면 다음과 같이 작성할 수 있습니다.

```ts
import { expect, test } from "vitest";
import { Stocks } from "./stocks.js";

const stocks = new Stocks();

test("if Bill stock hasn't failed, sell apples to him", () => {
  stocks.syncStocks("Bill");
  expect(stocks.stockFailed("Bill")).toBeFalsy();
});
```

JavaScript에서 `false`, `null`, `undefined`, `NaN`, `0`, `-0`, `0n`, `""`, `document.all`을 제외한 모든 값은 truthy입니다.

## toBeNull

- **Type:** `() => Awaitable<void>`

`toBeNull`은 값이 `null`인지 간단히 검증합니다. `.toBe(null)`의 별칭입니다.

```ts
import { expect, test } from "vitest";

function apples() {
  return null;
}

test("we don't have apples", () => {
  expect(apples()).toBeNull();
});
```

## toBeNullable

- **Type:** `() => Awaitable<void>`

`toBeNullable`은 값이 nullable(`null` 또는 `undefined`)인지 간단히 검증합니다.

```ts
import { expect, test } from "vitest";

function apples() {
  return null;
}

function bananas() {
  return undefined;
}

test("we don't have apples", () => {
  expect(apples()).toBeNullable();
});

test("we don't have bananas", () => {
  expect(bananas()).toBeNullable();
});
```

## toBeNaN

- **Type:** `() => Awaitable<void>`

`toBeNaN`은 값이 `NaN`인지 간단히 검증합니다. `.toBe(NaN)`의 별칭입니다.

```ts
import { expect, test } from "vitest";

let i = 0;

function getApplesCount() {
  i++;
  return i > 1 ? Number.NaN : i;
}

test("getApplesCount has some unusual side effects...", () => {
  expect(getApplesCount()).not.toBeNaN();
  expect(getApplesCount()).toBeNaN();
});
```

## toBeOneOf

- **Type:** `(sample: Array<any> | Set<any>) => any`

`toBeOneOf`는 값이 제공된 배열 또는 집합의 값 중 하나와 일치하는지 검증합니다.

::: warning EXPERIMENTAL
`Set` 제공은 실험적 기능이며 향후 릴리스에서 변경될 수 있습니다.
:::

```ts
import { expect, test } from "vitest";

test("fruit is one of the allowed values", () => {
  expect(fruit).toBeOneOf(["apple", "banana", "orange"]);
});
```

이 비대칭 matcher는 `null` 또는 `undefined`가 될 수 있는 선택적 속성을 테스트할 때 특히 유용합니다.

```ts
test("optional properties can be null or undefined", () => {
  const user = {
    firstName: "John",
    middleName: undefined,
    lastName: "Doe",
  };

  expect(user).toEqual({
    firstName: expect.any(String),
    middleName: expect.toBeOneOf([expect.any(String), undefined]),
    lastName: expect.any(String),
  });
});
```

:::tip
`expect.not`을 이 matcher와 함께 사용하면 값이 제공된 어떤 옵션과도 일치하지 않음을 보장할 수 있습니다.
:::

## toBeTypeOf

- **Type:** `(c: 'bigint' | 'boolean' | 'function' | 'number' | 'object' | 'string' | 'symbol' | 'undefined') => Awaitable<void>`

`toBeTypeOf`는 실제 값의 타입이 전달된 타입인지 검증합니다.

```ts
import { expect, test } from "vitest";

const actual = "stock";

test("stock is type of string", () => {
  expect(actual).toBeTypeOf("string");
});
```

:::warning
`toBeTypeOf`는 내부적으로 네이티브 `typeof` 연산자를 사용하며, 그 특이점도 그대로 따릅니다. 대표적으로 `null` 값의 타입은 `object`입니다.

```ts
test("toBeTypeOf cannot check for null or array", () => {
  expect(null).toBeTypeOf("object");
  expect([]).toBeTypeOf("object");
});
```

:::

## toBeInstanceOf

- **Type:** `(c: any) => Awaitable<void>`

`toBeInstanceOf`는 실제 값이 전달된 클래스의 인스턴스인지 검증합니다.

```ts
import { expect, test } from "vitest";
import { Stocks } from "./stocks.js";

const stocks = new Stocks();

test("stocks are instance of Stocks", () => {
  expect(stocks).toBeInstanceOf(Stocks);
});
```

## toBeGreaterThan

- **Type:** `(n: number | bigint) => Awaitable<void>`

`toBeGreaterThan`은 실제 값이 전달된 값보다 큰지 검증합니다. 같은 값이면 테스트가 실패합니다.

```ts
import { expect, test } from "vitest";
import { getApples } from "./stocks.js";

test("have more then 10 apples", () => {
  expect(getApples()).toBeGreaterThan(10);
});
```

## toBeGreaterThanOrEqual

- **Type:** `(n: number | bigint) => Awaitable<void>`

`toBeGreaterThanOrEqual`은 실제 값이 전달된 값보다 크거나 같은지 검증합니다.

```ts
import { expect, test } from "vitest";
import { getApples } from "./stocks.js";

test("have 11 apples or more", () => {
  expect(getApples()).toBeGreaterThanOrEqual(11);
});
```

## toBeLessThan

- **Type:** `(n: number | bigint) => Awaitable<void>`

`toBeLessThan`은 실제 값이 전달된 값보다 작은지 검증합니다. 같은 값이면 테스트가 실패합니다.

```ts
import { expect, test } from "vitest";
import { getApples } from "./stocks.js";

test("have less then 20 apples", () => {
  expect(getApples()).toBeLessThan(20);
});
```

## toBeLessThanOrEqual

- **Type:** `(n: number | bigint) => Awaitable<void>`

`toBeLessThanOrEqual`은 실제 값이 전달된 값보다 작거나 같은지 검증합니다.

```ts
import { expect, test } from "vitest";
import { getApples } from "./stocks.js";

test("have 11 apples or less", () => {
  expect(getApples()).toBeLessThanOrEqual(11);
});
```

## toEqual

- **Type:** `(received: any) => Awaitable<void>`

`toEqual`은 실제 값이 전달된 값과 같은지, 또는 객체인 경우 같은 구조인지(재귀적으로 비교) 검증합니다. `toEqual`과 [`toBe`](#tobe)의 차이는 다음 예제에서 확인할 수 있습니다.

```ts
import { expect, test } from "vitest";

const stockBill = {
  type: "apples",
  count: 13,
};

const stockMary = {
  type: "apples",
  count: 13,
};

test("stocks have the same properties", () => {
  expect(stockBill).toEqual(stockMary);
});

test("stocks are not the same", () => {
  expect(stockBill).not.toBe(stockMary);
});
```

:::warning
`Error` 객체의 경우 `name`, `message`, `cause`, `AggregateError.errors` 같은 non-enumerable 속성도 비교합니다. `Error.cause` 비교는 비대칭으로 수행됩니다.

```ts
// success
expect(new Error("hi", { cause: "x" })).toEqual(new Error("hi"));

// fail
expect(new Error("hi")).toEqual(new Error("hi", { cause: "x" }));
```

무언가가 throw되었는지 테스트하려면 [`toThrowError`](#tothrowerror) assertion을 사용하세요.
:::

## toStrictEqual

- **Type:** `(received: any) => Awaitable<void>`

`toStrictEqual`은 실제 값이 전달된 값과 같은지, 또는 객체인 경우 같은 구조인지(재귀적으로 비교) 검증하며, 타입도 동일해야 합니다.

[`.toEqual`](#toequal)과의 차이점:

- `undefined` 속성을 가진 키를 검사합니다. 예: `.toStrictEqual` 사용 시 `{a: undefined, b: 2}`는 `{b: 2}`와 일치하지 않습니다.
- 배열의 희소성(sparseness)을 검사합니다. 예: `.toStrictEqual` 사용 시 `[, 1]`은 `[undefined, 1]`과 일치하지 않습니다.
- 객체 타입이 동일한지 검사합니다. 예: 필드 `a`, `b`를 가진 클래스 인스턴스는 필드 `a`, `b`를 가진 리터럴 객체와 같지 않습니다.

```ts
import { expect, test } from "vitest";

class Stock {
  constructor(type) {
    this.type = type;
  }
}

test("structurally the same, but semantically different", () => {
  expect(new Stock("apples")).toEqual({ type: "apples" });
  expect(new Stock("apples")).not.toStrictEqual({ type: "apples" });
});
```

## toContain

- **Type:** `(received: string) => Awaitable<void>`

`toContain`은 실제 값이 배열에 포함되어 있는지 검증합니다. 또한 어떤 문자열이 다른 문자열의 부분 문자열인지도 확인할 수 있습니다. 브라우저 유사 환경에서 테스트를 실행 중이라면, 이 assertion은 클래스가 `classList`에 포함되어 있는지, 혹은 어떤 요소가 다른 요소 내부에 있는지도 확인할 수 있습니다.

```ts
import { expect, test } from "vitest";
import { getAllFruits } from "./stocks.js";

test("the fruit list contains orange", () => {
  expect(getAllFruits()).toContain("orange");
});

test("pineapple contains apple", () => {
  expect("pineapple").toContain("apple");
});

test("the element contains a class and is contained", () => {
  const element = document.querySelector("#el");
  // element has a class
  expect(element.classList).toContain("flex");
  // element is inside another one
  expect(document.querySelector("#wrapper")).toContain(element);
});
```

## toContainEqual

- **Type:** `(received: any) => Awaitable<void>`

`toContainEqual`은 특정 구조와 값을 가진 항목이 배열에 포함되어 있는지 검증합니다.
각 요소 내부에서 [`toEqual`](#toequal)처럼 동작합니다.

```ts
import { expect, test } from "vitest";
import { getFruitStock } from "./stocks.js";

test("apple available", () => {
  expect(getFruitStock()).toContainEqual({ fruit: "apple", count: 5 });
});
```

## toHaveLength

- **Type:** `(received: number) => Awaitable<void>`

`toHaveLength`는 객체에 `.length` 속성이 있고, 그 값이 특정 숫자로 설정되어 있는지 검증합니다.

```ts
import { expect, test } from "vitest";

test("toHaveLength", () => {
  expect("abc").toHaveLength(3);
  expect([1, 2, 3]).toHaveLength(3);

  expect("").not.toHaveLength(3); // doesn't have .length of 3
  expect({ length: 3 }).toHaveLength(3);
});
```

## toHaveProperty

- **Type:** `(key: any, received?: any) => Awaitable<void>`

`toHaveProperty`는 제공된 참조 `key` 위치의 속성이 객체에 존재하는지 검증합니다.

`toEqual` matcher처럼 받은 속성 값을 비교하기 위해, deep equality라고도 하는 선택적 값 인수도 제공할 수 있습니다.

```ts
import { expect, test } from "vitest";

const invoice = {
  isActive: true,
  "P.O": "12345",
  customer: {
    first_name: "John",
    last_name: "Doe",
    location: "China",
  },
  total_amount: 5000,
  items: [
    {
      type: "apples",
      quantity: 10,
    },
    {
      type: "oranges",
      quantity: 5,
    },
  ],
};

test("John Doe Invoice", () => {
  expect(invoice).toHaveProperty("isActive"); // assert that the key exists
  expect(invoice).toHaveProperty("total_amount", 5000); // assert that the key exists and the value is equal

  expect(invoice).not.toHaveProperty("account"); // assert that this key does not exist

  // Deep referencing using dot notation
  expect(invoice).toHaveProperty("customer.first_name");
  expect(invoice).toHaveProperty("customer.last_name", "Doe");
  expect(invoice).not.toHaveProperty("customer.location", "India");

  // Deep referencing using an array containing the key
  expect(invoice).toHaveProperty("items[0].type", "apples");
  expect(invoice).toHaveProperty("items.0.type", "apples"); // dot notation also works

  // Deep referencing using an array containing the keyPath
  expect(invoice).toHaveProperty(["items", 0, "type"], "apples");
  expect(invoice).toHaveProperty(["items", "0", "type"], "apples"); // string notation also works

  // Wrap your key in an array to avoid the key from being parsed as a deep reference
  expect(invoice).toHaveProperty(["P.O"], "12345");

  // Deep equality of object property
  expect(invoice).toHaveProperty("items[0]", { type: "apples", quantity: 10 });
});
```

## toMatch

- **Type:** `(received: string | regexp) => Awaitable<void>`

`toMatch`는 문자열이 정규식 또는 문자열과 일치하는지 검증합니다.

```ts
import { expect, test } from "vitest";

test("top fruits", () => {
  expect("top fruits include apple, orange and grape").toMatch(/apple/);
  expect("applefruits").toMatch("fruit"); // toMatch also accepts a string
});
```

## toMatchObject

- **Type:** `(received: object | array) => Awaitable<void>`

`toMatchObject`는 객체가 다른 객체 속성의 부분집합과 일치하는지 검증합니다.

객체 배열도 전달할 수 있습니다. 이는 받은 배열에 추가 요소를 허용하는 `arrayContaining`과 달리, 두 배열이 요소 개수와 순서까지 일치하는지 확인하려는 경우에 유용합니다.

```ts
import { expect, test } from "vitest";

const johnInvoice = {
  isActive: true,
  customer: {
    first_name: "John",
    last_name: "Doe",
    location: "China",
  },
  total_amount: 5000,
  items: [
    {
      type: "apples",
      quantity: 10,
    },
    {
      type: "oranges",
      quantity: 5,
    },
  ],
};

const johnDetails = {
  customer: {
    first_name: "John",
    last_name: "Doe",
    location: "China",
  },
};

test("invoice has john personal details", () => {
  expect(johnInvoice).toMatchObject(johnDetails);
});

test("the number of elements must match exactly", () => {
  // Assert that an array of object matches
  expect([{ foo: "bar" }, { baz: 1 }]).toMatchObject([
    { foo: "bar" },
    { baz: 1 },
  ]);
});
```

## toThrowError

- **Type:** `(received: any) => Awaitable<void>`

- **Alias:** `toThrow`

`toThrowError`는 함수를 호출했을 때 오류를 던지는지 검증합니다.

특정 오류가 throw되는지 테스트하려면 선택적 인수를 제공할 수 있습니다:

- `RegExp`: 에러 메시지가 패턴과 일치함
- `string`: 에러 메시지에 해당 부분 문자열이 포함됨
- `Error`, `AsymmetricMatcher`: `toEqual(received)`와 유사하게 전달된 객체와 비교함

:::tip
코드를 반드시 함수로 감싸야 합니다. 그렇지 않으면 에러가 포착되지 않아 테스트가 실패합니다.

이는 async 호출에는 적용되지 않습니다. [rejects](#rejects)가 promise를 올바르게 언래핑하기 때문입니다:

```ts
test("expect rejects toThrow", async ({ expect }) => {
  const promise = Promise.reject(new Error("Test"));
  await expect(promise).rejects.toThrowError();
});
```

:::

예를 들어 `getFruitStock('pineapples')`가 throw 하는지 테스트하려면 다음과 같이 작성할 수 있습니다:

```ts
import { expect, test } from "vitest";

function getFruitStock(type: string) {
  if (type === "pineapples") {
    throw new Error("Pineapples are not in stock");
  }

  // Do some other stuff
}

test("throws on pineapples", () => {
  // Test that the error message says "stock" somewhere: these are equivalent
  expect(() => getFruitStock("pineapples")).toThrowError(/stock/);
  expect(() => getFruitStock("pineapples")).toThrowError("stock");

  // Test the exact error message
  expect(() => getFruitStock("pineapples")).toThrowError(
    /^Pineapples are not in stock$/,
  );

  expect(() => getFruitStock("pineapples")).toThrowError(
    new Error("Pineapples are not in stock"),
  );
  expect(() => getFruitStock("pineapples")).toThrowError(
    expect.objectContaining({
      message: "Pineapples are not in stock",
    }),
  );
});
```

:::tip
async 함수를 테스트할 때는 [rejects](#rejects)와 함께 사용하세요.

```js
function getAsyncFruitStock() {
  return Promise.reject(new Error("empty"));
}

test("throws on pineapples", async () => {
  await expect(() => getAsyncFruitStock()).rejects.toThrowError("empty");
});
```

:::

## toMatchSnapshot

- **Type:** `<T>(shape?: Partial<T> | string, hint?: string) => void`

값이 최신 스냅샷과 일치하는지 확인합니다.

선택적으로 `hint` 문자열 인수를 제공할 수 있으며, 이 값은 테스트 이름 뒤에 추가됩니다. Vitest는 스냅샷 이름 끝에 항상 숫자를 붙이지만, 하나의 it 또는 test 블록에 여러 스냅샷이 있을 때는 숫자보다 짧고 설명적인 힌트가 더 유용할 수 있습니다. Vitest는 해당 `.snap` 파일에서 스냅샷을 이름순으로 정렬합니다.

:::tip
스냅샷 불일치로 테스트가 실패했을 때, 그 불일치가 의도된 것이라면 `u` 키를 눌러 한 번 스냅샷을 업데이트할 수 있습니다. 또는 `-u`나 `--update` CLI 옵션을 전달해 Vitest가 항상 테스트를 업데이트하도록 할 수 있습니다.
:::

```ts
import { expect, test } from "vitest";

test("matches snapshot", () => {
  const data = { foo: new Set(["bar", "snapshot"]) };
  expect(data).toMatchSnapshot();
});
```

객체의 형태만 테스트하고 100% 호환될 필요가 없다면, 객체 shape를 함께 제공할 수도 있습니다:

```ts
import { expect, test } from "vitest";

test("matches snapshot", () => {
  const data = { foo: new Set(["bar", "snapshot"]) };
  expect(data).toMatchSnapshot({ foo: expect.any(Set) });
});
```

## toMatchInlineSnapshot

- **Type:** `<T>(shape?: Partial<T> | string, snapshot?: string, hint?: string) => void`

값이 최신 스냅샷과 일치하는지 확인합니다.

Vitest는 테스트 파일에서 matcher의 inlineSnapshot 문자열 인수를 추가하고 업데이트합니다(외부 `.snap` 파일 대신).

```ts
import { expect, test } from "vitest";

test("matches inline snapshot", () => {
  const data = { foo: new Set(["bar", "snapshot"]) };
  // Vitest will update following content when updating the snapshot
  expect(data).toMatchInlineSnapshot(`
    {
      "foo": Set {
        "bar",
        "snapshot",
      },
    }
  `);
});
```

객체의 형태만 테스트하고 100% 호환될 필요가 없다면, 객체 shape를 함께 제공할 수도 있습니다:

```ts
import { expect, test } from "vitest";

test("matches snapshot", () => {
  const data = { foo: new Set(["bar", "snapshot"]) };
  expect(data).toMatchInlineSnapshot(
    { foo: expect.any(Set) },
    `
    {
      "foo": Any<Set>,
    }
  `,
  );
});
```

## toMatchFileSnapshot {#tomatchfilesnapshot}

- **Type:** `<T>(filepath: string, hint?: string) => Promise<void>`

명시적으로 지정한 파일의 내용으로 스냅샷을 비교하거나 업데이트합니다(`.snap` 파일 대신).

```ts
import { expect, it } from "vitest";

it("render basic", async () => {
  const result = renderHTML(h("div", { class: "foo" }));
  await expect(result).toMatchFileSnapshot("./test/basic.output.html");
});
```

파일 시스템 작업은 async이므로 `toMatchFileSnapshot()`과 함께 `await`를 사용해야 합니다. `await`를 사용하지 않으면 Vitest는 이를 `expect.soft`처럼 처리하므로, 스냅샷이 불일치하더라도 해당 문장 이후 코드는 계속 실행됩니다. 테스트가 끝난 뒤 Vitest가 스냅샷을 확인하고, 불일치가 있으면 실패 처리합니다.

## toThrowErrorMatchingSnapshot

- **Type:** `(hint?: string) => void`

[`toMatchSnapshot`](#tomatchsnapshot)과 동일하지만, [`toThrowError`](#tothrowerror)와 같은 값을 기대합니다.

## toThrowErrorMatchingInlineSnapshot

- **Type:** `(snapshot?: string, hint?: string) => void`

[`toMatchInlineSnapshot`](#tomatchinlinesnapshot)과 동일하지만, [`toThrowError`](#tothrowerror)와 같은 값을 기대합니다.

## toHaveBeenCalled

- **Type:** `() => Awaitable<void>`

함수가 호출되었는지 테스트할 때 유용한 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("spy function", () => {
  const buySpy = vi.spyOn(market, "buy");

  expect(buySpy).not.toHaveBeenCalled();

  market.buy("apples", 10);

  expect(buySpy).toHaveBeenCalled();
});
```

## toHaveBeenCalledTimes

- **Type**: `(amount: number) => Awaitable<void>`

함수가 특정 횟수만큼 호출되었는지 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("spy function called two times", () => {
  const buySpy = vi.spyOn(market, "buy");

  market.buy("apples", 10);
  market.buy("apples", 20);

  expect(buySpy).toHaveBeenCalledTimes(2);
});
```

## toHaveBeenCalledWith

- **Type**: `(...args: any[]) => Awaitable<void>`

함수가 특정 파라미터로 최소 한 번 호출되었는지 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("spy function", () => {
  const buySpy = vi.spyOn(market, "buy");

  market.buy("apples", 10);
  market.buy("apples", 20);

  expect(buySpy).toHaveBeenCalledWith("apples", 10);
  expect(buySpy).toHaveBeenCalledWith("apples", 20);
});
```

## toHaveBeenCalledBefore 3.0.0 {#tohavebeencalledbefore}

- **Type**: `(mock: MockInstance, failIfNoFirstInvocation?: boolean) => Awaitable<void>`

한 `Mock`이 다른 `Mock`보다 먼저 호출되었는지 확인하는 assertion입니다.

```ts
test("calls mock1 before mock2", () => {
  const mock1 = vi.fn();
  const mock2 = vi.fn();

  mock1();
  mock2();
  mock1();

  expect(mock1).toHaveBeenCalledBefore(mock2);
});
```

## toHaveBeenCalledAfter 3.0.0 {#tohavebeencalledafter}

- **Type**: `(mock: MockInstance, failIfNoFirstInvocation?: boolean) => Awaitable<void>`

한 `Mock`이 다른 `Mock`보다 나중에 호출되었는지 확인하는 assertion입니다.

```ts
test("calls mock1 after mock2", () => {
  const mock1 = vi.fn();
  const mock2 = vi.fn();

  mock2();
  mock1();
  mock2();

  expect(mock1).toHaveBeenCalledAfter(mock2);
});
```

## toHaveBeenCalledExactlyOnceWith 3.0.0 {#tohavebeencalledexactlyoncewith}

- **Type**: `(...args: any[]) => Awaitable<void>`

함수가 정확히 한 번, 그리고 특정 파라미터로 호출되었는지 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("spy function", () => {
  const buySpy = vi.spyOn(market, "buy");

  market.buy("apples", 10);

  expect(buySpy).toHaveBeenCalledExactlyOnceWith("apples", 10);
});
```

## toHaveBeenLastCalledWith

- **Type**: `(...args: any[]) => Awaitable<void>`

함수가 마지막 호출에서 특정 파라미터로 호출되었는지 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("spy function", () => {
  const buySpy = vi.spyOn(market, "buy");

  market.buy("apples", 10);
  market.buy("apples", 20);

  expect(buySpy).not.toHaveBeenLastCalledWith("apples", 10);
  expect(buySpy).toHaveBeenLastCalledWith("apples", 20);
});
```

## toHaveBeenNthCalledWith

- **Type**: `(time: number, ...args: any[]) => Awaitable<void>`

함수가 특정 번째 호출에서 특정 파라미터로 호출되었는지 확인하는 assertion입니다. 카운트는 1부터 시작합니다. 따라서 두 번째 항목을 확인하려면 `.toHaveBeenNthCalledWith(2, ...)`처럼 작성합니다.

`expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

const market = {
  buy(subject: string, amount: number) {
    // ...
  },
};

test("first call of spy function called with right params", () => {
  const buySpy = vi.spyOn(market, "buy");

  market.buy("apples", 10);
  market.buy("apples", 20);

  expect(buySpy).toHaveBeenNthCalledWith(1, "apples", 10);
});
```

## toHaveReturned

- **Type**: `() => Awaitable<void>`

함수가 최소 한 번 성공적으로 값을 반환했는지(즉, 에러를 throw 하지 않았는지) 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

function getApplesPrice(amount: number) {
  const PRICE = 10;
  return amount * PRICE;
}

test("spy function returned a value", () => {
  const getPriceSpy = vi.fn(getApplesPrice);

  const price = getPriceSpy(10);

  expect(price).toBe(100);
  expect(getPriceSpy).toHaveReturned();
});
```

## toHaveReturnedTimes

- **Type**: `(amount: number) => Awaitable<void>`

함수가 정확히 지정한 횟수만큼 성공적으로 값을 반환했는지(즉, 에러를 throw 하지 않았는지) 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function returns a value two times", () => {
  const sell = vi.fn((product: string) => ({ product }));

  sell("apples");
  sell("bananas");

  expect(sell).toHaveReturnedTimes(2);
});
```

## toHaveReturnedWith

- **Type**: `(returnValue: any) => Awaitable<void>`

함수가 특정 값으로 최소 한 번 성공적으로 반환했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function returns a product", () => {
  const sell = vi.fn((product: string) => ({ product }));

  sell("apples");

  expect(sell).toHaveReturnedWith({ product: "apples" });
});
```

## toHaveLastReturnedWith

- **Type**: `(returnValue: any) => Awaitable<void>`

함수가 마지막 호출에서 특정 값을 성공적으로 반환했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function returns bananas on a last call", () => {
  const sell = vi.fn((product: string) => ({ product }));

  sell("apples");
  sell("bananas");

  expect(sell).toHaveLastReturnedWith({ product: "bananas" });
});
```

## toHaveNthReturnedWith

- **Type**: `(time: number, returnValue: any) => Awaitable<void>`

함수가 특정 번째 호출에서 특정 값을 성공적으로 반환했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

카운트는 1부터 시작합니다. 따라서 두 번째 항목을 확인하려면 `.toHaveNthReturnedWith(2, ...)`처럼 작성합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function returns bananas on second call", () => {
  const sell = vi.fn((product: string) => ({ product }));

  sell("apples");
  sell("bananas");

  expect(sell).toHaveNthReturnedWith(2, { product: "bananas" });
});
```

## toHaveResolved

- **Type**: `() => Awaitable<void>`

함수가 최소 한 번 성공적으로 값을 resolve 했는지(즉, reject 하지 않았는지) 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

함수가 promise를 반환했지만 아직 resolve되지 않았다면 실패합니다.

```ts
import { expect, test, vi } from "vitest";
import db from "./db/apples.js";

async function getApplesPrice(amount: number) {
  return amount * (await db.get("price"));
}

test("spy function resolved a value", async () => {
  const getPriceSpy = vi.fn(getApplesPrice);

  const price = await getPriceSpy(10);

  expect(price).toBe(100);
  expect(getPriceSpy).toHaveResolved();
});
```

## toHaveResolvedTimes

- **Type**: `(amount: number) => Awaitable<void>`

함수가 정확히 지정한 횟수만큼 성공적으로 값을 resolve 했는지(즉, reject 하지 않았는지) 확인하는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

resolve된 promise만 카운트합니다. 함수가 promise를 반환했지만 아직 resolve되지 않았다면 카운트되지 않습니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function resolved a value two times", async () => {
  const sell = vi.fn((product: string) => Promise.resolve({ product }));

  await sell("apples");
  await sell("bananas");

  expect(sell).toHaveResolvedTimes(2);
});
```

## toHaveResolvedWith

- **Type**: `(returnValue: any) => Awaitable<void>`

함수가 특정 값을 최소 한 번 성공적으로 resolve 했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

함수가 promise를 반환했지만 아직 resolve되지 않았다면 실패합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function resolved a product", async () => {
  const sell = vi.fn((product: string) => Promise.resolve({ product }));

  await sell("apples");

  expect(sell).toHaveResolvedWith({ product: "apples" });
});
```

## toHaveLastResolvedWith

- **Type**: `(returnValue: any) => Awaitable<void>`

함수가 마지막 호출에서 특정 값을 성공적으로 resolve 했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

함수가 promise를 반환했지만 아직 resolve되지 않았다면 실패합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function resolves bananas on a last call", async () => {
  const sell = vi.fn((product: string) => Promise.resolve({ product }));

  await sell("apples");
  await sell("bananas");

  expect(sell).toHaveLastResolvedWith({ product: "bananas" });
});
```

## toHaveNthResolvedWith

- **Type**: `(time: number, returnValue: any) => Awaitable<void>`

함수가 특정 호출에서 특정 값을 성공적으로 resolve 했는지 확인할 때 사용할 수 있는 assertion입니다. `expect`에 spy 함수를 전달해야 합니다.

함수가 promise를 반환했지만 아직 resolve되지 않았다면 실패합니다.

카운트는 1부터 시작합니다. 따라서 두 번째 항목을 확인하려면 `.toHaveNthResolvedWith(2, ...)`처럼 작성합니다.

```ts
import { expect, test, vi } from "vitest";

test("spy function returns bananas on second call", async () => {
  const sell = vi.fn((product: string) => Promise.resolve({ product }));

  await sell("apples");
  await sell("bananas");

  expect(sell).toHaveNthResolvedWith(2, { product: "bananas" });
});
```

## toSatisfy

- **Type:** `(predicate: (value: any) => boolean) => Awaitable<void>`

값이 특정 predicate를 만족하는지 확인하는 assertion입니다.

```ts
import { describe, expect, it } from "vitest";

const isOdd = (value: number) => value % 2 !== 0;

describe("toSatisfy()", () => {
  it("pass with 0", () => {
    expect(1).toSatisfy(isOdd);
  });

  it("pass with negation", () => {
    expect(2).not.toSatisfy(isOdd);
  });
});
```

## resolves

- **Type:** `Promisify<Assertions>`

`resolves`는 비동기 코드 assertion 시 반복 코드를 줄이기 위한 기능입니다. 대기 중인 promise에서 값을 언래핑하고, 일반 assertion으로 그 값을 검증할 때 사용합니다. promise가 reject되면 assertion은 실패합니다.

동일한 `Assertions` 객체를 반환하지만, 이제 모든 matcher가 `Promise`를 반환하므로 `await`가 필요합니다. `chai` assertions와도 함께 동작합니다.

예를 들어 API 호출을 수행하고 데이터를 반환하는 함수가 있다면, 다음 코드로 반환값을 검증할 수 있습니다:

```ts
import { expect, test } from "vitest";

async function buyApples() {
  return fetch("/buy/apples").then((r) => r.json());
}

test("buyApples returns new stock id", async () => {
  // toEqual returns a promise now, so you HAVE to await it
  await expect(buyApples()).resolves.toEqual({ id: 1 }); // jest API
  await expect(buyApples()).resolves.to.equal({ id: 1 }); // chai API
});
```

:::warning
assertion에 `await`를 하지 않으면 항상 통과하는 false-positive 테스트가 됩니다. assertion이 실제로 호출되는지 보장하려면 [`expect.assertions(number)`](#expect-assertions)를 사용할 수 있습니다.

Vitest 3부터 메서드에 `await`를 하지 않으면 테스트 끝에 경고가 표시됩니다. Vitest 4에서는 assertion에 `await`를 하지 않으면 테스트가 "failed"로 처리됩니다.
:::

## rejects

- **Type:** `Promisify<Assertions>`

`rejects`는 비동기 코드 assertion 시 반복 코드를 줄이기 위한 기능입니다. promise가 reject된 이유를 언래핑해 일반 assertion으로 해당 값을 검증할 때 사용합니다. promise가 성공적으로 resolve되면 assertion은 실패합니다.

동일한 `Assertions` 객체를 반환하지만, 이제 모든 matcher가 `Promise`를 반환하므로 `await`가 필요합니다. `chai` assertions와도 함께 동작합니다.

예를 들어 호출 시 실패하는 함수가 있다면, 다음 코드로 실패 이유를 검증할 수 있습니다:

```ts
import { expect, test } from "vitest";

async function buyApples(id) {
  if (!id) {
    throw new Error("no id");
  }
}

test("buyApples throws an error when no id provided", async () => {
  // toThrow returns a promise now, so you HAVE to await it
  await expect(buyApples()).rejects.toThrow("no id");
});
```

:::warning
assertion에 `await`를 하지 않으면 항상 통과하는 false-positive 테스트가 됩니다. assertion이 실제로 호출되었는지 보장하려면 [`expect.assertions(number)`](#expect-assertions)를 사용할 수 있습니다.

Vitest 3부터 메서드에 `await`를 하지 않으면 테스트 끝에 경고가 표시됩니다. Vitest 4에서는 assertion에 `await`를 하지 않으면 테스트가 "failed"로 처리됩니다.
:::

## expect.assertions

- **Type:** `(count: number) => void`

테스트가 통과하거나 실패한 뒤, 테스트 중 특정 개수의 assertion이 호출되었는지 검증합니다. 비동기 코드가 호출되었는지 확인할 때 유용합니다.

예를 들어 비동기로 두 matcher를 호출하는 함수가 있다면, 실제로 호출되었는지 assertion할 수 있습니다.

```ts
import { expect, test } from "vitest";

async function doAsync(...cbs) {
  await Promise.all(cbs.map((cb, index) => cb({ index })));
}

test("all assertions are called", async () => {
  expect.assertions(2);
  function callback1(data) {
    expect(data).toBeTruthy();
  }
  function callback2(data) {
    expect(data).toBeTruthy();
  }

  await doAsync(callback1, callback2);
});
```

::: warning
async concurrent 테스트에서 `assertions`를 사용할 때는 올바른 테스트를 감지할 수 있도록 로컬 [Test Context](https://vitest.dev/guide/test-context)의 `expect`를 사용해야 합니다.
:::

## expect.hasAssertions

- **Type:** `() => void`

테스트가 통과하거나 실패한 뒤, 테스트 중 최소 한 개의 assertion이 호출되었는지 검증합니다. 비동기 코드가 호출되었는지 확인할 때 유용합니다.

예를 들어 콜백을 호출하는 코드가 있다면, 콜백 내부에서 assertion을 할 수 있지만 assertion 호출 여부를 확인하지 않으면 테스트는 항상 통과합니다.

```ts
import { expect, test } from "vitest";
import { db } from "./db.js";

const cbs = [];

function onSelect(cb) {
  cbs.push(cb);
}

// after selecting from db, we call all callbacks
function select(id) {
  return db.select({ id }).then((data) => {
    return Promise.all(cbs.map((cb) => cb(data)));
  });
}

test("callback was called", async () => {
  expect.hasAssertions();
  onSelect((data) => {
    // should be called on select
    expect(data).toBeTruthy();
  });
  // if not awaited, test will fail
  // if you don't have expect.hasAssertions(), test will pass
  await select(3);
});
```

## expect.unreachable

- **Type:** `(message?: string) => never`

이 메서드는 특정 코드 줄에 절대 도달하면 안 된다는 것을 assertion할 때 사용합니다.

예를 들어 전달받은 디렉터리에 `src` 폴더가 없어 `build()`가 throw 하는지 테스트하고, 각 에러를 별도로 처리하고 싶다면 다음과 같이 할 수 있습니다:

```ts
import { expect, test } from "vitest";

async function build(dir) {
  if (dir.includes("no-src")) {
    throw new Error(`${dir}/src does not exist`);
  }
}

const errorDirs = [
  "no-src-folder",
  // ...
];

test.each(errorDirs)('build fails with "%s"', async (dir) => {
  try {
    await build(dir);
    expect.unreachable("Should not pass build");
  } catch (err: any) {
    expect(err).toBeInstanceOf(Error);
    expect(err.stack).toContain("build");

    switch (dir) {
      case "no-src-folder":
        expect(err.message).toBe(`${dir}/src does not exist`);
        break;
      default:
        // to exhaust all error tests
        expect.unreachable("All error test must be handled");
        break;
    }
  }
});
```

## expect.anything

- **Type:** `() => any`

이 비대칭 matcher는 `null` 또는 `undefined`를 제외한 모든 값과 일치합니다. 어떤 프로퍼티가 `null`이나 `undefined`가 아닌 임의의 값으로 존재하는지만 확인하고 싶을 때 유용합니다.

```ts
import { expect, test } from "vitest";

test('object has "apples" key', () => {
  expect({ apples: 22 }).toEqual({ apples: expect.anything() });
});
```

## expect.any

- **타입:** `(constructor: unknown) => any`

이 비대칭 matcher를 동등성 검사와 함께 사용하면, 값이 지정한 constructor의 인스턴스인 경우에만 `true`를 반환합니다. 매번 생성되는 값이 있을 때, 해당 값이 올바른 타입으로 존재하는지만 확인하고 싶다면 유용합니다.

```ts
import { expect, test } from "vitest";
import { generateId } from "./generators.js";

test('"id" is a number', () => {
  expect({ id: generateId() }).toEqual({ id: expect.any(Number) });
});
```

## expect.closeTo {#expect-closeto}

- **타입:** `(expected: any, precision?: number) => any`

`expect.closeTo`는 객체 프로퍼티나 배열 항목의 부동소수점 숫자를 비교할 때 유용합니다. 숫자 자체를 비교해야 한다면 대신 `.toBeCloseTo`를 사용하세요.

선택적 `precision` 인수는 소수점 **이후** 검사할 자릿수를 제한합니다. 기본값 `2`에서는 테스트 기준이 `Math.abs(expected - received) < 0.005 (that is, 10 ** -2 / 2)`입니다.

예를 들어, 다음 테스트는 정밀도 5자리에서 통과합니다:

```js
test("compare float in object properties", () => {
  expect({
    title: "0.1 + 0.2",
    sum: 0.1 + 0.2,
  }).toEqual({
    title: "0.1 + 0.2",
    sum: expect.closeTo(0.3, 5),
  });
});
```

## expect.arrayContaining

- **타입:** `<T>(expected: T[]) => any`

동등성 검사와 함께 사용하면, 이 비대칭 matcher는 값이 배열이고 지정한 항목들을 포함할 때 `true`를 반환합니다.

```ts
import { expect, test } from "vitest";

test("basket includes fuji", () => {
  const basket = {
    varieties: ["Empire", "Fuji", "Gala"],
    count: 3,
  };
  expect(basket).toEqual({
    count: 3,
    varieties: expect.arrayContaining(["Fuji"]),
  });
});
```

:::tip
이 matcher와 함께 `expect.not`을 사용해 기대값을 부정할 수 있습니다.
:::

## expect.objectContaining

- **타입:** `(expected: any) => any`

동등성 검사와 함께 사용하면, 이 비대칭 matcher는 값이 유사한 형태를 가질 때 `true`를 반환합니다.

```ts
import { expect, test } from "vitest";

test("basket has empire apples", () => {
  const basket = {
    varieties: [
      {
        name: "Empire",
        count: 1,
      },
    ],
  };
  expect(basket).toEqual({
    varieties: [expect.objectContaining({ name: "Empire" })],
  });
});
```

:::tip
이 matcher와 함께 `expect.not`을 사용해 기대값을 부정할 수 있습니다.
:::

## expect.stringContaining

- **타입:** `(expected: any) => any`

동등성 검사와 함께 사용하면, 이 비대칭 matcher는 값이 문자열이고 지정한 부분 문자열을 포함할 때 `true`를 반환합니다.

```ts
import { expect, test } from "vitest";

test('variety has "Emp" in its name', () => {
  const variety = {
    name: "Empire",
    count: 1,
  };
  expect(variety).toEqual({
    name: expect.stringContaining("Emp"),
    count: 1,
  });
});
```

:::tip
이 matcher와 함께 `expect.not`을 사용해 기대값을 부정할 수 있습니다.
:::

## expect.stringMatching

- **타입:** `(expected: any) => any`

동등성 검사와 함께 사용하면, 이 비대칭 matcher는 값이 문자열이며 지정한 부분 문자열을 포함하거나 문자열이 정규식과 일치할 때 `true`를 반환합니다.

```ts
import { expect, test } from "vitest";

test('variety ends with "re"', () => {
  const variety = {
    name: "Empire",
    count: 1,
  };
  expect(variety).toEqual({
    name: expect.stringMatching(/re$/),
    count: 1,
  });
});
```

:::tip
이 matcher와 함께 `expect.not`을 사용해 기대값을 부정할 수 있습니다.
:::

## expect.schemaMatching

- **타입:** `(expected: StandardSchemaV1) => any`

동등성 검사와 함께 사용하면, 이 비대칭 matcher는 값이 제공된 스키마와 일치할 때 `true`를 반환합니다. 해당 스키마는 [Standard Schema v1](https://standardschema.dev/) 명세를 구현해야 합니다.

```ts
import { expect, test } from "vitest";
import { z } from "zod";
import * as v from "valibot";
import { type } from "arktype";

test("email validation", () => {
  const user = { email: "john@example.com" };

  // using Zod
  expect(user).toEqual({
    email: expect.schemaMatching(z.string().email()),
  });

  // using Valibot
  expect(user).toEqual({
    email: expect.schemaMatching(v.pipe(v.string(), v.email())),
  });

  // using ArkType
  expect(user).toEqual({
    email: expect.schemaMatching(type("string.email")),
  });
});
```

:::tip
이 matcher와 함께 `expect.not`을 사용해 기대값을 부정할 수 있습니다.
:::

## expect.addSnapshotSerializer

- **타입:** `(plugin: PrettyFormatPlugin) => void`

이 메서드는 스냅샷 생성 시 호출되는 커스텀 serializer를 추가합니다. 고급 기능이므로, 더 알고 싶다면 [커스텀 serializer 가이드](https://vitest.dev/guide/snapshot#custom-serializer)를 읽어보세요.

커스텀 serializer를 추가하는 경우, 이 메서드는 [`setupFiles`](https://vitest.dev/config/setupfiles) 내부에서 호출해야 합니다. 그러면 모든 스냅샷에 영향을 줍니다.

:::tip
이전에 Jest와 함께 Vue CLI를 사용했다면 [jest-serializer-vue](https://www.npmjs.com/package/jest-serializer-vue)를 설치하는 것이 좋습니다. 그렇지 않으면 스냅샷이 문자열로 감싸져 `"`가 이스케이프됩니다.
:::

## expect.extend

- **타입:** `(matchers: MatchersObject) => void`

기본 matcher를 사용자 정의 matcher로 확장할 수 있습니다. 이 함수는 matchers 객체를 커스텀 matcher로 확장하는 데 사용됩니다.

이 방식으로 matcher를 정의하면, `expect.stringContaining`처럼 사용할 수 있는 비대칭 matcher도 함께 생성됩니다.

```ts
import { expect, test } from "vitest";

test("custom matchers", () => {
  expect.extend({
    toBeFoo: (received, expected) => {
      if (received !== "foo") {
        return {
          message: () => `expected ${received} to be foo`,
          pass: false,
        };
      }
    },
  });

  expect("foo").toBeFoo();
  expect({ foo: "foo" }).toEqual({ foo: expect.toBeFoo() });
});
```

::: tip
모든 테스트에서 matcher를 사용하고 싶다면, 이 메서드를 [`setupFiles`](https://vitest.dev/config/setupfiles) 내부에서 호출해야 합니다.
:::

이 함수는 Jest의 `expect.extend`와 호환되므로, 이를 사용해 커스텀 matcher를 만드는 모든 라이브러리는 Vitest에서도 동작합니다.

TypeScript를 사용한다면, Vitest 0.31.0부터는 아래 코드처럼 ambient declaration 파일(예: `vitest.d.ts`)에서 기본 `Assertion` 인터페이스를 확장할 수 있습니다:

```ts
interface CustomMatchers<R = unknown> {
  toBeFoo: () => R;
}

declare module "vitest" {
  interface Assertion<T = any> extends CustomMatchers<T> {}
  interface AsymmetricMatchersContaining extends CustomMatchers {}
}
```

::: warning
`tsconfig.json`에 ambient declaration 파일을 포함하는 것을 잊지 마세요.
:::

:::tip
더 자세히 알고 싶다면 [matcher 확장 가이드](https://vitest.dev/guide/extending-matchers)를 확인하세요.
:::

## expect.addEqualityTesters {#expect-addequalitytesters}

- **타입:** `(tester: Array<Tester>) => void`

이 메서드를 사용해 커스텀 tester를 정의할 수 있습니다. tester는 matcher가 두 객체가 동일한지 테스트할 때 사용하는 메서드입니다. Jest의 `expect.addEqualityTesters`와 호환됩니다.

```ts
import { expect, test } from "vitest";

class AnagramComparator {
  public word: string;

  constructor(word: string) {
    this.word = word;
  }

  equals(other: AnagramComparator): boolean {
    const cleanStr1 = this.word.replace(/ /g, "").toLowerCase();
    const cleanStr2 = other.word.replace(/ /g, "").toLowerCase();

    const sortedStr1 = cleanStr1.split("").sort().join("");
    const sortedStr2 = cleanStr2.split("").sort().join("");

    return sortedStr1 === sortedStr2;
  }
}

function isAnagramComparator(a: unknown): a is AnagramComparator {
  return a instanceof AnagramComparator;
}

function areAnagramsEqual(a: unknown, b: unknown): boolean | undefined {
  const isAAnagramComparator = isAnagramComparator(a);
  const isBAnagramComparator = isAnagramComparator(b);

  if (isAAnagramComparator && isBAnagramComparator) {
    return a.equals(b);
  } else if (isAAnagramComparator === isBAnagramComparator) {
    return undefined;
  } else {
    return false;
  }
}

expect.addEqualityTesters([areAnagramsEqual]);

test("custom equality tester", () => {
  expect(new AnagramComparator("listen")).toEqual(
    new AnagramComparator("silent"),
  );
});
```
