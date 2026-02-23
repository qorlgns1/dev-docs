---
title: 'No assign module variable'
description: '> Prevent assignment to the  variable.'
---

# No assign module variable | Next.js

Source URL: https://nextjs.org/docs/messages/no-assign-module-variable

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No assign module variable

# No assign module variable

> Prevent assignment to the `module` variable.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-assign-module-variable#why-this-error-occurred)

A value is being assigned to the `module` variable. The `module` variable is already used and it is highly likely that assigning to this variable will cause errors.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-assign-module-variable#possible-ways-to-fix-it)

Use a different variable name:

example.js
[code]
    let myModule = {...}
[/code]

Was this helpful?

supported.

Send
