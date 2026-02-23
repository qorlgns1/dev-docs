---
title: '함수: useSelectedLayoutSegment'
description: '최종 업데이트: 2026년 2월 20일'
---

# 함수: useSelectedLayoutSegment | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)useSelectedLayoutSegment

페이지 복사

# useSelectedLayoutSegment

최종 업데이트: 2026년 2월 20일

`useSelectedLayoutSegment`는 호출된 레이아웃 기준으로 **한 단계 아래**의 활성 라우트 세그먼트를 읽을 수 있게 해 주는 **클라이언트 컴포넌트** 훅입니다.

이 훅은 활성 자식 세그먼트에 따라 스타일이 달라지는 상위 레이아웃 내부 탭과 같은 내비게이션 UI에 유용합니다.

app/example-client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSelectedLayoutSegment } from 'next/navigation'
     
    export default function ExampleClientComponent() {
      const segment = useSelectedLayoutSegment()
     
      return <p>Active segment: {segment}</p>
    }
[/code]

> **알아 두면 좋은 점** :
> 
>   * `useSelectedLayoutSegment`는 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components) 훅이며, 레이아웃은 기본적으로 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)이므로, 보통 레이아웃에 임포트되는 클라이언트 컴포넌트에서 `useSelectedLayoutSegment`를 호출합니다.
>   * `useSelectedLayoutSegment`는 한 단계 아래의 세그먼트만 반환합니다. 모든 활성 세그먼트를 얻으려면 [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)를 참조하세요.
>   * [캐치올](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments) 라우트에서는 매칭된 세그먼트가 하나의 문자열로 연결되어 반환됩니다. 예를 들어 `app/blog/[...slug]/page.js`와 `/blog/a/b/c`를 방문할 때 `app/blog/layout.js`에서 호출하면 `'a/b/c'`가 반환됩니다.
> 

## 매개변수[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#parameters)
[code] 
    const segment = useSelectedLayoutSegment(parallelRoutesKey?: string)
[/code]

`useSelectedLayoutSegment`는 선택적으로 [`parallelRoutesKey`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#with-useselectedlayoutsegments)를 받아 해당 슬롯 내의 활성 라우트 세그먼트를 읽을 수 있습니다.

## 반환값[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#returns)

`useSelectedLayoutSegment`는 활성 세그먼트의 문자열을 반환하며, 존재하지 않으면 `null`을 반환합니다.

아래 레이아웃과 URL이 주어졌을 때 반환되는 세그먼트는 다음과 같습니다:

Layout|Visited URL|Returned Segment  
---|---|---  
`app/layout.js`|`/`|`null`  
`app/layout.js`|`/dashboard`|`'dashboard'`  
`app/dashboard/layout.js`|`/dashboard`|`null`  
`app/dashboard/layout.js`|`/dashboard/settings`|`'settings'`  
`app/dashboard/layout.js`|`/dashboard/analytics`|`'analytics'`  
`app/dashboard/layout.js`|`/dashboard/analytics/monthly`|`'analytics'`  

캐치올 라우트(`[...slug]`)의 경우, 반환된 세그먼트에는 매칭된 모든 경로 세그먼트가 하나의 문자열로 결합됩니다:

Layout|Visited URL|Returned Segment  
---|---|---  
`app/blog/layout.js`|`/blog/a/b/c`|`'a/b/c'`  

## 예시[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#examples)

### 활성 링크 컴포넌트 만들기[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#creating-an-active-link-component)

`useSelectedLayoutSegment`를 사용하면 활성 세그먼트에 따라 스타일이 달라지는 활성 링크 컴포넌트를 만들 수 있습니다. 예를 들어, 블로그 사이드바의 특집 포스트 목록에 사용할 수 있습니다:

app/blog/blog-nav-link.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import { useSelectedLayoutSegment } from 'next/navigation'
     
    // This *client* component will be imported into a blog layout
    export default function BlogNavLink({
      slug,
      children,
    }: {
      slug: string
      children: React.ReactNode
    }) {
      // Navigating to `/blog/hello-world` will return 'hello-world'
      // for the selected layout segment
      const segment = useSelectedLayoutSegment()
      const isActive = slug === segment
     
      return (
        <Link
          href={`/blog/${slug}`}
          // Change style depending on whether the link is active
          style={{ fontWeight: isActive ? 'bold' : 'normal' }}
        >
          {children}
        </Link>
      )
    }
[/code]

app/blog/layout.tsx

JavaScriptTypeScript
[code]
    // Import the Client Component into a parent Layout (Server Component)
    import { BlogNavLink } from './blog-nav-link'
    import getFeaturedPosts from './get-featured-posts'
     
    export default async function Layout({
      children,
    }: {
      children: React.ReactNode
    }) {
      const featuredPosts = await getFeaturedPosts()
      return (
        <div>
          {featuredPosts.map((post) => (
            <div key={post.id}>
              <BlogNavLink slug={post.slug}>{post.title}</BlogNavLink>
            </div>
          ))}
          <div>{children}</div>
        </div>
      )
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#version-history)

Version|Changes  
---|---  
`v13.0.0`|`useSelectedLayoutSegment` 도입.  

도움이 되었나요?

지원됨.

보내기
