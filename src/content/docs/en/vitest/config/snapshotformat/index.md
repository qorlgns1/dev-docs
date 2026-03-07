---
title: "snapshotFormat"
description: "Format options for snapshot testing. These options are passed down to our fork of . In addition to the  options we support ."
---

Source URL: https://vitest.dev/config/snapshotformat

# snapshotFormat

- **Type:** `PrettyFormatOptions`

Format options for snapshot testing. These options are passed down to our fork of [`pretty-format`](https://www.npmjs.com/package/pretty-format). In addition to the `pretty-format` options we support `printShadowRoot: boolean`.

::: tip
Beware that `plugins` field on this object will be ignored.

If you need to extend snapshot serializer via pretty-format plugins, please, use [`expect.addSnapshotSerializer`](https://vitest.dev/api/expect#expect-addsnapshotserializer) API or [snapshotSerializers](#snapshotserializers) option.
:::
