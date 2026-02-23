---
title: 'Functions: getStaticProps'
description: 'Last updated February 20, 2026'
---

# Functions: getStaticProps | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/functions/get-static-props

[API Reference](https://nextjs.org/docs/pages/api-reference)[Functions](https://nextjs.org/docs/pages/api-reference/functions)getStaticProps

Copy page

# getStaticProps

Last updated February 20, 2026

`getStaticProps`라는 함수를 export하면 함수가 반환한 props를 사용해 빌드 시점에 페이지를 사전 렌더링합니다:

pages/index.tsx

JavaScriptTypeScript
[code]
    import type { InferGetStaticPropsType, GetStaticProps } from 'next'
     
    type Repo = {
      name: string
      stargazers_count: number
    }
     
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

`getStaticProps`에서 사용할 모듈을 최상위 스코프에서 import할 수 있습니다. 이렇게 import한 모듈은 **클라이언트 번들에 포함되지 않습니다**. 즉 **서버 전용 코드를 `getStaticProps` 안에 직접 작성**할 수 있으며, 여기에 데이터베이스 조회도 포함됩니다.

## Context parameter[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#context-parameter)

`context` 파라미터는 다음 키들을 포함하는 객체입니다:

Name| Description  
---|---  
`params`| [동적 라우트](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)를 사용하는 페이지의 라우트 파라미터를 담습니다. 예를 들어 페이지 이름이 `[id].js`라면 `params`는 `{ id: ... }` 형태입니다. 뒤에서 설명할 `getStaticPaths`와 함께 사용해야 합니다.  
`preview`| (`draftMode`로 대체됨) 페이지가 [미리보기 모드](https://nextjs.org/docs/pages/guides/preview-mode)일 때 `true`, 아니면 `false`가 됩니다.  
`previewData`| (`draftMode`로 대체됨) `setPreviewData`로 설정한 [미리보기](https://nextjs.org/docs/pages/guides/preview-mode) 데이터입니다.  
`draftMode`| 페이지가 [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)일 때 `true`, 아니면 `false`입니다.  
`locale`| 활성화된 로케일이 포함됩니다(활성화된 경우).  
`locales`| 지원되는 모든 로케일이 포함됩니다(활성화된 경우).  
`defaultLocale`| 구성된 기본 로케일이 포함됩니다(활성화된 경우).  
`revalidateReason`| 함수가 호출된 이유를 제공합니다. 가능한 값: "build"(빌드 시 실행), "stale"(재검증 주기가 만료되었거나 [개발 모드](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#runs-on-every-request-in-development)에서 실행), "on-demand"([온디맨드 재검증](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)을 통해 트리거)  
  
## getStaticProps return values[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#getstaticprops-return-values)

`getStaticProps` 함수는 `props`, `redirect`, `notFound` 중 하나를 포함하는 객체를 반환해야 하며, 뒤에 **선택적으로** `revalidate`를 덧붙일 수 있습니다.

### `props`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#props)

`props` 객체는 키-값 쌍이며 각 값은 페이지 컴포넌트에서 받습니다. 전달하는 props는 [`JSON.stringify`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)를 통해 직렬화될 수 있도록 [직렬화 가능한 객체](https://developer.mozilla.org/docs/Glossary/Serialization)여야 합니다.
[code] 
    export async function getStaticProps(context) {
      return {
        props: { message: `Next.js is awesome` }, // will be passed to the page component as props
      }
    }
[/code]

### `revalidate`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#revalidate)

`revalidate` 속성은 페이지를 다시 생성할 수 있는 초 단위의 기간입니다(기본값은 `false`, 즉 재검증 없음).
[code] 
    // This function gets called at build time on server-side.
    // It may be called again, on a serverless function, if
    // revalidation is enabled and a new request comes in
    export async function getStaticProps() {
      const res = await fetch('https://.../posts')
      const posts = await res.json()
     
      return {
        props: {
          posts,
        },
        // Next.js will attempt to re-generate the page:
        // - When a request comes in
        // - At most once every 10 seconds
        revalidate: 10, // In seconds
      }
    }
[/code]

[Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)에 대해 더 알아보세요.

ISR을 활용하는 페이지의 캐시 상태는 `x-nextjs-cache` 응답 헤더 값을 통해 확인할 수 있습니다. 가능한 값은 다음과 같습니다:

  * `MISS` \- 경로가 캐시에 없음(최대 한 번, 첫 방문에서 발생)
  * `STALE` \- 경로가 캐시에 있지만 재검증 시간이 지남; 백그라운드에서 갱신됨
  * `HIT` \- 경로가 캐시에 있고 재검증 시간이 지나지 않음



### `notFound`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#notfound)

`notFound` boolean은 페이지가 `404` 상태와 [404 페이지](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)를 반환하도록 합니다. `notFound: true`이면 이전에 성공적으로 생성된 페이지가 있더라도 `404`를 반환합니다. 이는 사용자 생성 콘텐츠가 작성자에 의해 삭제되는 상황을 지원하기 위한 것입니다. `notFound`는 [여기](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#revalidate)에서 설명한 것과 동일한 `revalidate` 동작을 따릅니다.
[code] 
    export async function getStaticProps(context) {
      const res = await fetch(`https://.../data`)
      const data = await res.json()
     
      if (!data) {
        return {
          notFound: true,
        }
      }
     
      return {
        props: { data }, // will be passed to the page component as props
      }
    }
[/code]

> **알아두면 좋아요**: [`fallback: false`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false) 모드에서는 `notFound`가 필요 없습니다. `getStaticPaths`가 반환한 경로만 사전 렌더링되기 때문입니다.

### `redirect`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#redirect)

`redirect` 객체를 사용하면 내부 또는 외부 리소스로 리디렉트할 수 있습니다. `{ destination: string, permanent: boolean }` 형태여야 합니다.

드물게 오래된 `HTTP` 클라이언트가 올바르게 리디렉트되도록 커스텀 상태 코드를 지정해야 할 수 있습니다. 이런 경우 `permanent` 대신 `statusCode` 속성을 사용할 수 있지만 **둘을 동시에 사용할 수는 없습니다**. `next.config.js`의 redirect와 마찬가지로 `basePath: false`를 설정할 수도 있습니다.
[code] 
    export async function getStaticProps(context) {
      const res = await fetch(`https://...`)
      const data = await res.json()
     
      if (!data) {
        return {
          redirect: {
            destination: '/',
            permanent: false,
            // statusCode: 301
          },
        }
      }
     
      return {
        props: { data }, // will be passed to the page component as props
      }
    }
[/code]

리디렉트가 빌드 시점에 이미 알려져 있다면 [`next.config.js`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)에 추가해야 합니다.

## Reading files: Use `process.cwd()`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#reading-files-use-processcwd)

`getStaticProps`에서는 파일 시스템에서 파일을 직접 읽을 수 있습니다.

이를 위해 파일의 전체 경로를 얻어야 합니다.

Next.js가 코드를 별도의 디렉터리로 컴파일하기 때문에 Pages Router와 경로가 달라지는 `__dirname`을 사용할 수 없습니다.

대신 Next.js가 실행되는 디렉터리를 반환하는 `process.cwd()`를 사용할 수 있습니다.
[code] 
    import { promises as fs } from 'fs'
    import path from 'path'
     
    // posts will be populated at build time by getStaticProps()
    function Blog({ posts }) {
      return (
        <ul>
          {posts.map((post) => (
            <li>
              <h3>{post.filename}</h3>
              <p>{post.content}</p>
            </li>
          ))}
        </ul>
      )
    }
     
    // This function gets called at build time on server-side.
    // It won't be called on client-side, so you can even do
    // direct database queries.
    export async function getStaticProps() {
      const postsDirectory = path.join(process.cwd(), 'posts')
      const filenames = await fs.readdir(postsDirectory)
     
      const posts = filenames.map(async (filename) => {
        const filePath = path.join(postsDirectory, filename)
        const fileContents = await fs.readFile(filePath, 'utf8')
     
        // Generally you would parse/transform the contents
        // For example you can transform markdown to HTML here
     
        return {
          filename,
          content: fileContents,
        }
      })
      // By returning { props: { posts } }, the Blog component
      // will receive `posts` as a prop at build time
      return {
        props: {
          posts: await Promise.all(posts),
        },
      }
    }
     
    export default Blog
[/code]

## Version History[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#version-history)

Version| Changes  
---|---  
`v13.4.0`| [App Router](https://nextjs.org/docs/app/getting-started/fetching-data)가 단순화된 데이터 패칭과 함께 안정화되었습니다.  
`v12.2.0`| [온디맨드 Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)이 안정화되었습니다.  
`v12.1.0`| [온디맨드 Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)이 베타로 추가되었습니다.  
`v10.0.0`| `locale`, `locales`, `defaultLocale`, `notFound` 옵션이 추가되었습니다.  
`v10.0.0`| `fallback: 'blocking'` 반환 옵션이 추가되었습니다.  
`v9.5.0`| [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)이 안정화되었습니다.  
`v9.3.0`| `getStaticProps`가 도입되었습니다.  
  
Was this helpful?

supported.

Send
