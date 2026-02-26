---
title: '개요[\u200b](https://next-auth.js.org/providers/email#overview "Direct link to heading")'
description: 'Email provider는 로그인에 사용할 수 있는 "magic links"를 이메일로 전송하며, Slack 같은 서비스를 사용해 봤다면 아마 본 적이 있을 것입니다.'
---

Source URL: https://next-auth.js.org/providers/email

# 이메일 | NextAuth.js

버전: v4

## 개요[​](https://next-auth.js.org/providers/email#overview "Direct link to heading")

Email provider는 로그인에 사용할 수 있는 "magic links"를 이메일로 전송하며, Slack 같은 서비스를 사용해 봤다면 아마 본 적이 있을 것입니다.

하나 이상의 OAuth 서비스에 더해 이메일 로그인 지원을 추가하면, 사용자가 OAuth 계정(예: 잠기거나 삭제된 경우)에 접근하지 못할 때 로그인할 수 있는 방법을 제공할 수 있습니다.

Email provider는 하나 이상의 OAuth provider와 함께(또는 대신) 사용할 수 있습니다.

### 작동 방식[​](https://next-auth.js.org/providers/email#how-it-works "Direct link to heading")

최초 로그인 시, 입력한 이메일 주소로 **Verification Token**이 전송됩니다. 기본적으로 이 토큰은 24시간 동안 유효합니다. 해당 시간 내에 Verification Token이 사용되면(즉, 이메일의 링크를 클릭하면) 사용자 계정이 생성되고 로그인됩니다.

로그인할 때 _기존 계정_ 의 이메일 주소를 입력하면 이메일이 전송되며, 이메일의 링크를 따라가면 해당 이메일 주소에 연결된 계정으로 로그인됩니다.

tip

Email Provider는 JSON Web Tokens 및 데이터베이스 세션 모두와 함께 사용할 수 있지만, 이를 사용하려면 데이터베이스를 **반드시** 설정해야 합니다. 데이터베이스 없이 이메일 로그인을 활성화하는 것은 불가능합니다.

## 옵션[​](https://next-auth.js.org/providers/email#options "Direct link to heading")

