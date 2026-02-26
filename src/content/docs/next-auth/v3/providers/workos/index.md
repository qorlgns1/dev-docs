---
title: "WorkOS"
description: "필요에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/workos

# WorkOS | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/workos#documentation "Direct link to heading")

<https://workos.com/docs/sso/guide>

## 설정[​](https://next-auth.js.org/v3/providers/workos#configuration "Direct link to heading")

<https://dashboard.workos.com>

## 옵션[​](https://next-auth.js.org/v3/providers/workos#options "Direct link to heading")

**WorkOS Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [WorkOS Provider options](https://github.com/nextauthjs/next-auth/blob/main/src/providers/workos.js)

필요에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/workos#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.WorkOS({
        clientId: process.env.WORKOS_CLIENT_ID,
        clientSecret: process.env.WORKOS_API_KEY,
      }),
    ],
    ...

```

WorkOS 자체는 ID 공급자가 아니라, 여러 single sign-on (SSO) 공급자를 연결하는 브리지입니다. 따라서 WorkOS를 사용해 사용자를 인증하려면 몇 가지 추가 변경이 필요합니다.

WorkOS를 사용해 사용자를 로그인시키려면, 어떤 WorkOS Connection을 사용할지 지정해야 합니다. 일반적인 방법은 사용자의 이메일 주소를 수집한 뒤 도메인을 추출하는 것입니다.

이는 사용자 지정 로그인 페이지를 사용해 구현할 수 있습니다.

사용자 지정 로그인 페이지를 추가하려면 `pages` 옵션을 사용할 수 있습니다:

pages/api/auth/[...nextauth].js

```
    ...
      pages: {
        signIn: '/auth/signin',
      }

```

그다음 사용자가 이메일 주소를 입력할 수 있는 입력 필드를 표시하는 사용자 지정 로그인 페이지를 추가할 수 있습니다. 이후 사용자의 이메일 주소에서 도메인을 추출해 `signIn` 함수의 `authorizationParams` 파라미터로 전달합니다:

pages/auth/signin.js

```
    import { getProviders, signIn } from "next-auth/client"

    export default function SignIn({ providers }) {
      const [email, setEmail] = useState("")

      return (
        <>
          {Object.values(providers).map((provider) => {
            if (provider.id === "workos") {
              return (
                  <input
                    type="email"
                    value={email}
                    placeholder="Email"
                    onChange={(event) => setEmail(event.target.value)}
                  />
                  <button
                    onClick={() =>
                      signIn(provider.id, undefined, {
                        domain: email.split("@")[1],
                      })
                    }
                  >
                    Sign in with SSO
                  </button>
              )
            }

            return (
                <button onClick={() => signIn(provider.id)}>
                  Sign in with {provider.name}
                </button>
            )
          })}
        </>
      )
    }

    // This is the recommended way for Next.js 9.3 or newer
    export async function getServerSideProps(context) {
      const providers = await getProviders()
      return {
        props: { providers },
      }
    }

    /*
    // If older than Next.js 9.3
    SignIn.getInitialProps = async () => {
      return {
        providers: await getProviders()
      }
    }
    */

```
