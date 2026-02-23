---
title: '가이드: 데이터 보안'
description: '원본 URL: https://nextjs.org/docs/app/guides/data-security'
---

# 가이드: 데이터 보안 | Next.js

원본 URL: https://nextjs.org/docs/app/guides/data-security

[App Router](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)데이터 보안

# Next.js에서 데이터 보안을 생각하는 방법

마지막 업데이트 2026년 2월 20일

[React Server Components](https://react.dev/reference/rsc/server-components)는 성능을 개선하고 데이터 패칭을 단순화하지만, 데이터에 접근하는 위치와 방식이 바뀌면서 프런트엔드 앱에서 데이터를 다룰 때의 기존 보안 가정도 일부 달라집니다.

이 가이드는 Next.js에서 데이터 보안을 어떻게 바라보고 모범 사례를 구현할지 이해하는 데 도움을 줍니다.

## 데이터 가져오기 접근 방식[](https://nextjs.org/docs/app/guides/data-security#data-fetching-approaches)

프로젝트의 규모와 연차에 따라 Next.js에서 데이터를 가져오는 방식으로 세 가지를 권장합니다.

  * [HTTP API](https://nextjs.org/docs/app/guides/data-security#external-http-apis): 기존 대규모 애플리케이션과 조직에 적합합니다.
  * [데이터 액세스 레이어](https://nextjs.org/docs/app/guides/data-security#data-access-layer): 신규 프로젝트에 권장합니다.
  * [컴포넌트 수준 데이터 액세스](https://nextjs.org/docs/app/guides/data-security#component-level-data-access): 프로토타입과 학습용에 적합합니다.

데이터 패칭 접근 방식은 하나만 선택해 혼용을 피하는 것이 좋습니다. 이렇게 하면 코드베이스에서 작업하는 개발자와 보안 감사자 모두가 예상할 수 있는 경계를 갖게 됩니다.

### 외부 HTTP API[](https://nextjs.org/docs/app/guides/data-security#external-http-apis)

기존 프로젝트에 Server Components를 도입할 때는 **제로 트러스트** 모델을 따르세요. Server Components에서 [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch)를 사용해 기존 REST 또는 GraphQL API 엔드포인트를 클라이언트 컴포넌트와 동일하게 계속 호출할 수 있습니다.

app/page.tsx
[code]
    import { cookies } from 'next/headers'

    export default async function Page() {
      const cookieStore = cookies()
      const token = cookieStore.get('AUTH_TOKEN')?.value

      const res = await fetch('https://api.example.com/profile', {
        headers: {
          Cookie: `AUTH_TOKEN=${token}`,
          // Other headers
        },
      })

      // ....
    }
[/code]

다음과 같은 경우에 특히 잘 맞습니다.

  * 이미 보안 관행이 갖춰져 있을 때.
  * 별도 백엔드 팀이 다른 언어를 사용하거나 API를 독립적으로 관리할 때.

### 데이터 액세스 레이어[](https://nextjs.org/docs/app/guides/data-security#data-access-layer)

신규 프로젝트에는 전용 **데이터 액세스 레이어(DAL)**를 만드는 것을 권장합니다. 이는 데이터를 언제 어떻게 가져와 렌더링 컨텍스트에 무엇을 전달할지를 통제하는 내부 라이브러리입니다.

데이터 액세스 레이어는 다음을 만족해야 합니다.

  * 서버에서만 실행됩니다.
  * 인가 검사를 수행합니다.
  * 안전하고 최소한의 **데이터 전송 객체(DTO)**를 반환합니다.

이 접근 방식은 모든 데이터 액세스 로직을 중앙집중화해 일관된 데이터 접근을 강제하고 인가 버그 위험을 줄입니다. 또한 요청의 여러 부분에서 메모리 내 캐시를 공유하는 이점도 얻습니다.

data/auth.ts
[code]
    import { cache } from 'react'
    import { cookies } from 'next/headers'

    // Cached helper methods makes it easy to get the same value in many places
    // without manually passing it around. This discourages passing it from Server
    // Component to Server Component which minimizes risk of passing it to a Client
    // Component.
    export const getCurrentUser = cache(async () => {
      const token = cookies().get('AUTH_TOKEN')
      const decodedToken = await decryptAndValidate(token)
      // Don't include secret tokens or private information as public fields.
      // Use classes to avoid accidentally passing the whole object to the client.
      return new User(decodedToken.id)
    })
[/code]

data/user-dto.tsx
[code]
    import 'server-only'
    import { getCurrentUser } from './auth'

    function canSeeUsername(viewer: User) {
      // Public info for now, but can change
      return true
    }

    function canSeePhoneNumber(viewer: User, team: string) {
      // Privacy rules
      return viewer.isAdmin || team === viewer.team
    }

    export async function getProfileDTO(slug: string) {
      // Don't pass values, read back cached values, also solves context and easier to make it lazy

      // use a database API that supports safe templating of queries
      const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
      const userData = rows[0]

      const currentUser = await getCurrentUser()

      // only return the data relevant for this query and not everything
      // <https://www.w3.org/2001/tag/doc/APIMinimization>
      return {
        username: canSeeUsername(currentUser) ? userData.username : null,
        phonenumber: canSeePhoneNumber(currentUser, userData.team)
          ? userData.phonenumber
          : null,
      }
    }
[/code]

app/page.tsx
[code]
    import { getProfile } from '../../data/user'

    export async function Page({ params: { slug } }) {
      // This page can now safely pass around this profile knowing
      // that it shouldn't contain anything sensitive.
      const profile = await getProfile(slug);
      ...
    }
[/code]

> **알아두면 좋아요:** 비밀 키는 환경 변수에 저장하되, `process.env`에 접근하는 주체를 데이터 액세스 레이어로만 제한하세요. 이렇게 하면 애플리케이션의 다른 부분에서 비밀이 노출되는 것을 막을 수 있습니다.

### 컴포넌트 수준 데이터 액세스[](https://nextjs.org/docs/app/guides/data-security#component-level-data-access)

빠른 프로토타입과 반복을 위해 데이터베이스 쿼리를 Server Components에 직접 배치할 수도 있습니다.

하지만 이 접근 방식은 다음과 같이 클라이언트에 개인 데이터를 실수로 노출하기 쉬워집니다.

app/page.tsx
[code]
    import Profile from './components/profile.tsx'

    export async function Page({ params: { slug } }) {
      const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
      const userData = rows[0]
      // EXPOSED: This exposes all the fields in userData to the client because
      // we are passing the data from the Server Component to the Client.
      return <Profile user={userData} />
    }
[/code]

app/ui/profile.tsx
[code]
    'use client'

    // BAD: This is a bad props interface because it accepts way more data than the
    // Client Component needs and it encourages server components to pass all that
    // data down. A better solution would be to accept a limited object with just
    // the fields necessary for rendering the profile.
    export default async function Profile({ user }: { user: User }) {
      return (
        <div>
          <h1>{user.name}</h1>
          ...
        </div>
      )
    }
[/code]

클라이언트 컴포넌트로 전달하기 전에 데이터를 정제해야 합니다.

data/user.ts
[code]
    import { sql } from './db'

    export async function getUser(slug: string) {
      const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
      const user = rows[0]

      // Return only the public fields
      return {
        name: user.name,
      }
    }
[/code]

app/page.tsx
[code]
    import { getUser } from '../data/user'
    import Profile from './ui/profile'

    export default async function Page({
      params: { slug },
    }: {
      params: { slug: string }
    }) {
      const publicProfile = await getUser(slug)
      return <Profile user={publicProfile} />
    }
[/code]

## 데이터 읽기[](https://nextjs.org/docs/app/guides/data-security#reading-data)

### 서버에서 클라이언트로 데이터 전달[](https://nextjs.org/docs/app/guides/data-security#passing-data-from-server-to-client)

초기 로드 시 Server Components와 Client Components 모두 서버에서 실행되어 HTML을 생성하지만, 서로 격리된 모듈 시스템에서 실행됩니다. 이로 인해 Server Components는 비공개 데이터와 API에 접근할 수 있고, Client Components는 접근할 수 없습니다.

**Server Components:**

  * 서버에서만 실행됩니다.
  * 환경 변수, 비밀, 데이터베이스, 내부 API에 안전하게 접근할 수 있습니다.

**Client Components:**

  * 프리렌더링 동안에는 서버에서 실행되지만 브라우저에서 실행되는 코드와 동일한 보안 가정을 따라야 합니다.
  * 권한 있는 데이터나 서버 전용 모듈에 접근해서는 안 됩니다.

이 설계 덕분에 앱은 기본적으로 안전하지만, 데이터를 가져오거나 컴포넌트로 전달하는 방식에 따라 개인 데이터가 실수로 노출될 수 있습니다.

### Tainting[](https://nextjs.org/docs/app/guides/data-security#tainting)

개인 데이터가 클라이언트에 실수로 전달되는 것을 막기 위해 React Taint API를 사용할 수 있습니다.

  * 데이터 객체용 [`experimental_taintObjectReference`](https://react.dev/reference/react/experimental_taintObjectReference)
  * 특정 값용 [`experimental_taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue)

Next.js 앱에서는 `next.config.js`의 [`experimental.taint`](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint) 옵션으로 활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      experimental: {
        taint: true,
      },
    }
[/code]

이렇게 하면 taint된 객체나 값을 클라이언트로 전달하지 못합니다. 다만 이는 추가적인 방어 계층일 뿐이므로, React 렌더링 컨텍스트에 전달하기 전에 [DAL](https://nextjs.org/docs/app/guides/data-security#data-access-layer)에서 데이터를 필터링하고 정제해야 합니다.

> **알아두면 좋아요:**
>
>   * 기본적으로 환경 변수는 서버에서만 사용할 수 있습니다. Next.js는 `NEXT_PUBLIC_` 접두사가 붙은 환경 변수를 클라이언트에 노출합니다. [자세히 알아보기](https://nextjs.org/docs/app/guides/environment-variables)
>   * 함수와 클래스는 기본적으로 Client Components로 전달되지 않도록 차단됩니다.
>

### 서버 전용 코드의 클라이언트 실행 방지[](https://nextjs.org/docs/app/guides/data-security#preventing-client-side-execution-of-server-only-code)

서버 전용 코드가 클라이언트에서 실행되지 않도록 [`server-only`](https://www.npmjs.com/package/server-only) 패키지로 모듈에 표시할 수 있습니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add server-only
[/code]

lib/data.ts
[code]
    import 'server-only'

    //...
[/code]

이렇게 하면 해당 모듈이 클라이언트 환경에서 import될 경우 빌드 오류를 발생시켜 독점 코드나 내부 비즈니스 로직이 서버에만 남게 됩니다.

## 데이터 변경[](https://nextjs.org/docs/app/guides/data-security#mutating-data)

Next.js는 [Server Actions](https://react.dev/reference/rsc/server-functions)로 변경 작업을 처리합니다.

### 내장 Server Actions 보안 기능[](https://nextjs.org/docs/app/guides/data-security#built-in-server-actions-security-features)

Server Action을 생성해 export하면 기본적으로 공개 HTTP 엔드포인트가 만들어지므로 동일한 보안 가정과 인가 검사를 적용해야 합니다. 즉, Server Action이나 유틸리티 함수가 코드의 다른 곳에서 import되지 않더라도 여전히 공개적으로 접근 가능합니다.

보안을 강화하기 위해 Next.js는 다음과 같은 내장 기능을 제공합니다.

  * **보안 액션 ID:** Next.js는 클라이언트가 Server Action을 참조하고 호출할 수 있도록 암호화된 비결정적 ID를 생성합니다. 이 ID는 보안을 강화하기 위해 빌드 사이사이에 주기적으로 재계산됩니다.
  * **데드 코드 제거:** 사용되지 않는 Server Action(ID로 참조됨)은 클라이언트 번들에서 제거되어 공개 접근을 방지합니다.

> **알아두면 좋아요** :
>
> ID는 컴파일 중 생성되며 최대 14일 동안 캐시됩니다. 새 빌드가 시작되거나 빌드 캐시가 무효화되면 다시 생성됩니다. 이 보안 개선은 인증 레이어가 누락된 경우의 위험을 줄여주지만, 여전히 Server Actions를 공개 HTTP 엔드포인트처럼 다뤄야 합니다.
[code]
    // app/actions.js
    'use server'
[/code]

// If this action **is** used in our application, Next.js
    // will create a secure ID to allow the client to reference
    // and call the Server Action.
    export async function updateUserAction(formData) {}

    // If this action **is not** used in our application, Next.js
    // will automatically remove this code during `next build`
    // and will not create a public endpoint.
    export async function deleteUserAction(formData) {}
[/code]

### 클라이언트 입력 검증[](https://nextjs.org/docs/app/guides/data-security#validating-client-input)

클라이언트 입력은 쉽게 변경될 수 있으므로 항상 검증해야 합니다. 예를 들어, 폼 데이터, URL 매개변수, 헤더, `searchParams` 등이 여기에 해당합니다:

app/page.tsx
[code]
    // BAD: Trusting searchParams directly
    export default async function Page({ searchParams }) {
      const isAdmin = searchParams.get('isAdmin')
      if (isAdmin === 'true') {
        // Vulnerable: relies on untrusted client data
        return <AdminPanel />
      }
    }

    // GOOD: Re-verify every time
    import { cookies } from 'next/headers'
    import { verifyAdmin } from './auth'

    export default async function Page() {
      const token = cookies().get('AUTH_TOKEN')
      const isAdmin = await verifyAdmin(token)

      if (isAdmin) {
        return <AdminPanel />
      }
    }
[/code]

### 인증 및 권한 부여[](https://nextjs.org/docs/app/guides/data-security#authentication-and-authorization)

사용자가 특정 작업을 수행할 권한이 있는지 항상 확인해야 합니다. 예를 들어:

app/actions.ts
[code]
    'use server'

    import { auth } from './lib'

    export function addItem() {
      const { user } = auth()
      if (!user) {
        throw new Error('You must be signed in to perform this action')
      }

      // ...
    }
[/code]

Next.js에서 [Authentication](https://nextjs.org/docs/app/guides/authentication)에 대해 더 알아보세요.

### 클로저와 암호화[](https://nextjs.org/docs/app/guides/data-security#closures-and-encryption)

컴포넌트 안에서 Server Action을 정의하면 해당 액션이 바깥 함수의 스코프에 접근할 수 있는 [클로저](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)가 만들어집니다. 예를 들어 `publish` 액션은 `publishVersion` 변수에 접근할 수 있습니다:

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const publishVersion = await getLatestVersion();

      async function publish() {
        "use server";
        if (publishVersion !== await getLatestVersion()) {
          throw new Error('The version has changed since pressing publish');
        }
        ...
      }

      return (
        <form>
          <button formAction={publish}>Publish</button>
        </form>
      );
    }
[/code]

클로저는 렌더링 시점의 데이터를 _스냅샷_ 으로 캡처해 나중에 액션이 호출될 때 사용할 수 있어야 할 때 유용합니다.

하지만 이를 위해 캡처된 변수가 액션 호출 시 클라이언트로 전송되고 다시 서버로 돌아옵니다. 민감한 데이터가 클라이언트에 노출되는 것을 막기 위해 Next.js는 클로저로 묶인 변수를 자동으로 암호화합니다. Next.js 애플리케이션이 빌드될 때마다 각 액션마다 새로운 개인 키가 생성되므로, 특정 빌드에서만 액션을 호출할 수 있습니다.

> **알아두면 좋아요:** 민감한 값이 클라이언트에 노출되는 것을 막기 위해 암호화에만 의존하는 것은 권장하지 않습니다.

### 암호화 키 덮어쓰기(고급)[](https://nextjs.org/docs/app/guides/data-security#overwriting-encryption-keys-advanced)

Next.js 애플리케이션을 여러 서버에 **자가 호스팅**하는 경우, 각 서버 인스턴스가 서로 다른 암호화 키를 갖게 되어 불일치가 발생할 수 있습니다.

이를 완화하려면 `process.env.NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` 환경 변수를 사용해 암호화 키를 덮어쓸 수 있습니다. 이 변수를 지정하면 빌드 간에도 암호화 키가 유지되며 모든 서버 인스턴스가 동일한 키를 사용합니다.

키는 base64로 인코딩된 값이어야 하며, 디코딩했을 때 길이가 유효한 AES 키 크기(16, 24, 32바이트)와 일치해야 합니다. Next.js는 기본적으로 32바이트 키를 생성합니다. 예를 들어 다음과 같이 플랫폼의 암호화 도구를 사용해 호환 키를 생성할 수 있습니다:
[code]
    openssl rand -base64 32
[/code]

이는 여러 배포 환경에서 일관된 암호화 동작이 중요한 고급 사용 사례입니다. 키 순환과 서명 같은 표준 보안 관행을 따르세요. 배포별 고려 사항은 [Self-Hosting 가이드](https://nextjs.org/docs/app/guides/self-hosting#server-functions-encryption-key)를 참조하세요.

### 허용된 오리진(고급)[](https://nextjs.org/docs/app/guides/data-security#allowed-origins-advanced)

Server Action은 `<form>` 요소에서 호출될 수 있으므로 [CSRF 공격](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)에 노출될 수 있습니다.

내부적으로 Server Action은 `POST` 메서드를 사용하며, 이 HTTP 메서드만 액션 호출에 허용됩니다. 이는 기본적으로 [SameSite 쿠키](https://web.dev/articles/samesite-cookies-explained)를 사용하는 현대 브라우저에서 대부분의 CSRF 취약점을 방지합니다.

추가 보호를 위해 Next.js의 Server Action은 [Origin 헤더](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)를 [Host 헤더](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host)(또는 `X-Forwarded-Host`)와 비교합니다. 둘이 일치하지 않으면 요청이 중단됩니다. 즉, Server Action은 해당 페이지를 호스팅하는 동일한 호스트에서만 호출될 수 있습니다.

대규모 애플리케이션에서 리버스 프록시나 다층 백엔드 아키텍처(서버 API와 프로덕션 도메인이 다른 경우)를 사용하는 경우, 안전한 오리진 목록을 지정하기 위해 [`serverActions.allowedOrigins`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions) 설정 옵션을 사용하는 것이 좋습니다. 이 옵션은 문자열 배열을 받습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    module.exports = {
      experimental: {
        serverActions: {
          allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
        },
      },
    }
[/code]

[Security and Server Actions](https://nextjs.org/blog/security-nextjs-server-components-actions)에 대해 더 자세히 알아보세요.

### 렌더링 중 부작용 방지[](https://nextjs.org/docs/app/guides/data-security#avoiding-side-effects-during-rendering)

뮤테이션(예: 사용자 로그아웃, 데이터베이스 업데이트, 캐시 무효화)은 Server 컴포넌트와 Client 컴포넌트 모두에서 부작용으로 발생해서는 안 됩니다. 예상치 못한 부작용을 방지하기 위해 Next.js는 렌더링 메서드 내에서 쿠키 설정이나 캐시 재검증을 명시적으로 막습니다.

app/page.tsx
[code]
    // BAD: Triggering a mutation during rendering
    export default async function Page({ searchParams }) {
      if (searchParams.get('logout')) {
        cookies().delete('AUTH_TOKEN')
      }

      return <UserProfile />
    }
[/code]

대신 Server Action을 사용해 뮤테이션을 처리해야 합니다.

app/page.tsx
[code]
    // GOOD: Using Server Actions to handle mutations
    import { logout } from './actions'

    export default function Page() {
      return (
        <>
          <UserProfile />
          <form action={logout}>
            <button type="submit">Logout</button>
          </form>
        </>
      )
    }
[/code]

> **알아두면 좋아요:** Next.js는 `POST` 요청을 사용해 뮤테이션을 처리합니다. 이는 GET 요청에서 발생할 수 있는 우발적 부작용을 방지해 CSRF 위험을 줄여 줍니다.

## 감사[](https://nextjs.org/docs/app/guides/data-security#auditing)

Next.js 프로젝트를 감사하는 경우 다음 영역을 특히 살펴보길 권장합니다:

  * **데이터 액세스 레이어:** 격리된 데이터 액세스 레이어에 대한 확립된 관행이 있나요? 데이터베이스 패키지와 환경 변수가 데이터 액세스 레이어 밖에서 임포트되지 않았는지 확인하세요.
  * **`"use client"` 파일:** 컴포넌트 prop이 민감한 데이터를 기대하나요? 타입 시그니처가 과도하게 넓지 않은가요?
  * **`"use server"` 파일:** 액션 인수는 액션 내부 또는 데이터 액세스 레이어에서 검증되고 있나요? 액션 내에서 사용자를 다시 인증하나요?
  * **`/[param]/.`** 대괄호가 있는 폴더는 사용자 입력입니다. 파라미터가 검증되나요?
  * **`proxy.ts` 및 `route.ts`:** 매우 강력합니다. 전통적인 기법으로 이 파일들을 추가로 감사하세요. 팀의 소프트웨어 개발 생명주기에 맞춰 침투 테스트 또는 취약성 스캐닝을 정기적으로 수행하세요.

## 다음 단계

이 가이드에서 언급한 주제에 대해 더 알아보세요.

- [인증](https://nextjs.org/docs/app/guides/authentication)
  - AuthenticationNext.js 애플리케이션에서 인증을 구현하는 방법을 알아보세요.

- [콘텐츠 보안 정책](https://nextjs.org/docs/app/guides/content-security-policy)
  - Content Security PolicyNext.js 애플리케이션에 콘텐츠 보안 정책(CSP)을 설정하는 방법을 알아보세요.

- [폼](https://nextjs.org/docs/app/guides/forms)
  - FormsReact Server Actions와 함께 Next.js에서 폼을 만드는 방법을 알아보세요.

보내기
