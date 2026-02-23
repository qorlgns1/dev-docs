---
title: 'next.config.js Options: headers'
description: 'Last updated February 20, 2026'
---

# next.config.js Options: headers | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)headers

Copy page

# headers

Last updated February 20, 2026

Headers allow you to set custom HTTP headers on the response to an incoming request on a given path.

To set custom HTTP headers you can use the `headers` key in `next.config.js`:

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            source: '/about',
            headers: [
              {
                key: 'x-custom-header',
                value: 'my custom header value',
              },
              {
                key: 'x-another-custom-header',
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
[/code]

`headers` is an async function that expects an array to be returned holding objects with `source` and `headers` properties:

  * `source` is the incoming request path pattern.
  * `headers` is an array of response header objects, with `key` and `value` properties.
  * `basePath`: `false` or `undefined` \- if false the basePath won't be included when matching, can be used for external rewrites only.
  * `locale`: `false` or `undefined` \- whether the locale should not be included when matching.
  * `has` is an array of [has objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
  * `missing` is an array of [missing objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.



Headers are checked before the filesystem which includes pages and `/public` files.

## Header Overriding Behavior[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-overriding-behavior)

If two headers match the same path and set the same header key, the last header key will override the first. Using the below headers, the path `/hello` will result in the header `x-hello` being `world` due to the last header value set being `world`.

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            source: '/:path*',
            headers: [
              {
                key: 'x-hello',
                value: 'there',
              },
            ],
          },
          {
            source: '/hello',
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
        ]
      },
    }
[/code]

## Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#path-matching)

Path matches are allowed, for example `/blog/:slug` will match `/blog/first-post` (no nested paths):

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:slug',
            headers: [
              {
                key: 'x-slug',
                value: ':slug', // Matched parameters can be used in the value
              },
              {
                key: 'x-slug-:slug', // Matched parameters can be used in the key
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
[/code]

The pattern `/blog/:slug` matches `/blog/first-post` and `/blog/post-1` but not a nested path like `/blog/a/b`. Patterns are anchored to the start, `/blog/:slug` will not match `/archive/blog/first-post`.

You can use modifiers on parameters: `*` (zero or more), `+` (one or more), `?` (zero or one). For example, `/blog/:slug*` matches `/blog`, `/blog/a`, and `/blog/a/b/c`.

Read more details on [path-to-regexp](https://github.com/pillarjs/path-to-regexp) documentation.

### Wildcard Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#wildcard-path-matching)

To match a wildcard path you can use `*` after a parameter, for example `/blog/:slug*` will match `/blog/a/b/c/d/hello-world`:

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:slug*',
            headers: [
              {
                key: 'x-slug',
                value: ':slug*', // Matched parameters can be used in the value
              },
              {
                key: 'x-slug-:slug*', // Matched parameters can be used in the key
                value: 'my other custom header value',
              },
            ],
          },
        ]
      },
    }
[/code]

### Regex Path Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#regex-path-matching)

To match a regex path you can wrap the regex in parenthesis after a parameter, for example `/blog/:slug(\\d{1,})` will match `/blog/123` but not `/blog/abc`:

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            source: '/blog/:post(\\d{1,})',
            headers: [
              {
                key: 'x-post',
                value: ':post',
              },
            ],
          },
        ]
      },
    }
[/code]

The following characters `(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` are used for regex path matching, so when used in the `source` as non-special values they must be escaped by adding `\\` before them:

next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          {
            // this will match `/english(default)/something` being requested
            source: '/english\\(default\\)/:slug',
            headers: [
              {
                key: 'x-header',
                value: 'value',
              },
            ],
          },
        ]
      },
    }
[/code]

## Header, Cookie, and Query Matching[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching)

To only apply a header when header, cookie, or query values also match the `has` field or don't match the `missing` field can be used. Both the `source` and all `has` items must match and all `missing` items must not match for the header to be applied.

