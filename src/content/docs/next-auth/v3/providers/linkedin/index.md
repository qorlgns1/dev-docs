---
title: "LinkedIn"
description: "원본 URL: https://next-auth.js.org/v3/providers/linkedin"
---

원본 URL: https://next-auth.js.org/v3/providers/linkedin

# LinkedIn | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/linkedin#documentation "Direct link to heading")

<https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow>

## 구성[​](https://next-auth.js.org/v3/providers/linkedin#configuration "Direct link to heading")

<https://www.linkedin.com/developers/apps/>

Auth 탭에서 client ID와 client secret을 가져오세요. 같은 탭에서 LinkedIn이 애플리케이션으로 올바르게 다시 리디렉션할 수 있도록 `http://localhost:3000/api/auth/callback/linkedin` 같은 redirect URL을 추가하세요. 마지막으로 Products 탭으로 이동해 "Sign In with LinkedIn" 제품을 활성화하세요. 테스트를 진행하기 전에 LinkedIn 팀이 요청을 검토하고 승인해야 합니다.

![image](https://user-images.githubusercontent.com/330396/114429603-68195600-9b72-11eb-8311-62e58383c42b.png)

## 옵션[​](https://next-auth.js.org/v3/providers/linkedin#options "Direct link to heading")

**LinkedIn Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [LinkedIn Provider 옵션](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/linkedin.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/linkedin#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.LinkedIn({
        clientId: process.env.LINKEDIN_CLIENT_ID,
        clientSecret: process.env.LINKEDIN_CLIENT_SECRET
      })
    ]
    ...

```
