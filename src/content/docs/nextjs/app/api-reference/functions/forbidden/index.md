---
title: '함수: forbidden'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로, 프로덕션 환경에서는 권장되지 않습니다. 테스트해 보고 GitHub에서 피드백을 공유해주세요.'
---

# 함수: forbidden | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/forbidden

Copy page

# forbidden

이 기능은 현재 실험 단계이며 변경될 수 있으므로, 프로덕션 환경에서는 권장되지 않습니다. 테스트해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해주세요.

마지막 업데이트 2026년 2월 20일

`forbidden` 함수는 Next.js 403 오류 페이지를 렌더링하는 오류를 발생시킵니다. 애플리케이션에서 인증 오류를 처리할 때 유용합니다. [`forbidden.js` 파일](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)을 사용해 UI를 커스터마이즈할 수 있습니다.

`forbidden`을 사용하려면 `next.config.js` 파일에서 실험적 구성 옵션인 [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)를 활성화하세요:

next.config.ts

JavaScriptTypeScript
```
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        authInterrupts: true,
      },
    }

    export default nextConfig
```

`forbidden`은 [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 호출할 수 있습니다.

app/auth/page.tsx

JavaScriptTypeScript
```
    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'

    export default async function AdminPage() {
      const session = await verifySession()

      // Check if the user has the 'admin' role
      if (session.role !== 'admin') {
        forbidden()
      }

      // Render the admin page for authorized users
      return <></>
    }
```

## 알아두면 좋은 점[](https://nextjs.org/docs/app/api-reference/functions/forbidden#good-to-know)

  * `forbidden` 함수는 [root layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)에서 호출할 수 없습니다.

## 예시[](https://nextjs.org/docs/app/api-reference/functions/forbidden#examples)

### 역할 기반 라우트 보호[](https://nextjs.org/docs/app/api-reference/functions/forbidden#role-based-route-protection)

`forbidden`을 사용하면 사용자 역할에 따라 특정 라우트 접근을 제한할 수 있습니다. 이는 인증되었지만 필요한 권한이 없는 사용자가 해당 라우트에 접근하지 못하도록 보장합니다.

app/admin/page.tsx

JavaScriptTypeScript
```
    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'

    export default async function AdminPage() {
      const session = await verifySession()

      // Check if the user has the 'admin' role
      if (session.role !== 'admin') {
        forbidden()
      }

      // Render the admin page for authorized users
      return (
        <main>
          <h1>Admin Dashboard</h1>
          <p>Welcome, {session.user.name}!</p>
        </main>
      )
    }
```

### Server Actions에서의 변이[](https://nextjs.org/docs/app/api-reference/functions/forbidden#mutations-with-server-actions)

Server Actions에서 변이를 구현할 때 `forbidden`을 사용하면 특정 역할을 가진 사용자만 민감한 데이터를 업데이트하도록 제한할 수 있습니다.

app/actions/update-role.ts

JavaScriptTypeScript
```
    'use server'

    import { verifySession } from '@/app/lib/dal'
    import { forbidden } from 'next/navigation'
    import db from '@/app/lib/db'

    export async function updateRole(formData: FormData) {
      const session = await verifySession()

      // Ensure only admins can update roles
      if (session.role !== 'admin') {
        forbidden()
      }

      // Perform the role update for authorized users
      // ...
    }
```

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/forbidden#version-history)

Version| Changes
---|---
`v15.1.0`| `forbidden` 도입.

##

- [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
  - 의 특별 파일에 대한 API 레퍼런스입니다.

supported.

Send