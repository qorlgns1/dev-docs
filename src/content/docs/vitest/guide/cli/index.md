---
title: "명령줄 인터페이스"
description: "현재 디렉터리에서 Vitest를 시작합니다. 개발 환경에서는 자동으로 watch 모드로, CI(또는 비대화형 터미널)에서는 run 모드로 진입합니다."
---

출처 URL: https://vitest.dev/guide/cli

# 명령줄 인터페이스

## 명령어

### `vitest`

현재 디렉터리에서 Vitest를 시작합니다. 개발 환경에서는 자동으로 watch 모드로, CI(또는 비대화형 터미널)에서는 run 모드로 진입합니다.

실행할 테스트 파일의 필터로 추가 인수를 전달할 수 있습니다. 예를 들어:

```bash
vitest foobar
```

경로에 `foobar`를 포함한 테스트 파일만 실행합니다. 이 필터는 포함 여부만 확인하며 regexp나 glob 패턴은 지원하지 않습니다(Vitest가 필터를 받기 전에 터미널이 이를 처리하는 경우는 예외).

Vitest 3부터는 파일명과 줄 번호로 테스트를 지정할 수도 있습니다:

```bash
$ vitest basic/foo.test.ts:10
```

::: warning
이 기능이 동작하려면 Vitest에 전체 파일명을 전달해야 합니다. 현재 작업 디렉터리 기준 상대 경로 또는 절대 파일 경로를 사용할 수 있습니다.

```bash
$ vitest basic/foo.js:10 # ✅
$ vitest ./basic/foo.js:10 # ✅
$ vitest /users/project/basic/foo.js:10 # ✅
$ vitest foo:10 # ❌
$ vitest ./basic/foo:10 # ❌
```

현재 Vitest는 범위 지정도 지원하지 않습니다:

```bash
$ vitest basic/foo.test.ts:10, basic/foo.test.ts:25 # ✅
$ vitest basic/foo.test.ts:10-25 # ❌
```

:::

### `vitest run`

watch 모드 없이 한 번만 실행합니다.

### `vitest watch`

모든 테스트 스위트를 실행하되 변경 사항을 감시하고 변경 시 테스트를 다시 실행합니다. 인수 없이 `vitest`를 호출하는 것과 동일합니다. CI 환경이거나 stdin이 TTY가 아닐 때(비대화형 환경)는 `vitest run`으로 대체됩니다.

### `vitest dev`

`vitest watch`의 별칭입니다.

### `vitest related`

소스 파일 목록을 커버하는 테스트만 실행합니다. 정적 import(예: `import('./index.js')` 또는 `import index from './index.js`)는 동작하지만, 동적 import(예: `import(filepath)`)는 동작하지 않습니다. 모든 파일은 루트 폴더 기준 상대 경로여야 합니다.

