---
title: "exclude"
description: "테스트 파일에서 제외해야 하는 glob 패턴 목록입니다. 이 패턴들은 (기본값: )를 기준으로 해석됩니다."
---

출처 URL: https://vitest.dev/config/exclude

# exclude

- **타입:** `string[]`
- **기본값:** `['**/node_modules/**', '**/.git/**']`
- **CLI:** `vitest --exclude "**/excluded-file" --exclude "*/other-files/*.js"`

테스트 파일에서 제외해야 하는 [glob 패턴](https://superchupu.dev/tinyglobby/comparison) 목록입니다. 이 패턴들은 [`root`](https://vitest.dev/config/root)(기본값: [`process.cwd()`](https://nodejs.org/api/process.html#processcwd))를 기준으로 해석됩니다.

Vitest는 glob을 해석하기 위해 [`tinyglobby`](https://www.npmjs.com/package/tinyglobby) 패키지를 사용합니다.

::: warning
이 옵션은 커버리지에 영향을 주지 않습니다. 커버리지 보고서에서 특정 파일을 제거해야 한다면 [`coverage.exclude`](https://vitest.dev/config/coverage#exclude)를 사용하세요.

이 옵션은 CLI 플래그로 제공해도 기존 구성을 덮어쓰지 않는 유일한 옵션입니다. `--exclude` 플래그로 추가한 모든 glob 패턴은 config의 `exclude`에 추가됩니다.
:::

## 예시

```js
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    exclude: ["**/node_modules/**", "**/dist/**", "./temp/**"],
  },
});
```

::: tip
CLI `exclude` 옵션은 누적(additive)되지만, config에서 `exclude`를 수동으로 설정하면 기본값이 대체됩니다. 기본 `exclude` 패턴을 확장하려면 `vitest/config`의 `configDefaults`를 사용하세요:

```js{6}
import { configDefaults, defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    exclude: [
      ...configDefaults.exclude,
      'packages/template/*',
      './temp/**',
    ],
  },
})
```

:::
