---
title: '개요[​](https://next-auth.js.org/v3/providers/email#overview "Direct link to heading")'
description: 'Email provider는 이메일을 사용해 로그인에 사용할 수 있는 "매직 링크"를 전송합니다. Slack 같은 서비스를 사용해 봤다면 이미 보셨을 가능성이 높습니다.'
---

Source URL: https://next-auth.js.org/v3/providers/email

# 이메일 | NextAuth.js

버전: v3

## 개요[​](https://next-auth.js.org/v3/providers/email#overview "Direct link to heading")

Email provider는 이메일을 사용해 로그인에 사용할 수 있는 "매직 링크"를 전송합니다. Slack 같은 서비스를 사용해 봤다면 이미 보셨을 가능성이 높습니다.

하나 이상의 OAuth 서비스에 더해 이메일 로그인 지원을 추가하면, 사용자가 OAuth 계정에 접근할 수 없게 되었을 때(예: 잠기거나 삭제된 경우) 로그인할 수 있는 방법을 제공할 수 있습니다.

Email provider는 하나 이상의 OAuth provider와 함께(또는 이를 대신해) 사용할 수 있습니다.

### 동작 방식[​](https://next-auth.js.org/v3/providers/email#how-it-works "Direct link to heading")

최초 로그인 시, 입력한 이메일 주소로 **Verification Token**이 전송됩니다. 기본적으로 이 토큰은 24시간 동안 유효합니다. 해당 시간 내에 Verification Token을 사용하면(즉, 이메일의 링크를 클릭하면) 사용자 계정이 생성되고 로그인됩니다.

로그인할 때 누군가 _기존 계정_ 의 이메일 주소를 입력하면 이메일이 전송되고, 이메일의 링크를 따라가면 해당 이메일 주소에 연결된 계정으로 로그인됩니다.

tip

Email Provider는 JSON Web Token 및 데이터베이스 세션 모두와 함께 사용할 수 있지만, 이를 사용하려면 데이터베이스를 **반드시** 설정해야 합니다. 데이터베이스 없이 이메일 로그인을 활성화하는 것은 불가능합니다.

## 옵션[​](https://next-auth.js.org/v3/providers/email#options "Direct link to heading")

