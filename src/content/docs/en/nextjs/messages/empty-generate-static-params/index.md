---
title: 'Empty generateStaticParams with Cache Components'
description: "You're using Cache Components in your Next.js application, and one of your  functions returned an empty array, which causes a build error."
---

# Empty generateStaticParams with Cache Components | Next.js

Source URL: https://nextjs.org/docs/messages/empty-generate-static-params

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Empty generateStaticParams with Cache Components

# Empty generateStaticParams with Cache Components

## Why This Error Occurred[](https://nextjs.org/docs/messages/empty-generate-static-params#why-this-error-occurred)

You're using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) in your Next.js application, and one of your `generateStaticParams` functions returned an empty array, which causes a build error.

When Cache Components is enabled, Next.js performs build-time validation to ensure your routes can be properly prerendered without runtime dynamic access errors. If `generateStaticParams` returns an empty array, Next.js cannot validate that your route won't access dynamic values (like `await cookies()`, `await headers()`, or `await searchParams`) at runtime, which would cause errors.

This strict requirement ensures:

  * Build-time validation catches potential runtime errors early
  * All routes using Cache Components have at least one static variant to validate against
  * You don't accidentally deploy routes that will fail at runtime



## Possible Ways to Fix It[](https://nextjs.org/docs/messages/empty-generate-static-params#possible-ways-to-fix-it)

### Option 1: Return at least one static param[](https://nextjs.org/docs/messages/empty-generate-static-params#option-1-return-at-least-one-static-param)

Modify your `generateStaticParams` function to return at least one set of parameters. This is the most common fix and allows build-time validation to work properly.

app/blog/[slug]/page.tsx
[code]
    // This will cause an error with Cache Components
    export async function generateStaticParams() {
      return [] // Empty array not allowed
    }
     
    // Return at least one sample param
    export async function generateStaticParams() {
      return [{ slug: 'hello-world' }, { slug: 'getting-started' }]
    }
[/code]

These samples serve dual purposes:

  1. **Build-time validation** : Verify your route structure is safe
  2. **Prerendering** : Generate instant-loading pages for popular routes



The build process only validates code paths that execute with your sample params. If runtime parameters trigger conditional logic that renders branches accessing runtime APIs (like `cookies()`) without Suspense, or dynamic content without Suspense or `use cache`, those will cause runtime errors.

### Option 2: Use a placeholder param[](https://nextjs.org/docs/messages/empty-generate-static-params#option-2-use-a-placeholder-param)

If you don't know actual values at build time, you can use a placeholder for validation. However, this defeats the purpose of build-time validation and should be avoided:

app/blog/[slug]/page.tsx
[code]
    export async function generateStaticParams() {
      // Placeholder only validates one code path
      return [{ slug: '__placeholder__' }]
    }
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
     
      // Handle placeholder case
      if (slug === '__placeholder__') {
        notFound()
      }
     
      // Real params may trigger code paths
      // that access dynamic APIs incorrectly, causing
      // runtime errors that cannot be caught by error boundaries
      const post = await getPost(slug)
      return <div>{post.title}</div>
    }
[/code]

Using placeholders provides minimal build-time validation and increases the risk of runtime errors for actual parameter values.

## Useful Links[](https://nextjs.org/docs/messages/empty-generate-static-params#useful-links)

  * [Cache Components Documentation](https://nextjs.org/docs/app/getting-started/cache-components)
  * [generateStaticParams API Reference](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
  * [Dynamic Routes with Cache Components](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)



Was this helpful?

supported.

Send
