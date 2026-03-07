---
title: "coverage {#coverage}"
description: "커버리지 수집에는 , , 또는 사용자 정의 커버리지 솔루션을 사용할 수 있습니다."
---

출처 URL: https://vitest.dev/config/coverage

# coverage {#coverage}

커버리지 수집에는 [`v8`](https://vitest.dev/guide/coverage.html#v8-provider), [`istanbul`](https://vitest.dev/guide/coverage.html#istanbul-provider), 또는 [사용자 정의 커버리지 솔루션](https://vitest.dev/guide/coverage#custom-coverage-provider)을 사용할 수 있습니다.

점 표기법(dot notation)으로 CLI에 커버리지 옵션을 전달할 수 있습니다:

```sh
npx vitest --coverage.enabled --coverage.provider=istanbul
```

::: warning
점 표기법으로 커버리지 옵션을 사용할 때는 `--coverage.enabled`를 반드시 지정하세요. 이 경우 단일 `--coverage` 옵션은 사용하지 마세요.
:::

## coverage.provider

- **Type:** `'v8' | 'istanbul' | 'custom'`
- **Default:** `'v8'`
- **CLI:** `--coverage.provider=<provider>`

`provider`를 사용해 커버리지 수집 도구를 선택합니다.

## coverage.enabled

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.enabled`, `--coverage.enabled=false`

커버리지 수집을 활성화합니다. `--coverage` CLI 옵션으로 재정의할 수 있습니다.

## coverage.include

- **Type:** `string[]`
- **Default:** 테스트 실행 중 import된 파일
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.include=<pattern>`, `--coverage.include=<pattern1> --coverage.include=<pattern2>`

커버리지에 포함할 파일 목록을 glob 패턴으로 지정합니다. 기본적으로는 테스트에서 커버된 파일만 포함됩니다.

패턴에 파일 확장자를 포함하는 것을 권장합니다.

예시는 [Including and excluding files from coverage report](https://vitest.dev/guide/coverage.html#including-and-excluding-files-from-coverage-report)를 참고하세요.

## coverage.exclude

- **Type:** `string[]`
- **Default:** : `[]`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.exclude=<path>`, `--coverage.exclude=<path1> --coverage.exclude=<path2>`

커버리지에서 제외할 파일 목록을 glob 패턴으로 지정합니다.

예시는 [Including and excluding files from coverage report](https://vitest.dev/guide/coverage.html#including-and-excluding-files-from-coverage-report)를 참고하세요.

## coverage.clean

- **Type:** `boolean`
- **Default:** `true`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.clean`, `--coverage.clean=false`

테스트 실행 전에 커버리지 결과를 정리합니다.

## coverage.cleanOnRerun

- **Type:** `boolean`
- **Default:** `true`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.cleanOnRerun`, `--coverage.cleanOnRerun=false`

watch 재실행 시 커버리지 리포트를 정리합니다. watch 모드에서 이전 실행의 커버리지 결과를 유지하려면 `false`로 설정하세요.

## coverage.reportsDirectory

- **Type:** `string`
- **Default:** `'./coverage'`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.reportsDirectory=<path>`

::: warning
`coverage.clean`이 활성화되어 있으면(기본값), Vitest는 테스트 실행 전에 이 디렉터리를 삭제합니다.
:::

커버리지 리포트를 기록할 디렉터리입니다.

[HTML reporter](https://vitest.dev/guide/reporters.html#html-reporter) 출력에서 커버리지 리포트를 미리 보려면, 이 옵션은 html 리포트 디렉터리의 하위 디렉터리로 설정해야 합니다(예: `./html/coverage`).

## coverage.reporter

- **Type:** `string | string[] | [string, {}][]`
- **Default:** `['text', 'html', 'clover', 'json']`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.reporter=<reporter>`, `--coverage.reporter=<reporter1> --coverage.reporter=<reporter2>`

사용할 커버리지 리포터입니다. 전체 리포터 목록은 [istanbul documentation](https://istanbul.js.org/docs/advanced/alternative-reporters/)을 참고하세요. 리포터별 옵션은 [`@types/istanbul-reporter`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/276d95e4304b3670eaf6e8e5a7ea9e265a14e338/types/istanbul-reports/index.d.ts)를 참고하세요.

리포터는 세 가지 형태를 지원합니다:

- 단일 리포터: `{ reporter: 'html' }`
- 옵션 없는 다중 리포터: `{ reporter: ['html', 'json'] }`
- 리포터 옵션이 포함된 단일 또는 다중 리포터:
  ```ts
  {
    reporter: [
      ["lcov", { projectRoot: "./src" }],
      ["json", { file: "coverage.json" }],
      ["text"],
    ];
  }
  ```

사용자 정의 커버리지 리포터도 전달할 수 있습니다. 자세한 내용은 [Guide - Custom Coverage Reporter](https://vitest.dev/guide/coverage#custom-coverage-reporter)를 참고하세요.

```ts
{
  reporter: [
    // Specify reporter using name of the NPM package
    "@vitest/custom-coverage-reporter",
    ["@vitest/custom-coverage-reporter", { someOption: true }],

    // Specify reporter using local path
    "/absolute/path/to/custom-reporter.cjs",
    ["/absolute/path/to/custom-reporter.cjs", { someOption: true }],
  ];
}
```

Vitest UI에서 커버리지 리포트를 확인할 수도 있습니다. 자세한 내용은 [Vitest UI Coverage](https://vitest.dev/guide/coverage#vitest-ui)를 참고하세요.

## coverage.reportOnFailure {#coverage-reportonfailure}

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.reportOnFailure`, `--coverage.reportOnFailure=false`

테스트가 실패해도 커버리지 리포트를 생성합니다.

## coverage.allowExternal

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.allowExternal`, `--coverage.allowExternal=false`

[project `root`](#root) 외부 파일의 커버리지를 수집합니다.

## coverage.excludeAfterRemap

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.excludeAfterRemap`, `--coverage.excludeAfterRemap=false`

커버리지를 원본 소스로 remap한 뒤 제외 규칙을 다시 적용합니다.
소스 파일이 트랜스파일되어 비소스 파일의 source map을 포함할 수 있는 경우 유용합니다.

`coverage.exclude` 패턴과 일치하는데도 리포트에 파일이 표시된다면 이 옵션을 사용하세요.

## coverage.skipFull

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.skipFull`, `--coverage.skipFull=false`

statement, branch, function 커버리지가 모두 100%인 파일은 표시하지 않습니다.

## coverage.thresholds

커버리지 임계값(threshold) 옵션입니다.

임계값을 양수로 설정하면 필요한 최소 커버리지 비율로 해석됩니다. 예를 들어 lines 임계값을 `90`으로 설정하면, 라인의 90%가 커버되어야 합니다.

임계값을 음수로 설정하면 허용되는 미커버 항목의 최대 개수로 해석됩니다. 예를 들어 lines 임계값을 `-10`으로 설정하면, 미커버 라인은 10개를 초과할 수 없습니다.

```ts
{
  coverage: {
    thresholds: {
      // Requires 90% function coverage
      functions: 90,

      // Require that no more than 10 lines are uncovered
      lines: -10,
    }
  }
}
```

### coverage.thresholds.lines

- **Type:** `number`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.lines=<number>`

라인에 대한 전역 임계값입니다.

### coverage.thresholds.functions

- **Type:** `number`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.functions=<number>`

함수에 대한 전역 임계값입니다.

### coverage.thresholds.branches

- **Type:** `number`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.branches=<number>`

브랜치에 대한 전역 임계값입니다.

### coverage.thresholds.statements

- **Type:** `number`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.statements=<number>`

statement에 대한 전역 임계값입니다.

### coverage.thresholds.perFile

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.perFile`, `--coverage.thresholds.perFile=false`

파일별로 임계값을 검사합니다.

### coverage.thresholds.autoUpdate

- **Type:** `boolean | function`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.autoUpdate=<boolean>`

현재 커버리지가 설정된 임계값보다 좋으면 `lines`, `functions`, `branches`, `statements`의 모든 임계값을 설정 파일에 업데이트합니다.
이 옵션은 커버리지가 개선될 때 임계값을 유지 관리하는 데 도움이 됩니다.

업데이트된 임계값 값을 포맷하기 위한 함수를 전달할 수도 있습니다:

```ts
{
  coverage: {
    thresholds: {
      // Update thresholds without decimals
      autoUpdate: (newThreshold) => Math.floor(newThreshold),

      // 95.85 -> 95
      functions: 95,
    }
  }
}
```

### coverage.thresholds.100

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.thresholds.100`, `--coverage.thresholds.100=false`

전역 임계값을 100으로 설정합니다.
`--coverage.thresholds.lines 100 --coverage.thresholds.functions 100 --coverage.thresholds.branches 100 --coverage.thresholds.statements 100`의 단축 옵션입니다.

### coverage.thresholds[glob-pattern]

- **Type:** `{ statements?: number functions?: number branches?: number lines?: number }`
- **Default:** `undefined`
- **Available for providers:** `'v8' | 'istanbul'`

glob 패턴과 일치하는 파일에 대한 임계값을 설정합니다.

::: tip NOTE
Vitest는 glob-pattern으로 커버된 파일을 포함한 모든 파일을 전역 커버리지 임계값에 포함해 계산합니다.
이는 Jest 동작과 다릅니다.
:::

```ts
{
  coverage: {
    thresholds: {
      // Thresholds for all files
      functions: 95,
      branches: 70,

      // Thresholds for matching glob pattern
      'src/utils/**.ts': {
        statements: 95,
        functions: 90,
        branches: 85,
        lines: 80,
      },

      // Files matching this pattern will only have lines thresholds set.
      // Global thresholds are not inherited.
      '**/math.ts': {
        lines: 100,
      }
    }
  }
}
```

### coverage.thresholds[glob-pattern].100

- **Type:** `boolean`
- **Default:** `false`
- **Available for providers:** `'v8' | 'istanbul'`

glob 패턴과 일치하는 파일의 임계값을 100으로 설정합니다.

```ts
{
  coverage: {
    thresholds: {
      // Thresholds for all files
      functions: 95,
      branches: 70,

      // Thresholds for matching glob pattern
      'src/utils/**.ts': { 100: true },
      '**/math.ts': { 100: true }
    }
  }
}
```

## coverage.ignoreClassMethods

- **Type:** `string[]`
- **Default:** `[]`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.ignoreClassMethods=<method>`

커버리지에서 무시할 클래스 메서드 이름 배열을 설정합니다.
자세한 내용은 [istanbul documentation](https://github.com/istanbuljs/nyc#ignoring-methods)을 참고하세요.

## coverage.watermarks

- **Type:**

```ts
{
  statements?: [number, number],
  functions?: [number, number],
  branches?: [number, number],
  lines?: [number, number]
}
```

- **Default:**

```ts
{
  statements: [50, 80],
  functions: [50, 80],
  branches: [50, 80],
  lines: [50, 80]
}
```

- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.watermarks.statements=50,80`, `--coverage.watermarks.branches=50,80`

statements, lines, branches, functions에 대한 워터마크입니다. 자세한 내용은 [istanbul documentation](https://github.com/istanbuljs/nyc#high-and-low-watermarks)을 참고하세요.

## coverage.processingConcurrency

- **Type:** `boolean`
- **Default:** `Math.min(20, os.availableParallelism?.() ?? os.cpus().length)`
- **Available for providers:** `'v8' | 'istanbul'`
- **CLI:** `--coverage.processingConcurrency=<number>`

커버리지 결과 처리 시 사용하는 동시성 한도입니다.

## coverage.customProviderModule

- **Type:** `string`
- **Available for providers:** `'custom'`
- **CLI:** `--coverage.customProviderModule=<path or module name>`

사용자 정의 커버리지 provider 모듈의 모듈 이름 또는 경로를 지정합니다. 자세한 내용은 [Guide - Custom Coverage Provider](https://vitest.dev/guide/coverage#custom-coverage-provider)를 참고하세요.
