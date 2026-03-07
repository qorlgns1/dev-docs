---
title: "assert"
description: "Vitest는 불변 조건을 검증하기 위해 의  메서드를 다시 내보냅니다."
---

출처 URL: https://vitest.dev/api/assert

# assert

Vitest는 불변 조건을 검증하기 위해 [`chai`](https://www.chaijs.com/api/assert/)의 `assert` 메서드를 다시 내보냅니다.

## assert

- **유형:** `(expression: any, message?: string) => asserts expression`

주어진 `expression`이 truthy임을 단언합니다. 그렇지 않으면 단언이 실패합니다.

```ts
import { assert, test } from "vitest";

test("assert", () => {
  assert("foo" !== "bar", "foo should not be equal to bar");
});
```

## fail

- **유형:**
  - `(message?: string) => never`
  - `<T>(actual: T, expected: T, message?: string, operator?: string) => never`

단언을 강제로 실패시킵니다.

```ts
import { assert, test } from "vitest";

test("assert.fail", () => {
  assert.fail("error message on failure");
  assert.fail("foo", "bar", "foo is not bar", "===");
});
```

## isOk

- **유형:** `<T>(value: T, message?: string) => asserts value`
- **별칭** `ok`

주어진 `value`가 truthy임을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isOk", () => {
  assert.isOk("foo", "every truthy is ok");
  assert.isOk(false, "this will fail since false is not truthy");
});
```

## isNotOk

- **유형:** `<T>(value: T, message?: string) => void`
- **별칭** `notOk`

주어진 `value`가 falsy임을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isNotOk", () => {
  assert.isNotOk("foo", "this will fail, every truthy is not ok");
  assert.isNotOk(false, "this will pass since false is falsy");
});
```

## equal

- **유형:** `<T>(actual: T, expected: T, message?: string) => void`

`actual`과 `expected`의 비엄격 동등성(==)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.equal", () => {
  assert.equal(Math.sqrt(4), "2");
});
```

## notEqual

- **유형:** `<T>(actual: T, expected: T, message?: string) => void`

`actual`과 `expected`의 비엄격 비동등성(!=)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.equal", () => {
  assert.notEqual(Math.sqrt(4), 3);
});
```

## strictEqual

- **유형:** `<T>(actual: T, expected: T, message?: string) => void`

`actual`과 `expected`의 엄격 동등성(===)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.strictEqual", () => {
  assert.strictEqual(Math.sqrt(4), 2);
});
```

## deepEqual

- **유형:** `<T>(actual: T, expected: T, message?: string) => void`

`actual`이 `expected`와 깊은 동등(deep equal)함을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.deepEqual", () => {
  assert.deepEqual({ color: "green" }, { color: "green" });
});
```

## notDeepEqual

- **유형:** `<T>(actual: T, expected: T, message?: string) => void`

`actual`이 `expected`와 깊은 동등이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.notDeepEqual", () => {
  assert.notDeepEqual({ color: "green" }, { color: "red" });
});
```

## isAbove

- **유형:** `(valueToCheck: number, valueToBeAbove: number, message?: string) => void`

`valueToCheck`가 `valueToBeAbove`보다 엄격히 큼(>)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isAbove", () => {
  assert.isAbove(5, 2, "5 is strictly greater than 2");
});
```

## isAtLeast

- **유형:** `(valueToCheck: number, valueToBeAtLeast: number, message?: string) => void`

`valueToCheck`가 `valueToBeAtLeast`보다 크거나 같음(>=)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isAtLeast", () => {
  assert.isAtLeast(5, 2, "5 is greater or equal to 2");
  assert.isAtLeast(3, 3, "3 is greater or equal to 3");
});
```

## isBelow

- **유형:** `(valueToCheck: number, valueToBeBelow: number, message?: string) => void`

`valueToCheck`가 `valueToBeBelow`보다 엄격히 작음(\<)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isBelow", () => {
  assert.isBelow(3, 6, "3 is strictly less than 6");
});
```

## isAtMost

- **유형:** `(valueToCheck: number, valueToBeAtMost: number, message?: string) => void`

`valueToCheck`가 `valueToBeAtMost`보다 작거나 같음(\<=)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isAtMost", () => {
  assert.isAtMost(3, 6, "3 is less than or equal to 6");
  assert.isAtMost(4, 4, "4 is less than or equal to 4");
});
```

## isTrue

- **유형:** `<T>(value: T, message?: string) => asserts value is true`

`value`가 true임을 단언합니다.

```ts
import { assert, test } from "vitest";

const testPassed = true;

test("assert.isTrue", () => {
  assert.isTrue(testPassed);
});
```

## isNotTrue

- **유형:** `<T>(value: T, message?: string) => asserts value is Exclude<T, true>`

`value`가 true가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const testPassed = "ok";

test("assert.isNotTrue", () => {
  assert.isNotTrue(testPassed);
});
```

## isFalse

- **유형:** `<T>(value: T, message?: string) => asserts value is false`

`value`가 false임을 단언합니다.

```ts
import { assert, test } from "vitest";

const testPassed = false;

test("assert.isFalse", () => {
  assert.isFalse(testPassed);
});
```

## isNotFalse

- **유형:** `<T>(value: T, message?: string) => asserts value is Exclude<T, false>`

`value`가 false가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const testPassed = "no";

test("assert.isNotFalse", () => {
  assert.isNotFalse(testPassed);
});
```

## isNull

- **유형:** `<T>(value: T, message?: string) => asserts value is null`

`value`가 null임을 단언합니다.

```ts
import { assert, test } from "vitest";

const error = null;

test("assert.isNull", () => {
  assert.isNull(error, "error is null");
});
```

## isNotNull

- **유형:** `<T>(value: T, message?: string) => asserts value is Exclude<T, null>`

`value`가 null이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const error = { message: "error was occurred" };

test("assert.isNotNull", () => {
  assert.isNotNull(error, "error is not null but object");
});
```

## isNaN

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 NaN임을 단언합니다.

```ts
import { assert, test } from "vitest";

const calculation = 1 * "vitest";

test("assert.isNaN", () => {
  assert.isNaN(calculation, '1 * "vitest" is NaN');
});
```

