---
title: '가이드: 인증'
description: '인증을 이해하는 것은 애플리케이션 데이터를 보호하는 데 필수적입니다. 이 페이지에서는 인증을 구현할 때 사용할 React 및 Next.js 기능을 안내합니다.'
---

# 가이드: 인증 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/authentication

# Next.js에서 인증을 구현하는 방법

마지막 업데이트 2026년 2월 20일

인증을 이해하는 것은 애플리케이션 데이터를 보호하는 데 필수적입니다. 이 페이지에서는 인증을 구현할 때 사용할 React 및 Next.js 기능을 안내합니다.

시작하기 전에 프로세스를 세 가지 개념으로 나누면 도움이 됩니다:

  1. **[Authentication](https://nextjs.org/docs/pages/guides/authentication#authentication)** : 사용자가 본인이 맞는지 확인합니다. 사용자 이름과 비밀번호처럼 사용자가 가진 것으로 신원을 증명해야 합니다.
  2. **[Session Management](https://nextjs.org/docs/pages/guides/authentication#session-management)** : 요청 전반에서 사용자의 인증 상태를 추적합니다.
  3. **[Authorization](https://nextjs.org/docs/pages/guides/authentication#authorization)** : 사용자가 접근할 수 있는 라우트와 데이터를 결정합니다.

다음 다이어그램은 React와 Next.js 기능을 사용한 인증 흐름을 보여줍니다:

이 페이지의 예제는 학습 목적의 기본 사용자 이름/비밀번호 인증을 다룹니다. 직접 인증 솔루션을 구현할 수도 있지만, 보안성과 단순성을 높이려면 인증 라이브러리를 사용하는 것이 좋습니다. 이러한 라이브러리는 인증, 세션 관리, 권한 부여에 대한 빌트인 해결책과 더불어 소셜 로그인, 다중 요소 인증, 역할 기반 접근 제어 같은 기능도 제공합니다. 라이브러리 목록은 [Auth Libraries](https://nextjs.org/docs/pages/guides/authentication#auth-libraries) 섹션에서 확인할 수 있습니다.

## Authentication[](https://nextjs.org/docs/pages/guides/authentication#authentication)

회원가입 및/또는 로그인 폼을 구현하는 단계는 다음과 같습니다:

  1. 사용자가 폼을 통해 자격 증명을 제출합니다.
  2. 폼이 API 라우트에서 처리되는 요청을 전송합니다.
  3. 검증이 성공하면 프로세스가 완료되어 사용자의 인증이 성공했음을 나타냅니다.
  4. 검증이 실패하면 에러 메시지를 표시합니다.

사용자가 자격 증명을 입력할 수 있는 로그인 폼을 생각해 보세요:

pages/login.tsx

JavaScriptTypeScript
[code]
    import { FormEvent } from 'react'
    import { useRouter } from 'next/router'

    export default function LoginPage() {
      const router = useRouter()

      async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        const formData = new FormData(event.currentTarget)
        const email = formData.get('email')
        const password = formData.get('password')

        const response = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password }),
        })

        if (response.ok) {
          router.push('/profile')
        } else {
          // Handle errors
        }
      }

      return (
        <form onSubmit={handleSubmit}>
          <input type="email" name="email" placeholder="Email" required />
          <input type="password" name="password" placeholder="Password" required />
          <button type="submit">Login</button>
        </form>
      )
    }
[/code]

위 폼에는 사용자의 이메일과 비밀번호를 입력받는 두 개의 인풋 필드가 있습니다. 제출 시 `/api/auth/login` API 라우트로 POST 요청을 보내는 함수를 실행합니다.

그런 다음 API 라우트에서 인증 공급자의 API를 호출해 인증을 처리할 수 있습니다:

pages/api/auth/login.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
    import { signIn } from '@/auth'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      try {
        const { email, password } = req.body
        await signIn('credentials', { email, password })

        res.status(200).json({ success: true })
      } catch (error) {
        if (error.type === 'CredentialsSignin') {
          res.status(401).json({ error: 'Invalid credentials.' })
        } else {
          res.status(500).json({ error: 'Something went wrong.' })
        }
      }
    }
