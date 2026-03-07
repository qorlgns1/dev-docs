---
title: "fileParallelism"
description: "Should all test files run in parallel. Setting this to  will override  option to ."
---

Source URL: https://vitest.dev/config/fileparallelism

# fileParallelism

- **Type:** `boolean`
- **Default:** `true`
- **CLI:** `--no-file-parallelism`, `--fileParallelism=false`

Should all test files run in parallel. Setting this to `false` will override `maxWorkers` option to `1`.

::: tip
This option doesn't affect tests running in the same file. If you want to run those in parallel, use `concurrent` option on [describe](https://vitest.dev/api/#describe-concurrent) or via [a config](#sequence-concurrent).
:::
