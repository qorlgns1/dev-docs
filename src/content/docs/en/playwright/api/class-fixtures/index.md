---
title: "Fixtures"
description: "Playwright Test is based on the concept of the test fixtures. Test fixtures are used to establish environment for each test, giving the test everythin..."
---

Source URL: https://playwright.dev/docs/api/class-fixtures

# Fixtures | Playwright

Playwright Test is based on the concept of the [test fixtures](https://playwright.dev/docs/test-fixtures). Test fixtures are used to establish environment for each test, giving the test everything it needs and nothing else.

Playwright Test looks at each test declaration, analyses the set of fixtures the test needs and prepares those fixtures specifically for the test. Values prepared by the fixtures are merged into a single object that is available to the `test`, hooks, annotations and other fixtures as a first parameter.

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page }) => {
      // ...
    });

```

Given the test above, Playwright Test will set up the `page` fixture before running the test, and tear it down after the test has finished. `page` fixture provides a [Page](https://playwright.dev/docs/api/class-page "Page") object that is available to the test.

Playwright Test comes with builtin fixtures listed below, and you can add your own fixtures as well. Playwright Test also [provides options](https://playwright.dev/docs/api/class-testoptions "TestOptions") to configure [fixtures.browser](https://playwright.dev/docs/api/class-fixtures#fixtures-browser), [fixtures.context](https://playwright.dev/docs/api/class-fixtures#fixtures-context) and [fixtures.page](https://playwright.dev/docs/api/class-fixtures#fixtures-page).

---

## Properties[​](https://playwright.dev/docs/api/class-fixtures#properties "Direct link to Properties")

### browser[​](https://playwright.dev/docs/api/class-fixtures#fixtures-browser "Direct link to browser")

Added in: v1.10 fixtures.browser

[Browser](https://playwright.dev/docs/api/class-browser "Browser") instance is shared between all tests in the [same worker](https://playwright.dev/docs/test-parallel) \- this makes testing efficient. However, each test runs in an isolated [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") and gets a fresh environment.

Learn how to [configure browser](https://playwright.dev/docs/test-configuration) and see [available options](https://playwright.dev/docs/api/class-testoptions "TestOptions").

**Usage**

```
    test.beforeAll(async ({ browser }) => {
      const page = await browser.newPage();
      // ...
    });

```

**Type**

- [Browser](https://playwright.dev/docs/api/class-browser "Browser")

---

### browserName[​](https://playwright.dev/docs/api/class-fixtures#fixtures-browser-name "Direct link to browserName")

Added in: v1.10 fixtures.browserName

Name of the browser that runs tests. Defaults to `'chromium'`. Useful to [annotate tests](https://playwright.dev/docs/test-annotations) based on the browser.

**Usage**

```
    test('skip this test in Firefox', async ({ page, browserName }) => {
      test.skip(browserName === 'firefox', 'Still working on it');
      // ...
    });

```

**Type**

- "chromium" | "firefox" | "webkit"

---

### context[​](https://playwright.dev/docs/api/class-fixtures#fixtures-context "Direct link to context")

Added in: v1.10 fixtures.context

Isolated [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") instance, created for each test. Since contexts are isolated between each other, every test gets a fresh environment, even when multiple tests run in a single [Browser](https://playwright.dev/docs/api/class-browser "Browser") for maximum efficiency.

Learn how to [configure context](https://playwright.dev/docs/test-configuration) and see [available options](https://playwright.dev/docs/api/class-testoptions "TestOptions").

Default [fixtures.page](https://playwright.dev/docs/api/class-fixtures#fixtures-page) belongs to this context.

**Usage**

```
    test('example test', async ({ page, context }) => {
      await context.route('*external.com/*', route => route.abort());
      // ...
    });

```

**Type**

- [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")

---

### page[​](https://playwright.dev/docs/api/class-fixtures#fixtures-page "Direct link to page")

Added in: v1.10 fixtures.page

Isolated [Page](https://playwright.dev/docs/api/class-page "Page") instance, created for each test. Pages are isolated between tests due to [fixtures.context](https://playwright.dev/docs/api/class-fixtures#fixtures-context) isolation.

This is the most common fixture used in a test.

**Usage**

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page }) => {
      await page.goto('/signin');
      await page.getByLabel('User Name').fill('user');
      await page.getByLabel('Password').fill('password');
      await page.getByText('Sign in').click();
      // ...
    });

```

**Type**

- [Page](https://playwright.dev/docs/api/class-page "Page")

---

### request[​](https://playwright.dev/docs/api/class-fixtures#fixtures-request "Direct link to request")

Added in: v1.10 fixtures.request

Isolated [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext") instance for each test.

**Usage**

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ request }) => {
      await request.post('/signin', {
        data: {
          username: 'user',
          password: 'password'
        }
      });
      // ...
    });

```

**Type**

- [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")
