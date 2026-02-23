---
title: 'next.config.js Options: typescript'
description: 'Configure TypeScript behavior with the  option in :'
---

# next.config.js Options: typescript | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)typescript

Copy page

# typescript

Last updated February 20, 2026

Configure TypeScript behavior with the `typescript` option in `next.config.js`:

next.config.js
[code]
    module.exports = {
      typescript: {
        ignoreBuildErrors: false,
        tsconfigPath: 'tsconfig.json',
      },
    }
[/code]

## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#options)

Option| Type| Default| Description  
---|---|---|---  
`ignoreBuildErrors`| `boolean`| `false`| Allow production builds to complete even with TypeScript errors.  
`tsconfigPath`| `string`| `'tsconfig.json'`| Path to a custom `tsconfig.json` file.  
  
## `ignoreBuildErrors`[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#ignorebuilderrors)

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

next.config.js
[code]
    module.exports = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
[/code]

## `tsconfigPath`[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#tsconfigpath)

Use a different TypeScript configuration file for builds or tooling:

next.config.js
[code]
    module.exports = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }
[/code]

See the [TypeScript configuration](https://nextjs.org/docs/app/api-reference/config/typescript#custom-tsconfig-path) page for more details.

Was this helpful?

supported.

Send
