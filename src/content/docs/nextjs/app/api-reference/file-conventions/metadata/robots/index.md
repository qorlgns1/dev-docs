---
title: '메타데이터 파일: robots.txt'
description: '검색 엔진 크롤러에게 사이트에서 접근 가능한 URL을 알리려면  디렉터리의 루트에 Robots 배제 표준을 따르는  파일을 추가하거나 생성하세요.'
---

# 메타데이터 파일: robots.txt | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots

Copy page

# robots.txt

마지막 업데이트 2026년 2월 20일

검색 엔진 크롤러에게 사이트에서 접근 가능한 URL을 알리려면 `app` 디렉터리의 **루트**에 [Robots 배제 표준](https://en.wikipedia.org/wiki/Robots.txt#Standard)을 따르는 `robots.txt` 파일을 추가하거나 생성하세요.

## 정적 `robots.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)

app/robots.txt
```
    User-Agent: *
    Allow: /
    Disallow: /private/

    Sitemap: https://acme.com/sitemap.xml
```

## Robots 파일 생성하기[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)

[`Robots` 객체](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object)를 반환하는 `robots.js` 또는 `robots.ts` 파일을 추가하세요.

> **참고**: `robots.js`는 특별한 Route Handler이며, [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)나 [동적 구성](https://nextjs.org/docs/app/guides/caching#segment-config-options)을 사용하지 않는 한 기본적으로 캐시됩니다.

app/robots.ts

JavaScriptTypeScript
```
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
```

출력:
```
    User-Agent: *
    Allow: /
    Disallow: /private/

    Sitemap: https://acme.com/sitemap.xml
```

### 특정 사용자 에이전트 사용자 지정[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#customizing-specific-user-agents)

`rules` 속성에 사용자 에이전트 배열을 전달해 개별 검색 엔진 봇의 크롤링 방식을 사용자 지정할 수 있습니다. 예:

app/robots.ts

JavaScriptTypeScript
```
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
```

출력:
```
    User-Agent: Googlebot
    Allow: /
    Disallow: /private/

    User-Agent: Applebot
    Disallow: /

    User-Agent: Bingbot
    Disallow: /

    Sitemap: https://acme.com/sitemap.xml
```

### Robots 객체[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object)
```
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
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#version-history)

Version| Changes
---|---
`v13.3.0`| `robots`가 도입됨.

supported.

Send