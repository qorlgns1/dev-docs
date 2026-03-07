---
title: "expect"
description: "모든 테스트 시작 시 를 호출하는 것과 같습니다. 이렇게 하면 어떤 테스트도 실수로 통과하지 않도록 보장합니다."
---

# expect

- **타입:** `ExpectOptions`

## expect.requireAssertions

- **타입:** `boolean`
- **기본값:** `false`

모든 테스트 시작 시 [`expect.hasAssertions()`](https://vitest.dev/api/expect#expect-hasassertions)를 호출하는 것과 같습니다. 이렇게 하면 어떤 테스트도 실수로 통과하지 않도록 보장합니다.

::: tip
이 기능은 Vitest의 `expect`에서만 동작합니다. `assert` 또는 `.should` 단언을 사용하면 카운트되지 않으며, `expect` 단언이 없어서 테스트가 실패합니다.

`vi.setConfig({ expect: { requireAssertions: false } })`를 호출해 이 값을 변경할 수 있습니다. 설정은 `vi.resetConfig`를 수동으로 호출할 때까지 이후의 모든 `expect` 호출에 적용됩니다.
:::

::: warning
`sequence.concurrent`와 `expect.requireAssertions`를 `true`로 설정해 테스트를 실행할 때는 전역 `expect` 대신 [local expect](https://vitest.dev/guide/test-context.html#expect)를 사용해야 합니다. 그렇지 않으면 [일부 상황(#8469)](https://github.com/vitest-dev/vitest/issues/8469)에서 false negative가 발생할 수 있습니다.
:::

## expect.poll

[`expect.poll`](https://vitest.dev/api/expect#poll)의 전역 설정 옵션입니다. 이는 `expect.poll(condition, options)`에 전달할 수 있는 옵션과 동일합니다.

### expect.poll.interval

- **타입:** `number`
- **기본값:** `50`

밀리초 단위의 폴링 간격

### expect.poll.timeout

- **타입:** `number`
- **기본값:** `1000`

밀리초 단위의 폴링 타임아웃
