---
title: 'Guides: Content Security Policy'
description: 'Last updated February 20, 2026'
---

# Guides: Content Security Policy | Next.js

Source URL: https://nextjs.org/docs/app/guides/content-security-policy

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Content Security Policy

Copy page

# How to set a Content Security Policy (CSP) for your Next.js application

Last updated February 20, 2026

[Content Security Policy (CSP)](https://developer.mozilla.org/docs/Web/HTTP/CSP) is important to guard your Next.js application against various security threats such as cross-site scripting (XSS), clickjacking, and other code injection attacks.

By using CSP, developers can specify which origins are permissible for content sources, scripts, stylesheets, images, fonts, objects, media (audio, video), iframes, and more.

Examples

  * [Strict CSP](https://github.com/vercel/next.js/tree/canary/examples/with-strict-csp)



## Nonces[](https://nextjs.org/docs/app/guides/content-security-policy#nonces)

A [nonce](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce) is a unique, random string of characters created for a one-time use. It is used in conjunction with CSP to selectively allow certain inline scripts or styles to execute, bypassing strict CSP directives.

### Why use a nonce?[](https://nextjs.org/docs/app/guides/content-security-policy#why-use-a-nonce)

CSP can block both inline and external scripts to prevent attacks. A nonce lets you safely allow specific scripts to run—only if they include the matching nonce value.

If an attacker wanted to load a script into your page, they'd need to guess the nonce value. That's why the nonce must be unpredictable and unique for every request.

### Adding a nonce with Proxy[](https://nextjs.org/docs/app/guides/content-security-policy#adding-a-nonce-with-proxy)

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) enables you to add headers and generate nonces before the page renders.

Every time a page is viewed, a fresh nonce should be generated. This means that you **must use[dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) to add nonces**.

For example:

> **Good to know** : In development, `'unsafe-eval'` is required because React uses `eval` to provide enhanced debugging information, such as reconstructing server-side error stacks in the browser. `unsafe-eval` is not required for production. Neither React nor Next.js use `eval` in production by default.

proxy.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'
     
    export function proxy(request: NextRequest) {
      const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
      const isDev = process.env.NODE_ENV === 'development'
      const cspHeader = `
        default-src 'self';
        script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self' 'nonce-${nonce}';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `
      // Replace newline characters and spaces
      const contentSecurityPolicyHeaderValue = cspHeader
        .replace(/\s{2,}/g, ' ')
        .trim()
     
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('x-nonce', nonce)
     
      requestHeaders.set(
        'Content-Security-Policy',
        contentSecurityPolicyHeaderValue
      )
     
      const response = NextResponse.next({
        request: {
          headers: requestHeaders,
        },
      })
      response.headers.set(
        'Content-Security-Policy',
        contentSecurityPolicyHeaderValue
      )
     
      return response
    }
[/code]

By default, Proxy runs on all requests. You can filter Proxy to run on specific paths using a [`matcher`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher).

We recommend ignoring matching prefetches (from `next/link`) and static assets that don't need the CSP header.

proxy.ts

JavaScriptTypeScript
[code]
    export const config = {
      matcher: [
        /*
         * Match all request paths except for the ones starting with:
         * - api (API routes)
         * - _next/static (static files)
         * - _next/image (image optimization files)
         * - favicon.ico (favicon file)
         */
        {
          source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
          missing: [
            { type: 'header', key: 'next-router-prefetch' },
            { type: 'header', key: 'purpose', value: 'prefetch' },
          ],
        },
      ],
    }
[/code]

### How nonces work in Next.js[](https://nextjs.org/docs/app/guides/content-security-policy#how-nonces-work-in-nextjs)

To use a nonce, your page must be **dynamically rendered**. This is because Next.js applies nonces during **server-side rendering** , based on the CSP header present in the request. Static pages are generated at build time, when no request or response headers exist—so no nonce can be injected.

Here’s how nonce support works in a dynamically rendered page:

  1. **Proxy generates a nonce** : Your proxy creates a unique nonce for the request, adds it to your `Content-Security-Policy` header, and also sets it in a custom `x-nonce` header.
  2. **Next.js extracts the nonce** : During rendering, Next.js parses the `Content-Security-Policy` header and extracts the nonce using the `'nonce-{value}'` pattern.
  3. **Nonce is applied automatically** : Next.js attaches the nonce to:
     * Framework scripts (React, Next.js runtime)
     * Page-specific JavaScript bundles
     * Inline styles and scripts generated by Next.js
     * Any `<Script>` components using the `nonce` prop



Because of this automatic behavior, you don’t need to manually add a nonce to each tag.

### Forcing dynamic rendering[](https://nextjs.org/docs/app/guides/content-security-policy#forcing-dynamic-rendering)

If you're using nonces, you may need to explicitly opt pages into dynamic rendering:

app/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
     
    export default async function Page() {
      // wait for an incoming request to render this page
      await connection()
      // Your page content
    }
[/code]

### Reading the nonce[](https://nextjs.org/docs/app/guides/content-security-policy#reading-the-nonce)

You can read the nonce from a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) using [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers):

