---
title: "Dropbox"
description: "원본 URL: https://next-auth.js.org/v3/providers/dropbox"
---

원본 URL: https://next-auth.js.org/v3/providers/dropbox

# Dropbox | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/dropbox#documentation "Direct link to heading")

<https://developers.dropbox.com/oauth-guide>

## 구성[​](https://next-auth.js.org/v3/providers/dropbox#configuration "Direct link to heading")

<https://www.dropbox.com/developers/apps>

## 옵션[​](https://next-auth.js.org/v3/providers/dropbox#options "Direct link to heading")

**Dropbox Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Dropbox Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/dropbox.js)

자신의 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/dropbox#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Dropbox({
        clientId: process.env.DROPBOX_CLIENT_ID,
        clientSecret: process.env.DROPBOX_CLIENT_SECRET
      })
    ]
    ...

```
