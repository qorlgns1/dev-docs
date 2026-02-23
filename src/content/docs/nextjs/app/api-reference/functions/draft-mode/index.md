---
title: '함수: draftMode'
description: '는 Server Component에서 Draft Mode가 활성화되어 있는지 확인하고, Draft Mode를 활성화·비활성화할 수 있는 async 함수입니다.'
---

# 함수: draftMode | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/functions/draft-mode

# draftMode

마지막 업데이트 2026년 2월 20일

`draftMode`는 [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 Draft Mode가 활성화되어 있는지 확인하고, [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)를 활성화·비활성화할 수 있는 **async** 함수입니다.

app/page.ts

JavaScriptTypeScript
```
    import { draftMode } from 'next/headers'

    export default async function Page() {
      const { isEnabled } = await draftMode()
    }
```

## 참고[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#reference)

다음 메서드와 속성을 사용할 수 있습니다:

Method| Description
---|---
`isEnabled`| Draft Mode가 활성화되어 있는지 나타내는 불리언 값입니다.
`enable()`| 쿠키(`__prerender_bypass`)를 설정하여 Route Handler에서 Draft Mode를 활성화합니다.
`disable()`| 쿠키를 삭제하여 Route Handler에서 Draft Mode를 비활성화합니다.

## 알아두기[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#good-to-know)

  * `draftMode`는 프로미스를 반환하는 **비동기** 함수이므로 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 14 버전 및 그 이전 버전에서 `draftMode`는 동기 함수였습니다. 하위 호환을 돕기 위해 Next.js 15에서도 동기식으로 접근할 수 있지만, 향후 이 동작은 지원 중단될 예정입니다.
  * `next build`를 실행할 때마다 새로운 바이패스 쿠키 값이 생성되어 쿠키가 추측되지 않도록 합니다.
  * HTTP 환경에서 Draft Mode를 로컬로 테스트하려면 브라우저가 서드파티 쿠키와 로컬 스토리지 접근을 허용해야 합니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#examples)

### Draft Mode 활성화[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#enabling-draft-mode)

Draft Mode를 활성화하려면 새 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)를 만들고 `enable()` 메서드를 호출합니다:

app/draft/route.ts

JavaScriptTypeScript
```
    import { draftMode } from 'next/headers'

    export async function GET(request: Request) {
      const draft = await draftMode()
      draft.enable()
      return new Response('Draft mode is enabled')
    }
```

### Draft Mode 비활성화[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#disabling-draft-mode)

기본적으로 Draft Mode 세션은 브라우저를 닫으면 종료됩니다.

Draft Mode를 수동으로 비활성화하려면 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 `disable()` 메서드를 호출합니다:

app/draft/route.ts

JavaScriptTypeScript
```
    import { draftMode } from 'next/headers'

    export async function GET(request: Request) {
      const draft = await draftMode()
      draft.disable()
      return new Response('Draft mode is disabled')
    }
```

이후 Route Handler를 호출하도록 요청을 전송합니다. [`<Link>` 컴포넌트](https://nextjs.org/docs/app/api-reference/components/link)를 사용해 라우트를 호출하는 경우, 사전 가져오기 시 쿠키가 실수로 삭제되는 것을 막기 위해 반드시 `prefetch={false}`를 전달해야 합니다.

### Draft Mode 활성화 여부 확인[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#checking-if-draft-mode-is-enabled)

Server Component에서 `isEnabled` 속성으로 Draft Mode가 활성화되어 있는지 확인할 수 있습니다:

app/page.ts

JavaScriptTypeScript
```
    import { draftMode } from 'next/headers'

    export default async function Page() {
      const { isEnabled } = await draftMode()
      return (
        <main>
          <h1>My Blog Post</h1>
          <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
        </main>
      )
    }
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#version-history)

Version| Changes
---|---
`v15.0.0-RC`| `draftMode`가 이제 async 함수입니다. [코드 변환 도구](https://nextjs.org/docs/app/guides/upgrading/codemods#150)가 제공됩니다.
`v13.4.0`| `draftMode`가 도입되었습니다.

## 다음 단계

이 단계별 가이드를 통해 Draft Mode 사용 방법을 알아보세요.

- [드래프트 모드](https://nextjs.org/docs/app/guides/draft-mode)
  - Draft ModeNext.js에는 정적 페이지와 동적 페이지 간 전환을 위한 draft mode가 있습니다. App Router로 동작 방식을 여기에서 배울 수 있습니다.

보내기