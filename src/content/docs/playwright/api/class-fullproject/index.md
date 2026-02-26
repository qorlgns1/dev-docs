---
title: "FullProject"
description: "테스트 프로젝트 구성의 런타임 표현입니다. 테스트에서는 testInfo.project 및 workerInfo.project를 통해 접근할 수 있으며, 테스트 리포터에도 전달됩니다. Playwright 구성 파일에서의 프로젝트 형식을 보려면 TestProject를 대신 ..."
---

Source URL: https://playwright.dev/docs/api/class-fullproject

# FullProject | Playwright

테스트 프로젝트 구성의 런타임 표현입니다. 테스트에서는 [testInfo.project](https://playwright.dev/docs/api/class-testinfo#test-info-project) 및 [workerInfo.project](https://playwright.dev/docs/api/class-workerinfo#worker-info-project)를 통해 접근할 수 있으며, 테스트 리포터에도 전달됩니다. Playwright 구성 파일에서의 프로젝트 형식을 보려면 [TestProject](https://playwright.dev/docs/api/class-testproject "TestProject")를 대신 참조하세요.

---

## 속성[​](https://playwright.dev/docs/api/class-fullproject#properties "Direct link to Properties")

### dependencies[​](https://playwright.dev/docs/api/class-fullproject#full-project-dependencies "Direct link to dependencies")

추가된 버전: v1.31 fullProject.dependencies

[testProject.dependencies](https://playwright.dev/docs/api/class-testproject#test-project-dependencies)를 참조하세요.

**사용법**

```
    fullProject.dependencies

```

**타입**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>

---

### grep[​](https://playwright.dev/docs/api/class-fullproject#full-project-grep "Direct link to grep")

추가된 버전: v1.10 fullProject.grep

[testProject.grep](https://playwright.dev/docs/api/class-testproject#test-project-grep)를 참조하세요.

**사용법**

```
    fullProject.grep

```

**타입**

- [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### grepInvert[​](https://playwright.dev/docs/api/class-fullproject#full-project-grep-invert "Direct link to grepInvert")

추가된 버전: v1.10 fullProject.grepInvert

[testProject.grepInvert](https://playwright.dev/docs/api/class-testproject#test-project-grep-invert)를 참조하세요.

**사용법**

```
    fullProject.grepInvert

```

**타입**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### metadata[​](https://playwright.dev/docs/api/class-fullproject#full-project-metadata "Direct link to metadata")

추가된 버전: v1.10 fullProject.metadata

[testProject.metadata](https://playwright.dev/docs/api/class-testproject#test-project-metadata)를 참조하세요.

**사용법**

```
    fullProject.metadata

```

**타입**

- [Metadata](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object<string, any>")

---

### name[​](https://playwright.dev/docs/api/class-fullproject#full-project-name "Direct link to name")

추가된 버전: v1.10 fullProject.name

[testProject.name](https://playwright.dev/docs/api/class-testproject#test-project-name)를 참조하세요.

**사용법**

```
    fullProject.name

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### outputDir[​](https://playwright.dev/docs/api/class-fullproject#full-project-output-dir "Direct link to outputDir")

추가된 버전: v1.10 fullProject.outputDir

[testProject.outputDir](https://playwright.dev/docs/api/class-testproject#test-project-output-dir)를 참조하세요.

**사용법**

```
    fullProject.outputDir

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### repeatEach[​](https://playwright.dev/docs/api/class-fullproject#full-project-repeat-each "Direct link to repeatEach")

추가된 버전: v1.10 fullProject.repeatEach

[testProject.repeatEach](https://playwright.dev/docs/api/class-testproject#test-project-repeat-each)를 참조하세요.

**사용법**

```
    fullProject.repeatEach

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### retries[​](https://playwright.dev/docs/api/class-fullproject#full-project-retries "Direct link to retries")

추가된 버전: v1.10 fullProject.retries

[testProject.retries](https://playwright.dev/docs/api/class-testproject#test-project-retries)를 참조하세요.

**사용법**

```
    fullProject.retries

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### snapshotDir[​](https://playwright.dev/docs/api/class-fullproject#full-project-snapshot-dir "Direct link to snapshotDir")

추가된 버전: v1.10 fullProject.snapshotDir

[testProject.snapshotDir](https://playwright.dev/docs/api/class-testproject#test-project-snapshot-dir)를 참조하세요.

**사용법**

```
    fullProject.snapshotDir

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### teardown[​](https://playwright.dev/docs/api/class-fullproject#full-project-teardown "Direct link to teardown")

추가된 버전: v1.34 fullProject.teardown

[testProject.teardown](https://playwright.dev/docs/api/class-testproject#test-project-teardown)를 참조하세요.

**사용법**

```
    fullProject.teardown

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### testDir[​](https://playwright.dev/docs/api/class-fullproject#full-project-test-dir "Direct link to testDir")

추가된 버전: v1.10 fullProject.testDir

[testProject.testDir](https://playwright.dev/docs/api/class-testproject#test-project-test-dir)를 참조하세요.

**사용법**

```
    fullProject.testDir

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### testIgnore[​](https://playwright.dev/docs/api/class-fullproject#full-project-test-ignore "Direct link to testIgnore")

추가된 버전: v1.10 fullProject.testIgnore

[testProject.testIgnore](https://playwright.dev/docs/api/class-testproject#test-project-test-ignore)를 참조하세요.

**사용법**

```
    fullProject.testIgnore

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### testMatch[​](https://playwright.dev/docs/api/class-fullproject#full-project-test-match "Direct link to testMatch")

추가된 버전: v1.10 fullProject.testMatch

[testProject.testMatch](https://playwright.dev/docs/api/class-testproject#test-project-test-match)를 참조하세요.

**사용법**

```
    fullProject.testMatch

```

**타입**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### timeout[​](https://playwright.dev/docs/api/class-fullproject#full-project-timeout "Direct link to timeout")

추가된 버전: v1.10 fullProject.timeout

[testProject.timeout](https://playwright.dev/docs/api/class-testproject#test-project-timeout)를 참조하세요.

**사용법**

```
    fullProject.timeout

```

**타입**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### use[​](https://playwright.dev/docs/api/class-fullproject#full-project-use "Direct link to use")

추가된 버전: v1.10 fullProject.use

[testProject.use](https://playwright.dev/docs/api/class-testproject#test-project-use)를 참조하세요.

**사용법**

```
    fullProject.use

```

**타입**

- [Fixtures](https://playwright.dev/docs/api/class-fixtures "Fixtures")
