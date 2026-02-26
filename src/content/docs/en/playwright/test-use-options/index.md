---
title: "Configuration (use)"
description: "In addition to configuring the test runner you can also configure Emulation, Network and Recording for the Browser or BrowserContext. These options ar..."
---

Source URL: https://playwright.dev/docs/test-use-options

# Configuration (use) | Playwright

## Introduction[​](https://playwright.dev/docs/test-use-options#introduction "Direct link to Introduction")

In addition to configuring the test runner you can also configure [Emulation](https://playwright.dev/docs/test-use-options#emulation-options), [Network](https://playwright.dev/docs/test-use-options#network-options) and [Recording](https://playwright.dev/docs/test-use-options#recording-options) for the [Browser](https://playwright.dev/docs/api/class-browser "Browser") or [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext"). These options are passed to the `use: {}` object in the Playwright config.

### Basic Options[​](https://playwright.dev/docs/test-use-options#basic-options "Direct link to Basic Options")

Set the base URL and storage state for all tests:

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        // Base URL to use in actions like `await page.goto('/')`.
        baseURL: 'http://localhost:3000',

        // Populates context with given storage state.
        storageState: 'state.json',
      },
    });

```

| Option | Description | [testOptions.baseURL](https://playwright.dev/docs/api/class-testoptions#test-options-base-url) | Base URL used for all pages in the context. Allows navigating by using just the path, for example `page.goto('/settings')`. | [testOptions.storageState](https://playwright.dev/docs/api/class-testoptions#test-options-storage-state) | Populates context with given storage state. Useful for easy authentication, [learn more](https://playwright.dev/docs/auth). |
| ------ | ----------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |

### Emulation Options[​](https://playwright.dev/docs/test-use-options#emulation-options "Direct link to Emulation Options")

With Playwright you can emulate a real device such as a mobile phone or tablet. See our [guide on projects](https://playwright.dev/docs/test-projects) for more info on emulating devices. You can also emulate the `"geolocation"`, `"locale"` and `"timezone"` for all tests or for a specific test as well as set the `"permissions"` to show notifications or change the `"colorScheme"`. See our [Emulation](https://playwright.dev/docs/emulation) guide to learn more.

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        // Emulates `'prefers-colors-scheme'` media feature.
        colorScheme: 'dark',

        // Context geolocation.
        geolocation: { longitude: 12.492507, latitude: 41.889938 },

        // Emulates the user locale.
        locale: 'en-GB',

        // Grants specified permissions to the browser context.
        permissions: ['geolocation'],

        // Emulates the user timezone.
        timezoneId: 'Europe/Paris',

        // Viewport used for all pages in the context.
        viewport: { width: 1280, height: 720 },
      },
    });

```

| Option | Description | [testOptions.colorScheme](https://playwright.dev/docs/api/class-testoptions#test-options-color-scheme) | [Emulates](https://playwright.dev/docs/emulation#color-scheme-and-media) `'prefers-colors-scheme'` media feature, supported values are `'light'` and `'dark'` | [testOptions.geolocation](https://playwright.dev/docs/api/class-testoptions#test-options-geolocation) | Context [geolocation](https://playwright.dev/docs/emulation#geolocation). | [testOptions.locale](https://playwright.dev/docs/api/class-testoptions#test-options-locale) | [Emulates](https://playwright.dev/docs/emulation#locale--timezone) the user locale, for example `en-GB`, `de-DE`, etc. | [testOptions.permissions](https://playwright.dev/docs/api/class-testoptions#test-options-permissions) | A list of [permissions](https://playwright.dev/docs/emulation#permissions) to grant to all pages in the context. | [testOptions.timezoneId](https://playwright.dev/docs/api/class-testoptions#test-options-timezone-id) | Changes the [timezone](https://playwright.dev/docs/emulation#locale--timezone) of the context. | [testOptions.viewport](https://playwright.dev/docs/api/class-testoptions#test-options-viewport) | [Viewport](https://playwright.dev/docs/emulation#viewport) used for all pages in the context. |
| ------ | ----------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |

### Network Options[​](https://playwright.dev/docs/test-use-options#network-options "Direct link to Network Options")

Available options to configure networking:

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        // Whether to automatically download all the attachments.
        acceptDownloads: false,

        // An object containing additional HTTP headers to be sent with every request.
        extraHTTPHeaders: {
          'X-My-Header': 'value',
        },

        // Credentials for HTTP authentication.
        httpCredentials: {
          username: 'user',
          password: 'pass',
        },

        // Whether to ignore HTTPS errors during navigation.
        ignoreHTTPSErrors: true,

        // Whether to emulate network being offline.
        offline: true,

        // Proxy settings used for all pages in the test.
        proxy: {
          server: 'http://myproxy.com:3128',
          bypass: 'localhost',
        },
      },
    });

