---
title: "Suite"
description: "is a group of tests. All tests in Playwright Test form the following hierarchy:"
---

Source URL: https://playwright.dev/docs/api/class-suite

# Suite | Playwright

`Suite` is a group of tests. All tests in Playwright Test form the following hierarchy:

- Root suite has a child suite for each [FullProject](https://playwright.dev/docs/api/class-fullproject "FullProject").
  - Project suite #1. Has a child suite for each test file in the project.
    - File suite #1
      - [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") #1
      - [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") #2
      - Suite corresponding to a [test.describe()](https://playwright.dev/docs/api/class-test#test-describe) group
        - [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") #1 in a group
        - [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") #2 in a group
      - < more test cases ... >
    - File suite #2
    - < more file suites ... >
  - Project suite #2
  - < more project suites ... >

Reporter is given a root suite in the [reporter.onBegin()](https://playwright.dev/docs/api/class-reporter#reporter-on-begin) method.

---

## Methods[​](https://playwright.dev/docs/api/class-suite#methods "Direct link to Methods")

### allTests[​](https://playwright.dev/docs/api/class-suite#suite-all-tests "Direct link to allTests")

Added in: v1.10 suite.allTests

Returns the list of all test cases in this suite and its descendants, as opposite to [suite.tests](https://playwright.dev/docs/api/class-suite#suite-tests).

**Usage**

```
    suite.allTests();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")>[#](https://playwright.dev/docs/api/class-suite#suite-all-tests-return)

---

### entries[​](https://playwright.dev/docs/api/class-suite#suite-entries "Direct link to entries")

Added in: v1.44 suite.entries

Test cases and suites defined directly in this suite. The elements are returned in their declaration order. You can differentiate between various entry types by using [testCase.type](https://playwright.dev/docs/api/class-testcase#test-case-type) and [suite.type](https://playwright.dev/docs/api/class-suite#suite-type).

**Usage**

```
    suite.entries();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") | [Suite](https://playwright.dev/docs/api/class-suite "Suite")>[#](https://playwright.dev/docs/api/class-suite#suite-entries-return)

---

### project[​](https://playwright.dev/docs/api/class-suite#suite-project "Direct link to project")

Added in: v1.10 suite.project

Configuration of the project this suite belongs to, or [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void") for the root suite.

**Usage**

```
    suite.project();

```

**Returns**

- [FullProject](https://playwright.dev/docs/api/class-fullproject "FullProject") | [undefined][#](https://playwright.dev/docs/api/class-suite#suite-project-return)

---

### titlePath[​](https://playwright.dev/docs/api/class-suite#suite-title-path "Direct link to titlePath")

Added in: v1.10 suite.titlePath

Returns a list of titles from the root down to this suite.

**Usage**

```
    suite.titlePath();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-suite#suite-title-path-return)

---

## Properties[​](https://playwright.dev/docs/api/class-suite#properties "Direct link to Properties")

### location[​](https://playwright.dev/docs/api/class-suite#suite-location "Direct link to location")

Added in: v1.10 suite.location

Location in the source where the suite is defined. Missing for root and project suites.

**Usage**

```
    suite.location

```

**Type**

- [Location](https://playwright.dev/docs/api/class-location "Location")

---

### parent[​](https://playwright.dev/docs/api/class-suite#suite-parent "Direct link to parent")

Added in: v1.10 suite.parent

Parent suite, missing for the root suite.

**Usage**

```
    suite.parent

```

**Type**

- [Suite](https://playwright.dev/docs/api/class-suite "Suite")

---

### suites[​](https://playwright.dev/docs/api/class-suite#suite-suites "Direct link to suites")

Added in: v1.10 suite.suites

Child suites. See [Suite](https://playwright.dev/docs/api/class-suite "Suite") for the hierarchy of suites.

**Usage**

```
    suite.suites

```

**Type**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Suite](https://playwright.dev/docs/api/class-suite "Suite")>

---

### tests[​](https://playwright.dev/docs/api/class-suite#suite-tests "Direct link to tests")

Added in: v1.10 suite.tests

Test cases in the suite. Note that only test cases defined directly in this suite are in the list. Any test cases defined in nested [test.describe()](https://playwright.dev/docs/api/class-test#test-describe) groups are listed in the child [suite.suites](https://playwright.dev/docs/api/class-suite#suite-suites).

**Usage**

```
    suite.tests

```

**Type**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")>

---

### title[​](https://playwright.dev/docs/api/class-suite#suite-title "Direct link to title")

Added in: v1.10 suite.title

Suite title.

- Empty for root suite.
- Project name for project suite.
- File path for file suite.
- Title passed to [test.describe()](https://playwright.dev/docs/api/class-test#test-describe) for a group suite.

**Usage**

```
    suite.title

```

**Type**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### type[​](https://playwright.dev/docs/api/class-suite#suite-type "Direct link to type")

Added in: v1.44 suite.type

Returns the type of the suite. The Suites form the following hierarchy: `root` -> `project` -> `file` -> `describe` -> ...`describe` -> `test`.

**Usage**

```
    suite.type

```

**Type**

- "root" | "project" | "file" | "describe"
