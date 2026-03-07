---
title: "TestCollection"
description: "은 스위트 또는 모듈에서 최상위 suite와 test의 컬렉션을 나타냅니다. 또한 자기 자신을 순회할 수 있는 유용한 메서드도 제공합니다."
---

출처 URL: https://vitest.dev/api/advanced/test-collection

# TestCollection

`TestCollection`은 스위트 또는 모듈에서 최상위 [suite](https://vitest.dev/api/advanced/test-suite)와 [test](https://vitest.dev/api/advanced/test-case)의 컬렉션을 나타냅니다. 또한 자기 자신을 순회할 수 있는 유용한 메서드도 제공합니다.

::: info
대부분의 메서드는 컬렉션의 모든 항목이 필요하지 않은 경우 더 나은 성능을 위해 배열 대신 이터레이터를 반환합니다. 배열로 작업하는 것을 선호한다면 이터레이터를 펼쳐 사용할 수 있습니다: `[...children.allSuites()]`.

또한 컬렉션 자체도 이터레이터라는 점에 유의하세요:

```ts
for (const child of module.children) {
  console.log(child.type, child.name);
}
```

:::

## size

컬렉션에 있는 테스트와 스위트의 개수입니다.

::: warning
이 숫자에는 최상위 수준의 테스트와 스위트만 포함되며, 중첩된 스위트와 테스트는 포함되지 않습니다.
:::

## at

```ts
function at(index: number): TestCase | TestSuite | undefined;
```

특정 인덱스에 있는 테스트 또는 스위트를 반환합니다. 이 메서드는 음수 인덱스를 허용합니다.

## array

```ts
function array(): (TestCase | TestSuite)[];
```

동일한 컬렉션을 배열로 반환합니다. 이는 `TaskCollection` 구현에서 지원되지 않는 `map`, `filter` 같은 `Array` 메서드를 사용하려는 경우에 유용합니다.

## allSuites

```ts
function allSuites(): Generator<TestSuite, undefined, void>;
```

이 컬렉션과 그 하위 항목에 포함된 모든 스위트를 필터링합니다.

```ts
for (const suite of module.children.allSuites()) {
  if (suite.errors().length) {
    console.log("failed to collect", suite.errors());
  }
}
```

## allTests

```ts
function allTests(state?: TestState): Generator<TestCase, undefined, void>;
```

이 컬렉션과 그 하위 항목에 포함된 모든 테스트를 필터링합니다.

```ts
for (const test of module.children.allTests()) {
  if (test.result().state === "pending") {
    console.log("test", test.fullName, "did not finish");
  }
}
```

`state` 값을 전달해 상태별로 테스트를 필터링할 수 있습니다.

## tests

```ts
function tests(state?: TestState): Generator<TestCase, undefined, void>;
```

이 컬렉션에 포함된 테스트만 필터링합니다. `state` 값을 전달해 상태별로 테스트를 필터링할 수 있습니다.

## suites

```ts
function suites(): Generator<TestSuite, undefined, void>;
```

이 컬렉션에 포함된 스위트만 필터링합니다.
. `state` 값을 전달해 상태별로 테스트를 필터링할 수 있습니다.

## suites

```ts
function suites(): Generator<TestSuite, undefined, void>;
```

이 컬렉션에 포함된 스위트만 필터링합니다.
