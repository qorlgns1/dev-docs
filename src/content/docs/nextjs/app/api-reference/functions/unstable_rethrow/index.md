---
title: '함수: unstable_rethrow'
description: '이 기능은 현재 불안정하며 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. GitHub에 피드백을 공유해 주세요.'
---

# 함수: unstable_rethrow | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow

# unstable_rethrow

이 기능은 현재 불안정하며 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에 피드백을 공유해 주세요.

마지막 업데이트: 2026년 2월 20일

`unstable_rethrow`는 애플리케이션 코드에서 발생한 오류를 처리하려다 Next.js 내부 오류를 잡아버리는 상황을 피하는 데 사용할 수 있습니다.

예를 들어 `notFound` 함수를 호출하면 내부 Next.js 오류가 발생하고 [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) 컴포넌트가 렌더링됩니다. 그러나 `try/catch` 문의 `try` 블록에서 사용하면 오류가 포착되어 `not-found.js` 렌더링이 차단됩니다:

@/app/ui/component.tsx
[code]
    import { notFound } from 'next/navigation'

    export default async function Page() {
      try {
        const post = await fetch('https://.../posts/1').then((res) => {
          if (res.status === 404) notFound()
          if (!res.ok) throw new Error(res.statusText)
          return res.json()
        })
      } catch (err) {
        console.error(err)
      }
    }
[/code]

`unstable_rethrow` API를 사용하면 내부 오류를 다시 던져 예상된 동작을 이어갈 수 있습니다:

@/app/ui/component.tsx
[code]
    import { notFound, unstable_rethrow } from 'next/navigation'

    export default async function Page() {
      try {
        const post = await fetch('https://.../posts/1').then((res) => {
          if (res.status === 404) notFound()
          if (!res.ok) throw new Error(res.statusText)
          return res.json()
        })
      } catch (err) {
        unstable_rethrow(err)
        console.error(err)
      }
    }
[/code]

다음 Next.js API는 오류를 던지는 방식에 의존하므로 다시 던져서 Next.js 자체가 처리하도록 해야 합니다.

  * [`notFound()`](https://nextjs.org/docs/app/api-reference/functions/not-found)
  * [`redirect()`](https://nextjs.org/docs/app/guides/redirecting#redirect-function)
  * [`permanentRedirect()`](https://nextjs.org/docs/app/guides/redirecting#permanentredirect-function)

라우트 세그먼트가 정적이 아니면 오류를 던지도록 표시된 경우, Dynamic API 호출도 마찬가지로 개발자가 잡지 말아야 하는 오류를 던집니다. Partial Prerendering(PPR) 역시 이 동작에 영향을 줍니다. 해당 API는 다음과 같습니다.

  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)
  * `fetch(..., { cache: 'no-store' })`
  * `fetch(..., { next: { revalidate: 0 } })`

> **알아두면 좋아요** :
>
>   * 이 메서드는 catch 블록의 가장 위에서 오류 객체 하나만 인자로 전달해 호출하세요. Promise의 `.catch` 핸들러에서도 사용할 수 있습니다.
>   * 예외를 던지는 API 호출을 캡슐화해 **호출자**가 예외를 처리하도록 만들면 `unstable_rethrow` 사용을 피할 수 있습니다.
>   * 잡힌 예외에 애플리케이션 오류와 프레임워크 제어 예외(`redirect()`, `notFound()` 등)가 섞여 있을 때만 `unstable_rethrow`를 사용하세요.
>   * 리소스 정리(인터벌, 타이머 등)는 `unstable_rethrow` 호출 전에 수행하거나 `finally` 블록에서 처리해야 합니다.
>

보내기