## isNotNaN

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 NaN이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const calculation = 1 * 2;

test("assert.isNotNaN", () => {
  assert.isNotNaN(calculation, "1 * 2 is Not NaN but 2");
});
```

## exists

- **유형:** `<T>(value: T, message?: string) => asserts value is NonNullable<T>`

`value`가 null도 undefined도 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const name = "foo";

test("assert.exists", () => {
  assert.exists(name, "foo is neither null nor undefined");
});
```

## notExists

- **유형:** `<T>(value: T, message?: string) => asserts value is null | undefined`

`value`가 null 또는 undefined임을 단언합니다.

```ts
import { assert, test } from "vitest";

const foo = null;
const bar = undefined;

test("assert.notExists", () => {
  assert.notExists(foo, "foo is null so not exist");
  assert.notExists(bar, "bar is undefined so not exist");
});
```

## isUndefined

- **유형:** `<T>(value: T, message?: string) => asserts value is undefined`

`value`가 undefined임을 단언합니다.

```ts
import { assert, test } from "vitest";

const name = undefined;

test("assert.isUndefined", () => {
  assert.isUndefined(name, "name is undefined");
});
```

## isDefined

- **유형:** `<T>(value: T, message?: string) => asserts value is Exclude<T, undefined>`

`value`가 undefined가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const name = "foo";

test("assert.isDefined", () => {
  assert.isDefined(name, "name is not undefined");
});
```

## isFunction

- **유형:** `<T>(value: T, message?: string) => void`
- **별칭:** `isCallable`
  `value`가 함수임을 단언합니다.

```ts
import { assert, test } from "vitest";

function name() {
  return "foo";
}

test("assert.isFunction", () => {
  assert.isFunction(name, "name is function");
});
```

## isNotFunction

- **유형:** `<T>(value: T, message?: string) => void`
- **별칭:** `isNotCallable`

`value`가 함수가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const name = "foo";

test("assert.isNotFunction", () => {
  assert.isNotFunction(name, "name is not function but string");
});
```

## isObject

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 Object 타입의 객체임을 단언합니다(Object.prototype.toString 기준). 이 단언은 하위 클래스로 확장된 객체에는 일치하지 않습니다.

```ts
import { assert, test } from "vitest";

const someThing = { color: "red", shape: "circle" };

test("assert.isObject", () => {
  assert.isObject(someThing, "someThing is object");
});
```

## isNotObject

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 Object 타입의 객체가 아님을 단언합니다(Object.prototype.toString 기준). 이 단언은 하위 클래스로 확장된 객체에는 일치하지 않습니다.

```ts
import { assert, test } from "vitest";

const someThing = "redCircle";

test("assert.isNotObject", () => {
  assert.isNotObject(someThing, "someThing is not object but string");
});
```

## isArray

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 배열임을 단언합니다.

```ts
import { assert, test } from "vitest";

const color = ["red", "green", "yellow"];

test("assert.isArray", () => {
  assert.isArray(color, "color is array");
});
```

## isNotArray

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 배열이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const color = "red";

test("assert.isNotArray", () => {
  assert.isNotArray(color, "color is not array but string");
});
```

## isString

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 문자열임을 단언합니다.

```ts
import { assert, test } from "vitest";

const color = "red";

test("assert.isString", () => {
  assert.isString(color, "color is string");
});
```

## isNotString

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 문자열이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const color = ["red", "green", "yellow"];

test("assert.isNotString", () => {
  assert.isNotString(color, "color is not string but array");
});
```

## isNumber

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 숫자임을 단언합니다.

```ts
import { assert, test } from "vitest";

const colors = 3;

test("assert.isNumber", () => {
  assert.isNumber(colors, "colors is number");
});
```

## isNotNumber

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 숫자가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const colors = "3 colors";

test("assert.isNotNumber", () => {
  assert.isNotNumber(colors, "colors is not number but strings");
});
```

## isFinite

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 유한한 숫자임을 단언합니다(NaN, Infinity 제외).

```ts
import { assert, test } from "vitest";

const colors = 3;

test("assert.isFinite", () => {
  assert.isFinite(colors, "colors is number not NaN or Infinity");
});
```

## isBoolean

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 불리언임을 단언합니다.

```ts
import { assert, test } from "vitest";

const isReady = true;

test("assert.isBoolean", () => {
  assert.isBoolean(isReady, "isReady is a boolean");
});
```

## isNotBoolean

- **유형:** `<T>(value: T, message?: string) => void`

`value`가 불리언이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

const isReady = "sure";

test("assert.isBoolean", () => {
  assert.isBoolean(isReady, "isReady is not a boolean but string");
});
```

## typeOf

- **유형:** `<T>(value: T, name: string, message?: string) => void`

Object.prototype.toString으로 판별했을 때 `value`의 타입이 `name`임을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.typeOf", () => {
  assert.typeOf({ color: "red" }, "object", "we have an object");
  assert.typeOf(["red", "green"], "array", "we have an array");
  assert.typeOf("red", "string", "we have a string");
  assert.typeOf(/red/, "regexp", "we have a regular expression");
  assert.typeOf(null, "null", "we have a null");
  assert.typeOf(undefined, "undefined", "we have an undefined");
});
```

## notTypeOf

- **유형:** `<T>(value: T, name: string, message?: string) => void`

Object.prototype.toString으로 판별했을 때 `value`의 타입이 `name`이 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.notTypeOf", () => {
  assert.notTypeOf("red", "number", '"red" is not a number');
});
```

## instanceOf

- **유형:** `<T>(value: T, constructor: Function, message?: string) => asserts value is T`

`value`가 `constructor`의 인스턴스임을 단언합니다.

```ts
import { assert, test } from "vitest";

function Person(name) {
  this.name = name;
}
const foo = new Person("foo");

class Tea {
  constructor(name) {
    this.name = name;
  }
}
const coffee = new Tea("coffee");

test("assert.instanceOf", () => {
  assert.instanceOf(foo, Person, "foo is an instance of Person");
  assert.instanceOf(coffee, Tea, "coffee is an instance of Tea");
});
```

## notInstanceOf

- **유형:** `<T>(value: T, constructor: Function, message?: string) => asserts value is Exclude<T, U>`

