---
title: 'Getting Started: Upgrading'
description: 'To update to the latest version of Next.js, you can use the  command:'
---

# Getting Started: Upgrading | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/upgrading

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Upgrading

Copy page

# Upgrading

Last updated February 20, 2026

## Latest version[](https://nextjs.org/docs/app/getting-started/upgrading#latest-version)

To update to the latest version of Next.js, you can use the `upgrade` command:

pnpmnpmyarnbun

Terminal
[code]
    pnpm next upgrade
[/code]

Next.js 15 and earlier do not support the `upgrade` command and need to use a separate package instead:

Terminal
[code]
    npx @next/codemod@canary upgrade latest
[/code]

If you prefer to upgrade manually, install the latest Next.js and React versions:

pnpmnpmyarnbun

Terminal
[code]
    pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
[/code]

## Canary version[](https://nextjs.org/docs/app/getting-started/upgrading#canary-version)

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add next@canary
[/code]

### Features available in canary[](https://nextjs.org/docs/app/getting-started/upgrading#features-available-in-canary)

The following features are currently available in canary:

**Authentication** :

  * [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden)
  * [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
  * [`forbidden.js`](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
  * [`unauthorized.js`](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
  * [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)



## Version guides

See the version guides for in-depth upgrade instructions.

### [Version 16Upgrade your Next.js Application from Version 15 to 16.](https://nextjs.org/docs/app/guides/upgrading/version-16)### [Version 15Upgrade your Next.js Application from Version 14 to 15.](https://nextjs.org/docs/app/guides/upgrading/version-15)### [Version 14Upgrade your Next.js Application from Version 13 to 14.](https://nextjs.org/docs/app/guides/upgrading/version-14)

Was this helpful?

supported.

Send
