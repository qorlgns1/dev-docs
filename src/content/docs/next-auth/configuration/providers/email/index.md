---
title: "Email"
description: 'Email provider는 사용자가 클릭해 로그인할 수 있는 이메일 "매직 링크"를 전송합니다. Slack 같은 소프트웨어를 사용해 봤다면 이미 보셨을 가능성이 큽니다.'
---

Source URL: https://next-auth.js.org/configuration/providers/email

# Email | NextAuth.js

버전: v4

### nodemailer 설치[​](https://next-auth.js.org/configuration/providers/email#install-nodemailer "Direct link to heading")

- npm
- yarn
- pnpm

```
    npm install nodemailer
```

```
    yarn add nodemailer
```

```
    pnpm add nodemailer
```

### 사용 방법[​](https://next-auth.js.org/configuration/providers/email#how-to "Direct link to heading")

Email provider는 사용자가 클릭해 로그인할 수 있는 이메일 "매직 링크"를 전송합니다. Slack 같은 소프트웨어를 사용해 봤다면 이미 보셨을 가능성이 큽니다.

하나 이상의 OAuth 서비스와 함께 이메일 로그인 지원을 추가하면, 사용자가 OAuth 계정에 접근할 수 없게 되었을 때(예: 계정이 잠기거나 삭제된 경우) 로그인할 수 있는 방법을 제공합니다.

설정 방식은 다른 provider와 비슷하지만, 옵션은 다릅니다:

pages/api/auth/[...nextauth].js

```
    import EmailProvider from "next-auth/providers/email"
    ...
    providers: [
      EmailProvider({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM,
        // maxAge: 24 * 60 * 60, // How long email links are valid for (default 24h)
      }),
    ],
    ...

```

이메일 로그인 설정에 대한 자세한 내용은 [Email provider documentation](https://next-auth.js.org/providers/email)을 참고하세요.

note

Email provider는 데이터베이스가 필요하며, 데이터베이스 없이 사용할 수 없습니다.

### 옵션[​](https://next-auth.js.org/configuration/providers/email#options "Direct link to heading")

| 이름                    | 설명                                                                            | 타입                             | 필수   |
| ----------------------- | ------------------------------------------------------------------------------- | -------------------------------- | ------ |
| id                      | provider의 고유 ID                                                              | `string`                         | 아니요 |
| name                    | provider의 설명용 이름                                                          | `string`                         | 아니요 |
| type                    | provider 타입, 이 경우 `email`                                                  | `"email"`                        | 아니요 |
| server                  | 이메일 서버를 가리키는 경로 또는 객체                                           | `string` 또는 `Object`           | 아니요 |
| sendVerificationRequest | 인증 요청 전송 시 실행할 콜백, 기본값은 nodemailer 사용                         | `(params) => Promise<undefined>` | 아니요 |
| from                    | 이메일 발신 주소, 기본값: "[no-reply@example.com](mailto:no-reply@example.com)" | `string`                         | 아니요 |
| maxAge                  | 이메일로 사용자를 로그인시킬 수 있는 유효 시간(초). 기본값은 1일                | `number`                         | 아니요 |
