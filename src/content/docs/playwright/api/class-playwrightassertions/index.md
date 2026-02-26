---
title: "PlaywrightAssertions"
description: "Playwright gives you Web-First Assertions with convenience methods for creating assertions that will wait and retry until the expected condition is me..."
---

Source URL: https://playwright.dev/docs/api/class-playwrightassertions

# PlaywrightAssertions | Playwright

Playwright gives you Web-First Assertions with convenience methods for creating assertions that will wait and retry until the expected condition is met.

Consider the following example:

```
    import { test, expect } from '@playwright/test';

    test('status becomes submitted', async ({ page }) => {
      // ...
      await page.locator('#submit-button').click();
      await expect(page.locator('.status')).toHaveText('Submitted');
    });

```

Playwright will be re-testing the node with the selector `.status` until fetched Node has the `"Submitted"` text. It will be re-fetching the node and checking it over and over, until the condition is met or until the timeout is reached. You can pass this timeout as an option.

By default, the timeout for assertions is set to 5 seconds.

---

## Methods[​](https://playwright.dev/docs/api/class-playwrightassertions#methods "Direct link to Methods")

### expect(response)[​](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-api-response "Direct link to expect(response)")

Added in: v1.18 playwrightAssertions.expect(response)

Creates a [APIResponseAssertions](https://playwright.dev/docs/api/class-apiresponseassertions "APIResponseAssertions") object for the given [APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse").

**Usage**

**Arguments**

- `response` [APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-api-response-option-response)

[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse") object to use for assertions.

**Returns**

- [APIResponseAssertions](https://playwright.dev/docs/api/class-apiresponseassertions "APIResponseAssertions")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-api-response-return)

---

### expect(value)[​](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-generic "Direct link to expect(value)")

Added in: v1.9 playwrightAssertions.expect(value)

Creates a [GenericAssertions](https://playwright.dev/docs/api/class-genericassertions "GenericAssertions") object for the given value.

**Usage**

```
    expect(value);

```

**Arguments**

- `value` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-generic-option-value)

Value that will be asserted.

**Returns**

- [GenericAssertions](https://playwright.dev/docs/api/class-genericassertions "GenericAssertions")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-generic-return)

---

### expect(locator)[​](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-locator "Direct link to expect(locator)")

Added in: v1.18 playwrightAssertions.expect(locator)

Creates a [LocatorAssertions](https://playwright.dev/docs/api/class-locatorassertions "LocatorAssertions") object for the given [Locator](https://playwright.dev/docs/api/class-locator "Locator").

**Usage**

**Arguments**

- `locator` [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-locator-option-locator)

[Locator](https://playwright.dev/docs/api/class-locator "Locator") object to use for assertions.

**Returns**

- [LocatorAssertions](https://playwright.dev/docs/api/class-locatorassertions "LocatorAssertions")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-locator-return)

---

### expect(page)[​](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-page "Direct link to expect(page)")

Added in: v1.18 playwrightAssertions.expect(page)

Creates a [PageAssertions](https://playwright.dev/docs/api/class-pageassertions "PageAssertions") object for the given [Page](https://playwright.dev/docs/api/class-page "Page").

**Usage**

**Arguments**

- `page` [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-page-option-page)

[Page](https://playwright.dev/docs/api/class-page "Page") object to use for assertions.

**Returns**

- [PageAssertions](https://playwright.dev/docs/api/class-pageassertions "PageAssertions")[#](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-page-return)
