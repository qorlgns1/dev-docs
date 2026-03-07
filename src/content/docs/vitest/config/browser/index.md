---
title: "브라우저 설정 레퍼런스"
description: "import { defineConfig } from 'vitest/config'"
---

출처 URL: https://vitest.dev/config/browser

# 브라우저 설정 레퍼런스

[config file](https://vitest.dev/config/)의 `test.browser` 필드를 업데이트하여 브라우저 설정을 변경할 수 있습니다. 간단한 config file 예시는 다음과 같습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [
        {
          browser: "chromium",
          setupFile: "./chromium-setup.js",
        },
      ],
    },
  },
});
```

다양한 config 예시는 ["Config Reference"](https://vitest.dev/config/) 문서를 참고하세요.

::: warning
이 페이지에 나열된 *모든 옵션*은 설정 내부의 `test` 속성 안에 위치합니다:

```ts [vitest.config.js]
export default defineConfig({
  test: {
    browser: {},
  },
});
```

:::

## browser.enabled

- **Type:** `boolean`
- **Default:** `false`
- **CLI:** `--browser`, `--browser.enabled=false`

기본적으로 모든 테스트를 브라우저 안에서 실행합니다. `--browser`는 [`browser.instances`](#browser-instances) 항목이 최소 하나 이상 있을 때만 동작합니다.

## browser.instances

- **Type:** `BrowserConfig`
- **Default:** `[]`

여러 브라우저 설정을 정의합니다. 각 config에는 최소한 `browser` 필드가 있어야 합니다.

[project options](https://vitest.dev/config/)의 대부분(아이콘이 표시되지 않은 항목)과 `browser.testerHtmlPath` 같은 일부 `browser` 옵션을 지정할 수 있습니다.

::: warning
모든 browser config는 루트 config의 옵션을 상속합니다:

```ts{3,9} [vitest.config.ts]
export default defineConfig({
  test: {
    setupFile: ['./root-setup-file.js'],
    browser: {
      enabled: true,
      testerHtmlPath: './custom-path.html',
      instances: [
        {
          // will have both setup files: "root" and "browser"
          setupFile: ['./browser-setup-file.js'],
          // implicitly has "testerHtmlPath" from the root config // [!code warning]
          // testerHtmlPath: './custom-path.html', // [!code warning]
        },
      ],
    },
  },
})
```

더 많은 예시는 ["Multiple Setups"](https://vitest.dev/guide/browser/multiple-setups) 가이드를 참고하세요.
:::

사용 가능한 `browser` 옵션 목록:

- [`browser.headless`](#browser-headless)
- [`browser.locators`](#browser-locators)
- [`browser.viewport`](#browser-viewport)
- [`browser.testerHtmlPath`](#browser-testerhtmlpath)
- [`browser.screenshotDirectory`](#browser-screenshotdirectory)
- [`browser.screenshotFailures`](#browser-screenshotfailures)
- [`browser.provider`](#browser-provider)

내부적으로 Vitest는 이 인스턴스들을 별도의 [test projects](https://vitest.dev/api/advanced/test-project)로 변환하며, 더 나은 캐시 성능을 위해 단일 Vite 서버를 공유합니다.

## browser.headless

- **Type:** `boolean`
- **Default:** `process.env.CI`
- **CLI:** `--browser.headless`, `--browser.headless=false`

브라우저를 `headless` 모드로 실행합니다. CI에서 Vitest를 실행하면 기본적으로 활성화됩니다.

## browser.isolate

- **Type:** `boolean`
- **Default:** [`--isolate`](https://vitest.dev/config/#isolate)와 동일
- **CLI:** `--browser.isolate`, `--browser.isolate=false`

각 테스트를 별도의 iframe에서 실행합니다.

::: danger DEPRECATED
이 옵션은 deprecated 되었습니다. 대신 [`isolate`](https://vitest.dev/config/#isolate)를 사용하세요.
:::

## browser.testerHtmlPath

- **Type:** `string`

HTML entry point 경로입니다. 프로젝트 루트 기준 상대 경로를 사용할 수 있습니다. 이 파일은 [`transformIndexHtml`](https://vite.dev/guide/api-plugin#transformindexhtml) hook으로 처리됩니다.

## browser.api

- **Type:** `number | { port?, strictPort?, host? }`
- **Default:** `63315`
- **CLI:** `--browser.api=63315`, `--browser.api.port=1234, --browser.api.host=example.com`

브라우저에서 코드를 제공하는 Vite 서버 옵션을 설정합니다. [`test.api`](#api) 옵션에는 영향을 주지 않습니다. 기본적으로 Vitest는 개발 서버와의 충돌을 피하기 위해 `63315` 포트를 할당하므로, 둘을 병렬로 실행할 수 있습니다.

## browser.provider {#browser-provider}

- **Type:** `BrowserProviderOption`
- **Default:** `'preview'`
- **CLI:** `--browser.provider=playwright`

provider factory의 반환값입니다. `@vitest/browser-<provider-name>`에서 factory를 가져오거나 자체 provider를 만들 수 있습니다:

```ts{8-10}
import { playwright } from '@vitest/browser-playwright'
import { webdriverio } from '@vitest/browser-webdriverio'
import { preview } from '@vitest/browser-preview'

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      provider: webdriverio(),
      provider: preview(), // default
    },
  },
})
```

provider가 브라우저를 초기화하는 방식을 설정하려면 factory function에 옵션을 전달할 수 있습니다:

```ts{7-13,20-26}
import { playwright } from '@vitest/browser-playwright'

