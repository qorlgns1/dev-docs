---
title: '가이드: Preview Mode'
description: '이는 레거시 API이며 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.'
---

# 가이드: Preview Mode | Next.js

Source URL: https://nextjs.org/docs/pages/guides/preview-mode

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Preview Mode

Copy page

# Preview Mode를 활용해 Next.js에서 콘텐츠 미리 보기

이는 레거시 API이며 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.

Last updated February 20, 2026

> **Note** : 이 기능은 [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)로 대체되었습니다.

Examples

  * [Agility CMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-agilitycms) ([Demo](https://next-blog-agilitycms.vercel.app/))
  * [Builder.io Example](https://github.com/vercel/next.js/tree/canary/examples/cms-builder-io) ([Demo](https://cms-builder-io.vercel.app/))
  * [ButterCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-buttercms) ([Demo](https://next-blog-buttercms.vercel.app/))
  * [Contentful Example](https://github.com/vercel/next.js/tree/canary/examples/cms-contentful) ([Demo](https://app-router-contentful.vercel.app/))
  * [Cosmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-cosmic) ([Demo](https://next-blog-cosmic.vercel.app/))
  * [DatoCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-datocms) ([Demo](https://next-blog-datocms.vercel.app/))
  * [DotCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-dotcms) ([Demo](https://nextjs-dotcms-blog.vercel.app/))
  * [Drupal Example](https://github.com/vercel/next.js/tree/canary/examples/cms-drupal) ([Demo](https://cms-drupal.vercel.app/))
  * [Enterspeed Example](https://github.com/vercel/next.js/tree/canary/examples/cms-enterspeed) ([Demo](https://next-blog-demo.enterspeed.com/))
  * [GraphCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-graphcms) ([Demo](https://next-blog-graphcms.vercel.app/))
  * [Keystone Example](https://github.com/vercel/next.js/tree/canary/examples/cms-keystonejs-embedded) ([Demo](https://nextjs-keystone-demo.vercel.app/))
  * [Kontent.ai Example](https://github.com/vercel/next.js/tree/canary/examples/cms-kontent-ai) ([Demo](https://next-blog-kontent-ai.vercel.app/))
  * [Makeswift Example](https://github.com/vercel/next.js/tree/canary/examples/cms-makeswift) ([Demo](https://nextjs-makeswift-example.vercel.app/))
  * [Plasmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-plasmic) ([Demo](https://nextjs-plasmic-example.vercel.app/))
  * [Prepr Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prepr) ([Demo](https://next-blog-prepr.vercel.app/))
  * [Prismic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prismic) ([Demo](https://next-blog-prismic.vercel.app/))
  * [Sanity Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sanity) ([Demo](https://next-blog.sanity.build/))
  * [Sitecore XM Cloud Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sitecore-xmcloud) ([Demo](https://vercel-sitecore-xmcloud-demo.vercel.app/))
  * [Storyblok Example](https://github.com/vercel/next.js/tree/canary/examples/cms-storyblok) ([Demo](https://next-blog-storyblok.vercel.app/))
  * [Strapi Example](https://github.com/vercel/next.js/tree/canary/examples/cms-strapi) ([Demo](https://next-blog-strapi.vercel.app/))
  * [TakeShape Example](https://github.com/vercel/next.js/tree/canary/examples/cms-takeshape) ([Demo](https://next-blog-takeshape.vercel.app/))
  * [Tina Example](https://github.com/vercel/next.js/tree/canary/examples/cms-tina) ([Demo](https://cms-tina-example.vercel.app/))
  * [Umbraco Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco) ([Demo](https://nextjs-umbraco-sample-blog.vercel.app/))
  * [Umbraco Heartcore Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco-heartcore) ([Demo](https://next-blog-umbraco-heartcore.vercel.app/))
  * [Webiny Example](https://github.com/vercel/next.js/tree/canary/examples/cms-webiny) ([Demo](https://webiny-headlesscms-nextjs-example.vercel.app/))
  * [WordPress Example](https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress) ([Demo](https://next-blog-wordpress.vercel.app/))
  * [Blog Starter Example](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([Demo](https://next-blog-starter.vercel.app/))

[Pages 문서](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)와 [Data Fetching 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching)에서는 `getStaticProps`와 `getStaticPaths`를 사용해 빌드 시점(**Static Generation**)에 페이지를 사전 렌더링하는 방법을 다뤘습니다.

Static Generation은 페이지가 헤드리스 CMS에서 데이터를 가져올 때 유용합니다. 하지만 헤드리스 CMS에서 초안을 작성하고 곧바로 페이지에서 **미리 보기**를 하고 싶다면 적절하지 않습니다. 이런 경우 Next.js가 빌드 시점이 아닌 **요청 시점**에 페이지를 렌더링하고 게시된 콘텐츠 대신 초안 콘텐츠를 가져오길 원하게 됩니다. 오직 이 특정 상황에서만 Static Generation을 우회해야 합니다.

Next.js에는 이 문제를 해결하는 **Preview Mode** 기능이 있습니다. 사용 방법은 다음과 같습니다.

## Step 1: 미리 보기 API 경로 생성 및 접근[](https://nextjs.org/docs/pages/guides/preview-mode#step-1-create-and-access-a-preview-api-route)

> Next.js API Routes가 익숙하지 않다면 먼저 [API Routes 문서](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)를 확인하세요.

먼저 **preview API route**를 만듭니다. 이름은 자유롭게 정할 수 있습니다. 예: `pages/api/preview.js` (TypeScript 사용 시 `.ts`).

이 API route에서 응답 객체의 `setPreviewData`를 호출해야 합니다. `setPreviewData`에 전달하는 인수는 객체여야 하며, 이후 `getStaticProps`에서 사용할 수 있습니다(뒤에서 설명). 지금은 `{}`를 사용하겠습니다.
```
    export default function handler(req, res) {
      // ...
      res.setPreviewData({})
      // ...
    }
```

`res.setPreviewData`는 브라우저에 일부 **쿠키**를 설정하고 preview mode를 활성화합니다. 이 쿠키가 포함된 Next.js 요청은 **preview mode**로 간주되며, 정적으로 생성된 페이지의 동작이 달라집니다(자세한 내용은 뒤에서 설명).

아래와 같은 API route를 만들고 브라우저에서 직접 접근해 수동으로 테스트할 수 있습니다:

pages/api/preview.js
```
    // 브라우저에서 수동으로 테스트하기 위한 간단한 예제.
    export default function handler(req, res) {
      res.setPreviewData({})
      res.end('Preview mode enabled')
    }
```

브라우저 개발자 도구를 열고 `/api/preview`를 방문하면 이 요청에 `__prerender_bypass`와 `__next_preview_data` 쿠키가 설정되는 것을 확인할 수 있습니다.

### Headless CMS에서 안전하게 접근하기[](https://nextjs.org/docs/pages/guides/preview-mode#securely-accessing-it-from-your-headless-cms)

실무에서는 헤드리스 CMS에서 이 API route를 _안전하게_ 호출하길 원합니다. 구체적인 단계는 사용하는 CMS에 따라 다르지만, 공통으로 적용할 수 있는 단계는 다음과 같습니다.

아래 단계는 사용 중인 헤드리스 CMS가 **custom preview URL** 설정을 지원한다고 가정합니다. 지원하지 않는 경우에도 이 방법으로 preview URL을 보호할 수 있지만, preview URL을 직접 구성하고 접근해야 합니다.

**첫째**, 원하는 토큰 생성기를 사용해 **secret token 문자열**을 만듭니다. 이 secret은 Next.js 앱과 헤드리스 CMS만 알고 있어야 합니다. 이를 통해 CMS에 접근할 수 없는 사람이 preview URL을 열람하지 못하도록 합니다.

**둘째**, 헤드리스 CMS가 custom preview URL 설정을 지원한다면 preview URL로 아래 값을 지정합니다. preview API route가 `pages/api/preview.js`에 있다고 가정합니다.

Terminal
```
    https://<your-site>/api/preview?secret=<token>&slug=<path>
```

  * `<your-site>`에는 배포 도메인을 입력합니다.
  * `<token>`에는 앞에서 생성한 secret token을 넣습니다.
  * `<path>`에는 미리 보려는 페이지 경로를 적습니다. `/posts/foo`를 미리 보려면 `&slug=/posts/foo`를 사용하면 됩니다.

헤드리스 CMS에서 preview URL에 변수를 포함할 수 있도록 지원한다면 `<path>`를 CMS 데이터 기반으로 동적으로 설정할 수 있습니다. 예: `&slug=/posts/{entry.fields.slug}`

**마지막으로**, preview API route에서 다음을 수행합니다:

  * secret이 일치하는지와 `slug` 파라미터가 존재하는지 확인합니다(없다면 요청을 실패시키기).
  *   * `res.setPreviewData`를 호출합니다.
  * 그런 다음 브라우저를 `slug`에 지정된 경로로 리디렉션합니다. (아래 예제는 [307 redirect](https://developer.mozilla.org/docs/Web/HTTP/Status/307)를 사용합니다.)

```
    export default async (req, res) => {
      // Check the secret and next parameters
      // This secret should only be known to this API route and the CMS
      if (req.query.secret !== 'MY_SECRET_TOKEN' || !req.query.slug) {
        return res.status(401).json({ message: 'Invalid token' })
      }

      // Fetch the headless CMS to check if the provided `slug` exists
      // getPostBySlug would implement the required fetching logic to the headless CMS
      const post = await getPostBySlug(req.query.slug)

      // If the slug doesn't exist prevent preview mode from being enabled
      if (!post) {
        return res.status(401).json({ message: 'Invalid slug' })
      }

      // Enable Preview Mode by setting the cookies
      res.setPreviewData({})

      // Redirect to the path from the fetched post
      // We don't redirect to req.query.slug as that might lead to open redirect vulnerabilities
      res.redirect(post.slug)
    }
```

성공하면 브라우저는 preview mode 쿠키가 설정된 상태로 미리 보고 싶은 경로로 리디렉션됩니다.

## Step 2: `getStaticProps` 업데이트[](https://nextjs.org/docs/pages/guides/preview-mode#step-2-update-getstaticprops)

다음 단계는 `getStaticProps`가 preview mode를 지원하도록 수정하는 것입니다.

preview mode 쿠키(`res.setPreviewData`를 통해 설정)를 가진 상태로 `getStaticProps`가 있는 페이지를 요청하면 `getStaticProps`는 **빌드 시점** 대신 **요청 시점**에 호출됩니다.

또한 `context` 객체와 함께 호출되며, 여기에는 다음이 포함됩니다:

  * `context.preview` 값은 `true`입니다.
  * `context.previewData`는 `setPreviewData`에 전달했던 인수와 동일합니다.

```
    export async function getStaticProps(context) {
      // If you request this page with the preview mode cookies set:
      //
      // - context.preview will be true
      // - context.previewData will be the same as
      //   the argument used for `setPreviewData`.
    }
```

preview API route에서 `res.setPreviewData({})`를 사용했으므로 `context.previewData`는 `{}`입니다. 필요하다면 preview API route에서 `getStaticProps`로 세션 정보를 전달하는 데 활용할 수 있습니다.

`getStaticPaths`도 사용 중이라면 `context.params`도 함께 제공됩니다.

### 미리 보기 데이터 가져오기[](https://nextjs.org/docs/pages/guides/preview-mode#fetch-preview-data)

`context.preview`나 `context.previewData`에 따라 다른 데이터를 가져오도록 `getStaticProps`를 업데이트할 수 있습니다.

예를 들어 헤드리스 CMS에 초안 게시물 전용 API endpoint가 있다면, 아래와 같이 `context.preview`를 활용해 API endpoint URL을 수정할 수 있습니다:
```
    export async function getStaticProps(context) {
      // If context.preview is true, append "/preview" to the API endpoint
      // to request draft data instead of published data. This will vary
      // based on which headless CMS you're using.
      const res = await fetch(`https://.../${context.preview ? 'preview' : ''}`)
      // ...
    }
```

이게 전부입니다! 헤드리스 CMS에서 또는 수동으로 프리뷰 API 경로(`secret` 및 `slug` 포함)에 접근하면 이제 프리뷰 콘텐츠를 볼 수 있습니다. 게시하지 않고 초안을 업데이트해도 초안을 미리 볼 수 있습니다.

이 URL을 헤드리스 CMS의 프리뷰 URL로 설정하거나 수동으로 접근하면 프리뷰를 확인할 수 있습니다.

터미널
```
    https://<your-site>/api/preview?secret=<token>&slug=<path>
```

## 자세한 내용[](https://nextjs.org/docs/pages/guides/preview-mode#more-details)

> **알아두면 좋아요** : 렌더링 중 `next/router`가 `isPreview` 플래그를 노출하므로 [router object docs](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object)에서 자세한 내용을 확인하세요.

### 프리뷰 모드 지속 시간 지정[](https://nextjs.org/docs/pages/guides/preview-mode#specify-the-preview-mode-duration)

`setPreviewData`는 옵션 객체를 두 번째 인자로 선택적으로 받을 수 있습니다. 다음 키를 허용합니다:

  * `maxAge`: 프리뷰 세션이 유지될 시간(초)을 지정합니다.
  * `path`: 쿠키를 적용할 경로를 지정합니다. 기본값은 `/`로 모든 경로에서 프리뷰 모드를 활성화합니다.

```
    setPreviewData(data, {
      maxAge: 60 * 60, // The preview mode cookies expire in 1 hour
      path: '/about', // The preview mode cookies apply to paths with /about
    })
```

### 프리뷰 모드 쿠키 지우기[](https://nextjs.org/docs/pages/guides/preview-mode#clear-the-preview-mode-cookies)

기본적으로 프리뷰 모드 쿠키에는 만료 날짜가 설정되지 않으므로 브라우저를 닫으면 프리뷰 세션이 종료됩니다.

프리뷰 모드 쿠키를 수동으로 지우려면 `clearPreviewData()`를 호출하는 API 경로를 만듭니다:

pages/api/clear-preview-mode-cookies.js
```
    export default function handler(req, res) {
      res.clearPreviewData({})
    }
```

그런 다음 `/api/clear-preview-mode-cookies`에 요청을 보내 API 경로를 호출하세요. [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link)를 사용해 이 경로를 호출하는 경우 링크 프리페칭 중 `clearPreviewData`가 호출되지 않도록 `prefetch={false}`를 전달해야 합니다.

`setPreviewData` 호출에서 경로를 지정했다면 동일한 경로를 `clearPreviewData`에도 전달해야 합니다:

pages/api/clear-preview-mode-cookies.js
```
    export default function handler(req, res) {
      const { path } = req.query

      res.clearPreviewData({ path })
    }
```

### `previewData` 크기 제한[](https://nextjs.org/docs/pages/guides/preview-mode#previewdata-size-limits)

`setPreviewData`에 객체를 전달하고 이를 `getStaticProps`에서 사용할 수 있습니다. 그러나 데이터가 쿠키에 저장되므로 크기 제한이 있습니다. 현재 프리뷰 데이터는 2KB로 제한됩니다.

### `getServerSideProps`와 함께 동작[](https://nextjs.org/docs/pages/guides/preview-mode#works-with-getserversideprops)

프리뷰 모드는 `getServerSideProps`에서도 동작하며, `preview`와 `previewData`가 포함된 `context` 객체에서도 사용할 수 있습니다.

> **알아두면 좋아요** : 프리뷰 모드를 사용할 때는 우회할 수 없으므로 `Cache-Control` 헤더를 설정하지 마세요. 대신 [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)을 사용하는 것이 좋습니다.

### API 경로와 함께 동작[](https://nextjs.org/docs/pages/guides/preview-mode#works-with-api-routes)

API 경로는 요청 객체에서 `preview`와 `previewData`에 접근할 수 있습니다. 예:

```
    export default function myApiRoute(req, res) {
      const isPreview = req.preview
      const previewData = req.previewData
      // ...
    }
```

### `next build`마다 고유[](https://nextjs.org/docs/pages/guides/preview-mode#unique-per-next-build)

`next build`가 완료될 때마다 bypass 쿠키 값과 `previewData`를 암호화하는 개인 키가 바뀝니다. 이를 통해 bypass 쿠키가 추측되지 않도록 보장합니다.

> **알아두면 좋아요** : HTTP 환경에서 로컬로 프리뷰 모드를 테스트하려면 브라우저에서 서드파티 쿠키와 로컬 스토리지 접근을 허용해야 합니다.

보내기