`has` and `missing` items can have the following fields:

  * `type`: `String` \- must be either `header`, `cookie`, `host`, or `query`.
  * `key`: `String` \- the key from the selected type to match against.
  * `value`: `String` or `undefined` \- the value to check for, if undefined any value will match. A regex like string can be used to capture a specific part of the value, e.g. if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`.



next.config.js
[code]
    module.exports = {
      async headers() {
        return [
          // if the header `x-add-header` is present,
          // the `x-another-header` header will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-add-header',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: 'hello',
              },
            ],
          },
          // if the header `x-no-header` is not present,
          // the `x-another-header` header will be applied
          {
            source: '/:path*',
            missing: [
              {
                type: 'header',
                key: 'x-no-header',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: 'hello',
              },
            ],
          },
          // if the source, query, and cookie are matched,
          // the `x-authorized` header will be applied
          {
            source: '/specific/:path*',
            has: [
              {
                type: 'query',
                key: 'page',
                // the page value will not be available in the
                // header key/values since value is provided and
                // doesn't use a named capture group e.g. (?<page>home)
                value: 'home',
              },
              {
                type: 'cookie',
                key: 'authorized',
                value: 'true',
              },
            ],
            headers: [
              {
                key: 'x-authorized',
                value: ':authorized',
              },
            ],
          },
          // if the header `x-authorized` is present and
          // contains a matching value, the `x-another-header` will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'header',
                key: 'x-authorized',
                value: '(?<authorized>yes|true)',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: ':authorized',
              },
            ],
          },
          // if the host is `example.com`,
          // this header will be applied
          {
            source: '/:path*',
            has: [
              {
                type: 'host',
                value: 'example.com',
              },
            ],
            headers: [
              {
                key: 'x-another-header',
                value: ':authorized',
              },
            ],
          },
        ]
      },
    }
[/code]

## Headers with basePath support[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#headers-with-basepath-support)

When leveraging [`basePath` support](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) with headers each `source` is automatically prefixed with the `basePath` unless you add `basePath: false` to the header:

next.config.js
[code]
    module.exports = {
      basePath: '/docs',
     
      async headers() {
        return [
          {
            source: '/with-basePath', // becomes /docs/with-basePath
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            source: '/without-basePath', // is not modified since basePath: false is set
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
            basePath: false,
          },
        ]
      },
    }
[/code]

## Headers with i18n support[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#headers-with-i18n-support)

When leveraging [`i18n` support](https://nextjs.org/docs/pages/guides/internationalization) with headers each `source` is automatically prefixed to handle the configured `locales` unless you add `locale: false` to the header. If `locale: false` is used you must prefix the `source` with a locale for it to be matched correctly.

next.config.js
[code]
    module.exports = {
      i18n: {
        locales: ['en', 'fr', 'de'],
        defaultLocale: 'en',
      },
     
      async headers() {
        return [
          {
            source: '/with-locale', // automatically handles all locales
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            // does not handle locales automatically since locale: false is set
            source: '/nl/with-locale-manual',
            locale: false,
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            // this matches '/' since `en` is the defaultLocale
            source: '/en',
            locale: false,
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
          {
            // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
            // `/` or `/fr` routes like /:path* would
            source: '/(.*)',
            headers: [
              {
                key: 'x-hello',
                value: 'world',
              },
            ],
          },
        ]
      },
    }
[/code]

## Cache-Control[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#cache-control)

Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` for truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). You cannot set `Cache-Control` headers in `next.config.js` for these assets.

However, you can set `Cache-Control` headers for other responses or data.

If you need to revalidate the cache of a page that has been [statically generated](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation), you can do so by setting the `revalidate` prop in the page's [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) function.

To cache the response from an [API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes), you can use `res.setHeader`:

pages/api/hello.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    type ResponseData = {
      message: string
    }
     
    export default function handler(
      req: NextApiRequest,
      res: NextApiResponse<ResponseData>
    ) {
      res.setHeader('Cache-Control', 's-maxage=86400')
      res.status(200).json({ message: 'Hello from Next.js!' })
    }
[/code]

You can also use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/).

pages/index.tsx

