---
title: "LinkedIn"
description: "Auth 탭에서 client ID와 client secret을 확인하세요. 같은 탭에서 http://localhost:3000/api/auth/callback/linkedin 같은 redirect URL을 추가해 LinkedIn이 애플리케이션으로 올바르게 다시 리디렉션..."
---

Source URL: https://next-auth.js.org/providers/linkedin

# LinkedIn | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/linkedin#documentation "헤딩으로 바로 가는 링크")

<https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow>

## 구성[​](https://next-auth.js.org/providers/linkedin#configuration "헤딩으로 바로 가는 링크")

<https://www.linkedin.com/developers/apps/>

Auth 탭에서 client ID와 client secret을 확인하세요. 같은 탭에서 http://localhost:3000/api/auth/callback/linkedin 같은 redirect URL을 추가해 LinkedIn이 애플리케이션으로 올바르게 다시 리디렉션할 수 있도록 설정합니다. 마지막으로 Products 탭으로 이동해 "Sign In with LinkedIn" 제품을 활성화하세요. 테스트를 진행하기 전에 LinkedIn 팀이 요청을 검토하고 승인해야 합니다.

![image](https://user-images.githubusercontent.com/330396/114429603-68195600-9b72-11eb-8311-62e58383c42b.png)

## 옵션[​](https://next-auth.js.org/providers/linkedin#options "헤딩으로 바로 가는 링크")

**LinkedIn Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [LinkedIn Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/linkedin.ts)

사용 사례에 맞게 원하는 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/linkedin#example "헤딩으로 바로 가는 링크")

```
    import LinkedInProvider from "next-auth/providers/linkedin";
    ...
    providers: [
      LinkedInProvider({
        clientId: process.env.LINKEDIN_CLIENT_ID,
        clientSecret: process.env.LINKEDIN_CLIENT_SECRET
      })
    ]
    ...

```
