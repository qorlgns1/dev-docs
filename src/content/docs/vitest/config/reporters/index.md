---
title: "reporters"
description: "interface UserConfig {"
---

출처 URL: https://vitest.dev/config/reporters

# reporters

- **유형:**

```ts
interface UserConfig {
  reporters?: ConfigReporter | Array<ConfigReporter>;
}

type ConfigReporter = string | Reporter | [string, object?];
```

- **기본값:** [`'default'`](https://vitest.dev/guide/reporters#default-reporter)
- **CLI:**
  - 단일 reporter의 경우 `--reporter=tap`
  - 여러 reporter의 경우 `--reporter=verbose --reporter=github-actions`

이 옵션은 테스트 실행 중 Vitest에서 사용할 단일 reporter 또는 reporter 목록을 정의합니다.

내장 reporter와 함께, 사용자 정의 [`Reporter` interface](https://vitest.dev/api/advanced/reporters) 구현체를 전달하거나, 이를 default export로 내보내는 모듈 경로(예: `'./path/to/reporter.ts'`, `'@scope/reporter'`)를 전달할 수도 있습니다.

문자열이 reporter 이름이고 객체가 해당 reporter의 옵션인 튜플 `[string, object]`을 제공해 reporter를 구성할 수 있습니다.

::: warning
[coverage](https://vitest.dev/guide/coverage) 기능은 이 옵션 대신 별도의 [`coverage.reporter`](https://vitest.dev/config/coverage#reporter) 옵션을 사용한다는 점에 유의하세요.
:::

## 내장 Reporters

- `default`
- `verbose`
- `tree`
- `dot`
- `junit`
- `json`
- `html`
- `tap`
- `tap-flat`
- `hanging-process`
- `github-actions`
- `blob`

## 예시

::: code-group

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    reporters: [
      "default",
      // conditional reporter
      process.env.CI ? "github-actions" : {},
      // custom reporter from npm package
      // options are passed down as a tuple
      ["vitest-sonar-reporter", { outputFile: "sonar-report.xml" }],
    ],
  },
});
```

```bash [CLI]
vitest --reporter=github-actions --reporter=junit
```

:::
