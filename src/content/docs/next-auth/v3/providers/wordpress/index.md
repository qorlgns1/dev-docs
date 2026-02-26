---
title: "WordPress.com"
description: "원본 URL: https://next-auth.js.org/v3/providers/wordpress"
---

원본 URL: https://next-auth.js.org/v3/providers/wordpress

# WordPress.com | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/wordpress#documentation "Direct link to heading")

<https://developer.wordpress.com/docs/oauth2/>

## 구성[​](https://next-auth.js.org/v3/providers/wordpress#configuration "Direct link to heading")

<https://developer.wordpress.com/apps/>

## 옵션[​](https://next-auth.js.org/v3/providers/wordpress#options "Direct link to heading")

**Wordpress Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Wordpress Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/wordpress.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/wordpress#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.WordPress({
        clientId: process.env.WORDPRESS_CLIENT_ID,
        clientSecret: process.env.WORDPRESS_CLIENT_SECRET
      })
    }
    ...

```

tip

애플리케이션을 등록해 <https://developer.wordpress.com/apps/>에서 Client ID와 Client Secret을 발급받으세요. Type은 Web로 선택하고, Redirect URL은 `http://example.com/api/auth/callback/wordpress`로 설정하세요. 여기서 example.com은 사이트 도메인입니다.