[`lint-staged`](https://github.com/okonet/lint-staged) 또는 CI 설정과 함께 사용하기 좋습니다.

```bash
vitest related /src/index.ts /src/hello-world.js
```

::: tip
Vitest는 기본적으로 watch 모드가 활성화된 상태로 실행된다는 점을 잊지 마세요. `lint-staged` 같은 도구를 사용 중이라면 명령이 정상 종료되도록 `--run` 옵션도 함께 전달해야 합니다.

```js [.lintstagedrc.js]
export default {
  "*.{js,ts}": "vitest related --run",
};
```

:::

### `vitest bench`

성능 결과를 비교하는 [benchmark](https://vitest.dev/guide/features.html#benchmarking) 테스트만 실행합니다.

### `vitest init`

`vitest init <name>`은 프로젝트 설정을 구성하는 데 사용할 수 있습니다. 현재는 [`browser`](https://vitest.dev/guide/browser/) 값만 지원합니다:

```bash
vitest init browser
```

### `vitest list`

`vitest list` 명령은 일치하는 모든 테스트 목록을 출력하기 위해 모든 `vitest` 옵션을 상속합니다. 이 명령은 `reporters` 옵션을 무시합니다. 기본적으로 파일 필터와 이름 패턴에 일치한 모든 테스트 이름을 출력합니다:

```shell
vitest list filename.spec.ts -t="some-test"
```

```txt
describe > some-test
describe > some-test > test 1
describe > some-test > test 2
```

`--json` 플래그를 전달해 테스트를 JSON 형식으로 출력하거나 별도 파일로 저장할 수 있습니다:

```bash
vitest list filename.spec.ts -t="some-test" --json=./file.json
```

`--json` 플래그에 값을 전달하지 않으면 JSON을 stdout으로 출력합니다.

`--filesOnly` 플래그를 전달해 테스트 파일만 출력할 수도 있습니다:

```bash
vitest list --filesOnly
```

```txt
tests/test1.test.ts
tests/test2.test.ts
```

## 옵션

::: tip
Vitest는 CLI 인수에서 camel case와 kebab case를 모두 지원합니다. 예를 들어 `--passWithNoTests`와 `--pass-with-no-tests`는 둘 다 동작합니다(`--no-color`와 `--inspect-brk`는 예외).

값 지정 방식도 여러 형태를 지원합니다. `--reporter dot`과 `--reporter=dot`은 모두 유효합니다.

옵션이 값 배열을 지원하는 경우, 해당 옵션을 여러 번 전달해야 합니다:

```
vitest --reporter=dot --reporter=default
```

불리언 옵션은 `no-` 접두사로 부정할 수 있습니다. 값을 `false`로 지정하는 방식도 동작합니다:

```
vitest --no-api
vitest --api=false
```

:::

### root

- **CLI:** `-r, --root <path>`
- **Config:** [root](https://vitest.dev/config/root)

루트 경로

### config

- **CLI:** `-c, --config <path>`

설정 파일 경로

### update

- **CLI:** `-u, --update`
- **Config:** [update](https://vitest.dev/config/update)

스냅샷 업데이트

### watch

- **CLI:** `-w, --watch`
- **Config:** [watch](https://vitest.dev/config/watch)

watch 모드 활성화

### testNamePattern

- **CLI:** `-t, --testNamePattern <pattern>`
- **Config:** [testNamePattern](https://vitest.dev/config/testnamepattern)

지정된 regexp 패턴과 전체 이름이 일치하는 테스트 실행

### dir

- **CLI:** `--dir <path>`
- **Config:** [dir](https://vitest.dev/config/dir)

테스트 파일을 스캔할 기본 디렉터리

### ui

- **CLI:** `--ui`

UI 활성화

### open

- **CLI:** `--open`
- **Config:** [open](https://vitest.dev/config/open)

UI 자동 열기 (기본값: `!process.env.CI`)

### api.port

- **CLI:** `--api.port [port]`

서버 포트를 지정합니다. 이미 사용 중인 포트라면 Vite가 자동으로 다음 사용 가능한 포트를 시도하므로, 실제 서버 리슨 포트와 다를 수 있습니다. `true`이면 `51204`로 설정됩니다.

### api.host

- **CLI:** `--api.host [host]`

서버가 수신할 IP 주소를 지정합니다. LAN 및 공인 주소를 포함한 모든 주소에서 수신하려면 `0.0.0.0` 또는 `true`로 설정하세요.

### api.strictPort

- **CLI:** `--api.strictPort`

포트가 이미 사용 중일 때 다음 포트를 자동으로 시도하지 않고 종료하려면 true로 설정합니다.

### silent

- **CLI:** `--silent [value]`
- **Config:** [silent](https://vitest.dev/config/silent)

테스트의 콘솔 출력을 표시하지 않습니다. 실패한 테스트의 로그만 보려면 `'passed-only'`를 사용하세요.

### hideSkippedTests

- **CLI:** `--hideSkippedTests`

건너뛴 테스트의 로그 숨기기

### reporters

- **CLI:** `--reporter <name>`
- **Config:** [reporters](https://vitest.dev/config/reporters)

리포터 지정 (default, blob, verbose, dot, json, tap, tap-flat, junit, tree, hanging-process, github-actions)

### outputFile

- **CLI:** `--outputFile <filename/-s>`
- **Config:** [outputFile](https://vitest.dev/config/outputfile)

supporter reporter가 함께 지정된 경우 테스트 결과를 파일에 기록합니다. 여러 reporter의 개별 출력에는 cac의 dot 표기법을 사용하세요(예: `--outputFile.tap=./tap.txt`)

### coverage.provider

- **CLI:** `--coverage.provider <name>`
- **Config:** [coverage.provider](https://vitest.dev/config/coverage#coverage-provider)

커버리지 수집 도구를 선택합니다. 사용 가능한 값: "v8", "istanbul", "custom"

### coverage.enabled

- **CLI:** `--coverage.enabled`
- **Config:** [coverage.enabled](https://vitest.dev/config/coverage#coverage-enabled)

커버리지 수집을 활성화합니다. `--coverage` CLI 옵션으로 덮어쓸 수 있습니다(기본값: `false`).

### coverage.include

- **CLI:** `--coverage.include <pattern>`
- **Config:** [coverage.include](https://vitest.dev/config/coverage#coverage-include)

커버리지에 포함할 파일을 glob 패턴으로 지정합니다. 여러 패턴을 사용할 때는 여러 번 지정할 수 있습니다. 기본적으로는 테스트가 커버한 파일만 포함됩니다.

### coverage.exclude

- **CLI:** `--coverage.exclude <pattern>`
- **Config:** [coverage.exclude](https://vitest.dev/config/coverage#coverage-exclude)

커버리지에서 제외할 파일입니다. 여러 확장자를 사용할 때는 여러 번 지정할 수 있습니다.

### coverage.clean

- **CLI:** `--coverage.clean`
- **Config:** [coverage.clean](https://vitest.dev/config/coverage#coverage-clean)

테스트 실행 전에 커버리지 결과를 정리합니다(기본값: true).

### coverage.cleanOnRerun

- **CLI:** `--coverage.cleanOnRerun`
- **Config:** [coverage.cleanOnRerun](https://vitest.dev/config/coverage#coverage-cleanonrerun)

watch 재실행 시 커버리지 리포트를 정리합니다(기본값: true).

### coverage.reportsDirectory

- **CLI:** `--coverage.reportsDirectory <path>`
- **Config:** [coverage.reportsDirectory](https://vitest.dev/config/coverage#coverage-reportsdirectory)

커버리지 리포트를 기록할 디렉터리(기본값: ./coverage)

### coverage.reporter

- **CLI:** `--coverage.reporter <name>`
- **Config:** [coverage.reporter](https://vitest.dev/config/coverage#coverage-reporter)

사용할 커버리지 리포터입니다. 자세한 내용은 [`coverage.reporter`](https://vitest.dev/config/#coverage-reporter)를 참고하세요(기본값: `["text", "html", "clover", "json"]`).

### coverage.reportOnFailure

- **CLI:** `--coverage.reportOnFailure`
- **Config:** [coverage.reportOnFailure](https://vitest.dev/config/coverage#coverage-reportonfailure)

테스트가 실패해도 커버리지 리포트를 생성합니다(기본값: `false`).

### coverage.allowExternal

- **CLI:** `--coverage.allowExternal`
- **Config:** [coverage.allowExternal](https://vitest.dev/config/coverage#coverage-allowexternal)

프로젝트 루트 외부 파일의 커버리지를 수집합니다(기본값: `false`).

### coverage.skipFull

- **CLI:** `--coverage.skipFull`
- **Config:** [coverage.skipFull](https://vitest.dev/config/coverage#coverage-skipfull)

구문, 분기, 함수 커버리지가 100%인 파일은 표시하지 않습니다(기본값: `false`).

### coverage.thresholds.100

- **CLI:** `--coverage.thresholds.100`
- **Config:** [coverage.thresholds.100](https://vitest.dev/config/coverage#coverage-thresholds-100)

모든 커버리지 임계값을 100으로 설정하는 단축 옵션(기본값: `false`)

### coverage.thresholds.perFile

- **CLI:** `--coverage.thresholds.perFile`
- **Config:** [coverage.thresholds.perFile](https://vitest.dev/config/coverage#coverage-thresholds-perfile)

파일별로 임계값을 검사합니다. 실제 임계값은 `--coverage.thresholds.lines`, `--coverage.thresholds.functions`, `--coverage.thresholds.branches`, `--coverage.thresholds.statements`를 참고하세요(기본값: `false`).

### coverage.thresholds.autoUpdate

- **CLI:** `--coverage.thresholds.autoUpdate <boolean|function>`
- **Config:** [coverage.thresholds.autoUpdate](https://vitest.dev/config/coverage#coverage-thresholds-autoupdate)

현재 커버리지가 설정된 임계값을 초과하면 "lines", "functions", "branches", "statements" 임계값을 설정 파일에 업데이트합니다(기본값: `false`).

### coverage.thresholds.lines

- **CLI:** `--coverage.thresholds.lines <number>`

라인 임계값입니다. 자세한 내용은 [istanbuljs](https://github.com/istanbuljs/nyc#coverage-thresholds)를 참고하세요. 이 옵션은 custom provider에서는 사용할 수 없습니다.

### coverage.thresholds.functions

- **CLI:** `--coverage.thresholds.functions <number>`

함수 임계값입니다. 자세한 내용은 [istanbuljs](https://github.com/istanbuljs/nyc#coverage-thresholds)를 참고하세요. 이 옵션은 custom provider에서는 사용할 수 없습니다.

### coverage.thresholds.branches

- **CLI:** `--coverage.thresholds.branches <number>`

분기 임계값입니다. 자세한 내용은 [istanbuljs](https://github.com/istanbuljs/nyc#coverage-thresholds)를 참고하세요. 이 옵션은 custom provider에서는 사용할 수 없습니다.

### coverage.thresholds.statements

- **CLI:** `--coverage.thresholds.statements <number>`

구문 임계값입니다. 자세한 내용은 [istanbuljs](https://github.com/istanbuljs/nyc#coverage-thresholds)를 참고하세요. 이 옵션은 custom provider에서는 사용할 수 없습니다.

### coverage.ignoreClassMethods

- **CLI:** `--coverage.ignoreClassMethods <name>`
- **Config:** [coverage.ignoreClassMethods](https://vitest.dev/config/coverage#coverage-ignoreclassmethods)

커버리지에서 무시할 클래스 메서드 이름 배열입니다. 자세한 내용은 [istanbuljs](https://github.com/istanbuljs/nyc#ignoring-methods)를 참고하세요. 이 옵션은 istanbul provider에서만 사용할 수 있습니다(기본값: `[]`).

### coverage.processingConcurrency

- **CLI:** `--coverage.processingConcurrency <number>`
- **Config:** [coverage.processingConcurrency](https://vitest.dev/config/coverage#coverage-processingconcurrency)

커버리지 결과 처리 시 사용하는 동시성 한도입니다. (기본값: 20과 CPU 개수 중 작은 값)

### coverage.customProviderModule

- **CLI:** `--coverage.customProviderModule <path>`
- **Config:** [coverage.customProviderModule](https://vitest.dev/config/coverage#coverage-customprovidermodule)

커스텀 커버리지 provider 모듈의 모듈 이름 또는 경로를 지정합니다. 자세한 내용은 [Custom Coverage Provider](https://vitest.dev/guide/coverage#custom-coverage-provider)를 참고하세요. 이 옵션은 custom provider에서만 사용할 수 있습니다.

### coverage.watermarks.statements

- **CLI:** `--coverage.watermarks.statements <watermarks>`

구문에 대한 상한/하한 워터마크를 `<high>,<low>` 형식으로 지정합니다.

### coverage.watermarks.lines

- **CLI:** `--coverage.watermarks.lines <watermarks>`

라인에 대한 상한/하한 워터마크를 `<high>,<low>` 형식으로 지정합니다.

### coverage.watermarks.branches

- **CLI:** `--coverage.watermarks.branches <watermarks>`

`<high>,<low>` 형식의 브랜치용 상한 및 하한 워터마크

### coverage.watermarks.functions

- **CLI:** `--coverage.watermarks.functions <watermarks>`

`<high>,<low>` 형식의 함수용 상한 및 하한 워터마크

### mode

- **CLI:** `--mode <name>`
- **Config:** [mode](https://vitest.dev/config/mode)

Vite 모드를 재정의합니다 (기본값: `test` 또는 `benchmark`)

### isolate

- **CLI:** `--isolate`
- **Config:** [isolate](https://vitest.dev/config/isolate)

모든 테스트 파일을 격리하여 실행합니다. 격리를 비활성화하려면 `--no-isolate`를 사용하세요 (기본값: `true`)

### globals

- **CLI:** `--globals`
- **Config:** [globals](https://vitest.dev/config/globals)

API를 전역으로 주입합니다

### dom

- **CLI:** `--dom`

happy-dom으로 브라우저 API를 모킹합니다

### browser.enabled

- **CLI:** `--browser.enabled`
- **Config:** [browser.enabled](https://vitest.dev/config/browser/enabled)

브라우저에서 테스트를 실행합니다. `--browser.enabled`와 동일합니다 (기본값: `false`)

### browser.name

- **CLI:** `--browser.name <name>`

특정 브라우저에서 모든 테스트를 실행합니다. 일부 브라우저는 특정 provider에서만 사용할 수 있습니다 (`--browser.provider` 참고).

### browser.headless

- **CLI:** `--browser.headless`
- **Config:** [browser.headless](https://vitest.dev/config/browser/headless)

헤드리스 모드(즉, GUI(Graphical User Interface)를 열지 않음)로 브라우저를 실행합니다. CI에서 Vitest를 실행하는 경우 기본적으로 활성화됩니다 (기본값: `process.env.CI`)

### browser.api.port

- **CLI:** `--browser.api.port [port]`
- **Config:** [browser.api.port](https://vitest.dev/config/browser/api#api-port)

서버 포트를 지정합니다. 포트가 이미 사용 중이면 Vite가 자동으로 다음 사용 가능한 포트를 시도하므로, 실제로 서버가 리스닝하는 포트는 다를 수 있습니다. `true`이면 `63315`로 설정됩니다

### browser.api.host

- **CLI:** `--browser.api.host [host]`
- **Config:** [browser.api.host](https://vitest.dev/config/browser/api#api-host)

서버가 리스닝할 IP 주소를 지정합니다. LAN 및 공인 주소를 포함한 모든 주소에서 리스닝하려면 `0.0.0.0` 또는 `true`로 설정하세요

### browser.api.strictPort

- **CLI:** `--browser.api.strictPort`
- **Config:** [browser.api.strictPort](https://vitest.dev/config/browser/api#api-strictport)

포트가 이미 사용 중일 때 다음 포트를 자동 시도하지 않고 종료하려면 true로 설정합니다

### browser.isolate

- **CLI:** `--browser.isolate`
- **Config:** [browser.isolate](https://vitest.dev/config/browser/isolate)

모든 브라우저 테스트 파일을 격리하여 실행합니다. 격리를 비활성화하려면 `--browser.isolate=false`를 사용하세요 (기본값: `true`)

### browser.ui

- **CLI:** `--browser.ui`
- **Config:** [browser.ui](https://vitest.dev/config/browser/ui)

테스트 실행 시 Vitest UI를 표시합니다 (기본값: `!process.env.CI`)

### browser.fileParallelism

- **CLI:** `--browser.fileParallelism`

브라우저 테스트 파일을 병렬로 실행할지 여부입니다. 비활성화하려면 `--browser.fileParallelism=false`를 사용하세요 (기본값: `true`)

### browser.connectTimeout

- **CLI:** `--browser.connectTimeout <timeout>`
- **Config:** [browser.connectTimeout](https://vitest.dev/config/browser/connecttimeout)

브라우저 연결에 이 시간보다 오래 걸리면 테스트 스위트가 실패합니다 (기본값: `60_000`)

### browser.trackUnhandledErrors

- **CLI:** `--browser.trackUnhandledErrors`
- **Config:** [browser.trackUnhandledErrors](https://vitest.dev/config/browser/trackunhandlederrors)

Vitest가 처리되지 않은 예외를 포착해 보고할지 제어합니다 (기본값: `true`)

### browser.trace

- **CLI:** `--browser.trace <mode>`
- **Config:** [browser.trace](https://vitest.dev/config/browser/trace)

트레이스 뷰 모드를 활성화합니다. 지원 값: "on", "off", "on-first-retry", "on-all-retries", "retain-on-failure".

### pool

- **CLI:** `--pool <pool>`
- **Config:** [pool](https://vitest.dev/config/pool)

브라우저에서 실행하지 않는 경우 pool을 지정합니다 (기본값: `forks`)

### execArgv

- **CLI:** `--execArgv <option>`
- **Config:** [execArgv](https://vitest.dev/config/execargv)

`worker_threads` 또는 `child_process`를 생성할 때 `node` 프로세스에 추가 인수를 전달합니다.

### vmMemoryLimit

- **CLI:** `--vmMemoryLimit <limit>`
- **Config:** [vmMemoryLimit](https://vitest.dev/config/vmmemorylimit)

VM pool의 메모리 제한입니다. 메모리 누수가 보인다면 이 값을 조정해 보세요.

### fileParallelism

- **CLI:** `--fileParallelism`
- **Config:** [fileParallelism](https://vitest.dev/config/fileparallelism)

모든 테스트 파일을 병렬로 실행할지 여부입니다. 비활성화하려면 `--no-file-parallelism`을 사용하세요 (기본값: `true`)

### maxWorkers

- **CLI:** `--maxWorkers <workers>`
- **Config:** [maxWorkers](https://vitest.dev/config/maxworkers)

테스트 실행에 사용할 최대 워커 수 또는 비율입니다

### environment

- **CLI:** `--environment <name>`
- **Config:** [environment](https://vitest.dev/config/environment)

브라우저에서 실행하지 않는 경우 러너 환경을 지정합니다 (기본값: `node`)

### passWithNoTests

- **CLI:** `--passWithNoTests`
- **Config:** [passWithNoTests](https://vitest.dev/config/passwithnotests)

테스트를 찾지 못해도 통과 처리합니다

### logHeapUsage

- **CLI:** `--logHeapUsage`
- **Config:** [logHeapUsage](https://vitest.dev/config/logheapusage)

node에서 실행 시 각 테스트의 힙 크기를 표시합니다

### allowOnly

- **CLI:** `--allowOnly`
- **Config:** [allowOnly](https://vitest.dev/config/allowonly)

`only`로 표시된 테스트와 스위트를 허용합니다 (기본값: `!process.env.CI`)

### dangerouslyIgnoreUnhandledErrors

- **CLI:** `--dangerouslyIgnoreUnhandledErrors`
- **Config:** [dangerouslyIgnoreUnhandledErrors](https://vitest.dev/config/dangerouslyignoreunhandlederrors)

발생하는 모든 처리되지 않은 오류를 무시합니다

### sequence.shuffle.files

- **CLI:** `--sequence.shuffle.files`
- **Config:** [sequence.shuffle.files](https://vitest.dev/config/sequence#sequence-shuffle-files)

파일을 무작위 순서로 실행합니다. 이 옵션을 활성화해도 오래 걸리는 테스트가 더 일찍 시작되지는 않습니다. (기본값: `false`)

### sequence.shuffle.tests

- **CLI:** `--sequence.shuffle.tests`
- **Config:** [sequence.shuffle.tests](https://vitest.dev/config/sequence#sequence-shuffle-tests)

테스트를 무작위 순서로 실행합니다 (기본값: `false`)

### sequence.concurrent

- **CLI:** `--sequence.concurrent`
- **Config:** [sequence.concurrent](https://vitest.dev/config/sequence#sequence-concurrent)

테스트를 병렬로 실행합니다 (기본값: `false`)

### sequence.seed

- **CLI:** `--sequence.seed <seed>`
- **Config:** [sequence.seed](https://vitest.dev/config/sequence#sequence-seed)

무작위화 시드를 설정합니다. `--sequence.shuffle`이 falsy이면 이 옵션은 효과가 없습니다. 자세한 내용은 ["Random Seed" page](https://en.wikipedia.org/wiki/Random_seed)를 참고하세요

### sequence.hooks

- **CLI:** `--sequence.hooks <order>`
- **Config:** [sequence.hooks](https://vitest.dev/config/sequence#sequence-hooks)

훅 실행 순서를 변경합니다. 허용 값은 "stack", "list", "parallel"입니다. 자세한 내용은 [`sequence.hooks`](https://vitest.dev/config/#sequence-hooks)를 참고하세요 (기본값: `"parallel"`)

### sequence.setupFiles

- **CLI:** `--sequence.setupFiles <order>`
- **Config:** [sequence.setupFiles](https://vitest.dev/config/sequence#sequence-setupfiles)

setup 파일 실행 순서를 변경합니다. 허용 값은 "list"와 "parallel"입니다. "list"로 설정하면 정의된 순서대로 setup 파일을 실행합니다. "parallel"로 설정하면 setup 파일을 병렬 실행합니다 (기본값: `"parallel"`)

### inspect

- **CLI:** `--inspect [[host:]port]`

Node.js inspector를 활성화합니다 (기본값: `127.0.0.1:9229`)

### inspectBrk

- **CLI:** `--inspectBrk [[host:]port]`

Node.js inspector를 활성화하고 테스트 시작 전에 중단합니다

### testTimeout

- **CLI:** `--testTimeout <timeout>`
- **Config:** [testTimeout](https://vitest.dev/config/testtimeout)

테스트의 기본 타임아웃(밀리초)입니다 (기본값: `5000`). 타임아웃을 완전히 비활성화하려면 `0`을 사용하세요.

### hookTimeout

- **CLI:** `--hookTimeout <timeout>`
- **Config:** [hookTimeout](https://vitest.dev/config/hooktimeout)

훅의 기본 타임아웃(밀리초)입니다 (기본값: `10000`). 타임아웃을 완전히 비활성화하려면 `0`을 사용하세요.

### bail

- **CLI:** `--bail <number>`
- **Config:** [bail](https://vitest.dev/config/bail)

지정한 개수만큼 테스트가 실패하면 테스트 실행을 중단합니다 (기본값: `0`)

### retry

- **CLI:** `--retry <times>`
- **Config:** [retry](https://vitest.dev/config/retry)

실패한 테스트를 지정한 횟수만큼 재시도합니다 (기본값: `0`)

### diff.aAnnotation

- **CLI:** `--diff.aAnnotation <annotation>`
- **Config:** [diff.aAnnotation](https://vitest.dev/config/diff#diff-aannotation)

예상 라인용 주석입니다 (기본값: `Expected`)

### diff.aIndicator

- **CLI:** `--diff.aIndicator <indicator>`
- **Config:** [diff.aIndicator](https://vitest.dev/config/diff#diff-aindicator)

예상 라인용 표시자입니다 (기본값: `-`)

### diff.bAnnotation

- **CLI:** `--diff.bAnnotation <annotation>`
- **Config:** [diff.bAnnotation](https://vitest.dev/config/diff#diff-bannotation)

실제 수신 라인용 주석입니다 (기본값: `Received`)

### diff.bIndicator

- **CLI:** `--diff.bIndicator <indicator>`
- **Config:** [diff.bIndicator](https://vitest.dev/config/diff#diff-bindicator)

실제 수신 라인용 표시자입니다 (기본값: `+`)

### diff.commonIndicator

- **CLI:** `--diff.commonIndicator <indicator>`
- **Config:** [diff.commonIndicator](https://vitest.dev/config/diff#diff-commonindicator)

공통 라인용 표시자입니다 (기본값: ` `)

### diff.contextLines

- **CLI:** `--diff.contextLines <lines>`
- **Config:** [diff.contextLines](https://vitest.dev/config/diff#diff-contextlines)

각 변경 주변에 표시할 컨텍스트 라인 수입니다 (기본값: `5`)

### diff.emptyFirstOrLastLinePlaceholder

- **CLI:** `--diff.emptyFirstOrLastLinePlaceholder <placeholder>`
- **Config:** [diff.emptyFirstOrLastLinePlaceholder](https://vitest.dev/config/diff#diff-emptyfirstorlastlineplaceholder)

비어 있는 첫 줄 또는 마지막 줄용 플레이스홀더입니다 (기본값: `""`)

### diff.expand

- **CLI:** `--diff.expand`
- **Config:** [diff.expand](https://vitest.dev/config/diff#diff-expand)

모든 공통 라인을 펼쳐서 표시합니다 (기본값: `true`)

### diff.includeChangeCounts

- **CLI:** `--diff.includeChangeCounts`
- **Config:** [diff.includeChangeCounts](https://vitest.dev/config/diff#diff-includechangecounts)

diff 출력에 비교 개수를 포함합니다 (기본값: `false`)

### diff.omitAnnotationLines

- **CLI:** `--diff.omitAnnotationLines`
- **Config:** [diff.omitAnnotationLines](https://vitest.dev/config/diff#diff-omitannotationlines)

출력에서 주석 라인을 생략합니다 (기본값: `false`)

### diff.printBasicPrototype

- **CLI:** `--diff.printBasicPrototype`
- **Config:** [diff.printBasicPrototype](https://vitest.dev/config/diff#diff-printbasicprototype)

기본 프로토타입 Object와 Array를 출력합니다 (기본값: `true`)

### diff.maxDepth

- **CLI:** `--diff.maxDepth <maxDepth>`
- **Config:** [diff.maxDepth](https://vitest.dev/config/diff#diff-maxdepth)

중첩 객체 출력 시 재귀 깊이를 제한합니다 (기본값: `20`)

### diff.truncateThreshold

- **CLI:** `--diff.truncateThreshold <threshold>`
- **Config:** [diff.truncateThreshold](https://vitest.dev/config/diff#diff-truncatethreshold)

각 변경 전후로 표시할 라인 수입니다 (기본값: `0`)

### diff.truncateAnnotation

- **CLI:** `--diff.truncateAnnotation <annotation>`
- **Config:** [diff.truncateAnnotation](https://vitest.dev/config/diff#diff-truncateannotation)

잘린 라인용 주석입니다 (기본값: `... Diff result is truncated`)

### exclude

- **CLI:** `--exclude <glob>`
- **Config:** [exclude](https://vitest.dev/config/exclude)

테스트에서 제외할 추가 파일 glob입니다

### expandSnapshotDiff

- **CLI:** `--expandSnapshotDiff`
- **Config:** [expandSnapshotDiff](https://vitest.dev/config/expandsnapshotdiff)

스냅샷 실패 시 전체 diff를 표시합니다

### disableConsoleIntercept

- **CLI:** `--disableConsoleIntercept`

- **Config:** [disableConsoleIntercept](https://vitest.dev/config/disableconsoleintercept)

콘솔 로깅 자동 인터셉트를 비활성화합니다 (기본값: `false`)

### typecheck.enabled

- **CLI:** `--typecheck.enabled`
- **Config:** [typecheck.enabled](https://vitest.dev/config/typecheck#typecheck-enabled)

테스트와 함께 타입체크를 활성화합니다 (기본값: `false`)

### typecheck.only

- **CLI:** `--typecheck.only`
- **Config:** [typecheck.only](https://vitest.dev/config/typecheck#typecheck-only)

타입체크 테스트만 실행합니다. 이 옵션은 자동으로 typecheck를 활성화합니다 (기본값: `false`)

### typecheck.checker

- **CLI:** `--typecheck.checker <name>`
- **Config:** [typecheck.checker](https://vitest.dev/config/typecheck#typecheck-checker)

사용할 타입체커를 지정합니다. 사용 가능한 값은 "tsc", "vue-tsc", 그리고 실행 파일 경로입니다 (기본값: `"tsc"`)

### typecheck.allowJs

- **CLI:** `--typecheck.allowJs`
- **Config:** [typecheck.allowJs](https://vitest.dev/config/typecheck#typecheck-allowjs)

JavaScript 파일도 타입체크하도록 허용합니다. 기본적으로 `tsconfig.json`의 값을 따릅니다

### typecheck.ignoreSourceErrors

- **CLI:** `--typecheck.ignoreSourceErrors`
- **Config:** [typecheck.ignoreSourceErrors](https://vitest.dev/config/typecheck#typecheck-ignoresourceerrors)

소스 파일의 타입 오류를 무시합니다

### typecheck.tsconfig

- **CLI:** `--typecheck.tsconfig <path>`
- **Config:** [typecheck.tsconfig](https://vitest.dev/config/typecheck#typecheck-tsconfig)

커스텀 tsconfig 파일 경로입니다

### typecheck.spawnTimeout

- **CLI:** `--typecheck.spawnTimeout <time>`
- **Config:** [typecheck.spawnTimeout](https://vitest.dev/config/typecheck#typecheck-spawntimeout)

타입체커를 스폰하는 데 걸리는 최소 시간(밀리초)입니다

### project

- **CLI:** `--project <name>`

Vitest workspace 기능을 사용하는 경우 실행할 프로젝트 이름입니다. 여러 프로젝트에 대해 반복 지정할 수 있습니다: `--project=1 --project=2`. `--project=packages*`처럼 와일드카드로 프로젝트를 필터링할 수도 있고, `--project=!pattern`으로 프로젝트를 제외할 수도 있습니다.

### slowTestThreshold

- **CLI:** `--slowTestThreshold <threshold>`
- **Config:** [slowTestThreshold](https://vitest.dev/config/slowtestthreshold)

테스트 또는 스위트를 느린 것으로 간주하는 임계값(밀리초)입니다 (기본값: `300`)

### teardownTimeout

- **CLI:** `--teardownTimeout <timeout>`
- **Config:** [teardownTimeout](https://vitest.dev/config/teardowntimeout)

teardown 함수의 기본 타임아웃(밀리초)입니다 (기본값: `10000`)

### maxConcurrency

- **CLI:** `--maxConcurrency <number>`
- **Config:** [maxConcurrency](https://vitest.dev/config/maxconcurrency)

스위트에서 동시에 실행 가능한 테스트의 최대 개수입니다 (기본값: `5`)

### expect.requireAssertions

- **CLI:** `--expect.requireAssertions`
- **Config:** [expect.requireAssertions](https://vitest.dev/config/expect#expect-requireassertions)

모든 테스트에 최소 하나의 assertion이 있도록 강제합니다

### expect.poll.interval

- **CLI:** `--expect.poll.interval <interval>`
- **Config:** [expect.poll.interval](https://vitest.dev/config/expect#expect-poll-interval)

`expect.poll()` assertion의 폴링 간격(밀리초)입니다 (기본값: `50`)

### expect.poll.timeout

- **CLI:** `--expect.poll.timeout <timeout>`
- **Config:** [expect.poll.timeout](https://vitest.dev/config/expect#expect-poll-timeout)

`expect.poll()` assertion의 폴링 타임아웃(밀리초)입니다 (기본값: `1000`)

### printConsoleTrace

- **CLI:** `--printConsoleTrace`
- **Config:** [printConsoleTrace](https://vitest.dev/config/printconsoletrace)

항상 콘솔 스택 트레이스를 출력합니다

### includeTaskLocation

- **CLI:** `--includeTaskLocation`
- **Config:** [includeTaskLocation](https://vitest.dev/config/includetasklocation)

테스트 및 스위트의 위치를 `location` 속성에 수집합니다

### attachmentsDir

- **CLI:** `--attachmentsDir <dir>`
- **Config:** [attachmentsDir](https://vitest.dev/config/attachmentsdir)

`context.annotate`의 첨부 파일이 저장되는 디렉터리입니다 (기본값: `.vitest-attachments`)

### run

- **CLI:** `--run`

watch 모드를 비활성화합니다

### color

- **CLI:** `--no-color`

콘솔 출력에서 색상을 제거합니다

### clearScreen

- **CLI:** `--clearScreen`

watch 모드에서 테스트를 다시 실행할 때 터미널 화면을 지웁니다 (기본값: `true`)

### configLoader

- **CLI:** `--configLoader <loader>`

`bundle`을 사용하면 esbuild로 config를 번들링하고, `runner`(실험적)를 사용하면 즉시 처리합니다. 이 옵션은 vite 버전 6.1.0 이상에서만 사용할 수 있습니다. (기본값: `bundle`)

### standalone

- **CLI:** `--standalone`

테스트를 실행하지 않고 Vitest를 시작합니다. 테스트는 변경이 있을 때만 실행됩니다. CLI 파일 필터가 전달되면 이 옵션은 무시됩니다. (기본값: `false`)

### clearCache

- **CLI:** `--clearCache`

테스트를 실행하지 않고 `experimental.fsModuleCache`를 포함한 모든 Vitest 캐시를 삭제합니다. 이후 테스트 실행 성능이 저하될 수 있습니다.

### experimental.fsModuleCache

- **CLI:** `--experimental.fsModuleCache`
- **Config:** [experimental.fsModuleCache](https://vitest.dev/config/experimental#experimental-fsmodulecache)

재실행 간 파일 시스템에 모듈 캐싱을 활성화합니다.

### experimental.printImportBreakdown

- **CLI:** `--experimental.printImportBreakdown`
- **Config:** [experimental.printImportBreakdown](https://vitest.dev/config/experimental#experimental-printimportbreakdown)

요약 뒤에 import 분석 내역을 출력합니다. reporter가 요약을 지원하지 않으면 효과가 없습니다. UI의 "Module Graph" 탭에는 항상 import 분석 내역이 표시됩니다.

### changed

- **Type**: `boolean | string`
- **Default**: false

변경된 파일에 대해서만 테스트를 실행합니다. 값을 제공하지 않으면 커밋되지 않은 변경 사항(staged 및 unstaged 포함)을 기준으로 테스트를 실행합니다.

마지막 커밋에서 발생한 변경에 대해 테스트를 실행하려면 `--changed HEAD~1`을 사용할 수 있습니다. 커밋 해시(예: `--changed 09a9920`)나 브랜치 이름(예: `--changed origin/develop`)도 전달할 수 있습니다.

코드 커버리지와 함께 사용하면 보고서에는 변경 사항과 관련된 파일만 포함됩니다.

[`forceRerunTriggers`](https://vitest.dev/config/#forcereruntriggers) config 옵션과 함께 사용하면 `forceRerunTriggers` 목록에 있는 파일 중 하나라도 변경될 때 전체 테스트 스위트를 실행합니다. 기본적으로 Vitest config 파일과 `package.json`의 변경은 항상 전체 스위트를 다시 실행합니다.

### shard

- **Type**: `string`
- **Default**: disabled

실행할 테스트 스위트 샤드이며 형식은 `<index>`/`<count>`입니다. 여기서:

- `count`는 분할된 파트 수를 나타내는 양의 정수입니다
- `index`는 분할된 파트의 인덱스를 나타내는 양의 정수입니다

이 명령은 모든 테스트를 `count`개의 동일한 파트로 나누고, 그중 `index` 파트에 해당하는 테스트만 실행합니다. 예를 들어 테스트 스위트를 3개 파트로 나누려면 다음을 사용하세요:

```sh
vitest run --shard=1/3
vitest run --shard=2/3
vitest run --shard=3/3
```

:::warning
`--watch`가 활성화된 상태(기본적으로 dev에서 활성화됨)에서는 이 옵션을 사용할 수 없습니다.
:::

::: tip
`--reporter=blob`를 출력 파일 없이 사용하면, 다른 Vitest 프로세스와의 충돌을 피하기 위해 기본 경로에 현재 shard 설정이 포함됩니다.
:::

### merge-reports

- **Type:** `boolean | string`

지정된 폴더(기본값 `.vitest-reports`)에 있는 모든 blob 보고서를 병합합니다. 이 명령에서는 어떤 reporter든 사용할 수 있습니다([`blob`](https://vitest.dev/guide/reporters#blob-reporter) 제외):

```sh
vitest --merge-reports --reporter=junit
```
