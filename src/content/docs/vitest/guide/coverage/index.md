---
title: "커버리지"
description: "Vitest는 을 통한 네이티브 코드 커버리지와 을 통한 계측 기반 코드 커버리지를 지원합니다."
---

출처 URL: https://vitest.dev/guide/coverage

# 커버리지

Vitest는 [`v8`](https://v8.dev/blog/javascript-code-coverage)을 통한 네이티브 코드 커버리지와 [`istanbul`](https://istanbul.js.org/)을 통한 계측 기반 코드 커버리지를 지원합니다.

## 커버리지 프로바이더

`v8` 및 `istanbul` 지원은 모두 선택 사항입니다. 기본값으로는 `v8`이 사용됩니다.

`test.coverage.provider`를 `v8` 또는 `istanbul`로 설정해 커버리지 도구를 선택할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      provider: "v8", // or 'istanbul'
    },
  },
});
```

Vitest 프로세스를 시작하면, 해당 지원 패키지를 자동으로 설치하라는 프롬프트가 표시됩니다.

또는 수동 설치를 선호한다면:

::: code-group

```bash [v8]
npm i -D @vitest/coverage-v8
```

```bash [istanbul]
npm i -D @vitest/coverage-istanbul
```

:::

## V8 프로바이더

::: info
아래의 V8 커버리지 설명은 Vitest에 특화된 내용이며 다른 테스트 러너에는 적용되지 않습니다.
`v3.2.0`부터 Vitest는 V8 커버리지에 [AST 기반 커버리지 리매핑](https://vitest.dev/blog/vitest-3-2#coverage-v8-ast-aware-remapping)을 사용하며, Istanbul과 동일한 커버리지 리포트를 생성합니다.

이를 통해 사용자는 V8 커버리지의 속도와 Istanbul 커버리지의 정확도를 함께 얻을 수 있습니다.
:::

기본적으로 Vitest는 `'v8'` 커버리지 프로바이더를 사용합니다.
이 프로바이더는 [V8 엔진](https://v8.dev/) 위에서 구현된 Javascript 런타임이 필요하며, NodeJS, Deno, Google Chrome 같은 Chromium 기반 브라우저가 이에 해당합니다.

커버리지 수집은 런타임 중 [`node:inspector`](https://nodejs.org/api/inspector.html)와 브라우저의 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/)을 사용해 V8에 지시하여 수행됩니다. 사용자의 소스 파일은 사전 계측 없이 그대로 실행할 수 있습니다.

- ✅ 사용 권장 옵션
- ✅ 사전 트랜스파일 단계가 없습니다. 테스트 파일을 있는 그대로 실행할 수 있습니다.
- ✅ Istanbul보다 실행 시간이 빠릅니다.
- ✅ Istanbul보다 메모리 사용량이 낮습니다.
- ✅ 커버리지 리포트 정확도는 Istanbul과 동일한 수준입니다([Vitest `v3.2.0`부터](https://vitest.dev/blog/vitest-3-2#coverage-v8-ast-aware-remapping)).
- ⚠️ 일부 경우에는 Istanbul보다 느릴 수 있습니다. 예: 서로 다른 모듈을 매우 많이 로드하는 경우. V8은 특정 모듈로 커버리지 수집 범위를 제한하는 기능을 지원하지 않습니다.
- ⚠️ V8 엔진에서 정한 일부 경미한 제한 사항이 있습니다. [`ast-v8-to-istanbul` | Limitations](https://github.com/AriPerkkio/ast-v8-to-istanbul?tab=readme-ov-file#limitations)을 참고하세요.
- ❌ Firefox나 Bun처럼 V8을 사용하지 않는 환경에서는 동작하지 않습니다. 또한 Cloudflare Workers처럼 프로파일러를 통해 V8 커버리지를 노출하지 않는 환경에서도 동작하지 않습니다.

## Istanbul 프로바이더

[Istanbul 코드 커버리지 도구](https://istanbul.js.org/)는 2012년부터 존재해 왔으며, 오랜 기간 충분히 검증되었습니다.
이 프로바이더는 사용자의 소스 파일을 계측하여 커버리지를 추적하므로 어떤 Javascript 런타임에서도 동작합니다.

실제로 소스 파일을 계측한다는 것은 사용자 파일에 추가 Javascript를 삽입하는 것을 의미합니다:

```js
// Simplified example of branch and function coverage counters
const coverage = {
  // [!code ++]
  branches: { 1: [0, 0] }, // [!code ++]
  functions: { 1: 0 }, // [!code ++]
}; // [!code ++]

