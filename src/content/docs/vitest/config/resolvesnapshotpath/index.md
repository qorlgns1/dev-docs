---
title: "resolveSnapshotPath"
description: "기본 스냅샷 경로를 재정의합니다. 예를 들어, 테스트 파일 옆에 스냅샷을 저장하려면 다음과 같이 합니다."
---

출처 URL: https://vitest.dev/config/resolvesnapshotpath

# resolveSnapshotPath

- **타입**: `(testPath: string, snapExtension: string, context: { config: SerializedConfig }) => string`
- **기본값**: 스냅샷 파일을 `__snapshots__` 디렉터리에 저장

기본 스냅샷 경로를 재정의합니다. 예를 들어, 테스트 파일 옆에 스냅샷을 저장하려면 다음과 같이 합니다.

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    resolveSnapshotPath: (testPath, snapExtension) => testPath + snapExtension,
  },
});
```

`context` 파라미터를 사용해 프로젝트의 직렬화된 설정에 접근할 수도 있습니다. 이는 여러 [projects](https://vitest.dev/guide/projects)를 사용할 때 프로젝트 이름에 따라 서로 다른 위치에 스냅샷을 저장하려는 경우에 유용합니다.

```ts
import { basename, dirname, join } from "node:path";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    resolveSnapshotPath(testPath, snapExtension, context) {
      return join(
        dirname(testPath),
        "__snapshots__",
        context.config.name ?? "default",
        basename(testPath) + snapExtension,
      );
    },
  },
});
```
