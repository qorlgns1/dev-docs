---
title: 'Metadata Files: robots.txt'
description: 'Add or generate a  file that matches the Robots Exclusion Standard in the root of  directory to tell search engine crawlers which URLs they can access...'
---

# Metadata Files: robots.txt | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots

[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)[Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)robots.txt

Copy page

# robots.txt

Last updated February 20, 2026

Add or generate a `robots.txt` file that matches the [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots.txt#Standard) in the **root** of `app` directory to tell search engine crawlers which URLs they can access on your site.

## Static `robots.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)

app/robots.txt
[code]
    User-Agent: *
    Allow: /
    Disallow: /private/
    
    Sitemap: https://acme.com/sitemap.xml
[/code]

## Generate a Robots file[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)

Add a `robots.js` or `robots.ts` file that returns a [`Robots` object](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object).

> **Good to know** : `robots.js` is a special Route Handler that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.

app/robots.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function robots(): MetadataRoute.Robots {
      return {
        rules: {
          userAgent: '*',
          allow: '/',
          disallow: '/private/',
        },
        sitemap: 'https://acme.com/sitemap.xml',
      }
    }
[/code]

Output:
[code] 
    User-Agent: *
    Allow: /
    Disallow: /private/
    
    Sitemap: https://acme.com/sitemap.xml
[/code]

### Customizing specific user agents[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#customizing-specific-user-agents)

You can customize how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:

app/robots.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function robots(): MetadataRoute.Robots {
      return {
        rules: [
          {
            userAgent: 'Googlebot',
            allow: ['/'],
            disallow: '/private/',
          },
          {
            userAgent: ['Applebot', 'Bingbot'],
            disallow: ['/'],
          },
        ],
        sitemap: 'https://acme.com/sitemap.xml',
      }
    }
[/code]

Output:
[code] 
    User-Agent: Googlebot
    Allow: /
    Disallow: /private/
    
    User-Agent: Applebot
    Disallow: /
    
    User-Agent: Bingbot
    Disallow: /
    
    Sitemap: https://acme.com/sitemap.xml
[/code]

### Robots object[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object)
[code] 
    type Robots = {
      rules:
        | {
            userAgent?: string | string[]
            allow?: string | string[]
            disallow?: string | string[]
            crawlDelay?: number
          }
        | Array<{
            userAgent: string | string[]
            allow?: string | string[]
            disallow?: string | string[]
            crawlDelay?: number
          }>
      sitemap?: string | string[]
      host?: string
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#version-history)

Version| Changes  
---|---  
`v13.3.0`| `robots` introduced.  
  
Was this helpful?

supported.

Send
