---
title: '파일 시스템 규칙: 병렬 라우트'
description: 'Parallel Routes는 동일한 레이아웃 안에서 하나 이상의 페이지를 동시에 또는 조건부로 렌더링할 수 있게 해줍니다. 대시보드나 소셜 사이트의 피드처럼 매우 동적인 앱 섹션에 유용합니다.'
---

# 파일 시스템 규칙: 병렬 라우트 | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)Parallel Routes

Copy page

# Parallel Routes

마지막 업데이트 2026년 2월 20일

Parallel Routes는 동일한 레이아웃 안에서 하나 이상의 페이지를 동시에 또는 조건부로 렌더링할 수 있게 해줍니다. 대시보드나 소셜 사이트의 피드처럼 매우 동적인 앱 섹션에 유용합니다.

예를 들어, 대시보드를 생각해 보면 `team` 페이지와 `analytics` 페이지를 동시에 렌더링하기 위해 병렬 라우트를 사용할 수 있습니다.

## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#convention)

### Slots[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots)

병렬 라우트는 이름이 있는 **slot**으로 만들어집니다. slot은 `@folder` 규칙으로 정의됩니다. 예를 들어, 다음과 같은 파일 구조는 `@analytics`와 `@team` 두 개의 slot을 정의합니다:

slot은 공유 부모 레이아웃에 props로 전달됩니다. 위 예시에서는 `app/layout.js`의 컴포넌트가 이제 `@analytics`와 `@team` slot props를 받아 `children` prop과 나란히 병렬로 렌더링할 수 있습니다:

app/layout.tsx

JavaScriptTypeScript
```
    export default function Layout({
      children,
      team,
      analytics,
    }: {
      children: React.ReactNode
      analytics: React.ReactNode
      team: React.ReactNode
    }) {
      return (
        <>
          {children}
          {team}
          {analytics}
        </>
      )
    }
```

하지만 slot은 **라우트 세그먼트가 아니며** URL 구조에 영향을 주지 않습니다. 예를 들어, `/@analytics/views`의 URL은 `@analytics`가 slot이므로 `/views`가 됩니다. slot은 일반 [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) 컴포넌트와 결합되어 라우트 세그먼트에 연결된 최종 페이지를 형성합니다. 이 때문에 동일한 라우트 세그먼트 수준에서 [static](https://nextjs.org/docs/app/guides/caching#static-rendering) slot과 [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) slot을 따로 가질 수 없습니다. 한 slot이 dynamic이면 해당 수준의 모든 slot이 dynamic이어야 합니다.

> **알아두면 좋아요** :
>
>   * `children` prop은 폴더에 매핑할 필요가 없는 암묵적인 slot입니다. 즉, `app/page.js`는 `app/@children/page.js`와 동일합니다.
>

### `default.js`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs)

초기 로드나 전체 페이지 새로고침 시 일치하지 않는 slot에 대한 폴백을 렌더링하려면 `default.js` 파일을 정의할 수 있습니다.

다음 폴더 구조를 생각해 보세요. `@team` slot에는 `/settings` 페이지가 있지만 `@analytics`에는 없습니다.

`/settings`로 이동하면 `@team` slot은 `/settings` 페이지를 렌더링하면서 `@analytics` slot의 현재 활성 페이지를 유지합니다.

새로고침 시 Next.js는 `@analytics`에 대해 `default.js`를 렌더링합니다. `default.js`가 없으면 대신 `404`가 렌더링됩니다.

또한 `children`이 암묵적 slot이므로, Next.js가 부모 페이지의 활성 상태를 복구할 수 없을 때 `children`에 대한 폴백을 렌더링하도록 `default.js` 파일을 만들어야 합니다.

## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#behavior)

기본적으로 Next.js는 각 slot의 활성 _상태_(또는 서브페이지)를 추적합니다. 그러나 slot 안에 렌더링되는 내용은 탐색 유형에 따라 달라집니다:

  * [**Soft Navigation**](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions): 클라이언트 측 탐색 동안 Next.js는 [부분 렌더](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions)를 수행하여 slot 내 서브페이지를 변경하면서, URL과 일치하지 않더라도 다른 slot의 활성 서브페이지는 유지합니다.
  * **Hard Navigation** : 전체 페이지 로드(브라우저 새로고침) 이후에는 현재 URL과 일치하지 않는 slot의 활성 상태를 Next.js가 판단할 수 없습니다. 대신 해당 slot에 대한 [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs) 파일을 렌더링하거나 `default.js`가 없으면 `404`를 렌더링합니다.

> **알아두면 좋아요** :
>
>   * 일치하지 않는 라우트에 대한 `404`는 의도하지 않은 페이지에서 병렬 라우트가 실수로 렌더링되는 일을 방지합니다.
>

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#examples)

### With `useSelectedLayoutSegment(s)`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#with-useselectedlayoutsegments)

[`useSelectedLayoutSegment`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)와 [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)는 slot 내 활성 라우트 세그먼트를 읽을 수 있도록 `parallelRoutesKey` 매개변수를 받습니다.

app/layout.tsx

JavaScriptTypeScript
```
    'use client'

    import { useSelectedLayoutSegment } from 'next/navigation'

    export default function Layout({ auth }: { auth: React.ReactNode }) {
      const loginSegment = useSelectedLayoutSegment('auth')
      // ...
    }
```

사용자가 `app/@auth/login`(또는 URL 바의 `/login`)으로 이동하면 `loginSegment`는 문자열 `"login"`과 같습니다.

### Conditional Routes[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#conditional-routes)

사용자 역할과 같은 조건에 따라 라우트를 조건부로 렌더링하려면 Parallel Routes를 사용할 수 있습니다. 예를 들어 `/admin` 또는 `/user` 역할에 대해 서로 다른 대시보드 페이지를 렌더링하려면 다음과 같이 작성합니다:

app/dashboard/layout.tsx

JavaScriptTypeScript
```
    import { checkUserRole } from '@/lib/auth'

    export default function Layout({
      user,
      admin,
    }: {
      user: React.ReactNode
      admin: React.ReactNode
    }) {
      const role = checkUserRole()
      return role === 'admin' ? admin : user
    }
```

### Tab Groups[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#tab-groups)

slot 안에 `layout`을 추가하여 사용자가 해당 slot을 독립적으로 탐색할 수 있게 만들 수 있습니다. 이는 탭을 만드는 데 유용합니다.

예를 들어 `@analytics` slot에는 `/page-views`와 `/visitors`라는 두 개의 서브페이지가 있습니다.

`@analytics` 안에 [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) 파일을 생성하여 두 페이지 간에 탭을 공유합니다:

app/@analytics/layout.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'

    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <>
          <nav>
            <Link href="/page-views">Page Views</Link>
            <Link href="/visitors">Visitors</Link>
          </nav>
          <div>{children}</div>
        </>
      )
    }
