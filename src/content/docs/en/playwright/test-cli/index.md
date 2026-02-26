---
title: "Command line"
description: "Playwright provides a powerful command line interface for running tests, generating code, debugging, and more. The most up to date list of commands an..."
---

Source URL: https://playwright.dev/docs/test-cli

# Command line | Playwright

Playwright provides a powerful command line interface for running tests, generating code, debugging, and more. The most up to date list of commands and arguments available on the CLI can always be retrieved via `npx playwright --help`.

## Essential Commands[​](https://playwright.dev/docs/test-cli#essential-commands "Direct link to Essential Commands")

### Run Tests[​](https://playwright.dev/docs/test-cli#run-tests "Direct link to Run Tests")

Run your Playwright tests. [Read more about running tests](https://playwright.dev/docs/running-tests).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax "Direct link to Syntax")

```
    npx playwright test [options] [test-filter...]

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples "Direct link to Examples")

```
    # Run all tests
    npx playwright test

    # Run a single test file
    npx playwright test tests/todo-page.spec.ts

    # Run a set of test files
    npx playwright test tests/todo-page/ tests/landing-page/

    # Run tests at a specific line
    npx playwright test my-spec.ts:42

    # Run tests by title
    npx playwright test -g "add a todo item"

    # Run tests in headed browsers
    npx playwright test --headed

    # Run tests for a specific project
    npx playwright test --project=chromium

    # Get help
    npx playwright test --help

```

**Disable[parallelization](https://playwright.dev/docs/test-parallel)**

```
    npx playwright test --workers=1

```

**Run in debug mode with[Playwright Inspector](https://playwright.dev/docs/debug)**

```
    npx playwright test --debug

```

**Run tests in interactive[UI mode](https://playwright.dev/docs/test-ui-mode)**

```
    npx playwright test --ui

```

#### Common Options[​](https://playwright.dev/docs/test-cli#common-options "Direct link to Common Options")

| Option | Description | `--debug` | Run tests with Playwright Inspector. Shortcut for `PWDEBUG=1` environment variable and `--timeout=0 --max-failures=1 --headed --workers=1` options. | `--headed` | Run tests in headed browsers (default: headless). | `-g <grep>` or `--grep <grep>` | Only run tests matching this regular expression (default: ".\*"). | `--project <project-name...>` | Only run tests from the specified list of projects, supports '\*' wildcard (default: run all projects). | `--ui` | Run tests in interactive UI mode. | `-j <workers>` or `--workers <workers>` | Number of concurrent workers or percentage of logical CPU cores, use 1 to run in a single worker (default: 50%). |
| ------ | ----------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | ------ | --------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |

#### All Options[​](https://playwright.dev/docs/test-cli#all-options "Direct link to All Options")

| Option | Description | Non-option arguments | Each argument is treated as a regular expression matched against the full test file path. Only tests from files matching the pattern will be executed. Special symbols like `$` or `*` should be escaped with `\`. In many shells/terminals you may need to quote the arguments. | `-c <file>` or `--config <file>` | Configuration file, or a test directory with optional "playwright.config.{m,c}?{js,ts}". Defaults to `playwright.config.ts` or `playwright.config.js` in the current directory. | `--debug` | Run tests with Playwright Inspector. Shortcut for `PWDEBUG=1` environment variable and `--timeout=0 --max-failures=1 --headed --workers=1` options. | `--fail-on-flaky-tests` | Fail if any test is flagged as flaky (default: false). | `--forbid-only` | Fail if `test.only` is called (default: false). Useful on CI. | `--fully-parallel` | Run all tests in parallel (default: false). | `--global-timeout <timeout>` | Maximum time this test suite can run in milliseconds (default: unlimited). | `-g <grep>` or `--grep <grep>` | Only run tests matching this regular expression (default: ".\*"). | `--grep-invert <grep>` | Only run tests that do not match this regular expression. | `--headed` | Run tests in headed browsers (default: headless). | `--ignore-snapshots` | Ignore screenshot and snapshot expectations. | `-j <workers>` or `--workers <workers>` | Number of concurrent workers or percentage of logical CPU cores, use 1 to run in a single worker (default: 50%). | `--last-failed` | Only re-run the failures. | `--list` | Collect all the tests and report them, but do not run. | `--max-failures <N>` or `-x` | Stop after the first `N` failures. Passing `-x` stops after the first failure. | `--no-deps` | Do not run project dependencies. | `--output <dir>` | Folder for output artifacts (default: "test-results"). | `--only-changed [ref]` | Only run test files that have been changed between 'HEAD' and 'ref'. Defaults to running all uncommitted changes. Only supports Git. | `--pass-with-no-tests` | Makes test run succeed even if no tests were found. | `--project <project-name...>` | Only run tests from the specified list of projects, supports '\*' wildcard (default: run all projects). | `--quiet` | Suppress stdio. | `--repeat-each <N>` | Run each test `N` times (default: 1). | `--reporter <reporter>` | Reporter to use, comma-separated, can be "dot", "line", "list", or others (default: "list"). You can also pass a path to a custom reporter file. | `--retries <retries>` | Maximum retry count for flaky tests, zero for no retries (default: no retries). | `--shard <shard>` | Shard tests and execute only the selected shard, specified in the form "current/all", 1-based, e.g., "3/5". | `--test-list <file>` | Path to a file containing a list of tests to run. See [test list](https://playwright.dev/docs/test-cli#test-list) for details. | `--test-list-invert <file>` | Path to a file containing a list of tests to skip. See [test list](https://playwright.dev/docs/test-cli#test-list) for details. | `--timeout <timeout>` | Specify test timeout threshold in milliseconds, zero for unlimited (default: 30 seconds). | `--trace <mode>` | Force tracing mode, can be `on`, `off`, `on-first-retry`, `on-all-retries`, `retain-on-failure`, `retain-on-first-failure`. | `--tsconfig <path>` | Path to a single tsconfig applicable to all imported files (default: look up tsconfig for each imported file separately). | `--ui` | Run tests in interactive UI mode. | `--ui-host <host>` | Host to serve UI on; specifying this option opens UI in a browser tab. | `--ui-port <port>` | Port to serve UI on, 0 for any free port; specifying this option opens UI in a browser tab. | `-u` or `--update-snapshots [mode]` | Update snapshots with actual results. Possible values are "all", "changed", "missing", and "none". Running tests without the flag defaults to "missing"; running tests with the flag but without a value defaults to "changed". | `--update-source-method [mode]` | Update snapshots with actual results. Possible values are "patch" (default), "3way" and "overwrite". "Patch" creates a unified diff file that can be used to update the source code later. "3way" generates merge conflict markers in source code. "Overwrite" overwrites the source code with the new snapshot values. | `-x` | Stop after the first failure. |
| ------ | ----------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------ | --------------- | ------------------------------------------------------------- | ------------------ | ------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------- | ---------------------- | --------------------------------------------------------- | ---------- | ------------------------------------------------- | -------------------- | -------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------- | -------- | ------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------ | ----------- | -------------------------------- | ---------------- | ------------------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | --------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | --------- | --------------- | ------------------- | ------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------ | --------------------------------- | ------------------ | ---------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----------------------------- |

#### Test list[​](https://playwright.dev/docs/test-cli#test-list "Direct link to Test list")

Options `--test-list` and `--test-list-invert` accept a path to a test list file. This file should list tests in the format similar to the output produced in `--list` mode.

```
    # This is a test list file.
    # It can include comments and empty lines.

    # Run ALL tests in a file:
    path/to/example.spec.ts

    # Run all tests in a file for a specific project:
    [chromium] › path/to/example.spec.ts

    # Run all tests in a specific group/suite:
    path/to/example.spec.ts › suite name

    # Run all tests in a nested group:
    path/to/example.spec.ts › outer suite › inner suite

    # Fully qualified test with a project:
    [chromium] › path/to/example.spec.ts:3:9 › suite › nested suite › example test

    # This test is included for all projects:
    path/to/example.spec.ts:3:9 › example test

    # Use "›" or ">" as a separator:
    [firefox] > example.spec.ts > suite > nested suite > example test

    # Line/column numbers are completely ignored, you can omit them.
    # Three entries below refer to the same test:
    example.spec.ts › example test
    example.spec.ts:15 › example test
    example.spec.ts:42:42 › example test

```

### Show Report[​](https://playwright.dev/docs/test-cli#show-report "Direct link to Show Report")

Display HTML report from previous test run. [Read more about the HTML reporter](https://playwright.dev/docs/test-reporters#html-reporter).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-1 "Direct link to Syntax")

```
    npx playwright show-report [report] [options]

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples-1 "Direct link to Examples")

