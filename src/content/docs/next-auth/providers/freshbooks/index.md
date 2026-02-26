---
title: "Freshbooks"
description: "Freshbooks Provider에는 기본 옵션 세트가 포함되어 있습니다."
---

Source URL: https://next-auth.js.org/providers/freshbooks

# Freshbooks | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/freshbooks#documentation "Direct link to heading")

<https://www.freshbooks.com/api/authenticating-with-oauth-2-0-on-the-new-freshbooks-api>

## 구성[​](https://next-auth.js.org/providers/freshbooks#configuration "Direct link to heading")

<https://my.freshbooks.com/#/developer>

## 옵션[​](https://next-auth.js.org/providers/freshbooks#options "Direct link to heading")

Freshbooks Provider에는 기본 옵션 세트가 포함되어 있습니다.

<https://www.freshbooks.com/api/start>

자체 사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/providers/freshbooks#example "Direct link to heading")

```
    import FreshbooksProvider from "next-auth/providers/freshbooks";
    ...
    providers: [
      FreshbooksProvider({
        clientId: process.env.FRESHBOOKS_CLIENT_ID,
        clientSecret: process.env.FRESHBOOKS_CLIENT_SECRET,
      })
    ]
    ...

```
