---
title: "특정 테스트 파일에만 격리 비활성화하기"
description: "항목마다 를 지정하면, 특정 파일 집합에 대해서만 격리를 비활성화하여 테스트 실행 속도를 높일 수 있습니다:"
---

출처 URL: https://vitest.dev/guide/recipes

# 레시피

## 특정 테스트 파일에만 격리 비활성화하기

`projects` 항목마다 `isolate`를 지정하면, 특정 파일 집합에 대해서만 격리를 비활성화하여 테스트 실행 속도를 높일 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        // Non-isolated unit tests
        name: "Unit tests",
        isolate: false,
        exclude: ["**.integration.test.ts"],
      },
      {
        // Isolated integration tests
        name: "Integration tests",
        include: ["**.integration.test.ts"],
      },
    ],
  },
});
```

## 병렬 및 순차 테스트 파일

`projects` 옵션을 사용하면 테스트 파일을 병렬 그룹과 순차 그룹으로 나눌 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        name: "Parallel",
        exclude: ["**.sequential.test.ts"],
      },
      {
        name: "Sequential",
        include: ["**.sequential.test.ts"],
        fileParallelism: false,
      },
    ],
  },
});
```
