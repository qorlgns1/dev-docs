---
title: "Matcher 확장하기"
description: "Vitest는 Chai와 Jest 모두와 호환되므로, 선호에 따라  API 또는 를 사용할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/extending-matchers

# Matcher 확장하기

Vitest는 Chai와 Jest 모두와 호환되므로, 선호에 따라 `chai.use` API 또는 `expect.extend`를 사용할 수 있습니다.

이 가이드에서는 `expect.extend`로 matcher를 확장하는 방법을 살펴봅니다. Chai API에 관심이 있다면 [가이드](https://www.chaijs.com/guide/plugins/)를 확인하세요.

기본 matcher를 확장하려면, matcher를 포함한 객체를 `expect.extend`에 전달하세요.

```ts
expect.extend({
  toBeFoo(received, expected) {
    const { isNot } = this;
    return {
      // do not alter your "pass" based on isNot. Vitest does it for you
      pass: received === "foo",
      message: () => `${received} is${isNot ? " not" : ""} foo`,
    };
  },
});
```

TypeScript를 사용하는 경우, ambient declaration 파일(예: `vitest.d.ts`)에서 아래 코드로 기본 `Assertion` 인터페이스를 확장할 수 있습니다.

::: code-group

```ts [<Version>3.2.0</Version>]
import "vitest";

interface CustomMatchers<R = unknown> {
  toBeFoo: () => R;
}

declare module "vitest" {
  interface Matchers<T = any> extends CustomMatchers<T> {}
}
```

```ts [<Version>3.0.0</Version>]
import "vitest";

interface CustomMatchers<R = unknown> {
  toBeFoo: () => R;
}

declare module "vitest" {
  interface Assertion<T = any> extends CustomMatchers<T> {}
  interface AsymmetricMatchersContaining extends CustomMatchers {}
}
```

:::

::: tip
Vitest 3.2부터는 `Matchers` 인터페이스를 확장해 `expect.extend`, `expect().*`, `expect.*` 메서드에서 동시에 타입 안전한 assertion을 사용할 수 있습니다. 이전에는 각각에 대해 별도의 인터페이스를 정의해야 했습니다.
:::

::: warning
ambient declaration 파일을 `tsconfig.json`에 포함하는 것을 잊지 마세요.
:::

matcher의 반환값은 다음 인터페이스와 호환되어야 합니다.

```ts
interface ExpectationResult {
  pass: boolean;
  message: () => string;
  // If you pass these, they will automatically appear inside a diff when
  // the matcher does not pass, so you don't need to print the diff yourself
  actual?: unknown;
  expected?: unknown;
}
```

::: warning
비동기 matcher를 만들었다면, 테스트 자체에서 결과를 `await`하는 것을 잊지 마세요 (`await expect('foo').toBeFoo()`)::

```ts
expect.extend({
  async toBeAsyncAssertion() {
    // ...
  },
});

await expect().toBeAsyncAssertion();
```

:::

matcher 함수의 첫 번째 인수는 전달된 값(`expect(received)` 안의 값)입니다. 나머지는 matcher에 직접 전달된 인수입니다.

matcher 함수는 다음 속성을 가진 `this` 컨텍스트에 접근할 수 있습니다.

### `isNot`

matcher가 `not`에 대해 호출된 경우 true를 반환합니다 (`expect(received).not.toBeFoo()`).

### `promise`

matcher가 `resolved/rejected`에서 호출되었다면 이 값에는 modifier 이름이 들어갑니다. 그렇지 않으면 빈 문자열입니다.

### `equals`

두 값을 비교할 수 있는 유틸리티 함수입니다. 값이 같으면 `true`, 그렇지 않으면 `false`를 반환합니다. 이 함수는 거의 모든 matcher에서 내부적으로 사용됩니다. 기본적으로 asymmetric matcher가 포함된 객체도 지원합니다.

### `utils`

메시지를 표시할 때 사용할 수 있는 유틸리티 함수 집합이 들어 있습니다.

`this` 컨텍스트에는 현재 테스트 정보도 포함됩니다. `expect.getState()`를 호출해서도 가져올 수 있습니다. 가장 유용한 속성은 다음과 같습니다.

### `currentTestName`

현재 테스트의 전체 이름(`describe` 블록 포함)입니다.

### `task` 4.0.11 {#task}

가능한 경우 [the `Test` runner task](https://vitest.dev/api/advanced/runner#tasks)에 대한 참조를 포함합니다.

::: warning
동시성 테스트에서 전역 `expect`를 사용할 경우 `this.task`는 `undefined`입니다. 커스텀 matcher에서 `task`를 사용할 수 있도록 `context.expect`를 대신 사용하세요.
:::

### `testPath`

현재 테스트의 경로입니다.
