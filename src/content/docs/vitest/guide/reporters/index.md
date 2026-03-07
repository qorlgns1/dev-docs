---
title: "리포터 출력"
description: "Vitest는 다양한 형식으로 테스트 출력을 표시할 수 있도록 여러 내장 리포터를 제공하며, 커스텀 리포터를 사용할 수도 있습니다. 리포터는  명령줄 옵션을 사용하거나 configuration file에  속성을 포함해 선택할 수 있습니다. 리포터를 지정하지 않으면 아..."
---

출처 URL: https://vitest.dev/guide/reporters

# 리포터

Vitest는 다양한 형식으로 테스트 출력을 표시할 수 있도록 여러 내장 리포터를 제공하며, 커스텀 리포터를 사용할 수도 있습니다. 리포터는 `--reporter` 명령줄 옵션을 사용하거나 [configuration file](https://vitest.dev/config/#reporters)에 `reporters` 속성을 포함해 선택할 수 있습니다. 리포터를 지정하지 않으면 아래 설명된 `default` 리포터가 사용됩니다.

명령줄에서 리포터 사용:

```bash
npx vitest --reporter=verbose
```

[`vitest.config.ts`](https://vitest.dev/config/)를 통한 리포터 사용:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    reporters: ["verbose"],
  },
});
```

일부 리포터는 추가 옵션을 전달해 커스터마이즈할 수 있습니다. 리포터별 옵션은 아래 섹션에서 설명합니다.

```ts
export default defineConfig({
  test: {
    reporters: ["default", ["junit", { suiteName: "UI tests" }]],
  },
});
```

## 리포터 출력

기본적으로 Vitest의 리포터는 터미널에 출력을 표시합니다. `json`, `html`, `junit` 리포터를 사용할 때는 Vite 설정 파일 또는 CLI에서 `outputFile` [configuration option](https://vitest.dev/config/#outputfile)을 지정해 테스트 출력을 파일로 쓸 수 있습니다.

:::code-group

```bash [CLI]
npx vitest --reporter=json --outputFile=./test-output.json
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["json"],
    outputFile: "./test-output.json",
  },
});
```

:::

## 리포터 조합

여러 리포터를 동시에 사용해 테스트 결과를 다양한 형식으로 출력할 수 있습니다. 예를 들어:

```bash
npx vitest --reporter=json --reporter=default
```

```ts
export default defineConfig({
  test: {
    reporters: ["json", "default"],
    outputFile: "./test-output.json",
  },
});
```

위 예시는 테스트 결과를 기본 스타일로 터미널에 출력하는 동시에, 지정된 출력 파일에 JSON으로 기록합니다.

여러 리포터를 사용할 때는 다음과 같이 여러 출력 파일을 지정할 수도 있습니다:

```ts
export default defineConfig({
  test: {
    reporters: ["junit", "json", "verbose"],
    outputFile: {
      junit: "./junit-report.xml",
      json: "./json-report.json",
    },
  },
});
```

이 예시는 JSON 및 XML 리포트를 각각 생성하고, 터미널에는 verbose 리포트를 출력합니다.

## 내장 리포터

### Default Reporter

기본값(즉, 리포터를 지정하지 않은 경우)에서는 Vitest가 실행 중인 테스트와 상태의 요약을 하단에 표시합니다. 스위트가 통과하면 해당 상태가 요약 위쪽에 보고됩니다.

리포터 설정으로 요약 표시를 비활성화할 수 있습니다:

:::code-group

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: [["default", { summary: false }]],
  },
});
```

:::

테스트 진행 중 출력 예시:

```bash
 ✓ test/example-1.test.ts (5 tests | 1 skipped) 306ms
 ✓ test/example-2.test.ts (5 tests | 1 skipped) 307ms

 ❯ test/example-3.test.ts 3/5
 ❯ test/example-4.test.ts 1/5

 Test Files 2 passed (4)
      Tests 10 passed | 3 skipped (65)
   Start at 11:01:36
   Duration 2.00s
```