JavaScriptTypeScript
[code]
    import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'
     
    // This value is considered fresh for ten seconds (s-maxage=10).
    // If a request is repeated within the next 10 seconds, the previously
    // cached value will still be fresh. If the request is repeated before 59 seconds,
    // the cached value will be stale but still render (stale-while-revalidate=59).
    //
    // In the background, a revalidation request will be made to populate the cache
    // with a fresh value. If you refresh the page, you will see the new value.
    export const getServerSideProps = (async (context) => {
      context.res.setHeader(
        'Cache-Control',
        'public, s-maxage=10, stale-while-revalidate=59'
      )
     
      return {
        props: {},
      }
    }) satisfies GetServerSideProps
[/code]

## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#options)

### CORS[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#cors)

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS) is a security feature that allows you to control which sites can access your resources. You can set the `Access-Control-Allow-Origin` header to allow a specific origin to access your API Endpoints.
[code] 
    async headers() {
        return [
          {
            source: "/api/:path*",
            headers: [
              {
                key: "Access-Control-Allow-Origin",
                value: "*", // Set your origin
              },
              {
                key: "Access-Control-Allow-Methods",
                value: "GET, POST, PUT, DELETE, OPTIONS",
              },
              {
                key: "Access-Control-Allow-Headers",
                value: "Content-Type, Authorization",
              },
            ],
          },
        ];
      },
[/code]

### X-DNS-Prefetch-Control[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-dns-prefetch-control)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control) controls DNS prefetching, allowing browsers to proactively perform domain name resolution on external links, images, CSS, JavaScript, and more. This prefetching is performed in the background, so the [DNS](https://developer.mozilla.org/docs/Glossary/DNS) is more likely to be resolved by the time the referenced items are needed. This reduces latency when the user clicks a link.
[code] 
    {
      key: 'X-DNS-Prefetch-Control',
      value: 'on'
    }
[/code]

### Strict-Transport-Security[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#strict-transport-security)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) informs browsers it should only be accessed using HTTPS, instead of using HTTP. Using the configuration below, all present and future subdomains will use HTTPS for a `max-age` of 2 years. This blocks access to pages or subdomains that can only be served over HTTP.
[code] 
    {
      key: 'Strict-Transport-Security',
      value: 'max-age=63072000; includeSubDomains; preload'
    }
[/code]

### X-Frame-Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-frame-options)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Frame-Options) indicates whether the site should be allowed to be displayed within an `iframe`. This can prevent against clickjacking attacks.

**This header has been superseded by CSP's`frame-ancestors` option**, which has better support in modern browsers (see [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy) for configuration details).
[code] 
    {
      key: 'X-Frame-Options',
      value: 'SAMEORIGIN'
    }
[/code]

### Permissions-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#permissions-policy)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Permissions-Policy) allows you to control which features and APIs can be used in the browser. It was previously named `Feature-Policy`.
[code] 
    {
      key: 'Permissions-Policy',
      value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
    }
[/code]

### X-Content-Type-Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#x-content-type-options)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Content-Type-Options) prevents the browser from attempting to guess the type of content if the `Content-Type` header is not explicitly set. This can prevent XSS exploits for websites that allow users to upload and share files.

For example, a user trying to download an image, but having it treated as a different `Content-Type` like an executable, which could be malicious. This header also applies to downloading browser extensions. The only valid value for this header is `nosniff`.
[code] 
    {
      key: 'X-Content-Type-Options',
      value: 'nosniff'
    }
[/code]

### Referrer-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#referrer-policy)

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Referrer-Policy) controls how much information the browser includes when navigating from the current website (origin) to another.
[code] 
    {
      key: 'Referrer-Policy',
      value: 'origin-when-cross-origin'
    }
[/code]

### Content-Security-Policy[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#content-security-policy)

Learn more about adding a [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy) to your application.

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#version-history)

Version| Changes  
---|---  
`v13.3.0`| `missing` added.  
`v10.2.0`| `has` added.  
`v9.5.0`| Headers added.  
  
Was this helpful?

supported.

Send