[/code]

## Session Management[](https://nextjs.org/docs/pages/guides/authentication#session-management)

세션 관리는 사용자의 인증 상태가 요청 간에도 유지되도록 보장합니다. 세션 또는 토큰을 생성, 저장, 갱신, 삭제하는 과정을 포함합니다.

세션에는 두 가지 유형이 있습니다:

  1. [**Stateless**](https://nextjs.org/docs/pages/guides/authentication#stateless-sessions): 세션 데이터(또는 토큰)를 브라우저 쿠키에 저장합니다. 쿠키는 각 요청마다 전송되어 서버에서 세션을 검증할 수 있게 합니다. 구현이 간단하지만 올바르게 구현하지 않으면 보안성이 떨어질 수 있습니다.
  2. [**Database**](https://nextjs.org/docs/pages/guides/authentication#database-sessions): 세션 데이터를 데이터베이스에 저장하고, 사용자의 브라우저에는 암호화된 세션 ID만 전달합니다. 더 안전하지만 복잡하고 서버 리소스를 더 사용할 수 있습니다.

> **알아두면 좋아요:** 두 방법 중 하나 또는 둘 다 사용할 수 있지만, [iron-session](https://github.com/vvo/iron-session)이나 [Jose](https://github.com/panva/jose) 같은 세션 관리 라이브러리를 사용하는 것을 권장합니다.

### Stateless Sessions[](https://nextjs.org/docs/pages/guides/authentication#stateless-sessions)

#### 쿠키 설정 및 삭제[](https://nextjs.org/docs/pages/guides/authentication#setting-and-deleting-cookies)

[API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)를 사용해 서버에서 세션을 쿠키로 설정할 수 있습니다:

pages/api/login.ts

JavaScriptTypeScript
[code]
    import { serialize } from 'cookie'
    import type { NextApiRequest, NextApiResponse } from 'next'
    import { encrypt } from '@/app/lib/session'

    export default function handler(req: NextApiRequest, res: NextApiResponse) {
      const sessionData = req.body
      const encryptedSessionData = encrypt(sessionData)

      const cookie = serialize('session', encryptedSessionData, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        maxAge: 60 * 60 * 24 * 7, // One week
        path: '/',
      })
      res.setHeader('Set-Cookie', cookie)
      res.status(200).json({ message: 'Successfully set cookie!' })
    }
[/code]

### Database Sessions[](https://nextjs.org/docs/pages/guides/authentication#database-sessions)

데이터베이스 세션을 생성하고 관리하려면 다음 단계를 수행해야 합니다:

  1. 세션과 데이터를 저장할 데이터베이스 테이블을 만들거나, Auth 라이브러리가 이를 처리하는지 확인합니다.
  2. 세션을 삽입, 업데이트, 삭제하는 기능을 구현합니다.
  3. 세션 ID를 사용자의 브라우저에 저장하기 전에 암호화하고, 데이터베이스와 쿠키가 동기 상태를 유지하도록 합니다(선택 사항이지만 [Proxy](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional)의 낙관적 인증 체크에 권장됩니다).

**서버에서 세션 생성** :

pages/api/create-session.ts

JavaScriptTypeScript
[code]
    import db from '../../lib/db'
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      try {
        const user = req.body
        const sessionId = generateSessionId()
        await db.insertSession({
          sessionId,
          userId: user.id,
          createdAt: new Date(),
        })

        res.status(200).json({ sessionId })
      } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' })
      }
    }
[/code]

## Authorization[](https://nextjs.org/docs/pages/guides/authentication#authorization)

사용자가 인증되고 세션이 생성되면, 애플리케이션 내에서 사용자가 접근하고 수행할 수 있는 작업을 제어하기 위해 권한 부여를 구현할 수 있습니다.

