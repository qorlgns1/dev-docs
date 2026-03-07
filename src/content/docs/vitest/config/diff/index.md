---
title: "diff"
description: "객체 또는 를 내보내는 모듈 경로입니다. diff 표시를 사용자 정의하려는 경우 유용합니다."
---

출처 URL: https://vitest.dev/config/diff

# diff

- **Type:** `string`
- **CLI:** `--diff=<path>`

`DiffOptions` 객체 또는 `DiffOptions`를 내보내는 모듈 경로입니다. diff 표시를 사용자 정의하려는 경우 유용합니다.

예를 들어, 설정 객체로는 다음과 같습니다:

```ts
import { defineConfig } from "vitest/config";
import c from "picocolors";

export default defineConfig({
  test: {
    diff: {
      aIndicator: c.bold("--"),
      bIndicator: c.bold("++"),
      omitAnnotationLines: true,
    },
  },
});
```

또는 모듈로는 다음과 같습니다:

:::code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    diff: "./vitest.diff.ts",
  },
});
```

```ts [vitest.diff.ts]
import type { DiffOptions } from "vitest";
import c from "picocolors";

export default {
  aIndicator: c.bold("--"),
  bIndicator: c.bold("++"),
  omitAnnotationLines: true,
} satisfies DiffOptions;
```

:::

## diff.expand

- **Type**: `boolean`
- **Default**: `true`
- **CLI:** `--diff.expand=false`

모든 공통 라인을 펼칩니다.

## diff.truncateThreshold

- **Type**: `number`
- **Default**: `0`
- **CLI:** `--diff.truncateThreshold=<path>`

표시할 diff 결과의 최대 길이입니다. 이 임계값을 초과하는 diff는 잘립니다.
기본값 `0`에서는 잘림이 적용되지 않습니다.

## diff.truncateAnnotation

- **Type**: `string`
- **Default**: `'... Diff result is truncated'`
- **CLI:** `--diff.truncateAnnotation=<annotation>`

diff 결과가 잘린 경우, 결과 끝에 출력되는 주석입니다.

## diff.truncateAnnotationColor

- **Type**: `DiffOptionsColor = (arg: string) => string`
- **Default**: `noColor = (string: string): string => string`

잘림 주석의 색상입니다. 기본값은 색상 없이 출력됩니다.

## diff.printBasicPrototype

- **Type**: `boolean`
- **Default**: `false`

diff 출력에서 기본 프로토타입 `Object` 및 `Array`를 출력합니다.

## diff.maxDepth

- **Type**: `number`
- **Default**: `20` (또는 서로 다른 타입 비교 시 `8`)

중첩된 객체를 출력할 때 재귀 깊이를 제한합니다.
