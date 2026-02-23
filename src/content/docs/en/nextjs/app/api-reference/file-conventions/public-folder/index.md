---
title: 'File-system conventions: public'
description: 'Last updated February 20, 2026'
---

# File-system conventions: public | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/public-folder

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)public

Copy page

# public Folder

Last updated February 20, 2026

Next.js can serve static files, like images, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

For example, the file `public/avatars/me.png` can be viewed by visiting the `/avatars/me.png` path. The code to display that image might look like:

avatar.js
[code]
    import Image from 'next/image'
     
    export function Avatar({ id, alt }) {
      return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
    }
     
    export function AvatarOfMe() {
      return <Avatar id="me" alt="A portrait of me" />
    }
[/code]

## Caching[](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder#caching)

Next.js cannot safely cache assets in the `public` folder because they may change. The default caching headers applied are:
[code] 
    Cache-Control: public, max-age=0
[/code]

## Robots, Favicons, and others[](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder#robots-favicons-and-others)

For static metadata files, such as `robots.txt`, `favicon.ico`, etc, you should use [special metadata files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata) inside the `app` folder.

Was this helpful?

supported.

Send
