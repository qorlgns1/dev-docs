---
title: "WordPress.com"
description: "원본 URL: https://next-auth.js.org/providers/wordpress"
---

원본 URL: https://next-auth.js.org/providers/wordpress

# WordPress.com | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/wordpress#documentation "제목으로 바로 가는 링크")

<https://developer.wordpress.com/docs/oauth2/>

## 설정[​](https://next-auth.js.org/providers/wordpress#configuration "제목으로 바로 가는 링크")

<https://developer.wordpress.com/apps/>

## 옵션[​](https://next-auth.js.org/providers/wordpress#options "제목으로 바로 가는 링크")

**Wordpress Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Wordpress Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/wordpress.js)

각 옵션은 사용 사례에 맞게 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/wordpress#example "제목으로 바로 가는 링크")

```
    import WordpressProvider from "next-auth/providers/wordpress";
    ...
    providers: [
      WordpressProvider({
        clientId: process.env.WORDPRESS_CLIENT_ID,
        clientSecret: process.env.WORDPRESS_CLIENT_SECRET
      })
    }
    ...

```

tip

<https://developer.wordpress.com/apps/>에서 애플리케이션을 등록해 Client ID와 Client Secret을 발급받으세요. Type은 Web으로 선택하고 Redirect URL은 `http://example.com/api/auth/callback/wordpress`로 설정하세요. 여기서 example.com은 사이트 도메인입니다.
