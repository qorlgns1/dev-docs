---
title: "reporters"
description: "interface UserConfig {"
---

Source URL: https://vitest.dev/config/reporters

# reporters

- **Type:**

```ts
interface UserConfig {
  reporters?: ConfigReporter | Array<ConfigReporter>;
}

type ConfigReporter = string | Reporter | [string, object?];
```

- **Default:** [`'default'`](https://vitest.dev/guide/reporters#default-reporter)
- **CLI:**
  - `--reporter=tap` for a single reporter
  - `--reporter=verbose --reporter=github-actions` for multiple reporters

This option defines a single reporter or a list of reporters available to Vitest during the test run.

Alongside built-in reporters, you can also pass down a custom implementation of a [`Reporter` interface](https://vitest.dev/api/advanced/reporters), or a path to a module that exports it as a default export (e.g. `'./path/to/reporter.ts'`, `'@scope/reporter'`).

You can configure a reporter by providing a tuple: `[string, object]`, where the string is a reporter name, and the object is the reporter's options.

::: warning
Note that the [coverage](https://vitest.dev/guide/coverage) feature uses a different [`coverage.reporter`](https://vitest.dev/config/coverage#reporter) option instead of this one.
:::

## Built-in Reporters

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

## Example

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
