---
title: "sequence"
description: "테스트를 정렬하는 방법에 대한 옵션입니다."
---

출처 URL: https://vitest.dev/config/sequence

# sequence

- **Type**: `{ sequencer?, shuffle?, seed?, hooks?, setupFiles?, groupOrder }`

테스트를 정렬하는 방법에 대한 옵션입니다.

점 표기법을 사용해 CLI에 sequence 옵션을 전달할 수 있습니다:

```sh
npx vitest --sequence.shuffle --sequence.seed=1000
```

## sequence.sequencer

- **Type**: `TestSequencerConstructor`
- **Default**: `BaseSequencer`

샤딩과 정렬을 위한 메서드를 정의하는 사용자 지정 클래스입니다. `sort`와 `shard` 메서드 중 하나만 재정의하면 되는 경우 `vitest/node`의 `BaseSequencer`를 확장할 수 있지만, 두 메서드는 모두 존재해야 합니다.

샤딩은 정렬 전에 수행되며, `--shard` 옵션이 제공된 경우에만 적용됩니다.

[`sequencer.groupOrder`](#grouporder)가 지정된 경우, 시퀀서는 각 그룹과 풀마다 한 번씩 호출됩니다.

## sequence.groupOrder

- **Type:** `number`
- **Default:** `0`

여러 [projects](https://vitest.dev/guide/projects)를 사용할 때 이 프로젝트의 테스트 실행 순서를 제어합니다.

- 동일한 group order 번호를 가진 프로젝트는 함께 실행되며, 그룹은 낮은 번호에서 높은 번호 순으로 실행됩니다.
- 이 옵션을 설정하지 않으면 모든 프로젝트가 병렬로 실행됩니다.
- 여러 프로젝트가 같은 group order를 사용하면 동시에 실행됩니다.

이 설정은 프로젝트 실행 순서에만 영향을 주며, 프로젝트 내부 테스트 순서에는 영향을 주지 않습니다.
테스트 격리나 프로젝트 내부 테스트 순서를 제어하려면 [`isolate`](#isolate) 및 [`sequence.sequencer`](#sequence-sequencer) 옵션을 사용하세요.

::: details 예시
다음 예시를 보세요:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        test: {
          name: "slow",
          sequence: {
            groupOrder: 0,
          },
        },
      },
      {
        test: {
          name: "fast",
          sequence: {
            groupOrder: 0,
          },
        },
      },
      {
        test: {
          name: "flaky",
          sequence: {
            groupOrder: 1,
          },
        },
      },
    ],
  },
});
```

이 프로젝트들의 테스트는 다음 순서로 실행됩니다:

```
 0. slow  |
          |> running together
 0. fast  |

 1. flaky |> runs after slow and fast alone
```

:::

## sequence.shuffle

- **Type**: `boolean | { files?, tests? }`
- **Default**: `false`
- **CLI**: `--sequence.shuffle`, `--sequence.shuffle=false`

파일과 테스트를 무작위로 실행하려면 이 옵션 또는 CLI 인자 [`--sequence.shuffle`](https://vitest.dev/guide/cli)을 활성화할 수 있습니다.

Vitest는 일반적으로 캐시를 사용해 테스트를 정렬하므로, 오래 걸리는 테스트를 먼저 시작해 전체 실행 시간을 단축합니다. 파일과 테스트를 무작위 순서로 실행하면 이 성능 이점을 잃게 되지만, 이전 테스트 실행에 우연히 의존하는 테스트를 추적하는 데는 유용할 수 있습니다.

### sequence.shuffle.files {#sequence-shuffle-files}

- **Type**: `boolean`
- **Default**: `false`
- **CLI**: `--sequence.shuffle.files`, `--sequence.shuffle.files=false`

파일 순서를 무작위화할지 여부입니다. 이 옵션을 활성화하면 오래 걸리는 테스트가 먼저 시작되지 않습니다.

### sequence.shuffle.tests {#sequence-shuffle-tests}

- **Type**: `boolean`
- **Default**: `false`
- **CLI**: `--sequence.shuffle.tests`, `--sequence.shuffle.tests=false`

테스트 순서를 무작위화할지 여부입니다.

## sequence.concurrent {#sequence-concurrent}

- **Type**: `boolean`
- **Default**: `false`
- **CLI**: `--sequence.concurrent`, `--sequence.concurrent=false`

테스트를 병렬로 실행하려면 이 옵션 또는 CLI 인자 [`--sequence.concurrent`](https://vitest.dev/guide/cli)을 활성화할 수 있습니다.

::: warning
`sequence.concurrent`와 `expect.requireAssertions`를 `true`로 설정해 테스트를 실행할 때는 전역 expect 대신 [local expect](https://vitest.dev/guide/test-context.html#expect)를 사용해야 합니다. 그렇지 않으면 [일부 상황 (#8469)](https://github.com/vitest-dev/vitest/issues/8469)에서 false negative가 발생할 수 있습니다.
:::

## sequence.seed

- **Type**: `number`
- **Default**: `Date.now()`
- **CLI**: `--sequence.seed=1000`

테스트가 무작위 순서로 실행될 때 무작위화 시드를 설정합니다.

## sequence.hooks

- **Type**: `'stack' | 'list' | 'parallel'`
- **Default**: `'stack'`
- **CLI**: `--sequence.hooks=<value>`

hooks 실행 순서를 변경합니다.

- `stack`은 "after" hooks를 역순으로 정렬하며, "before" hooks는 정의된 순서대로 실행됩니다.
- `list`는 모든 hooks를 정의된 순서대로 정렬합니다.
- `parallel`은 단일 그룹 내 hooks를 병렬로 실행합니다(상위 suite의 hooks는 여전히 현재 suite의 hooks보다 먼저 실행됩니다).

::: tip
이 옵션은 [`onTestFinished`](https://vitest.dev/api/#ontestfinished)에 영향을 주지 않습니다. 이는 항상 역순으로 호출됩니다.
:::

## sequence.setupFiles {#sequence-setupfiles}

- **Type**: `'list' | 'parallel'`
- **Default**: `'parallel'`
- **CLI**: `--sequence.setupFiles=<value>`

setup files 실행 순서를 변경합니다.

- `list`는 setup files를 정의된 순서대로 실행합니다.
- `parallel`은 setup files를 병렬로 실행합니다.
