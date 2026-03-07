---
title: "hookTimeout"
description: "Default timeout of a hook in milliseconds. Use  to disable timeout completely."
---

Source URL: https://vitest.dev/config/hooktimeout

# hookTimeout

- **Type:** `number`
- **Default:** `10_000` in Node.js, `30_000` if `browser.enabled` is `true`
- **CLI:** `--hook-timeout=10000`, `--hookTimeout=10000`

Default timeout of a hook in milliseconds. Use `0` to disable timeout completely.
