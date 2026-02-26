---
title: "Cypress로 테스트하기"
description: "NextAuth.js 구현을 테스트하려면 Cypress 사용을 권장합니다."
---

Source URL: https://next-auth.js.org/tutorials/testing-with-cypress

# Cypress로 테스트하기 | NextAuth.js

버전: v4

NextAuth.js 구현을 테스트하려면 [Cypress](https://cypress.io) 사용을 권장합니다.

## Cypress 설정하기[​](https://next-auth.js.org/tutorials/testing-with-cypress#setting-up-cypress "Direct link to heading")

시작하려면 의존성을 설치하세요:

- npm
- yarn
- pnpm

```
    npm install --save-dev cypress cypress-social-logins @testing-library/cypress
```

```
    yarn add --dev cypress cypress-social-logins @testing-library/cypress
```

```
    pnpm add --save-dev cypress cypress-social-logins @testing-library/cypress
```

note

username/password 기반 로그인을 사용 중이라면 `cypress-social-login` 의존성은 필요하지 않습니다.

Cypress는 예제 통합 테스트, 플러그인용 폴더 등과 함께 폴더 구조를 설치하고 초기화합니다.

다음으로 Cypress용 설정 파일 몇 가지를 만들어야 합니다.

먼저, 기본 cypress 설정입니다:

cypress.json

```
    {
      "baseUrl": "http://localhost:3000",
      "chromeWebSecurity": false
    }

```

이 초기 Cypress 설정은 최초 실행 시 사이트를 어디서 찾을지 Cypress에 알려주고, 페이지 도메인이 아닌 URL도 열 수 있게 해줍니다. 예를 들어 소셜 제공자로 로그인할 수 있게 됩니다.

두 번째는 환경 변수를 위한 cypress 파일입니다. 이것들도 `cypress.json`의 `env` 키 아래에 정의할 수 있지만, 여기에는 username/password를 저장하므로 별도 파일로 분리해야 합니다. 그리고 `cypress.env.json`이 아니라 `cypress.json`만 버전 관리에 커밋해야 합니다.

cypress.env.json

```
    {
      "GOOGLE_USER": "username@company.com",
      "GOOGLE_PW": "password",
      "COOKIE_NAME": "next-auth.session-token",
      "SITE_NAME": "http://localhost:3000"
    }

```

사용하려는 로그인 자격 증명으로 반드시 변경해야 하며, 다른 제공자를 사용한다면 `GOOGLE_*` 변수 이름도 다시 정의할 수 있습니다. 하지만 `COOKIE_NAME`은 NextAuth.js에서 해당 값으로 설정되어야 합니다.

세 번째로, `cypress-social-login` 플러그인을 사용한다면 `/cypress/plugins/index.js` 파일에 아래처럼 추가해야 합니다:

cypress/plugins/index.js

```
    const { GoogleSocialLogin } = require("cypress-social-logins").plugins

    module.exports = (on, config) => {
      on("task", {
        GoogleSocialLogin: GoogleSocialLogin,
      })
    }

```

마지막으로, `package.json`에 다음 npm 스크립트도 추가할 수 있습니다:

```
    "test:e2e:open": "cypress open",
    "test:e2e:run": "cypress run"

```

## 테스트 작성하기[​](https://next-auth.js.org/tutorials/testing-with-cypress#writing-a-test "Direct link to heading")

이제 모든 설정이 끝났으니, NextAuth.js를 사용해 로그인하는 테스트 작성을 시작할 수 있습니다.

기본 로그인 테스트는 다음과 같습니다:

cypress/integration/login.js

```
    describe("Login page", () => {
      before(() => {
        cy.log(`Visiting https://company.tld`)
        cy.visit("/")
      })
      it("Login with Google", () => {
        const username = Cypress.env("GOOGLE_USER")
        const password = Cypress.env("GOOGLE_PW")
        const loginUrl = Cypress.env("SITE_NAME")
        const cookieName = Cypress.env("COOKIE_NAME")
        const socialLoginOptions = {
          username,
          password,
          loginUrl,
          headless: true,
          logs: false,
          isPopup: true,
          loginSelector: `a[href="${Cypress.env(
            "SITE_NAME"
          )}/api/auth/signin/google"]`,
          postLoginSelector: ".unread-count",
        }

        return cy
          .task("GoogleSocialLogin", socialLoginOptions)
          .then(({ cookies }) => {
            cy.clearCookies()

            const cookie = cookies
              .filter((cookie) => cookie.name === cookieName)
              .pop()
            if (cookie) {
              cy.setCookie(cookie.name, cookie.value, {
                domain: cookie.domain,
                expiry: cookie.expires,
                httpOnly: cookie.httpOnly,
                path: cookie.path,
                secure: cookie.secure,
              })

              Cypress.Cookies.defaults({
                preserve: cookieName,
              })

              // remove the two lines below if you need to stay logged in
              // for your remaining tests
              cy.visit("/api/auth/signout")
              cy.get("form").submit()
            }
          })
      })
    })

```

여기서 주의할 점은, `postLoginSelector` 아래에 정의된 CSS selector를 사용자가 로그인한 뒤 페이지에서 찾을 수 있는 selector에 맞게 조정해야 한다는 것입니다. Cypress는 이를 통해 성공 여부를 판단합니다. 또한 다른 provider를 사용 중이라면 `loginSelector` URL도 조정해야 합니다.
