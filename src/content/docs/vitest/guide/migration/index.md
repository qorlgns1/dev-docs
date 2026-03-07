---
title: "마이그레이션 가이드"
description: "Vitest의 V8 코드 커버리지 프로바이더는 이제 더 정확한 커버리지 결과 리매핑 로직을 사용합니다."
---

출처 URL: https://vitest.dev/guide/migration

# 마이그레이션 가이드

## Vitest 4.0으로 마이그레이션 {#vitest-4}

### V8 코드 커버리지 주요 변경사항

Vitest의 V8 코드 커버리지 프로바이더는 이제 더 정확한 커버리지 결과 리매핑 로직을 사용합니다.
Vitest v3에서 업데이트할 때 커버리지 리포트에 변화가 나타나는 것이 예상됩니다.

과거에는 Vitest가 V8 커버리지 결과를 소스 파일에 리매핑하기 위해 [`v8-to-istanbul`](https://github.com/istanbuljs/v8-to-istanbul)을 사용했습니다.
이 방식은 정확도가 높지 않았고 커버리지 리포트에서 많은 거짓 양성(false positive)을 만들었습니다.
이제 우리는 V8 커버리지에 AST 기반 분석을 활용하는 새 패키지를 개발했습니다.
이를 통해 V8 리포트가 `@vitest/coverage-istanbul` 리포트만큼 정확해졌습니다.

- 커버리지 무시 힌트가 업데이트되었습니다. [Coverage | Ignoring Code](https://vitest.dev/guide/coverage.html#ignoring-code)를 참고하세요.
- `coverage.ignoreEmptyLines`가 제거되었습니다. 런타임 코드가 없는 줄은 더 이상 리포트에 포함되지 않습니다.
- `coverage.experimentalAstAwareRemapping`이 제거되었습니다. 이 옵션은 이제 기본으로 활성화되며, 유일하게 지원되는 리매핑 방식입니다.
- `coverage.ignoreClassMethods`가 이제 V8 프로바이더에서도 지원됩니다.

### `coverage.all` 및 `coverage.extensions` 옵션 제거

이전 버전에서 Vitest는 기본적으로 커버리지 리포트에 커버되지 않은 모든 파일을 포함했습니다.
이는 `coverage.all`의 기본값이 `true`이고, `coverage.include`의 기본값이 `**`였기 때문입니다.
이 기본값은 충분한 이유가 있었습니다. 테스트 도구는 사용자의 소스 파일 저장 위치를 추측할 수 없기 때문입니다.

이로 인해 Vitest의 커버리지 프로바이더가 minified Javascript 같은 예상치 못한 파일을 처리하게 되었고, 커버리지 리포트 생성이 느려지거나 멈추는 문제가 발생했습니다.
Vitest v4에서는 `coverage.all`을 완전히 제거했고, **리포트에는 기본적으로 커버된 파일만 포함되도록 변경**했습니다.

v4로 업그레이드할 때는 설정에 `coverage.include`를 정의하고, 필요하면 간단한 `coverage.exclude` 패턴을 적용하기 시작하는 것을 권장합니다.

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    coverage: {
      // Include covered and uncovered files matching this pattern:
      include: ["packages/**/src/**.{js,jsx,ts,tsx}"], // [!code ++]

      // Exclusion is applied for the files that match include pattern above
      // No need to define root level *.config.ts files or node_modules, as we didn't add those in include
      exclude: ["**/some-pattern/**"], // [!code ++]

      // These options are removed now
      all: true, // [!code --]
      extensions: ["js", "ts"], // [!code --]
    },
  },
});
```

`coverage.include`가 정의되지 않은 경우, 커버리지 리포트에는 테스트 실행 중 로드된 파일만 포함됩니다.

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    coverage: {
      // Include not set, include only files that are loaded during test run
      include: undefined, // [!code ++]

      // Loaded files that match this pattern will be excluded:
      exclude: ["**/some-pattern/**"], // [!code ++]
    },
  },
});
```

