---
title: 'Routing'
description: 'integrates with Next.js’ routing system in two places:'
---

Source URL: https://next-intl.dev/docs/routing

[Docs](https://next-intl.dev/docs/getting-started "Docs")Routing

# Routing

`next-intl` integrates with Next.js’ routing system in two places:

  1. **Proxy / middleware** : Negotiates the locale and handles redirects & rewrites (e.g. `/` → `/en`)
  2. **Navigation APIs** : Lightweight wrappers around Next.js’ navigation APIs like `<Link />`

This enables you to express your app in terms of APIs like `<Link href="/about">`, while aspects like the locale and user-facing pathnames are automatically handled behind the scenes (e.g. `/de/über-uns`).

[Set up routing→](https://next-intl.dev/docs/routing/setup)[Configuration→](https://next-intl.dev/docs/routing/configuration)[Proxy / middleware→](https://next-intl.dev/docs/routing/middleware)[Navigation APIs→](https://next-intl.dev/docs/routing/navigation)

Prefer to watch a video?

[Locale-based routing](https://learn.next-intl.dev/chapters/06-routing/01-setup)

