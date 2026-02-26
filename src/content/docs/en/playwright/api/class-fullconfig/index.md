---
title: "FullConfig"
description: "Resolved configuration which is accessible via testInfo.config and is passed to the test reporters. To see the format of Playwright configuration file..."
---

Source URL: https://playwright.dev/docs/api/class-fullconfig

# FullConfig | Playwright

Resolved configuration which is accessible via [testInfo.config](https://playwright.dev/docs/api/class-testinfo#test-info-config) and is passed to the test reporters. To see the format of Playwright configuration file, please see [TestConfig](https://playwright.dev/docs/api/class-testconfig "TestConfig") instead.

---

## Properties[​](https://playwright.dev/docs/api/class-fullconfig#properties "Direct link to Properties")

### configFile[​](https://playwright.dev/docs/api/class-fullconfig#full-config-config-file "Direct link to configFile")

Added in: v1.20 fullConfig.configFile

Path to the configuration file used to run the tests. The value is an empty string if no config file was used.

**Usage**

```
    fullConfig.configFile

```

**Type**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### forbidOnly[​](https://playwright.dev/docs/api/class-fullconfig#full-config-forbid-only "Direct link to forbidOnly")

Added in: v1.10 fullConfig.forbidOnly

See [testConfig.forbidOnly](https://playwright.dev/docs/api/class-testconfig#test-config-forbid-only).

**Usage**

```
    fullConfig.forbidOnly

```

**Type**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### fullyParallel[​](https://playwright.dev/docs/api/class-fullconfig#full-config-fully-parallel "Direct link to fullyParallel")

Added in: v1.20 fullConfig.fullyParallel

See [testConfig.fullyParallel](https://playwright.dev/docs/api/class-testconfig#test-config-fully-parallel).

**Usage**

```
    fullConfig.fullyParallel

```

**Type**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### globalSetup[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-setup "Direct link to globalSetup")

Added in: v1.10 fullConfig.globalSetup

See [testConfig.globalSetup](https://playwright.dev/docs/api/class-testconfig#test-config-global-setup).

**Usage**

```
    fullConfig.globalSetup

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### globalTeardown[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-teardown "Direct link to globalTeardown")

Added in: v1.10 fullConfig.globalTeardown

See [testConfig.globalTeardown](https://playwright.dev/docs/api/class-testconfig#test-config-global-teardown).

**Usage**

```
    fullConfig.globalTeardown

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### globalTimeout[​](https://playwright.dev/docs/api/class-fullconfig#full-config-global-timeout "Direct link to globalTimeout")

Added in: v1.10 fullConfig.globalTimeout

See [testConfig.globalTimeout](https://playwright.dev/docs/api/class-testconfig#test-config-global-timeout).

**Usage**

```
    fullConfig.globalTimeout

```

**Type**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### grep[​](https://playwright.dev/docs/api/class-fullconfig#full-config-grep "Direct link to grep")

Added in: v1.10 fullConfig.grep

See [testConfig.grep](https://playwright.dev/docs/api/class-testconfig#test-config-grep).

**Usage**

```
    fullConfig.grep

```

**Type**

- [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### grepInvert[​](https://playwright.dev/docs/api/class-fullconfig#full-config-grep-invert "Direct link to grepInvert")

Added in: v1.10 fullConfig.grepInvert

See [testConfig.grepInvert](https://playwright.dev/docs/api/class-testconfig#test-config-grep-invert).

**Usage**

```
    fullConfig.grepInvert

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")>

---

### maxFailures[​](https://playwright.dev/docs/api/class-fullconfig#full-config-max-failures "Direct link to maxFailures")

Added in: v1.10 fullConfig.maxFailures

See [testConfig.maxFailures](https://playwright.dev/docs/api/class-testconfig#test-config-max-failures).

**Usage**

```
    fullConfig.maxFailures

```

**Type**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### metadata[​](https://playwright.dev/docs/api/class-fullconfig#full-config-metadata "Direct link to metadata")

Added in: v1.10 fullConfig.metadata

See [testConfig.metadata](https://playwright.dev/docs/api/class-testconfig#test-config-metadata).

**Usage**

```
    fullConfig.metadata

```

**Type**

- [Metadata](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object<string, any>")

---

### preserveOutput[​](https://playwright.dev/docs/api/class-fullconfig#full-config-preserve-output "Direct link to preserveOutput")

Added in: v1.10 fullConfig.preserveOutput

See [testConfig.preserveOutput](https://playwright.dev/docs/api/class-testconfig#test-config-preserve-output).

**Usage**

```
    fullConfig.preserveOutput

```

**Type**

- "always" | "never" | "failures-only"

---

### projects[​](https://playwright.dev/docs/api/class-fullconfig#full-config-projects "Direct link to projects")

Added in: v1.10 fullConfig.projects

List of resolved projects.

**Usage**

```
    fullConfig.projects

```

**Type**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[FullProject](https://playwright.dev/docs/api/class-fullproject "FullProject")>

---

### quiet[​](https://playwright.dev/docs/api/class-fullconfig#full-config-quiet "Direct link to quiet")

Added in: v1.10 fullConfig.quiet

See [testConfig.quiet](https://playwright.dev/docs/api/class-testconfig#test-config-quiet).

**Usage**

```
    fullConfig.quiet

```

**Type**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

---

### reportSlowTests[​](https://playwright.dev/docs/api/class-fullconfig#full-config-report-slow-tests "Direct link to reportSlowTests")

Added in: v1.10 fullConfig.reportSlowTests

See [testConfig.reportSlowTests](https://playwright.dev/docs/api/class-testconfig#test-config-report-slow-tests).

**Usage**

```
    fullConfig.reportSlowTests

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `max` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

The maximum number of slow test files to report.

    * `threshold` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

Test file duration in milliseconds that is considered slow.

---

### reporter[​](https://playwright.dev/docs/api/class-fullconfig#full-config-reporter "Direct link to reporter")

Added in: v1.10 fullConfig.reporter

See [testConfig.reporter](https://playwright.dev/docs/api/class-testconfig#test-config-reporter).

**Usage**

```
    fullConfig.reporter

```

**Type**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> | "list" | "dot" | "line" | "github" | "json" | "junit" | "null" | "html"
  - `0` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Reporter name or module or file path

    * `1` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")

An object with reporter options if any

---

### rootDir[​](https://playwright.dev/docs/api/class-fullconfig#full-config-root-dir "Direct link to rootDir")

Added in: v1.20 fullConfig.rootDir

Base directory for all relative paths used in the reporters.

**Usage**

```
    fullConfig.rootDir

```

**Type**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### shard[​](https://playwright.dev/docs/api/class-fullconfig#full-config-shard "Direct link to shard")

Added in: v1.10 fullConfig.shard

See [testConfig.shard](https://playwright.dev/docs/api/class-testconfig#test-config-shard).

**Usage**

```
    fullConfig.shard

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `total` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

The total number of shards.

    * `current` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

The index of the shard to execute, one-based.

---

### tags[​](https://playwright.dev/docs/api/class-fullconfig#full-config-tags "Direct link to tags")

Added in: v1.57 fullConfig.tags

Resolved global tags. See [testConfig.tag](https://playwright.dev/docs/api/class-testconfig#test-config-tag).

**Usage**

```
    fullConfig.tags

```

**Type**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>

---

### updateSnapshots[​](https://playwright.dev/docs/api/class-fullconfig#full-config-update-snapshots "Direct link to updateSnapshots")

Added in: v1.10 fullConfig.updateSnapshots

See [testConfig.updateSnapshots](https://playwright.dev/docs/api/class-testconfig#test-config-update-snapshots).

**Usage**

```
    fullConfig.updateSnapshots

```

**Type**

- "all" | "changed" | "missing" | "none"

---

### updateSourceMethod[​](https://playwright.dev/docs/api/class-fullconfig#full-config-update-source-method "Direct link to updateSourceMethod")

Added in: v1.50 fullConfig.updateSourceMethod

See [testConfig.updateSourceMethod](https://playwright.dev/docs/api/class-testconfig#test-config-update-source-method).

**Usage**

```
    fullConfig.updateSourceMethod

```

**Type**

- "overwrite" | "3way" | "patch"

---

### version[​](https://playwright.dev/docs/api/class-fullconfig#full-config-version "Direct link to version")

Added in: v1.20 fullConfig.version

Playwright version.

**Usage**

```
    fullConfig.version

```

**Type**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### webServer[​](https://playwright.dev/docs/api/class-fullconfig#full-config-web-server "Direct link to webServer")

Added in: v1.10 fullConfig.webServer

See [testConfig.webServer](https://playwright.dev/docs/api/class-testconfig#test-config-web-server).

**Usage**

```
    fullConfig.webServer

```

**Type**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")

---

### workers[​](https://playwright.dev/docs/api/class-fullconfig#full-config-workers "Direct link to workers")

Added in: v1.10 fullConfig.workers

See [testConfig.workers](https://playwright.dev/docs/api/class-testconfig#test-config-workers).

**Usage**

```
    fullConfig.workers

```

**Type**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")