`value`가 `constructor`의 인스턴스가 아님을 단언합니다.

```ts
import { assert, test } from "vitest";

function Person(name) {
  this.name = name;
}
const foo = new Person("foo");

class Tea {
  constructor(name) {
    this.name = name;
  }
}
const coffee = new Tea("coffee");

test("assert.instanceOf", () => {
  assert.instanceOf(foo, Tea, "foo is not an instance of Tea");
});
```

## include

- **유형:**
  - `(haystack: string, needle: string, message?: string) => void`
  - `<T>(haystack: readonly T[] | ReadonlySet<T> | ReadonlyMap<any, T>, needle: T, message?: string) => void`
  - `<T extends object>(haystack: WeakSet<T>, needle: T, message?: string) => void`
  - `<T>(haystack: T, needle: Partial<T>, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 배열의 값 포함, 문자열의 부분 문자열 포함, 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.include", () => {
  assert.include([1, 2, 3], 2, "array contains value");
  assert.include("foobar", "foo", "string contains substring");
  assert.include(
    { foo: "bar", hello: "universe" },
    { foo: "bar" },
    "object contains property",
  );
});
```

## notInclude

- **유형:**
  - `(haystack: string, needle: string, message?: string) => void`
  - `<T>(haystack: readonly T[] | ReadonlySet<T> | ReadonlyMap<any, T>, needle: T, message?: string) => void`
  - `<T extends object>(haystack: WeakSet<T>, needle: T, message?: string) => void`
  - `<T>(haystack: T, needle: Partial<T>, message?: string) => void`

`haystack`에 `needle`이 포함되지 않음을 단언합니다. 배열의 값 부재, 문자열의 부분 문자열 부재, 객체의 속성 부분집합 부재를 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.notInclude", () => {
  assert.notInclude([1, 2, 3], 4, "array doesn't contain 4");
  assert.notInclude("foobar", "baz", "foobar doesn't contain baz");
  assert.notInclude(
    { foo: "bar", hello: "universe" },
    { foo: "baz" },
    "object doesn't contain property",
  );
});
```

## deepInclude

- **유형:**
- `(haystack: string, needle: string, message?: string) => void`
- `<T>(haystack: readonly T[] | ReadonlySet<T> | ReadonlyMap<any, T>, needle: T, message?: string) => void`
- `<T>(haystack: T, needle: T extends WeakSet<any> ? never : Partial<T>, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 배열의 값 포함 또는 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다. 깊은 동등성(deep equality)을 사용합니다.

```ts
import { assert, test } from "vitest";

const obj1 = { a: 1 };
const obj2 = { b: 2 };

test("assert.deepInclude", () => {
  assert.deepInclude([obj1, obj2], { a: 1 });
  assert.deepInclude({ foo: obj1, bar: obj2 }, { foo: { a: 1 } });
});
```

## notDeepInclude

- **유형:**
  - `(haystack: string, needle: string, message?: string) => void`
  - `<T>(haystack: readonly T[] | ReadonlySet<T> | ReadonlyMap<any, T>, needle: T, message?: string) => void`
  - `<T>(haystack: T, needle: T extends WeakSet<any> ? never : Partial<T>, message?: string) => void`

`haystack`에 `needle`이 포함되지 않음을 단언합니다. 배열의 값 부재 또는 객체의 속성 부분집합 부재를 단언할 때 사용할 수 있습니다. 깊은 동등성(deep equality)을 사용합니다.

```ts
import { assert, test } from "vitest";

const obj1 = { a: 1 };
const obj2 = { b: 2 };

test("assert.notDeepInclude", () => {
  assert.notDeepInclude([obj1, obj2], { a: 10 });
  assert.notDeepInclude({ foo: obj1, bar: obj2 }, { foo: { a: 10 } });
});
```

## nestedInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다. 중첩 속성 참조를 위해 dot 표기법과 bracket 표기법을 사용할 수 있습니다. 속성 이름의 ‘[]’와 ‘.’는 이중 백슬래시로 이스케이프할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.nestedInclude", () => {
  assert.nestedInclude({ ".a": { b: "x" } }, { "\\.a.[b]": "x" });
  assert.nestedInclude({ a: { "[b]": "x" } }, { "a.\\[b\\]": "x" });
});
```

## notNestedInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함되지 않음을 단언합니다. 객체의 속성 부분집합 포함 여부를 단언할 때 사용할 수 있습니다. 중첩 속성 참조를 위해 dot 표기법과 bracket 표기법을 사용할 수 있습니다. 속성 이름의 ‘[]’와 ‘.’는 이중 백슬래시로 이스케이프할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.nestedInclude", () => {
  assert.notNestedInclude({ ".a": { b: "x" } }, { "\\.a.b": "y" });
  assert.notNestedInclude({ a: { "[b]": "x" } }, { "a.\\[b\\]": "y" });
});
```

## deepNestedInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 깊은 동등성을 확인하면서 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다. 중첩 속성 참조를 위해 dot 표기법과 bracket 표기법을 사용할 수 있습니다. 속성 이름의 ‘[]’와 ‘.’는 이중 백슬래시로 이스케이프할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.deepNestedInclude", () => {
  assert.deepNestedInclude({ a: { b: [{ x: 1 }] } }, { "a.b[0]": { x: 1 } });
  assert.deepNestedInclude(
    { ".a": { "[b]": { x: 1 } } },
    { "\\.a.\\[b\\]": { x: 1 } },
  );
});
```

## notDeepNestedInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함되지 않음을 단언합니다. 깊은 동등성을 확인하면서 객체의 속성 부분집합 부재를 단언할 때 사용할 수 있습니다. 중첩 속성 참조를 위해 dot 표기법과 bracket 표기법을 사용할 수 있습니다. 속성 이름의 ‘[]’와 ‘.’는 이중 백슬래시로 이스케이프할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.notDeepNestedInclude", () => {
  assert.notDeepNestedInclude({ a: { b: [{ x: 1 }] } }, { "a.b[0]": { y: 1 } });
  assert.notDeepNestedInclude(
    { ".a": { "[b]": { x: 1 } } },
    { "\\.a.\\[b\\]": { y: 2 } },
  );
});
```

## ownInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 상속된 속성을 무시하면서 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.ownInclude", () => {
  assert.ownInclude({ a: 1 }, { a: 1 });
});
```

## notOwnInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 상속된 속성을 무시하면서 객체의 속성 부분집합 부재를 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

const obj1 = {
  b: 2,
};

const obj2 = object.create(obj1);
obj2.a = 1;

test("assert.notOwnInclude", () => {
  assert.notOwnInclude(obj2, { b: 2 });
});
```

## deepOwnInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함됨을 단언합니다. 상속된 속성을 무시하고 깊은 동등성을 확인하면서 객체의 속성 부분집합 포함을 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.deepOwnInclude", () => {
  assert.deepOwnInclude({ a: { b: 2 } }, { a: { b: 2 } });
});
```

## notDeepOwnInclude

- **유형:** `(haystack: any, needle: any, message?: string) => void`

`haystack`에 `needle`이 포함되지 않음을 단언합니다. 상속된 속성을 무시하고 깊은 동등성을 확인하면서 객체의 속성 부분집합 부재를 단언할 때 사용할 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.notDeepOwnInclude", () => {
  assert.notDeepOwnInclude({ a: { b: 2 } }, { a: { c: 3 } });
});
```

## match

- **유형:** `(value: string, regexp: RegExp, message?: string) => void`

`value`가 정규식 `regexp`와 일치함을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.match", () => {
  assert.match("foobar", /^foo/, "regexp matches");
});
```

## notMatch

- **Type:** `(value: string, regexp: RegExp, message?: string) => void`

`value`가 정규식 `regexp`와 일치하지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.notMatch", () => {
  assert.notMatch("foobar", /^foo/, "regexp does not match");
});
```

## property

- **Type:** `<T>(object: T, property: string, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.property", () => {
  assert.property({ tea: { green: "matcha" } }, "tea");
  assert.property({ tea: { green: "matcha" } }, "toString");
});
```

## notProperty

- **Type:** `<T>(object: T, property: string, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.notProperty", () => {
  assert.notProperty({ tea: { green: "matcha" } }, "coffee");
});
```

## propertyVal

- **Type:** `<T, V>(object: T, property: string, value: V, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있으며, 그 값이 `value`임을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notPropertyVal", () => {
  assert.propertyVal({ tea: "is good" }, "tea", "is good");
});
```

## notPropertyVal

- **Type:** `<T, V>(object: T, property: string, value: V, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 `value` 값으로 가지고 있지 않음을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notPropertyVal", () => {
  assert.notPropertyVal({ tea: "is good" }, "tea", "is bad");
  assert.notPropertyVal({ tea: "is good" }, "coffee", "is good");
});
```

## deepPropertyVal

- **Type:** `<T, V>(object: T, property: string, value: V, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있으며, 그 값이 `value`임을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.deepPropertyVal", () => {
  assert.deepPropertyVal({ tea: { green: "matcha" } }, "tea", {
    green: "matcha",
  });
});
```

## notDeepPropertyVal

- **Type:** `<T, V>(object: T, property: string, value: V, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 `value` 값으로 가지고 있지 않음을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.deepPropertyVal", () => {
  assert.notDeepPropertyVal({ tea: { green: "matcha" } }, "tea", {
    black: "matcha",
  });
  assert.notDeepPropertyVal({ tea: { green: "matcha" } }, "tea", {
    green: "oolong",
  });
  assert.notDeepPropertyVal({ tea: { green: "matcha" } }, "coffee", {
    green: "matcha",
  });
});
```

## nestedProperty

- **Type:** `<T>(object: T, property: string, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있음을 단언하며, `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용하는 문자열일 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.deepPropertyVal", () => {
  assert.nestedProperty({ tea: { green: "matcha" } }, "tea.green");
});
```

## notNestedProperty

- **Type:** `<T>(object: T, property: string, message?: string) => void`

`object`가 `property`로 지정된 이름의 직접 또는 상속된 속성을 가지고 있지 않음을 단언하며, `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용하는 문자열일 수 있습니다.

```ts
import { assert, test } from "vitest";

test("assert.deepPropertyVal", () => {
  assert.notNestedProperty({ tea: { green: "matcha" } }, "tea.oolong");
});
```

## nestedPropertyVal

- **Type:** `<T>(object: T, property: string, value: any, message?: string) => void`

`object`가 `property`로 지정된 이름의 속성을 가지고 있으며 그 값이 `value`임을 단언합니다. `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용할 수 있습니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.nestedPropertyVal", () => {
  assert.nestedPropertyVal({ tea: { green: "matcha" } }, "tea.green", "matcha");
});
```

## notNestedPropertyVal

- **Type:** `<T>(object: T, property: string, value: any, message?: string) => void`

`object`가 `property`로 지정된 이름의 속성을 `value` 값으로 가지고 있지 않음을 단언합니다. `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용할 수 있습니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notNestedPropertyVal", () => {
  assert.notNestedPropertyVal(
    { tea: { green: "matcha" } },
    "tea.green",
    "konacha",
  );
  assert.notNestedPropertyVal(
    { tea: { green: "matcha" } },
    "coffee.green",
    "matcha",
  );
});
```

## deepNestedPropertyVal

- **Type:** `<T>(object: T, property: string, value: any, message?: string) => void`

`object`가 `property`로 지정된 이름의 속성을 가지고 있으며 그 값이 `value`임을 단언합니다. `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용할 수 있습니다. 깊은 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notNestedPropertyVal", () => {
  assert.notNestedPropertyVal(
    { tea: { green: "matcha" } },
    "tea.green",
    "konacha",
  );
  assert.notNestedPropertyVal(
    { tea: { green: "matcha" } },
    "coffee.green",
    "matcha",
  );
});
```

## notDeepNestedPropertyVal

- **Type:** `<T>(object: T, property: string, value: any, message?: string) => void`