app/page.tsx

JavaScriptTypeScript
[code]
    import { headers } from 'next/headers'
    import Script from 'next/script'
     
    export default async function Page() {
      const nonce = (await headers()).get('x-nonce')
     
      return (
        <Script
          src="https://www.googletagmanager.com/gtag/js"
          strategy="afterInteractive"
          nonce={nonce}
        />
      )
    }
[/code]

## Static vs Dynamic Rendering with CSP[](https://nextjs.org/docs/app/guides/content-security-policy#static-vs-dynamic-rendering-with-csp)

Using nonces has important implications for how your Next.js application renders:

### Dynamic Rendering Requirement[](https://nextjs.org/docs/app/guides/content-security-policy#dynamic-rendering-requirement)

When you use nonces in your CSP, **all pages must be dynamically rendered**. This means:

  * Pages will build successfully but may encounter runtime errors if not properly configured for dynamic rendering
  * Each request generates a fresh page with a new nonce
  * Static optimization and Incremental Static Regeneration (ISR) are disabled
  * Pages cannot be cached by CDNs without additional configuration
  * **Partial Prerendering (PPR) is incompatible** with nonce-based CSP since static shell scripts won't have access to the nonce



### Performance Implications[](https://nextjs.org/docs/app/guides/content-security-policy#performance-implications)

The shift from static to dynamic rendering affects performance:

  * **Slower initial page loads** : Pages must be generated on each request
  * **Increased server load** : Every request requires server-side rendering
  * **No CDN caching** : Dynamic pages cannot be cached at the edge by default
  * **Higher hosting costs** : More server resources needed for dynamic rendering



### When to use nonces[](https://nextjs.org/docs/app/guides/content-security-policy#when-to-use-nonces)

Consider nonces when:

  * You have strict security requirements that prohibit `'unsafe-inline'`
  * Your application handles sensitive data
  * You need to allow specific inline scripts while blocking others
  * Compliance requirements mandate strict CSP



## Without Nonces[](https://nextjs.org/docs/app/guides/content-security-policy#without-nonces)

For applications that do not require nonces, you can set the CSP header directly in your [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js) file:

next.config.js
[code]
    const isDev = process.env.NODE_ENV === 'development'
     
    const cspHeader = `
        default-src 'self';
        script-src 'self' 'unsafe-inline'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self' 'unsafe-inline';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `
     
    module.exports = {
      async headers() {
        return [
          {
            source: '/(.*)',
            headers: [
              {
                key: 'Content-Security-Policy',
                value: cspHeader.replace(/\n/g, ''),
              },
            ],
          },
        ]
      },
    }
[/code]

## Subresource Integrity (Experimental)[](https://nextjs.org/docs/app/guides/content-security-policy#subresource-integrity-experimental)

As an alternative to nonces, Next.js offers experimental support for hash-based CSP using Subresource Integrity (SRI). This approach allows you to maintain static generation while still having a strict CSP.

> **Good to know** : This feature is experimental and only available with webpack bundler in App Router applications.

### How SRI works[](https://nextjs.org/docs/app/guides/content-security-policy#how-sri-works)

Instead of using nonces, SRI generates cryptographic hashes of your JavaScript files at build time. These hashes are added as `integrity` attributes to script tags, allowing browsers to verify that files haven't been modified during transit.

### Enabling SRI[](https://nextjs.org/docs/app/guides/content-security-policy#enabling-sri)

Add the experimental SRI configuration to your `next.config.js`:

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      experimental: {
        sri: {
          algorithm: 'sha256', // or 'sha384' or 'sha512'
        },
      },
    }
     
    module.exports = nextConfig
[/code]

### CSP configuration with SRI[](https://nextjs.org/docs/app/guides/content-security-policy#csp-configuration-with-sri)

When SRI is enabled, you can continue using your existing CSP policies. SRI works independently by adding `integrity` attributes to your assets:

> **Good to know** : For dynamic rendering scenarios, you can still generate nonces with proxy if needed, combining both SRI integrity attributes and nonce-based CSP approaches.