export default defineConfig({
  test: {
    browser: {
      // shared provider options between all instances
      provider: playwright({
        launchOptions: {
          slowMo: 50,
          channel: 'chrome-beta',
        },
        actionTimeout: 5_000,
      }),
      instances: [
        { browser: 'chromium' },
        {
          browser: 'firefox',
          // overriding options only for a single instance
          // this will NOT merge options with the parent one
          provider: playwright({
            launchOptions: {
              firefoxUserPrefs: {
                'browser.startup.homepage': 'https://example.com',
              },
            },
          })
        }
      ],
    },
  },
})
```

### Custom Provider advanced

::: danger ADVANCED API
Custom provider API는 매우 실험적이며 패치 버전 간에도 변경될 수 있습니다. 브라우저에서 테스트만 실행하면 된다면 [`browser.instances`](#browser-instances) 옵션을 대신 사용하세요.
:::

```ts
export interface BrowserProvider {
  name: string;
  mocker?: BrowserModuleMocker;
  readonly initScripts?: string[];
  /**
   * @experimental opt-in into file parallelisation
   */
  supportsParallelism: boolean;
  getCommandsContext: (sessionId: string) => Record<string, unknown>;
  openPage: (sessionId: string, url: string) => Promise<void>;
  getCDPSession?: (sessionId: string) => Promise<CDPSession>;
  close: () => Awaitable<void>;
}
```

## browser.ui

- **Type:** `boolean`
- **Default:** `!isCI`
- **CLI:** `--browser.ui=false`

Vitest UI를 페이지에 주입할지 여부입니다. 기본적으로 개발 중에는 UI iframe을 주입합니다.

## browser.viewport

- **Type:** `{ width, height }`
- **Default:** `414x896`

기본 iframe viewport입니다.

## browser.locators

내장 [browser locators](https://vitest.dev/api/browser/locators)에 대한 옵션입니다.

### browser.locators.testIdAttribute

- **Type:** `string`
- **Default:** `data-testid`

`getByTestId` locator로 요소를 찾을 때 사용하는 속성입니다.

## browser.screenshotDirectory

- **Type:** `string`
- **Default:** 테스트 파일 디렉터리의 `__screenshots__`

`root` 기준 스크린샷 디렉터리 경로입니다.

## browser.screenshotFailures

- **Type:** `boolean`
- **Default:** `!browser.ui`

테스트 실패 시 Vitest가 스크린샷을 찍을지 여부입니다.

## browser.orchestratorScripts

- **Type:** `BrowserScript[]`
- **Default:** `[]`

테스트 iframe이 초기화되기 전에 orchestrator HTML에 주입할 custom script입니다. 이 HTML 문서는 iframe만 설정하며 실제로 사용자 코드를 import하지는 않습니다.

script의 `src`와 `content`는 Vite plugins에 의해 처리됩니다. script는 다음 형태로 제공해야 합니다:

```ts
export interface BrowserScript {
  /**
   * If "content" is provided and type is "module", this will be its identifier.
   *
   * If you are using TypeScript, you can add `.ts` extension here for example.
   * @default `injected-${index}.js`
   */
  id?: string;
  /**
   * JavaScript content to be injected. This string is processed by Vite plugins if type is "module".
   *
   * You can use `id` to give Vite a hint about the file extension.
   */
  content?: string;
  /**
   * Path to the script. This value is resolved by Vite so it can be a node module or a file path.
   */
  src?: string;
  /**
   * If the script should be loaded asynchronously.
   */
  async?: boolean;
  /**
   * Script type.
   * @default 'module'
   */
  type?: string;
}
```

## browser.commands

- **Type:** `Record<string, BrowserCommand>`
- **Default:** `{ readFile, writeFile, ... }`

브라우저 테스트 중 `vitest/browser`에서 import할 수 있는 custom [commands](https://vitest.dev/api/browser/commands)입니다.

## browser.connectTimeout

- **Type:** `number`
- **Default:** `60_000`

밀리초 단위 timeout입니다. 브라우저 연결이 이보다 오래 걸리면 테스트 스위트가 실패합니다.

::: info
이는 브라우저가 Vitest 서버와 WebSocket 연결을 수립하는 데 걸려야 하는 시간입니다. 일반적인 상황에서는 이 timeout에 도달하면 안 됩니다.
:::

## browser.trace

- **Type:** `'on' | 'off' | 'on-first-retry' | 'on-all-retries' | 'retain-on-failure' | object`
- **CLI:** `--browser.trace=on`, `--browser.trace=retain-on-failure`
- **Default:** `'off'`

브라우저 테스트 실행의 trace를 캡처합니다. [Playwright Trace Viewer](https://trace.playwright.dev/)로 trace를 미리 볼 수 있습니다.

이 옵션은 다음 값을 지원합니다:

- `'on'` - 모든 테스트의 trace를 캡처합니다. (성능 부담이 커서 권장되지 않음)
- `'off'` - trace를 캡처하지 않습니다.
- `'on-first-retry'` - 테스트를 처음 재시도할 때만 trace를 캡처합니다.
- `'on-all-retries'` - 테스트의 모든 재시도에서 trace를 캡처합니다.
- `'retain-on-failure'` - 실패한 테스트의 trace만 캡처합니다. 통과한 테스트의 trace는 자동으로 삭제됩니다.
- `object` - 다음 형태의 객체:

```ts
interface TraceOptions {
  mode:
    | "on"
    | "off"
    | "on-first-retry"
    | "on-all-retries"
    | "retain-on-failure";
  /**
   * The directory where all traces will be stored. By default, Vitest
   * stores all traces in `__traces__` folder close to the test file.
   */
  tracesDir?: string;
  /**
   * Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview.
   * @default true
   */
  screenshots?: boolean;
  /**
   * If this option is true tracing will
   * - capture DOM snapshot on every action
   * - record network activity
   * @default true
   */
  snapshots?: boolean;
}
```

::: danger WARNING
이 옵션은 [**playwright**](https://vitest.dev/config/browser/playwright) provider에서만 지원됩니다.
:::

## browser.trackUnhandledErrors

- **Type:** `boolean`
- **Default:** `true`

포착되지 않은 오류와 예외를 추적해 Vitest가 보고할 수 있도록 합니다.

특정 오류를 숨겨야 한다면 [`onUnhandledError`](https://vitest.dev/config/#onunhandlederror) 옵션을 사용하는 것이 권장됩니다.

이를 비활성화하면 모든 Vitest 오류 핸들러가 완전히 제거되며, "Pause on exceptions" 체크박스를 켠 상태에서 디버깅할 때 도움이 될 수 있습니다.

## browser.expect

- **Type:** `ExpectOptions`

### browser.expect.toMatchScreenshot

[`toMatchScreenshot` assertion](https://vitest.dev/api/browser/assertions.html#tomatchscreenshot)의
기본 옵션입니다.
이 옵션은 모든 screenshot assertion에 적용됩니다.

::: tip
screenshot assertion의 전역 기본값을 설정하면 테스트 스위트 전반의 일관성을 유지하고
개별 테스트의 반복을 줄일 수 있습니다. 필요할 때는 특정 테스트 케이스에서
assertion 수준으로 이 기본값을 여전히 override할 수 있습니다.
:::

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      expect: {
        toMatchScreenshot: {
          comparatorName: "pixelmatch",
          comparatorOptions: {
            threshold: 0.2,
            allowedMismatchedPixels: 100,
          },
          resolveScreenshotPath: ({ arg, browserName, ext, testFileName }) =>
            `custom-screenshots/${testFileName}/${arg}-${browserName}${ext}`,
        },
      },
    },
  },
});
```