```

### Modals[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#modals)

Parallel Routes는 [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)와 함께 사용하여 딥 링크를 지원하는 모달을 만들 수 있습니다. 이를 통해 다음과 같은 모달 구축 시 흔한 문제를 해결할 수 있습니다:

  * 모달 콘텐츠를 **URL로 공유**할 수 있게 만들기.
  * 모달이 닫히는 대신 페이지가 새로고침될 때 **컨텍스트 유지**.
  * 이전 라우트로 이동하는 대신 **뒤로 탐색 시 모달 닫기**.
  * **앞으로 탐색 시 모달 다시 열기**.

다음 UI 패턴을 고려해 보세요. 사용자는 레이아웃에서 클라이언트 측 탐색을 사용해 로그인 모달을 열거나 별도의 `/login` 페이지에 접근할 수 있습니다:

이 패턴을 구현하려면 먼저 **메인** 로그인 페이지를 렌더링하는 `/login` 라우트를 만듭니다.

app/login/page.tsx

JavaScriptTypeScript
```
    import { Login } from '@/app/ui/login'

    export default function Page() {
      return <Login />
    }
```

그런 다음 `@auth` slot 내부에 `default.js`(https://nextjs.org/docs/app/api-reference/file-conventions/default) 파일을 추가하여 `null`을 반환합니다. 이는 모달이 활성 상태가 아닐 때 렌더링되지 않도록 보장합니다.

app/@auth/default.tsx

JavaScriptTypeScript
```
    export default function Default() {
      return null
    }
```

`@auth` slot 내부에서 `/login` 라우트를 가로채기 위해 `<Modal>` 컴포넌트와 그 자식들을 `@auth/(.)login/page.tsx` 파일로 가져오고 폴더 이름을 `/@auth/(.)login/page.tsx`로 업데이트합니다.

app/@auth/(.)login/page.tsx

JavaScriptTypeScript
```
    import { Modal } from '@/app/ui/modal'
    import { Login } from '@/app/ui/login'

    export default function Page() {
      return (
        <Modal>
          <Login />
        </Modal>
      )
    }
