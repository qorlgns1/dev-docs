---
title: "타입 테스트"
description: "Vitest는  또는  문법을 사용해 타입에 대한 테스트를 작성할 수 있게 해줍니다. 기본적으로  파일 안의 모든 테스트는 타입 테스트로 간주되지만,  설정 옵션으로 변경할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/testing-types

# 타입 테스트

::: tip 샘플 프로젝트

[GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/typecheck) - [온라인 실행](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/typecheck?initialPath=__vitest__/)

:::

Vitest는 `expectTypeOf` 또는 `assertType` 문법을 사용해 타입에 대한 테스트를 작성할 수 있게 해줍니다. 기본적으로 `*.test-d.ts` 파일 안의 모든 테스트는 타입 테스트로 간주되지만, [`typecheck.include`](https://vitest.dev/config/#typecheck-include) 설정 옵션으로 변경할 수 있습니다.

내부적으로 Vitest는 설정에 따라 `tsc` 또는 `vue-tsc`를 호출하고, 그 결과를 파싱합니다. 문제가 발견되면 Vitest는 소스 코드의 타입 에러도 출력합니다. 이 동작은 [`typecheck.ignoreSourceErrors`](https://vitest.dev/config/#typecheck-ignoresourceerrors) 설정 옵션으로 비활성화할 수 있습니다.

Vitest는 이 파일들을 실행하지 않고, 컴파일러가 정적으로 분석만 한다는 점을 기억하세요. 즉, 동적 이름이나 `test.each`, `test.for`를 사용하면 테스트 이름이 평가되지 않고 작성된 그대로 표시됩니다.

::: warning
Vitest 2.1 이전에는 `typecheck.include`가 `include` 패턴을 덮어썼기 때문에, 런타임 테스트가 실제로 실행되지 않고 타입 체크만 수행되었습니다.

Vitest 2.1부터는 `include`와 `typecheck.include`가 겹치는 경우, Vitest가 타입 테스트와 런타임 테스트를 별도의 항목으로 보고합니다.
:::

`--allowOnly`, `-t` 같은 CLI 플래그도 타입 체크에서 지원됩니다.

```ts [mount.test-d.ts]
import { assertType, expectTypeOf } from "vitest";
import { mount } from "./mount.js";

test("my types work properly", () => {
  expectTypeOf(mount).toBeFunction();
  expectTypeOf(mount).parameter(0).toExtend<{ name: string }>();

  // @ts-expect-error name is a string
  assertType(mount({ name: 42 }));
});
```

테스트 파일 내부에서 발생한 모든 타입 에러는 테스트 에러로 처리되므로, 프로젝트의 타입을 테스트하기 위해 원하는 타입 트릭을 자유롭게 사용할 수 있습니다.

사용 가능한 matcher 목록은 [API 섹션](https://vitest.dev/api/expect-typeof)에서 확인할 수 있습니다.

## 에러 읽기

`expectTypeOf` API를 사용한다면, 에러 메시지에 대해서는 [expect-type 문서의 error messages](https://github.com/mmkal/expect-type#error-messages)를 참고하세요.

타입이 일치하지 않을 때 `.toEqualTypeOf`와 `.toExtend`는 가능한 한 실행 가능한 에러 메시지를 만들기 위해 특수 헬퍼 타입을 사용합니다. 다만 이를 이해할 때 약간의 뉘앙스가 있습니다. 단언은 "플루언트" 방식으로 작성되므로, 실패는 "actual" 타입이 아니라 "expected" 타입 기준으로 봐야 합니다(`expect<Actual>().toEqualTypeOf<Expected>()`). 그래서 타입 에러가 다소 헷갈릴 수 있는데, 이 라이브러리는 기대값이 무엇인지 명시적으로 보여주기 위해 `MismatchInfo` 타입을 생성합니다. 예를 들어:

```ts
expectTypeOf({ a: 1 }).toEqualTypeOf<{ a: string }>();
```

이는 실패하는 단언입니다. `{a: 1}`의 타입은 `{a: number}`이지 `{a: string}`이 아니기 때문입니다. 이 경우 에러 메시지는 대략 다음과 같이 표시됩니다:

```
test/test.ts:999:999 - error TS2344: Type '{ a: string; }' does not satisfy the constraint '{ a: \\"Expected: string, Actual: number\\"; }'.
  Types of property 'a' are incompatible.
    Type 'string' is not assignable to type '\\"Expected: string, Actual: number\\"'.

999 expectTypeOf({a: 1}).toEqualTypeOf<{a: string}>()
```

보고되는 타입 제약은 "expected"와 "actual" 타입을 모두 명시하는 사람이 읽기 쉬운 메시지라는 점에 주의하세요. `Types of property 'a' are incompatible // Type 'string' is not assignable to type "Expected: string, Actual: number"`라는 문장을 문자 그대로 해석하기보다, 속성 이름(`'a'`)과 메시지(`Expected: string, Actual: number`)를 보면 됩니다. 대부분의 경우 이것만으로 무엇이 잘못됐는지 알 수 있습니다. 물론 매우 복잡한 타입은 디버깅에 더 많은 노력이 필요하고, 실험이 필요할 수 있습니다. 에러 메시지가 실제로 오해를 일으킨다면 [이슈를 등록](https://github.com/mmkal/expect-type)해 주세요.

`toBe...` 메서드(`toBeString`, `toBeNumber`, `toBeVoid` 등)는 테스트 대상 `Actual` 타입이 맞지 않으면 호출 불가능한 타입으로 해석되며 실패합니다. 예를 들어 `expectTypeOf(1).toBeString()` 같은 단언 실패는 대략 다음과 같이 보입니다:

```
test/test.ts:999:999 - error TS2349: This expression is not callable.
  Type 'ExpectString<number>' has no call signatures.

999 expectTypeOf(1).toBeString()
                    ~~~~~~~~~~
```

`This expression is not callable` 부분은 크게 도움이 되지 않고, 의미 있는 에러는 다음 줄의 `Type 'ExpectString<number> has no call signatures`입니다. 이는 본질적으로 number를 전달했지만 string이어야 한다고 단언했다는 뜻입니다.

TypeScript가 ["throw" types](https://github.com/microsoft/TypeScript/pull/40468)를 지원하면 이런 에러 메시지를 훨씬 개선할 수 있습니다. 그전까지는 어느 정도 눈을 가늘게 뜨고 해석해야 합니다.

#### 구체적인 "expected" 객체 vs typearg

다음과 같은 단언의 에러 메시지는:

```ts
expectTypeOf({ a: 1 }).toEqualTypeOf({ a: "" });
```

다음과 같은 단언보다 덜 유용합니다:

```ts
expectTypeOf({ a: 1 }).toEqualTypeOf<{ a: string }>();
```

이는 TypeScript 컴파일러가 `.toEqualTypeOf({a: ''})` 스타일에서 typearg를 추론해야 하고, 이 라이브러리는 이를 제네릭 `Mismatch` 타입과 비교하는 방식으로만 실패 표시를 할 수 있기 때문입니다. 가능하면 `.toEqualTypeOf`와 `.toExtend`에서는 구체 타입보다 typearg를 사용하세요. 두 구체 타입을 비교하는 편이 훨씬 편리하다면 `typeof`를 사용할 수 있습니다:

```ts
const one = valueFromFunctionOne({ some: { complex: inputs } });
const two = valueFromFunctionTwo({ some: { other: inputs } });

expectTypeOf(one).toEqualTypeOf<typeof two>();
```

`expectTypeOf` API와 에러 해석이 어렵다면, 더 단순한 `assertType` API를 항상 사용할 수 있습니다:

```ts
const answer = 42;

assertType<number>(answer);
// @ts-expect-error answer is not a string
assertType<string>(answer);
```

::: tip
`@ts-expect-error` 문법을 사용할 때는 오타가 없는지 확인하는 것이 좋습니다. 이를 위해 타입 파일을 [`test.include`](https://vitest.dev/config/#include) 설정 옵션에 포함하면, Vitest가 이 테스트들도 실제로 *실행*하고 `ReferenceError`로 실패하게 할 수 있습니다.

다음 코드는 에러를 기대하기 때문에 통과하지만, “answer”에 오타가 있어 false positive 에러입니다:

```ts
// @ts-expect-error answer is not a string
assertType<string>(answr);
```

:::

## 타입 체크 실행

타입 체크를 활성화하려면 `package.json`의 Vitest 명령에 [`--typecheck`](https://vitest.dev/config/#typecheck) 플래그를 추가하면 됩니다:

```json [package.json]
{
  "scripts": {
    "test": "vitest --typecheck"
  }
}
```

이제 타입 체크를 실행할 수 있습니다:

::: code-group

```bash [npm]
npm run test
```

```bash [yarn]
yarn test
```

```bash [pnpm]
pnpm run test
```

```bash [bun]
bun test
```

:::

Vitest는 설정에 따라 `tsc --noEmit` 또는 `vue-tsc --noEmit`를 사용하므로, 파이프라인에서 해당 스크립트들을 제거할 수 있습니다.
