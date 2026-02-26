---
title: "Reporter"
description: "Test runner notifies the reporter about various events during test execution. All methods of the reporter are optional."
---

Source URL: https://playwright.dev/docs/api/class-reporter

# Reporter | Playwright

Test runner notifies the reporter about various events during test execution. All methods of the reporter are optional.

You can create a custom reporter by implementing a class with some of the reporter methods. Make sure to export this class as default.

- TypeScript
- JavaScript

my-awesome-reporter.ts

```
    import type {
      Reporter, FullConfig, Suite, TestCase, TestResult, FullResult
    } from '@playwright/test/reporter';

    class MyReporter implements Reporter {
      constructor(options: { customOption?: string } = {}) {
        console.log(`my-awesome-reporter setup with customOption set to ${options.customOption}`);
      }

      onBegin(config: FullConfig, suite: Suite) {
        console.log(`Starting the run with ${suite.allTests().length} tests`);
      }

      onTestBegin(test: TestCase) {
        console.log(`Starting test ${test.title}`);
      }

      onTestEnd(test: TestCase, result: TestResult) {
        console.log(`Finished test ${test.title}: ${result.status}`);
      }

      onEnd(result: FullResult) {
        console.log(`Finished the run: ${result.status}`);
      }
    }
    export default MyReporter;

```

my-awesome-reporter.js

```
    // @ts-check

    /** @implements {import('@playwright/test/reporter').Reporter} */
    class MyReporter {
      constructor(options) {
        console.log(`my-awesome-reporter setup with customOption set to ${options.customOption}`);
      }

      onBegin(config, suite) {
        console.log(`Starting the run with ${suite.allTests().length} tests`);
      }

      onTestBegin(test) {
        console.log(`Starting test ${test.title}`);
      }

      onTestEnd(test, result) {
        console.log(`Finished test ${test.title}: ${result.status}`);
      }

      onEnd(result) {
        console.log(`Finished the run: ${result.status}`);
      }
    }

    module.exports = MyReporter;

```

Now use this reporter with [testConfig.reporter](https://playwright.dev/docs/api/class-testconfig#test-config-reporter). Learn more about [using reporters](https://playwright.dev/docs/test-reporters).

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      reporter: [['./my-awesome-reporter.ts', { customOption: 'some value' }]],
    });

