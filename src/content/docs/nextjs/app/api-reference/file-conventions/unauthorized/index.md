---
title: '파일 시스템 규칙: unauthorized.js'
description: '이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. GitHub에서 체험 후 피드백을 공유해 주세요.'
---

# 파일 시스템 규칙: unauthorized.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)unauthorized.js

페이지 복사

# unauthorized.js

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에서 체험 후 피드백을 공유해 주세요.

마지막 업데이트: 2026년 2월 20일

**unauthorized** 파일은 인증 과정에서 [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) 함수가 호출될 때 UI를 렌더링하는 데 사용됩니다. UI를 커스터마이즈할 수 있을 뿐 아니라, Next.js는 `401` 상태 코드를 반환합니다.

app/unauthorized.tsx

JavaScriptTypeScript
[code]
    import Login from '@/app/components/Login'
     
    export default function Unauthorized() {
      return (
        <main>
          <h1>401 - Unauthorized</h1>
          <p>Please log in to access this page.</p>
          <Login />
        </main>
      )
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#props)

`unauthorized.js` 컴포넌트는 어떤 props도 받지 않습니다.

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#examples)

### Displaying login UI to unauthenticated users[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#displaying-login-ui-to-unauthenticated-users)

[`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized) 함수를 사용하여 로그인 UI가 포함된 `unauthorized.js` 파일을 렌더링할 수 있습니다.

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

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized#version-history)

버전| 변경 사항  
---|---  
`v15.1.0`| `unauthorized.js` 도입.  
  
## 

### [unauthorized 함수에 대한 API Reference.](https://nextjs.org/docs/app/api-reference/functions/unauthorized)

도움이 되었나요?

지원됨.

보내기