**Email Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Email Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/email.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 설정[​](https://next-auth.js.org/providers/email#configuration "Direct link to heading")

NextAuth.js는 HTTP 또는 SMTP를 통해 이메일을 보낼 수 있습니다.

### HTTP[​](https://next-auth.js.org/providers/email#http "Direct link to heading")

[HTTP-based Email Provider](https://authjs.dev/guides/configuring-http-email) 가이드를 확인하세요.

### SMTP[​](https://next-auth.js.org/providers/email#smtp "Direct link to heading")

1. NextAuth.js는 `nodemailer`를 의존성으로 포함하지 않으므로, Email Provider를 사용하려면 직접 설치해야 합니다. `npm install nodemailer` 또는 `yarn add nodemailer`를 실행하세요.
2. SMTP 계정이 필요합니다. 이상적으로는 [`nodemailer`와 동작이 검증된 서비스](https://community.nodemailer.com/2-0-0-beta/setup-smtp/well-known-services/) 중 하나를 사용하세요.
3. SMTP 서버 연결을 설정하는 방법은 두 가지입니다.

연결 문자열을 사용하거나 `nodemailer` 설정 객체 또는 transport를 사용할 수 있습니다.

2.1 **연결 문자열 사용**

프로젝트 루트에 `.env` 파일을 만들고 연결 문자열과 이메일 주소를 추가합니다.

.env

```
        EMAIL_SERVER=smtp://username:password@smtp.example.com:587
        EMAIL_FROM=noreply@example.com

```

이제 다음과 같이 email provider를 추가할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import EmailProvider from "next-auth/providers/email";
    ...
    providers: [
      EmailProvider({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM
      }),
    ],

```

2.2 **설정 객체 사용**

프로젝트 루트의 `.env` 파일에 설정 객체 옵션을 각각 개별적으로 추가하면 됩니다.

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
    import EmailProvider from "next-auth/providers/email";
    ...
    providers: [
      EmailProvider({
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

3. Email verification token 저장을 위해 데이터베이스 [adapters](https://authjs.dev/getting-started/database) 중 하나를 설정하는 것을 잊지 마세요.

4. 이제 `/api/auth/signin`에서 이메일 주소로 로그인할 수 있습니다.

사용자 계정(즉, Users 테이블의 항목)은 사용자가 처음으로 이메일 주소를 인증하기 전까지 생성되지 않습니다. 이메일 주소가 이미 계정에 연결되어 있다면, 사용자가 이메일의 링크를 사용할 때 해당 계정으로 로그인됩니다.

## 이메일 커스터마이징[​](https://next-auth.js.org/providers/email#customizing-emails "Direct link to heading")

`EmailProvider()`의 `sendVerificationRequest` 옵션으로 사용자 정의 함수를 전달하면 전송되는 로그인 이메일을 완전히 커스터마이징할 수 있습니다.

예시:

pages/api/auth/[...nextauth].js

```
    import EmailProvider from "next-auth/providers/email";
    ...
    providers: [
      EmailProvider({
        server: process.env.EMAIL_SERVER,
        from: process.env.EMAIL_FROM,
        sendVerificationRequest({
          identifier: email,
          url,
          provider: { server, from },
        }) {
          /* your function */
        },
      }),
    ]

```

다음 코드는 내장 `sendVerificationRequest()` 메서드의 전체 소스를 보여줍니다:

```
    import { createTransport } from "nodemailer"

    async function sendVerificationRequest(params) {
      const { identifier, url, provider, theme } = params
      const { host } = new URL(url)
      // NOTE: You are not required to use `nodemailer`, use whatever you want.
      const transport = createTransport(provider.server)
      const result = await transport.sendMail({
        to: identifier,
        from: provider.from,
        subject: `Sign in to ${host}`,
        text: text({ url, host }),
        html: html({ url, host, theme }),
      })
      const failed = result.rejected.concat(result.pending).filter(Boolean)
      if (failed.length) {
        throw new Error(`Email(s) (${failed.join(", ")}) could not be sent`)
      }
    }

    /**
     * Email HTML body
     * Insert invisible space into domains from being turned into a hyperlink by email
     * clients like Outlook and Apple mail, as this is confusing because it seems
     * like they are supposed to click on it to sign in.
     *
     * @note We don't add the email address to avoid needing to escape it, if you do, remember to sanitize it!
     */
    function html(params: { url: string, host: string, theme: Theme }) {
      const { url, host, theme } = params

      const escapedHost = host.replace(/\./g, "&#8203;.")

      const brandColor = theme.brandColor || "#346df1"
      const color = {
        background: "#f9f9f9",
        text: "#444",
        mainBackground: "#fff",
        buttonBackground: brandColor,
        buttonBorder: brandColor,
        buttonText: theme.buttonText || "#fff",
      }

      return `
    <body style="background: ${color.background};">
      <table width="100%" border="0" cellspacing="20" cellpadding="0"
        style="background: ${color.mainBackground}; max-width: 600px; margin: auto; border-radius: 10px;">
        <tr>
          <td align="center"
            style="padding: 10px 0px; font-size: 22px; font-family: Helvetica, Arial, sans-serif; color: ${color.text};">
            Sign in to <strong>${escapedHost}</strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 20px 0;">
            <table border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td align="center" style="border-radius: 5px;" bgcolor="${color.buttonBackground}"><a href="${url}"
                    target="_blank"
                    style="font-size: 18px; font-family: Helvetica, Arial, sans-serif; color: ${color.buttonText}; text-decoration: none; border-radius: 5px; padding: 10px 20px; border: 1px solid ${color.buttonBorder}; display: inline-block; font-weight: bold;">Sign
                    in</a></td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td align="center"
            style="padding: 0px 0px 10px 0px; font-size: 16px; line-height: 22px; font-family: Helvetica, Arial, sans-serif; color: ${color.text};">
            If you did not request this email you can safely ignore it.
          </td>
        </tr>
      </table>
    </body>
    `
    }

    /** Email Text body (fallback for email clients that don't render HTML, e.g. feature phones) */
    function text({ url, host }: { url: string, host: string }) {
      return `Sign in to ${host}\n${url}\n\n`
    }

```

tip

React로 이메일 클라이언트 호환성이 뛰어난 HTML을 만들고 싶다면 <https://mjml.io>를 확인하세요.

## Verification Token 커스터마이징[​](https://next-auth.js.org/providers/email#customizing-the-verification-token "Direct link to heading")

기본적으로 무작위 verification token을 생성합니다. 이를 재정의하려면 provider 옵션에 `generateVerificationToken` 메서드를 정의할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    providers: [
      EmailProvider({
        async generateVerificationToken() {
          return "ABC123"
        }
      })
    ],

```

## 이메일 주소 정규화[​](https://next-auth.js.org/providers/email#normalizing-the-email-address "Direct link to heading")

기본적으로 NextAuth.js는 이메일 주소를 정규화합니다. 값은 대소문자를 구분하지 않는 것으로 처리하며(기술적으로는 [RFC 2821 spec](https://datatracker.ietf.org/doc/html/rfc2821)을 준수하지 않지만, 실제로는 데이터베이스에서 e-mail로 사용자를 조회할 때처럼 해결보다 문제가 더 많이 생깁니다), 쉼표로 구분된 목록으로 전달된 보조 이메일 주소도 제거합니다. `EmailProvider`의 `normalizeIdentifier` 메서드를 통해 자체 정규화를 적용할 수 있습니다. 다음 예시는 기본 동작을 보여줍니다:

```
    EmailProvider({
      // ...
      normalizeIdentifier(identifier: string): string {
        // Get the first two elements only,
        // separated by `@` from user input.
        let [local, domain] = identifier.toLowerCase().trim().split("@")
        // The part before "@" can contain a ","
        // but we remove it on the domain part
        domain = domain.split(",")[0]
        return `${local}@${domain}`

        // You can also throw an error, which will redirect the user
        // to the error page with error=EmailSignin in the URL
        // if (identifier.split("@").length > 2) {
        //   throw new Error("Only one email allowed")
        // }
      },
    })

```

danger

여러 개가 전달되었더라도, 항상 단일 e-mail 주소를 반환하도록 해야 합니다.

## 기존 사용자에게 Magic Link 보내기[​](https://next-auth.js.org/providers/email#sending-magic-links-to-existing-users "Direct link to heading")

기존 사용자에게만 magic login link가 전송되도록 할 수 있습니다. 사용자가 입력한 이메일을 가져와 데이터베이스의 "User" 컬렉션에 해당 이메일이 이미 존재하는지 확인해야 합니다. 존재하면 사용자에게 magic link를 전송하고, 그렇지 않으면 "/register" 같은 다른 페이지로 보낼 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import User from "../../../models/User";
    import db from "../../../utils/db";
    ...
    callbacks: {
      async signIn({ user, account, email }) {
        await db.connect();
        const userExists = await User.findOne({
          email: user.email,  //the user object has an email property, which contains the email the user entered.
        });
        if (userExists) {
          return true;   //if the email exists in the User collection, email them a magic login link
        } else {
          return "/register";
        }
      },
     ...

```
