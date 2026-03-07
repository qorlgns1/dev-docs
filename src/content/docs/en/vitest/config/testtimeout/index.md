---
title: "testTimeout"
description: "Default timeout of a test in milliseconds. Use  to disable timeout completely."
---

Source URL: https://vitest.dev/config/testtimeout

# testTimeout

- **Type:** `number`
- **Default:** `5_000` in Node.js, `15_000` if `browser.enabled` is `true`
- **CLI:** `--test-timeout=5000`, `--testTimeout=5000`

Default timeout of a test in milliseconds. Use `0` to disable timeout completely.
