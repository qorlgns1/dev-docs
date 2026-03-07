---
title: "snapshotEnvironment"
description: "커스텀 스냅샷 환경 구현의 경로입니다. Node.js API를 지원하지 않는 환경에서 테스트를 실행하는 경우 유용합니다. 이 옵션은 브라우저 러너에서는 아무런 영향이 없습니다."
---

출처 URL: https://vitest.dev/config/snapshotenvironment

# snapshotEnvironment

- **타입:** `string`

커스텀 스냅샷 환경 구현의 경로입니다. Node.js API를 지원하지 않는 환경에서 테스트를 실행하는 경우 유용합니다. 이 옵션은 브라우저 러너에서는 아무런 영향이 없습니다.

이 객체는 `SnapshotEnvironment` 형태를 가져야 하며, 스냅샷 파일의 경로 해석 및 읽기/쓰기에 사용됩니다:

```ts
export interface SnapshotEnvironment {
  getVersion: () => string;
  getHeader: () => string;
  resolvePath: (filepath: string) => Promise<string>;
  resolveRawPath: (testPath: string, rawPath: string) => Promise<string>;
  saveSnapshotFile: (filepath: string, snapshot: string) => Promise<void>;
  readSnapshotFile: (filepath: string) => Promise<string | null>;
  removeSnapshotFile: (filepath: string) => Promise<void>;
}
```

API의 일부만 덮어써야 하는 경우, `vitest/snapshot` 엔트리 포인트에서 기본 `VitestSnapshotEnvironment`를 확장할 수 있습니다.

::: warning
이 옵션은 저수준 옵션이며, 기본 Node.js API에 접근할 수 없는 고급 사례에서만 사용해야 합니다.

스냅샷 기능만 구성하면 된다면 [`snapshotFormat`](#snapshotformat) 또는 [`resolveSnapshotPath`](#resolvesnapshotpath) 옵션을 사용하세요.
:::
