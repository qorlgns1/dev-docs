---
title: "vmMemoryLimit"
description: "이 옵션은  및  풀에만 영향을 줍니다."
---

출처 URL: https://vitest.dev/config/vmmemorylimit

# vmMemoryLimit

- **타입:** `string | number`
- **기본값:** `1 / CPU Cores`

이 옵션은 `vmForks` 및 `vmThreads` 풀에만 영향을 줍니다.

워커가 재활용되기 전에 적용할 메모리 제한을 지정합니다. 이 값은 환경에 크게 의존하므로, 기본값에 의존하기보다 수동으로 지정하는 것이 좋습니다.

::: tip
구현은 Jest의 [`workerIdleMemoryLimit`](https://jestjs.io/docs/configuration#workeridlememorylimit-numberstring)을 기반으로 합니다.

제한값은 여러 방식으로 지정할 수 있으며, 최종 결과값은 `Math.floor`를 사용해 정수 값으로 변환됩니다:

- `<= 1` - 값을 시스템 메모리의 백분율로 간주합니다. 따라서 0.5는 워커의 메모리 제한을 전체 시스템 메모리의 절반으로 설정합니다.
- `\> 1` - 고정 바이트 값으로 간주합니다. 앞선 규칙 때문에 1바이트 값이 필요하다면(왜 그러는지는 모르겠지만) 1.1을 사용할 수 있습니다.
- 단위 포함
  - `50%` - 위와 같이 전체 시스템 메모리의 백분율
  - `100KB`, `65MB` 등 - 고정 메모리 제한을 나타내는 단위 포함 값
    - `K` / `KB` - 킬로바이트 (x1000)
    - `KiB` - 키비바이트 (x1024)
    - `M` / `MB` - 메가바이트
    - `MiB` - 메비바이트
    - `G` / `GB` - 기가바이트
    - `GiB` - 기비바이트
      :::

::: warning
백분율 기반 메모리 제한은 보고되는 시스템 메모리 정보가 부정확하기 때문에 Linux CircleCI 워커에서 [작동하지 않습니다](https://github.com/jestjs/jest/issues/11956#issuecomment-1212925677).
:::