```

Here is a typical order of reporter calls:

- [reporter.onBegin()](https://playwright.dev/docs/api/class-reporter#reporter-on-begin) is called once with a root suite that contains all other suites and tests. Learn more about [suites hierarchy](https://playwright.dev/docs/api/class-suite "Suite").
- [reporter.onTestBegin()](https://playwright.dev/docs/api/class-reporter#reporter-on-test-begin) is called for each test run. It is given a [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase") that is executed, and a [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult") that is almost empty. Test result will be populated while the test runs (for example, with steps and stdio) and will get final `status` once the test finishes.
- [reporter.onStepBegin()](https://playwright.dev/docs/api/class-reporter#reporter-on-step-begin) and [reporter.onStepEnd()](https://playwright.dev/docs/api/class-reporter#reporter-on-step-end) are called for each executed step inside the test. When steps are executed, test run has not finished yet.
- [reporter.onTestEnd()](https://playwright.dev/docs/api/class-reporter#reporter-on-test-end) is called when test run has finished. By this time, [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult") is complete and you can use [testResult.status](https://playwright.dev/docs/api/class-testresult#test-result-status), [testResult.error](https://playwright.dev/docs/api/class-testresult#test-result-error) and more.
- [reporter.onEnd()](https://playwright.dev/docs/api/class-reporter#reporter-on-end) is called once after all tests that should run had finished.
- [reporter.onExit()](https://playwright.dev/docs/api/class-reporter#reporter-on-exit) is called immediately before the test runner exits.

Additionally, [reporter.onStdOut()](https://playwright.dev/docs/api/class-reporter#reporter-on-std-out) and [reporter.onStdErr()](https://playwright.dev/docs/api/class-reporter#reporter-on-std-err) are called when standard output is produced in the worker process, possibly during a test execution, and [reporter.onError()](https://playwright.dev/docs/api/class-reporter#reporter-on-error) is called when something went wrong outside of the test execution.

If your custom reporter does not print anything to the terminal, implement [reporter.printsToStdio()](https://playwright.dev/docs/api/class-reporter#reporter-prints-to-stdio) and return `false`. This way, Playwright will use one of the standard terminal reporters in addition to your custom reporter to enhance user experience.

**Reporter errors**

Playwright will swallow any errors thrown in your custom reporter methods. If you need to detect or fail on reporter errors, you must wrap and handle them yourself.

**Merged report API notes**

When merging multiple [`blob`](https://playwright.dev/docs/test-reporters#blob-reporter) reports via [`merge-reports`](https://playwright.dev/docs/test-sharding#merge-reports-cli) CLI command, the same [Reporter](https://playwright.dev/docs/api/class-reporter "Reporter") API is called to produce final reports and all existing reporters should work without any changes. There some subtle differences though which might affect some custom reporters.

- Projects from different shards are always kept as separate [TestProject](https://playwright.dev/docs/api/class-testproject "TestProject") objects. E.g. if project 'Desktop Chrome' was sharded across 5 machines then there will be 5 instances of projects with the same name in the config passed to [reporter.onBegin()](https://playwright.dev/docs/api/class-reporter#reporter-on-begin).

---

## Methods[​](https://playwright.dev/docs/api/class-reporter#methods "Direct link to Methods")

### onBegin[​](https://playwright.dev/docs/api/class-reporter#reporter-on-begin "Direct link to onBegin")

Added in: v1.10 reporter.onBegin

Called once before running tests. All tests have been already discovered and put into a hierarchy of [Suite](https://playwright.dev/docs/api/class-suite "Suite")s.

**Usage**

```
    reporter.onBegin(config, suite);

```

**Arguments**

- `config` [FullConfig](https://playwright.dev/docs/api/class-fullconfig "FullConfig")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-begin-option-config)

Resolved configuration.

- `suite` [Suite](https://playwright.dev/docs/api/class-suite "Suite")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-begin-option-suite)

The root suite that contains all projects, files and test cases.

---

### onEnd[​](https://playwright.dev/docs/api/class-reporter#reporter-on-end "Direct link to onEnd")

Added in: v1.10 reporter.onEnd

Called after all tests have been run, or testing has been interrupted. Note that this method may return a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise") and Playwright Test will await it. Reporter is allowed to override the status and hence affect the exit code of the test runner.

**Usage**

```
    await reporter.onEnd(result);

```

**Arguments**

- `result` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-end-option-result)
  - `status` "passed" | "failed" | "timedout" | "interrupted"

Test run status.

    * `startTime` [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date "Date")

Test run start wall time.

    * `duration` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

Test run duration in milliseconds.

Result of the full test run, `status` can be one of:

    * `'passed'` \- Everything went as expected.
    * `'failed'` \- Any test has failed.
    * `'timedout'` \- The [testConfig.globalTimeout](https://playwright.dev/docs/api/class-testconfig#test-config-global-timeout) has been reached.
    * `'interrupted'` \- Interrupted by the user.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-reporter#reporter-on-end-return)
  - `status` "passed" | "failed" | "timedout" | "interrupted" _(optional)_

---

### onError[​](https://playwright.dev/docs/api/class-reporter#reporter-on-error "Direct link to onError")

Added in: v1.10 reporter.onError

Called on some global error, for example unhandled exception in the worker process.

**Usage**

```
    reporter.onError(error);

```

**Arguments**

- `error` [TestError](https://playwright.dev/docs/api/class-testerror "TestError")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-error-option-error)

The error.

---

### onExit[​](https://playwright.dev/docs/api/class-reporter#reporter-on-exit "Direct link to onExit")

Added in: v1.33 reporter.onExit

Called immediately before test runner exists. At this point all the reporters have received the [reporter.onEnd()](https://playwright.dev/docs/api/class-reporter#reporter-on-end) signal, so all the reports should be build. You can run the code that uploads the reports in this hook.

**Usage**

```
    await reporter.onExit();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-reporter#reporter-on-exit-return)