테스트 완료 후 최종 출력:

```bash
 ✓ test/example-1.test.ts (5 tests | 1 skipped) 306ms
 ✓ test/example-2.test.ts (5 tests | 1 skipped) 307ms
 ✓ test/example-3.test.ts (5 tests | 1 skipped) 307ms
 ✓ test/example-4.test.ts (5 tests | 1 skipped) 307ms

 Test Files  4 passed (4)
      Tests  16 passed | 4 skipped (20)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

실행 중인 테스트 파일이 하나뿐이면 Vitest는 해당 파일의 전체 테스트 트리를 [`tree`](#tree-reporter) 리포터와 비슷하게 출력합니다. 또한 파일 내에 실패한 테스트가 하나 이상 있으면 default 리포터도 테스트 트리를 출력합니다.

```bash
✓ __tests__/file1.test.ts (2) 725ms
   ✓ first test file (2) 725ms
     ✓ 2 + 2 should equal 4
     ✓ 4 - 2 should equal 2

 Test Files  1 passed (1)
      Tests  2 passed (2)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

### Verbose Reporter

verbose 리포터는 각 테스트 케이스가 완료될 때마다 출력합니다. 스위트나 파일을 별도로 보고하지는 않습니다. `--includeTaskLocation`이 활성화되어 있으면 출력에 각 테스트의 위치도 포함됩니다. `default` 리포터와 마찬가지로 설정을 통해 요약 표시를 비활성화할 수 있습니다.

또한 `verbose` 리포터는 테스트 오류 메시지를 즉시 출력합니다. 전체 테스트 오류는 테스트 실행이 끝났을 때 보고됩니다.

이 리포터는 테스트가 실패하지 않아도 [annotations](https://vitest.dev/guide/test-annotations)을 보고하는 유일한 터미널 리포터입니다.

:::code-group

```bash [CLI]
npx vitest --reporter=verbose
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: [["verbose", { summary: false }]],
  },
});
```

:::

출력 예시:

```bash
✓ __tests__/file1.test.ts > first test file > 2 + 2 should equal 4 1ms
✓ __tests__/file1.test.ts > first test file > 4 - 2 should equal 2 1ms
✓ __tests__/file2.test.ts > second test file > 1 + 1 should equal 2 1ms
✓ __tests__/file2.test.ts > second test file > 2 - 1 should equal 1 1ms

 Test Files  2 passed (2)
      Tests  4 passed (4)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

`--includeTaskLocation` 사용 예시:

```bash
✓ __tests__/file1.test.ts:2:1 > first test file > 2 + 2 should equal 4 1ms
✓ __tests__/file1.test.ts:3:1 > first test file > 4 - 2 should equal 2 1ms
✓ __tests__/file2.test.ts:2:1 > second test file > 1 + 1 should equal 2 1ms
✓ __tests__/file2.test.ts:3:1 > second test file > 2 - 1 should equal 1 1ms

 Test Files  2 passed (2)
      Tests  4 passed (4)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

### Tree Reporter

tree 리포터는 `default` 리포터와 동일하지만, 스위트가 완료된 뒤 각 개별 테스트도 표시합니다. `default` 리포터와 마찬가지로 설정을 통해 요약 표시를 비활성화할 수 있습니다.

:::code-group

```bash [CLI]
npx vitest --reporter=tree
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: [["tree", { summary: false }]],
  },
});
```

:::

기본 `slowTestThreshold: 300`에서 테스트 진행 중 출력 예시:

```bash
 ✓ __tests__/example-1.test.ts (2) 725ms
   ✓ first test file (2) 725ms
     ✓ 2 + 2 should equal 4
     ✓ 4 - 2 should equal 2

 ❯ test/example-2.test.ts 3/5
   ↳ should run longer than three seconds 1.57s
 ❯ test/example-3.test.ts 1/5

 Test Files 2 passed (4)
      Tests 10 passed | 3 skipped (65)
   Start at 11:01:36
   Duration 2.00s
```

통과한 테스트 스위트의 최종 터미널 출력 예시:

```bash
✓ __tests__/file1.test.ts (2) 725ms
   ✓ first test file (2) 725ms
     ✓ 2 + 2 should equal 4
     ✓ 4 - 2 should equal 2
✓ __tests__/file2.test.ts (2) 746ms
  ✓ second test file (2) 746ms
    ✓ 1 + 1 should equal 2
    ✓ 2 - 1 should equal 1

 Test Files  2 passed (2)
      Tests  4 passed (4)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

### Dot Reporter

완료된 테스트마다 점 하나를 출력하여, 실행된 모든 테스트를 보여주면서도 출력을 최소화합니다. 상세 정보는 실패한 테스트에 대해서만 제공되며, 스위트 요약도 함께 표시됩니다.

:::code-group

```bash [CLI]
npx vitest --reporter=dot
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["dot"],
  },
});
```

:::

통과한 테스트 스위트의 터미널 출력 예시:

```bash
....

 Test Files  2 passed (2)
      Tests  4 passed (4)
   Start at  12:34:32
   Duration  1.26s (transform 35ms, setup 1ms, collect 90ms, tests 1.47s, environment 0ms, prepare 267ms)
