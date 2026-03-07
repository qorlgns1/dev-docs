---
title: "Profiling Test Performance"
description: "When you run Vitest it reports multiple time metrics of your tests:"
---

Source URL: https://vitest.dev/guide/profiling-test-performance

# Profiling Test Performance

When you run Vitest it reports multiple time metrics of your tests:

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

- Transform: How much time was spent transforming the files. See [File Transform](#file-transform).
- Setup: Time spent for running the [`setupFiles`](https://vitest.dev/config/setupfiles) files.
- Import: Time it took to import your test files and their dependencies. This also includes the time spent collecting all tests. Note that this doesn't include dynamic imports inside of tests.
- Tests: Time spent for actually running the test cases.
- Environment: Time spent for setting up the test [`environment`](https://vitest.dev/config/#environment), for example JSDOM.

## Test Runner

In cases where your test execution time is high, you can generate a profile of the test runner. See NodeJS documentation for following options:

- `--cpu-prof`
- `--heap-prof`
- `--prof`

:::warning
The `--prof` option does not work with `pool: 'threads'` due to `node:worker_threads` limitations.
:::

To pass these options to Vitest's test runner, define `execArgv` in your Vitest configuration:

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

After the tests have run there should be a `test-runner-profile/*.cpuprofile` and `test-runner-profile/*.heapprofile` files generated. See [Inspecting profiling records](#inspecting-profiling-records) for instructions how to analyze these files.

See [Profiling | Examples](https://github.com/vitest-dev/vitest/tree/main/examples/profiling) for example.

## Main Thread

Profiling main thread is useful for debugging Vitest's Vite usage and [`globalSetup`](https://vitest.dev/config/#globalsetup) files.
This is also where your Vite plugins are running.

:::tip
See [Performance | Vite](https://vitejs.dev/guide/performance.html) for more tips about Vite specific profiling.

We recommend [`vite-plugin-inspect`](https://github.com/antfu-collective/vite-plugin-inspect) for profiling your Vite plugin performance.
:::

To do this you'll need to pass arguments to the Node process that runs Vitest.

```bash
$ node --cpu-prof --cpu-prof-dir=main-profile ./node_modules/vitest/vitest.mjs --run
#      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                  ^^^^^
#               NodeJS arguments                                           Vitest arguments
```

After the tests have run there should be a `main-profile/*.cpuprofile` file generated. See [Inspecting profiling records](#inspecting-profiling-records) for instructions how to analyze these files.

## File Transform

This profiling strategy is a good way to identify unnecessary transforms caused by [barrel files](https://vitejs.dev/guide/performance.html#avoid-barrel-files).
If these logs contain files that should not be loaded when your test is run, you might have barrel files that are importing files unnecessarily.

You can also use [Vitest UI](https://vitest.dev/guide/ui) to debug slowness caused by barrel file.
The example below shows how importing files without barrel file reduces amount of transformed files by ~85%.

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

To see how files are transformed, you can use `VITEST_DEBUG_DUMP` environment variable to write transformed files in the file system:

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

If code coverage generation is slow on your project you can use `DEBUG=vitest:coverage` environment variable to enable performance logging.

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

This profiling approach is great for detecting large files that are accidentally picked by coverage providers.
For example if your configuration is accidentally including large built minified Javascript files in code coverage, they should appear in logs.
In these cases you might want to adjust your [`coverage.include`](https://vitest.dev/config/#coverage-include) and [`coverage.exclude`](https://vitest.dev/config/#coverage-exclude) options.

## Inspecting Profiling Records

You can inspect the contents of `*.cpuprofile` and `*.heapprofile` with various tools. See list below for examples.

- Speedscope
- Performance Profiling JavaScript in Visual Studio Code
- Profile Node.js performance with the Performance panel | developer.chrome.com
- Memory panel overview | developer.chrome.com
