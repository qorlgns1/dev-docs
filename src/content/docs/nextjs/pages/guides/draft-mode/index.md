---
title: '가이드: 드래프트 모드'
description: '정적 생성은 페이지가 헤드리스 CMS에서 데이터를 가져올 때 유용합니다. 그러나 헤드리스 CMS에서 초안을 작성하면서 즉시 페이지에서 보고 싶다면 적합하지 않습니다. 이런 경우에는 Next.js가 빌드 시점이 아니라 요청 시점에 페이지를 렌더링하고, 게시본 대신 초안...'
---

# 가이드: 드래프트 모드 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/draft-mode

[페이지 라우터](https://nextjs.org/docs/pages)[가이드](https://nextjs.org/docs/pages/guides)드래프트 모드

페이지 복사

# Next.js에서 드래프트 모드로 콘텐츠 미리보기 방법

최종 업데이트 2026년 2월 20일

[페이지 문서](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)와 [데이터 패칭 문서](https://nextjs.org/docs/pages/building-your-application/data-fetching)에서는 `getStaticProps`와 `getStaticPaths`를 사용해 빌드 시점(**Static Generation**)에 페이지를 사전 렌더링하는 방법을 다뤘습니다.

정적 생성은 페이지가 헤드리스 CMS에서 데이터를 가져올 때 유용합니다. 그러나 헤드리스 CMS에서 초안을 작성하면서 즉시 페이지에서 보고 싶다면 적합하지 않습니다. 이런 경우에는 Next.js가 빌드 시점이 아니라 **요청 시점**에 페이지를 렌더링하고, 게시본 대신 초안 콘텐츠를 가져오길 원할 것입니다. 특정 상황에서만 정적 생성을 우회하도록 Next.js에 요청하게 됩니다.

Next.js에는 이 문제를 해결하는 **드래프트 모드** 기능이 있습니다. 사용 방법은 다음과 같습니다.

## 1단계: API 경로 생성 및 접근[](https://nextjs.org/docs/pages/guides/draft-mode#step-1-create-and-access-the-api-route)

> Next.js API 경로가 익숙하지 않다면 먼저 [API Routes 문서](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)를 살펴보세요.

먼저 **API 경로**를 만듭니다. 이름은 자유롭게 정할 수 있습니다(예: `pages/api/draft.ts`).

이 API 경로에서는 응답 객체에서 `setDraftMode`를 호출해야 합니다.
[code] 
    export default function handler(req, res) {
      // ...
      res.setDraftMode({ enable: true })
      // ...
    }
[/code]

이렇게 하면 드래프트 모드를 활성화하는 **쿠키**가 설정됩니다. 이 쿠키가 포함된 후속 요청은 **드래프트 모드**를 트리거하여 정적으로 생성된 페이지의 동작을 변경합니다(자세한 내용은 아래 참고).

브라우저에서 수동으로 아래와 같은 API 경로를 만들어 직접 접근해 볼 수도 있습니다:

pages/api/draft.ts
[code]
    // simple example for testing it manually from your browser.
    export default function handler(req, res) {
      res.setDraftMode({ enable: true })
      res.end('Draft mode is enabled')
    }
[/code]

브라우저 개발자 도구를 열고 `/api/draft`를 방문하면 `__prerender_bypass`라는 쿠키가 `Set-Cookie` 응답 헤더에 있는 것을 확인할 수 있습니다.

### 헤드리스 CMS에서 안전하게 접근하기[](https://nextjs.org/docs/pages/guides/draft-mode#securely-accessing-it-from-your-headless-cms)

실제로는 헤드리스 CMS에서 이 API 경로를 _안전하게_ 호출하고자 할 것입니다. 구체적인 단계는 사용하는 헤드리스 CMS에 따라 다르지만, 일반적으로 다음 단계를 따르면 됩니다.

아래 단계는 사용하는 헤드리스 CMS가 **사용자 지정 드래프트 URL** 설정을 지원한다고 가정합니다. 지원하지 않더라도 이 방법으로 드래프트 URL을 보호할 수 있지만, 직접 드래프트 URL을 구성해 접근해야 합니다.

**첫 번째**, 원하는 토큰 생성기를 사용해 **비밀 토큰 문자열**을 만듭니다. 이 비밀은 Next.js 앱과 헤드리스 CMS만 알고 있어야 하며, CMS에 접근 권한이 없는 사람이 드래프트 URL에 접근하는 것을 막습니다.

**두 번째**, 헤드리스 CMS가 사용자 지정 드래프트 URL을 지원한다면 아래 값을 드래프트 URL로 지정합니다. 드래프트 API 경로가 `pages/api/draft.ts`에 있다고 가정합니다.

터미널
[code]
    https://<your-site>/api/draft?secret=<token>&slug=<path>
[/code]

  * `<your-site>`은 배포 도메인입니다.
  * `<token>`에는 생성한 비밀 토큰을 넣습니다.
  * `<path>`는 보고 싶은 페이지의 경로입니다. 예를 들어 `/posts/foo`를 보고 싶다면 `&slug=/posts/foo`를 사용합니다.

헤드리스 CMS가 드래프트 URL에 변수를 포함하도록 허용한다면 CMS 데이터에 기반해 `<path>`를 동적으로 설정할 수도 있습니다. 예: `&slug=/posts/{entry.fields.slug}`

**마지막으로**, 드래프트 API 경로에서 다음을 수행합니다:

  * 비밀이 일치하는지와 `slug` 매개변수가 존재하는지 확인합니다(없다면 요청은 실패해야 합니다).
  *   * `res.setDraftMode`를 호출합니다.
  * 그런 다음 브라우저를 `slug`에 지정된 경로로 리디렉션합니다(아래 예시는 [307 리디렉션](https://developer.mozilla.org/docs/Web/HTTP/Status/307)을 사용).

[code] 
    export default async (req, res) => {
      // Check the secret and next parameters
      // This secret should only be known to this API route and the CMS
      if (req.query.secret !== 'MY_SECRET_TOKEN' || !req.query.slug) {
        return res.status(401).json({ message: 'Invalid token' })
      }
     
      // Fetch the headless CMS to check if the provided `slug` exists
      // getPostBySlug would implement the required fetching logic to the headless CMS
      const post = await getPostBySlug(req.query.slug)
     
      // If the slug doesn't exist prevent draft mode from being enabled
      if (!post) {
        return res.status(401).json({ message: 'Invalid slug' })
      }
     
      // Enable Draft Mode by setting the cookie
      res.setDraftMode({ enable: true })
     
      // Redirect to the path from the fetched post
      // We don't redirect to req.query.slug as that might lead to open redirect vulnerabilities
      res.redirect(post.slug)
    }
[/code]

성공하면 브라우저가 드래프트 모드 쿠키와 함께 보고 싶은 경로로 리디렉션됩니다.

## 2단계: `getStaticProps` 업데이트[](https://nextjs.org/docs/pages/guides/draft-mode#step-2-update-getstaticprops)

다음 단계는 드래프트 모드를 지원하도록 `getStaticProps`를 업데이트하는 것입니다.

`res.setDraftMode`로 쿠키가 설정된 상태에서 `getStaticProps`가 있는 페이지를 요청하면, `getStaticProps`는 빌드 시점이 아니라 **요청 시점**에 호출됩니다.

또한 `context.draftMode`가 `true`인 `context` 객체와 함께 호출됩니다.
[code] 
    export async function getStaticProps(context) {
      if (context.draftMode) {
        // dynamic data
      }
    }
[/code]

드래프트 API 경로에서 `res.setDraftMode`를 사용했으므로 `context.draftMode`는 `true`가 됩니다.

`getStaticPaths`도 사용하는 경우 `context.params`도 사용할 수 있습니다.

### 드래프트 데이터 가져오기[](https://nextjs.org/docs/pages/guides/draft-mode#fetch-draft-data)

`context.draftMode`에 따라 다른 데이터를 가져오도록 `getStaticProps`를 업데이트할 수 있습니다.

예를 들어 헤드리스 CMS가 드래프트 게시물용 다른 API 엔드포인트를 제공한다면 다음과 같이 엔드포인트 URL을 바꿀 수 있습니다:
[code] 
    export async function getStaticProps(context) {
      const url = context.draftMode
        ? 'https://draft.example.com'
        : 'https://production.example.com'
      const res = await fetch(url)
      // ...
    }
[/code]

이제 끝입니다! 헤드리스 CMS에서(또는 수동으로) `secret`과 `slug`를 포함한 드래프트 API 경로에 접근하면 드래프트 콘텐츠를 볼 수 있습니다. 게시하지 않고 초안을 업데이트하더라도 계속 확인할 수 있습니다.

헤드리스 CMS에서 드래프트 URL로 설정하거나 수동으로 접근하면 드래프트를 볼 수 있습니다.

터미널
[code]
    https://<your-site>/api/draft?secret=<token>&slug=<path>
[/code]

## 추가 정보[](https://nextjs.org/docs/pages/guides/draft-mode#more-details)

### 드래프트 모드 쿠키 지우기[](https://nextjs.org/docs/pages/guides/draft-mode#clear-the-draft-mode-cookie)

기본적으로 드래프트 모드 세션은 브라우저를 닫으면 종료됩니다.

드래프트 모드 쿠키를 수동으로 지우려면 `setDraftMode({ enable: false })`를 호출하는 API 경로를 만듭니다:

pages/api/disable-draft.ts
[code]
    export default function handler(req, res) {
      res.setDraftMode({ enable: false })
    }
[/code]

그런 다음 `/api/disable-draft`로 요청을 보내 API 경로를 호출합니다. [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link)로 이 경로를 호출하는 경우 프리패치 시 쿠키가 실수로 삭제되는 것을 방지하려면 `prefetch={false}`를 전달해야 합니다.

### `getServerSideProps`와 함께 작동[](https://nextjs.org/docs/pages/guides/draft-mode#works-with-getserversideprops)

드래프트 모드는 `getServerSideProps`와 함께 작동하며, [`context`](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#context-parameter) 객체의 `draftMode` 키로 제공됩니다.

> **알아두면 좋아요**: 드래프트 모드를 사용할 때는 `Cache-Control` 헤더를 설정하면 우회할 수 없으므로 권장하지 않습니다. 대신 [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)을 사용하세요.

### API Routes와 함께 작동[](https://nextjs.org/docs/pages/guides/draft-mode#works-with-api-routes)

API Routes는 요청 객체에서 `draftMode`에 접근할 수 있습니다. 예:
[code] 
    export default function myApiRoute(req, res) {
      if (req.draftMode) {
        // get draft data
      }
    }
[/code]

### `next build`마다 고유[](https://nextjs.org/docs/pages/guides/draft-mode#unique-per-next-build)

`next build`를 실행할 때마다 새로운 바이패스 쿠키 값이 생성됩니다.

이렇게 하면 바이패스 쿠키를 추측할 수 없습니다.

> **알아두면 좋아요**: 로컬에서 HTTP로 드래프트 모드를 테스트하려면 브라우저가 타사 쿠키와 로컬 스토리지 접근을 허용해야 합니다.

도움이 되었나요?

지원됨.

보내기
