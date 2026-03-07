---
title: "fileParallelism"
description: "모든 테스트 파일을 병렬로 실행할지 여부를 설정합니다. 이를 로 설정하면  옵션이 로 강제됩니다."
---

출처 URL: https://vitest.dev/config/fileparallelism

# fileParallelism

- **유형:** `boolean`
- **기본값:** `true`
- **CLI:** `--no-file-parallelism`, `--fileParallelism=false`

모든 테스트 파일을 병렬로 실행할지 여부를 설정합니다. 이를 `false`로 설정하면 `maxWorkers` 옵션이 `1`로 강제됩니다.

::: tip
이 옵션은 동일한 파일 내에서 실행되는 테스트에는 영향을 주지 않습니다. 해당 테스트를 병렬로 실행하려면 [describe](https://vitest.dev/api/#describe-concurrent)에서 `concurrent` 옵션을 사용하거나 [config](#sequence-concurrent)를 통해 설정하세요.
:::
