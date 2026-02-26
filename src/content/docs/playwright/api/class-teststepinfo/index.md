---
title: "TestStepInfo"
description: "contains information about currently running test step. It is passed as an argument to the step function.  provides utilities to control test step exe..."
---

Source URL: https://playwright.dev/docs/api/class-teststepinfo

# TestStepInfo | Playwright

`TestStepInfo` contains information about currently running test step. It is passed as an argument to the step function. `TestStepInfo` provides utilities to control test step execution.

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page, browserName }) => {
      await test.step('check some behavior', async step => {
        step.skip(browserName === 'webkit', 'The feature is not available in WebKit');
        // ... rest of the step code
      });
    });

```

---

## Methods[​](https://playwright.dev/docs/api/class-teststepinfo#methods "Direct link to Methods")

### attach[​](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach "Direct link to attach")

Added in: v1.51 testStepInfo.attach

Attach a value or a file from disk to the current test step. Some reporters show test step attachments. Either [path](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-path) or [body](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-body) must be specified, but not both. Calling this method will attribute the attachment to the step, as opposed to [testInfo.attach()](https://playwright.dev/docs/api/class-testinfo#test-info-attach) which stores all attachments at the test level.

For example, you can attach a screenshot to the test step:

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page }) => {
      await page.goto('https://playwright.dev');
      await test.step('check page rendering', async step => {
        const screenshot = await page.screenshot();
        await step.attach('screenshot', { body: screenshot, contentType: 'image/png' });
      });
    });

```

Or you can attach files returned by your APIs:

```
    import { test, expect } from '@playwright/test';
    import { download } from './my-custom-helpers';

    test('basic test', async ({}) => {
      await test.step('check download behavior', async step => {
        const tmpPath = await download('a');
        await step.attach('downloaded', { path: tmpPath });
      });
    });

```

note

[testStepInfo.attach()](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach) automatically takes care of copying attached files to a location that is accessible to reporters. You can safely remove the attachment after awaiting the attach call.

**Usage**

```
    await testStepInfo.attach(name);
    await testStepInfo.attach(name, options);

```

**Arguments**

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-name)

Attachment name. The name will also be sanitized and used as the prefix of file name when saving to disk.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `body` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-body)

Attachment body. Mutually exclusive with [path](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-path).

    * `contentType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-content-type)

Content type of this attachment to properly present in the report, for example `'application/json'` or `'image/png'`. If omitted, content type is inferred based on the [path](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-path), or defaults to `text/plain` for [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") attachments and `application/octet-stream` for [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") attachments.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-path)

Path on the filesystem to the attached file. Mutually exclusive with [body](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-option-body).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-attach-return)

---

### skip()[​](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-skip-1 "Direct link to skip()")

Added in: v1.51 testStepInfo.skip()

Abort the currently running step and mark it as skipped. Useful for steps that are currently failing and planned for a near-term fix.

**Usage**

```
    import { test, expect } from '@playwright/test';

    test('my test', async ({ page }) => {
      await test.step('check expectations', async step => {
        step.skip();
        // step body below will not run
        // ...
      });
    });

```

---

### skip(condition)[​](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-skip-2 "Direct link to skip(condition)")

Added in: v1.51 testStepInfo.skip(condition)

Conditionally abort the currently running step and mark it as skipped with an optional description. Useful for steps that should not be executed in some cases.

**Usage**

```
    import { test, expect } from '@playwright/test';

    test('my test', async ({ page, isMobile }) => {
      await test.step('check desktop expectations', async step => {
        step.skip(isMobile, 'not present in the mobile layout');
        // step body below will not run
        // ...
      });
    });

```

**Arguments**

- `condition` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-skip-2-option-condition)

A skip condition. Test step is skipped when the condition is `true`.

- `description` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-skip-2-option-description)

Optional description that will be reflected in a test report.

---

## Properties[​](https://playwright.dev/docs/api/class-teststepinfo#properties "Direct link to Properties")

### titlePath[​](https://playwright.dev/docs/api/class-teststepinfo#test-step-info-title-path "Direct link to titlePath")

Added in: v1.55 testStepInfo.titlePath

The full title path starting with the test file name, including the step titles. See also [testInfo.titlePath](https://playwright.dev/docs/api/class-testinfo#test-info-title-path).

**Usage**

```
    testStepInfo.titlePath

```

**Type**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>
