---
title: '가이드: Draft Mode'
description: '이 문서는 Draft Mode를 활성화하고 사용하는 방법을 안내합니다.'
---

# 가이드: Draft Mode | Next.js

출처 URL: https://nextjs.org/docs/app/guides/draft-mode

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)Draft Mode

# Next.js에서 Draft Mode로 콘텐츠 미리 보는 방법

마지막 업데이트 2026년 2월 20일

**Draft Mode**를 사용하면 헤드리스 CMS의 초안 콘텐츠를 Next.js 애플리케이션에서 미리 볼 수 있습니다. 이는 정적 페이지를 빌드 시점에 생성하는 경우 특히 유용하며, [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 전환하여 사이트 전체를 다시 빌드하지 않고도 초안 변경 사항을 확인할 수 있습니다.

이 문서는 Draft Mode를 활성화하고 사용하는 방법을 안내합니다.

## 1단계: Route Handler 만들기[](https://nextjs.org/docs/app/guides/draft-mode#step-1-create-a-route-handler)

[Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)를 만듭니다. 이름은 자유롭게 정할 수 있으며 예를 들어 `app/api/draft/route.ts`가 있습니다.

app/api/draft/route.ts

JavaScriptTypeScript
[code]
    export async function GET(request: Request) {
      return new Response('')
    }
[/code]

그런 다음 [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode) 함수를 가져와 `enable()` 메서드를 호출합니다.

app/api/draft/route.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'

    export async function GET(request: Request) {
      const draft = await draftMode()
      draft.enable()
      return new Response('Draft mode is enabled')
    }
[/code]

이렇게 하면 Draft Mode를 활성화하는 **쿠키**가 설정됩니다. 이 쿠키가 포함된 이후 요청은 Draft Mode를 트리거하여 정적으로 생성된 페이지의 동작을 변경합니다.

브라우저 개발자 도구를 열어 `/api/draft`에 직접 방문하면 이를 수동으로 테스트할 수 있습니다. `__prerender_bypass`라는 이름의 쿠키가 포함된 `Set-Cookie` 응답 헤더를 확인하세요.

## 2단계: 헤드리스 CMS에서 Route Handler에 접근하기[](https://nextjs.org/docs/app/guides/draft-mode#step-2-access-the-route-handler-from-your-headless-cms)

> 다음 단계는 사용 중인 헤드리스 CMS가 **사용자 지정 초안 URL**을 설정할 수 있다고 가정합니다. 그렇지 않더라도 이 방법으로 초안 URL을 보호할 수 있지만, 초안 URL을 직접 구성하고 접근해야 합니다. 구체적인 절차는 사용하는 헤드리스 CMS에 따라 달라집니다.

헤드리스 CMS에서 Route Handler에 안전하게 접근하려면 다음을 수행하세요.

  1. 원하는 토큰 생성기를 사용해 **비밀 토큰 문자열**을 만듭니다. 이 비밀 값은 Next.js 앱과 헤드리스 CMS만 알고 있어야 합니다.
  2. 헤드리스 CMS가 사용자 지정 초안 URL을 지원한다면 초안 URL을 지정합니다(여기서는 Route Handler가 `app/api/draft/route.ts`에 있다고 가정). 예시는 다음과 같습니다.

Terminal
[code]
    https://<your-site>/api/draft?secret=<token>&slug=<path>
[/code]

>   * `<your-site>`에는 배포 도메인을 입력합니다.
>   * `<token>`에는 생성한 비밀 토큰을 넣습니다.
>   * `<path>`에는 확인하려는 페이지의 경로를 넣습니다. 예를 들어 `/posts/one`을 보고 싶다면 `&slug=/posts/one`을 사용합니다.
>

>
> 일부 헤드리스 CMS는 `<path>`를 CMS 데이터에 따라 동적으로 설정할 수 있도록 초안 URL에 변수를 포함하는 기능을 제공합니다. 예: `&slug=/posts/{entry.fields.slug}`

  3. Route Handler에서 비밀 값이 일치하는지, `slug` 매개변수가 존재하는지 확인하고(없으면 요청을 실패시켜야 합니다) `draftMode.enable()`을 호출해 쿠키를 설정한 뒤, `slug`로 지정된 경로로 브라우저를 리디렉션합니다:

app/api/draft/route.ts

JavaScriptTypeScript
[code]
    import { draftMode } from 'next/headers'
    import { redirect } from 'next/navigation'

    export async function GET(request: Request) {
      // Parse query string parameters
      const { searchParams } = new URL(request.url)
      const secret = searchParams.get('secret')
      const slug = searchParams.get('slug')

      // Check the secret and next parameters
      // This secret should only be known to this Route Handler and the CMS
      if (secret !== 'MY_SECRET_TOKEN' || !slug) {
        return new Response('Invalid token', { status: 401 })
      }

      // Fetch the headless CMS to check if the provided `slug` exists
      // getPostBySlug would implement the required fetching logic to the headless CMS
      const post = await getPostBySlug(slug)

      // If the slug doesn't exist prevent draft mode from being enabled
      if (!post) {
        return new Response('Invalid slug', { status: 401 })
      }

      // Enable Draft Mode by setting the cookie
      const draft = await draftMode()
      draft.enable()

      // Redirect to the path from the fetched post
      // We don't redirect to searchParams.slug as that might lead to open redirect vulnerabilities
      redirect(post.slug)
    }
[/code]

성공하면 브라우저가 Draft Mode 쿠키와 함께 원하는 경로로 리디렉션됩니다.

## 3단계: 초안 콘텐츠 미리 보기[](https://nextjs.org/docs/app/guides/draft-mode#step-3-preview-the-draft-content)

다음 단계는 페이지에서 `draftMode().isEnabled` 값을 확인하도록 업데이트하는 것입니다.

쿠키가 설정된 페이지를 요청하면 데이터가 **빌드 시점**이 아니라 **요청 시점**에 가져와집니다.

또한 `isEnabled` 값은 `true`가 됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    // page that fetches data
    import { draftMode } from 'next/headers'

    async function getData() {
      const { isEnabled } = await draftMode()

      const url = isEnabled
        ? 'https://draft.example.com'
        : 'https://production.example.com'

      const res = await fetch(url)

      return res.json()
    }

    export default async function Page() {
      const { title, desc } = await getData()

      return (
        <main>
          <h1>{title}</h1>
          <p>{desc}</p>
        </main>
      )
    }
[/code]

헤드리스 CMS에서(또는 URL을 이용해 수동으로) `secret`과 `slug`가 포함된 초안 Route Handler에 접근하면 이제 초안 콘텐츠를 볼 수 있습니다. 초안을 게시하지 않고 업데이트하더라도 초안 상태를 계속 확인할 수 있습니다.

## 다음 단계

Draft Mode 사용 방법에 대한 추가 정보는 API 레퍼런스를 참고하세요.

- [draftMode](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  - 함수의 API 레퍼런스.

보내기
