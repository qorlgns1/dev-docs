---
title: 'Conflicting Public File and Page File'
description: 'One of your public files has the same path as a page file which is not supported. Since only one resource can reside at the URL both public files and...'
---

# Conflicting Public File and Page File | Next.js

Source URL: https://nextjs.org/docs/messages/conflicting-public-file-page

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Conflicting Public File and Page File

# Conflicting Public File and Page File

## Why This Error Occurred[](https://nextjs.org/docs/messages/conflicting-public-file-page#why-this-error-occurred)

One of your public files has the same path as a page file which is not supported. Since only one resource can reside at the URL both public files and page files must be unique.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/conflicting-public-file-page#possible-ways-to-fix-it)

Rename either the public file or page file that is causing the conflict.

Example conflict between public file and page file

Folder structure
[code]
    public/
      hello
    pages/
      hello.js
[/code]

Non-conflicting public file and page file

Folder structure
[code]
    public/
      hello.txt
    pages/
      hello.js
[/code]

## Useful Links[](https://nextjs.org/docs/messages/conflicting-public-file-page#useful-links)

  * [Static file serving docs](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder)



Was this helpful?

supported.

Send
