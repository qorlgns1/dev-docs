---
title: "테스트 성능 프로파일링"
description: "Vitest를 실행하면 테스트에 대한 여러 시간 지표를 보고합니다:"
---

출처 URL: https://vitest.dev/guide/profiling-test-performance

# 테스트 성능 프로파일링

Vitest를 실행하면 테스트에 대한 여러 시간 지표를 보고합니다:

> ```bash
> RUN  v2.1.1 /x/vitest/examples/profiling
>
> ✓ test/prime-number.test.ts (1) 4517ms
>   ✓ generate prime number 4517ms
>
> Test Files  1 passed (1)
>      Tests  1 passed (1)
>   Start at  09:32:53
>   Duration  4.80s (transform 44ms, setup 0ms, import 35ms, tests 4.52s, environment 0ms)
>   # Time metrics ^^
> ```

- Transform: 파일 변환에 사용된 시간입니다. [File Transform](#file-transform)을 참고하세요.
- Setup: [`setupFiles`](https://vitest.dev/config/setupfiles) 파일 실행에 사용된 시간입니다.
- Import: 테스트 파일과 해당 의존성을 가져오는 데 걸린 시간입니다. 여기에는 모든 테스트를 수집하는 시간도 포함됩니다. 단, 테스트 내부의 동적 import는 포함되지 않습니다.
- Tests: 실제 테스트 케이스 실행에 사용된 시간입니다.
- Environment: 테스트 [`environment`](https://vitest.dev/config/#environment)(예: JSDOM) 설정에 사용된 시간입니다.

## Test Runner

테스트 실행 시간이 긴 경우, 테스트 러너의 프로파일을 생성할 수 있습니다. 다음 옵션은 NodeJS 문서를 참고하세요:

- `--cpu-prof`
- `--heap-prof`
- `--prof`

:::warning
`--prof` 옵션은 `node:worker_threads` 제한으로 인해 `pool: 'threads'`와 함께 동작하지 않습니다.
:::

이 옵션들을 Vitest의 테스트 러너에 전달하려면, Vitest 설정에서 `execArgv`를 정의하세요:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    fileParallelism: false,
    execArgv: [
      "--cpu-prof",
      "--cpu-prof-dir=test-runner-profile",
      "--heap-prof",
      "--heap-prof-dir=test-runner-profile",
    ],
  },
});
```

테스트 실행 후 `test-runner-profile/*.cpuprofile` 및 `test-runner-profile/*.heapprofile` 파일이 생성되어야 합니다. 이 파일 분석 방법은 [Inspecting profiling records](#inspecting-profiling-records)를 참고하세요.

예시는 [Profiling | Examples](https://github.com/vitest-dev/vitest/tree/main/examples/profiling)를 참고하세요.

## Main Thread

메인 스레드 프로파일링은 Vitest의 Vite 사용 방식과 [`globalSetup`](https://vitest.dev/config/#globalsetup) 파일을 디버깅할 때 유용합니다.
또한 이곳에서 Vite 플러그인이 실행됩니다.

:::tip
Vite 관련 프로파일링 팁은 [Performance | Vite](https://vitejs.dev/guide/performance.html)를 참고하세요.

Vite 플러그인 성능 프로파일링에는 [`vite-plugin-inspect`](https://github.com/antfu-collective/vite-plugin-inspect)를 권장합니다.
:::

이를 위해서는 Vitest를 실행하는 Node 프로세스에 인자를 전달해야 합니다.

```bash
$ node --cpu-prof --cpu-prof-dir=main-profile ./node_modules/vitest/vitest.mjs --run
#      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                  ^^^^^
#               NodeJS arguments                                           Vitest arguments
```

테스트 실행 후 `main-profile/*.cpuprofile` 파일이 생성되어야 합니다. 이 파일 분석 방법은 [Inspecting profiling records](#inspecting-profiling-records)를 참고하세요.

## File Transform

이 프로파일링 전략은 [barrel files](https://vitejs.dev/guide/performance.html#avoid-barrel-files)로 인해 발생하는 불필요한 변환을 식별하는 데 좋은 방법입니다.
로그에 테스트 실행 시 로드되면 안 되는 파일이 포함되어 있다면, 파일을 불필요하게 import하는 barrel file이 있을 수 있습니다.

또한 [Vitest UI](https://vitest.dev/guide/ui)를 사용해 barrel file로 인해 발생하는 느려짐을 디버깅할 수 있습니다.
아래 예시는 barrel file 없이 파일을 import했을 때 변환되는 파일 수가 약 85% 줄어드는 것을 보여줍니다.

::: code-group

```[File tree]
├── src
│   └── utils
│       ├── currency.ts
│       ├── formatters.ts  <-- File to test
│       ├── index.ts
│       ├── location.ts
│       ├── math.ts
│       ├── time.ts
│       └── users.ts
├── test
│   └── formatters.test.ts
└── vitest.config.ts
```

```ts [example.test.ts]
import { expect, test } from "vitest";
import { formatter } from "../src/utils"; // [!code --]
import { formatter } from "../src/utils/formatters"; // [!code ++]

test("formatter works", () => {
  expect(formatter).not.toThrow();
});
```

:::

파일이 어떻게 변환되는지 확인하려면 `VITEST_DEBUG_DUMP` 환경 변수를 사용해 변환된 파일을 파일 시스템에 기록할 수 있습니다:

```bash
$ VITEST_DEBUG_DUMP=true vitest --run

 RUN  v2.1.1 /x/vitest/examples/profiling
...

$ ls .vitest-dump/
_x_examples_profiling_global-setup_ts-1292904907.js
_x_examples_profiling_test_prime-number_test_ts-1413378098.js
_src_prime-number_ts-525172412.js
```

## Code Coverage

프로젝트에서 코드 커버리지 생성이 느리다면 `DEBUG=vitest:coverage` 환경 변수를 사용해 성능 로깅을 활성화할 수 있습니다.

```bash
$ DEBUG=vitest:coverage vitest --run --coverage

 RUN  v3.1.1 /x/vitest-example

  vitest:coverage Reading coverage results 2/2
  vitest:coverage Converting 1/2
  vitest:coverage 4 ms /x/src/multiply.ts
  vitest:coverage Converting 2/2
  vitest:coverage 552 ms /x/src/add.ts
  vitest:coverage Uncovered files 1/2
  vitest:coverage File "/x/src/large-file.ts" is taking longer than 3s # [!code error]
  vitest:coverage 3027 ms /x/src/large-file.ts
  vitest:coverage Uncovered files 2/2
  vitest:coverage 4 ms /x/src/untested-file.ts
  vitest:coverage Generate coverage total time 3521 ms
```

이 프로파일링 방식은 커버리지 제공자가 실수로 선택한 대용량 파일을 감지하는 데 매우 유용합니다.
예를 들어 설정에 의해 대용량 빌드된 minified Javascript 파일이 코드 커버리지에 실수로 포함되었다면, 로그에 나타나야 합니다.
이 경우 [`coverage.include`](https://vitest.dev/config/#coverage-include) 및 [`coverage.exclude`](https://vitest.dev/config/#coverage-exclude) 옵션을 조정하는 것이 좋습니다.

## Inspecting Profiling Records

`*.cpuprofile` 및 `*.heapprofile`의 내용을 다양한 도구로 확인할 수 있습니다. 아래는 예시 목록입니다.

- Speedscope
- Performance Profiling JavaScript in Visual Studio Code
- Profile Node.js performance with the Performance panel | developer.chrome.com
- Memory panel overview | developer.chrome.com
