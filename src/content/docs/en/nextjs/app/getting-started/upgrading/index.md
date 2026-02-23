---
title: 'Upgrading'
description: 'To update to the latest version of Next.js, you can use the  command:'
---

Source URL: https://nextjs.org/docs/app/getting-started/upgrading

# Upgrading

## Latest version

To update to the latest version of Next.js, you can use the `upgrade` command:

```bash package="pnpm"
pnpm next upgrade
```

```bash package="npm"
npx next upgrade
```

```bash package="yarn"
yarn next upgrade
```

```bash package="bun"
bunx next upgrade
```

Next.js 15 and earlier do not support the `upgrade` command and need to use a separate package instead:

```bash filename="Terminal"
npx @next/codemod@canary upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest eslint-config-next@latest
```

## Canary version

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

```bash package="pnpm"
pnpm add next@canary
```

```bash package="npm"
npm i next@canary
```

```bash package="yarn"
yarn add next@canary
```

```bash package="bun"
bun add next@canary
```

### Features available in canary

The following features are currently available in canary:

**Authentication**:

* [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden)
* [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
* [`forbidden.js`](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
* [`unauthorized.js`](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
* [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
## Version guides

See the version guides for in-depth upgrade instructions.

- [Version 16](https://nextjs.org/docs/app/guides/upgrading/version-16)
  - Upgrade your Next.js Application from Version 15 to 16.
- [Version 15](https://nextjs.org/docs/app/guides/upgrading/version-15)
  - Upgrade your Next.js Application from Version 14 to 15.
- [Version 14](https://nextjs.org/docs/app/guides/upgrading/version-14)
  - Upgrade your Next.js Application from Version 13 to 14.

---

