---
title: 'No HTML link for pages'
description: '> Prevent usage of  elements to navigate to internal Next.js pages.'
---

# No HTML link for pages | Next.js

Source URL: https://nextjs.org/docs/messages/no-html-link-for-pages

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No HTML link for pages

# No HTML link for pages

> Prevent usage of `<a>` elements to navigate to internal Next.js pages.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-html-link-for-pages#why-this-error-occurred)

An `<a>` element was used to navigate to a page route without using the `next/link` component, causing unnecessary full-page refreshes.

The `Link` component is required to enable client-side route transitions between pages and provide a single-page app experience.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-html-link-for-pages#possible-ways-to-fix-it)

Make sure to import the `Link` component and wrap anchor elements that route to different page routes.

**Before:**

pages/index.js
[code]
    function Home() {
      return (
        <div>
          <a href="/about">About Us</a>
        </div>
      )
    }
[/code]

**After:**

pages/index.js
[code]
    import Link from 'next/link'
     
    function Home() {
      return (
        <div>
          <Link href="/about">About Us</Link>
        </div>
      )
    }
     
    export default Home
[/code]

### Options[](https://nextjs.org/docs/messages/no-html-link-for-pages#options)

#### `pagesDir`[](https://nextjs.org/docs/messages/no-html-link-for-pages#pagesdir)

This rule can normally locate your `pages` directory automatically.

If you're working in a monorepo, we recommend configuring the [`rootDir`](https://nextjs.org/docs/pages/api-reference/config/eslint#specifying-a-root-directory-within-a-monorepo) setting in `eslint-plugin-next`, which `pagesDir` will use to locate your `pages` directory.

In some cases, you may also need to configure this rule directly by providing a `pages` directory. This can be a path or an array of paths.

eslint.config.json
[code]
    {
      "rules": {
        "@next/next/no-html-link-for-pages": ["error", "packages/my-app/pages/"]
      }
    }
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-html-link-for-pages#useful-links)

  * [next/link API Reference](https://nextjs.org/docs/pages/api-reference/components/link)



Was this helpful?

supported.

Send
