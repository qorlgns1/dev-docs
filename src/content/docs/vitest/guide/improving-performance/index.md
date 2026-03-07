---
title: "성능 개선"
description: "기본적으로 Vitest는 pool을 기반으로 모든 테스트 파일을 격리된 환경에서 실행합니다:"
---

출처 URL: https://vitest.dev/guide/improving-performance

# 성능 개선

## 테스트 격리

기본적으로 Vitest는 [pool](https://vitest.dev/config/#pool)을 기반으로 모든 테스트 파일을 격리된 환경에서 실행합니다:

- `threads` pool은 각 테스트 파일을 별도의 [`Worker`](https://nodejs.org/api/worker_threads.html#class-worker)에서 실행합니다.
- `forks` pool은 각 테스트 파일을 별도의 [forked child process](https://nodejs.org/api/child_process.html#child_processforkmodulepath-args-options)에서 실행합니다.
- `vmThreads` pool은 각 테스트 파일을 별도의 [VM context](https://nodejs.org/api/vm.html#vmcreatecontextcontextobject-options)에서 실행하지만, 병렬 처리를 위해 worker를 사용합니다.

이 방식은 테스트 시간을 크게 늘릴 수 있으며, 사이드 이펙트에 의존하지 않고 상태 정리를 적절히 수행하는 프로젝트(보통 `node` environment를 사용하는 프로젝트)에선 바람직하지 않을 수 있습니다. 이런 경우 격리를 비활성화하면 테스트 속도를 개선할 수 있습니다. 이를 위해 CLI에 `--no-isolate` flag를 전달하거나, config에서 [`test.isolate`](https://vitest.dev/config/#isolate) property를 `false`로 설정할 수 있습니다.

::: code-group

```bash [CLI]
vitest --no-isolate
```

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    isolate: false,
  },
});
```

:::

`projects`를 사용하면 특정 파일에 대해서만 격리를 비활성화할 수도 있습니다:

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        name: "Isolated",
        isolate: true, // (default value)
        exclude: ["**.non-isolated.test.ts"],
      },
      {
        name: "Non-isolated",
        isolate: false,
        include: ["**.non-isolated.test.ts"],
      },
    ],
  },
});
```

:::tip
`vmThreads` pool을 사용하는 경우 격리를 비활성화할 수 없습니다. 테스트 성능을 개선하려면 대신 `threads` pool을 사용하세요.
:::

일부 프로젝트에서는 시작 시간을 개선하기 위해 병렬 처리 자체를 비활성화하는 것이 더 유리할 수도 있습니다. 이를 위해 CLI에 `--no-file-parallelism` flag를 전달하거나, config에서 [`test.fileParallelism`](https://vitest.dev/config/#fileparallelism) property를 `false`로 설정하세요.

::: code-group

```bash [CLI]
vitest --no-file-parallelism
```

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    fileParallelism: false,
  },
});
```

:::

## 디렉터리 검색 제한

Vitest가 파일을 검색할 때 [`test.dir`](https://vitest.dev/config/#test-dir) option으로 작업 디렉터리를 제한할 수 있습니다. 루트 디렉터리에 관련 없는 폴더와 파일이 많은 경우 검색 속도가 더 빨라질 수 있습니다.

## Pool

기본적으로 Vitest는 `pool: 'forks'`로 테스트를 실행합니다. `'forks'` pool은 호환성 문제([hanging process](https://vitest.dev/guide/common-errors.html#failed-to-terminate-worker), [segfaults](https://vitest.dev/guide/common-errors.html#segfaults-and-native-code-errors))에 더 유리하지만, 대규모 프로젝트에서는 `pool: 'threads'`보다 약간 느릴 수 있습니다.

config에서 `pool` option을 변경해 테스트 실행 시간을 개선해볼 수 있습니다:

::: code-group

```bash [CLI]
vitest --pool=threads
```

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    pool: "threads",
  },
});
```

:::

## 샤딩