```

### JUnit Reporter

테스트 결과를 JUnit XML 형식으로 출력합니다. 터미널에 출력하거나 [`outputFile`](https://vitest.dev/config/#outputfile) configuration option을 사용해 XML 파일로 쓸 수 있습니다.

:::code-group

```bash [CLI]
npx vitest --reporter=junit
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["junit"],
  },
});
```

:::

JUnit XML 리포트 예시:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<testsuites name="vitest tests" tests="2" failures="1" errors="0" time="0.503">
    <testsuite name="__tests__/test-file-1.test.ts" timestamp="2023-10-19T17:41:58.580Z" hostname="My-Computer.local" tests="2" failures="1" errors="0" skipped="0" time="0.013">
        <testcase classname="__tests__/test-file-1.test.ts" name="first test file &gt; 2 + 2 should equal 4" time="0.01">
            <failure message="expected 5 to be 4 // Object.is equality" type="AssertionError">
AssertionError: expected 5 to be 4 // Object.is equality
 ❯ __tests__/test-file-1.test.ts:20:28
            </failure>
        </testcase>
        <testcase classname="__tests__/test-file-1.test.ts" name="first test file &gt; 4 - 2 should equal 2" time="0">
        </testcase>
    </testsuite>
</testsuites>
```

출력된 XML에는 중첩된 `testsuites` 및 `testcase` 태그가 포함됩니다. 이는 리포터 옵션 `suiteName`과 `classnameTemplate`로 커스터마이즈할 수도 있습니다. `classnameTemplate`은 템플릿 문자열 또는 함수가 될 수 있습니다.

`classnameTemplate` 옵션에서 지원되는 플레이스홀더는 다음과 같습니다:

- filename
- filepath

```ts
export default defineConfig({
  test: {
    reporters: [
      [
        "junit",
        {
          suiteName: "custom suite name",
          classnameTemplate: "filename:{filename} - filepath:{filepath}",
        },
      ],
    ],
  },
});
```

### JSON Reporter

