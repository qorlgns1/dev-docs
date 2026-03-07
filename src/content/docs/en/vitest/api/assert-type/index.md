---
title: "assertType"
description: "During runtime this function doesn't do anything. To enable typechecking, don't forget to pass down  flag."
---

Source URL: https://vitest.dev/api/assert-type

# assertType

::: warning
During runtime this function doesn't do anything. To [enable typechecking](https://vitest.dev/guide/testing-types#run-typechecking), don't forget to pass down `--typecheck` flag.
:::

- **Type:** `<T>(value: T): void`

You can use this function as an alternative for [`expectTypeOf`](https://vitest.dev/api/expect-typeof) to easily assert that the argument type is equal to the generic provided.

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
