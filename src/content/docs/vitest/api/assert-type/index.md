---
title: "assertType"
description: "런타임 동안 이 함수는 아무 동작도 하지 않습니다. 타입체크를 활성화하려면  플래그를 전달하는 것을 잊지 마세요."
---

출처 URL: https://vitest.dev/api/assert-type

# assertType

::: warning
런타임 동안 이 함수는 아무 동작도 하지 않습니다. [타입체크를 활성화](https://vitest.dev/guide/testing-types#run-typechecking)하려면 `--typecheck` 플래그를 전달하는 것을 잊지 마세요.
:::

- **Type:** `<T>(value: T): void`

제공된 제네릭과 인자 타입이 동일한지 손쉽게 단언하기 위해, 이 함수를 [`expectTypeOf`](https://vitest.dev/api/expect-typeof)의 대안으로 사용할 수 있습니다.

```ts
import { assertType } from "vitest";

function concat(a: string, b: string): string;
function concat(a: number, b: number): number;
function concat(a: string | number, b: string | number): string | number;

assertType<string>(concat("a", "b"));
assertType<number>(concat(1, 2));
// @ts-expect-error wrong types
assertType(concat("a", 2));
```
