---
title: '안내서: 인증'
description: '최종 업데이트: 2026년 2월 20일'
---

# 안내서: 인증 | Next.js

Source URL: https://nextjs.org/docs/app/guides/authentication

[앱 라우터](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Authentication

페이지 복사

# Next.js에서 인증을 구현하는 방법

최종 업데이트: 2026년 2월 20일

인증을 이해하는 것은 애플리케이션 데이터를 보호하는 데 매우 중요합니다. 이 페이지는 인증을 구현할 때 사용할 React 및 Next.js 기능을 안내합니다.

시작하기 전에 프로세스를 다음 세 가지 개념으로 나누면 도움이 됩니다:

  1. **[Authentication](https://nextjs.org/docs/app/guides/authentication#authentication)** : 사용자가 자신이 주장하는 사람인지 확인합니다. 사용자 이름과 비밀번호처럼 사용자가 가진 것으로 신원을 증명해야 합니다.
  2. **[Session Management](https://nextjs.org/docs/app/guides/authentication#session-management)** : 요청 전반에 걸쳐 사용자의 인증 상태를 추적합니다.
  3. **[Authorization](https://nextjs.org/docs/app/guides/authentication#authorization)** : 사용자가 접근할 수 있는 라우트와 데이터를 결정합니다.



이 다이어그램은 React와 Next.js 기능을 사용한 인증 플로우를 보여줍니다:

이 페이지의 예제는 교육 목적을 위해 기본적인 사용자 이름/비밀번호 인증을 다룹니다. 커스텀 인증 솔루션을 구현할 수 있지만, 보안과 단순성을 강화하려면 인증 라이브러리를 사용하는 것이 좋습니다. 이러한 라이브러리는 인증, 세션 관리, 권한 부여에 대한 내장 솔루션뿐 아니라 소셜 로그인, 다중 요소 인증, 역할 기반 접근 제어 같은 추가 기능도 제공합니다. 목록은 [Auth Libraries](https://nextjs.org/docs/app/guides/authentication#auth-libraries) 섹션에서 확인할 수 있습니다.

## Authentication[](https://nextjs.org/docs/app/guides/authentication#authentication)

### 회원가입 및 로그인 기능[](https://nextjs.org/docs/app/guides/authentication#sign-up-and-login-functionality)

React의 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)와 `useActionState`를 결합한 [`<form>`](https://react.dev/reference/react-dom/components/form) 요소를 사용해 사용자 자격 증명을 수집하고, 폼 필드를 검증하며, Authentication Provider의 API나 데이터베이스를 호출할 수 있습니다.

Server Actions는 항상 서버에서 실행되므로 인증 로직을 처리하기에 안전한 환경을 제공합니다.

회원가입/로그인 기능을 구현하는 단계는 다음과 같습니다:

#### 1\. 사용자 자격 증명 수집[](https://nextjs.org/docs/app/guides/authentication#1-capture-user-credentials)

사용자 자격 증명을 수집하려면 제출 시 Server Action을 호출하는 폼을 만듭니다. 예를 들어, 사용자 이름, 이메일, 비밀번호를 받는 회원가입 폼은 다음과 같습니다:

app/ui/signup-form.tsx

JavaScriptTypeScript
[code]
    import { signup } from '@/app/actions/auth'
     
    export function SignupForm() {
      return (
        <form action={signup}>
          <div>
            <label htmlFor="name">Name</label>
            <input id="name" name="name" placeholder="Name" />
          </div>
          <div>
            <label htmlFor="email">Email</label>
            <input id="email" name="email" type="email" placeholder="Email" />
          </div>
          <div>
            <label htmlFor="password">Password</label>
            <input id="password" name="password" type="password" />
          </div>
          <button type="submit">Sign Up</button>
        </form>
      )
    }
[/code]

app/actions/auth.ts

JavaScriptTypeScript
[code]
    export async function signup(formData: FormData) {}
[/code]

#### 2\. 서버에서 폼 필드를 검증[](https://nextjs.org/docs/app/guides/authentication#2-validate-form-fields-on-the-server)

Server Action을 사용해 서버에서 폼 필드를 검증합니다. 인증 제공자가 폼 검증을 지원하지 않는 경우 [Zod](https://zod.dev/)나 [Yup](https://github.com/jquense/yup) 같은 스키마 검증 라이브러리를 사용할 수 있습니다.

예시로 Zod를 사용하면 적절한 오류 메시지가 포함된 폼 스키마를 정의할 수 있습니다:

app/lib/definitions.ts

JavaScriptTypeScript
[code]
    import * as z from 'zod'
     
    export const SignupFormSchema = z.object({
      name: z
        .string()
        .min(2, { error: 'Name must be at least 2 characters long.' })
        .trim(),
      email: z.email({ error: 'Please enter a valid email.' }).trim(),
      password: z
        .string()
        .min(8, { error: 'Be at least 8 characters long' })
        .regex(/[a-zA-Z]/, { error: 'Contain at least one letter.' })
        .regex(/[0-9]/, { error: 'Contain at least one number.' })
        .regex(/[^a-zA-Z0-9]/, {
          error: 'Contain at least one special character.',
        })
        .trim(),
    })
     
    export type FormState =
      | {
          errors?: {
            name?: string[]
            email?: string[]
            password?: string[]
          }
          message?: string
        }
      | undefined
[/code]

정의된 스키마와 일치하지 않는 폼 필드가 있다면 Server Action에서 `return`하여 인증 제공자의 API나 데이터베이스를 불필요하게 호출하지 않도록 합니다.

app/actions/auth.ts

JavaScriptTypeScript
[code]
    import { SignupFormSchema, FormState } from '@/app/lib/definitions'
     
    export async function signup(state: FormState, formData: FormData) {
      // Validate form fields
      const validatedFields = SignupFormSchema.safeParse({
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password'),
      })
     
      // If any form fields are invalid, return early
      if (!validatedFields.success) {
        return {
          errors: validatedFields.error.flatten().fieldErrors,
        }
      }
     
      // Call the provider or db to create a user...
    }
[/code]

`<SignupForm />` 내부에서 React의 `useActionState` 훅을 사용하면 폼이 제출되는 동안 검증 오류를 표시할 수 있습니다:

app/ui/signup-form.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { signup } from '@/app/actions/auth'
    import { useActionState } from 'react'
     
    export default function SignupForm() {
      const [state, action, pending] = useActionState(signup, undefined)
     
      return (
        <form action={action}>
          <div>
            <label htmlFor="name">Name</label>
            <input id="name" name="name" placeholder="Name" />
          </div>
          {state?.errors?.name && <p>{state.errors.name}</p>}
     
          <div>
            <label htmlFor="email">Email</label>
            <input id="email" name="email" placeholder="Email" />
          </div>
          {state?.errors?.email && <p>{state.errors.email}</p>}
     
          <div>
            <label htmlFor="password">Password</label>
            <input id="password" name="password" type="password" />
          </div>
          {state?.errors?.password && (
            <div>
              <p>Password must:</p>
              <ul>
                {state.errors.password.map((error) => (
                  <li key={error}>- {error}</li>
                ))}
              </ul>
            </div>
          )}
          <button disabled={pending} type="submit">
            Sign Up
          </button>
        </form>
      )
    }
[/code]

> **알아두면 좋아요:**
> 
>   * React 19에서는 `useFormStatus`가 data, method, action처럼 추가 키를 반환합니다. React 19를 사용하지 않는다면 `pending` 키만 사용할 수 있습니다.
>   * 데이터를 변경하기 전에 사용자가 해당 작업을 수행할 권한이 있는지 항상 확인해야 합니다. [Authentication and Authorization](https://nextjs.org/docs/app/guides/authentication#authorization)을 참고하세요.
> 


#### 3\. 사용자 생성 또는 자격 증명 확인[](https://nextjs.org/docs/app/guides/authentication#3-create-a-user-or-check-user-credentials)

폼 필드를 검증한 후에는 인증 제공자의 API나 데이터베이스를 호출하여 새 사용자 계정을 만들거나 사용자가 존재하는지 확인할 수 있습니다.

이전 예제를 이어서:

app/actions/auth.tsx

JavaScriptTypeScript
[code]
    export async function signup(state: FormState, formData: FormData) {
      // 1. Validate form fields
      // ...
     
      // 2. Prepare data for insertion into database
      const { name, email, password } = validatedFields.data
      // e.g. Hash the user's password before storing it
      const hashedPassword = await bcrypt.hash(password, 10)
     
      // 3. Insert the user into the database or call an Auth Library's API
      const data = await db
        .insert(users)
        .values({
          name,
          email,
          password: hashedPassword,
        })
        .returning({ id: users.id })
     
      const user = data[0]
     
      if (!user) {
        return {
          message: 'An error occurred while creating your account.',
        }
      }
     
      // TODO:
      // 4. Create user session
      // 5. Redirect user
    }
[/code]

사용자 계정을 성공적으로 생성하거나 자격 증명을 확인한 후에는 세션을 생성해 사용자의 인증 상태를 관리할 수 있습니다. 세션 관리 전략에 따라 세션은 쿠키, 데이터베이스 또는 둘 다에 저장할 수 있습니다. 자세한 내용은 [Session Management](https://nextjs.org/docs/app/guides/authentication#session-management) 섹션을 확인하세요.

> **팁:**
> 
>   * 위 예제는 교육 목적상 인증 단계를 자세히 분해했기 때문에 장황합니다. 이를 통해 직접 안전한 솔루션을 구현하는 일이 빠르게 복잡해질 수 있음을 보여줍니다. 프로세스를 단순화하려면 [Auth Library](https://nextjs.org/docs/app/guides/authentication#auth-libraries) 사용을 고려하세요.
>   * 사용자 경험을 개선하기 위해 등록 흐름 초반에 중복 이메일이나 사용자 이름을 확인하고 싶을 수 있습니다. 예를 들어 사용자가 사용자 이름을 입력하는 동안 또는 입력 필드가 포커스를 잃을 때 확인하면 불필요한 폼 제출을 방지하고 즉각적인 피드백을 제공할 수 있습니다. 이러한 확인 빈도를 관리하려면 [use-debounce](https://www.npmjs.com/package/use-debounce) 같은 라이브러리로 요청을 디바운스하세요.
> 


## Session Management[](https://nextjs.org/docs/app/guides/authentication#session-management)

세션 관리는 사용자의 인증된 상태를 요청 전반에 걸쳐 유지합니다. 여기에는 세션이나 토큰을 생성, 저장, 갱신, 삭제하는 작업이 포함됩니다.

세션에는 두 가지 유형이 있습니다:

  1. [**Stateless**](https://nextjs.org/docs/app/guides/authentication#stateless-sessions): 세션 데이터(또는 토큰)가 브라우저의 쿠키에 저장됩니다. 쿠키가 각 요청과 함께 전송되어 서버에서 세션을 검증할 수 있습니다. 구현이 잘못되면 보안이 떨어질 수 있지만, 방법 자체는 단순합니다.
  2. [**Database**](https://nextjs.org/docs/app/guides/authentication#database-sessions): 세션 데이터가 데이터베이스에 저장되고, 사용자의 브라우저는 암호화된 세션 ID만 받습니다. 더 안전하지만 복잡도가 높고 서버 리소스를 더 많이 사용할 수 있습니다.



> **알아두면 좋아요:** 두 방법 중 하나 또는 둘 다 사용할 수 있지만, [iron-session](https://github.com/vvo/iron-session)이나 [Jose](https://github.com/panva/jose) 같은 세션 관리 라이브러리를 사용하는 것이 좋습니다.

### Stateless Sessions[](https://nextjs.org/docs/app/guides/authentication#stateless-sessions)

무상태 세션을 생성하고 관리하려면 다음 단계를 따르면 됩니다:

  1. 세션 서명에 사용할 비밀 키를 생성하고 [environment variable](https://nextjs.org/docs/app/guides/environment-variables)로 저장합니다.
  2. 세션 관리 라이브러리를 사용해 세션 데이터를 암호화/복호화하는 로직을 작성합니다.
  3. Next.js [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API를 사용해 쿠키를 관리합니다.

위의 내용에 더해, 사용자가 애플리케이션으로 돌아왔을 때 세션을 [업데이트(또는 새로 고침)](https://nextjs.org/docs/app/guides/authentication#updating-or-refreshing-sessions)하고, 로그아웃 시 세션을 [삭제](https://nextjs.org/docs/app/guides/authentication#deleting-the-session)하는 기능을 추가하는 것도 고려하세요.

> **참고:** 사용하는 [인증 라이브러리](https://nextjs.org/docs/app/guides/authentication#auth-libraries)에 세션 관리 기능이 포함되어 있는지 확인하세요.

#### 1\. 비밀 키 생성[](https://nextjs.org/docs/app/guides/authentication#1-generating-a-secret-key)

세션에 서명할 비밀 키를 생성하는 방법은 여러 가지가 있습니다. 예를 들어, 터미널에서 `openssl` 명령을 사용할 수 있습니다:

terminal
[code]
    openssl rand -base64 32
[/code]

이 명령은 비밀 키로 사용할 수 있는 32자 길이의 랜덤 문자열을 생성하며, 이를 [환경 변수 파일](https://nextjs.org/docs/app/guides/environment-variables)에 저장할 수 있습니다:

.env
[code]
    SESSION_SECRET=your_secret_key
[/code]

이후 세션 관리 로직에서 이 키를 참조할 수 있습니다:

app/lib/session.js
[code]
    const secretKey = process.env.SESSION_SECRET
[/code]

#### 2\. 세션 암호화 및 복호화[](https://nextjs.org/docs/app/guides/authentication#2-encrypting-and-decrypting-sessions)

다음으로, 선호하는 [세션 관리 라이브러리](https://nextjs.org/docs/app/guides/authentication#session-management-libraries)를 사용해 세션을 암호화하고 복호화할 수 있습니다. 앞선 예제를 이어서, [Jose](https://www.npmjs.com/package/jose)([Edge Runtime](https://nextjs.org/docs/app/api-reference/edge) 호환)와 React의 [`server-only`](https://www.npmjs.com/package/server-only) 패키지를 사용해 세션 관리 로직이 서버에서만 실행되도록 하겠습니다.

app/lib/session.ts

JavaScriptTypeScript
[code]
    import 'server-only'
    import { SignJWT, jwtVerify } from 'jose'
    import { SessionPayload } from '@/app/lib/definitions'
     
    const secretKey = process.env.SESSION_SECRET
    const encodedKey = new TextEncoder().encode(secretKey)
     
    export async function encrypt(payload: SessionPayload) {
      return new SignJWT(payload)
        .setProtectedHeader({ alg: 'HS256' })
        .setIssuedAt()
        .setExpirationTime('7d')
        .sign(encodedKey)
    }
     
    export async function decrypt(session: string | undefined = '') {
      try {
        const { payload } = await jwtVerify(session, encodedKey, {
          algorithms: ['HS256'],
        })
        return payload
      } catch (error) {
        console.log('Failed to verify session')
      }
    }
[/code]

> **팁** :
> 
>   * 페이로드에는 이후 요청에서 사용할 최소한의 고유 사용자 데이터(예: 사용자 ID, 역할 등)만 포함하세요. 전화번호, 이메일, 신용카드 정보와 같은 개인 식별 정보나 비밀번호 같은 민감한 데이터는 포함하지 않아야 합니다.
> 

#### 3\. 쿠키 설정(권장 옵션)[](https://nextjs.org/docs/app/guides/authentication#3-setting-cookies-recommended-options)

세션을 쿠키에 저장하려면 Next.js [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API를 사용하세요. 쿠키는 서버에서 설정해야 하며, 다음과 같은 권장 옵션을 포함해야 합니다:

  * **HttpOnly** : 클라이언트측 JavaScript가 쿠키에 접근하지 못하도록 합니다.
  * **Secure** : https를 사용해 쿠키를 전송합니다.
  * **SameSite** : 쿠키가 크로스 사이트 요청과 함께 전송될 수 있는지 지정합니다.
  * **Max-Age 또는 Expires** : 일정 기간 이후 쿠키를 삭제합니다.
  * **Path** : 쿠키의 URL 경로를 정의합니다.

각 옵션에 대한 자세한 내용은 [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)을 참고하세요.

app/lib/session.ts

JavaScriptTypeScript
[code]
    import 'server-only'
    import { cookies } from 'next/headers'
     
    export async function createSession(userId: string) {
      const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
      const session = await encrypt({ userId, expiresAt })
      const cookieStore = await cookies()
     
      cookieStore.set('session', session, {
        httpOnly: true,
        secure: true,
        expires: expiresAt,
        sameSite: 'lax',
        path: '/',
      })
    }
[/code]

서버 액션으로 돌아가 `createSession()` 함수를 호출한 뒤 [`redirect()`](https://nextjs.org/docs/app/guides/redirecting) API를 사용해 사용자를 적절한 페이지로 리디렉션할 수 있습니다:

app/actions/auth.ts

JavaScriptTypeScript
[code]
    import { createSession } from '@/app/lib/session'
     
    export async function signup(state: FormState, formData: FormData) {
      // Previous steps:
      // 1. Validate form fields
      // 2. Prepare data for insertion into database
      // 3. Insert the user into the database or call an Library API
     
      // Current steps:
      // 4. Create user session
      await createSession(user.id)
      // 5. Redirect user
      redirect('/profile')
    }
[/code]

> **팁** :
> 
>   * **쿠키는 서버에서 설정**해 클라이언트 측 변조를 방지하세요.
>   * 🎥 시청: Next.js로 상태 비저장 세션과 인증을 이해하기 → [YouTube (11분)](https://www.youtube.com/watch?v=DJvM2lSPn6w).
> 

#### 세션 업데이트(또는 새로 고침)[](https://nextjs.org/docs/app/guides/authentication#updating-or-refreshing-sessions)

세션 만료 시간을 연장할 수도 있습니다. 이는 사용자가 애플리케이션에 다시 접근했을 때 로그인 상태를 유지하는 데 유용합니다. 예를 들어:

app/lib/session.ts

JavaScriptTypeScript
[code]
    import 'server-only'
    import { cookies } from 'next/headers'
    import { decrypt } from '@/app/lib/session'
     
    export async function updateSession() {
      const session = (await cookies()).get('session')?.value
      const payload = await decrypt(session)
     
      if (!session || !payload) {
        return null
      }
     
      const expires = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
     
      const cookieStore = await cookies()
      cookieStore.set('session', session, {
        httpOnly: true,
        secure: true,
        expires: expires,
        sameSite: 'lax',
        path: '/',
      })
    }
[/code]

> **팁:** 인증 라이브러리가 리프레시 토큰을 지원하는지 확인하세요. 리프레시 토큰은 사용자 세션을 연장하는 데 사용할 수 있습니다.

#### 세션 삭제[](https://nextjs.org/docs/app/guides/authentication#deleting-the-session)

세션을 삭제하려면 쿠키를 삭제하면 됩니다:

app/lib/session.ts

JavaScriptTypeScript
[code]
    import 'server-only'
    import { cookies } from 'next/headers'
     
    export async function deleteSession() {
      const cookieStore = await cookies()
      cookieStore.delete('session')
    }
[/code]

그런 다음 애플리케이션에서 `deleteSession()` 함수를 재사용할 수 있으며, 예를 들어 로그아웃 시 다음과 같이 사용할 수 있습니다:

app/actions/auth.ts

JavaScriptTypeScript
[code]
    import { cookies } from 'next/headers'
    import { deleteSession } from '@/app/lib/session'
     
    export async function logout() {
      await deleteSession()
      redirect('/login')
    }
[/code]

### 데이터베이스 세션[](https://nextjs.org/docs/app/guides/authentication#database-sessions)

데이터베이스 세션을 생성하고 관리하려면 다음 단계를 따라야 합니다:

  1. 세션과 데이터를 저장할 데이터베이스 테이블을 생성합니다(또는 인증 라이브러리가 이를 처리하는지 확인).
  2. 세션을 삽입, 업데이트, 삭제하는 기능을 구현합니다.
  3. 세션 ID를 사용자 브라우저에 저장하기 전에 암호화하고, 데이터베이스와 쿠키가 동기화되도록 합니다(선택 사항이지만 [Proxy](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)에서 낙관적 인증 검사를 위해 권장).

예를 들어:

app/lib/session.ts

JavaScriptTypeScript
[code]
    import cookies from 'next/headers'
    import { db } from '@/app/lib/db'
    import { encrypt } from '@/app/lib/session'
     
    export async function createSession(id: number) {
      const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
     
      // 1. Create a session in the database
      const data = await db
        .insert(sessions)
        .values({
          userId: id,
          expiresAt,
        })
        // Return the session ID
        .returning({ id: sessions.id })
     
      const sessionId = data[0].id
     
      // 2. Encrypt the session ID
      const session = await encrypt({ sessionId, expiresAt })
     
      // 3. Store the session in cookies for optimistic auth checks
      const cookieStore = await cookies()
      cookieStore.set('session', session, {
        httpOnly: true,
        secure: true,
        expires: expiresAt,
        sameSite: 'lax',
        path: '/',
      })
    }
[/code]

> **팁** :
> 
>   * 더 빠른 접근을 위해 세션 기간 동안 서버 캐시를 추가하는 것을 고려할 수 있습니다. 또한 세션 데이터를 기본 데이터베이스에 유지하고, 데이터 요청을 결합해 쿼리 수를 줄일 수 있습니다.
>   * 사용자가 마지막으로 로그인한 시간, 활성 기기 수 추적 또는 모든 기기에서 로그아웃할 수 있는 기능 등 고급 사용 사례를 위해 데이터베이스 세션을 선택할 수 있습니다.
> 

세션 관리 구현 후에는 애플리케이션 내에서 사용자가 접근하고 수행할 수 있는 작업을 제어하기 위한 권한 부여 로직을 추가해야 합니다. 자세한 내용은 [Authorization](https://nextjs.org/docs/app/guides/authentication#authorization) 섹션을 계속 확인하세요.

## Authorization[](https://nextjs.org/docs/app/guides/authentication#authorization)

사용자가 인증되고 세션이 생성된 후, 애플리케이션에서 사용자가 접근하고 수행할 수 있는 작업을 제어하기 위해 권한 부여를 구현할 수 있습니다.

권한 검사는 크게 두 가지 유형이 있습니다:

  1. **Optimistic** : 쿠키에 저장된 세션 데이터를 사용해 사용자가 특정 경로에 접근하거나 작업을 수행할 권한이 있는지 확인합니다. UI 요소 표시/숨김, 권한이나 역할에 따른 리디렉션과 같은 빠른 작업에 유용합니다.
  2. **Secure** : 데이터베이스에 저장된 세션 데이터를 사용해 사용자가 특정 경로에 접근하거나 작업을 수행할 권한이 있는지 확인합니다. 민감한 데이터나 작업에 접근해야 하는 경우와 같이 보안이 중요한 상황에 사용됩니다.

두 경우 모두 다음을 권장합니다:

  * 권한 부여 로직을 중앙집중화하기 위해 [데이터 접근 계층(Data Access Layer)](https://nextjs.org/docs/app/guides/authentication#creating-a-data-access-layer-dal)을 만듭니다.
  * 필요한 데이터만 반환하기 위해 [DTO(Data Transfer Objects)](https://nextjs.org/docs/app/guides/authentication#using-data-transfer-objects-dto)를 사용합니다.
  * 선택적으로 [Proxy](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)를 사용해 낙관적 검사를 수행합니다.

### Proxy를 통한 낙관적 검사(선택 사항)[](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)

다음과 같은 경우 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)를 사용해 권한에 따라 사용자를 리디렉션하고 싶을 수 있습니다:

  * 낙관적 검사를 수행하기 위해. Proxy는 모든 경로에서 실행되므로 리디렉션 로직을 중앙집중화하고 권한이 없는 사용자를 사전에 걸러내기에 좋습니다.
  * 사용자 간에 데이터를 공유하는 정적 경로(예: 유료 콘텐츠)를 보호하기 위해.

그러나 Proxy는 [사전 패치된](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) 경로를 포함한 모든 경로에서 실행되므로, 성능 문제를 피하기 위해 쿠키에서 세션만 읽는(낙관적 검사) 방식으로 사용하고 데이터베이스 검사는 피하는 것이 중요합니다.

예를 들어:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse } from 'next/server'
    import { decrypt } from '@/app/lib/session'
    import { cookies } from 'next/headers'
     
    // 1. Specify protected and public routes
    const protectedRoutes = ['/dashboard']
[/code]

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

Proxy는 초기 점검에 유용하지만, 데이터를 보호하기 위한 유일한 방어선이 되어서는 안 됩니다. 보안 점검 대부분은 데이터 소스와 가능한 한 가까운 지점에서 수행되어야 하며, 자세한 내용은 [Data Access Layer](https://nextjs.org/docs/app/guides/authentication#creating-a-data-access-layer-dal)를 참조하세요.

> **Tips** :
> 
>   * Proxy에서는 `req.cookies.get('session').value`를 사용해 쿠키를 읽을 수도 있습니다.
>   * Proxy는 Node.js 런타임을 사용하므로, Auth 라이브러리와 세션 관리 라이브러리가 호환되는지 확인하세요. Auth 라이브러리가 [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)만 지원한다면 [Middleware](https://github.com/vercel/next.js/blob/v15.5.6/docs/01-app/03-api-reference/03-file-conventions/middleware.mdx)를 사용해야 할 수도 있습니다.
>   * Proxy에서 `matcher` 속성을 사용해 Proxy가 실행되어야 하는 라우트를 지정할 수 있습니다. 다만 인증 목적이라면 전체 라우트에서 Proxy를 실행하는 것이 권장됩니다.
> 


### 데이터 액세스 레이어(DAL) 만들기[](https://nextjs.org/docs/app/guides/authentication#creating-a-data-access-layer-dal)

데이터 요청과 권한 부여 로직을 중앙화하기 위해 DAL을 만드는 것이 좋습니다.

DAL에는 사용자가 애플리케이션과 상호작용할 때 세션을 검증하는 함수가 포함되어야 합니다. 최소한 이 함수는 세션이 유효한지 확인한 뒤, 추가 요청에 필요한 사용자 정보를 반환하거나 리디렉션해야 합니다.

예를 들어 `verifySession()` 함수를 포함하는 별도 DAL 파일을 만들고, React의 [cache](https://react.dev/reference/react/cache) API를 사용해 렌더 패스 동안 함수 반환 값을 메모이제이션합니다:

app/lib/dal.ts

JavaScriptTypeScript
[code]
    import 'server-only'
     
    import { cookies } from 'next/headers'
    import { decrypt } from '@/app/lib/session'
     
    export const verifySession = cache(async () => {
      const cookie = (await cookies()).get('session')?.value
      const session = await decrypt(cookie)
     
      if (!session?.userId) {
        redirect('/login')
      }
     
      return { isAuth: true, userId: session.userId }
    })
[/code]

그런 다음 데이터 요청, Server Actions, Route Handlers에서 `verifySession()` 함수를 호출할 수 있습니다:

app/lib/dal.ts

JavaScriptTypeScript
[code]
    export const getUser = cache(async () => {
      const session = await verifySession()
      if (!session) return null
     
      try {
        const data = await db.query.users.findMany({
          where: eq(users.id, session.userId),
          // Explicitly return the columns you need rather than the whole user object
          columns: {
            id: true,
            name: true,
            email: true,
          },
        })
     
        const user = data[0]
     
        return user
      } catch (error) {
        console.log('Failed to fetch user')
        return null
      }
    })
[/code]

> **Tip** :
> 
>   * DAL은 요청 시점에 가져오는 데이터를 보호하는 데 사용할 수 있습니다. 그러나 사용자 간에 데이터를 공유하는 정적 라우트에서는 데이터가 요청 시점이 아니라 빌드 시점에 가져옵니다. 정적 라우트를 보호하려면 [Proxy](https://nextjs.org/docs/app/guides/authentication#optimistic-checks-with-proxy-optional)를 사용하세요.
>   * 보안을 강화하려면 세션 ID를 데이터베이스와 비교해 세션 유효성을 확인하세요. 렌더 패스 동안 데이터베이스에 불필요한 중복 요청을 피하려면 React의 [cache](https://react.dev/reference/react/cache) 함수를 사용하세요.
>   * 관련 데이터 요청을 JavaScript 클래스에 모아두고, 어떤 메서드든 실행 전에 `verifySession()`을 호출하도록 구성할 수 있습니다.
> 


### 데이터 전송 객체(DTO) 사용하기[](https://nextjs.org/docs/app/guides/authentication#using-data-transfer-objects-dto)

데이터를 조회할 때 애플리케이션에서 사용할 필수 데이터만 반환하고 전체 객체를 보내지 않는 것이 좋습니다. 예를 들어 사용자 데이터를 가져올 때 비밀번호, 전화번호 등 전체 사용자 객체 대신 사용자 ID와 이름만 반환할 수 있습니다.

반환되는 데이터 구조를 제어할 수 없거나, 전체 객체가 클라이언트로 전달되는 것을 피하고 싶은 팀 환경이라면 클라이언트에 노출해도 안전한 필드를 지정하는 전략을 사용할 수 있습니다.

app/lib/dto.ts

JavaScriptTypeScript
[code]
    import 'server-only'
    import { getUser } from '@/app/lib/dal'
     
    function canSeeUsername(viewer: User) {
      return true
    }
     
    function canSeePhoneNumber(viewer: User, team: string) {
      return viewer.isAdmin || team === viewer.team
    }
     
    export async function getProfileDTO(slug: string) {
      const data = await db.query.users.findMany({
        where: eq(users.slug, slug),
        // Return specific columns here
      })
      const user = data[0]
     
      const currentUser = await getUser(user.id)
     
      // Or return only what's specific to the query here
      return {
        username: canSeeUsername(currentUser) ? user.username : null,
        phonenumber: canSeePhoneNumber(currentUser, user.team)
          ? user.phonenumber
          : null,
      }
    }
[/code]

DAL에서 데이터 요청과 권한 로직을 중앙화하고 DTO를 사용하면 모든 데이터 요청의 보안과 일관성을 보장할 수 있어, 애플리케이션이 확장될 때 유지보수·감사·디버깅이 쉬워집니다.

> **알아두면 좋아요** :
> 
>   * DTO를 정의하는 방법은 `toJSON()` 사용부터 위 예시와 같은 개별 함수, 혹은 JS 클래스까지 다양합니다. 이는 React나 Next.js 기능이 아니라 JavaScript 패턴이므로, 애플리케이션에 가장 적합한 패턴을 찾기 위해 조사를 권장합니다.
>   * [Security in Next.js article](https://nextjs.org/blog/security-nextjs-server-components-actions)에서 보안 모범 사례를 더 알아보세요.
> 


### 서버 컴포넌트[](https://nextjs.org/docs/app/guides/authentication#server-components)

[Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서의 인증 검사는 역할 기반 접근 제어에 유용합니다. 예를 들어 사용자 역할에 따라 컴포넌트를 조건부로 렌더링할 수 있습니다:

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
     
    export default async function Dashboard() {
      const session = await verifySession()
      const userRole = session?.user?.role // Assuming 'role' is part of the session object
     
      if (userRole === 'admin') {
        return <AdminDashboard />
      } else if (userRole === 'user') {
        return <UserDashboard />
      } else {
        redirect('/login')
      }
    }
[/code]

이 예시에서는 DAL의 `verifySession()` 함수를 사용해 'admin', 'user', 미승인 역할을 확인합니다. 이 패턴을 사용하면 각 사용자가 자신의 역할에 맞는 컴포넌트와만 상호작용하게 할 수 있습니다.

### 레이아웃과 인증 검사[](https://nextjs.org/docs/app/guides/authentication#layouts-and-auth-checks)

[Partial Rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) 때문에 [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout)에서 검사를 수행할 때 주의해야 합니다. 레이아웃은 네비게이션 시 다시 렌더링되지 않아, 모든 라우트 변경 시 사용자 세션을 검사하지 못할 수 있습니다.

대신 데이터 소스나 조건부로 렌더링될 컴포넌트 가까이에서 검사를 수행하세요.

예를 들어 사용자 데이터를 가져와 네비게이션에 사용자 이미지를 표시하는 공유 레이아웃이 있다면, 레이아웃에서 인증 검사를 수행하는 대신 레이아웃에서 사용자 데이터를 (`getUser()`) 가져오고 DAL에서 인증 검사를 수행하세요.

이는 애플리케이션 어디에서든 `getUser()`가 호출될 때 인증 검사가 수행되도록 해, 개발자가 데이터 접근 권한 확인을 빠뜨리는 것을 방지합니다.

#### 페이지 컴포넌트에서의 인증 검사[](https://nextjs.org/docs/app/guides/authentication#auth-checks-in-page-components)

예를 들어 대시보드 페이지에서 사용자 세션을 검증하고 사용자 데이터를 가져올 수 있습니다:

app/dashboard/page.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
     
    export default async function DashboardPage() {
      const session = await verifySession()
     
      // Fetch user-specific data from your database or data source
      const user = await getUserData(session.userId)
     
      return (
        <div>
          <h1>Welcome, {user.name}</h1>
          {/* Dashboard content */}
        </div>
      )
    }
[/code]

#### 리프 컴포넌트에서의 인증 검사[](https://nextjs.org/docs/app/guides/authentication#auth-checks-in-leaf-components)

사용자 권한에 따라 UI 요소를 조건부로 렌더링하는 리프 컴포넌트에서도 인증 검사를 수행할 수 있습니다. 예를 들어 관리자 전용 액션을 표시하는 컴포넌트입니다:

app/ui/admin-actions.tsx

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
     
    export default async function AdminActions() {
      const session = await verifySession()
      const userRole = session?.user?.role
     
      if (userRole !== 'admin') {
        return null
      }
     
      return (
        <div>
          <button>Delete User</button>
          <button>Edit Settings</button>
        </div>
      )
    }
[/code]

이 패턴을 사용하면 각 컴포넌트 렌더 시 인증 검사를 수행하면서 사용자 권한에 따라 UI 요소를 표시하거나 숨길 수 있습니다.

> **알아두면 좋아요:**
> 
>   * SPA에서 흔한 패턴은 사용자가 승인되지 않았을 때 레이아웃이나 최상위 컴포넌트에서 `return null`을 하는 것입니다. Next.js 애플리케이션에는 여러 진입점이 있으므로 이 패턴은 중첩 라우트 세그먼트와 Server Actions 접근을 막지 못해 **권장되지 않습니다**.
>   * 이러한 컴포넌트에서 호출되는 모든 Server Actions 역시 자체적인 권한 검사를 수행해야 합니다. 클라이언트 UI만으로는 보안을 보장할 수 없습니다.
> 


### Server Actions[](https://nextjs.org/docs/app/guides/authentication#server-actions)

[Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)는 공개 API 엔드포인트와 동일한 보안 기준으로 다루고, 사용자가 해당 변조 작업을 수행할 권한이 있는지 확인해야 합니다.

아래 예시에서는 작업을 진행하기 전에 사용자 역할을 확인합니다:

app/lib/actions.ts

JavaScriptTypeScript
[code]
    'use server'
    import { verifySession } from '@/app/lib/dal'
     
    export async function serverAction(formData: FormData) {
      const session = await verifySession()
      const userRole = session?.user?.role
     
      // Return early if user is not authorized to perform the action
      if (userRole !== 'admin') {
        return null
      }

// Proceed with the action for authorized users
    }
[/code]

### 라우트 핸들러[](https://nextjs.org/docs/app/guides/authentication#route-handlers)

[Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)는 외부에 공개된 API 엔드포인트와 동일한 보안 기준으로 취급하고, 사용자가 해당 라우트 핸들러에 접근할 권한이 있는지 반드시 확인하세요.

예시:

app/api/route.ts

JavaScriptTypeScript
[code]
    import { verifySession } from '@/app/lib/dal'
     
    export async function GET() {
      // User authentication and role verification
      const session = await verifySession()
     
      // Check if the user is authenticated
      if (!session) {
        // User is not authenticated
        return new Response(null, { status: 401 })
      }
     
      // Check if the user has the 'admin' role
      if (session.user.role !== 'admin') {
        // User is authenticated but does not have the right permissions
        return new Response(null, { status: 403 })
      }
     
      // Continue for authorized users
    }
[/code]

위 예시는 두 단계 보안 검사를 수행하는 라우트 핸들러를 보여줍니다. 먼저 활성 세션이 있는지 확인하고, 이후 로그인한 사용자가 'admin'인지 검증합니다.

## 컨텍스트 프로바이더[](https://nextjs.org/docs/app/guides/authentication#context-providers)

[인터리빙](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#interleaving-server-and-client-components) 덕분에 인증용 컨텍스트 프로바이더를 사용할 수 있습니다. 다만 Server Components에서는 React `context`가 지원되지 않으므로 Client Components에서만 적용됩니다.

이 방식은 동작하지만, 자식 Server Components는 먼저 서버에서 렌더링되고 컨텍스트 프로바이더의 세션 데이터에 접근할 수 없습니다:

app/layout.ts

JavaScriptTypeScript
[code]
    import { ContextProvider } from 'auth-lib'
     
    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>
            <ContextProvider>{children}</ContextProvider>
          </body>
        </html>
      )
    }
[/code]
[code]
    'use client';
     
    import { useSession } from "auth-lib";
     
    export default function Profile() {
      const { userId } = useSession();
      const { data } = useSWR(`/api/user/${userId}`, fetcher)
     
      return (
        // ...
      );
    }
[/code]

클라이언트 컴포넌트에서 세션 데이터가 필요하다면(예: 클라이언트 측 데이터 패칭), 민감한 세션 데이터가 클라이언트에 노출되지 않도록 React의 [`taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue) API를 사용하세요.

## 리소스[](https://nextjs.org/docs/app/guides/authentication#resources)

이제 Next.js 인증을 학습했으니, 안전한 인증과 세션 관리를 구현하는 데 도움이 되는 Next.js 호환 라이브러리와 리소스를 확인하세요:

### 인증 라이브러리[](https://nextjs.org/docs/app/guides/authentication#auth-libraries)

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



### 세션 관리 라이브러리[](https://nextjs.org/docs/app/guides/authentication#session-management-libraries)

  * [Iron Session](https://github.com/vvo/iron-session)
  * [Jose](https://github.com/panva/jose)



## 추가 학습 자료[](https://nextjs.org/docs/app/guides/authentication#further-reading)

인증과 보안에 대해 더 배우고 싶다면 다음 자료를 참고하세요:

  * [How to think about security in Next.js](https://nextjs.org/blog/security-nextjs-server-components-actions)
  * [Understanding XSS Attacks](https://vercel.com/guides/understanding-xss-attacks)
  * [Understanding CSRF Attacks](https://vercel.com/guides/understanding-csrf-attacks)
  * [The Copenhagen Book](https://thecopenhagenbook.com/)



도움이 되었나요?

지원됨.

보내기