테스트 샤딩은 테스트 스위트를 그룹, 즉 shard로 분할하는 과정입니다. 대규모 테스트 스위트가 있고 여러 머신에서 해당 스위트의 하위 집합을 동시에 실행할 수 있을 때 유용합니다.

여러 번의 실행에 걸쳐 Vitest 테스트를 분할하려면 [`--shard`](https://vitest.dev/guide/cli#shard) option을 [`--reporter=blob`](https://vitest.dev/guide/reporters#blob-reporter) option과 함께 사용하세요:

```sh
vitest run --reporter=blob --shard=1/3 # 1st machine
vitest run --reporter=blob --shard=2/3 # 2nd machine
vitest run --reporter=blob --shard=3/3 # 3rd machine
```

> Vitest는 테스트 케이스가 아니라 *test files*를 shard로 분할합니다. 테스트 파일이 1000개라면 `--shard=1/4` option은 각 파일의 테스트 케이스 수와 관계없이 250개의 테스트 파일을 실행합니다.

각 머신에서 `.vitest-reports` 디렉터리에 저장된 결과를 수집한 뒤 [`--merge-reports`](https://vitest.dev/guide/cli#merge-reports) option으로 병합하세요:

```sh
vitest run --merge-reports
```

::: details GitHub Actions 예시
이 설정은 https://github.com/vitest-tests/test-sharding 에서도 사용됩니다.

```yaml
# Inspired from https://playwright.dev/docs/test-sharding
name: Tests
on:
  push:
    branches:
      - main
jobs:
  tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shardIndex: [1, 2, 3, 4]
        shardTotal: [4]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install pnpm
        uses: pnpm/action-setup@a7487c7e89a18df4991f7f222e4898a00d66ddda # v4.1.0

      - name: Install dependencies
        run: pnpm i

      - name: Run tests
        run: pnpm run test --reporter=blob --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}

      - name: Upload blob report to GitHub Actions Artifacts
        if: ${{ !cancelled() }}
        uses: actions/upload-artifact@v4
        with:
          name: blob-report-${{ matrix.shardIndex }}
          path: .vitest-reports/*
          include-hidden-files: true
          retention-days: 1

  merge-reports:
    if: ${{ !cancelled() }}
    needs: [tests]

    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install pnpm
        uses: pnpm/action-setup@a7487c7e89a18df4991f7f222e4898a00d66ddda # v4.1.0

      - name: Install dependencies
        run: pnpm i

      - name: Download blob reports from GitHub Actions Artifacts
        uses: actions/download-artifact@v4
        with:
          path: .vitest-reports
          pattern: blob-report-*
          merge-multiple: true

      - name: Merge reports
        run: npx vitest --merge-reports
```

:::

:::tip
CPU 코어 수가 많은 머신에서는 테스트 샤딩이 더욱 유용할 수 있습니다.

Vitest는 main thread에서 단 하나의 Vite server만 실행합니다. 나머지 thread들은 테스트 파일 실행에 사용됩니다.
CPU 코어 수가 많은 머신에서는 main thread가 thread들에서 들어오는 모든 요청을 처리하지 못해 병목이 될 수 있습니다. 예를 들어 CPU가 32개인 머신에서는 main thread가 31개 테스트 thread에서 오는 부하를 처리해야 합니다.

main thread의 Vite server 부하를 줄이려면 테스트 샤딩을 사용할 수 있습니다. 부하를 여러 Vite server로 분산할 수 있습니다.

```sh
# Example for splitting tests on 32 CPU to 4 shards.
# As each process needs 1 main thread, there's 7 threads for test runners (1+7)*4 = 32
# Use VITEST_MAX_WORKERS:
VITEST_MAX_WORKERS=7 vitest run --reporter=blob --shard=1/4 & \
VITEST_MAX_WORKERS=7 vitest run --reporter=blob --shard=2/4 & \
VITEST_MAX_WORKERS=7 vitest run --reporter=blob --shard=3/4 & \
VITEST_MAX_WORKERS=7 vitest run --reporter=blob --shard=4/4 & \
wait # https://man7.org/linux/man-pages/man2/waitpid.2.html

vitest run --merge-reports
```

:::
