---
title: '함수: unauthorized'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 대신 테스트해 보고 GitHub에서 피드백을 공유해주세요.'
---

# 함수: unauthorized | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/unauthorized

# unauthorized

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. 대신 테스트해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해주세요.

2026년 2월 20일에 마지막으로 업데이트됨

`unauthorized` 함수는 Next.js 401 에러 페이지를 렌더링하는 에러를 발생시킵니다. 애플리케이션에서 인증 오류를 처리할 때 유용합니다. [`unauthorized.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)을 사용해 UI를 커스터마이즈할 수 있습니다.

`unauthorized`를 사용하려면 `next.config.js` 파일에서 실험적 설정 옵션인 [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)를 활성화하세요:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        authInterrupts: true,
      },
    }

    export default nextConfig
[/code]

`unauthorized`는 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 호출할 수 있습니다.

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'

    export default async function DashboardPage() {
      const session = await verifySession()

      if (!session) {
        unauthorized()
      }

      // Render the dashboard for authenticated users
      return (
        <main>
          <h1>Welcome to the Dashboard</h1>
          <p>Hi, {session.user.name}.</p>
        </main>
      )
    }
[/code]

## 알아두면 좋은 정보[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#good-to-know)

  * `unauthorized` 함수는 [루트 레이아웃](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)에서 호출할 수 없습니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#examples)

### 인증되지 않은 사용자에게 로그인 UI 표시[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#displaying-login-ui-to-unauthenticated-users)

`unauthorized` 함수를 사용해 로그인 UI가 포함된 `unauthorized.js` 파일을 표시할 수 있습니다.

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'

    export default async function DashboardPage() {
      const session = await verifySession()

      if (!session) {
        unauthorized()
      }

      return <div>Dashboard</div>
    }
[/code]

app/unauthorized.tsx

JavaScriptTypeScript
[code]
    import Login from '@/app/components/Login'

    export default function UnauthorizedPage() {
      return (
        <main>
          <h1>401 - Unauthorized</h1>
          <p>Please log in to access this page.</p>
          <Login />
        </main>
      )
    }
[/code]

### Server Actions와 함께 사용하는 변이[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#mutations-with-server-actions)

특정 변이를 인증된 사용자만 실행하도록 보장하기 위해 Server Actions에서 `unauthorized`를 호출할 수 있습니다.

app/actions/update-profile.ts

JavaScriptTypeScript
[code]
    'use server'

    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'
    import db from '@/app/lib/db'

    export async function updateProfile(data: FormData) {
      const session = await verifySession()

      // If the user is not authenticated, return a 401
      if (!session) {
        unauthorized()
      }

      // Proceed with mutation
      // ...
    }
[/code]

### Route Handlers로 데이터 가져오기[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#fetching-data-with-route-handlers)

`unauthorized`를 Route Handlers에서 사용해 인증된 사용자만 엔드포인트에 접근하도록 할 수 있습니다.

app/api/profile/route.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'
    import { verifySession } from '@/app/lib/dal'
    import { unauthorized } from 'next/navigation'

    export async function GET(req: NextRequest): Promise<NextResponse> {
      // Verify the user's session
      const session = await verifySession()

      // If no session exists, return a 401 and render unauthorized.tsx
      if (!session) {
        unauthorized()
      }

      // Fetch data
      // ...
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#version-history)

Version| Changes
---|---
`v15.1.0`| `unauthorized` 도입

##

- [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
  - 특수 파일 unauthorized.js에 대한 API 레퍼런스.

보내기