next.config.js
[code]
    const isDev = process.env.NODE_ENV === 'development'
     
    const cspHeader = `
        default-src 'self';
        script-src 'self'${isDev ? " 'unsafe-eval'" : ''};
        style-src 'self';
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `
     
    module.exports = {
      experimental: {
        sri: {
          algorithm: 'sha256',
        },
      },
      async headers() {
        return [
          {
            source: '/(.*)',
            headers: [
              {
                key: 'Content-Security-Policy',
                value: cspHeader.replace(/\n/g, ''),
              },
            ],
          },
        ]
      },
    }
[/code]

### Benefits of SRI over nonces[](https://nextjs.org/docs/app/guides/content-security-policy#benefits-of-sri-over-nonces)

  * **Static generation** : Pages can be statically generated and cached
  * **CDN compatibility** : Static pages work with CDN caching
  * **Better performance** : No server-side rendering required for each request
  * **Build-time security** : Hashes are generated at build time, ensuring integrity



### Limitations of SRI[](https://nextjs.org/docs/app/guides/content-security-policy#limitations-of-sri)

  * **Experimental** : Feature may change or be removed
  * **Webpack only** : Not available with Turbopack
  * **App Router only** : Not supported in Pages Router
  * **Build-time only** : Cannot handle dynamically generated scripts



## Development vs Production Considerations[](https://nextjs.org/docs/app/guides/content-security-policy#development-vs-production-considerations)

CSP implementation differs between development and production environments:

### Development Environment[](https://nextjs.org/docs/app/guides/content-security-policy#development-environment)

In development, you will need to enable `'unsafe-eval'` because React uses `eval` to provide enhanced debugging information, such as reconstructing server-side error stacks in the browser to show you where errors originated on the server:

proxy.ts

JavaScriptTypeScript
[code]
    export function proxy(request: NextRequest) {
      const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
      const isDev = process.env.NODE_ENV === 'development'
     
      const cspHeader = `
        default-src 'self';
        script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${isDev ? "'unsafe-eval'" : ''};
        style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`};
        img-src 'self' blob: data:;
        font-src 'self';
        object-src 'none';
        base-uri 'self';
        form-action 'self';
        frame-ancestors 'none';
        upgrade-insecure-requests;
    `
     
      // Rest of proxy implementation
    }
[/code]

### Production Deployment[](https://nextjs.org/docs/app/guides/content-security-policy#production-deployment)

Common issues in production:

  * **Nonce not applied** : Ensure your proxy runs on all necessary routes
  * **Static assets blocked** : Verify your CSP allows Next.js static assets
  * **Third-party scripts** : Add necessary domains to your CSP policy



## Troubleshooting[](https://nextjs.org/docs/app/guides/content-security-policy#troubleshooting)

### Third-party Scripts[](https://nextjs.org/docs/app/guides/content-security-policy#third-party-scripts)

When using third-party scripts with CSP:

app/layout.tsx

JavaScriptTypeScript
[code]
    import { GoogleTagManager } from '@next/third-parties/google'
    import { headers } from 'next/headers'
     
    export default async function RootLayout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const nonce = (await headers()).get('x-nonce')
     
      return (
        <html lang="en">
          <body>
            {children}
            <GoogleTagManager gtmId="GTM-XYZ" nonce={nonce} />
          </body>
        </html>
      )
    }
[/code]

Update your CSP to allow third-party domains:

proxy.ts

JavaScriptTypeScript
[code]
    const cspHeader = `
      default-src 'self';
      script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
      connect-src 'self' https://www.google-analytics.com;
      img-src 'self' data: https://www.google-analytics.com;
    `
[/code]

### Common CSP Violations[](https://nextjs.org/docs/app/guides/content-security-policy#common-csp-violations)

  1. **Inline styles** : Use CSS-in-JS libraries that support nonces or move styles to external files
  2. **Dynamic imports** : Ensure dynamic imports are allowed in your script-src policy
  3. **WebAssembly** : Add `'wasm-unsafe-eval'` if using WebAssembly
  4. **Service workers** : Add appropriate policies for service worker scripts



## Version History[](https://nextjs.org/docs/app/guides/content-security-policy#version-history)

Version| Changes  
---|---  
`v14.0.0`| Experimental SRI support added for hash-based CSP  
`v13.4.20`| Recommended for proper nonce handling and CSP header parsing.  
  
## 

### [proxy.jsAPI reference for the proxy.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)### [headersAPI reference for the headers function.](https://nextjs.org/docs/app/api-reference/functions/headers)

Was this helpful?

supported.

Send
