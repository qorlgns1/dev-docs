---
title: "browser.instances"
description: "Defines multiple browser setups. Every config has to have at least a  field."
---

Source URL: https://vitest.dev/config/browser/instances

# browser.instances

- **Type:** `BrowserConfig`
- **Default:** `[]`

Defines multiple browser setups. Every config has to have at least a `browser` field.

You can specify most of the [project options](https://vitest.dev/config/) (not marked with a icon) and some of the `browser` options like `browser.testerHtmlPath`.

::: warning
Every browser config inherits options from the root config:

```ts{3,9} [vitest.config.ts]
export default defineConfig({
  test: {
    setupFile: ['./root-setup-file.js'],
    browser: {
      enabled: true,
      testerHtmlPath: './custom-path.html',
      instances: [
        {
          // will have both setup files: "root" and "browser"
          setupFile: ['./browser-setup-file.js'],
          // implicitly has "testerHtmlPath" from the root config // [!code warning]
          // testerHtmlPath: './custom-path.html', // [!code warning]
        },
      ],
    },
  },
})
```

For more examples, refer to the ["Multiple Setups" guide](https://vitest.dev/guide/browser/multiple-setups).
:::

List of available `browser` options:

- `browser` (the name of the browser)
- `headless`
- `locators`
- `viewport`
- `testerHtmlPath`
- `screenshotDirectory`
- `screenshotFailures`
- `provider`

Under the hood, Vitest transforms these instances into separate [test projects](https://vitest.dev/api/advanced/test-project) sharing a single Vite server for better caching performance.