```

| Option | Description | [testOptions.acceptDownloads](https://playwright.dev/docs/api/class-testoptions#test-options-accept-downloads) | Whether to automatically download all the attachments, defaults to `true`. [Learn more](https://playwright.dev/docs/downloads) about working with downloads. | [testOptions.extraHTTPHeaders](https://playwright.dev/docs/api/class-testoptions#test-options-extra-http-headers) | An object containing additional HTTP headers to be sent with every request. All header values must be strings. | [testOptions.httpCredentials](https://playwright.dev/docs/api/class-testoptions#test-options-http-credentials) | Credentials for [HTTP authentication](https://playwright.dev/docs/network#http-authentication). | [testOptions.ignoreHTTPSErrors](https://playwright.dev/docs/api/class-testoptions#test-options-ignore-https-errors) | Whether to ignore HTTPS errors during navigation. | [testOptions.offline](https://playwright.dev/docs/api/class-testoptions#test-options-offline) | Whether to emulate network being offline. | [testOptions.proxy](https://playwright.dev/docs/api/class-testoptions#test-options-proxy) | [Proxy settings](https://playwright.dev/docs/network#http-proxy) used for all pages in the test. |
| ------ | ----------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |

note

You don't have to configure anything to mock network requests. Just define a custom [Route](https://playwright.dev/docs/api/class-route "Route") that mocks the network for a browser context. See our [network mocking guide](https://playwright.dev/docs/network) to learn more.

### Recording Options[​](https://playwright.dev/docs/test-use-options#recording-options "Direct link to Recording Options")

With Playwright you can capture screenshots, record videos as well as traces of your test. By default these are turned off but you can enable them by setting the `screenshot`, `video` and `trace` options in your `playwright.config.js` file.

Trace files, screenshots and videos will appear in the test output directory, typically `test-results`.

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        // Capture screenshot after each test failure.
        screenshot: 'only-on-failure',

        // Record trace only when retrying a test for the first time.
        trace: 'on-first-retry',

        // Record video only when retrying a test for the first time.
        video: 'on-first-retry'
      },
    });

```

| Option | Description | [testOptions.screenshot](https://playwright.dev/docs/api/class-testoptions#test-options-screenshot) | Capture [screenshots](https://playwright.dev/docs/screenshots) of your test. Options include `'off'`, `'on'` and `'only-on-failure'` | [testOptions.trace](https://playwright.dev/docs/api/class-testoptions#test-options-trace) | Playwright can produce test traces while running the tests. Later on, you can view the trace and get detailed information about Playwright execution by opening [Trace Viewer](https://playwright.dev/docs/trace-viewer). Options include: `'off'`, `'on'`, `'retain-on-failure'` and `'on-first-retry'` | [testOptions.video](https://playwright.dev/docs/api/class-testoptions#test-options-video) | Playwright can record [videos](https://playwright.dev/docs/videos) for your tests. Options include: `'off'`, `'on'`, `'retain-on-failure'` and `'on-first-retry'` |
| ------ | ----------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Other Options[​](https://playwright.dev/docs/test-use-options#other-options "Direct link to Other Options")

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        // Maximum time each action such as `click()` can take. Defaults to 0 (no limit).
        actionTimeout: 0,

        // Name of the browser that runs tests. For example `chromium`, `firefox`, `webkit`.
        browserName: 'chromium',

        // Toggles bypassing Content-Security-Policy.
        bypassCSP: true,

        // Channel to use, for example "chrome", "chrome-beta", "msedge", "msedge-beta".
        channel: 'chrome',

        // Run browser in headless mode.
        headless: false,

        // Change the default data-testid attribute.
        testIdAttribute: 'pw-test-id',
      },
    });

