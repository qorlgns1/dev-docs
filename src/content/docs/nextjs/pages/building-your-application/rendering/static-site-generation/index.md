---
title: '렌더링: Static Site Generation (SSG)'
description: '페이지가 Static Generation 을 사용하면 페이지 HTML은 빌드 시점 에 생성됩니다. 즉, 프로덕션 환경에서는  를 실행할 때 페이지 HTML이 생성됩니다. 이 HTML은 각 요청마다 재사용되며 CDN에 캐싱할 수 있습니다.'
---

# 렌더링: Static Site Generation (SSG) | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[렌더링](https://nextjs.org/docs/pages/building-your-application/rendering)Static Site Generation (SSG)

# Static Site Generation (SSG)

마지막 업데이트 2026년 2월 20일

예시

  * [Agility CMS 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-agilitycms) ([데모](https://next-blog-agilitycms.vercel.app/))
  * [Builder.io 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-builder-io) ([데모](https://cms-builder-io.vercel.app/))
  * [ButterCMS 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-buttercms) ([데모](https://next-blog-buttercms.vercel.app/))
  * [Contentful 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-contentful) ([데모](https://app-router-contentful.vercel.app/))
  * [Cosmic 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-cosmic) ([데모](https://next-blog-cosmic.vercel.app/))
  * [DatoCMS 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-datocms) ([데모](https://next-blog-datocms.vercel.app/))
  * [DotCMS 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-dotcms) ([데모](https://nextjs-dotcms-blog.vercel.app/))
  * [Drupal 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-drupal) ([데모](https://cms-drupal.vercel.app/))
  * [Enterspeed 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-enterspeed) ([데모](https://next-blog-demo.enterspeed.com/))
  * [GraphCMS 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-graphcms) ([데모](https://next-blog-graphcms.vercel.app/))
  * [Keystone 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-keystonejs-embedded) ([데모](https://nextjs-keystone-demo.vercel.app/))
  * [Kontent.ai 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-kontent-ai) ([데모](https://next-blog-kontent-ai.vercel.app/))
  * [Makeswift 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-makeswift) ([데모](https://nextjs-makeswift-example.vercel.app/))
  * [Plasmic 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-plasmic) ([데모](https://nextjs-plasmic-example.vercel.app/))
  * [Prepr 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-prepr) ([데모](https://next-blog-prepr.vercel.app/))
  * [Prismic 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-prismic) ([데모](https://next-blog-prismic.vercel.app/))
  * [Sanity 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-sanity) ([데모](https://next-blog.sanity.build/))
  * [Sitecore XM Cloud 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-sitecore-xmcloud) ([데모](https://vercel-sitecore-xmcloud-demo.vercel.app/))
  * [Storyblok 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-storyblok) ([데모](https://next-blog-storyblok.vercel.app/))
  * [Strapi 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-strapi) ([데모](https://next-blog-strapi.vercel.app/))
  * [TakeShape 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-takeshape) ([데모](https://next-blog-takeshape.vercel.app/))
  * [Tina 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-tina) ([데모](https://cms-tina-example.vercel.app/))
  * [Umbraco 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco) ([데모](https://nextjs-umbraco-sample-blog.vercel.app/))
  * [Umbraco Heartcore 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco-heartcore) ([데모](https://next-blog-umbraco-heartcore.vercel.app/))
  * [Webiny 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-webiny) ([데모](https://webiny-headlesscms-nextjs-example.vercel.app/))
  * [WordPress 예제](https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress) ([데모](https://next-blog-wordpress.vercel.app/))
  * [블로그 스타터 예제](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([데모](https://next-blog-starter.vercel.app/))
  * [Static Tweet (데모)](https://react-tweet.vercel.app/)

페이지가 **Static Generation** 을 사용하면 페이지 HTML은 **빌드 시점** 에 생성됩니다. 즉, 프로덕션 환경에서는 `next build` 를 실행할 때 페이지 HTML이 생성됩니다. 이 HTML은 각 요청마다 재사용되며 CDN에 캐싱할 수 있습니다.

Next.js에서는 페이지를 **데이터 유무와 관계없이** 정적으로 생성할 수 있습니다. 각 경우를 살펴보겠습니다.

### Static Generation without data[](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation#static-generation-without-data)

기본적으로 Next.js는 데이터를 가져오지 않고 Static Generation으로 페이지를 사전 렌더링합니다. 예시는 다음과 같습니다:
[code]
    function About() {
      return <div>About</div>
    }

    export default About
[/code]

이 페이지는 사전 렌더링을 위해 외부 데이터를 가져올 필요가 없습니다. 이런 경우 Next.js는 빌드 시 각 페이지마다 단일 HTML 파일을 생성합니다.

### Static Generation with data[](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation#static-generation-with-data)

일부 페이지는 사전 렌더링을 위해 외부 데이터를 가져와야 합니다. 두 가지 시나리오가 있으며, 하나 또는 둘 다 적용될 수 있습니다. 각 경우에 Next.js가 제공하는 다음 함수를 사용할 수 있습니다:

  1. 페이지 **콘텐츠** 가 외부 데이터에 의존할 때: `getStaticProps` 를 사용합니다.
  2. 페이지 **경로** 가 외부 데이터에 의존할 때: `getStaticPaths` 를 사용합니다(보통 `getStaticProps` 와 함께).

#### Scenario 1: Your page content depends on external data[](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation#scenario-1-your-page-content-depends-on-external-data)

**예시** : 블로그 페이지가 CMS(콘텐츠 관리 시스템)에서 블로그 글 목록을 가져와야 할 수 있습니다.
[code]
    // TODO: Need to fetch `posts` (by calling some API endpoint)
    //       before this page can be pre-rendered.
    export default function Blog({ posts }) {
      return (
        <ul>
          {posts.map((post) => (
            <li>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

이 데이터를 사전 렌더링 시 가져오기 위해 Next.js는 동일한 파일에서 `getStaticProps` 라는 `async` 함수를 `export` 할 수 있게 합니다. 이 함수는 빌드 시 호출되며 가져온 데이터를 페이지의 `props` 로 전달할 수 있게 해줍니다.
[code]
    export default function Blog({ posts }) {
      // Render posts...
    }

    // This function gets called at build time
    export async function getStaticProps() {
      // Call an external API endpoint to get posts
      const res = await fetch('https://.../posts')
      const posts = await res.json()

      // By returning { props: { posts } }, the Blog component
      // will receive `posts` as a prop at build time
      return {
        props: {
          posts,
        },
      }
    }
[/code]

`getStaticProps` 작동 방식에 대해 더 알아보려면 [데이터 패칭 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 확인하세요.

#### Scenario 2: Your page paths depend on external data[](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation#scenario-2-your-page-paths-depend-on-external-data)

Next.js에서는 **동적 라우트** 로 페이지를 만들 수 있습니다. 예를 들어 `pages/posts/[id].js` 파일을 생성하여 `id` 에 따라 단일 블로그 글을 표시할 수 있습니다. 그러면 `posts/1` 에 접근할 때 `id: 1`인 블로그 글을 보여줄 수 있습니다.

> 동적 라우팅에 대해 더 알아보려면 [동적 라우팅 문서](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 확인하세요.

그러나 빌드 시 어떤 `id` 를 사전 렌더링할지는 외부 데이터에 따라 달라질 수 있습니다.

**예시** : 데이터베이스에 `id: 1`인 블로그 글 하나만 추가했다고 가정합니다. 이 경우 빌드 시에는 `posts/1`만 사전 렌더링하면 됩니다.

이후 `id: 2`인 두 번째 글을 추가하면 `posts/2`도 사전 렌더링하고 싶을 것입니다.

따라서 사전 렌더링할 페이지 **경로** 는 외부 데이터에 의존합니다. 이를 처리하기 위해 Next.js는 동적 페이지(이 경우 `pages/posts/[id].js`)에서 `getStaticPaths` 라는 `async` 함수를 `export` 할 수 있게 합니다. 이 함수는 빌드 시 호출되며 사전 렌더링하고 싶은 경로를 지정할 수 있습니다.
[code]
    // This function gets called at build time
    export async function getStaticPaths() {
      // Call an external API endpoint to get posts
      const res = await fetch('https://.../posts')
      const posts = await res.json()

      // Get the paths we want to pre-render based on posts
      const paths = posts.map((post) => ({
        params: { id: post.id },
      }))

      // We'll pre-render only these paths at build time.
      // { fallback: false } means other routes should 404.
      return { paths, fallback: false }
    }
[/code]

또한 `pages/posts/[id].js` 에서 `getStaticProps` 를 내보내 `id` 에 해당하는 글의 데이터를 가져와 페이지를 사전 렌더링해야 합니다:
[code]
    export default function Post({ post }) {
      // Render post...
    }

    export async function getStaticPaths() {
      // ...
    }

    // This also gets called at build time
    export async function getStaticProps({ params }) {
      // params contains the post `id`.
      // If the route is like /posts/1, then params.id is 1
      const res = await fetch(`https://.../posts/${params.id}`)
      const post = await res.json()

      // Pass post data to the page via props
      return { props: { post } }
    }
[/code]

`getStaticPaths` 작동 방식에 대해 더 알아보려면 [데이터 패칭 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)를 확인하세요.

### When should I use Static Generation?[](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation#when-should-i-use-static-generation)

가능하다면 **Static Generation** (데이터 유무와 상관없이) 사용을 권장합니다. 페이지를 한 번만 빌드해 CDN에서 제공할 수 있어 요청마다 서버가 페이지를 렌더링하는 것보다 훨씬 빠르기 때문입니다.

Static Generation은 다음과 같은 다양한 유형의 페이지에 사용할 수 있습니다:

  * 마케팅 페이지
  * 블로그 글 및 포트폴리오
  * 전자상거래 상품 목록
  * 도움말 및 문서

다음 질문을 스스로에게 던져보세요: "사용자 요청 **이전에** 이 페이지를 사전 렌더링할 수 있는가?" 대답이 예라면 Static Generation을 선택해야 합니다.

반면, 사용자 요청 이전에 페이지를 사전 렌더링할 수 없다면 Static Generation은 **좋은 선택이 아닙니다**. 페이지가 자주 업데이트되는 데이터를 보여주고 요청마다 내용이 바뀌는 경우일 수 있습니다.

이런 상황에서는 다음 중 하나를 선택할 수 있습니다:

  * **클라이언트 측 데이터 페칭** 을 사용하는 Static Generation: 페이지의 일부는 사전 렌더링을 건너뛰고 클라이언트 측 JavaScript로 채울 수 있습니다. 이 방식에 대해 자세히 알아보려면 [데이터 패칭 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)를 확인하세요.
  * **Server-Side Rendering** 사용: Next.js가 각 요청마다 페이지를 사전 렌더링합니다. CDN에 캐시할 수 없으므로 더 느리지만, 사전 렌더링된 페이지는 항상 최신 상태를 유지합니다. 이 방식은 아래에서 다룹니다.

보내기
