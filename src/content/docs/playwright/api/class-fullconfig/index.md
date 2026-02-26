---
title: "FullConfig"
description: "추가된 버전: v1.20 fullConfig.configFile"
---

Source URL: https://playwright.dev/docs/api/class-fullconfig

# FullConfig | Playwright

[testInfo.config](https://playwright.dev/docs/api/class-testinfo#test-info-config)에서 접근할 수 있고 테스트 리포터에 전달되는, 해석된 구성입니다. Playwright 구성 파일의 형식을 확인하려면 [TestConfig](https://playwright.dev/docs/api/class-testconfig "TestConfig")를 참고하세요.

---

## 속성[​](https://playwright.dev/docs/api/class-fullconfig#properties "Direct link to Properties")

### configFile[​](https://playwright.dev/docs/api/class-fullconfig#full-config-config-file "Direct link to configFile")

추가된 버전: v1.20 fullConfig.configFile

테스트 실행에 사용된 구성 파일의 경로입니다. 구성 파일을 사용하지 않은 경우 값은 빈 문자열입니다.

**사용법**

```
    fullConfig.configFile

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### forbidOnly[​](https://playwright.dev/docs/api/class-fullconfig#full-config-forbid-only "Direct link to forbidOnly")

추가된 버전: v1.10 fullConfig.forbidOnly

[testConfig.forbidOnly](https://playwright.dev/docs/api/class-testconfig#test-config-forbid-only)를 참고하세요.

**사용법**

```
    fullConfig.forbidOnly

```

**타입**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### fullyParallel[​](https://playwright.dev/docs/api/class-fullconfig#full-config-fully-parallel "Direct link to fullyParallel")

추가된 버전: v1.20 fullConfig.fullyParallel

[testConfig.fullyParallel](https://playwright.dev/docs/api/class-testconfig#test-config-fully-parallel)를 참고하세요.

**사용법**

```
    fullConfig.fullyParallel

```

**타입**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### globalSetup[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-setup "Direct link to globalSetup")

추가된 버전: v1.10 fullConfig.globalSetup

[testConfig.globalSetup](https://playwright.dev/docs/api/class-testconfig#test-config-global-setup)를 참고하세요.

**사용법**

```
    fullConfig.globalSetup

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### globalTeardown[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-teardown "Direct link to globalTeardown")

추가된 버전: v1.10 fullConfig.globalTeardown

[testConfig.globalTeardown](https://playwright.dev/docs/api/class-testconfig#test-config-global-teardown)를 참고하세요.

**사용법**

```
    fullConfig.globalTeardown

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### globalTimeout[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-timeout "Direct link to globalTimeout")

추가된 버전: v1.10 fullConfig.globalTimeout

[testConfig.globalTimeout](https://playwright.dev/docs/api/class-testconfig#test-config-global-timeout)를 참고하세요.

**사용법**

```
    fullConfig.globalTimeout

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### grep[​](https://playwright.dev/docs/api/class-fullconfig#full-config-grep "Direct link to grep")

추가된 버전: v1.10 fullConfig.grep

[testConfig.grep](https://playwright.dev/docs/api/class-testconfig#test-config-grep)를 참고하세요.

**사용법**

```
    fullConfig.grep

```

**타입**

- [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### grepInvert[​](https://playwright.dev/docs/api/class-fullconfig#full-config-grep-invert "Direct link to grepInvert")

추가된 버전: v1.10 fullConfig.grepInvert

[testConfig.grepInvert](https://playwright.dev/docs/api/class-testconfig#test-config-grep-invert)를 참고하세요.

**사용법**

```
    fullConfig.grepInvert

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### maxFailures[​](https://playwright.dev/docs/api/class-fullconfig#full-config-max-failures "Direct link to maxFailures")

추가된 버전: v1.10 fullConfig.maxFailures

[testConfig.maxFailures](https://playwright.dev/docs/api/class-testconfig#test-config-max-failures)를 참고하세요.

**사용법**

```
    fullConfig.maxFailures

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### metadata[​](https://playwright.dev/docs/api/class-fullconfig#full-config-metadata "Direct link to metadata")

추가된 버전: v1.10 fullConfig.metadata

[testConfig.metadata](https://playwright.dev/docs/api/class-testconfig#test-config-metadata)를 참고하세요.

**사용법**

```
    fullConfig.metadata

```

**타입**

- [Metadata](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object<string, any>")

---

### preserveOutput[​](https://playwright.dev/docs/api/class-fullconfig#full-config-preserve-output "Direct link to preserveOutput")

추가된 버전: v1.10 fullConfig.preserveOutput

[testConfig.preserveOutput](https://playwright.dev/docs/api/class-testconfig#test-config-preserve-output)를 참고하세요.

**사용법**

```
    fullConfig.preserveOutput

```

**타입**

- "always" | "never" | "failures-only"

---

### projects[​](https://playwright.dev/docs/api/class-fullconfig#full-config-projects "Direct link to projects")

추가된 버전: v1.10 fullConfig.projects

해석된 프로젝트 목록입니다.

**사용법**

```
    fullConfig.projects

```

**타입**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[FullProject](https://playwright.dev/docs/api/class-fullproject "FullProject")>

---

### quiet[​](https://playwright.dev/docs/api/class-fullconfig#full-config-quiet "Direct link to quiet")

추가된 버전: v1.10 fullConfig.quiet

[testConfig.quiet](https://playwright.dev/docs/api/class-testconfig#test-config-quiet)를 참고하세요.

**사용법**

```
    fullConfig.quiet

```

**타입**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### reportSlowTests[​](https://playwright.dev/docs/api/class-fullconfig#full-config-report-slow-tests "Direct link to reportSlowTests")

추가된 버전: v1.10 fullConfig.reportSlowTests

[testConfig.reportSlowTests](https://playwright.dev/docs/api/class-testconfig#test-config-report-slow-tests)를 참고하세요.

**사용법**

```
    fullConfig.reportSlowTests

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `max` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

보고할 느린 테스트 파일의 최대 개수입니다.

    * `threshold` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

느리다고 간주되는 테스트 파일 실행 시간(밀리초)입니다.

---

### reporter[​](https://playwright.dev/docs/api/class-fullconfig#full-config-reporter "Direct link to reporter")

추가된 버전: v1.10 fullConfig.reporter

[testConfig.reporter](https://playwright.dev/docs/api/class-testconfig#test-config-reporter)를 참고하세요.

**사용법**

```
    fullConfig.reporter

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> | "list" | "dot" | "line" | "github" | "json" | "junit" | "null" | "html"
  - `0` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

리포터 이름, 모듈 또는 파일 경로

    * `1` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")

리포터 옵션이 있는 경우 해당 옵션 객체

---

### rootDir[​](https://playwright.dev/docs/api/class-fullconfig#full-config-root-dir "Direct link to rootDir")

추가된 버전: v1.20 fullConfig.rootDir

리포터에서 사용되는 모든 상대 경로의 기준 디렉터리입니다.

**사용법**

```
    fullConfig.rootDir

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### shard[​](https://playwright.dev/docs/api/class-fullconfig#full-config-shard "Direct link to shard")

추가된 버전: v1.10 fullConfig.shard

[testConfig.shard](https://playwright.dev/docs/api/class-testconfig#test-config-shard)를 참고하세요.

**사용법**

```
    fullConfig.shard

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `total` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

샤드의 총 개수입니다.

    * `current` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

실행할 샤드의 인덱스(1부터 시작)입니다.

---

### tags[​](https://playwright.dev/docs/api/class-fullconfig#full-config-tags "Direct link to tags")

추가된 버전: v1.57 fullConfig.tags

해석된 전역 태그입니다. [testConfig.tag](https://playwright.dev/docs/api/class-testconfig#test-config-tag)를 참고하세요.

**사용법**

```
    fullConfig.tags

```

**타입**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>

---

### updateSnapshots[​](https://playwright.dev/docs/api/class-fullconfig#full-config-update-snapshots "Direct link to updateSnapshots")

추가된 버전: v1.10 fullConfig.updateSnapshots

[testConfig.updateSnapshots](https://playwright.dev/docs/api/class-testconfig#test-config-update-snapshots)를 참고하세요.

**사용법**

```
    fullConfig.updateSnapshots

```

**타입**

- "all" | "changed" | "missing" | "none"

---

### updateSourceMethod[​](https://playwright.dev/docs/api/class-fullconfig#full-config-update-source-method "Direct link to updateSourceMethod")

추가된 버전: v1.50 fullConfig.updateSourceMethod

[testConfig.updateSourceMethod](https://playwright.dev/docs/api/class-testconfig#test-config-update-source-method)를 참고하세요.

**사용법**

```
    fullConfig.updateSourceMethod

```

**타입**

- "overwrite" | "3way" | "patch"

---

### version[​](https://playwright.dev/docs/api/class-fullconfig#full-config-version "Direct link to version")

추가된 버전: v1.20 fullConfig.version

Playwright 버전입니다.

**사용법**

```
    fullConfig.version

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### webServer[​](https://playwright.dev/docs/api/class-fullconfig#full-config-web-server "Direct link to webServer")

추가된 버전: v1.10 fullConfig.webServer

[testConfig.webServer](https://playwright.dev/docs/api/class-testconfig#test-config-web-server)를 참고하세요.

**사용법**

```
    fullConfig.webServer

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")

---

### workers[​](https://playwright.dev/docs/api/class-fullconfig#full-config-workers "Direct link to workers")

추가된 버전: v1.10 fullConfig.workers

[testConfig.workers](https://playwright.dev/docs/api/class-testconfig#test-config-workers)를 참고하세요.

**사용법**

```
    fullConfig.workers

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")