---

### onStdErr[​](https://playwright.dev/docs/api/class-reporter#reporter-on-std-err "Direct link to onStdErr")

Added in: v1.10 reporter.onStdErr

Called when something has been written to the standard error in the worker process.

**Usage**

```
    reporter.onStdErr(chunk, test, result);

```

**Arguments**

- `chunk` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-err-option-chunk)

Output chunk.

- `test` [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void") | [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-err-option-test)

Test that was running. Note that output may happen when no test is running, in which case this will be [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void").

- `result` [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void") | [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-err-option-result)

Result of the test run, this object gets populated while the test runs.

---

### onStdOut[​](https://playwright.dev/docs/api/class-reporter#reporter-on-std-out "Direct link to onStdOut")

Added in: v1.10 reporter.onStdOut

Called when something has been written to the standard output in the worker process.

**Usage**

```
    reporter.onStdOut(chunk, test, result);

```

**Arguments**

- `chunk` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-out-option-chunk)

Output chunk.

- `test` [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void") | [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-out-option-test)

Test that was running. Note that output may happen when no test is running, in which case this will be [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void").

- `result` [void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void") | [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-std-out-option-result)

Result of the test run, this object gets populated while the test runs.

---

### onStepBegin[​](https://playwright.dev/docs/api/class-reporter#reporter-on-step-begin "Direct link to onStepBegin")

Added in: v1.10 reporter.onStepBegin

Called when a test step started in the worker process.

**Usage**

```
    reporter.onStepBegin(test, result, step);

```

**Arguments**

- `test` [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-begin-option-test)

Test that the step belongs to.

- `result` [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-begin-option-result)

Result of the test run, this object gets populated while the test runs.

- `step` [TestStep](https://playwright.dev/docs/api/class-teststep "TestStep")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-begin-option-step)

Test step instance that has started.

---

### onStepEnd[​](https://playwright.dev/docs/api/class-reporter#reporter-on-step-end "Direct link to onStepEnd")

Added in: v1.10 reporter.onStepEnd

Called when a test step finished in the worker process.

**Usage**

```
    reporter.onStepEnd(test, result, step);

```

**Arguments**

- `test` [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-end-option-test)

Test that the step belongs to.

- `result` [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-end-option-result)

Result of the test run.

- `step` [TestStep](https://playwright.dev/docs/api/class-teststep "TestStep")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-step-end-option-step)

Test step instance that has finished.

---

### onTestBegin[​](https://playwright.dev/docs/api/class-reporter#reporter-on-test-begin "Direct link to onTestBegin")

Added in: v1.10 reporter.onTestBegin

Called after a test has been started in the worker process.

**Usage**

```
    reporter.onTestBegin(test, result);

```

**Arguments**

- `test` [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-test-begin-option-test)

Test that has been started.

- `result` [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-test-begin-option-result)

Result of the test run, this object gets populated while the test runs.

---

### onTestEnd[​](https://playwright.dev/docs/api/class-reporter#reporter-on-test-end "Direct link to onTestEnd")

Added in: v1.10 reporter.onTestEnd

Called after a test has been finished in the worker process.

**Usage**

```
    reporter.onTestEnd(test, result);

```

**Arguments**

- `test` [TestCase](https://playwright.dev/docs/api/class-testcase "TestCase")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-test-end-option-test)

Test that has been finished.

- `result` [TestResult](https://playwright.dev/docs/api/class-testresult "TestResult")[#](https://playwright.dev/docs/api/class-reporter#reporter-on-test-end-option-result)

Result of the test run.

---

### printsToStdio[​](https://playwright.dev/docs/api/class-reporter#reporter-prints-to-stdio "Direct link to printsToStdio")

Added in: v1.10 reporter.printsToStdio

Whether this reporter uses stdio for reporting. When it does not, Playwright Test could add some output to enhance user experience. If your reporter does not print to the terminal, it is strongly recommended to return `false`.

**Usage**

```
    reporter.printsToStdio();

```

**Returns**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-reporter#reporter-prints-to-stdio-return)
