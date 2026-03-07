---
title: "Reporters 확장 고급 {#extending-reporters}"
description: '이것은 고급 API입니다. 내장 리포터를 구성하기만 원한다면 "Reporters" 가이드를 읽어보세요.'
---

# Reporters 확장 고급 {#extending-reporters}

::: warning
이것은 고급 API입니다. 내장 리포터를 구성하기만 원한다면 ["Reporters"](https://vitest.dev/guide/reporters) 가이드를 읽어보세요.
:::

`vitest/reporters`에서 리포터를 import해서 확장하면 커스텀 리포터를 만들 수 있습니다.

## 내장 리포터 확장하기

일반적으로 리포터를 처음부터 만들 필요는 없습니다. `vitest`에는 확장할 수 있는 여러 기본 리포팅 프로그램이 포함되어 있습니다.

```ts
import { DefaultReporter } from "vitest/reporters";

export default class MyDefaultReporter extends DefaultReporter {
  // do something
}
```

물론 리포터를 처음부터 만들 수도 있습니다. `BaseReporter` 클래스를 확장하고 필요한 메서드를 구현하면 됩니다.

다음은 커스텀 리포터의 예시입니다:

```ts [custom-reporter.js]
import { BaseReporter } from "vitest/reporters";

export default class CustomReporter extends BaseReporter {
  onTestModuleCollected() {
    const files = this.ctx.state.getFiles(this.watchFilters);
    this.reportTestSummary(files);
  }
}
```

또는 `Reporter` 인터페이스를 구현할 수 있습니다:

```ts [custom-reporter.js]
import type { Reporter } from "vitest/node";

export default class CustomReporter implements Reporter {
  onTestModuleCollected() {
    // print something
  }
}
```

그런 다음 `vitest.config.ts` 파일에서 커스텀 리포터를 사용할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import CustomReporter from "./custom-reporter.js";

export default defineConfig({
  test: {
    reporters: [new CustomReporter()],
  },
});
```

## 보고된 작업

리포터가 받는 task를 사용하는 대신, Reported Tasks API를 사용하는 것을 권장합니다.

`vitest.state.getReportedEntity(runnerTask)`를 호출해 이 API에 접근할 수 있습니다:

```ts twoslash
import type { Reporter, TestModule } from "vitest/node";

class MyReporter implements Reporter {
  onTestRunEnd(testModules: ReadonlyArray<TestModule>) {
    for (const testModule of testModules) {
      for (const task of testModule.children) {
        //                          ^?
        console.log("test run end", task.type, task.fullName);
      }
    }
  }
}
```

## Export된 리포터

`vitest`에는 바로 사용할 수 있는 몇 가지 [내장 리포터](https://vitest.dev/guide/reporters)가 포함되어 있습니다.

### 내장 리포터:

1. `DefaultReporter`
1. `DotReporter`
1. `JsonReporter`
1. `VerboseReporter`
1. `TapReporter`
1. `JUnitReporter`
1. `TapFlatReporter`
1. `HangingProcessReporter`
1. `TreeReporter`

### 기본 추상 리포터:

1. `BaseReporter`

### 인터페이스 리포터:

1. `Reporter`
