---
title: "WorkOS"
description: "원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/workos

# WorkOS | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/workos#documentation "Direct link to heading")

<https://workos.com/docs/sso/guide>

## 구성[​](https://next-auth.js.org/providers/workos#configuration "Direct link to heading")

<https://dashboard.workos.com>

## 옵션[​](https://next-auth.js.org/providers/workos#options "Direct link to heading")

**WorkOS Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [WorkOS Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/workos.ts)

원하는 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/workos#example "Direct link to heading")

```
    import WorkOSProvider from "next-auth/providers/workos";
    ...
    providers: [
      WorkOSProvider({
        clientId: process.env.WORKOS_CLIENT_ID,
        clientSecret: process.env.WORKOS_API_KEY,
      }),
    ],
    ...

```

WorkOS는 자체적으로 신원 제공자(identity provider)가 아니라, 여러 single sign-on(SSO) 제공자를 연결하는 브리지입니다. 따라서 WorkOS를 사용해 사용자를 인증하려면 몇 가지 추가 변경이 필요합니다.

WorkOS를 사용해 사용자를 로그인시키려면 어떤 WorkOS Connection을 사용할지 지정해야 합니다. 사용할 연결을 지정하려면 `organization` 또는 `connection` `authorizationParams`를 사용해야 합니다.

```
    import { signIn } from "next-auth/react"

    const organization = 'ORGANIZATION_ID';
    signIn(provider.id, undefined, {
      organization,
    });

```

이는 사용자 지정 로그인 페이지를 사용해 구현할 수 있습니다. [WorkOS SSO와 NextAuth.js로 Next.js 애플리케이션 만들기](https://workos.com/docs/integrations/next-auth/6-creating-a-custom-login-page)를 참고하세요.