export function getUsername(id) {
  // Function coverage increased when this is invoked  // [!code ++]
  coverage.functions["1"]++; // [!code ++]

  if (id == null) {
    // Branch coverage increased when this is invoked  // [!code ++]
    coverage.branches["1"][0]++; // [!code ++]

    throw new Error("User ID is required");
  }
  // Implicit else coverage increased when if-statement condition not met  // [!code ++]
  coverage.branches["1"][1]++; // [!code ++]

  return database.getUser(id);
}

globalThis.__VITEST_COVERAGE__ ||= {}; // [!code ++]
globalThis.__VITEST_COVERAGE__[filename] = coverage; // [!code ++]
```

- ✅ 어떤 Javascript 런타임에서도 동작
- ✅ 13년 이상 널리 사용되며 충분히 검증됨
- ✅ 일부 경우 V8보다 빠름. V8은 모든 모듈이 계측되는 반면, 커버리지 계측 범위를 특정 파일로 제한할 수 있음
- ❌ 사전 계측 단계가 필요함
- ❌ 계측 오버헤드로 인해 실행 속도가 V8보다 느림
- ❌ 계측으로 파일 크기가 증가함
- ❌ 메모리 사용량이 V8보다 높음

## 커버리지 설정

::: tip
모든 커버리지 옵션은 [Coverage Config Reference](https://vitest.dev/config/#coverage)에 나열되어 있습니다.
:::

커버리지를 활성화해 테스트하려면 CLI에서 `--coverage` 플래그를 전달하거나 `vitest.config.ts`에서 `coverage.enabled`를 설정할 수 있습니다:

::: code-group

```json [package.json]
{
  "scripts": {
    "test": "vitest",
    "coverage": "vitest run --coverage"
  }
}
```

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      enabled: true,
    },
  },
});
```

:::

## 커버리지 리포트에서 파일 포함 및 제외

