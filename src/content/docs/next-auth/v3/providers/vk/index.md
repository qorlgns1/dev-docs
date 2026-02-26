---
title: '문서[​](https://next-auth.js.org/v3/providers/vk#documentation "제목으로 바로 가는 링크")'
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

원문 URL: https://next-auth.js.org/v3/providers/vk

# VK | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/vk#documentation "제목으로 바로 가는 링크")

<https://vk.com/dev/first_guide>

## 구성[​](https://next-auth.js.org/v3/providers/vk#configuration "제목으로 바로 가는 링크")

<https://vk.com/apps?act=manage>

## 옵션[​](https://next-auth.js.org/v3/providers/vk#options "제목으로 바로 가는 링크")

**VK Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [VK Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/vk.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/vk#example "제목으로 바로 가는 링크")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.VK({
        clientId: process.env.VK_CLIENT_ID,
        clientSecret: process.env.VK_CLIENT_SECRET
      })
    ]
    ...

```

참고

기본적으로 provider는 API `5.126` 버전을 사용합니다. 자세한 내용은 <https://vk.com/dev/versions> 를 참고하세요.

다른 버전을 사용하려면 provider의 options 객체에 해당 버전을 전달할 수 있습니다:

```
    // pages/api/auth/[...nextauth].js

    const apiVersion = "5.126"
    ...
    providers: [
      Providers.VK({
        accessTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        requestTokenUrl: `https://oauth.vk.com/access_token?v=${apiVersion}`,
        authorizationUrl:
          `https://oauth.vk.com/authorize?response_type=code&v=${apiVersion}`,
        profileUrl: `https://api.vk.com/method/users.get?fields=photo_100&v=${apiVersion}`,
      })
    ]
    ...

```
