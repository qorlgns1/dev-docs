---
title: 'next.config.js: taint'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 GitHub에서 의견을 공유해 주세요.'
---

# next.config.js: taint | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/taint

Copy page

# taint

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 의견을 공유해 주세요.

마지막 업데이트 2026년 2월 20일

## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#usage)

`taint` 옵션은 객체와 값을 오염(taint)시키는 실험적 React API 지원을 활성화합니다. 이 기능은 민감한 데이터가 실수로 클라이언트로 전달되는 것을 방지하는 데 도움이 됩니다. 활성화하면 다음을 사용할 수 있습니다.

  * [`experimental_taintObjectReference`](https://react.dev/reference/react/experimental_taintObjectReference)로 객체 참조를 오염시킵니다.
  * [`experimental_taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue)로 고유 값을 오염시킵니다.

> **알아두면 좋아요**: 이 플래그를 활성화하면 `app` 디렉터리에서 React `experimental` 채널도 함께 활성화됩니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      experimental: {
        taint: true,
      },
    }

    export default nextConfig
[/code]

> **경고:** 민감한 데이터를 클라이언트에 노출하지 않기 위한 유일한 메커니즘으로 taint API에만 의존하지 마세요. [보안 권장 사항](https://nextjs.org/blog/security-nextjs-server-components-actions)을 참고하세요.

taint API는 서버-클라이언트 경계를 통과할 수 없는 데이터를 선언적으로 명시하여 방어적으로 대응할 수 있게 해 줍니다. 객체나 값이 서버-클라이언트 경계를 통과하면 React는 오류를 발생시킵니다.

다음과 같은 경우에 유용합니다.

  * 데이터를 읽는 메서드를 직접 제어할 수 없을 때
  * 직접 정의하지 않은 민감한 데이터 형태를 다뤄야 할 때
  * 서버 컴포넌트 렌더링 중에 민감한 데이터에 접근할 때

민감한 데이터가 필요 없는 컨텍스트로 반환되지 않도록 데이터와 API를 모델링하는 것이 좋습니다.

## Caveats[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#caveats)

  * taint 처리는 참조로 객체를 추적할 수 있을 뿐입니다. 객체를 복사하면 오염되지 않은 새 버전이 생성되어 API가 제공하던 모든 보장이 사라집니다. 복사본도 다시 오염시켜야 합니다.
  * taint 처리는 오염된 값에서 파생된 데이터를 추적할 수 없습니다. 파생 값 역시 오염시켜야 합니다.
  * 값은 수명 동안 참조가 스코프에 있는 한 오염된 상태로 유지됩니다. 자세한 내용은 [`experimental_taintUniqueValue` 매개변수 참조](https://react.dev/reference/react/experimental_taintUniqueValue#parameters)를 확인하세요.

## Examples[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#examples)

### Tainting an object reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#tainting-an-object-reference)

이 예에서는 `getUserDetails` 함수가 특정 사용자에 대한 데이터를 반환합니다. 서버-클라이언트 경계를 넘지 못하도록 사용자 객체 참조를 오염시킵니다. 예를 들어 `UserCard`가 클라이언트 컴포넌트라고 가정합니다.
[code]
    import { experimental_taintObjectReference } from 'react'

    function getUserDetails(id: string): UserDetails {
      const user = await db.queryUserById(id)

      experimental_taintObjectReference(
        'Do not use the entire user info object. Instead, select only the fields you need.',
        user
      )

      return user
    }
[/code]

오염된 `userDetails` 객체에서도 개별 필드에는 계속 접근할 수 있습니다.
[code]
    export async function ContactPage({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const userDetails = await getUserDetails(id)

      return (
        <UserCard
          firstName={userDetails.firstName}
          lastName={userDetails.lastName}
        />
      )
    }
[/code]

이제 전체 객체를 클라이언트 컴포넌트에 전달하면 오류가 발생합니다.
[code]
    export async function ContactPage({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const userDetails = await getUserDetails(id)

      // Throws an error
      return <UserCard user={userDetails} />
    }
[/code]

### Tainting a unique value[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#tainting-a-unique-value)

이 경우 `config.getConfigDetails` 호출을 await 하여 서버 구성을 가져올 수 있습니다. 그러나 시스템 구성에는 클라이언트에 노출하고 싶지 않은 `SERVICE_API_KEY`가 포함되어 있습니다.

`config.SERVICE_API_KEY` 값을 오염시킬 수 있습니다.
[code]
    import { experimental_taintUniqueValue } from 'react'

    function getSystemConfig(): SystemConfig {
      const config = await config.getConfigDetails()

      experimental_taintUniqueValue(
        'Do not pass configuration tokens to the client',
        config,
        config.SERVICE_API_KEY
      )

      return config
    }
[/code]

`systemConfig` 객체의 다른 속성에는 여전히 접근할 수 있습니다.
[code]
    export async function Dashboard() {
      const systemConfig = await getSystemConfig()

      return <ClientDashboard version={systemConfig.SERVICE_API_VERSION} />
    }
[/code]

하지만 `SERVICE_API_KEY`를 `ClientDashboard`에 전달하면 오류가 발생합니다.
[code]
    export async function Dashboard() {
      const systemConfig = await getSystemConfig()
      // Someone makes a mistake in a PR
      const version = systemConfig.SERVICE_API_KEY

      return <ClientDashboard version={version} />
    }
[/code]

`systemConfig.SERVICE_API_KEY`가 새 변수에 재할당되더라도, 클라이언트 컴포넌트에 전달하면 여전히 오류가 발생한다는 점에 유의하세요.

반면, 오염된 고유 값에서 파생된 값은 클라이언트에 노출됩니다.
[code]
    export async function Dashboard() {
      const systemConfig = await getSystemConfig()
      // Someone makes a mistake in a PR
      const version = `version::${systemConfig.SERVICE_API_KEY}`

      return <ClientDashboard version={version} />
    }
[/code]

더 나은 접근 방식은 `getSystemConfig`가 반환하는 데이터에서 `SERVICE_API_KEY`를 제거하는 것입니다.

Was this helpful?

supported.

Send
