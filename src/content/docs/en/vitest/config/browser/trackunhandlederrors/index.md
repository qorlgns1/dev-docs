---
title: "browser.trackUnhandledErrors"
description: "Enables tracking uncaught errors and exceptions so they can be reported by Vitest."
---

Source URL: https://vitest.dev/config/browser/trackunhandlederrors

# browser.trackUnhandledErrors

- **Type:** `boolean`
- **Default:** `true`

Enables tracking uncaught errors and exceptions so they can be reported by Vitest.

If you need to hide certain errors, it is recommended to use [`onUnhandledError`](https://vitest.dev/config/#onunhandlederror) option instead.

Disabling this will completely remove all Vitest error handlers, which can help debugging with the "Pause on exceptions" checkbox turned on.
