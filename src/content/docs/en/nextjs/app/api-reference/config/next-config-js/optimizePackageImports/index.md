---
title: 'next.config.js: optimizePackageImports'
description: "This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub."
---

# next.config.js: optimizePackageImports | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)optimizePackageImports

Copy page

# optimizePackageImports

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.

Adding a package to `experimental.optimizePackageImports` will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.

next.config.js
[code]
    module.exports = {
      experimental: {
        optimizePackageImports: ['package-name'],
      },
    }
[/code]

The following libraries are optimized by default:

  * `lucide-react`
  * `date-fns`
  * `lodash-es`
  * `ramda`
  * `antd`
  * `react-bootstrap`
  * `ahooks`
  * `@ant-design/icons`
  * `@headlessui/react`
  * `@headlessui-float/react`
  * `@heroicons/react/20/solid`
  * `@heroicons/react/24/solid`
  * `@heroicons/react/24/outline`
  * `@visx/visx`
  * `@tremor/react`
  * `rxjs`
  * `@mui/material`
  * `@mui/icons-material`
  * `recharts`
  * `react-use`
  * `@material-ui/core`
  * `@material-ui/icons`
  * `@tabler/icons-react`
  * `mui-core`
  * `react-icons/*`
  * `effect`
  * `@effect/*`



Was this helpful?

supported.

Send
