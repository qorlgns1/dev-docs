---
title: 'No Cache Detected'
description: 'A Next.js build was triggered in a continuous integration environment, but no cache was detected.'
---

# No Cache Detected | Next.js

Source URL: https://nextjs.org/docs/messages/no-cache

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Cache Detected

# No Cache Detected

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-cache#why-this-error-occurred)

A Next.js build was triggered in a continuous integration environment, but no cache was detected.

This results in slower builds and can hurt Next.js' filesystem cache of client-side bundles across builds.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-cache#possible-ways-to-fix-it)

> **Note** : If this is a new project, or being built for the first time in your CI, you can ignore this error. However, you'll want to make sure it doesn't continue to happen and fix it if it does!

Follow the instructions in [CI Build Caching](https://nextjs.org/docs/pages/guides/ci-build-caching) to ensure your Next.js cache is persisted between builds.

Was this helpful?

supported.

Send
