---
title: 'Metadata Files: manifest.json'
description: 'Add or generate a  file that matches the Web Manifest Specification in the root of  directory to provide information about your web application for th...'
---

# Metadata Files: manifest.json | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest

[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)[Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)manifest.json

Copy page

# manifest.json

Last updated February 20, 2026

Add or generate a `manifest.(json|webmanifest)` file that matches the [Web Manifest Specification](https://developer.mozilla.org/docs/Web/Manifest) in the **root** of `app` directory to provide information about your web application for the browser.

## Static Manifest file[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#static-manifest-file)

app/manifest.json | app/manifest.webmanifest
[code]
    {
      "name": "My Next.js Application",
      "short_name": "Next.js App",
      "description": "An application built with Next.js",
      "start_url": "/"
      // ...
    }
[/code]

## Generate a Manifest file[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#generate-a-manifest-file)

Add a `manifest.js` or `manifest.ts` file that returns a [`Manifest` object](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object).

> Good to know: `manifest.js` is special Route Handlers that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.

app/manifest.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function manifest(): MetadataRoute.Manifest {
      return {
        name: 'Next.js App',
        short_name: 'Next.js App',
        description: 'Next.js App',
        start_url: '/',
        display: 'standalone',
        background_color: '#fff',
        theme_color: '#fff',
        icons: [
          {
            src: '/favicon.ico',
            sizes: 'any',
            type: 'image/x-icon',
          },
        ],
      }
    }
[/code]

### Manifest Object[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object)

The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin) or see the [MDN](https://developer.mozilla.org/docs/Web/Manifest) docs.

Was this helpful?

supported.

Send
