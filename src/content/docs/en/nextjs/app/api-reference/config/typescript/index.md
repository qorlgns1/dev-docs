---
title: 'Configuration: TypeScript'
description: 'Last updated February 20, 2026'
---

# Configuration: TypeScript | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/typescript

[API Reference](https://nextjs.org/docs/app/api-reference)[Configuration](https://nextjs.org/docs/app/api-reference/config)TypeScript

Copy page

# TypeScript

Last updated February 20, 2026

Next.js comes with built-in TypeScript, automatically installing the necessary packages and configuring the proper settings when you create a new project with `create-next-app`.

To add TypeScript to an existing project, rename a file to `.ts` / `.tsx`. Run `next dev` and `next build` to automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

> **Good to know** : If you already have a `jsconfig.json` file, copy the `paths` compiler option from the old `jsconfig.json` into the new `tsconfig.json` file, and delete the old `jsconfig.json` file.

## IDE Plugin[](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin)

Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.

You can enable the plugin in VS Code by:

  1. Opening the command palette (`Ctrl/⌘` \+ `Shift` \+ `P`)
  2. Searching for "TypeScript: Select TypeScript Version"
  3. Selecting "Use Workspace Version"



Now, when editing files, the custom plugin will be enabled. When running `next build`, the custom type checker will be used.

The TypeScript plugin can help with:

  * Warning if invalid values for [segment config options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) are passed.
  * Showing available options and in-context documentation.
  * Ensuring the `'use client'` directive is used correctly.
  * Ensuring client hooks (like `useState`) are only used in Client Components.



> **🎥 Watch:** Learn about the built-in TypeScript plugin → [YouTube (3 minutes)](https://www.youtube.com/watch?v=pqMqn9fKEf8)

## End-to-End Type Safety[](https://nextjs.org/docs/app/api-reference/config/typescript#end-to-end-type-safety)

The Next.js App Router has **enhanced type safety**. This includes:

  1. **No serialization of data between fetching function and page** : You can `fetch` directly in components, layouts, and pages on the server. This data _does not_ need to be serialized (converted to a string) to be passed to the client side for consumption in React. Instead, since `app` uses Server Components by default, we can use values like `Date`, `Map`, `Set`, and more without any extra steps. Previously, you needed to manually type the boundary between server and client with Next.js-specific types.
  2. **Streamlined data flow between components** : With the removal of `_app` in favor of root layouts, it is now easier to visualize the data flow between components and pages. Previously, data flowing between individual `pages` and `_app` were difficult to type and could introduce confusing bugs. With [colocated data fetching](https://nextjs.org/docs/app/getting-started/fetching-data) in the App Router, this is no longer an issue.



[Data Fetching in Next.js](https://nextjs.org/docs/app/getting-started/fetching-data) now provides as close to end-to-end type safety as possible without being prescriptive about your database or content provider selection.

We're able to type the response data as you would expect with normal TypeScript. For example:

app/page.tsx

JavaScriptTypeScript
[code]
    async function getData() {
      const res = await fetch('https://api.example.com/...')
      // The return value is *not* serialized
      // You can return Date, Map, Set, etc.
      return res.json()
    }
     
    export default async function Page() {
      const name = await getData()
     
      return '...'
    }
[/code]

For _complete_ end-to-end type safety, this also requires your database or content provider to support TypeScript. This could be through using an [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) or type-safe query builder.

## Route-Aware Type Helpers[](https://nextjs.org/docs/app/api-reference/config/typescript#route-aware-type-helpers)

Next.js generates global helpers for App Router route types. These are available without imports and are generated during `next dev`, `next build`, or via [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options):

  * [`PageProps`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)
  * [`LayoutProps`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)
  * [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)



## `next-env.d.ts`[](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts)

Next.js generates a `next-env.d.ts` file in your project root. This file references Next.js type definitions, allowing TypeScript to recognize non-code imports (images, stylesheets, etc.) and Next.js-specific types.

Running `next dev`, `next build`, or [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options) regenerates this file.

> **Good to know** :
> 
>   * We recommend adding `next-env.d.ts` to your `.gitignore` file.
>   * The file must be in your `tsconfig.json` `include` array (`create-next-app` does this automatically).
> 


## Examples[](https://nextjs.org/docs/app/api-reference/config/typescript#examples)

### Type Checking Next.js Configuration Files[](https://nextjs.org/docs/app/api-reference/config/typescript#type-checking-nextjs-configuration-files)

You can use TypeScript and import types in your Next.js configuration by using `next.config.ts`.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      /* config options here */
    }
     
    export default nextConfig
[/code]

Module resolution in `next.config.ts` is currently limited to CommonJS. However, ECMAScript Modules (ESM) syntax is available when [using Node.js native TypeScript resolver](https://nextjs.org/docs/app/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts) for Node.js v22.10.0 and higher.

When using the `next.config.js` file, you can add some type checking in your IDE using JSDoc as below:

next.config.js
[code]
    // @ts-check
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }
     
    module.exports = nextConfig
[/code]

### Using Node.js Native TypeScript Resolver for `next.config.ts`[](https://nextjs.org/docs/app/api-reference/config/typescript#using-nodejs-native-typescript-resolver-for-nextconfigts)

> **Note** : Available on Node.js v22.10.0+ and only when the feature is enabled. Next.js does not enable it.

Next.js detects the [Node.js native TypeScript resolver](https://nodejs.org/api/typescript.html) via [`process.features.typescript`](https://nodejs.org/api/process.html#processfeaturestypescript), added in **v22.10.0**. When present, `next.config.ts` can use native ESM, including top‑level `await` and dynamic `import()`. This mechanism inherits the capabilities and limitations of Node's resolver.

In Node.js versions **v22.18.0+** , `process.features.typescript` is enabled by default. For versions between **v22.10.0** and **22.17.x** , opt in with `NODE_OPTIONS=--experimental-transform-types`:

Terminal
[code]
    NODE_OPTIONS=--experimental-transform-types next <command>
[/code]

#### For CommonJS Projects (Default)[](https://nextjs.org/docs/app/api-reference/config/typescript#for-commonjs-projects-default)

Although `next.config.ts` supports native ESM syntax in CommonJS projects, Node.js will still assume `next.config.ts` is a CommonJS file by default, resulting in Node.js reparsing the file as ESM when module syntax is detected. Therefore, we recommend using the `next.config.mts` file for CommonJS projects to explicitly indicate it's an ESM module:

next.config.mts
[code]
    import type { NextConfig } from 'next'
     
    // Top-level await and dynamic import are supported
    const flags = await import('./flags.js').then((m) => m.default ?? m)
     
    const nextConfig: NextConfig = {
      /* config options here */
      typedRoutes: Boolean(flags?.typedRoutes),
    }
     
    export default nextConfig
[/code]

#### For ESM Projects[](https://nextjs.org/docs/app/api-reference/config/typescript#for-esm-projects)

When `"type"` is set to `"module"` in `package.json`, your project uses ESM. Learn more about this setting [in the Node.js docs](https://nodejs.org/api/packages.html#type). In this case, you can write `next.config.ts` directly with ESM syntax.

> **Good to know** : When using `"type": "module"` in your `package.json`, all `.js` and `.ts` files in your project are treated as ESM modules by default. You may need to rename files with CommonJS syntax to `.cjs` or `.cts` extensions if needed.

### Statically Typed Links[](https://nextjs.org/docs/app/api-reference/config/typescript#statically-typed-links)

Next.js can statically type links to prevent typos and other errors when using `next/link`, improving type safety when navigating between pages.

Works in both the Pages and App Router for the `href` prop in `next/link`. In the App Router, it also types `next/navigation` methods like `push`, `replace`, and `prefetch`. It does not type `next/router` methods in Pages Router.

Literal `href` strings are validated, while non-literal `href`s may require a cast with `as Route`.

To opt-into this feature, `typedRoutes` needs to be enabled and the project needs to be using TypeScript.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      typedRoutes: true,
    }
     
    export default nextConfig
[/code]

Next.js will generate a link definition in `.next/types` that contains information about all existing routes in your application, which TypeScript can then use to provide feedback in your editor about invalid links.

> **Good to know** : If you set up your project without `create-next-app`, ensure the generated Next.js types are included by adding `.next/types/**/*.ts` to the `include` array in your `tsconfig.json`:

tsconfig.json
[code]
    {
      "include": [
        "next-env.d.ts",
        ".next/types/**/*.ts",
        "**/*.ts",
        "**/*.tsx"
      ],
      "exclude": ["node_modules"]
    }
[/code]

Currently, support includes any string literal, including dynamic segments. For non-literal strings, you need to manually cast with `as Route`. The example below shows both `next/link` and `next/navigation` usage:

app/example-client.tsx
[code]
    'use client'
     
    import type { Route } from 'next'
    import Link from 'next/link'
    import { useRouter } from 'next/navigation'
     
    export default function Example() {
      const router = useRouter()
      const slug = 'nextjs'
     
      return (
        <>
          {/* Link: literal and dynamic */}
          <Link href="/about" />
          <Link href={`/blog/${slug}`} />
          <Link href={('/blog/' + slug) as Route} />
          {/* TypeScript error if href is not a valid route */}
          <Link href="/aboot" />
     
          {/* Router: literal and dynamic strings are validated */}
          <button onClick={() => router.push('/about')}>Push About</button>
          <button onClick={() => router.replace(`/blog/${slug}`)}>
            Replace Blog
          </button>
          <button onClick={() => router.prefetch('/contact')}>
            Prefetch Contact
          </button>
     
          {/* For non-literal strings, cast to Route */}
          <button onClick={() => router.push(('/blog/' + slug) as Route)}>
            Push Non-literal Blog
          </button>
        </>
      )
    }
[/code]

The same applies for redirecting routes defined by proxy:

proxy.ts
[code]
    import { NextRequest, NextResponse } from 'next/server'
     
    export function proxy(request: NextRequest) {
      if (request.nextUrl.pathname === '/proxy-redirect') {
        return NextResponse.redirect(new URL('/', request.url))
      }
     
      return NextResponse.next()
    }
[/code]

app/some/page.tsx
[code]
    import type { Route } from 'next'
     
    export default function Page() {
      return <Link href={'/proxy-redirect' as Route}>Link Text</Link>
    }
[/code]

To accept `href` in a custom component wrapping `next/link`, use a generic:
[code] 
    import type { Route } from 'next'
    import Link from 'next/link'
     
    function Card<T extends string>({ href }: { href: Route<T> | URL }) {
      return (
        <Link href={href}>
          <div>My Card</div>
        </Link>
      )
    }
[/code]

You can also type a simple data structure and iterate to render links:

components/nav-items.ts
[code]
    import type { Route } from 'next'
     
    type NavItem<T extends string = string> = {
      href: T
      label: string
    }
     
    export const navItems: NavItem<Route>[] = [
      { href: '/', label: 'Home' },
      { href: '/about', label: 'About' },
      { href: '/blog', label: 'Blog' },
    ]
[/code]

Then, map over the items to render `Link`s:

components/nav.tsx
[code]
    import Link from 'next/link'
    import { navItems } from './nav-items'
     
    export function Nav() {
      return (
        <nav>
          {navItems.map((item) => (
            <Link key={item.href} href={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>
      )
    }
[/code]

> **How does it work?**
> 
> When running `next dev` or `next build`, Next.js generates a hidden `.d.ts` file inside `.next` that contains information about all existing routes in your application (all valid routes as the `href` type of `Link`). This `.d.ts` file is included in `tsconfig.json` and the TypeScript compiler will check that `.d.ts` and provide feedback in your editor about invalid links.

### Type IntelliSense for Environment Variables[](https://nextjs.org/docs/app/api-reference/config/typescript#type-intellisense-for-environment-variables)

During development, Next.js generates a `.d.ts` file in `.next/types` that contains information about the loaded environment variables for your editor's IntelliSense. If the same environment variable key is defined in multiple files, it is deduplicated according to the [Environment Variable Load Order](https://nextjs.org/docs/app/guides/environment-variables#environment-variable-load-order).

To opt-into this feature, `experimental.typedEnv` needs to be enabled and the project needs to be using TypeScript.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        typedEnv: true,
      },
    }
     
    export default nextConfig
[/code]

> **Good to know** : Types are generated based on the environment variables loaded at development runtime, which excludes variables from `.env.production*` files by default. To include production-specific variables, run `next dev` with `NODE_ENV=production`.

### With Async Server Components[](https://nextjs.org/docs/app/api-reference/config/typescript#with-async-server-components)

To use an `async` Server Component with TypeScript, ensure you are using TypeScript `5.1.3` or higher and `@types/react` `18.2.8` or higher.

If you are using an older version of TypeScript, you may see a `'Promise<Element>' is not a valid JSX element` type error. Updating to the latest version of TypeScript and `@types/react` should resolve this issue.

### Incremental type checking[](https://nextjs.org/docs/app/api-reference/config/typescript#incremental-type-checking)

Since `v10.2.1` Next.js supports [incremental type checking](https://www.typescriptlang.org/tsconfig#incremental) when enabled in your `tsconfig.json`, this can help speed up type checking in larger applications.

### Custom `tsconfig` path[](https://nextjs.org/docs/app/api-reference/config/typescript#custom-tsconfig-path)

In some cases, you might want to use a different TypeScript configuration for builds or tooling. To do that, set `typescript.tsconfigPath` in `next.config.ts` to point Next.js to another `tsconfig` file.

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }
     
    export default nextConfig
[/code]

For example, switch to a different config for production builds:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const isProd = process.env.NODE_ENV === 'production'
     
    const nextConfig: NextConfig = {
      typescript: {
        tsconfigPath: isProd ? 'tsconfig.build.json' : 'tsconfig.json',
      },
    }
     
    export default nextConfig
[/code]

Why you might use a separate `tsconfig` for builds

You might need to relax checks in scenarios like monorepos, where the build also validates shared dependencies that don't match your project's standards, or when loosening checks in CI to continue delivering while migrating locally to stricter TypeScript settings (and still wanting your IDE to highlight misuse).

For example, if your project uses `useUnknownInCatchVariables` but some monorepo dependencies still assume `any`:

tsconfig.build.json
[code]
    {
      "extends": "./tsconfig.json",
      "compilerOptions": {
        "useUnknownInCatchVariables": false
      }
    }
[/code]

This keeps your editor strict via `tsconfig.json` while allowing the production build to use relaxed settings.

> **Good to know** :
> 
>   * IDEs typically read `tsconfig.json` for diagnostics and IntelliSense, so you can still see IDE warnings while production builds use the alternate config. Mirror critical options if you want parity in the editor.
>   * In development, only `tsconfig.json` is watched for changes. If you edit a different file name via `typescript.tsconfigPath`, restart the dev server to apply changes.
>   * The configured file is used in `next dev`, `next build`, and `next typegen`.
> 


### Disabling TypeScript errors in production[](https://nextjs.org/docs/app/api-reference/config/typescript#disabling-typescript-errors-in-production)

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

Open `next.config.ts` and enable the `ignoreBuildErrors` option in the [`typescript`](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript) config:

next.config.ts
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
     
    export default nextConfig
[/code]

> **Good to know** : You can run `tsc --noEmit` to check for TypeScript errors yourself before building. This is useful for CI/CD pipelines where you'd like to check for TypeScript errors before deploying.

### Custom type declarations[](https://nextjs.org/docs/app/api-reference/config/typescript#custom-type-declarations)

When you need to declare custom types, you might be tempted to modify `next-env.d.ts`. However, this file is automatically generated, so any changes you make will be overwritten. Instead, you should create a new file, let's call it `new-types.d.ts`, and reference it in your `tsconfig.json`:

tsconfig.json
[code]
    {
      "compilerOptions": {
        "skipLibCheck": true
        //...truncated...
      },
      "include": [
        "new-types.d.ts",
        "next-env.d.ts",
        ".next/types/**/*.ts",
        "**/*.ts",
        "**/*.tsx"
      ],
      "exclude": ["node_modules"]
    }
[/code]

## Version Changes[](https://nextjs.org/docs/app/api-reference/config/typescript#version-changes)

Version| Changes  
---|---  
`v15.0.0`| [`next.config.ts`](https://nextjs.org/docs/app/api-reference/config/typescript#type-checking-nextjs-configuration-files) support added for TypeScript projects.  
`v13.2.0`| Statically typed links are available in beta.  
`v12.0.0`| [SWC](https://nextjs.org/docs/architecture/nextjs-compiler) is now used by default to compile TypeScript and TSX for faster builds.  
`v10.2.1`| [Incremental type checking](https://www.typescriptlang.org/tsconfig#incremental) support added when enabled in your `tsconfig.json`.  
  
Was this helpful?

supported.

Send
