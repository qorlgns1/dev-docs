---
title: 'Routing: Dynamic Routes'
description: '미리 정확한 세그먼트 이름을 알지 못하고 동적 데이터에서 라우트를 생성하려면, 요청 시점에 채워지거나 빌드 시점에 프리렌더링되는 Dynamic Segment를 사용할 수 있습니다.'
---

# Routing: Dynamic Routes | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Routing](https://nextjs.org/docs/pages/building-your-application/routing)Dynamic Routes

Copy page

# Dynamic Routes

Last updated February 20, 2026

미리 정확한 세그먼트 이름을 알지 못하고 동적 데이터에서 라우트를 생성하려면, 요청 시점에 채워지거나 빌드 시점에 [프리렌더링](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)되는 Dynamic Segment를 사용할 수 있습니다.

## Convention[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention)

파일 또는 폴더 이름을 대괄호로 감싸면 Dynamic Segment를 만들 수 있습니다: `[segmentName]`. 예를 들어 `[id]` 또는 `[slug]`가 있습니다.

Dynamic Segment는 [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router)에서 접근할 수 있습니다.

## Example[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#example)

예를 들어 블로그에는 `pages/blog/[slug].js` 라우트를 둘 수 있으며, 여기서 `[slug]`는 블로그 게시물용 Dynamic Segment입니다.
[code]
    import { useRouter } from 'next/router'

    export default function Page() {
      const router = useRouter()
      return <p>Post: {router.query.slug}</p>
    }
[/code]

Route| Example URL| `params`
---|---|---
`pages/blog/[slug].js`| `/blog/a`| `{ slug: 'a' }`
`pages/blog/[slug].js`| `/blog/b`| `{ slug: 'b' }`
`pages/blog/[slug].js`| `/blog/c`| `{ slug: 'c' }`

## Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)

Dynamic Segment는 대괄호 안에 줄임표를 추가해 `[...segmentName]`처럼 작성하면 이후 세그먼트를 **모두 포착(catch-all)** 하도록 확장할 수 있습니다.

예를 들어 `pages/shop/[...slug].js`는 `/shop/clothes`뿐 아니라 `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts` 등도 모두 일치시킵니다.

Route| Example URL| `params`
---|---|---
`pages/shop/[...slug].js`| `/shop/a`| `{ slug: ['a'] }`
`pages/shop/[...slug].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`
`pages/shop/[...slug].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`

## Optional Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)

Catch-all Segment는 매개변수를 이중 대괄호로 감싸 `[[...segmentName]]`처럼 작성하면 **선택적(optional)** 으로 만들 수 있습니다.

예를 들어 `pages/shop/[[...slug]].js`는 `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`에 더해 `/shop`도 **일치** 시킵니다.

**Catch-all**과 **optional catch-all** 세그먼트의 차이는, optional에서는 매개변수 없이도 라우트가 일치한다는 점입니다(위 예시에서 `/shop`).

Route| Example URL| `params`
---|---|---
`pages/shop/[[...slug]].js`| `/shop`| `{ slug: undefined }`
`pages/shop/[[...slug]].js`| `/shop/a`| `{ slug: ['a'] }`
`pages/shop/[[...slug]].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`
`pages/shop/[[...slug]].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`

## Next Steps

다음에 무엇을 해야 하는지 더 알고 싶다면 아래 섹션을 참고하세요.

- [링크 및 탐색](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)
  - Linking and NavigatingNext.js에서 내비게이션이 어떻게 동작하는지, Link 컴포넌트와 `useRouter` 훅을 사용하는 방법을 알아보세요.

- [useRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router)
  - Next.js Router API를 더 깊이 이해하고, 페이지에서 useRouter 훅으로 라우터 인스턴스에 접근하는 방법을 확인하세요.

Was this helpful?

supported.

Send