테스트 결과를 Jest의 `--json` 옵션과 호환되는 JSON 형식 리포트로 생성합니다. 터미널에 출력하거나 [`outputFile`](https://vitest.dev/config/#outputfile) configuration option을 사용해 파일로 쓸 수 있습니다.

:::code-group

```bash [CLI]
npx vitest --reporter=json
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["json"],
  },
});
```

:::

JSON 리포트 예시:

```json
{
  "numTotalTestSuites": 4,
  "numPassedTestSuites": 2,
  "numFailedTestSuites": 1,
  "numPendingTestSuites": 1,
  "numTotalTests": 4,
  "numPassedTests": 1,
  "numFailedTests": 1,
  "numPendingTests": 1,
  "numTodoTests": 1,
  "startTime": 1697737019307,
  "success": false,
  "testResults": [
    {
      "assertionResults": [
        {
          "ancestorTitles": ["", "first test file"],
          "fullName": " first test file 2 + 2 should equal 4",
          "status": "failed",
          "title": "2 + 2 should equal 4",
          "duration": 9,
          "failureMessages": ["expected 5 to be 4 // Object.is equality"],
          "location": {
            "line": 20,
            "column": 28
          },
          "meta": {}
        }
      ],
      "startTime": 1697737019787,
      "endTime": 1697737019797,
      "status": "failed",
      "message": "",
      "name": "/root-directory/__tests__/test-file-1.test.ts"
    }
  ],
  "coverageMap": {}
}
```

::: info
Vitest 3부터, coverage가 활성화된 경우 JSON 리포터는 `coverageMap`에 coverage 정보를 포함합니다.
:::

### HTML Reporter

대화형 [GUI](https://vitest.dev/guide/ui)로 테스트 결과를 볼 수 있는 HTML 파일을 생성합니다. 파일 생성 후 Vitest는 로컬 개발 서버를 계속 실행하며, 브라우저에서 리포트를 볼 수 있는 링크를 제공합니다.

출력 파일은 [`outputFile`](https://vitest.dev/config/#outputfile) configuration option으로 지정할 수 있습니다. `outputFile` 옵션을 제공하지 않으면 새로운 HTML 파일이 생성됩니다.

:::code-group

```bash [CLI]
npx vitest --reporter=html
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["html"],
  },
});
```

:::

::: tip
이 리포터를 사용하려면 [`@vitest/ui`](https://vitest.dev/guide/ui) 패키지가 설치되어 있어야 합니다.
:::

### TAP Reporter

[Test Anything Protocol](https://testanything.org/) (TAP)을 따르는 리포트를 출력합니다.

:::code-group

```bash [CLI]
npx vitest --reporter=tap
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["tap"],
  },
});
```

:::

TAP 리포트 예시:

```bash
TAP version 13
1..1
not ok 1 - __tests__/test-file-1.test.ts # time=14.00ms {
    1..1
    not ok 1 - first test file # time=13.00ms {
        1..2
        not ok 1 - 2 + 2 should equal 4 # time=11.00ms
            ---
            error:
                name: "AssertionError"
                message: "expected 5 to be 4 // Object.is equality"
            at: "/root-directory/__tests__/test-file-1.test.ts:20:28"
            actual: "5"
            expected: "4"
            ...
        ok 2 - 4 - 2 should equal 2 # time=1.00ms
    }
}
```

### TAP Flat Reporter

TAP flat 리포트를 출력합니다. `tap` 리포터와 마찬가지로 테스트 결과는 TAP 표준을 따르도록 포맷되지만, 테스트 스위트는 중첩 계층 대신 평탄한 목록으로 포맷됩니다.

:::code-group

```bash [CLI]
npx vitest --reporter=tap-flat
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["tap-flat"],
  },
});
```

:::

TAP flat 리포트 예시:

```bash
TAP version 13
1..2
not ok 1 - __tests__/test-file-1.test.ts > first test file > 2 + 2 should equal 4 # time=11.00ms
    ---
    error:
        name: "AssertionError"
        message: "expected 5 to be 4 // Object.is equality"
    at: "/root-directory/__tests__/test-file-1.test.ts:20:28"
    actual: "5"
    expected: "4"
    ...
ok 2 - __tests__/test-file-1.test.ts > first test file > 4 - 2 should equal 2 # time=0.00ms
```

### Hanging Process Reporter

Vitest가 안전하게 종료되지 못하도록 막는 프로세스가 있으면, 해당 hanging process 목록을 표시합니다. `hanging-process` 리포터 자체는 테스트 결과를 표시하지 않지만, 테스트 실행 중 프로세스를 모니터링하기 위해 다른 리포터와 함께 사용할 수 있습니다. 이 리포터는 리소스 사용량이 클 수 있으므로, 일반적으로 Vitest가 지속적으로 프로세스를 종료하지 못하는 상황에서 디버깅 목적으로 사용하는 것이 좋습니다.

:::code-group

```bash [CLI]
npx vitest --reporter=hanging-process
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["hanging-process"],
  },
});
```

:::

### GitHub Actions Reporter {#github-actions-reporter}

테스트 실패에 대한 annotation을 제공하기 위해 [workflow commands](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-error-message)를 출력합니다. 이 리포터는 `process.env.GITHUB_ACTIONS === 'true'`일 때 [`default`](#default-reporter) 리포터와 함께 자동으로 활성화됩니다.

기본이 아닌 리포터를 구성하는 경우 `github-actions`를 명시적으로 추가해야 합니다.

```ts
export default defineConfig({
  test: {
    reporters: process.env.GITHUB_ACTIONS ? ["dot", "github-actions"] : ["dot"],
  },
});
```

`onWritePath` 옵션을 사용하면 [GitHub's annotation command format](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)으로 출력되는 파일 경로를 커스터마이즈할 수 있습니다. 이는 Docker 같은 컨테이너 환경에서 Vitest를 실행할 때 파일 경로가 GitHub Actions 환경의 경로와 일치하지 않을 수 있어 유용합니다.

```ts
export default defineConfig({
  test: {
    reporters: process.env.GITHUB_ACTIONS
      ? [
          "default",
          [
            "github-actions",
            {
              onWritePath(path) {
                return path.replace(
                  /^\/app\//,
                  `${process.env.GITHUB_WORKSPACE}/`,
                );
              },
            },
          ],
        ]
      : ["default"],
  },
});
```

[Annotations API](https://vitest.dev/guide/test-annotations)를 사용 중이면, 리포터가 GitHub UI에 이를 자동으로 인라인 표시합니다. `displayAnnotations` 옵션을 `false`로 설정하면 비활성화할 수 있습니다:

```ts
export default defineConfig({
  test: {
    reporters: [["github-actions", { displayAnnotations: false }]],
  },
});
```

### Blob Reporter

테스트 결과를 머신에 저장해 나중에 [`--merge-reports`](https://vitest.dev/guide/cli#merge-reports) 명령으로 병합할 수 있게 합니다.
기본적으로 모든 결과를 `.vitest-reports` 폴더에 저장하며, `--outputFile` 또는 `--outputFile.blob` 플래그로 재정의할 수 있습니다.

```bash
npx vitest --reporter=blob --outputFile=reports/blob-1.json
```

[`--shard`](https://vitest.dev/guide/cli#shard) 플래그로 여러 머신에서 Vitest를 실행하는 경우 이 리포터 사용을 권장합니다.
CI 파이프라인 마지막에 `--merge-reports` 명령을 사용하면 모든 blob 리포트를 어떤 리포트로든 병합할 수 있습니다:

```bash
npx vitest --merge-reports=reports --reporter=json --reporter=default
```

::: tip
`--reporter=blob`와 `--merge-reports`는 모두 watch mode에서 동작하지 않습니다.
:::

## 커스텀 리포터

NPM에서 설치한 서드파티 커스텀 리포터는 reporters 옵션에 패키지 이름을 지정해 사용할 수 있습니다:

:::code-group

```bash [CLI]
npx vitest --reporter=some-published-vitest-reporter
```

```ts [vitest.config.ts]
export default defineConfig({
  test: {
    reporters: ["some-published-vitest-reporter"],
  },
});
```

:::

또한 직접 [custom reporters](https://vitest.dev/guide/advanced/reporters)를 정의하고 파일 경로를 지정해 사용할 수도 있습니다:

```bash
npx vitest --reporter=./path/to/reporter.ts
```

커스텀 리포터는 [Reporter interface](https://github.com/vitest-dev/vitest/blob/main/packages/vitest/src/node/types/reporter.ts)를 구현해야 합니다.
