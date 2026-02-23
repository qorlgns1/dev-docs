---
title: 'next.config.js Options: pageExtensions'
description: 'You can extend the default Page extensions (, , , ) used by Next.js. Inside , add the  config:'
---

# next.config.js Options: pageExtensions | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)pageExtensions

Copy page

# pageExtensions

Last updated February 20, 2026

You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

next.config.js
[code]
    module.exports = {
      pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
    }
[/code]

Changing these values affects _all_ Next.js pages, including the following:

  * [`proxy.js`](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
  * [`instrumentation.js`](https://nextjs.org/docs/pages/guides/instrumentation)
  * `pages/_document.js`
  * `pages/_app.js`
  * `pages/api/`



For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.

## Including non-page files in the `pages` directory[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions#including-non-page-files-in-the-pages-directory)

You can colocate test files or other files used by components in the `pages` directory. Inside `next.config.js`, add the `pageExtensions` config:

next.config.js
[code]
    module.exports = {
      pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
    }
[/code]

Then, rename your pages to have a file extension that includes `.page` (e.g. rename `MyPage.tsx` to `MyPage.page.tsx`). Ensure you rename _all_ Next.js pages, including the files mentioned above.

Was this helpful?

supported.

Send