[`coverage.include`](https://vitest.dev/config/#coverage-include)와 [`coverage.exclude`](https://vitest.dev/config/#coverage-exclude)를 구성하여 커버리지 리포트에 어떤 파일을 표시할지 정의할 수 있습니다.

기본적으로 Vitest는 테스트 실행 중 import된 파일만 표시합니다.
리포트에 미커버 파일도 포함하려면, 소스 파일을 선택하는 패턴으로 [`coverage.include`](https://vitest.dev/config/#coverage-include)를 구성해야 합니다:

::: code-group

```ts [vitest.config.ts] {6}
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      include: ["src/**/*.{ts,tsx}"],
    },
  },
});
```

```sh [Covered Files]
├── src
│   ├── components
│   │   └── counter.tsx   # [!code ++]
│   ├── mock-data
│   │   ├── products.json # [!code error]
│   │   └── users.json    # [!code error]
│   └── utils
│       ├── formatters.ts # [!code ++]
│       ├── time.ts       # [!code ++]
│       └── users.ts      # [!code ++]
├── test
│   └── utils.test.ts     # [!code error]
│
├── package.json          # [!code error]
├── tsup.config.ts        # [!code error]
└── vitest.config.ts      # [!code error]
```

:::

`coverage.include`에 매칭되는 파일을 제외하려면, 추가로 [`coverage.exclude`](https://vitest.dev/config/#coverage-exclude)를 정의할 수 있습니다:

::: code-group

```ts [vitest.config.ts] {7}
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      include: ["src/**/*.{ts,tsx}"],
      exclude: ["**/utils/users.ts"],
    },
  },
});
```

```sh [Covered Files]
├── src
│   ├── components
│   │   └── counter.tsx   # [!code ++]
│   ├── mock-data
│   │   ├── products.json # [!code error]
│   │   └── users.json    # [!code error]
│   └── utils
│       ├── formatters.ts # [!code ++]
│       ├── time.ts       # [!code ++]
│       └── users.ts      # [!code error]
├── test
│   └── utils.test.ts     # [!code error]
│
├── package.json          # [!code error]
├── tsup.config.ts        # [!code error]
└── vitest.config.ts      # [!code error]
```

:::

## 사용자 정의 커버리지 리포터

`test.coverage.reporter`에 패키지 이름 또는 절대 경로를 전달하여 사용자 정의 커버리지 리포터를 사용할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      reporter: [
        // Specify reporter using name of the NPM package
        ["@vitest/custom-coverage-reporter", { someOption: true }],

        // Specify reporter using local path
        "/absolute/path/to/custom-reporter.cjs",
      ],
    },
  },
});
```

사용자 정의 리포터는 Istanbul에서 로드되며, 해당 리포터 인터페이스를 충족해야 합니다. 참고용으로 [내장 리포터 구현](https://github.com/istanbuljs/istanbuljs/tree/master/packages/istanbul-reports/lib)을 확인하세요.

```js [custom-reporter.cjs]
const { ReportBase } = require("istanbul-lib-report");

module.exports = class CustomReporter extends ReportBase {
  constructor(opts) {
    super();

    // Options passed from configuration are available here
    this.file = opts.file;
  }

  onStart(root, context) {
    this.contentWriter = context.writer.writeFile(this.file);
    this.contentWriter.println("Start of custom coverage report");
  }

  onEnd() {
    this.contentWriter.println("End of custom coverage report");
    this.contentWriter.close();
  }
};
```

## 사용자 정의 커버리지 프로바이더

`test.coverage.provider`에 `'custom'`을 전달해 사용자 정의 커버리지 프로바이더를 제공할 수도 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      provider: "custom",
      customProviderModule: "my-custom-coverage-provider",
    },
  },
});
```

사용자 정의 프로바이더에는 `customProviderModule` 옵션이 필요하며, 이는 `CoverageProviderModule`을 로드할 모듈 이름 또는 경로입니다. 기본 export로 `CoverageProviderModule`을 구현한 객체를 내보내야 합니다:

```ts [my-custom-coverage-provider.ts]
import type {
  CoverageProvider,
  CoverageProviderModule,
  ResolvedCoverageOptions,
  Vitest,
} from "vitest";

const CustomCoverageProviderModule: CoverageProviderModule = {
  getProvider(): CoverageProvider {
    return new CustomCoverageProvider();
  },

  // Implements rest of the CoverageProviderModule ...
};

class CustomCoverageProvider implements CoverageProvider {
  name = "custom-coverage-provider";
  options!: ResolvedCoverageOptions;

  initialize(ctx: Vitest) {
    this.options = ctx.config.coverage;
  }

  // Implements rest of the CoverageProvider ...
}

export default CustomCoverageProviderModule;
```

자세한 내용은 타입 정의를 참고하세요.

## 코드 무시

두 커버리지 프로바이더 모두 커버리지 리포트에서 코드를 무시하는 자체 방법을 제공합니다:

- `v8`
- `istanbul`