**Email Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Email Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/email.js)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 구성[​](https://next-auth.js.org/v3/providers/email#configuration "Direct link to heading")

1. SMTP 계정이 필요합니다. 가능하면 [nodemailer와 함께 동작하는 것으로 알려진 서비스](http://nodemailer.com/smtp/well-known/) 중 하나를 사용하는 것이 좋습니다.
2. SMTP 서버 연결을 구성하는 방법은 두 가지입니다.

연결 문자열 또는 nodemailer 구성 객체를 사용할 수 있습니다.

2.1 **연결 문자열 사용**

프로젝트 루트에 .env 파일을 만들고 연결 문자열과 이메일 주소를 추가합니다.

.env

```
        EMAIL_SERVER=smtp://username:password@smtp.example.com:587
        EMAIL_FROM=noreply@example.com

```

이제 다음과 같이 email provider를 추가할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    providers: [
      Providers.Email({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM
      }),
    ],

```

2.2 **구성 객체 사용**

프로젝트 루트의 `.env` 파일에서 구성 객체 옵션을 각각 개별적으로 추가하면 됩니다.

.env

```
    EMAIL_SERVER_USER=username
    EMAIL_SERVER_PASSWORD=password
    EMAIL_SERVER_HOST=smtp.example.com
        EMAIL_SERVER_PORT=587
        EMAIL_FROM=noreply@example.com

```

이제 Email Provider에서 NextAuth.js 옵션 객체에 provider 설정을 추가할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    providers: [
      Providers.Email({
        server: {
          host: process.env.EMAIL_SERVER_HOST,
          port: process.env.EMAIL_SERVER_PORT,
          auth: {
            user: process.env.EMAIL_SERVER_USER,
            pass: process.env.EMAIL_SERVER_PASSWORD
          }
        },
        from: process.env.EMAIL_FROM
      }),
    ],

```

3. 이제 `/api/auth/signin` 에서 이메일 주소로 로그인할 수 있습니다.

사용자 계정(즉, Users 테이블의 항목)은 사용자가 처음으로 이메일 주소를 인증하기 전까지는 생성되지 않습니다. 이메일 주소가 이미 계정과 연결되어 있다면, 사용자가 이메일의 링크를 사용할 때 해당 계정으로 로그인됩니다.

## 이메일 커스터마이징[​](https://next-auth.js.org/v3/providers/email#customising-emails "Direct link to heading")

`Providers.Email()` 에 `sendVerificationRequest` 옵션으로 사용자 정의 함수를 전달하면 전송되는 로그인 이메일을 완전히 커스터마이징할 수 있습니다.

예:

pages/api/auth/[...nextauth].js

```
    providers: [
      Providers.Email({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM,
        sendVerificationRequest: ({
          identifier: email,
          url,
          token,
          baseUrl,
          provider,
        }) => {
          /* your function */
        },
      }),
    ]

```

다음 코드는 내장 `sendVerificationRequest()` 메서드의 전체 소스를 보여줍니다:

```
    import nodemailer from "nodemailer"

    const sendVerificationRequest = ({
      identifier: email,
      url,
      token,
      baseUrl,
      provider,
    }) => {
      return new Promise((resolve, reject) => {
        const { server, from } = provider
        // Strip protocol from URL and use domain as site name
        const site = baseUrl.replace(/^https?:\/\//, "")

        nodemailer.createTransport(server).sendMail(
          {
            to: email,
            from,
            subject: `Sign in to ${site}`,
            text: text({ url, site, email }),
            html: html({ url, site, email }),
          },
          (error) => {
            if (error) {
              logger.error("SEND_VERIFICATION_EMAIL_ERROR", email, error)
              return reject(new Error("SEND_VERIFICATION_EMAIL_ERROR", error))
            }
            return resolve()
          }
        )
      })
    }

    // Email HTML body
    const html = ({ url, site, email }) => {
      // Insert invisible space into domains and email address to prevent both the
      // email address and the domain from being turned into a hyperlink by email
      // clients like Outlook and Apple mail, as this is confusing because it seems
      // like they are supposed to click on their email address to sign in.
      const escapedEmail = `${email.replace(/\./g, "&#8203;.")}`
      const escapedSite = `${site.replace(/\./g, "&#8203;.")}`

      // Some simple styling options
      const backgroundColor = "#f9f9f9"
      const textColor = "#444444"
      const mainBackgroundColor = "#ffffff"
      const buttonBackgroundColor = "#346df1"
      const buttonBorderColor = "#346df1"
      const buttonTextColor = "#ffffff"

      // Uses tables for layout and inline CSS due to email client limitations
      return `
    <body style="background: ${backgroundColor};">
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td align="center" style="padding: 10px 0px 20px 0px; font-size: 22px; font-family: Helvetica, Arial, sans-serif; color: ${textColor};">
            <strong>${escapedSite}</strong>
          </td>
        </tr>
      </table>
      <table width="100%" border="0" cellspacing="20" cellpadding="0" style="background: ${mainBackgroundColor}; max-width: 600px; margin: auto; border-radius: 10px;">
        <tr>
          <td align="center" style="padding: 10px 0px 0px 0px; font-size: 18px; font-family: Helvetica, Arial, sans-serif; color: ${textColor};">
            Sign in as <strong>${escapedEmail}</strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 20px 0;">
            <table border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td align="center" style="border-radius: 5px;" bgcolor="${buttonBackgroundColor}"><a href="${url}" target="_blank" style="font-size: 18px; font-family: Helvetica, Arial, sans-serif; color: ${buttonTextColor}; text-decoration: none; text-decoration: none;border-radius: 5px; padding: 10px 20px; border: 1px solid ${buttonBorderColor}; display: inline-block; font-weight: bold;">Sign in</a></td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px 0px 10px 0px; font-size: 16px; line-height: 22px; font-family: Helvetica, Arial, sans-serif; color: ${textColor};">
            If you did not request this email you can safely ignore it.
          </td>
        </tr>
      </table>
    </body>
    `
    }

    // Email text body – fallback for email clients that don't render HTML
    const text = ({ url, site }) => `Sign in to ${site}\n${url}\n\n`

```

tip

React로 이메일 클라이언트 호환성이 뛰어난 멋진 HTML을 생성하고 싶다면 <https://mjml.io> 를 확인해 보세요.

## Verification Token 커스터마이징[​](https://next-auth.js.org/v3/providers/email#customising-the-verification-token "Direct link to heading")

기본적으로 무작위 verification token이 생성됩니다. 이를 재정의하려면 provider 옵션에 `generateVerificationToken` 메서드를 정의할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    providers: [
      Providers.Email({
        async generateVerificationToken() {
          return "ABC123"
        }
      })
    ],

```