[`toMatchScreenshot` assertion](https://vitest.dev/api/browser/assertions#options)에서 사용 가능한
[모든 옵션]은 여기서 설정할 수 있습니다. 추가로 두 가지 경로 해석 함수인
`resolveScreenshotPath`와 `resolveDiffPath`를 사용할 수 있습니다.

#### browser.expect.toMatchScreenshot.resolveScreenshotPath

- **Type:** `(data: PathResolveData) => string`
- **Default output:** `` `${root}/${testFileDirectory}/${screenshotDirectory}/${testFileName}/${arg}-${browserName}-${platform}${ext}` ``

참조 스크린샷 저장 위치를 커스터마이즈하는 함수입니다. 함수는 다음 속성을 가진
객체를 받습니다:

- `arg: string`

  확장자를 제외한 경로로, sanitize되어 테스트 파일 기준 상대 경로입니다.

  `toMatchScreenshot`에 전달된 인자에서 오며, 인자 없이 호출되면 자동 생성된 이름이 됩니다.

  ```ts
  test("calls `onClick`", () => {
    expect(locator).toMatchScreenshot();
    // arg = "calls-onclick-1"
  });

  expect(locator).toMatchScreenshot("foo/bar/baz.png");
  // arg = "foo/bar/baz"

  expect(locator).toMatchScreenshot("../foo/bar/baz.png");
  // arg = "foo/bar/baz"
  ```

- `ext: string`

  점(`.`)을 포함한 screenshot 확장자입니다.

  `toMatchScreenshot`에 전달된 인자로 설정할 수 있지만, 지원되지 않는 확장자를 사용하면
  값은 `'.png'`로 fallback됩니다.

- `browserName: string`

  인스턴스의 브라우저 이름입니다.

- `platform: NodeJS.Platform`

  [`process.platform`](https://nodejs.org/docs/v22.16.0/api/process.html#processplatform)의
  값입니다.

- `screenshotDirectory: string`

  [`browser.screenshotDirectory`](https://vitest.dev/config/browser/screenshotdirectory)에 제공된 값이며,
  제공되지 않으면 기본값입니다.

- `root: string`

  프로젝트 [`root`](https://vitest.dev/config/#root)의 절대 경로입니다.

- `testFileDirectory: string`

  프로젝트 [`root`](https://vitest.dev/config/#root) 기준 테스트 파일 경로입니다.

- `testFileName: string`

  테스트 파일명입니다.

- `testName: string`

  상위 [`describe`](https://vitest.dev/api/#describe)를 포함한 [`test`](https://vitest.dev/api/#test) 이름이며,
  sanitize된 값입니다.

- `attachmentsDir: string`

  [`attachmentsDir`](https://vitest.dev/config/#attachmentsdir)에 제공된 값이며,
  제공되지 않으면 기본값입니다.

예를 들어 브라우저별로 스크린샷을 그룹화하려면:

```ts
resolveScreenshotPath: ({ arg, browserName, ext, root, testFileName }) =>
  `${root}/screenshots/${browserName}/${testFileName}/${arg}${ext}`;
```

#### browser.expect.toMatchScreenshot.resolveDiffPath

- **Type:** `(data: PathResolveData) => string`
- **Default output:** `` `${root}/${attachmentsDir}/${testFileDirectory}/${testFileName}/${arg}-${browserName}-${platform}${ext}` ``

screenshot 비교가 실패했을 때 diff 이미지를 저장할 위치를 커스터마이즈하는 함수입니다.
[`resolveScreenshotPath`](#browser-expect-tomatchscreenshot-resolvescreenshotpath)와
동일한 데이터 객체를 받습니다.

예를 들어 attachments의 하위 디렉터리에 diff를 저장하려면:

```ts
resolveDiffPath: ({
  arg,
  attachmentsDir,
  browserName,
  ext,
  root,
  testFileName,
}) =>
  `${root}/${attachmentsDir}/screenshot-diffs/${testFileName}/${arg}-${browserName}${ext}`;
```

#### browser.expect.toMatchScreenshot.comparators

- **Type:** `Record<string, Comparator>`

[SSIM](https://en.wikipedia.org/wiki/Structural_similarity_index_measure)이나 기타 지각적 유사도 metric 같은 custom screenshot 비교 알고리즘을 등록합니다.

custom comparator를 만들려면 config에 등록해야 합니다. TypeScript를 사용한다면 `ScreenshotComparatorRegistry` interface에 해당 옵션을 선언하세요.

```ts
import { defineConfig } from "vitest/config";

// 1. Declare the comparator's options type
declare module "vitest/browser" {
  interface ScreenshotComparatorRegistry {
    myCustomComparator: {
      sensitivity?: number;
      ignoreColors?: boolean;
    };
  }
}

// 2. Implement the comparator
export default defineConfig({
  test: {
    browser: {
      expect: {
        toMatchScreenshot: {
          comparators: {
            myCustomComparator: async (
              reference,
              actual,
              {
                createDiff, // always provided by Vitest
                sensitivity = 0.01,
                ignoreColors = false,
              },
            ) => {
              // ...algorithm implementation
              return { pass, diff, message };
            },
          },
        },
      },
    },
  },
});
```

그다음 테스트에서 사용합니다:

```ts
await expect(locator).toMatchScreenshot({
  comparatorName: "myCustomComparator",
  comparatorOptions: {
    sensitivity: 0.08,
    ignoreColors: true,
  },
});
```

**Comparator Function Signature:**

```ts
type Comparator<Options> = (
  reference: {
    metadata: { height: number; width: number };
    data: TypedArray;
  },
  actual: {
    metadata: { height: number; width: number };
    data: TypedArray;
  },
  options: {
    createDiff: boolean;
  } & Options,
) =>
  | Promise<{
      pass: boolean;
      diff: TypedArray | null;
      message: string | null;
    }>
  | {
      pass: boolean;
      diff: TypedArray | null;
      message: string | null;
    };
```

`reference`와 `actual` 이미지는 적절한 codec(현재는 PNG만 지원)으로 디코딩됩니다. `data` 속성은 RGBA 형식의 픽셀 데이터를 담은 평탄한 `TypedArray`(`Buffer`, `Uint8Array`, 또는 `Uint8ClampedArray`)입니다:

- **픽셀당 4바이트**: red, green, blue, alpha (각각 `0`부터 `255`)
- **행 우선 순서(Row-major order)**: 픽셀은 왼쪽에서 오른쪽, 위에서 아래 순서로 저장
- **전체 길이**: `width × height × 4` bytes
- **알파 채널**: 항상 존재. 투명도가 없는 이미지는 alpha 값이 `255`(완전 불투명)로 설정됨

::: tip Performance Considerations
`createDiff` 옵션은 diff 이미지가 필요한지 여부를 나타냅니다. [stable screenshot detection](https://vitest.dev/guide/browser/visual-regression-testing#how-visual-tests-work) 중에 Vitest는 불필요한 작업을 피하기 위해 `createDiff: false`로 comparator를 호출합니다.

**테스트를 빠르게 유지하려면 이 플래그를 반드시 준수하세요**.
:::

::: warning Handle Missing Options
`toMatchScreenshot()`의 `options` 파라미터는 optional이므로, 사용자가 comparator 옵션을 모두 제공하지 않을 수 있습니다. 항상 기본값과 함께 optional로 처리하세요:

```ts
myCustomComparator: (
  reference,
  actual,
  { createDiff, threshold = 0.1, maxDiff = 100 },
) => {
  // ...comparison logic
};
```

:::
