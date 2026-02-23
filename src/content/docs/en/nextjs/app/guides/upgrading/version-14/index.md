---
title: 'Upgrading: Version 14'
description: 'Last updated February 20, 2026'
---

# Upgrading: Version 14 | Next.js

Source URL: https://nextjs.org/docs/app/guides/upgrading/version-14

[Guides](https://nextjs.org/docs/app/guides)[Upgrading](https://nextjs.org/docs/app/guides/upgrading)Version 14

Copy page

# How to upgrade to version 14

Last updated February 20, 2026

## Upgrading from 13 to 14[](https://nextjs.org/docs/app/guides/upgrading/version-14#upgrading-from-13-to-14)

To update to Next.js version 14, run the following command using your preferred package manager:

Terminal
[code]
    npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
[/code]

Terminal
[code]
    yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
[/code]

Terminal
[code]
    pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
[/code]

Terminal
[code]
    bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
[/code]

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

### v14 Summary[](https://nextjs.org/docs/app/guides/upgrading/version-14#v14-summary)

  * The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life.
  * The `next export` command has been removed in favor of `output: 'export'` config. Please see the [docs](https://nextjs.org/docs/app/guides/static-exports) for more information.
  * The `next/server` import for `ImageResponse` was renamed to `next/og`. A [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#next-og-import) to safely and automatically rename your imports.
  * The `@next/font` package has been fully removed in favor of the built-in `next/font`. A [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font) to safely and automatically rename your imports.
  * The WASM target for `next-swc` has been removed.



Was this helpful?

supported.

Send
