---
title: "Dropbox"
description: "자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/dropbox

# Dropbox | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/dropbox#documentation "제목으로 직접 연결")

<https://developers.dropbox.com/oauth-guide>

## 구성[​](https://next-auth.js.org/providers/dropbox#configuration "제목으로 직접 연결")

<https://www.dropbox.com/developers/apps>

## 옵션[​](https://next-auth.js.org/providers/dropbox#options "제목으로 직접 연결")

**Dropbox Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Dropbox Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/dropbox.js)

자신의 사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/dropbox#example "제목으로 직접 연결")

```
    import DropboxProvider from "next-auth/providers/dropbox";
    ...
    providers: [
      DropboxProvider({
        clientId: process.env.DROPBOX_CLIENT_ID,
        clientSecret: process.env.DROPBOX_CLIENT_SECRET
      })
    ]
    ...

```
