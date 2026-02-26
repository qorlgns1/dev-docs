---
title: 'Vercel[​](https://next-auth.js.org/deployment#vercel "Direct link to heading")'
description: "NextAuth.js를 배포하는 데는 몇 가지 단계만 필요합니다. Next.js 애플리케이션이 실행될 수 있는 곳이라면 어디서든 실행할 수 있습니다. 따라서 데이터베이스 없이 JWT 세션 전략만 사용하는 기본 구성에서는, 애플리케이션 외에 다음 몇 가지만 있으면 됩니다..."
---

Source URL: https://next-auth.js.org/deployment

Version: v4

# 배포

NextAuth.js를 배포하는 데는 몇 가지 단계만 필요합니다. Next.js 애플리케이션이 실행될 수 있는 곳이라면 어디서든 실행할 수 있습니다. 따라서 데이터베이스 없이 JWT 세션 전략만 사용하는 기본 구성에서는, 애플리케이션 외에 다음 몇 가지만 있으면 됩니다.

1. NextAuth.js 환경 변수
   - `NEXTAUTH_SECRET`
   - `NEXTAUTH_URL`

2. NextAuth.js API 라우트와 그 구성 (`/pages/api/auth/[...nextauth].js`)
   - OAuth Provider `clientId` / `clientSecret`

NextAuth.js를 사용하는 최신 JavaScript 애플리케이션 배포에서는 환경 변수가 올바르게 설정되어 있는지, NextAuth.js API 라우트의 구성이 올바르게 되어 있는지, 그리고 OAuth provider 자체의 설정(예: Callback URL 등)이 정확히 되어 있는지를 확인해야 합니다.

더 자세한 provider 설정은 아래를 참고하세요.

## Vercel[​](https://next-auth.js.org/deployment#vercel "Direct link to heading")

1. 프로젝트 설정에서 Vercel [System Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables)를 노출하도록 설정하세요.
2. 모든 환경에 대해 `NEXTAUTH_SECRET` 환경 변수를 생성하세요.
   - `openssl rand -base64 32` 또는 <https://generate-secret.vercel.app/32>를 사용해 임의 값을 생성할 수 있습니다.
   - Vercel에서는 `NEXTAUTH_URL` 환경 변수가 **필요하지 않습니다**.
3. provider의 client ID와 client secret을 환경 변수에 추가하세요. _( [OAuth Provider](https://next-auth.js.org/configuration/providers/oauth)를 사용하지 않는다면 이 단계는 건너뛰세요)_
4. 배포하세요!

예제 저장소: <https://github.com/nextauthjs/next-auth-example>

Vercel 배포에 대한 몇 가지 참고 사항이 있습니다. 환경 변수는 서버 측에서 읽히므로 `NEXT_PUBLIC_` 접두사를 붙일 필요가 없습니다. 여기서 배포할 때는 `NEXTAUTH_URL` 환경 변수를 명시적으로 설정할 필요가 없습니다. 다른 provider에서는 이 환경 변수도 **반드시** 설정해야 합니다.

### 미리보기 배포 보안 설정[​](https://next-auth.js.org/deployment#securing-a-preview-deployment "Direct link to heading")

미리보기 배포(OAuth provider 사용)를 보호할 때는 중요한 장애물이 있습니다. 대부분의 OAuth provider는 단일 redirect/callback URL 또는 최소한 정적인 전체 URL 집합만 허용합니다. 즉, 사이트를 게시하기 전에 값을 설정할 수 없고 OAuth provider의 callback URL 설정에서 와일드카드 서브도메인을 사용할 수 없습니다. 그럼에도 NextAuth.js를 사용해 Preview Deployment를 보호할 수 있는 몇 가지 방법이 있습니다.

#### Credentials Provider 사용[​](https://next-auth.js.org/deployment#using-the-credentials-provider "Direct link to heading")

`/pages/api/auth/[...nextauth].js` API 라우트/설정 파일에서 현재 Vercel preview 환경인지 확인하고, 그렇다면 username/password 방식의 간단한 "credential provider"를 활성화할 수 있습니다. Vercel은 `VERCEL_ENV` 같은 몇 가지 내장 [system environment variables](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables)를 제공합니다. 이를 확인해 preview 배포에서만 사용하는 기본 인증 전략(테스트 전용)을 적용할 수 있습니다.

여기서 유의할 점은 다음과 같습니다.

- 이 테스트 전용 사용자가 중요한 데이터에 접근할 수 없도록 하세요.
- 가능하다면 이 preview deployment를 운영 데이터베이스에 연결하지 마세요.

##### 예시[​](https://next-auth.js.org/deployment#example "Direct link to heading")

/pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import GoogleProvider from "next-auth/providers/google"
    import CredentialsProvider from "next-auth/providers/credentials"

    export default NextAuth({
      providers: [
        process.env.VERCEL_ENV === "preview"
          ? CredentialsProvider({
              name: "Credentials",
              credentials: {
                username: {
                  label: "Username",
                  type: "text",
                  placeholder: "jsmith",
                },
                password: { label: "Password", type: "password" },
              },
              async authorize() {
                return {
                  id: 1,
                  name: "J Smith",
                  email: "jsmith@example.com",
                  image: "https://i.pravatar.cc/150?u=jsmith@example.com",
                }
              },
            })
          : GoogleProvider({
              clientId: process.env.GOOGLE_ID,
              clientSecret: process.env.GOOGLE_SECRET,
            }),
      ],
    })

```

#### 브랜치 기반 preview URL 사용[​](https://next-auth.js.org/deployment#using-the-branch-based-preview-url "Direct link to heading")

Vercel의 Preview Deployment는 여러 URL로 제공되는 경우가 많습니다. 예를 들어 `master` 또는 `main`에 병합된 PR은 커밋/PR 전용 preview URL뿐 아니라 브랜치 전용 preview URL로도 접근할 수 있습니다. 이 브랜치 전용 URL은 같은 브랜치를 사용하는 한 변경되지 않습니다. 따라서 OAuth provider에 `{project}-git-main-{user}.vercel.app` preview URL을 추가할 수 있습니다. 이 URL은 해당 브랜치에서 고정되므로 인증 관련 배포를 테스트할 때 같은 preview deployment/URL을 재사용할 수 있습니다.

## Netlify[​](https://next-auth.js.org/deployment#netlify "Direct link to heading")

Netlify는 Vercel과 매우 유사해서 거의 추가 작업 없이 Next.js 프로젝트를 배포할 수 있습니다.

여기서 NextAuth.js를 올바르게 설정하려면 프로젝트 설정에 `NEXTAUTH_SECRET` 환경 변수를 추가해야 합니다. 프로젝트에서 [Essential Next.js Build Plugin](https://github.com/netlify/netlify-plugin-nextjs)을 사용 중이라면 `NEXTAUTH_URL` 환경 변수를 설정할 필요가 **없습니다**. 빌드 프로세스의 일부로 자동 설정되기 때문입니다.

Netlify도 [system environment variables](https://docs.netlify.com/configure-builds/environment-variables/)를 제공하며, 이를 통해 현재 어떤 `NODE_ENV`에 있는지 등 다양한 정보를 확인할 수 있습니다.

그다음에는 OAuth provider의 `clientId` / `clientSecret` 및 callback URL이 올바르게 설정되어 있는지만 확인하면 됩니다.
