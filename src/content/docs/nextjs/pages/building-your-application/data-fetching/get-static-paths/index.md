---
title: '데이터 패칭: getStaticPaths'
description: '페이지가 동적 라우트를 사용하고 를 정의한다면, 정적으로 생성할 경로 목록을 지정해야 합니다.'
---

# 데이터 패칭: getStaticPaths | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[데이터 패칭](https://nextjs.org/docs/pages/building-your-application/data-fetching)getStaticPaths

Copy page

# getStaticPaths

마지막 업데이트: 2026년 2월 20일

페이지가 [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 사용하고 `getStaticProps`를 정의한다면, 정적으로 생성할 경로 목록을 지정해야 합니다.

동적 라우트를 사용하는 페이지에서 `getStaticPaths`(정적 사이트 생성)라는 함수를 export하면, Next.js는 `getStaticPaths`가 지정한 모든 경로를 정적으로 사전 렌더링합니다.

pages/repo/[name].tsx

JavaScriptTypeScript
[code]
    import type {
      InferGetStaticPropsType,
      GetStaticProps,
      GetStaticPaths,
    } from 'next'
     
    type Repo = {
      name: string
      stargazers_count: number
    }
     
    export const getStaticPaths = (async () => {
      return {
        paths: [
          {
            params: {
              name: 'next.js',
            },
          }, // See the "paths" section below
        ],
        fallback: true, // false or "blocking"
      }
    }) satisfies GetStaticPaths
     
    export const getStaticProps = (async (context) => {
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const repo = await res.json()
      return { props: { repo } }
    }) satisfies GetStaticProps<{
      repo: Repo
    }>
     
    export default function Page({
      repo,
    }: InferGetStaticPropsType<typeof getStaticProps>) {
      return repo.stargazers_count
    }
[/code]

[`getStaticPaths` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths)는 `getStaticPaths`와 함께 사용할 수 있는 모든 매개변수와 props를 다룹니다.

## 언제 getStaticPaths를 사용해야 하나요?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#when-should-i-use-getstaticpaths)

동적 라우트를 사용하는 페이지를 정적으로 사전 렌더링하며 다음과 같은 경우 `getStaticPaths`를 사용해야 합니다.

  * 데이터가 헤드리스 CMS에서 오는 경우
  * 데이터가 데이터베이스에서 오는 경우
  * 데이터가 파일 시스템에서 오는 경우
  * 데이터가 공개적으로 캐시될 수 있는 경우(사용자별 데이터가 아님)
  * 페이지가 사전 렌더링되어야 하고(SEO용) 매우 빠른 속도를 요구하는 경우 — `getStaticProps`는 `HTML`과 `JSON` 파일을 생성하며, CDN이 모두 캐시할 수 있어 성능에 유리합니다.



## getStaticPaths는 언제 실행되나요?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#when-does-getstaticpaths-run)

`getStaticPaths`는 프로덕션에서 빌드 중에만 실행되며 런타임에는 호출되지 않습니다. [이 도구](https://next-code-elimination.vercel.app/)를 사용하면 `getStaticPaths` 내부에 작성한 코드가 클라이언트 번들에서 제거되었는지 검증할 수 있습니다.

### getStaticProps는 getStaticPaths와 어떤 관계로 실행되나요?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#how-does-getstaticprops-run-with-regards-to-getstaticpaths)

  * 빌드 중 반환된 모든 `paths`에 대해 `next build` 동안 `getStaticProps`가 실행됩니다.
  * `fallback: true`를 사용하는 경우 백그라운드에서 `getStaticProps`가 실행됩니다.
  * `fallback: blocking`을 사용하는 경우 초기 렌더 전에 `getStaticProps`가 호출됩니다.



## 어디에서 getStaticPaths를 사용할 수 있나요?[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#where-can-i-use-getstaticpaths)

  * `getStaticPaths`는 반드시 `getStaticProps`와 함께 사용해야 합니다.
  * [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)와 `getStaticPaths`를 함께 사용할 수 없습니다.
  * [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)에서 `getStaticProps`와 함께 `getStaticPaths`를 export할 수 있습니다.
  * 페이지가 아닌 파일(예: `components` 폴더)에서 `getStaticPaths`를 export할 수 없습니다.
  * 페이지 컴포넌트의 속성이 아니라 독립된 함수로 `getStaticPaths`를 export해야 합니다.



## 개발 환경에서는 모든 요청마다 실행됩니다[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#runs-on-every-request-in-development)

개발 환경(`next dev`)에서는 요청마다 `getStaticPaths`가 호출됩니다.

## 온디맨드로 경로 생성[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths#generating-paths-on-demand)

`getStaticPaths`를 사용하면 [`fallback`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)을 통해 온디맨드가 아니라 빌드 중에 어떤 페이지를 생성할지 제어할 수 있습니다. 빌드 중 더 많은 페이지를 생성할수록 빌드 속도는 느려집니다.

`paths`에 빈 배열을 반환하여 모든 페이지 생성을 온디맨드로 연기할 수 있습니다. 이는 Next.js 애플리케이션을 여러 환경에 배포할 때 특히 유용합니다. 예를 들어 프리뷰 환경에서는 모든 페이지를 온디맨드로 생성해 빌드를 빠르게 하고(프로덕션 빌드에서는 제외) 수백/수천 개의 정적 페이지가 있는 사이트에도 도움이 됩니다.

pages/posts/[id].js
[code]
    export async function getStaticPaths() {
      // When this is true (in preview environments) don't
      // prerender any static pages
      // (faster builds, but slower initial page load)
      if (process.env.SKIP_BUILD_STATIC_GENERATION) {
        return {
          paths: [],
          fallback: 'blocking',
        }
      }
     
      // Call an external API endpoint to get posts
      const res = await fetch('https://.../posts')
      const posts = await res.json()
     
      // Get the paths we want to prerender based on posts
      // In production environments, prerender all pages
      // (slower builds, but faster initial page load)
      const paths = posts.map((post) => ({
        params: { id: post.id },
      }))
     
      // { fallback: false } means other routes should 404
      return { paths, fallback: false }
    }
[/code]

Was this helpful?

supported.

Send
