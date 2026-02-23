---
title: 'Guides: Package Bundling'
description: 'Bundling is the process of combining your application code and its dependencies into optimized output files for the client and server. Smaller bundles...'
---

# Guides: Package Bundling | Next.js

Source URL: https://nextjs.org/docs/app/guides/package-bundling

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Package Bundling

Copy page

# Optimizing package bundling

Last updated February 20, 2026

Bundling is the process of combining your application code and its dependencies into optimized output files for the client and server. Smaller bundles load faster, reduce JavaScript execution time, improve [Core Web Vitals](https://web.dev/articles/vitals), and lower server cold start times.

Next.js automatically optimizes bundles by code splitting, tree-shaking, and other techniques. However, there are some cases where you may need to optimize your bundles manually.

There are two tools for analyzing your application's bundles:

  * [Next.js Bundle Analyzer for Turbopack (experimental)](https://nextjs.org/docs/app/guides/package-bundling#nextjs-bundle-analyzer-experimental)
  * [`@next/bundle-analyzer` plugin for Webpack](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)



This guide will walk you through how to use each tool and how to [optimize large bundles](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles).

## Next.js Bundle Analyzer (Experimental)[](https://nextjs.org/docs/app/guides/package-bundling#nextjs-bundle-analyzer-experimental)

> Available in v16.1 and later. You can share feedback in the [dedicated GitHub discussion](https://github.com/vercel/next.js/discussions/86731) and view the demo at [turbopack-bundle-analyzer-demo.vercel.sh](https://turbopack-bundle-analyzer-demo.vercel.sh/).

The Next.js Bundle Analyzer is integrated with Turbopack's module graph. You can inspect server and client modules with precise import tracing, making it easier to find large dependencies. Open the interactive Bundle Analyzer demo to explore the module graph.

### Step 1: Run the Turbopack Bundle Analyzer[](https://nextjs.org/docs/app/guides/package-bundling#step-1-run-the-turbopack-bundle-analyzer)

To get started, run the following command and open up the interactive view in your browser.

pnpmnpmyarnbun

Terminal
[code]
    pnpm next experimental-analyze
[/code]

### Step 2: Filter and inspect modules[](https://nextjs.org/docs/app/guides/package-bundling#step-2-filter-and-inspect-modules)

Within the UI, you can filter by route, environment (client or server), and type (JavaScript, CSS, JSON), or search by file:

Next.js bundle analyzer UI walkthrough

### Step 3: Trace modules with import chains[](https://nextjs.org/docs/app/guides/package-bundling#step-3-trace-modules-with-import-chains)

The treemap shows each module as a rectangle. Where the size of the module is represented by the area of the rectangle.

Click a module to see its size, inspect its full import chain and see exactly where it’s used in your application:

Next.js Bundle Analyzer import chain view

### Step 4: Write output to disk for sharing or diffing[](https://nextjs.org/docs/app/guides/package-bundling#step-4-write-output-to-disk-for-sharing-or-diffing)

If you want to share the analysis with teammates or compare bundle sizes before/after optimizations, you can skip the interactive view and save the analysis as a static file with the `--output` flag:

pnpmnpmyarnbun

Terminal
[code]
    pnpm next experimental-analyze --output
[/code]

This command writes the output to `.next/diagnostics/analyze`. You can copy this directory elsewhere to compare results:

Terminal
[code]
    cp -r .next/diagnostics/analyze ./analyze-before-refactor
[/code]

> More options are available for the Bundle Analyzer, see Next.js CLI reference docs for the full list.

## `@next/bundle-analyzer` for Webpack[](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack)

The [`@next/bundle-analyzer`](https://www.npmjs.com/package/@next/bundle-analyzer) is a plugin that helps you manage the size of your application bundles. It generates a visual report of the size of each package and their dependencies. You can use the information to remove large dependencies, split, or [lazy-load](https://nextjs.org/docs/app/guides/lazy-loading) your code.

### Step 1: Installation[](https://nextjs.org/docs/app/guides/package-bundling#step-1-installation)

Install the plugin by running the following command:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add @next/bundle-analyzer
[/code]

Then, add the bundle analyzer's settings to your `next.config.js`.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {}
     
    const withBundleAnalyzer = require('@next/bundle-analyzer')({
      enabled: process.env.ANALYZE === 'true',
    })
     
    module.exports = withBundleAnalyzer(nextConfig)
[/code]

### Step 2: Generating a report[](https://nextjs.org/docs/app/guides/package-bundling#step-2-generating-a-report)

Run the following command to analyze your bundles:
[code] 
    ANALYZE=true npm run build
    # or
    ANALYZE=true yarn build
    # or
    ANALYZE=true pnpm build
[/code]

The report will open three new tabs in your browser, which you can inspect.

## Optimizing large bundles[](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles)

Once you've identified a large module, the solution will depend on your use case. Below are common causes and how to fix them:

### Packages with many exports[](https://nextjs.org/docs/app/guides/package-bundling#packages-with-many-exports)

If you're using a package that exports hundreds of modules (such as icon and utility libraries), you can optimize how those imports are resolved using the [`optimizePackageImports`](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) option in your `next.config.js` file. This option will only load the modules you _actually_ use, while still giving you the convenience of writing import statements with many named exports.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        optimizePackageImports: ['icon-library'],
      },
    }
     
    module.exports = nextConfig
[/code]

> **Good to know:** Next.js also optimizes some libraries automatically, thus they do not need to be included in the `optimizePackageImports` list. See the [full list](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) of supported packages.

### Heavy client workloads[](https://nextjs.org/docs/app/guides/package-bundling#heavy-client-workloads)

A common cause of large client bundles is doing expensive rendering work in Client Components. This often happens with libraries that exist only to transform data into UI, such as syntax highlighting, chart rendering, or markdown parsing.

If that work does not require browser APIs or user interaction, it can be run in a Server Component.

In this example, a prism based highlighter runs in a Client Component. Even though the final output is just a `<code>` block, the entire highlighting library is bundled into the client JavaScript bundle:

app/blog/[slug]/page.tsx
[code]
    'use client'
     
    import Highlight from 'prism-react-renderer'
    import theme from 'prism-react-renderer/themes/github'
     
    export default function Page() {
      const code = `export function hello() {
        console.log("hi")
      }`
     
      return (
        <article>
          <h1>Blog Post Title</h1>
     
          {/* The prism package and its tokenization logic are shipped to the client */}
          <Highlight code={code} language="tsx" theme={theme}>
            {({ className, style, tokens, getLineProps, getTokenProps }) => (
              <pre className={className} style={style}>
                <code>
                  {tokens.map((line, i) => (
                    <div key={i} {...getLineProps({ line })}>
                      {line.map((token, key) => (
                        <span key={key} {...getTokenProps({ token })} />
                      ))}
                    </div>
                  ))}
                </code>
              </pre>
            )}
          </Highlight>
        </article>
      )
    }
[/code]

This increases bundle size because the client must download and execute the highlighting library, even though the result is static HTML.

Instead, move the highlighting logic to a Server Component and render the final HTML on the server. The client will only receive the rendered markup.

app/blog/[slug]/page.tsx
[code]
    import { codeToHtml } from 'shiki'
     
    export default async function Page() {
      const code = `export function hello() {
        console.log("hi")
      }`
     
      // The Shiki package runs on the server and is never bundled for the client.
      const highlightedHtml = await codeToHtml(code, {
        lang: 'tsx',
        theme: 'github-dark',
      })
     
      return (
        <article>
          <h1>Blog Post Title</h1>
     
          {/* Client receives plain markup */}
          <pre>
            <code dangerouslySetInnerHTML={{ __html: highlightedHtml }} />
          </pre>
        </article>
      )
    }
[/code]

### Opting specific packages out of bundling[](https://nextjs.org/docs/app/guides/package-bundling#opting-specific-packages-out-of-bundling)

Packages imported inside Server Components and Route Handlers are automatically bundled by Next.js.

You can opt specific packages out of bundling using the [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages) option in your `next.config.js`.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      serverExternalPackages: ['package-name'],
    }
     
    module.exports = nextConfig
[/code]

## 

Learn more about optimizing your application for production.

### [ProductionRecommendations to ensure the best performance and user experience before taking your Next.js application to production.](https://nextjs.org/docs/app/guides/production-checklist)

Was this helpful?

supported.

Send