`object`가 `property`로 지정된 이름의 속성을 `value` 값으로 가지고 있지 않음을 단언합니다. `property`는 중첩 참조를 위해 점 표기법 및 대괄호 표기법을 사용할 수 있습니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notDeepNestedPropertyVal", () => {
  assert.notDeepNestedPropertyVal(
    { tea: { green: { matcha: "yum" } } },
    "tea.green",
    { oolong: "yum" },
  );
  assert.notDeepNestedPropertyVal(
    { tea: { green: { matcha: "yum" } } },
    "tea.green",
    { matcha: "yuck" },
  );
  assert.notDeepNestedPropertyVal(
    { tea: { green: { matcha: "yum" } } },
    "tea.black",
    { matcha: "yum" },
  );
});
```

## lengthOf

- **Type:** `<T extends { readonly length?: number | undefined } | { readonly size?: number | undefined }>(object: T, length: number, message?: string) => void`

`object`가 예상된 값을 가진 `length` 또는 `size`를 가지고 있음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.lengthOf", () => {
  assert.lengthOf([1, 2, 3], 3, "array has length of 3");
  assert.lengthOf("foobar", 6, "string has length of 6");
  assert.lengthOf(new Set([1, 2, 3]), 3, "set has size of 3");
  assert.lengthOf(
    new Map([
      ["a", 1],
      ["b", 2],
      ["c", 3],
    ]),
    3,
    "map has size of 3",
  );
});
```

## hasAnyKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys` 중 최소 하나를 가지고 있음을 단언합니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.hasAnyKeys", () => {
  assert.hasAnyKeys({ foo: 1, bar: 2, baz: 3 }, ["foo", "iDontExist", "baz"]);
  assert.hasAnyKeys(
    { foo: 1, bar: 2, baz: 3 },
    { foo: 30, iDontExist: 99, baz: 1337 },
  );
  assert.hasAnyKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ foo: 1 }, "key"],
  );
  assert.hasAnyKeys(new Set([{ foo: "bar" }, "anotherKey"]), [
    { foo: "bar" },
    "anotherKey",
  ]);
});
```

## hasAllKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 모두, 그리고 그것만 가지고 있음을 단언합니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.hasAllKeys", () => {
  assert.hasAllKeys({ foo: 1, bar: 2, baz: 3 }, ["foo", "bar", "baz"]);
  assert.hasAllKeys(
    { foo: 1, bar: 2, baz: 3 },
    { foo: 30, bar: 99, baz: 1337 },
  );
  assert.hasAllKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ foo: 1 }, "key"],
  );
  assert.hasAllKeys(
    new Set([{ foo: "bar" }, "anotherKey"], [{ foo: "bar" }, "anotherKey"]),
  );
});
```

## containsAllKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 모두 가지고 있되, 목록에 없는 추가 키를 더 가질 수도 있음을 단언합니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.containsAllKeys", () => {
  assert.containsAllKeys({ foo: 1, bar: 2, baz: 3 }, ["foo", "baz"]);
  assert.containsAllKeys({ foo: 1, bar: 2, baz: 3 }, ["foo", "bar", "baz"]);
  assert.containsAllKeys({ foo: 1, bar: 2, baz: 3 }, { foo: 30, baz: 1337 });
  assert.containsAllKeys(
    { foo: 1, bar: 2, baz: 3 },
    { foo: 30, bar: 99, baz: 1337 },
  );
  assert.containsAllKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ foo: 1 }],
  );
  assert.containsAllKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ foo: 1 }, "key"],
  );
  assert.containsAllKeys(
    new Set([{ foo: "bar" }, "anotherKey"], [{ foo: "bar" }]),
  );
  assert.containsAllKeys(
    new Set([{ foo: "bar" }, "anotherKey"], [{ foo: "bar" }, "anotherKey"]),
  );
});
```

## doesNotHaveAnyKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 하나도 가지고 있지 않음을 단언합니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotHaveAnyKeys", () => {
  assert.doesNotHaveAnyKeys({ foo: 1, bar: 2, baz: 3 }, [
    "one",
    "two",
    "example",
  ]);
  assert.doesNotHaveAnyKeys(
    { foo: 1, bar: 2, baz: 3 },
    { one: 1, two: 2, example: "foo" },
  );
  assert.doesNotHaveAnyKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ one: "two" }, "example"],
  );
  assert.doesNotHaveAnyKeys(
    new Set([{ foo: "bar" }, "anotherKey"], [{ one: "two" }, "example"]),
  );
});
```

## doesNotHaveAllKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys` 중 적어도 하나는 가지고 있지 않음을 단언합니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.hasAnyKeys", () => {
  assert.doesNotHaveAnyKeys({ foo: 1, bar: 2, baz: 3 }, [
    "one",
    "two",
    "example",
  ]);
  assert.doesNotHaveAnyKeys(
    { foo: 1, bar: 2, baz: 3 },
    { one: 1, two: 2, example: "foo" },
  );
  assert.doesNotHaveAnyKeys(
    new Map([
      [{ foo: 1 }, "bar"],
      ["key", "value"],
    ]),
    [{ one: "two" }, "example"],
  );
  assert.doesNotHaveAnyKeys(new Set([{ foo: "bar" }, "anotherKey"]), [
    { one: "two" },
    "example",
  ]);
});
```

## hasAnyDeepKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys` 중 최소 하나를 가지고 있음을 단언합니다. Sets와 Maps는 객체를 키로 가질 수 있으므로, 이 단언을 사용해 깊은 비교를 수행할 수 있습니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.hasAnyDeepKeys", () => {
  assert.hasAnyDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [1, 2],
    ]),
    { one: "one" },
  );
  assert.hasAnyDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [1, 2],
    ]),
    [{ one: "one" }, { two: "two" }],
  );
  assert.hasAnyDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [{ two: "two" }, "valueTwo"],
    ]),
    [{ one: "one" }, { two: "two" }],
  );
  assert.hasAnyDeepKeys(new Set([{ one: "one" }, { two: "two" }]), {
    one: "one",
  });
  assert.hasAnyDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { one: "one" },
    { three: "three" },
  ]);
  assert.hasAnyDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { one: "one" },
    { two: "two" },
  ]);
});
```

## hasAllDeepKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 모두, 그리고 그것만 가지고 있음을 단언합니다. Sets와 Maps는 객체를 키로 가질 수 있으므로, 이 단언을 사용해 깊은 비교를 수행할 수 있습니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.hasAnyDeepKeys", () => {
  assert.hasAllDeepKeys(new Map([[{ one: "one" }, "valueOne"]]), {
    one: "one",
  });
  assert.hasAllDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [{ two: "two" }, "valueTwo"],
    ]),
    [{ one: "one" }, { two: "two" }],
  );
  assert.hasAllDeepKeys(new Set([{ one: "one" }]), { one: "one" });
  assert.hasAllDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { one: "one" },
    { two: "two" },
  ]);
});
```

## containsAllDeepKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 모두 포함함을 단언합니다. Sets와 Maps는 객체를 키로 가질 수 있으므로, 이 단언을 사용해 깊은 비교를 수행할 수 있습니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.containsAllDeepKeys", () => {
  assert.containsAllDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [1, 2],
    ]),
    { one: "one" },
  );
  assert.containsAllDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [{ two: "two" }, "valueTwo"],
    ]),
    [{ one: "one" }, { two: "two" }],
  );
  assert.containsAllDeepKeys(new Set([{ one: "one" }, { two: "two" }]), {
    one: "one",
  });
  assert.containsAllDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { one: "one" },
    { two: "two" },
  ]);
});
```

## doesNotHaveAnyDeepKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys`를 하나도 가지고 있지 않음을 단언합니다. Sets와 Maps는 객체를 키로 가질 수 있으므로, 이 단언을 사용해 깊은 비교를 수행할 수 있습니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotHaveAnyDeepKeys", () => {
  assert.doesNotHaveAnyDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [1, 2],
    ]),
    { thisDoesNot: "exist" },
  );
  assert.doesNotHaveAnyDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [{ two: "two" }, "valueTwo"],
    ]),
    [{ twenty: "twenty" }, { fifty: "fifty" }],
  );
  assert.doesNotHaveAnyDeepKeys(new Set([{ one: "one" }, { two: "two" }]), {
    twenty: "twenty",
  });
  assert.doesNotHaveAnyDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { twenty: "twenty" },
    { fifty: "fifty" },
  ]);
});
```

## doesNotHaveAllDeepKeys

- **Type:** `<T>(object: T, keys: Array<Object | string> | { [key: string]: any }, message?: string) => void`

`object`가 제공된 `keys` 중 적어도 하나는 가지고 있지 않음을 단언합니다. Sets와 Maps는 객체를 키로 가질 수 있으므로, 이 단언을 사용해 깊은 비교를 수행할 수 있습니다. 키 배열 대신 단일 객체를 제공할 수도 있으며, 이 경우 해당 객체의 키가 예상 키 집합으로 사용됩니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotHaveAllDeepKeys", () => {
  assert.doesNotHaveAllDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [1, 2],
    ]),
    { thisDoesNot: "exist" },
  );
  assert.doesNotHaveAllDeepKeys(
    new Map([
      [{ one: "one" }, "valueOne"],
      [{ two: "two" }, "valueTwo"],
    ]),
    [{ twenty: "twenty" }, { one: "one" }],
  );
  assert.doesNotHaveAllDeepKeys(new Set([{ one: "one" }, { two: "two" }]), {
    twenty: "twenty",
  });
  assert.doesNotHaveAllDeepKeys(new Set([{ one: "one" }, { two: "two" }]), [
    { one: "one" },
    { fifty: "fifty" },
  ]);
});
```

## throws

- **Type:**
  - `(fn: () => void, errMsgMatcher?: RegExp | string, ignored?: any, message?: string) => void`
  - `(fn: () => void, errorLike?: ErrorConstructor | Error | null, errMsgMatcher?: RegExp | string | null, message?: string) => void`
- **Alias:**
  - `throw`
  - `Throw`

`errorLike`가 Error 생성자이면 `fn`이 `errorLike`의 인스턴스인 오류를 던진다고 단언합니다. `errorLike`가 Error 인스턴스이면, 던져진 오류가 `errorLike`와 동일한 인스턴스임을 단언합니다. `errMsgMatcher`가 제공되면, 던져진 오류의 메시지가 `errMsgMatcher`와 일치함도 함께 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.throws", () => {
  assert.throws(fn, "Error thrown must have this msg");
  assert.throws(fn, /Error thrown must have a msg that matches this/);
  assert.throws(fn, ReferenceError);
  assert.throws(fn, errorInstance);
  assert.throws(
    fn,
    ReferenceError,
    "Error thrown must be a ReferenceError and have this msg",
  );
  assert.throws(
    fn,
    errorInstance,
    "Error thrown must be the same errorInstance and have this msg",
  );
  assert.throws(
    fn,
    ReferenceError,
    /Error thrown must be a ReferenceError and match this/,
  );
  assert.throws(
    fn,
    errorInstance,
    /Error thrown must be the same errorInstance and match this/,
  );
});
```

## doesNotThrow

- **Type:** `(fn: () => void, errMsgMatcher?: RegExp | string, ignored?: any, message?: string) => void`
- **Type:** `(fn: () => void, errorLike?: ErrorConstructor | Error | null, errMsgMatcher?: RegExp | string | null, message?: string) => void`

`errorLike`가 Error 생성자이면 `fn`이 `errorLike`의 인스턴스인 오류를 던지지 않는다고 단언합니다. `errorLike`가 Error 인스턴스이면, 던져진 오류가 `errorLike`와 동일한 인스턴스가 아님을 단언합니다. `errMsgMatcher`가 제공되면, 던져진 오류의 메시지가 `errMsgMatcher`와 일치하지 않음도 함께 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotThrow", () => {
  assert.doesNotThrow(fn, "Any Error thrown must not have this message");
  assert.doesNotThrow(fn, /Any Error thrown must not match this/);
  assert.doesNotThrow(fn, Error);
  assert.doesNotThrow(fn, errorInstance);
  assert.doesNotThrow(fn, Error, "Error must not have this message");
  assert.doesNotThrow(fn, errorInstance, "Error must not have this message");
  assert.doesNotThrow(fn, Error, /Error must not match this/);
  assert.doesNotThrow(fn, errorInstance, /Error must not match this/);
});
```

## operator

- **Type:** `(val1: OperatorComparable, operator: Operator, val2: OperatorComparable, message?: string) => void`

`operator`를 사용해 `val1`과 `val2`를 비교합니다.

