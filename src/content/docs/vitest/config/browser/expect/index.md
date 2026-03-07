---
title: "browser.expect"
description: "이 옵션들은 모든 스크린샷 assertion에 적용됩니다."
---

출처 URL: https://vitest.dev/config/browser/expect

# browser.expect

- **타입:** `ExpectOptions`

## browser.expect.toMatchScreenshot

[`toMatchScreenshot` assertion](https://vitest.dev/api/browser/assertions.html#tomatchscreenshot)의 기본 옵션입니다.
이 옵션들은 모든 스크린샷 assertion에 적용됩니다.

::: tip
스크린샷 assertion의 전역 기본값을 설정하면 테스트 스위트 전반의 일관성을 유지하고 개별 테스트의 반복을 줄이는 데 도움이 됩니다. 특정 테스트 케이스에서 필요할 경우 assertion 수준에서 이 기본값을 여전히 재정의할 수 있습니다.
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

[`toMatchScreenshot` assertion](https://vitest.dev/api/browser/assertions#options)에서 사용할 수 있는
모든 옵션을 여기에서 설정할 수 있습니다. 추가로, 두 가지 경로 해석 함수인
`resolveScreenshotPath`와 `resolveDiffPath`를 사용할 수 있습니다.

## browser.expect.toMatchScreenshot.resolveScreenshotPath

- **타입:** `(data: PathResolveData) => string`
- **기본 출력:** `` `${root}/${testFileDirectory}/${screenshotDirectory}/${testFileName}/${arg}-${browserName}-${platform}${ext}` ``

참조 스크린샷이 저장되는 위치를 커스터마이즈하는 함수입니다. 이 함수는 다음 속성을 가진 객체를 전달받습니다.

- `arg: string`

  확장자를 제외한 경로이며, sanitize된 테스트 파일 기준 상대 경로입니다.

  이 값은 `toMatchScreenshot`에 전달된 인수에서 오며, 인수 없이 호출된 경우 자동 생성된 이름이 됩니다.

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

  점(`.`)을 포함한 스크린샷 확장자입니다.

  이 값은 `toMatchScreenshot`에 전달된 인수로 설정할 수 있지만, 지원되지 않는 확장자를 사용하면 `'.png'`로 대체됩니다.

- `browserName: string`

  인스턴스의 브라우저 이름입니다.

- `platform: NodeJS.Platform`

  [`process.platform`](https://nodejs.org/docs/v22.16.0/api/process.html#processplatform)의 값입니다.

- `screenshotDirectory: string`

  [`browser.screenshotDirectory`](https://vitest.dev/config/browser/screenshotdirectory)에 제공된 값이며,
  제공되지 않으면 기본값이 사용됩니다.

- `root: string`

  프로젝트 [`root`](https://vitest.dev/config/#root)의 절대 경로입니다.

- `testFileDirectory: string`

  프로젝트 [`root`](https://vitest.dev/config/#root) 기준 테스트 파일의 상대 경로입니다.

- `testFileName: string`

  테스트 파일 이름입니다.

- `testName: string`

  부모 [`describe`](https://vitest.dev/api/#describe)를 포함한 [`test`](https://vitest.dev/api/#test)의 이름이며, sanitize된 값입니다.

- `attachmentsDir: string`

  [`attachmentsDir`](https://vitest.dev/config/#attachmentsdir)에 제공된 값이며, 제공되지 않으면 기본값이 사용됩니다.

예를 들어, 브라우저별로 스크린샷을 그룹화하려면:

```ts
resolveScreenshotPath: ({ arg, browserName, ext, root, testFileName }) =>
  `${root}/screenshots/${browserName}/${testFileName}/${arg}${ext}`;
```

## browser.expect.toMatchScreenshot.resolveDiffPath

- **타입:** `(data: PathResolveData) => string`
- **기본 출력:** `` `${root}/${attachmentsDir}/${testFileDirectory}/${testFileName}/${arg}-${browserName}-${platform}${ext}` ``

스크린샷 비교가 실패했을 때 diff 이미지가 저장되는 위치를 커스터마이즈하는 함수입니다.
[`resolveScreenshotPath`](#browser-expect-tomatchscreenshot-resolvescreenshotpath)와 동일한 데이터 객체를 전달받습니다.

예를 들어, attachments의 하위 디렉터리에 diff를 저장하려면:

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

## browser.expect.toMatchScreenshot.comparators

- **타입:** `Record<string, Comparator>`

[SSIM](https://en.wikipedia.org/wiki/Structural_similarity_index_measure) 같은 알고리즘이나 다른 지각적 유사도 지표 등, 커스텀 스크린샷 비교 알고리즘을 등록합니다.

커스텀 comparator를 만들려면 config에 등록해야 합니다. TypeScript를 사용하는 경우 `ScreenshotComparatorRegistry` 인터페이스에 해당 옵션을 선언하세요.

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

**Comparator 함수 시그니처:**

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

`reference`와 `actual` 이미지는 적절한 codec(현재는 PNG만 지원)으로 디코딩됩니다. `data` 속성은 RGBA 형식의 픽셀 데이터를 담는 평면 `TypedArray`(`Buffer`, `Uint8Array`, 또는 `Uint8ClampedArray`)입니다.

- **픽셀당 4바이트**: red, green, blue, alpha (각 값은 `0`부터 `255`)
- **행 우선 순서(Row-major order)**: 픽셀은 왼쪽에서 오른쪽, 위에서 아래 순으로 저장됨
- **전체 길이**: `width × height × 4` 바이트
- **알파 채널**: 항상 존재함. 투명도가 없는 이미지는 alpha 값이 `255`(완전 불투명)로 설정됨

::: tip Performance Considerations
`createDiff` 옵션은 diff 이미지가 필요한지 여부를 나타냅니다. [stable screenshot detection](https://vitest.dev/guide/browser/visual-regression-testing#how-visual-tests-work) 중에 Vitest는 불필요한 작업을 피하기 위해 `createDiff: false`로 comparator를 호출합니다.

**테스트를 빠르게 유지하려면 이 플래그를 반드시 준수하세요**.
:::

::: warning Handle Missing Options
`toMatchScreenshot()`의 `options` 매개변수는 선택 사항이므로, 사용자가 comparator 옵션을 모두 제공하지 않을 수 있습니다. 항상 기본값과 함께 optional로 처리하세요:

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