TypeScript를 사용할 때 소스 코드는 `esbuild`로 트랜스파일되며, 이 과정에서 모든 주석이 제거됩니다([esbuild#516](https://github.com/evanw/esbuild/issues/516)).
[legal comments](https://esbuild.github.io/api/#legal-comments)로 간주되는 주석은 유지됩니다.

ignore 힌트에 `@preserve` 키워드를 포함할 수 있습니다.
이러한 ignore 힌트는 최종 프로덕션 빌드에도 포함될 수 있다는 점에 유의하세요.

```diff
-/* istanbul ignore if */
+/* istanbul ignore if -- @preserve */
if (condition) {

-/* v8 ignore if */
+/* v8 ignore if -- @preserve */
if (condition) {
```

### 예시

::: code-group

```ts [if else]
/* v8 ignore if -- @preserve */
if (parameter) {
  // [!code error]
  console.log("Ignored"); // [!code error]
} // [!code error]
else {
  console.log("Included");
}

/* v8 ignore else -- @preserve */
if (parameter) {
  console.log("Included");
} else {
  // [!code error]
  console.log("Ignored"); // [!code error]
} // [!code error]
```

```ts [next node]
/* v8 ignore next -- @preserve */
console.log("Ignored"); // [!code error]
console.log("Included");

/* v8 ignore next -- @preserve */
function ignored() {
  // [!code error]
  console.log("all"); // [!code error]
  // [!code error]
  console.log("lines"); // [!code error]
  // [!code error]
  console.log("are"); // [!code error]
  // [!code error]
  console.log("ignored"); // [!code error]
} // [!code error]

/* v8 ignore next -- @preserve */
class Ignored {
  // [!code error]
  ignored() {} // [!code error]
  alsoIgnored() {} // [!code error]
} // [!code error]

/* v8 ignore next -- @preserve */
condition // [!code error]
  ? console.log("ignored") // [!code error]
  : console.log("also ignored"); // [!code error]
```

```ts [try catch]
/* v8 ignore next -- @preserve */
try {
  // [!code error]
  console.log("Ignored"); // [!code error]
} catch (error) {
  // [!code error]
  // [!code error]
  console.log("Ignored"); // [!code error]
} // [!code error]

try {
  console.log("Included");
} catch (error) {
  /* v8 ignore next -- @preserve */
  console.log("Ignored"); // [!code error]
  /* v8 ignore next -- @preserve */
  console.log("Ignored"); // [!code error]
}

// Requires rolldown-vite due to esbuild's lack of support.
// See https://vite.dev/guide/rolldown.html#how-to-try-rolldown
try {
  console.log("Included");
} catch (error) /* v8 ignore next */ {
  // [!code error]
  console.log("Ignored"); // [!code error]
} // [!code error]
```

```ts [switch case]
switch (type) {
  case 1:
    return "Included";

  /* v8 ignore next -- @preserve */
  case 2: // [!code error]
    return "Ignored"; // [!code error]

  case 3:
    return "Included";

  /* v8 ignore next -- @preserve */
  default: // [!code error]
    return "Ignored"; // [!code error]
}
```

```ts [whole file]
/* v8 ignore file -- @preserve */
export function ignored() {
  // [!code error]
  return "Whole file is ignored"; // [!code error]
} // [!code error]
```

:::

## 커버리지 성능

프로젝트에서 코드 커버리지 생성이 느리다면 [Profiling Test Performance | Code coverage](https://vitest.dev/guide/profiling-test-performance.html#code-coverage)를 참고하세요.

## Vitest UI

[Vitest UI](https://vitest.dev/guide/ui)에서 커버리지 리포트를 확인할 수 있습니다.

Vitest UI는 커버리지 리포트가 명시적으로 활성화되고 html 커버리지 리포터가 있을 때만 커버리지 리포트를 활성화하며, 그렇지 않으면 사용할 수 없습니다:

- 설정 파일에서 `coverage.enabled=true`를 활성화하거나 `--coverage.enabled=true` 플래그로 Vitest를 실행합니다
- `coverage.reporter` 목록에 `html`을 추가합니다: `subdir` 옵션을 활성화해 커버리지 리포트를 하위 디렉터리에 둘 수도 있습니다
