---
title: "outputFile {#outputfile}"
description: "Write test results to a file when the ,  or  option is also specified."
---

Source URL: https://vitest.dev/config/outputfile

# outputFile {#outputfile}

- **Type:** `string | Record<string, string>`
- **CLI:** `--outputFile=<path>`, `--outputFile.json=./path`

Write test results to a file when the `--reporter=json`, `--reporter=html` or `--reporter=junit` option is also specified.
By providing an object instead of a string you can define individual outputs when using multiple reporters.