```

| Option | Description | [testOptions.actionTimeout](https://playwright.dev/docs/api/class-testoptions#test-options-action-timeout) | Timeout for each Playwright action in milliseconds. Defaults to `0` (no timeout). Learn more about [timeouts](https://playwright.dev/docs/test-timeouts) and how to set them for a single test. | [testOptions.browserName](https://playwright.dev/docs/api/class-testoptions#test-options-browser-name) | Name of the browser that runs tests. Defaults to 'chromium'. Options include `chromium`, `firefox`, or `webkit`. | [testOptions.bypassCSP](https://playwright.dev/docs/api/class-testoptions#test-options-bypass-csp) | Toggles bypassing Content-Security-Policy. Useful when CSP includes the production origin. Defaults to `false`. | [testOptions.channel](https://playwright.dev/docs/api/class-testoptions#test-options-channel) | Browser channel to use. [Learn more](https://playwright.dev/docs/browsers) about different browsers and channels. | [testOptions.headless](https://playwright.dev/docs/api/class-testoptions#test-options-headless) | Whether to run the browser in headless mode meaning no browser is shown when running tests. Defaults to `true`. | [testOptions.testIdAttribute](https://playwright.dev/docs/api/class-testoptions#test-options-test-id-attribute) | Changes the default [`data-testid` attribute](https://playwright.dev/docs/locators#locate-by-test-id) used by Playwright locators. |
| ------ | ----------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |

### More browser and context options[​](https://playwright.dev/docs/test-use-options#more-browser-and-context-options "Direct link to More browser and context options")

Any options accepted by [browserType.launch()](https://playwright.dev/docs/api/class-browsertype#browser-type-launch), [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context) or [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect) can be put into `launchOptions`, `contextOptions` or `connectOptions` respectively in the `use` section.

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        launchOptions: {
          slowMo: 50,
        },
      },
    });

```

However, most common ones like `headless` or `viewport` are available directly in the `use` section - see [basic options](https://playwright.dev/docs/test-use-options#basic-options), [emulation](https://playwright.dev/docs/test-use-options#emulation-options) or [network](https://playwright.dev/docs/test-use-options#network-options).

### Explicit Context Creation and Option Inheritance[​](https://playwright.dev/docs/test-use-options#explicit-context-creation-and-option-inheritance "Direct link to Explicit Context Creation and Option Inheritance")

If using the built-in `browser` fixture, calling [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context) will create a context with options inherited from the config:

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        userAgent: 'some custom ua',
        viewport: { width: 100, height: 100 },
      },
    });

```

An example test illustrating the initial context options are set:

```
    test('should inherit use options on context when using built-in browser fixture', async ({
      browser,
    }) => {
      const context = await browser.newContext();
      const page = await context.newPage();
      expect(await page.evaluate(() => navigator.userAgent)).toBe('some custom ua');
      expect(await page.evaluate(() => window.innerWidth)).toBe(100);
      await context.close();
    });

```

### Configuration Scopes[​](https://playwright.dev/docs/test-use-options#configuration-scopes "Direct link to Configuration Scopes")

You can configure Playwright globally, per project, or per test. For example, you can set the locale to be used globally by adding `locale` to the `use` option of the Playwright config, and then override it for a specific project using the `project` option in the config. You can also override it for a specific test by adding `test.use({})` in the test file and passing in the options.

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        locale: 'en-GB'
      },
    });

```

You can override options for a specific project using the `project` option in the Playwright config.

```
    import { defineConfig, devices } from '@playwright/test';

    export default defineConfig({
      projects: [
        {
          name: 'chromium',
          use: {
            ...devices['Desktop Chrome'],
            locale: 'de-DE',
          },
        },
      ],
    });

```

You can override options for a specific test file by using the `test.use()` method and passing in the options. For example to run tests with the French locale for a specific test:

```
    import { test, expect } from '@playwright/test';

    test.use({ locale: 'fr-FR' });

    test('example', async ({ page }) => {
      // ...
    });

```

The same works inside a describe block. For example to run tests in a describe block with the French locale:

```
    import { test, expect } from '@playwright/test';

    test.describe('french language block', () => {

      test.use({ locale: 'fr-FR' });

      test('example', async ({ page }) => {
        // ...
      });
    });

```

### Reset an option[​](https://playwright.dev/docs/test-use-options#reset-an-option "Direct link to Reset an option")

You can reset an option to the value defined in the config file. Consider the following config that sets a `baseURL`:

playwright.config.ts

```
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        baseURL: 'https://playwright.dev',
      },
    });

```

You can now configure `baseURL` for a file, and also opt-out for a single test.

intro.spec.ts

```
    import { test } from '@playwright/test';

    // Configure baseURL for this file.
    test.use({ baseURL: 'https://playwright.dev/docs/intro' });

    test('check intro contents', async ({ page }) => {
      // This test will use "https://playwright.dev/docs/intro" base url as defined above.
    });

    test.describe(() => {
      // Reset the value to a config-defined one.
      test.use({ baseURL: undefined });

      test('can navigate to intro from the home page', async ({ page }) => {
        // This test will use "https://playwright.dev" base url as defined in the config.
      });
    });

```

If you would like to completely reset the value to `undefined`, use a long-form fixture notation.

intro.spec.ts

```
    import { test } from '@playwright/test';

    // Completely unset baseURL for this file.
    test.use({
      baseURL: [async ({}, use) => use(undefined), { scope: 'test' }],
    });

    test('no base url', async ({ page }) => {
      // This test will not have a base url.
    });

```