```
    # Show latest test report
    npx playwright show-report

    # Show a specific report
    npx playwright show-report playwright-report/

    # Show report on custom port
    npx playwright show-report --port 8080

```

#### Options[​](https://playwright.dev/docs/test-cli#options "Direct link to Options")

| Option | Description | `--host <host>` | Host to serve report on (default: localhost) | `--port <port>` | Port to serve report on (default: 9323) |
| ------ | ----------- | --------------- | -------------------------------------------- | --------------- | --------------------------------------- |

### Install Browsers[​](https://playwright.dev/docs/test-cli#install-browsers "Direct link to Install Browsers")

Install browsers required by Playwright. [Read more about Playwright's browser support](https://playwright.dev/docs/browsers).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-2 "Direct link to Syntax")

```
    npx playwright install [options] [browser...]
    npx playwright install-deps [options] [browser...]
    npx playwright uninstall

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples-2 "Direct link to Examples")

```
    # Install all browsers
    npx playwright install

    # Install only Chromium
    npx playwright install chromium

    # Install specific browsers
    npx playwright install chromium webkit

    # Install browsers with dependencies
    npx playwright install --with-deps

```

#### Install Options[​](https://playwright.dev/docs/test-cli#install-options "Direct link to Install Options")

| Option | Description | `--force` | Force reinstall of stable browser channels | `--with-deps` | Install browser system dependencies | `--dry-run` | Don't perform installation, just print information | `--only-shell` | Only install chromium-headless-shell instead of full Chromium | `--no-shell` | Don't install chromium-headless-shell |
| ------ | ----------- | --------- | ------------------------------------------ | ------------- | ----------------------------------- | ----------- | -------------------------------------------------- | -------------- | ------------------------------------------------------------- | ------------ | ------------------------------------- |

#### Install Deps Options[​](https://playwright.dev/docs/test-cli#install-deps-options "Direct link to Install Deps Options")

| Option | Description | `--dry-run` | Don't perform installation, just print information |
| ------ | ----------- | ----------- | -------------------------------------------------- |

## Generation & Debugging Tools[​](https://playwright.dev/docs/test-cli#generation--debugging-tools "Direct link to Generation & Debugging Tools")

### Code Generation[​](https://playwright.dev/docs/test-cli#code-generation "Direct link to Code Generation")

Record actions and generate tests for multiple languages. [Read more about Codegen](https://playwright.dev/docs/codegen-intro).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-3 "Direct link to Syntax")

```
    npx playwright codegen [options] [url]

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples-3 "Direct link to Examples")