```

> **알아두면 좋아요:**
>
>   * `(.)` 규칙은 라우트를 가로채는 데 사용됩니다. 자세한 내용은 [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) 문서를 참고하세요.
>   * `<Modal>` 기능을 모달 콘텐츠(`<Login>`)와 분리하면 모달 내부의 모든 콘텐츠(예: [forms](https://nextjs.org/docs/app/guides/forms))가 서버 컴포넌트임을 보장할 수 있습니다. 자세한 내용은 [Interleaving Client and Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#supported-pattern-passing-server-components-to-client-components-as-props)를 참고하세요.
>

#### Opening the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#opening-the-modal)

이제 Next.js 라우터를 활용해 모달을 열고 닫을 수 있습니다. 이렇게 하면 모달이 열릴 때와 뒤로/앞으로 탐색할 때 URL이 올바르게 업데이트됩니다.

모달을 열려면 `@auth` slot을 부모 레이아웃에 prop으로 전달하고 `children` prop과 함께 렌더링합니다.

app/layout.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'

    export default function Layout({
      auth,
      children,
    }: {
      auth: React.ReactNode
      children: React.ReactNode
    }) {
      return (
        <>
          <nav>
            <Link href="/login">Open modal</Link>
          </nav>
          <div>{auth}</div>
          <div>{children}</div>
        </>
      )
    }
```

사용자가 `<Link>`를 클릭하면 `/login` 페이지로 이동하는 대신 모달이 열립니다. 하지만 새로고침 또는 초기 로드 시 `/login`으로 이동하면 메인 로그인 페이지가 표시됩니다.

#### Closing the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#closing-the-modal)

`router.back()`을 호출하거나 `Link` 컴포넌트를 사용해 모달을 닫을 수 있습니다.

app/ui/modal.tsx

JavaScriptTypeScript
```
    'use client'

    import { useRouter } from 'next/navigation'

    export function Modal({ children }: { children: React.ReactNode }) {
      const router = useRouter()

      return (
        <>
          <button
            onClick={() => {
              router.back()
            }}
          >
            Close modal
          </button>
          <div>{children}</div>
        </>
      )
    }
```

`Link` 컴포넌트를 사용해 더 이상 `@auth` slot이 렌더링되지 않아야 하는 페이지로 이동할 때, 병렬 라우트가 `null`을 반환하는 컴포넌트와 일치하는지 확인해야 합니다. 예를 들어 루트 페이지로 돌아갈 때는 `@auth/page.tsx` 컴포넌트를 생성합니다:

app/ui/modal.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'

    export function Modal({ children }: { children: React.ReactNode }) {
      return (
        <>
          <Link href="/">Close modal</Link>
          <div>{children}</div>
        </>
      )
    }
```

app/@auth/page.tsx

JavaScriptTypeScript

```
    export default function Page() {
      return null
    }
```

다른 페이지(예: `/foo`, `/foo/bar` 등)로 이동하는 경우에는 캐치올 슬롯을 사용할 수 있습니다:

app/@auth/[...catchAll]/page.tsx

JavaScriptTypeScript
```
    export default function CatchAll() {
      return null
    }
```

> **알아두면 좋아요:**
>
>   * 병렬 라우트의 동작 방식 때문에 모달을 닫기 위해 `@auth` 슬롯에서 캐치올 라우트를 사용합니다. 슬롯과 더 이상 일치하지 않는 경로로 클라이언트 측 탐색을 수행하면 계속 표시되므로, 모달을 닫으려면 `null`을 반환하는 라우트와 슬롯을 일치시켜야 합니다.
>   * 다른 예로는 전용 `/photo/[id]` 페이지를 유지하면서 갤러리에서 사진 모달을 열거나, 사이드 모달에서 쇼핑 카트를 여는 경우가 있습니다.
>   * Intercepted 및 Parallel Routes와 함께하는 모달 [예시 보기](https://github.com/vercel-labs/nextgram).
>

### 로딩 및 오류 UI[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#loading-and-error-ui)

병렬 라우트는 독립적으로 스트리밍될 수 있으므로, 각 라우트에 대해 독립적인 오류 및 로딩 상태를 정의할 수 있습니다.

자세한 내용은 [Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading) 및 [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling) 문서를 참고하세요.

##

- [default.js](https://nextjs.org/docs/app/api-reference/file-conventions/default)
  - 파일에 대한 API Reference입니다.

보내기