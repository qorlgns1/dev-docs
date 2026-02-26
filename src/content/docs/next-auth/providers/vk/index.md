---
title: '문서[​](https://next-auth.js.org/providers/vk#documentation "Direct link to heading")'
description: "필요에 맞게 모든 옵션을 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/providers/vk

# VK | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/vk#documentation "Direct link to heading")

<https://vk.com/dev/first_guide>

## 설정[​](https://next-auth.js.org/providers/vk#configuration "Direct link to heading")

<https://vk.com/apps?act=manage>

## 옵션[​](https://next-auth.js.org/providers/vk#options "Direct link to heading")

**VK Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [VK Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/vk.ts)

필요에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/vk#example "Direct link to heading")

```
    import VkProvider from "next-auth/providers/vk";
    ...
    providers: [
      VkProvider({
        clientId: process.env.VK_CLIENT_ID,
        clientSecret: process.env.VK_CLIENT_SECRET
      })
    ]
    ...

```

참고

기본적으로 이 provider는 API 버전 `5.131`을 사용합니다. 자세한 내용은 <https://vk.com/dev/versions>를 참고하세요.

다른 버전을 사용하려면 provider의 options 객체에 해당 버전을 전달할 수 있습니다:

```
    // pages/api/auth/[...nextauth].js

    const apiVersion = "5.131"
    ...
    providers: [
      VkProvider({
        accessTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        requestTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        authorizationUrl:
          `https://oauth.vk.com/authorize?response_type=code&v=${apiVersion}`,
        profileUrl: `https://api.vk.com/method/users.get?fields=photo_100&v=${apiVersion}`,
      })
    ]
    ...

```
