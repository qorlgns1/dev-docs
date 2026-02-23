---
title: 'Functions: NextRequest'
description: 'Last updated February 20, 2026'
---

# Functions: NextRequest | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/next-request

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)NextRequest

Copy page

# NextRequest

Last updated February 20, 2026

NextRequest extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional convenience methods.

## `cookies`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#cookies)

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the request.

### `set(name, value)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#setname-value)

Given a name, set a cookie with the given value on the request.
[code] 
    // Given incoming request /home
    // Set a cookie to hide the banner
    // request will have a `Set-Cookie:show-banner=false;path=/home` header
    request.cookies.set('show-banner', 'false')
[/code]

### `get(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getname)

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.
[code] 
    // Given incoming request /home
    // { name: 'show-banner', value: 'false', Path: '/home' }
    request.cookies.get('show-banner')
[/code]

### `getAll()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getall)

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.
[code] 
    // Given incoming request /home
    // [
    //   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
    //   { name: 'experiments', value: 'winter-launch', Path: '/home' },
    // ]
    request.cookies.getAll('experiments')
    // Alternatively, get all cookies for the request
    request.cookies.getAll()
[/code]

### `delete(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#deletename)

Given a cookie name, delete the cookie from the request.
[code] 
    // Returns true for deleted, false is nothing is deleted
    request.cookies.delete('experiments')
[/code]

### `has(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#hasname)

Given a cookie name, return `true` if the cookie exists on the request.
[code] 
    // Returns true if cookie exists, false if it does not
    request.cookies.has('experiments')
[/code]

### `clear()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#clear)

Remove all cookies from the request.
[code] 
    request.cookies.clear()
[/code]

## `nextUrl`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#nexturl)

Extends the native [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API with additional convenience methods, including Next.js specific properties.
[code] 
    // Given a request to /home, pathname is /home
    request.nextUrl.pathname
    // Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
    request.nextUrl.searchParams
[/code]

The following options are available:

Property| Type| Description  
---|---|---  
`basePath`| `string`| The [base path](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath) of the URL.  
`buildId`| `string` | `undefined`| The build identifier of the Next.js application. Can be [customized](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId).  
`defaultLocale`| `string` | `undefined`| The default locale for [internationalization](https://nextjs.org/docs/pages/guides/internationalization).  
`domainLocale`| |   
\- `defaultLocale`| `string`| The default locale within a domain.  
\- `domain`| `string`| The domain associated with a specific locale.  
\- `http`| `boolean` | `undefined`| Indicates if the domain is using HTTP.  
`locales`| `string[]` | `undefined`| An array of available locales.  
`locale`| `string` | `undefined`| The currently active locale.  
`url`| `URL`| The URL object.  
  
## Version History[](https://nextjs.org/docs/pages/api-reference/functions/next-request#version-history)

Version| Changes  
---|---  
`v15.0.0`| `ip` and `geo` removed.  
  
Was this helpful?

supported.

Send
