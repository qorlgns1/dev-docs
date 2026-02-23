---
title: '애플리케이션 빌드: 데이터 가져오기'
description: 'Next.js의 데이터 가져오기는 애플리케이션의 사용 사례에 따라 다양한 방식으로 콘텐츠를 렌더링할 수 있게 해 줍니다. 여기에는 서버 사이드 렌더링 또는 정적 생성을 통한 사전 렌더링과, 런타임에 증분 정적 재생성으로 콘텐츠를 업데이트하거나 생성하는 방법이 포함됩니다...'
---

# 애플리케이션 빌드: 데이터 가져오기 | Next.js

출처 URL: https://nextjs.org/docs/pages/building-your-application/data-fetching

[Pages Router](https://nextjs.org/docs/pages)[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)데이터 가져오기

페이지 복사

# 데이터 가져오기

마지막 업데이트: 2026년 2월 20일

Next.js의 데이터 가져오기는 애플리케이션의 사용 사례에 따라 다양한 방식으로 콘텐츠를 렌더링할 수 있게 해 줍니다. 여기에는 **서버 사이드 렌더링** 또는 **정적 생성**을 통한 사전 렌더링과, 런타임에 **증분 정적 재생성**으로 콘텐츠를 업데이트하거나 생성하는 방법이 포함됩니다.

## 예제[](https://nextjs.org/docs/pages/building-your-application/data-fetching#examples)

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
  * [Blog Starter 예제](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([데모](https://next-blog-starter.vercel.app/))
  * [Static Tweet (데모)](https://react-tweet.vercel.app/)



### [getStaticProps`getStaticProps`로 데이터를 가져와 정적 페이지를 생성합니다. Next.js의 이 데이터 패칭 API에 대해 자세히 알아보세요.](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)### [getStaticPaths`getStaticPaths`로 데이터를 가져와 정적 페이지를 생성합니다. Next.js의 이 데이터 패칭 API에 대해 자세히 알아보세요.](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)### [Forms and MutationsNext.js에서 폼 제출과 데이터 변경을 처리하는 방법을 알아보세요.](https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations)### [getServerSideProps각 요청마다 `getServerSideProps`로 데이터를 가져옵니다.](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)### [Client-side Fetching클라이언트 측 데이터 가져오기와 캐싱, 재검증, 포커스 추적, 주기적 재요청 등을 처리하는 데이터 패칭 React 훅 라이브러리 SWR 사용 방법을 알아보세요.](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)

도움이 되었나요?

지원됨.

보내기