새 가이드도 참고하세요.

- 예시는 [Including and excluding files from coverage report](https://vitest.dev/guide/coverage.html#including-and-excluding-files-from-coverage-report)
- 커버리지 생성 디버깅 팁은 [Profiling Test Performance | Code coverage](https://vitest.dev/guide/profiling-test-performance.html#code-coverage)

### 단순화된 `exclude`

이제 기본적으로 Vitest는 `node_modules`와 `.git` 폴더의 테스트만 제외합니다. 즉, Vitest는 더 이상 다음을 제외하지 않습니다.

- `dist` 및 `cypress` 폴더
- `.idea`, `.cache`, `.output`, `.temp` 폴더
- `rollup.config.js`, `prettier.config.js`, `ava.config.js` 등의 설정 파일

테스트 파일이 위치한 디렉터리를 제한해야 한다면 파일 제외보다 성능이 더 좋은 [`test.dir`](https://vitest.dev/config/dir) 옵션을 대신 사용하세요.

```ts
import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    dir: "./frontend/tests", // [!code ++]
  },
});
```

이전 동작을 복원하려면 기존 `excludes`를 수동으로 지정하세요.

```ts
import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    exclude: [
      ...configDefaults.exclude,
      "**/dist/**", // [!code ++]
      "**/cypress/**", // [!code ++]
      "**/.{idea,git,cache,output,temp}/**", // [!code ++]
      "**/{karma,rollup,webpack,vite,vitest,jest,ava,babel,nyc,cypress,tsup,build,eslint,prettier}.config.*", // [!code ++]
    ],
  },
});
```

### `spyOn` 및 `fn` 생성자 지원

이전에는 `vi.spyOn`으로 생성자를 감시하려고 하면 `Constructor <name> requires 'new'` 같은 오류가 발생했습니다. Vitest 4부터는 `new` 키워드로 호출된 모든 mock이 `mock.apply`를 호출하는 대신 인스턴스를 생성합니다. 따라서 이런 경우 mock 구현은 `function` 또는 `class` 키워드를 사용해야 합니다.

```ts {12-14,16-20}
const cart = {
  Apples: class Apples {
    getApples() {
      return 42;
    }
  },
};

const Spy = vi
  .spyOn(cart, "Apples")
  .mockImplementation(() => ({ getApples: () => 0 })) // [!code --]
  // with a function keyword
  .mockImplementation(function () {
    this.getApples = () => 0;
  })
  // with a custom class
  .mockImplementation(
    class MockApples {
      getApples() {
        return 0;
      }
    },
  );

const mock = new Spy();
```

이제 화살표 함수를 제공하면 mock 호출 시 [`<anonymous> is not a constructor` error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_constructor)가 발생합니다.

### 모킹 변경사항

생성자 지원 같은 새 기능과 함께, Vitest 4는 수년간 접수된 여러 모듈 모킹 이슈를 해결하기 위해 mock 생성 방식을 변경했습니다. 이번 릴리스는 특히 클래스를 다룰 때 모듈 spy의 동작을 덜 혼란스럽게 만드는 것을 목표로 합니다.

- `vi.fn().getMockName()`은 이제 기본적으로 `spy` 대신 `vi.fn()`을 반환합니다. 이로 인해 mock이 포함된 스냅샷에 영향이 있을 수 있으며 이름이 `[MockFunction spy]`에서 `[MockFunction]`으로 바뀝니다. `vi.spyOn`으로 생성한 spy는 더 나은 디버깅 경험을 위해 기본적으로 원래 이름을 계속 사용합니다.
- `vi.restoreAllMocks`는 더 이상 spy의 상태를 리셋하지 않으며, 수동으로 `vi.spyOn`으로 만든 spy만 복원합니다. automock은 이제 이 함수의 영향을 받지 않습니다(설정 옵션 [`restoreMocks`](https://vitest.dev/config/#restoremocks)에도 동일하게 적용). 단, `.mockRestore`는 여전히 mock 구현을 리셋하고 상태를 비웁니다.
- mock에 대해 `vi.spyOn`을 호출하면 이제 동일한 mock을 반환합니다.
- `mock.settledResults`는 함수 호출 시점에 `'incomplete'` 결과로 즉시 채워집니다. Promise가 완료되면 결과에 따라 타입이 변경됩니다.
- automock된 인스턴스 메서드는 이제 올바르게 격리되지만 프로토타입과 상태를 공유합니다. 메서드에 자체 커스텀 mock 구현이 없는 한, 프로토타입 구현을 재정의하면 항상 인스턴스 메서드에 영향을 줍니다. mock에서 `.mockReset`을 호출해도 이 상속 구조가 더 이상 깨지지 않습니다.

```ts
import { AutoMockedClass } from "./example.js";
const instance1 = new AutoMockedClass();
const instance2 = new AutoMockedClass();

instance1.method.mockReturnValue(42);

expect(instance1.method()).toBe(42);
expect(instance2.method()).toBe(undefined);

expect(AutoMockedClass.prototype.method).toHaveBeenCalledTimes(2);

instance1.method.mockReset();
AutoMockedClass.prototype.method.mockReturnValue(100);

expect(instance1.method()).toBe(100);
expect(instance2.method()).toBe(100);

expect(AutoMockedClass.prototype.method).toHaveBeenCalledTimes(4);
```

- automock된 메서드는 수동 `.mockRestore`를 사용해도 더 이상 복원할 수 없습니다. `spy: true`를 사용한 automock 모듈은 이전처럼 계속 동작합니다.
- automock된 getter는 더 이상 원래 getter를 호출하지 않습니다. 기본적으로 automock getter는 이제 `undefined`를 반환합니다. getter를 spy하고 구현을 변경하려면 계속 `vi.spyOn(object, name, 'get')`을 사용할 수 있습니다.
- mock `vi.fn(implementation).mockReset()`은 이제 `.getMockImplementation()`에서 mock 구현을 올바르게 반환합니다.
- `vi.fn().mock.invocationCallOrder`는 이제 `0`이 아니라 Jest처럼 `1`부터 시작합니다.

### 파일명 필터와 함께 사용하는 Standalone 모드

사용자 경험 개선을 위해, [`--standalone`](https://vitest.dev/guide/cli#standalone)을 파일명 필터와 함께 사용하면 이제 Vitest가 일치하는 파일 실행을 시작합니다.

```sh
# In Vitest v3 and below this command would ignore "math.test.ts" filename filter.
# In Vitest v4 the math.test.ts will run automatically.
$ vitest --standalone math.test.ts
```

이를 통해 사용자는 standalone 모드용으로 재사용 가능한 `package.json` 스크립트를 만들 수 있습니다.

::: code-group

```json [package.json]
{
  "scripts": {
    "test:dev": "vitest --standalone"
  }
}
```

```bash [CLI]
# Start Vitest in standalone mode, without running any files on start
$ pnpm run test:dev

# Run math.test.ts immediately
$ pnpm run test:dev math.test.ts
```

:::

### `vite-node`를 [Module Runner](https://vite.dev/guide/api-environment-runtimes.html#modulerunner)로 대체

Module Runner는 Vite에 직접 구현된 `vite-node`의 후속입니다. Vitest는 이제 Vite SSR 핸들러 래퍼를 두는 대신 이를 직접 사용합니다. 따라서 일부 기능은 더 이상 사용할 수 없습니다.

- `VITE_NODE_DEPS_MODULE_DIRECTORIES` 환경 변수는 `VITEST_MODULE_DIRECTORIES`로 대체되었습니다.
- Vitest는 더 이상 모든 [test runner](https://vitest.dev/api/advanced/runner)에 `__vitest_executor`를 주입하지 않습니다. 대신 [`ModuleRunner`](https://vite.dev/guide/api-environment-runtimes.html#modulerunner) 인스턴스인 `moduleRunner`를 주입합니다.
- `vitest/execute` 엔트리 포인트가 제거되었습니다. 원래부터 내부용이었습니다.
- [Custom environments](https://vitest.dev/guide/environment)는 더 이상 `transformMode` 속성을 제공할 필요가 없습니다. 대신 `viteEnvironment`를 제공하세요. 이를 제공하지 않으면 Vitest는 환경 이름을 사용해 서버에서 파일을 변환합니다([`server.environments`](https://vite.dev/guide/api-environment-instances.html) 참고).
- `vite-node`는 더 이상 Vitest의 의존성이 아닙니다.
- `deps.optimizer.web`는 [`deps.optimizer.client`](https://vitest.dev/config/#deps-optimizer-client)로 이름이 변경되었습니다. 다른 서버 환경을 사용할 때는 사용자 정의 이름으로 optimizer 설정을 적용할 수도 있습니다.

Vite에는 자체 externalization 메커니즘이 있지만, breaking change 양을 줄이기 위해 기존 방식을 계속 사용하기로 했습니다. 패키지의 inline/externalize에는 계속 [`server.deps`](https://vitest.dev/config/#server-deps)를 사용할 수 있습니다.

위에서 언급한 고급 기능에 의존하지 않는 한 이 업데이트는 눈에 띄지 않을 것입니다.

### `workspace`가 `projects`로 대체됨

`workspace` 설정 옵션은 Vitest 3.2에서 [`projects`](https://vitest.dev/guide/projects)로 이름이 변경되었습니다. 기능적으로는 동일하지만, 이제는 워크스페이스 소스로 다른 파일을 지정할 수 없습니다(이전에는 프로젝트 배열을 export하는 파일을 지정할 수 있었습니다). `projects`로의 마이그레이션은 간단하며, `vitest.workspace.js`의 코드를 `vitest.config.ts`로 옮기면 됩니다.

::: code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    workspace: "./vitest.workspace.js", // [!code --]
    projects: [
      // [!code ++]
      "./packages/*", // [!code ++]
      {
        // [!code ++]
        test: {
          // [!code ++]
          name: "unit", // [!code ++]
        }, // [!code ++]
      }, // [!code ++]
    ], // [!code ++]
  },
});
```

```ts [vitest.workspace.js]
import { defineWorkspace } from "vitest/config"; // [!code --]

export default defineWorkspace([
  // [!code --]
  "./packages/*", // [!code --]
  {
    // [!code --]
    test: {
      // [!code --]
      name: "unit", // [!code --]
    }, // [!code --]
  }, // [!code --]
]); // [!code --]
```

:::

### Browser Provider 재작업

Vitest 4.0에서는 브라우저 프로바이더가 문자열(`'playwright'`, `'webdriverio'`) 대신 객체를 받습니다. `preview`는 더 이상 기본값이 아닙니다. 이로 인해 커스텀 옵션을 더 쉽게 다룰 수 있고, 더 이상 `/// <reference` 주석을 추가할 필요도 없습니다.

```ts
import { playwright } from "@vitest/browser-playwright"; // [!code ++]

export default defineConfig({
  test: {
    browser: {
      provider: "playwright", // [!code --]
      provider: playwright({
        // [!code ++]
        launchOptions: {
          // [!code ++]
          slowMo: 100, // [!code ++]
        }, // [!code ++]
      }), // [!code ++]
      instances: [
        {
          browser: "chromium",
          launch: {
            // [!code --]
            slowMo: 100, // [!code --]
          }, // [!code --]
        },
      ],
    },
  },
});
```

`playwright` 팩토리의 속성 이름도 [Playwright documentation](https://playwright.dev/docs/api/class-testoptions#test-options-launch-options)와 일치하도록 정렬되어 더 쉽게 찾을 수 있습니다.

이 변경으로 `@vitest/browser` 패키지는 더 이상 필요하지 않으며, 의존성에서 제거할 수 있습니다. context import를 지원하려면 `@vitest/browser/context`를 `vitest/browser`로 업데이트해야 합니다.

```ts
import { page } from "@vitest/browser/context"; // [!code --]
import { page } from "vitest/browser"; // [!code ++]

test("example", async () => {
  await page.getByRole("button").click();
});
```

모듈은 동일하므로 간단한 "Find and Replace"만으로 충분합니다.

`@vitest/browser/utils` 모듈을 사용 중이었다면, 이제 해당 유틸리티도 `vitest/browser`에서 import할 수 있습니다.

```ts
import { getElementError } from "@vitest/browser/utils"; // [!code --]
import { utils } from "vitest/browser"; // [!code ++]
const { getElementError } = utils; // [!code ++]
```

::: warning
전환 기간 동안 `@vitest/browser/context`와 `@vitest/browser/utils`는 런타임에서 모두 동작하지만, 향후 릴리스에서 제거될 예정입니다.
:::

### Pool 재작업

Vitest는 테스트 러너 워커에서 테스트 파일 실행 방식을 오케스트레이션하기 위해 [`tinypool`](https://github.com/tinylibs/tinypool)을 사용해 왔습니다. Tinypool은 병렬성, 격리, IPC 통신 같은 복잡한 작업이 내부적으로 어떻게 동작하는지를 제어해 왔습니다. 하지만 Tinypool에는 Vitest 개발 속도를 늦추는 결함이 있다는 점을 확인했습니다. Vitest v4에서는 Tinypool을 완전히 제거하고 추가 의존성 없이 pool 동작을 다시 작성했습니다. 배경은 [feat!: rewrite pools without tinypool #8705
](https://github.com/vitest-dev/vitest/pull/8705)에서 확인할 수 있습니다.

새 pool 아키텍처는 이전에 복잡했던 여러 설정 옵션을 단순화합니다.

- `maxThreads`와 `maxForks`는 이제 `maxWorkers`입니다.
- 환경 변수 `VITEST_MAX_THREADS`와 `VITEST_MAX_FORKS`는 이제 `VITEST_MAX_WORKERS`입니다.
- `singleThread`와 `singleFork`는 이제 `maxWorkers: 1, isolate: false`입니다. 테스트가 테스트 간 모듈 리셋에 의존하고 있었다면 [`beforeAll` test hook](https://vitest.dev/api/#beforeall)에서 [`vi.resetModules()`](https://vitest.dev/api/vi.html#vi-resetmodules)를 호출하는 [setupFile](https://vitest.dev/config/setupfiles)을 추가해야 합니다.
- `poolOptions`가 제거되었습니다. 기존 `poolOptions`는 이제 모두 최상위 옵션입니다. VM pool의 `memoryLimit`은 `vmMemoryLimit`로 이름이 변경되었습니다.
- `threads.useAtomics`가 제거되었습니다. 이 기능이 필요하다면 새 기능 요청을 등록해 주세요.
- 커스텀 pool 인터페이스가 다시 작성되었습니다. [Custom Pool](https://vitest.dev/guide/advanced/pool#custom-pool)을 참고하세요.

```ts
export default defineConfig({
  test: {
    poolOptions: {
      // [!code --]
      forks: {
        // [!code --]
        execArgv: ["--expose-gc"], // [!code --]
        isolate: false, // [!code --]
        singleFork: true, // [!code --]
      }, // [!code --]
      vmThreads: {
        // [!code --]
        memoryLimit: "300Mb", // [!code --]
      }, // [!code --]
    }, // [!code --]
    execArgv: ["--expose-gc"], // [!code ++]
    isolate: false, // [!code ++]
    maxWorkers: 1, // [!code ++]
    vmMemoryLimit: "300Mb", // [!code ++]
  },
});
```

이전에는 [Vitest Projects](https://vitest.dev/guide/projects)를 사용할 때 일부 pool 관련 옵션을 프로젝트별로 지정할 수 없었습니다. 새 아키텍처에서는 더 이상 문제가 되지 않습니다.

::: code-group

```ts [Isolation per project]
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

```ts [Parallel & Sequential projects]
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

```ts [Node CLI options per project]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        name: "Production env",
        execArgv: ["--env-file=.env.prod"],
      },
      {
        name: "Staging env",
        execArgv: ["--env-file=.env.staging"],
      },
    ],
  },
});
```

:::

더 많은 예시는 [Recipes](https://vitest.dev/guide/recipes)를 참고하세요.

### Reporter 업데이트

Reporter API `onCollected`, `onSpecsCollected`, `onPathsCollected`, `onTaskUpdate`, `onFinished`가 제거되었습니다. 새로운 대안은 [`Reporters API`](https://vitest.dev/api/advanced/reporters)를 참고하세요. 새 API는 Vitest `v3.0.0`에서 도입되었습니다.

`basic` reporter는 다음과 동일하므로 제거되었습니다.

```ts
export default defineConfig({
  test: {
    reporters: [["default", { summary: false }]],
  },
});
```

[`verbose`](https://vitest.dev/guide/reporters#verbose-reporter) reporter는 이제 테스트 케이스를 평탄한 목록으로 출력합니다. 이전 동작으로 되돌리려면 `--reporter=tree`를 사용하세요:

```ts
export default defineConfig({
  test: {
    reporters: ["verbose"], // [!code --]
    reporters: ["tree"], // [!code ++]
  },
});
```

### Custom Elements를 사용하는 Snapshot에서 Shadow Root 출력

Vitest 4.0에서는 custom elements를 포함한 snapshot이 shadow root 내용을 출력합니다. 이전 동작을 복원하려면 [`printShadowRoot` 옵션](https://vitest.dev/config/#snapshotformat)을 `false`로 설정하세요.

```js{15-22}
// before Vite 4.0
exports[`custom element with shadow root 1`] = `
"<body>
  <div>
    <custom-element />
  </div>
</body>"
`

// after Vite 4.0
exports[`custom element with shadow root 1`] = `
"<body>
  <div>
    <custom-element>
      #shadow-root
        <span
          class="some-name"
          data-test-id="33"
          id="5"
        >
          hello
        </span>
    </custom-element>
  </div>
</body>"
`
```

### Deprecated API 제거

Vitest 4.0에서는 다음을 포함한 일부 deprecated API가 제거됩니다:

- `poolMatchGlobs` config option. 대신 [`projects`](https://vitest.dev/guide/projects)를 사용하세요.
- `environmentMatchGlobs` config option. 대신 [`projects`](https://vitest.dev/guide/projects)를 사용하세요.
- `deps.external`, `deps.inline`, `deps.fallbackCJS` config options. 대신 `server.deps.external`, `server.deps.inline`, 또는 `server.deps.fallbackCJS`를 사용하세요.
- `browser.testerScripts` config option. 대신 [`browser.testerHtmlPath`](https://vitest.dev/config/browser/testerhtmlpath)를 사용하세요.
- `minWorkers` config option. 테스트 실행 방식에는 `maxWorkers`만 영향을 주므로, 이 공개 옵션은 제거됩니다.
- Vitest는 더 이상 `test`와 `describe`의 세 번째 인자로 테스트 옵션 객체를 전달하는 방식을 지원하지 않습니다. 대신 두 번째 인자를 사용하세요:

```ts
test(
  "example",
  () => {
    /* ... */
  },
  { retry: 2 },
); // [!code --]
test("example", { retry: 2 }, () => {
  /* ... */
}); // [!code ++]
```

마지막 인자로 timeout 숫자를 전달하는 방식은 여전히 지원됩니다:

```ts
test("example", () => {
  /* ... */
}, 1000); // ✅
```

이번 릴리스에서는 deprecated type도 모두 제거됩니다. 이로써 Vitest가 실수로 `@types/node`를 끌어오던 문제가 최종적으로 해결됩니다([#5481](https://github.com/vitest-dev/vitest/issues/5481), [#6141](https://github.com/vitest-dev/vitest/issues/6141) 참고).

## Jest에서 마이그레이션 {#jest}

Vitest는 Jest 호환 API를 목표로 설계되어, Jest에서의 마이그레이션을 최대한 단순하게 만들었습니다. 그럼에도 불구하고 다음과 같은 차이를 만날 수 있습니다:

### 기본값으로서의 Globals

Jest는 [globals API](https://jestjs.io/docs/api)가 기본적으로 활성화되어 있습니다. Vitest는 그렇지 않습니다. [the `globals` configuration setting](https://vitest.dev/config/#globals)으로 globals를 활성화하거나, 코드에서 `vitest` module의 import를 사용하도록 업데이트할 수 있습니다.

globals를 비활성화 상태로 유지한다면, [`testing-library`](https://testing-library.com/) 같은 일반적인 라이브러리에서 자동 DOM [cleanup](https://testing-library.com/docs/svelte-testing-library/api/#cleanup)이 실행되지 않는다는 점에 유의하세요.

### `mock.mockReset`

Jest의 [`mockReset`](https://jestjs.io/docs/mock-function-api#mockfnmockreset)은 mock 구현을 `undefined`를 반환하는
빈 함수로 교체합니다.

Vitest의 [`mockReset`](https://vitest.dev/api/mock#mockreset)은 mock 구현을 원래 상태로 재설정합니다.
즉, `vi.fn(impl)`로 생성한 mock을 재설정하면 mock 구현은 `impl`로 돌아갑니다.

### `mock.mock`는 Persistent

Jest는 `.mockClear`가 호출되면 mock state를 다시 생성하므로, 항상 getter로 접근해야 합니다. 반면 Vitest는 state에 대한 persistent reference를 유지하므로 재사용할 수 있습니다:

```ts
const mock = vi.fn();
const state = mock.mock;
mock.mockClear();

expect(state).toBe(mock.mock); // fails in Jest
```

### Module Mocks

Jest에서 module을 mocking할 때 factory 인자의 반환값은 default export입니다. Vitest에서는 factory 인자가 각 export를 명시적으로 정의한 객체를 반환해야 합니다. 예를 들어, 아래 `jest.mock`는 다음과 같이 업데이트해야 합니다:

```ts
jest.mock("./some-path", () => "hello"); // [!code --]
vi.mock("./some-path", () => ({
  // [!code ++]
  default: "hello", // [!code ++]
})); // [!code ++]
```

자세한 내용은 [`vi.mock` api section](https://vitest.dev/api/vi#vi-mock)을 참고하세요.

### Auto-Mocking Behaviour

Jest와 달리 `<root>/__mocks__`에 있는 mocked module은 `vi.mock()`이 호출되지 않으면 로드되지 않습니다. Jest처럼 모든 테스트에서 항상 mock되도록 하려면 [`setupFiles`](https://vitest.dev/config/setupfiles) 안에서 mock할 수 있습니다.

### Mocked Package의 Original 가져오기

package를 부분적으로만 mocking하는 경우, 이전에는 Jest의 `requireActual` 함수를 사용했을 수 있습니다. Vitest에서는 이 호출을 `vi.importActual`로 바꿔야 합니다.

```ts
const { cloneDeep } = jest.requireActual("lodash/cloneDeep"); // [!code --]
const { cloneDeep } = await vi.importActual("lodash/cloneDeep"); // [!code ++]
```

### 외부 라이브러리까지 mocking 확장

Jest는 기본적으로 처리하지만, module을 mocking할 때 같은 module을 사용하는 다른 외부 라이브러리에도 이 mocking을 확장하려면, 어떤 3rd-party library를 mock할지 명시적으로 알려야 합니다. 즉 외부 라이브러리가 source code의 일부가 되도록 [server.deps.inline](https://vitest.dev/config/#server-deps-inline)을 사용하세요.

```
server.deps.inline: ["lib-name"]
```

### expect.getState().currentTestName

Vitest의 `test` 이름은 테스트와 suite를 더 쉽게 구분할 수 있도록 `>` 기호로 연결됩니다. 반면 Jest는 빈 공백(` `)을 사용합니다.

```diff
- `${describeTitle} ${testTitle}`
+ `${describeTitle} > ${testTitle}`
```

### Envs

Jest와 마찬가지로, Vitest도 기존에 설정되지 않았다면 `NODE_ENV`를 `test`로 설정합니다. Vitest에는 `JEST_WORKER_ID`에 대응하는 `VITEST_POOL_ID`(항상 `maxWorkers` 이하)도 있으므로, 이에 의존하고 있다면 이름을 바꾸는 것을 잊지 마세요. 또한 Vitest는 실행 중인 worker의 고유 ID인 `VITEST_WORKER_ID`도 제공합니다. 이 숫자는 `maxWorkers`의 영향을 받지 않으며, worker가 생성될 때마다 증가합니다.

### Replace property

객체를 수정하려고 Jest에서 [replaceProperty API](https://jestjs.io/docs/jest-object#jestreplacepropertyobject-propertykey-value)를 사용했다면, Vitest에서도 동일하게 [`vi.stubEnv`](https://vitest.dev/api/#vi-stubenv) 또는 [`vi.spyOn`](https://vitest.dev/api/vi#vi-spyon)을 사용할 수 있습니다.

### Done Callback

Vitest는 callback 스타일의 테스트 선언을 지원하지 않습니다. `async`/`await` 함수를 사용하도록 다시 작성하거나, callback 스타일을 흉내 내기 위해 Promise를 사용할 수 있습니다.

```js
it('should work', (done) => {  // [!code --]
it('should work', () => new Promise(done => { // [!code ++]
  // ...
  done()
}) // [!code --]
})) // [!code ++]
```

### Hooks

Vitest에서는 `beforeAll`/`beforeEach` hook이 [teardown function](https://vitest.dev/api/#setup-and-teardown)을 반환할 수 있습니다. 따라서 `undefined` 또는 `null`이 아닌 값을 반환하는 경우, hook 선언을 다시 작성해야 할 수 있습니다:

```ts
beforeEach(() => setActivePinia(createTestingPinia())); // [!code --]
beforeEach(() => {
  setActivePinia(createTestingPinia());
}); // [!code ++]
```

Jest에서는 hook이 순차적으로(하나씩) 호출됩니다. 기본적으로 Vitest는 hook을 stack 방식으로 실행합니다. Jest 동작을 사용하려면 [`sequence.hooks`](https://vitest.dev/config/#sequence-hooks) 옵션을 업데이트하세요:

```ts
export default defineConfig({
  test: {
    sequence: {
      // [!code ++]
      hooks: "list", // [!code ++]
    }, // [!code ++]
  },
});
```

### Types

Vitest에는 `jest` namespace에 해당하는 것이 없으므로, type을 `vitest`에서 직접 import해야 합니다:

```ts
let fn: jest.Mock<(name: string) => number>; // [!code --]
import type { Mock } from "vitest"; // [!code ++]
let fn: Mock<(name: string) => number>; // [!code ++]
```

### Timers

Vitest는 Jest의 legacy timers를 지원하지 않습니다.

### Timeout

`jest.setTimeout`을 사용했다면 `vi.setConfig`로 마이그레이션해야 합니다:

```ts
jest.setTimeout(5_000); // [!code --]
vi.setConfig({ testTimeout: 5_000 }); // [!code ++]
```

### Vue Snapshots

이것은 Jest 전용 기능은 아니지만, 이전에 vue-cli preset과 함께 Jest를 사용했다면 [`jest-serializer-vue`](https://github.com/eddyerburgh/jest-serializer-vue) package를 설치하고, 이를 [`snapshotSerializers`](https://vitest.dev/config/#snapshotserializers)에 지정해야 합니다:

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    snapshotSerializers: ["jest-serializer-vue"],
  },
});
```

그렇지 않으면 snapshot에 escape된 `"` 문자가 많이 포함됩니다.
