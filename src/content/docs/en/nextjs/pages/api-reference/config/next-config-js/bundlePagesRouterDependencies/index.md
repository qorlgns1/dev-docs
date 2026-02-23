---
title: 'bundlePagesRouterDependencies'
description: 'Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.'
---

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies

# bundlePagesRouterDependencies

Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages) option.

## Version History

| Version   | Changes                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------- |
| `v15.0.0` | Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies` |
---
