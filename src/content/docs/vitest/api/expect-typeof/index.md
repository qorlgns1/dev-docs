---
title: "expectTypeOf"
description: "런타임 동안 이 함수는 아무 동작도 하지 않습니다. 타입체킹을 활성화하려면  플래그를 전달하는 것을 잊지 마세요."
---

출처 URL: https://vitest.dev/api/expect-typeof

# expectTypeOf

::: warning
런타임 동안 이 함수는 아무 동작도 하지 않습니다. [타입체킹을 활성화](https://vitest.dev/guide/testing-types#run-typechecking)하려면 `--typecheck` 플래그를 전달하는 것을 잊지 마세요.
:::

- **Type:** `<T>(a: unknown) => ExpectTypeOf`

## not

- **Type:** `ExpectTypeOf`

`.not` 속성을 사용해 모든 단언을 부정할 수 있습니다.

## toEqualTypeOf

- **Type:** `<T>(expected: T) => void`

이 matcher는 타입이 서로 완전히 동일한지 확인합니다. 두 객체의 값이 달라도 타입이 같다면 실패하지 않습니다. 하지만 객체에 프로퍼티가 하나라도 빠져 있으면 실패합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf({ a: 1 }).toEqualTypeOf<{ a: number }>();
expectTypeOf({ a: 1 }).toEqualTypeOf({ a: 1 });
expectTypeOf({ a: 1 }).toEqualTypeOf({ a: 2 });
expectTypeOf({ a: 1, b: 1 }).not.toEqualTypeOf<{ a: number }>();
```

## toMatchTypeOf

- **Type:** `<T>(expected: T) => void`

::: warning DEPRECATED
이 matcher는 expect-type v1.2.0부터 deprecated 되었습니다. 대신 [`toExtend`](#toextend)를 사용하세요.
:::
이 matcher는 기대 타입이 제공된 타입을 확장하는지 확인합니다. `toEqual`과는 다르며 [expect](https://vitest.dev/api/expect)의 `toMatchObject()`와 더 유사합니다. 이 matcher로 객체가 타입에 “매칭”되는지 확인할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf({ a: 1, b: 1 }).toMatchTypeOf({ a: 1 });
expectTypeOf<number>().toMatchTypeOf<string | number>();
expectTypeOf<string | number>().not.toMatchTypeOf<number>();
```

## toExtend

- **Type:** `<T>(expected: T) => void`

이 matcher는 기대 타입이 제공된 타입을 확장하는지 확인합니다. `toEqual`과는 다르며 [expect](https://vitest.dev/api/expect)의 `toMatchObject()`와 더 유사합니다. 이 matcher로 객체가 타입에 "매칭"되는지 확인할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf({ a: 1, b: 1 }).toExtend({ a: 1 });
expectTypeOf<number>().toExtend<string | number>();
expectTypeOf<string | number>().not.toExtend<number>();
```

## toMatchObjectType

- **Type:** `() => void`

이 matcher는 객체 타입에 대해 엄격한 검사를 수행하여, 기대 타입이 제공된 객체 타입과 일치하는지 보장합니다. [`toExtend`](#toextend)보다 더 엄격하며, readonly 프로퍼티 같은 문제를 더 잘 잡아낼 수 있어 객체 타입 작업 시 권장됩니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf({ a: 1, b: 2 }).toMatchObjectType<{ a: number }>(); // preferred
expectTypeOf({ a: 1, b: 2 }).toExtend<{ a: number }>(); // works but less strict

// Supports nested object checking
const user = {
  name: "John",
  address: { city: "New York", zip: "10001" },
};
expectTypeOf(user).toMatchObjectType<{
  name: string;
  address: { city: string };
}>();
```

::: warning
이 matcher는 일반 객체 타입에서만 동작합니다. 유니언 타입이나 기타 복잡한 타입에서는 실패합니다. 그런 경우에는 [`toExtend`](#toextend)를 대신 사용하세요.
:::

## extract

- **Type:** `ExpectTypeOf<ExtractedUnion>`

`.extract`를 사용해 타입을 좁혀서 추가 테스트를 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

type ResponsiveProp<T> = T | T[] | { xs?: T; sm?: T; md?: T };

interface CSSProperties {
  margin?: string;
  padding?: string;
}

function getResponsiveProp<T>(_props: T): ResponsiveProp<T> {
  return {};
}

const cssProperties: CSSProperties = { margin: "1px", padding: "2px" };

expectTypeOf(getResponsiveProp(cssProperties))
  .extract<{ xs?: any }>() // extracts the last type from a union
  .toEqualTypeOf<{
    xs?: CSSProperties;
    sm?: CSSProperties;
    md?: CSSProperties;
  }>();

expectTypeOf(getResponsiveProp(cssProperties))
  .extract<unknown[]>() // extracts an array from a union
  .toEqualTypeOf<CSSProperties[]>();
```

::: warning
유니언에서 타입을 찾지 못하면 `.extract`는 `never`를 반환합니다.
:::

## exclude

- **Type:** `ExpectTypeOf<NonExcludedUnion>`

`.exclude`를 사용해 유니언에서 타입을 제거하고 추가 테스트를 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

type ResponsiveProp<T> = T | T[] | { xs?: T; sm?: T; md?: T };

interface CSSProperties {
  margin?: string;
  padding?: string;
}

function getResponsiveProp<T>(_props: T): ResponsiveProp<T> {
  return {};
}

const cssProperties: CSSProperties = { margin: "1px", padding: "2px" };

expectTypeOf(getResponsiveProp(cssProperties))
  .exclude<unknown[]>()
  .exclude<{ xs?: unknown }>() // or just .exclude<unknown[] | { xs?: unknown }>()
  .toEqualTypeOf<CSSProperties>();
```

::: warning
유니언에서 타입을 찾지 못하면 `.exclude`는 `never`를 반환합니다.
:::

## returns

- **Type:** `ExpectTypeOf<ReturnValue>`

`.returns`를 사용해 함수 타입의 반환값을 추출할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(() => {}).returns.toBeVoid();
expectTypeOf((a: number) => [a, a]).returns.toEqualTypeOf([1, 2]);
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## parameters

- **Type:** `ExpectTypeOf<Parameters>`

`.parameters`로 함수 인자를 추출해 해당 값에 대해 단언할 수 있습니다. 매개변수는 배열로 반환됩니다.

```ts
import { expectTypeOf } from "vitest";

type NoParam = () => void;
type HasParam = (s: string) => void;

expectTypeOf<NoParam>().parameters.toEqualTypeOf<[]>();
expectTypeOf<HasParam>().parameters.toEqualTypeOf<[string]>();
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

::: tip
더 표현력 있는 단언을 위해 [`.toBeCallableWith`](#tobecallablewith) matcher를 사용할 수도 있습니다.
:::

## parameter

- **Type:** `(nth: number) => ExpectTypeOf`

`.parameter(number)` 호출로 특정 함수 인자를 추출해 추가 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

function foo(a: number, b: string) {
  return [a, b];
}

expectTypeOf(foo).parameter(0).toBeNumber();
expectTypeOf(foo).parameter(1).toBeString();
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## constructorParameters

- **Type:** `ExpectTypeOf<ConstructorParameters>`

이 메서드로 생성자 매개변수를 값 배열로 추출하고 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(Date).constructorParameters.toEqualTypeOf<
  [] | [string | number | Date]
>();
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

::: tip
더 표현력 있는 단언을 위해 [`.toBeConstructibleWith`](#tobeconstructiblewith) matcher를 사용할 수도 있습니다.
:::

## instance

- **Type:** `ExpectTypeOf<ConstructableInstance>`

이 속성은 제공된 클래스의 인스턴스에 대해 수행할 수 있는 matcher들에 접근할 수 있게 해줍니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(Date).instance.toHaveProperty("toISOString");
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## items

- **Type:** `ExpectTypeOf<T>`

`.items`로 배열 아이템 타입을 가져와 추가 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf([1, 2, 3]).items.toEqualTypeOf<number>();
expectTypeOf([1, 2, 3]).items.not.toEqualTypeOf<string>();
```

## resolves

- **Type:** `ExpectTypeOf<ResolvedPromise>`

이 matcher는 `Promise`의 resolve된 값을 추출하므로, 그 값에 대해 다른 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

async function asyncFunc() {
  return 123;
}

expectTypeOf(asyncFunc).returns.resolves.toBeNumber();
expectTypeOf(Promise.resolve("string")).resolves.toBeString();
```

::: warning
Promise 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## guards

- **Type:** `ExpectTypeOf<Guard>`

이 matcher는 guard 값(예: `v is number`)을 추출하므로, 그 값에 대해 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

function isString(v: any): v is string {
  return typeof v === "string";
}
expectTypeOf(isString).guards.toBeString();
```

::: warning
값이 guard 함수가 아니면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## asserts

- **Type:** `ExpectTypeOf<Assert>`

이 matcher는 assert 값(예: `assert v is number`)을 추출하므로, 그 값에 대해 단언을 수행할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

function assertNumber(v: any): asserts v is number {
  if (typeof v !== "number") {
    throw new TypeError("Nope !");
  }
}

expectTypeOf(assertNumber).asserts.toBeNumber();
```

::: warning
값이 assert 함수가 아니면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## toBeAny

- **Type:** `() => void`

이 matcher로 제공된 타입이 `any` 타입인지 확인할 수 있습니다. 타입이 너무 구체적이면 테스트는 실패합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf<any>().toBeAny();
expectTypeOf({} as any).toBeAny();
expectTypeOf("string").not.toBeAny();
```

## toBeUnknown

- **Type:** `() => void`

이 matcher는 제공된 타입이 `unknown` 타입인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf().toBeUnknown();
expectTypeOf({} as unknown).toBeUnknown();
expectTypeOf("string").not.toBeUnknown();
```

## toBeNever

- **Type:** `() => void`

이 matcher는 제공된 타입이 `never` 타입인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf<never>().toBeNever();
expectTypeOf((): never => {}).returns.toBeNever();
```

## toBeFunction

- **Type:** `() => void`

이 matcher는 제공된 타입이 `function`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(42).not.toBeFunction();
expectTypeOf((): never => {}).toBeFunction();
```

## toBeObject

- **Type:** `() => void`

이 matcher는 제공된 타입이 `object`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(42).not.toBeObject();
expectTypeOf({}).toBeObject();
```

## toBeArray

- **Type:** `() => void`

이 matcher는 제공된 타입이 `Array<T>`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(42).not.toBeArray();
expectTypeOf([]).toBeArray();
expectTypeOf([1, 2]).toBeArray();
expectTypeOf([{}, 42]).toBeArray();
```

## toBeString

- **Type:** `() => void`

이 matcher는 제공된 타입이 `string`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(42).not.toBeString();
expectTypeOf("").toBeString();
expectTypeOf("a").toBeString();
```

## toBeBoolean

- **Type:** `() => void`

이 matcher는 제공된 타입이 `boolean`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(42).not.toBeBoolean();
expectTypeOf(true).toBeBoolean();
expectTypeOf<boolean>().toBeBoolean();
```

## toBeVoid

- **Type:** `() => void`

이 matcher는 제공된 타입이 `void`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(() => {}).returns.toBeVoid();
expectTypeOf<void>().toBeVoid();
```

## toBeSymbol

- **Type:** `() => void`

이 matcher는 제공된 타입이 `symbol`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(Symbol(1)).toBeSymbol();
expectTypeOf<symbol>().toBeSymbol();
```

## toBeNull

- **Type:** `() => void`

이 matcher는 제공된 타입이 `null`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(null).toBeNull();
expectTypeOf<null>().toBeNull();
expectTypeOf(undefined).not.toBeNull();
```

## toBeUndefined

- **Type:** `() => void`

이 matcher는 제공된 타입이 `undefined`인지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(undefined).toBeUndefined();
expectTypeOf<undefined>().toBeUndefined();
expectTypeOf(null).not.toBeUndefined();
```

## toBeNullable

- **Type:** `() => void`

이 matcher는 제공된 타입에서 `null` 또는 `undefined`를 사용할 수 있는지 확인합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf<undefined | 1>().toBeNullable();
expectTypeOf<null | 1>().toBeNullable();
expectTypeOf<undefined | null | 1>().toBeNullable();
```

## toBeCallableWith

- **Type:** `() => void`

이 matcher는 제공된 함수를 특정 매개변수 집합으로 호출할 수 있는지 보장합니다.

```ts
import { expectTypeOf } from "vitest";

type NoParam = () => void;
type HasParam = (s: string) => void;

expectTypeOf<NoParam>().toBeCallableWith();
expectTypeOf<HasParam>().toBeCallableWith("some string");
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## toBeConstructibleWith

- **Type:** `() => void`

이 matcher는 특정 생성자 매개변수 집합으로 새 인스턴스를 만들 수 있는지 보장합니다.

```ts
import { expectTypeOf } from "vitest";

expectTypeOf(Date).toBeConstructibleWith(new Date());
expectTypeOf(Date).toBeConstructibleWith("01-01-2000");
```

::: warning
함수 타입이 아닌 것에 사용하면 `never`를 반환하므로 다른 matcher와 체이닝할 수 없습니다.
:::

## toHaveProperty

- **Type:** `<K extends keyof T>(property: K) => ExpectTypeOf<T[K>`

이 matcher는 제공된 객체에 프로퍼티가 존재하는지 확인합니다. 존재하면 해당 프로퍼티 타입에 대한 동일한 matcher 집합도 반환하므로 단언을 연달아 체이닝할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

const obj = { a: 1, b: "" };

expectTypeOf(obj).toHaveProperty("a");
expectTypeOf(obj).not.toHaveProperty("c");

expectTypeOf(obj).toHaveProperty("a").toBeNumber();
expectTypeOf(obj).toHaveProperty("b").toBeString();
expectTypeOf(obj).toHaveProperty("a").not.toBeString();
```

## branded

- **Type:** `ExpectTypeOf<BrandedType>`

`.branded`를 사용하면 의미적으로 동등하지만 표현 방식이 다른 타입에 대해서도 타입 단언이 통과되도록 할 수 있습니다.

```ts
import { expectTypeOf } from "vitest";

// Without .branded, this fails even though the types are effectively the same
expectTypeOf<{ a: { b: 1 } & { c: 1 } }>().toEqualTypeOf<{
  a: { b: 1; c: 1 };
}>();

// With .branded, the assertion succeeds
expectTypeOf<{ a: { b: 1 } & { c: 1 } }>().branded.toEqualTypeOf<{
  a: { b: 1; c: 1 };
}>();
```

::: warning
이 헬퍼는 성능 비용이 있으며, 지나치게 깊은 타입에 사용하면 TypeScript 컴파일러가 '포기'할 수 있습니다. 필요한 경우에만 신중하게 사용하세요.
:::
