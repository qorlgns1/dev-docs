---
title: 'next.config.js Options: distDir'
description: 'Last updated February 20, 2026'
---

# next.config.js Options: distDir | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)distDir

Copy page

# distDir

Last updated February 20, 2026

You can specify a name to use for a custom build directory to use instead of `.next`.

Open `next.config.js` and add the `distDir` config:

next.config.js
[code]
    module.exports = {
      distDir: 'build',
    }
[/code]

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.

> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.

Was this helpful?

supported.

Send