```
    # Start recording with interactive UI
    npx playwright codegen

    # Record on specific site
    npx playwright codegen https://playwright.dev

    # Generate Python code
    npx playwright codegen --target=python

```

#### Options[​](https://playwright.dev/docs/test-cli#options-1 "Direct link to Options")

| Option | Description | `-b, --browser <name>` | Browser to use: chromium, firefox, or webkit (default: chromium) | `-o, --output <file>` | Output file for the generated script | `--target <language>` | Language to use: javascript, playwright-test, python, etc. | `--test-id-attribute <attr>` | Attribute to use for test IDs |
| ------ | ----------- | ---------------------- | ---------------------------------------------------------------- | --------------------- | ------------------------------------ | --------------------- | ---------------------------------------------------------- | ---------------------------- | ----------------------------- |

### Trace Viewer[​](https://playwright.dev/docs/test-cli#trace-viewer "Direct link to Trace Viewer")

Analyze and view test traces for debugging. [Read more about Trace Viewer](https://playwright.dev/docs/trace-viewer).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-4 "Direct link to Syntax")

```
    npx playwright show-trace [options] [trace]

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples-4 "Direct link to Examples")

```
    # Open trace viewer without a specific trace (can load traces via UI)
    npx playwright show-trace

    # View a trace file
    npx playwright show-trace trace.zip

    # View trace from directory
    npx playwright show-trace trace/

```

#### Options[​](https://playwright.dev/docs/test-cli#options-2 "Direct link to Options")

| Option | Description | `-b, --browser <name>` | Browser to use: chromium, firefox, or webkit (default: chromium) | `-h, --host <host>` | Host to serve trace on | `-p, --port <port>` | Port to serve trace on |
| ------ | ----------- | ---------------------- | ---------------------------------------------------------------- | ------------------- | ---------------------- | ------------------- | ---------------------- |

## Specialized Commands[​](https://playwright.dev/docs/test-cli#specialized-commands "Direct link to Specialized Commands")

### Merge Reports[​](https://playwright.dev/docs/test-cli#merge-reports "Direct link to Merge Reports")

Read [blob](https://playwright.dev/docs/test-reporters#blob-reporter) reports and combine them. [Read more about merge-reports](https://playwright.dev/docs/test-sharding).

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-5 "Direct link to Syntax")

```
    npx playwright merge-reports [options] <blob dir>

```

#### Examples[​](https://playwright.dev/docs/test-cli#examples-5 "Direct link to Examples")

```
    # Combine test reports
    npx playwright merge-reports ./reports

```

#### Options[​](https://playwright.dev/docs/test-cli#options-3 "Direct link to Options")

| Option | Description | `-c, --config <file>` | Configuration file. Can be used to specify additional configuration for the output report | `--reporter <reporter>` | Reporter to use, comma-separated, can be "list", "line", "dot", "json", "junit", "null", "github", "html", "blob" (default: "list") |
| ------ | ----------- | --------------------- | ----------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |

### Clear Cache[​](https://playwright.dev/docs/test-cli#clear-cache "Direct link to Clear Cache")

Clear all Playwright caches.

#### Syntax[​](https://playwright.dev/docs/test-cli#syntax-6 "Direct link to Syntax")

```
    npx playwright clear-cache

```