권한 부여 체크는 두 가지 유형이 있습니다:

  1. **Optimistic** : 쿠키에 저장된 세션 데이터를 사용해 사용자가 라우트에 접근하거나 작업을 수행할 자격이 있는지 확인합니다. UI 요소의 표시/숨김이나 권한 및 역할에 따른 리디렉션 같이 빠른 작업에 유용합니다.
  2. **Secure** : 데이터베이스에 저장된 세션 데이터를 사용해 사용자가 라우트에 접근하거나 작업을 수행할 자격이 있는지 확인합니다. 민감한 데이터 접근이나 중요한 작업에 필요한 보다 안전한 체크입니다.

두 경우 모두 다음을 권장합니다:

  * 권한 부여 로직을 중앙화하기 위해 [Data Access Layer](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal)를 만듭니다.
  * 필요한 데이터만 반환하도록 [Data Transfer Objects (DTO)](https://nextjs.org/docs/pages/guides/authentication#using-data-transfer-objects-dto)를 사용합니다.
  * 선택적으로 [Proxy](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional)를 사용해 낙관적 체크를 수행합니다.

### Proxy를 사용한 낙관적 체크(선택 사항)[](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional)

일부 경우에는 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용해 권한에 따라 사용자를 리디렉션하고 싶을 수 있습니다:

  * 낙관적 체크를 수행하기 위해. Proxy는 모든 라우트에서 실행되므로 리디렉션 로직을 중앙화하고 권한이 없는 사용자를 미리 필터링하기에 좋습니다.
  * 사용자 간에 데이터를 공유하는 정적 라우트(예: 유료 벽 뒤의 콘텐츠)를 보호하기 위해.

그러나 Proxy는 [prefetched](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) 라우트를 포함해 모든 라우트에서 실행되므로, 쿠키에서 세션만 읽는 낙관적 체크에 집중하고 성능 문제를 피하기 위해 데이터베이스 체크는 피하는 것이 중요합니다.

예:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'
    import { decrypt } from '@/app/lib/session'
    import { cookies } from 'next/headers'

    // 1. Specify protected and public routes
    const protectedRoutes = ['/dashboard']
    const publicRoutes = ['/login', '/signup', '/']

    export default async function proxy(req: NextRequest) {
      // 2. Check if the current route is protected or public
      const path = req.nextUrl.pathname
      const isProtectedRoute = protectedRoutes.includes(path)
      const isPublicRoute = publicRoutes.includes(path)

      // 3. Decrypt the session from the cookie
      const cookie = (await cookies()).get('session')?.value
      const session = await decrypt(cookie)

      // 4. Redirect to /login if the user is not authenticated
      if (isProtectedRoute && !session?.userId) {
        return NextResponse.redirect(new URL('/login', req.nextUrl))
      }

      // 5. Redirect to /dashboard if the user is authenticated
      if (
        isPublicRoute &&
        session?.userId &&
        !req.nextUrl.pathname.startsWith('/dashboard')
      ) {
        return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
      }

      return NextResponse.next()
    }

    // Routes Proxy should not run on
    export const config = {
      matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
    }
[/code]

Proxy는 초기 체크에 유용하지만 데이터를 보호하는 유일한 방어선이 되어서는 안 됩니다. 대부분의 보안 체크는 데이터 소스에 가능한 한 가깝게 배치해야 하며, 자세한 내용은 [Data Access Layer](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal)를 참고하세요.

> **팁** :
>
>   * Proxy에서 `req.cookies.get('session').value`를 사용해 쿠키를 읽을 수도 있습니다.

> * Proxy는 Node.js 런타임을 사용하므로, 사용하는 Auth 라이브러리와 세션 관리 라이브러리가 호환되는지 확인하세요. Auth 라이브러리가 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)만 지원한다면 [Middleware](https://github.com/vercel/next.js/blob/v15.5.6/docs/01-app/03-api-reference/03-file-conventions/middleware.mdx)를 사용해야 할 수 있습니다.
> * Proxy에서는 `matcher` 속성을 사용해 Proxy가 실행되어야 하는 경로를 지정할 수 있습니다. 다만 인증 처리의 경우 모든 경로에서 Proxy를 실행하는 것이 권장됩니다.
>

### 데이터 액세스 계층(DAL) 만들기[](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal-1)

#### API 경로 보호하기[](https://nextjs.org/docs/pages/guides/authentication#protecting-api-routes)

Next.js의 API Routes는 서버 측 로직과 데이터 관리를 처리하는 데 필수적입니다. 특정 기능에 오직 권한 있는 사용자만 접근하도록 이러한 경로를 보호하는 것이 중요합니다. 일반적으로 사용자의 인증 상태와 역할 기반 권한을 검증하는 절차가 포함됩니다.

다음은 API Route를 보호하는 예시입니다.

pages/api/route.ts

JavaScriptTypeScript
[code]
    import { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const session = await getSession(req)

      // Check if the user is authenticated
      if (!session) {
        res.status(401).json({
          error: 'User is not authenticated',
        })
        return
      }

      // Check if the user has the 'admin' role
      if (session.user.role !== 'admin') {
        res.status(401).json({
          error: 'Unauthorized access: User does not have admin privileges.',
        })
        return
      }

      // Proceed with the route for authorized users
      // ... implementation of the API Route
    }
[/code]

이 예시는 인증과 인가를 위한 이중 보안 검사를 수행하는 API Route를 보여 줍니다. 먼저 활성 세션이 있는지 확인하고, 이어서 로그인한 사용자가 'admin'인지 검증합니다. 이 접근 방식은 인증되고 권한이 부여된 사용자에게만 요청 처리를 허용하여 강력한 보안을 유지합니다.

## 리소스[](https://nextjs.org/docs/pages/guides/authentication#resources)

이제 Next.js의 인증에 대해 배웠으니, 안전한 인증과 세션 관리를 구현하는 데 도움이 되는 Next.js 호환 라이브러리와 리소스를 소개합니다.

### Auth 라이브러리[](https://nextjs.org/docs/pages/guides/authentication#auth-libraries)

  * [Auth0](https://auth0.com/docs/quickstart/webapp/nextjs)
  * [Better Auth](https://www.better-auth.com/docs/integrations/next)
  * [Clerk](https://clerk.com/docs/quickstarts/nextjs)
  * [Descope](https://docs.descope.com/getting-started/nextjs)
  * [Kinde](https://kinde.com/docs/developer-tools/nextjs-sdk)
  * [Logto](https://docs.logto.io/quick-starts/next-app-router)
  * [NextAuth.js](https://authjs.dev/getting-started/installation?framework=next.js)
  * [Ory](https://www.ory.sh/docs/getting-started/integrate-auth/nextjs)
  * [Stack Auth](https://docs.stack-auth.com/getting-started/setup)
  * [Supabase](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
  * [Stytch](https://stytch.com/docs/guides/quickstarts/nextjs)
  * [WorkOS](https://workos.com/docs/user-management/nextjs)

### 세션 관리 라이브러리[](https://nextjs.org/docs/pages/guides/authentication#session-management-libraries)

  * [Iron Session](https://github.com/vvo/iron-session)
  * [Jose](https://github.com/panva/jose)

## 추가 학습 자료[](https://nextjs.org/docs/pages/guides/authentication#further-reading)

인증 및 보안에 대해 더 학습하고 싶다면 다음 자료를 확인하세요.

  * [Next.js에서 보안을 고민하는 방법](https://nextjs.org/blog/security-nextjs-server-components-actions)
  * [XSS 공격 이해하기](https://vercel.com/guides/understanding-xss-attacks)
  * [CSRF 공격 이해하기](https://vercel.com/guides/understanding-csrf-attacks)
  * [The Copenhagen Book](https://thecopenhagenbook.com/)
