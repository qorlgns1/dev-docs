---
title: "Assertions"
description: "Playwright includes test assertions in the form of  function. To make an assertion, call  and choose a matcher that reflects the expectation. There ar..."
---

Source URL: https://playwright.dev/docs/test-assertions

# Assertions | Playwright

## Introduction[​](https://playwright.dev/docs/test-assertions#introduction "Direct link to Introduction")

Playwright includes test assertions in the form of `expect` function. To make an assertion, call `expect(value)` and choose a matcher that reflects the expectation. There are many [generic matchers](https://playwright.dev/docs/api/class-genericassertions) like `toEqual`, `toContain`, `toBeTruthy` that can be used to assert any conditions.

```
    expect(success).toBeTruthy();

```

Playwright also includes web-specific [async matchers](https://playwright.dev/docs/api/class-locatorassertions) that will wait until the expected condition is met. Consider the following example:

```
    await expect(page.getByTestId('status')).toHaveText('Submitted');

```

Playwright will be re-testing the element with the test id of `status` until the fetched element has the `"Submitted"` text. It will re-fetch the element and check it over and over, until the condition is met or until the timeout is reached. You can either pass this timeout or configure it once via the [testConfig.expect](https://playwright.dev/docs/api/class-testconfig#test-config-expect) value in the test config.

By default, the timeout for assertions is set to 5 seconds. Learn more about [various timeouts](https://playwright.dev/docs/test-timeouts).

## Auto-retrying assertions[​](https://playwright.dev/docs/test-assertions#auto-retrying-assertions "Direct link to Auto-retrying assertions")

The following assertions will retry until the assertion passes, or the assertion timeout is reached. Note that retrying assertions are async, so you must `await` them.

| Assertion | Description | [await expect(locator).toBeAttached()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-attached) | Element is attached | [await expect(locator).toBeChecked()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-checked) | Checkbox is checked | [await expect(locator).toBeDisabled()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-disabled) | Element is disabled | [await expect(locator).toBeEditable()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-editable) | Element is editable | [await expect(locator).toBeEmpty()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-empty) | Container is empty | [await expect(locator).toBeEnabled()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-enabled) | Element is enabled | [await expect(locator).toBeFocused()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-focused) | Element is focused | [await expect(locator).toBeHidden()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-hidden) | Element is not visible | [await expect(locator).toBeInViewport()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-in-viewport) | Element intersects viewport | [await expect(locator).toBeVisible()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-visible) | Element is visible | [await expect(locator).toContainText()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-contain-text) | Element contains text | [await expect(locator).toContainClass()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-contain-class) | Element has specified CSS classes | [await expect(locator).toHaveAccessibleDescription()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-accessible-description) | Element has a matching [accessible description](https://w3c.github.io/accname/#dfn-accessible-description) | [await expect(locator).toHaveAccessibleName()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-accessible-name) | Element has a matching [accessible name](https://w3c.github.io/accname/#dfn-accessible-name) | [await expect(locator).toHaveAttribute()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-attribute) | Element has a DOM attribute | [await expect(locator).toHaveClass()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-class) | Element has specified CSS class property | [await expect(locator).toHaveCount()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-count) | List has exact number of children | [await expect(locator).toHaveCSS()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-css) | Element has CSS property | [await expect(locator).toHaveId()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-id) | Element has an ID | [await expect(locator).toHaveJSProperty()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-js-property) | Element has a JavaScript property | [await expect(locator).toHaveRole()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-role) | Element has a specific [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles) | [await expect(locator).toHaveScreenshot()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-screenshot-1) | Element has a screenshot | [await expect(locator).toHaveText()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-text) | Element matches text | [await expect(locator).toHaveValue()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-value) | Input has a value | [await expect(locator).toHaveValues()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-values) | Select has options selected | [await expect(locator).toMatchAriaSnapshot()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-match-aria-snapshot) | Element matches the Aria snapshot | [await expect(page).toHaveScreenshot()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1) | Page has a screenshot | [await expect(page).toHaveTitle()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-title) | Page has a title | [await expect(page).toHaveURL()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-url) | Page has a URL | [await expect(response).toBeOK()](https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok) | Response has an OK status |
| --------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |

## Non-retrying assertions[​](https://playwright.dev/docs/test-assertions#non-retrying-assertions "Direct link to Non-retrying assertions")

These assertions allow to test any conditions, but do not auto-retry. Most of the time, web pages show information asynchronously, and using non-retrying assertions can lead to a flaky test.

Prefer [auto-retrying](https://playwright.dev/docs/test-assertions#auto-retrying-assertions) assertions whenever possible. For more complex assertions that need to be retried, use [`expect.poll`](https://playwright.dev/docs/test-assertions#expectpoll) or [`expect.toPass`](https://playwright.dev/docs/test-assertions#expecttopass).

| Assertion | Description | [expect(value).toBe()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be) | Value is the same | [expect(value).toBeCloseTo()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-close-to) | Number is approximately equal | [expect(value).toBeDefined()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-defined) | Value is not `undefined` | [expect(value).toBeFalsy()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-falsy) | Value is falsy, e.g. `false`, `0`, `null`, etc. | [expect(value).toBeGreaterThan()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than) | Number is more than | [expect(value).toBeGreaterThanOrEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than-or-equal) | Number is more than or equal | [expect(value).toBeInstanceOf()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-instance-of) | Object is an instance of a class | [expect(value).toBeLessThan()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than) | Number is less than | [expect(value).toBeLessThanOrEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than-or-equal) | Number is less than or equal | [expect(value).toBeNaN()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-na-n) | Value is `NaN` | [expect(value).toBeNull()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-null) | Value is `null` | [expect(value).toBeTruthy()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-truthy) | Value is truthy, i.e. not `false`, `0`, `null`, etc. | [expect(value).toBeUndefined()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-undefined) | Value is `undefined` | [expect(value).toContain()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-1) | String contains a substring | [expect(value).toContain()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-2) | Array or set contains an element | [expect(value).toContainEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-equal) | Array or set contains a similar element | [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) | Value is similar - deep equality and pattern matching | [expect(value).toHaveLength()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-length) | Array or string has length | [expect(value).toHaveProperty()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-property) | Object has a property | [expect(value).toMatch()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match) | String matches a regular expression | [expect(value).toMatchObject()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match-object) | Object contains specified properties | [expect(value).toStrictEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-strict-equal) | Value is similar, including property types | [expect(value).toThrow()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw) | Function throws an error |
| --------- | ----------- | -------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------ |

## Asymmetric matchers[​](https://playwright.dev/docs/test-assertions#asymmetric-matchers "Direct link to Asymmetric matchers")

These expressions can be nested in other assertions to allow more relaxed matching against a given condition.

| Matcher | Description | [expect.any()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-any) | Matches any instance of a class/primitive | [expect.anything()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-anything) | Matches anything | [expect.arrayContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-containing) | Array contains specific elements | [expect.arrayOf()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-of) | Array contains elements of specific type | [expect.closeTo()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-close-to) | Number is approximately equal | [expect.objectContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-object-containing) | Object contains specific properties | [expect.stringContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-containing) | String contains a substring | [expect.stringMatching()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-matching) | String matches a regular expression |
| ------- | ----------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

## Negating matchers[​](https://playwright.dev/docs/test-assertions#negating-matchers "Direct link to Negating matchers")

In general, we can expect the opposite to be true by adding a `.not` to the front of the matchers:

```
    expect(value).not.toEqual(0);
    await expect(locator).not.toContainText('some text');

```

## Soft assertions[​](https://playwright.dev/docs/test-assertions#soft-assertions "Direct link to Soft assertions")

By default, failed assertion will terminate test execution. Playwright also supports _soft assertions_ : failed soft assertions **do not** terminate test execution, but mark the test as failed.

```
    // Make a few checks that will not stop the test when failed...
    await expect.soft(page.getByTestId('status')).toHaveText('Success');
    await expect.soft(page.getByTestId('eta')).toHaveText('1 day');

    // ... and continue the test to check more things.
    await page.getByRole('link', { name: 'next page' }).click();
    await expect.soft(page.getByRole('heading', { name: 'Make another order' })).toBeVisible();

```

At any point during test execution, you can check whether there were any soft assertion failures:

```
    // Make a few checks that will not stop the test when failed...
    await expect.soft(page.getByTestId('status')).toHaveText('Success');
    await expect.soft(page.getByTestId('eta')).toHaveText('1 day');

    // Avoid running further if there were soft assertion failures.
    expect(test.info().errors).toHaveLength(0);

```

Note that soft assertions only work with Playwright test runner.

## Custom expect message[​](https://playwright.dev/docs/test-assertions#custom-expect-message "Direct link to Custom expect message")

You can specify a custom expect message as a second argument to the `expect` function, for example:

```
    await expect(page.getByText('Name'), 'should be logged in').toBeVisible();

```

This message will be shown in reporters, both for passing and failing expects, providing more context about the assertion.

When expect passes, you might see a successful step like this:

```
    ✅ should be logged in    @example.spec.ts:18

```

When expect fails, the error would look like this:

```
        Error: should be logged in

        Call log:
          - expect.toBeVisible with timeout 5000ms
          - waiting for "getByText('Name')"

          2 |
          3 | test('example test', async({ page }) => {
        > 4 |   await expect(page.getByText('Name'), 'should be logged in').toBeVisible();
            |                                                                  ^
          5 | });
          6 |

```

Soft assertions also support custom message:

```
    expect.soft(value, 'my soft assertion').toBe(56);

```

## expect.configure[​](https://playwright.dev/docs/test-assertions#expectconfigure "Direct link to expect.configure")

You can create your own pre-configured `expect` instance to have its own defaults such as `timeout` and `soft`.

```
    const slowExpect = expect.configure({ timeout: 10000 });
    await slowExpect(locator).toHaveText('Submit');

    // Always do soft assertions.
    const softExpect = expect.configure({ soft: true });
    await softExpect(locator).toHaveText('Submit');

```

## expect.poll[​](https://playwright.dev/docs/test-assertions#expectpoll "Direct link to expect.poll")

You can convert any synchronous `expect` to an asynchronous polling one using `expect.poll`.

The following method will poll given function until it returns HTTP status 200:

```
    await expect.poll(async () => {
      const response = await page.request.get('https://api.example.com');
      return response.status();
    }, {
      // Custom expect message for reporting, optional.
      message: 'make sure API eventually succeeds',
      // Poll for 10 seconds; defaults to 5 seconds. Pass 0 to disable timeout.
      timeout: 10000,
    }).toBe(200);

```

You can also specify custom polling intervals:

```
    await expect.poll(async () => {
      const response = await page.request.get('https://api.example.com');
      return response.status();
    }, {
      // Probe, wait 1s, probe, wait 2s, probe, wait 10s, probe, wait 10s, probe
      // ... Defaults to [100, 250, 500, 1000].
      intervals: [1_000, 2_000, 10_000],
      timeout: 60_000
    }).toBe(200);

```

You can combine `expect.configure({ soft: true })` with expect.poll to perform soft assertions in polling logic.

```
    const softExpect = expect.configure({ soft: true });
    await softExpect.poll(async () => {
      const response = await page.request.get('https://api.example.com');
      return response.status();
    }, {}).toBe(200);

```

This allows the test to continue even if the assertion inside poll fails.

## expect.toPass[​](https://playwright.dev/docs/test-assertions#expecttopass "Direct link to expect.toPass")

You can retry blocks of code until they are passing successfully.

```
    await expect(async () => {
      const response = await page.request.get('https://api.example.com');
      expect(response.status()).toBe(200);
    }).toPass();

```

You can also specify custom timeout and retry intervals:

```
    await expect(async () => {
      const response = await page.request.get('https://api.example.com');
      expect(response.status()).toBe(200);
    }).toPass({
      // Probe, wait 1s, probe, wait 2s, probe, wait 10s, probe, wait 10s, probe
      // ... Defaults to [100, 250, 500, 1000].
      intervals: [1_000, 2_000, 10_000],
      timeout: 60_000
    });

```

Note that by default `toPass` has timeout 0 and does not respect custom [expect timeout](https://playwright.dev/docs/test-timeouts#expect-timeout).

## Add custom matchers using expect.extend[​](https://playwright.dev/docs/test-assertions#add-custom-matchers-using-expectextend "Direct link to Add custom matchers using expect.extend")

You can extend Playwright assertions by providing custom matchers. These matchers will be available on the `expect` object.

In this example we add a custom `toHaveAmount` function. Custom matcher should return a `pass` flag indicating whether the assertion passed, and a `message` callback that's used when the assertion fails.

fixtures.ts

```
    import { expect as baseExpect } from '@playwright/test';
    import type { Locator } from '@playwright/test';

    export { test } from '@playwright/test';

    export const expect = baseExpect.extend({
      async toHaveAmount(locator: Locator, expected: number, options?: { timeout?: number }) {
        const assertionName = 'toHaveAmount';
        let pass: boolean;
        let matcherResult: any;
        try {
          const expectation = this.isNot ? baseExpect(locator).not : baseExpect(locator);
          await expectation.toHaveAttribute('data-amount', String(expected), options);
          pass = true;
        } catch (e: any) {
          matcherResult = e.matcherResult;
          pass = false;
        }

        if (this.isNot) {
          pass =!pass;
        }

        const message = pass
          ? () => this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot }) +
              '\n\n' +
              `Locator: ${locator}\n` +
              `Expected: not ${this.utils.printExpected(expected)}\n` +
              (matcherResult ? `Received: ${this.utils.printReceived(matcherResult.actual)}` : '')
          : () =>  this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot }) +
              '\n\n' +
              `Locator: ${locator}\n` +
              `Expected: ${this.utils.printExpected(expected)}\n` +
              (matcherResult ? `Received: ${this.utils.printReceived(matcherResult.actual)}` : '');

        return {
          message,
          pass,
          name: assertionName,
          expected,
          actual: matcherResult?.actual,
        };
      },
    });

```

Now we can use `toHaveAmount` in the test.

example.spec.ts

```
    import { test, expect } from './fixtures';

    test('amount', async () => {
      await expect(page.locator('.cart')).toHaveAmount(4);
    });

```

### Compatibility with expect library[​](https://playwright.dev/docs/test-assertions#compatibility-with-expect-library "Direct link to Compatibility with expect library")

note

Do not confuse Playwright's `expect` with the [`expect` library](https://jestjs.io/docs/expect). The latter is not fully integrated with Playwright test runner, so make sure to use Playwright's own `expect`.

### Combine custom matchers from multiple modules[​](https://playwright.dev/docs/test-assertions#combine-custom-matchers-from-multiple-modules "Direct link to Combine custom matchers from multiple modules")

You can combine custom matchers from multiple files or modules.

fixtures.ts

```
    import { mergeTests, mergeExpects } from '@playwright/test';
    import { test as dbTest, expect as dbExpect } from 'database-test-utils';
    import { test as a11yTest, expect as a11yExpect } from 'a11y-test-utils';

    export const expect = mergeExpects(dbExpect, a11yExpect);
    export const test = mergeTests(dbTest, a11yTest);

```

test.spec.ts

```
    import { test, expect } from './fixtures';

    test('passes', async ({ database }) => {
      await expect(database).toHaveDatabaseUser('admin');
    });

```
