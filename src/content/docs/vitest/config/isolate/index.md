---
title: "isolate"
description: "격리된 환경에서 테스트를 실행합니다. 이 옵션은  및  풀에는 영향을 주지 않습니다."
---

# isolate

- **유형:** `boolean`
- **기본값:** `true`
- **CLI:** `--no-isolate`, `--isolate=false`

격리된 환경에서 테스트를 실행합니다. 이 옵션은 `vmThreads` 및 `vmForks` 풀에는 영향을 주지 않습니다.

코드가 부작용에 의존하지 않는다면(일반적으로 `node` 환경의 프로젝트에서 해당), 이 옵션을 비활성화하면 [성능이 향상](https://vitest.dev/guide/improving-performance)될 수 있습니다.

::: tip
Vitest 워크스페이스를 사용하고 프로젝트별로 격리를 비활성화하면 특정 테스트 파일에 대해서만 격리를 끌 수 있습니다.
:::