```ts
import { assert, test } from "vitest";

test("assert.operator", () => {
  assert.operator(1, "<", 2, "everything is ok");
});
```

## closeTo

- **Type:** `(actual: number, expected: number, delta: number, message?: string) => void`
- **Alias:** `approximately`

`actual`이 +/- `delta` 범위 내에서 `expected`와 같음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.closeTo", () => {
  assert.closeTo(1.5, 1, 0.5, "numbers are close");
});
```

## sameMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 순서와 관계없이 동일한 멤버를 가짐을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameMembers", () => {
  assert.sameMembers([1, 2, 3], [2, 1, 3], "same members");
});
```

## notSameMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 순서와 관계없이 동일한 멤버를 가지지 않음을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameMembers", () => {
  assert.notSameMembers([1, 2, 3], [5, 1, 3], "not same members");
});
```

## sameDeepMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 순서와 관계없이 동일한 멤버를 가짐을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameDeepMembers", () => {
  assert.sameDeepMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { a: 1 }, { c: 3 }],
    "same deep members",
  );
});
```

## notSameDeepMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 순서와 관계없이 동일한 멤버를 가지지 않음을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameDeepMembers", () => {
  assert.sameDeepMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { a: 1 }, { c: 3 }],
    "same deep members",
  );
});
```

## sameOrderedMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 동일한 순서로 동일한 멤버를 가짐을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameOrderedMembers", () => {
  assert.sameOrderedMembers([1, 2, 3], [1, 2, 3], "same ordered members");
});
```

## notSameOrderedMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 동일한 순서로 동일한 멤버를 가짐을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notSameOrderedMembers", () => {
  assert.notSameOrderedMembers(
    [1, 2, 3],
    [2, 1, 3],
    "not same ordered members",
  );
});
```

## sameDeepOrderedMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 동일한 순서로 동일한 멤버를 가짐을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.sameDeepOrderedMembers", () => {
  assert.sameDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    "same deep ordered members",
  );
});
```

## notSameDeepOrderedMembers

- **Type:** `<T>(set1: T[], set2: T[], message?: string) => void`

`set1`과 `set2`가 동일한 순서로 동일한 멤버를 가지지 않음을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notSameDeepOrderedMembers", () => {
  assert.notSameDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ a: 1 }, { b: 2 }, { z: 5 }],
    "not same deep ordered members",
  );
  assert.notSameDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { a: 1 }, { c: 3 }],
    "not same deep ordered members",
  );
});
```

## includeMembers

- **Type:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 순서와 관계없이 `superset`에 포함됨을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다. 중복은 무시됩니다.

```ts
import { assert, test } from "vitest";

test("assert.includeMembers", () => {
  assert.includeMembers([1, 2, 3], [2, 1, 2], "include members");
});
```

## notIncludeMembers

- **Type:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 순서와 관계없이 `superset`에 포함되지 않음을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다. 중복은 무시됩니다.

```ts
import { assert, test } from "vitest";

test("assert.notIncludeMembers", () => {
  assert.notIncludeMembers([1, 2, 3], [5, 1], "not include members");
});
```

## includeDeepMembers

- **Type:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 순서와 관계없이 `superset`에 포함됨을 단언합니다. 깊은 동등성 검사를 사용합니다. 중복은 무시됩니다.

```ts
import { assert, test } from "vitest";

test("assert.includeDeepMembers", () => {
  assert.includeDeepMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { a: 1 }, { b: 2 }],
    "include deep members",
  );
});
```

## notIncludeDeepMembers

- **Type:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 순서와 관계없이 `superset`에 포함되지 않음을 단언합니다. 깊은 동등성 검사를 사용합니다. 중복은 무시됩니다.

```ts
import { assert, test } from "vitest";

test("assert.notIncludeDeepMembers", () => {
  assert.notIncludeDeepMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { f: 5 }],
    "not include deep members",
  );
});
```

## includeOrderedMembers

- **타입:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 `superset`에 `superset`의 첫 번째 요소부터 시작해 동일한 순서로 포함되어 있음을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.includeOrderedMembers", () => {
  assert.includeOrderedMembers([1, 2, 3], [1, 2], "include ordered members");
});
```

## notIncludeOrderedMembers

- **타입:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 `superset`에 `superset`의 첫 번째 요소부터 시작해 동일한 순서로 포함되어 있지 않음을 단언합니다. 엄격한 동등성 검사(===)를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.notIncludeOrderedMembers", () => {
  assert.notIncludeOrderedMembers(
    [1, 2, 3],
    [2, 1],
    "not include ordered members",
  );
  assert.notIncludeOrderedMembers(
    [1, 2, 3],
    [2, 3],
    "not include ordered members",
  );
});
```

## includeDeepOrderedMembers

- **타입:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 `superset`에 `superset`의 첫 번째 요소부터 시작해 동일한 순서로 포함되어 있음을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.includeDeepOrderedMembers", () => {
  assert.includeDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ a: 1 }, { b: 2 }],
    "include deep ordered members",
  );
});
```

## notIncludeDeepOrderedMembers

- **타입:** `<T>(superset: T[], subset: T[], message?: string) => void`

`subset`이 `superset`에 `superset`의 첫 번째 요소부터 시작해 동일한 순서로 포함되어 있지 않음을 단언합니다. 깊은 동등성 검사를 사용합니다.

```ts
import { assert, test } from "vitest";

test("assert.includeDeepOrderedMembers", () => {
  assert.notIncludeDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ a: 1 }, { f: 5 }],
    "not include deep ordered members",
  );
  assert.notIncludeDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { a: 1 }],
    "not include deep ordered members",
  );
  assert.notIncludeDeepOrderedMembers(
    [{ a: 1 }, { b: 2 }, { c: 3 }],
    [{ b: 2 }, { c: 3 }],
    "not include deep ordered members",
  );
});
```

## oneOf

- **타입:** `<T>(inList: T, list: T[], message?: string) => void`

객체도 배열도 아닌 값 `inList`가 평탄한 배열 `list`에 나타남을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.oneOf", () => {
  assert.oneOf(1, [2, 1], "Not found in list");
});
```

## changes

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 `object`의 `property`를 변경함을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.changes", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 22;
  }
  assert.changes(fn, obj, "val");
});
```

## changesBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 `object`의 `property`를 `change`만큼 변경함을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.changesBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val += 2;
  }
  assert.changesBy(fn, obj, "val", 2);
});
```

## doesNotChange

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 `object`의 `property`를 변경하지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotChange", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val += 2;
  }
  assert.doesNotChange(fn, obj, "val", 2);
});
```

## changesButNotBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change:number, message?: string) => void`

`modifier`가 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼은 변경하지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.changesButNotBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val += 10;
  }
  assert.changesButNotBy(fn, obj, "val", 5);
});
```

## increases

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 숫자형 `object`의 `property`를 증가시킴을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.increases", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 13;
  }
  assert.increases(fn, obj, "val");
});
```

## increasesBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 숫자형 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼 증가시킴을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.increasesBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val += 10;
  }
  assert.increasesBy(fn, obj, "val", 10);
});
```

## doesNotIncrease

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 숫자형 `object`의 `property`를 증가시키지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotIncrease", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 8;
  }
  assert.doesNotIncrease(fn, obj, "val");
});
```

## increasesButNotBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 숫자형 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼은 증가시키지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.increasesButNotBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val += 15;
  }
  assert.increasesButNotBy(fn, obj, "val", 10);
});
```

## decreases

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 숫자형 `object`의 `property`를 감소시킴을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.decreases", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 5;
  }
  assert.decreases(fn, obj, "val");
});
```

## decreasesBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 숫자형 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼 감소시킴을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.decreasesBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val -= 5;
  }
  assert.decreasesBy(fn, obj, "val", 5);
});
```

## doesNotDecrease

- **타입:** `<T>(modifier: Function, object: T, property: string, message?: string) => void`

`modifier`가 숫자형 `object`의 `property`를 감소시키지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotDecrease", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 15;
  }
  assert.doesNotDecrease(fn, obj, "val");
});
```

## doesNotDecreaseBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 숫자형 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼 감소시키지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.doesNotDecreaseBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 5;
  }
  assert.doesNotDecreaseBy(fn, obj, "val", 1);
});
```

## decreasesButNotBy

- **타입:** `<T>(modifier: Function, object: T, property: string, change: number, message?: string) => void`

`modifier`가 숫자형 `object`의 `property` 또는 `modifier` 반환값을 `change`만큼은 감소시키지 않음을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.decreasesButNotBy", () => {
  const obj = { val: 10 };
  function fn() {
    obj.val = 5;
  }
  assert.decreasesButNotBy(fn, obj, "val", 1);
});
```

## ifError

- **타입:** `<T>(object: T, message?: string) => void`

`object`가 falsy 값이 아님을 단언하며, truthy 값이면 예외를 던집니다. 이는 chai가 Node의 assert 클래스에 대한 드롭인 대체제로 동작할 수 있도록 추가되었습니다.

```ts
import { assert, test } from "vitest";

test("assert.ifError", () => {
  const err = new Error("I am a custom error");
  assert.ifError(err); // Rethrows err!
});
```

## isExtensible

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `extensible`

`object`가 확장 가능함(새 속성을 추가할 수 있음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isExtensible", () => {
  assert.isExtensible({});
});
```

## isNotExtensible

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `notExtensible`

`object`가 확장 불가능함(새 속성을 추가할 수 없음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isNotExtensible", () => {
  const nonExtensibleObject = Object.preventExtensions({});
  const sealedObject = Object.seal({});
  const frozenObject = Object.freeze({});

  assert.isNotExtensible(nonExtensibleObject);
  assert.isNotExtensible(sealedObject);
  assert.isNotExtensible(frozenObject);
});
```

## isSealed

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `sealed`

`object`가 봉인(sealed) 상태임(새 속성을 추가할 수 없고 기존 속성을 제거할 수 없음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isSealed", () => {
  const sealedObject = Object.seal({});
  const frozenObject = Object.seal({});

  assert.isSealed(sealedObject);
  assert.isSealed(frozenObject);
});
```

## isNotSealed

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `notSealed`

`object`가 봉인(sealed) 상태가 아님(새 속성을 추가할 수 있고 기존 속성을 제거할 수 있음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isNotSealed", () => {
  assert.isNotSealed({});
});
```

## isFrozen

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `frozen`

object가 동결(frozen) 상태임(새 속성을 추가할 수 없고 기존 속성을 수정할 수 없음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isFrozen", () => {
  const frozenObject = Object.freeze({});
  assert.frozen(frozenObject);
});
```

## isNotFrozen

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `notFrozen`

`object`가 동결(frozen) 상태가 아님(새 속성을 추가할 수 있고 기존 속성을 수정할 수 있음)을 단언합니다.

```ts
import { assert, test } from "vitest";

test("assert.isNotFrozen", () => {
  assert.isNotFrozen({});
});
```

## isEmpty

- **타입:** `<T>(target: T, message?: string) => void`
- **별칭:** `empty`

`target`이 어떤 값도 포함하지 않음을 단언합니다. 배열과 문자열은 length 속성을 확인합니다. Map 및 Set 인스턴스는 size 속성을 확인합니다. 함수가 아닌 객체는 자체 enumerable 문자열 키의 개수를 확인합니다.

```ts
import { assert, test } from "vitest";

test("assert.isEmpty", () => {
  assert.isEmpty([]);
  assert.isEmpty("");
  assert.isEmpty(new Map());
  assert.isEmpty({});
});
```

## isNotEmpty

- **타입:** `<T>(object: T, message?: string) => void`
- **별칭:** `notEmpty`

`target`이 값을 포함하고 있음을 단언합니다. 배열과 문자열은 length 속성을 확인합니다. Map 및 Set 인스턴스는 size 속성을 확인합니다. 함수가 아닌 객체는 자체 enumerable 문자열 키의 개수를 확인합니다.

```ts
import { assert, test } from "vitest";

test("assert.isNotEmpty", () => {
  assert.isNotEmpty([1, 2]);
  assert.isNotEmpty("34");
  assert.isNotEmpty(new Set([5, 6]));
  assert.isNotEmpty({ key: 7 });
});
```
